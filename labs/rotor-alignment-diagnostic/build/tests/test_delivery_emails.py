"""Delivery, deletion, held reports, emails, check-in (Check D, deletion, hold rules)."""
from datetime import timedelta

import pytest

from conftest import Env, adaptive_output, canned_output, larchmere_blocks, order
from diagnostic import checks
from diagnostic.models import DELIVERED, DELIVERY_FAILED, HELD
from diagnostic.synthesis import FakeSynthesis


def delivered(consent=False, **env_kw):
    e = Env(**env_kw)
    c = e.company(consent_keep_report=consent)
    e.fill(c, 5)
    assert e.app.close_early(c.status_token).ok
    return e, c


# ---------------------------------------------------------------- delivery and deletion

def test_pass_emails_pdf_to_ceo_only():
    e, c = delivered()
    assert c.state == DELIVERED
    (m,) = e.emails_to("report")
    assert m.to == c.ceo_email
    name, data, mime = m.attachments[0]
    assert mime == "application/pdf" and data.startswith(b"%PDF") and len(data) > 2000


def test_after_delivery_no_summaries_or_fingerprints_remain():
    e, c = delivered()
    assert e.store.summaries(c.id) == []
    assert e.store._summaries == {}
    assert not e.store.has_fingerprint(c.id, "anything")
    assert e.store.deletion_log() == [{"date": "2026-11-10", "count": 5}]     # date and count only


def test_report_deleted_without_consent():
    e, c = delivered(consent=False)
    assert e.store.get_report(c.id) is None and e.store._reports == {}
    assert "have not kept a copy" in e.emails_to("report")[0].body


def test_report_kept_with_consent():
    e, c = delivered(consent=True)
    assert e.store.get_report(c.id).startswith("# Leadership alignment report")
    assert "=== CHECKS ===" not in e.store.get_report(c.id)
    assert "agreed at checkout" in e.emails_to("report")[0].body


def test_nothing_deleted_if_the_email_cannot_be_sent():
    e = Env(); c = e.company(); e.fill(c, 3)
    e.mailer.fail = True
    e.app.close_early(c.status_token)
    assert c.state == DELIVERY_FAILED
    assert len(e.store.summaries(c.id)) == 3 and e.store.deletion_log() == []
    e.mailer.fail = False
    assert e.app.release_held(c.id).ok and c.state == DELIVERED
    assert e.store.summaries(c.id) == [] and e.store.deletion_log()[-1]["count"] == 3


# ---------------------------------------------------------------- held reports

def held_env(output, **kw):
    e = Env(synth=FakeSynthesis(output), **kw)
    c = e.company(); e.fill(c, 5); e.app.close_early(c.status_token)
    return e, c


def assert_held(e, c, needle):
    assert c.state == HELD
    assert not e.emails_to("report")
    (alert,) = e.emails_to("held_alert")
    assert alert.to == e.cfg.alert_email
    assert any(needle in r for r in c.held_reasons)
    assert needle in alert.body
    assert len(e.store.summaries(c.id)) == 5                    # kept until delivery
    assert e.store.deletion_log() == []
    assert "Leader" not in alert.body and "ROTOR" not in alert.body     # no block content in the alert


def test_held_when_check_sheet_wrong():
    e, c = held_env(canned_output().replace("Any banned word: no", "Any banned word: yes"))
    assert_held(e, c, "Any banned word")


def test_held_when_banned_word():
    e, c = held_env(canned_output().replace("Rush jobs hurt.", "A pilot of rush jobs."))
    assert_held(e, c, "banned word")


def test_held_when_insufficient_even_with_enough_blocks():
    e, c = held_env("INSUFFICIENT: 2 valid blocks")
    assert_held(e, c, "INSUFFICIENT")


def test_held_when_second_check_flags():
    e, c = held_env(canned_output(), planted=["Priya"])      # not in the report: passes
    assert c.state == DELIVERED
    e2, c2 = held_env(canned_output().replace("Rush jobs hurt.", "Rush jobs hurt (Priya)."), planted=["Priya"])
    assert_held(e2, c2, "Priya")


def test_second_check_sees_only_the_report():
    e, c = delivered()
    (seen,) = e.idcheck.seen
    assert seen.startswith("# Leadership alignment report")
    assert "=== CHECKS ===" not in seen and "ROTOR INTERVIEW SUMMARY" not in seen


def test_held_when_refusal():
    e = Env(synth=FakeSynthesis("", stop_reason="refusal")); c = e.company(); e.fill(c, 3); e.app.close_early(c.status_token)
    assert c.state == HELD and "refusal" in c.held_reasons[0]
    assert not e.emails_to("report") and len(e.emails_to("held_alert")) == 1


def test_held_when_truncated():
    e = Env(synth=FakeSynthesis(canned_output(), stop_reason="max_tokens")); c = e.company(); e.fill(c, 3)
    e.app.close_early(c.status_token)
    assert c.state == HELD and not e.emails_to("report")


def test_held_when_agent_call_errors():
    class Boom:
        def synthesize(self, s, u): raise TimeoutError("x")
    e = Env(synth=Boom()); c = e.company(); e.fill(c, 3); e.app.close_early(c.status_token)
    assert c.state == HELD and "TimeoutError" in c.held_reasons[0]


def test_held_when_second_check_errors():
    e = Env()
    def boom(report): raise RuntimeError("down")
    e.idcheck.check = boom
    c = e.company(); e.fill(c, 3); e.app.close_early(c.status_token)
    assert c.state == HELD and not e.emails_to("report")


