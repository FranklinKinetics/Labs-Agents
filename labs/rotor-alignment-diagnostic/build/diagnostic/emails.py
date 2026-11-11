"""Email texts and the mail interface.

Rule: the only people we ever email are the CEO (from the order) and Brandon
(held-report alerts). Every builder below takes a Company, never a free
address, and nothing here has a way to address a leader.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .config import Config
from .models import Company

PROMPT_DIR = Path(__file__).parent / "prompts"


@dataclass
class Email:
    to: str
    subject: str
    body: str
    attachments: list = field(default_factory=list)   # (filename, bytes, mime)
    kind: str = ""


class Mailer:
    """Interface. send(Email)."""
    def send(self, email: Email) -> None:
        raise NotImplementedError


class FakeMailer(Mailer):
    def __init__(self, fail: bool = False):
        self.sent: list[Email] = []
        self.fail = fail

    def send(self, email):
        if self.fail:
            raise RuntimeError("fake mail failure")
        self.sent.append(email)


def nice_date(d) -> str:
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def first_name(full: str) -> str:
    return (full.split() or [""])[0]


def drop_link(cfg: Config, c: Company) -> str:
    return f"{cfg.app_base_url.rstrip('/')}/drop/{c.drop_token}"


def status_link(cfg: Config, c: Company) -> str:
    return f"{cfg.app_base_url.rstrip('/')}/status/{c.status_token}"


def leader_disclosure(cfg: Config, c: Company) -> str:
    """The note from 03-interviewer.md section 4. The CEO adds the interviewer
    link and their own sign-off."""
    t = (PROMPT_DIR / "leader_disclosure.md").read_text(encoding="utf-8").rstrip("\n")
    return (t.replace("[CEO first name]", first_name(c.ceo_name))
             .replace("[number]", str(c.planned_leaders))
             .replace("[platform]", c.platform)
             .replace("[date]", nice_date(c.window_closes_at)))


def interviewer_instructions(cfg: Config, c: Company) -> str:
    t = (PROMPT_DIR / "interviewer_instructions.md").read_text(encoding="utf-8")
    return (t.replace("[COMPANY]", c.company_name)
             .replace("[PLATFORM]", c.platform)
             .replace("[DROP-BOX LINK]", drop_link(cfg, c)))


def setup_kit(cfg: Config, c: Company) -> Email:
    body = f"""Hello {first_name(c.ceo_name)},

Thank you for ordering the Rotor Alignment Diagnostic for {c.company_name}. Here is what you need.

YOUR PRIVATE LINKS (please keep these to yourself and your leaders)
- Drop-box link, for your leaders to paste their summaries into:
  {drop_link(cfg, c)}
- Your status page, for you only:
  {status_link(cfg, c)}
  It shows one line, such as "2 of {c.planned_leaders} received". It never shows who has sent a summary or what it says.

HOW IT WORKS
1. Install the interviewer in your company's {c.platform} account. The interviewer instructions are attached to this email as a text file. The platform-specific install steps for {c.platform} are in the guide that goes with this kit.
2. Send your {c.planned_leaders} leaders (including yourself) the note below, with the link to the interviewer added.
3. Each leader has one conversation of about 20 minutes, checks the summary the interviewer gives them, and pastes it into the drop-box.
4. The drop-box is open until {nice_date(c.window_closes_at)}. Once at least {cfg.min_leaders} summaries are in, you can close it early from your status page, or extend it once by {cfg.extension_days} days.
5. We then write the report and email it to you. The summaries are deleted straight after.

Please don't ask your leaders to show you their summaries or their conversations. The diagnostic works because no one sees them. Franklin Kinetics never emails your leaders; everything comes through you.

If fewer than {cfg.min_leaders} leaders send a summary by the time the drop-box closes, there is no report and no refund. You can restart once, within {cfg.restart_months} months of purchase, with a fresh {cfg.window_days}-day window.

READ BEFORE YOU START
- How we handle information: {cfg.privacy_url}
- Terms: {cfg.terms_url}

