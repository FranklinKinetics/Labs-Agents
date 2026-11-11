"""The app's logic: companies, windows, drop-box, report pipeline, delivery.

Every external thing (storage, mail, AI, orders, clock) is passed in, so the
bench runs with in-memory fakes and no network.
"""
from __future__ import annotations

import calendar
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional

from . import blocks, checks, emails, synthesis
from .config import Config
from .models import (DELIVERED, DELIVERY_FAILED, HELD, NOT_ENOUGH, OPEN, Company,
                     OrderInput, Result, ScheduledEmail)
from .pdf import make_pdf
from .store import Store

QUEBEC = {"qc", "quebec", "québec", "que", "que."}


class OrderRejected(Exception):
    pass


def add_months(d: datetime, months: int) -> datetime:
    y, m = divmod(d.month - 1 + months, 12)
    year, month = d.year + y, m + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return d.replace(year=year, month=month, day=day)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class App:
    def __init__(self, store: Store, mailer: emails.Mailer,
                 synth: synthesis.SynthesisAdapter,
                 id_check: synthesis.IdentifierCheckAdapter,
                 config: Config | None = None,
                 clock: Callable[[], datetime] = utcnow,
                 pdf_maker: Callable[[str], bytes] = make_pdf):
        self.store, self.mailer, self.synth, self.id_check = store, mailer, synth, id_check
        self.cfg = config or Config()
        self.clock = clock
        self.pdf_maker = pdf_maker

    # ------------------------------------------------------------ companies

    def create_company_from_order(self, o: OrderInput) -> Optional[Company]:
        """Make a company from an order. Returns None if this order was already
        handled (idempotent on order id). Raises OrderRejected if it can't proceed."""
        if self.store.find_by_order(o.order_id) is not None or o.order_id in self.store.rejected_orders():
            return None
        problem = self._order_problem(o)
        if problem:
            self.store.reject_order(o.order_id, problem)
            raise OrderRejected(problem)
        now = self.clock()
        c = Company(
            id=uuid.uuid4().hex, order_id=o.order_id, ceo_name=o.ceo_name.strip(),
            ceo_email=o.ceo_email.strip(), company_name=o.company_name.strip(),
            province=o.province.strip(), platform=o.platform.strip(),
            planned_leaders=o.planned_leaders, consent_keep_report=bool(o.consent_keep_report),
            drop_token=secrets.token_urlsafe(32), status_token=secrets.token_urlsafe(32),
            salt=secrets.token_hex(32), purchased_at=now,
            window_closes_at=now + timedelta(days=self.cfg.window_days),
        )
        self.store.add_company(c)
        return c

    def _order_problem(self, o: OrderInput) -> str:
        if o.province.strip().casefold() in QUEBEC:
            return "Head office in Quebec: not offered (refund the order)"
        if not (self.cfg.min_leaders <= int(o.planned_leaders) <= self.cfg.max_leaders):
            return f"planned leaders must be {self.cfg.min_leaders} to {self.cfg.max_leaders}"
        if "@" not in o.ceo_email or not o.ceo_name.strip() or not o.company_name.strip():
            return "order is missing the CEO name or email, or the company name"
        return ""

    def poll_orders(self, source) -> list[Company]:
        """Turn new diagnostic orders into companies and send each setup kit once."""
        made = []
        for o in source.fetch_new_orders():
            try:
                c = self.create_company_from_order(o)
            except OrderRejected as e:
                self._alert_text(f"ORDER NOT PROCESSED: {o.order_id}", str(e))
                continue
            if c is None:
                continue
            self.mailer.send(emails.setup_kit(self.cfg, c))
            made.append(c)
        return made

    def _alert_text(self, subject: str, body: str):
        self.mailer.send(emails.Email(self.cfg.alert_email, subject, body, kind="order_alert"))

    # ------------------------------------------------------------ drop-box

    def submit_summary(self, drop_token: str, text: str, consent_ack: bool) -> Result:
        c = self.store.find_by_drop_token(drop_token)
        if c is None:
            return Result(False, "This link isn't valid. Please check the link your CEO sent you.")
        if c.state != OPEN or self.clock() >= c.window_closes_at:
            return Result(False, "This drop-box is closed. Please ask your CEO.")
        if not consent_ack:
            return Result(False, "Please tick the box to confirm you understand that unattributed quotes may appear in the report.")
        count = len(self.store.summaries(c.id))
        if count >= self.cfg.max_leaders:
            return Result(False, f"This drop-box already holds the maximum of {self.cfg.max_leaders} summaries.")
        try:
            prepared = blocks.prepare_block(text, bytes.fromhex(c.salt))
        except blocks.BlockRejected as e:
            return Result(False, str(e))          # nothing stored
        if self.store.has_fingerprint(c.id, prepared.fingerprint):
            return Result(False, "A summary from this leader has already been received. Only one per leader is needed.")
        self.store.add_summary(c.id, prepared.stripped_text, prepared.fingerprint)
        return Result(True, "Received.")

    def status_text(self, status_token: str) -> Optional[str]:
        """The whole status page: a count against the plan, nothing else."""
        c = self.store.find_by_status_token(status_token)
        if c is None:
            return None
        got = len(self.store.summaries(c.id))
        if got > c.planned_leaders:       # extra leaders are welcome, up to max_leaders (decision 2026-11-11)
            return f"{got} received ({c.planned_leaders} planned)"
        return f"{got} of {c.planned_leaders} received"

    # ------------------------------------------------------------ window

    def _ceo_company(self, status_token: str) -> Optional[Company]:
        return self.store.find_by_status_token(status_token)

    def close_early(self, status_token: str) -> Result:
        c = self._ceo_company(status_token)
        if c is None or c.state != OPEN:
            return Result(False, "The drop-box is not open.")
        n = len(self.store.summaries(c.id))
        if n < self.cfg.min_leaders:
            return Result(False, f"You can close early once at least {self.cfg.min_leaders} summaries are in.")
        self._close(c)
        return Result(True, "Closed. Your report is being prepared.")

    def extend(self, status_token: str) -> Result:
        c = self._ceo_company(status_token)
        if c is None or c.state != OPEN:
            return Result(False, "The drop-box is not open.")
        if c.extended:
            return Result(False, "The window has already been extended once.")
        c.window_closes_at += timedelta(days=self.cfg.extension_days)
        c.extended = True
        self.store.save_company(c)
        return Result(True, f"Extended by {self.cfg.extension_days} days.")

    def restart_allowed_until(self, c: Company) -> datetime:
        return add_months(c.purchased_at, self.cfg.restart_months)

    def restart(self, status_token: str) -> Result:
        c = self._ceo_company(status_token)
        if c is None or c.state != NOT_ENOUGH:
            return Result(False, "A restart is only available after a window closes with too few summaries.")
        if c.restarts_used >= 1:
            return Result(False, "The one restart has already been used.")
        now = self.clock()
        if now > self.restart_allowed_until(c):
            return Result(False, f"The {self.cfg.restart_months}-month restart period has ended.")
        c.restarts_used += 1
        c.state = OPEN
        c.extended = False
        c.window_closes_at = now + timedelta(days=self.cfg.window_days)
        # a fresh salt: the old fingerprints are already gone
        c.salt = secrets.token_hex(32)
        self.store.save_company(c)
        return Result(True, f"Restarted. The drop-box is open for {self.cfg.window_days} days.")

    # ------------------------------------------------------------ scheduled work

    def process_due(self) -> None:
        """Run by the scheduler. Closes expired windows and sends due check-ins."""
        now = self.clock()
        for c in self.store.list_companies():
            if c.state == OPEN and now >= c.window_closes_at:
                self._close(c)
        for e in self.store.due_emails(now):
            c = self.store.get_company(e.company_id)
            e.sent = True                      # mark first: never send twice
            if c is None or self.store.is_unsubscribed(c.ceo_email):
                continue
            if e.kind == "checkin":
                self.mailer.send(emails.checkin(self.cfg, c))

    # ------------------------------------------------------------ closing

    def _close(self, c: Company) -> None:
        blocks_ = self.store.summaries(c.id)
        if len(blocks_) < self.cfg.min_leaders:
            self._not_enough(c, len(blocks_))
            return
        self._run_pipeline(c)

    def _log_deletion(self, count: int):
        self.store.log_deletion(self.clock().date().isoformat(), count)

    def _not_enough(self, c: Company, received: int) -> None:
        deleted = self.store.delete_summaries(c.id)       # summaries and fingerprints
        self._log_deletion(deleted)
        c.state = NOT_ENOUGH
        self.store.save_company(c)
        can_restart = c.restarts_used < 1 and self.clock() <= self.restart_allowed_until(c)
        self.mailer.send(emails.not_enough_leaders(
            self.cfg, c, received, can_restart, self.restart_allowed_until(c)))

    def synthesize_and_check(self, c: Company, summaries: list[str]) -> checks.CheckOutcome:
        """Run the agent on the given blocks and check what comes back. Used by
        the pipeline; also callable directly (it does not look at the count)."""
        n = len(summaries)
        date = self.clock().date().isoformat()
        link = self.cfg.start_conversation_link
        system = synthesis.build_system_prompt(c.company_name, date, n, link)
        user = synthesis.build_user_message(summaries)
        try:
            result = self.synth.synthesize(system, user)
        except Exception as e:                      # network, quota, anything
            return checks.CheckOutcome(False, "", [f"synthesis call failed: {type(e).__name__}"])
        if result.stop_reason != "end_turn":
            return checks.CheckOutcome(False, "", [f"agent did not finish normally (stop reason: {result.stop_reason})"])
        outcome = checks.check_output(result.text, company=c.company_name, date=date, n=n, link=link)
        if outcome.report:
            try:
                flags = self.id_check.check(outcome.report)
            except Exception as e:
                flags = [f"second check failed to run: {type(e).__name__}"]
            if flags:
                outcome.problems.extend(flags)
                outcome.passed = False
        return outcome

    def _run_pipeline(self, c: Company) -> None:
        summaries = self.store.summaries(c.id)
        outcome = self.synthesize_and_check(c, summaries)
        if not outcome.passed:
            self._hold(c, outcome)
            return
        self._deliver(c, outcome.report, len(summaries))

    def _hold(self, c: Company, outcome: checks.CheckOutcome) -> None:
        c.state = HELD
        c.held_reasons = list(outcome.problems)
        self.store.save_company(c)
        if outcome.report:
            self.store.save_report(c.id, outcome.report)    # held for Brandon; summaries stay until delivery
        self.mailer.send(emails.held_alert(self.cfg, c, outcome.problems))

    def release_held(self, company_id: str, report_text: str | None = None) -> Result:
        """Brandon's decision to release a held report (optionally after fixing the text)."""
        c = self.store.get_company(company_id)
        if c is None or c.state not in (HELD, DELIVERY_FAILED):
            return Result(False, "No held report for that company.")
        text = report_text or self.store.get_report(c.id)
        if not text:
            return Result(False, "No report text to release.")
        self._deliver(c, text, len(self.store.summaries(c.id)))
        return Result(c.state == DELIVERED, c.state)

    def retry_held(self, company_id: str) -> Result:
        c = self.store.get_company(company_id)
        if c is None or c.state not in (HELD, DELIVERY_FAILED):
            return Result(False, "No held report for that company.")
        self.store.delete_report(c.id)
        self._run_pipeline(c)
        return Result(True, c.state)

    def _deliver(self, c: Company, report: str, n: int) -> None:
        try:
            pdf = self.pdf_maker(report)
            self.mailer.send(emails.report_delivery(self.cfg, c, pdf, n))
        except Exception as e:
            c.state = DELIVERY_FAILED
            c.held_reasons = [f"delivery failed: {type(e).__name__}"]
            self.store.save_company(c)
            self.store.save_report(c.id, report)
            try:
                self.mailer.send(emails.held_alert(self.cfg, c, c.held_reasons))
            except Exception:
                pass                                   # mail is down; the state is saved for the scheduler to surface
            return
        # only after the report has gone: delete
        count = self.store.delete_summaries(c.id)          # summaries and fingerprints
        self._log_deletion(count)                           # date and count only
        if c.consent_keep_report:
            self.store.save_report(c.id, report)
        else:
            self.store.delete_report(c.id)
        now = self.clock()
        c.state = DELIVERED
        c.delivered_at = now
        c.held_reasons = []
        self.store.save_company(c)
        self.store.schedule_email(ScheduledEmail(
            c.id, "checkin", now + timedelta(days=self.cfg.checkin_days)))