def test_brandon_can_release_a_held_report_and_it_then_delivers_and_deletes():
    e, c = held_env(canned_output().replace("Rush jobs hurt.", "A pilot of rush jobs."))
    fixed = e.store.get_report(c.id).replace("A pilot of rush jobs.", "Rush jobs hurt.")
    assert e.app.release_held(c.id, fixed).ok
    assert c.state == DELIVERED and len(e.emails_to("report")) == 1 and e.store.summaries(c.id) == []


def test_retry_held_runs_agent_again():
    e, c = held_env(canned_output().replace("Rush jobs hurt.", "A pilot of rush jobs."))
    e.synth.output = adaptive_output()
    assert e.app.retry_held(c.id).ok and c.state == DELIVERED


# ---------------------------------------------------------------- Check D: emails

def test_checkD_setup_kit_goes_to_ceo_with_the_right_links():
    from conftest import REPO
    from diagnostic.orders import FakeOrders
    e = Env()
    made = e.app.poll_orders(FakeOrders([order()]))
    c = made[0]
    (m,) = e.emails_to("setup_kit")
    assert m.to == c.ceo_email
    b = m.body
    assert e.cfg.privacy_url in b and e.cfg.terms_url in b
    assert f"/drop/{c.drop_token}" in b and f"/status/{c.status_token}" in b
    assert "No person reads your conversation" in b                        # the disclosure note
    assert "Your name and role are removed on arrival" in b
    assert "Dale" in b                                                      # CEO's first name filled in
    assert "[CEO first name]" not in b and "[platform]" not in b and "[number]" not in b and "[date]" not in b
    assert "no refund" in b
    attach = m.attachments[0][1].decode()
    assert "Larchmere Fabrication" in attach and f"/drop/{c.drop_token}" in attach and "[COMPANY]" not in attach
    assert "[PLATFORM]" not in attach and "[DROP-BOX LINK]" not in attach


def test_checkD_checkin_exactly_once_14_days_after_report_to_ceo_only():
    e, c = delivered()
    assert len(e.store.scheduled_emails()) == 1
    e.clock.advance(days=13); e.app.process_due()
    assert not e.emails_to("checkin")
    e.clock.advance(days=1); e.app.process_due()
    (m,) = e.emails_to("checkin")
    assert m.to == c.ceo_email
    assert "unsubscribe" in m.body.lower()
    assert e.cfg.sender_name in m.body and e.cfg.sender_address in m.body
    for _ in range(3):
        e.clock.advance(days=30); e.app.process_due()
    assert len(e.emails_to("checkin")) == 1


def test_checkin_skipped_after_unsubscribe():
    e, c = delivered()
    e.store.unsubscribe(c.ceo_email.upper())
    e.clock.advance(days=15); e.app.process_due()
    assert not e.emails_to("checkin")


def test_checkin_not_scheduled_when_no_report():
    e = Env(); c = e.company(); e.clock.advance(days=22); e.app.process_due()
    assert e.store.scheduled_emails() == []


def test_checkD_no_email_ever_goes_to_a_leader():
    from diagnostic.orders import FakeOrders
    e = Env()
    e.app.poll_orders(FakeOrders([order()]))
    c = e.store.list_companies()[0]
    e.fill(c, 5)
    e.app.close_early(c.status_token)
    e.clock.advance(days=15); e.app.process_due()
    # a second company that fails
    d = e.company(order_id="SQ-2", ceo_email="other@x.example"); e.clock.advance(days=22); e.app.process_due()
    allowed = {c.ceo_email, d.ceo_email, e.cfg.alert_email}
    assert {m.to for m in e.mailer.sent} <= allowed
    assert sorted(m.kind for m in e.mailer.sent) == ["checkin", "not_enough", "report", "setup_kit"]
    # no email text addresses leaders as the recipient or names any
    for m in e.mailer.sent:
        assert "Priya" not in m.body and "Marc" not in m.body


def test_all_emails_avoid_banned_words_and_promises():
    e, c = delivered()
    e.clock.advance(days=15); e.app.process_due()
    d = e.company(order_id="SQ-9"); e.clock.advance(days=22); e.app.process_due()
    for m in e.mailer.sent:
        assert not checks.BANNED.search(m.subject + m.body), m.kind
        low = m.body.lower()
        assert "guarantee" not in low and "will save" not in low and "will increase" not in low
        for mil in ("army", "military", "forces", "squadron", "dnd"):
            assert mil not in low


def test_not_enough_email_mentions_restart_deadline_and_no_refund():
    e = Env(); c = e.company(); e.fill(c, 1)
    e.clock.advance(days=22); e.app.process_due()
    (m,) = e.emails_to("not_enough")
    assert "November 10, 2027" in m.body
    assert f"/status/{c.status_token}" in m.body
    assert "1 of the at least 3" in m.body and "1 summary" in m.body


def test_checkin_placeholder_address_is_flagged_by_config():
    from diagnostic.config import Config
    assert any("sender_address" in p for p in Config().problems())
    assert not [p for p in Config(sender_address="1 Example St", app_base_url="https://x.example").problems()]


# ---------------------------------------------------------------- pdf

def test_pdf_is_valid_and_readable_size():
    from diagnostic.pdf import make_pdf
    pdf = make_pdf(checks.check_output(canned_output(), company="Larchmere Fabrication", date="2026-11-10",
                                       n=5, link="https://x.example").report)
    assert pdf.startswith(b"%PDF") and pdf.rstrip().endswith(b"%%EOF") and len(pdf) > 5000