NOTE FOR YOUR LEADERS (copy, add the link to the interviewer and your name)
------------------------------------------------------------
{leader_disclosure(cfg, c)}
------------------------------------------------------------

Questions? Write to {cfg.contact_email}.

{cfg.sender_name}
"""
    return Email(c.ceo_email, "Your Rotor Alignment Diagnostic: setup kit", body,
                 [("interviewer-instructions.txt", interviewer_instructions(cfg, c).encode("utf-8"), "text/plain")],
                 kind="setup_kit")


def report_delivery(cfg: Config, c: Company, pdf: bytes, n: int) -> Email:
    keep = ("You agreed at checkout that we may keep a copy of this report for our own research. "
            "You can ask us to delete it at any time." if c.consent_keep_report else
            "We have not kept a copy of the report.")
    body = f"""Hello {first_name(c.ceo_name)},

Your leadership alignment report for {c.company_name} is attached as a PDF. It is based on summaries from {n} of your leaders.

The summaries and the one-way name codes we used to catch duplicates have now been deleted. {keep}

The report shows where your leaders' views line up and where they differ. It doesn't say which view is right. That is for your team to settle.

Questions about the report or how your information was handled? Write to {cfg.contact_email}.

{cfg.sender_name}
"""
    return Email(c.ceo_email, f"Your leadership alignment report: {c.company_name}", body,
                 [("leadership-alignment-report.pdf", pdf, "application/pdf")], kind="report")


def not_enough_leaders(cfg: Config, c: Company, received: int, can_restart: bool, restart_until) -> Email:
    if can_restart:
        restart = (f"Your purchase is still valid. You can restart once, with a fresh {cfg.window_days}-day "
                   f"window, any time up to {nice_date(restart_until)}. Use the restart button on your status page:\n"
                   f"{status_link(cfg, c)}\n"
                   "Leaders who already took part can paste their saved summary again, or take the interview again.")
    else:
        restart = (f"Your one restart has already been used, or the {cfg.restart_months}-month restart period "
                   f"has ended. If you'd like to talk about options, write to {cfg.contact_email}.")
    body = f"""Hello {first_name(c.ceo_name)},

The drop-box for {c.company_name} has closed with {received} of the at least {cfg.min_leaders} summaries we need to write a report. So there is no report this time. As explained before you ordered, there is no refund in this case.

We have deleted the {received} summar{'y' if received == 1 else 'ies'} we received.

{restart}

{cfg.sender_name}
"""
    return Email(c.ceo_email, "Your Rotor Alignment Diagnostic: not enough leaders yet", body, kind="not_enough")


def held_alert(cfg: Config, c: Company, reasons: list[str]) -> Email:
    lines = "\n".join(f"- {r}" for r in reasons) or "- (no reason recorded)"
    body = f"""A report is on hold and has NOT been sent.

Company: {c.company_name} (order {c.order_id})
CEO: {c.ceo_name}

Why it was held:
{lines}

The report is held in the app. The summaries are kept until the report is delivered. Nothing has gone to the CEO. This alert does not include the report or any summary.
"""
    return Email(cfg.alert_email, f"HELD report: {c.company_name}", body, kind="held_alert")


def checkin(cfg: Config, c: Company) -> Email:
    body = f"""Hello {first_name(c.ceo_name)},

It has been two weeks since we sent your leadership alignment report for {c.company_name}. This is the one check-in email we promised.

If anything in the report was unclear or looked wrong, reply to this email and tell us. If you'd like help settling the questions it raises, you can start a conversation here: {cfg.start_conversation_link}

You don't need to do anything else.

{cfg.sender_name}
{cfg.sender_address}
{cfg.contact_email}

You are getting this because you bought the Rotor Alignment Diagnostic. To stop receiving emails from us, reply with the word "unsubscribe" or write to {cfg.contact_email}.
"""
    return Email(c.ceo_email, "Checking in on your leadership alignment report", body, kind="checkin")
