"""Changes agreed 2026-11-11 after the reconciliation with Rotor Product (M1, M2, M5),
plus the decisions on extra leaders and held reports."""
import re
from datetime import timedelta

import pytest

import aligned
from conftest import Env, LAB, LINK, canned_output, larchmere_blocks
from diagnostic import blocks as B
from diagnostic import checks, synthesis
from diagnostic.checks import DISTILLATION_SENTENCE, check_output
from diagnostic.config import Config, PLACEHOLDER_ADDRESS
from diagnostic.models import DELIVERED, HELD
from diagnostic.synthesis import FakeSynthesis

KW = dict(company=aligned.COMPANY, date="2026-11-10", n=5, link=LINK)
BETA = ("If you'd like help, settling these questions is what the Rotor Beta does. Over one quarter, we work with "
        "your leadership team to agree the main effort, the trade-offs and the warning signs, in your own words, "
        "and put them where your people make decisions.")


# ---------------------------------------------------------------- M1: section 9

def test_section_9_keeps_beta_paragraph_and_adds_distillation_sentence_and_one_link():
    for text in (synthesis.report_template(), canned_output(), aligned.aligned_output(LINK)):
        nine = checks.section(text, "## 9. Next step")
        assert BETA in " ".join(nine.split())
        assert DISTILLATION_SENTENCE in nine
        assert nine.count("http") <= 1 and nine.count("Start a conversation") == 1
        assert not re.search(r"\$\s?\d", nine)                      # no price


def test_section_9_gives_no_verdict_on_which_fits():
    nine = checks.section(synthesis.report_template(), "## 9. Next step").lower()
    for word in ("we recommend", "you should", "best fit", "right for you", "pilot"):
        assert word not in nine


def test_report_missing_the_distillation_sentence_is_checked_and_held():
    bad = canned_output().replace(DISTILLATION_SENTENCE + "\n\n", "")
    assert DISTILLATION_SENTENCE not in bad
    o = check_output(bad, **{**KW, "company": "Larchmere Fabrication"})
    assert not o.passed
    assert any("Distillation" in p for p in o.problems)
    # and through the app: the report is held, nothing goes to the CEO
    e = Env(synth=FakeSynthesis(bad))
    c = e.company(); e.fill(c, 5)
    e.app.close_early(c.status_token)
    assert c.state == HELD and not e.emails_to("report") and len(e.emails_to("held_alert")) == 1
    assert any("Distillation" in r for r in c.held_reasons)


def test_report_with_only_the_distillation_sentence_reworded_is_held():
    bad = canned_output().replace("takes your strategy into your AI tools", "fixes your AI strategy")
    assert not check_output(bad, **{**KW, "company": "Larchmere Fabrication"}).passed


def test_prompt_copies_carry_the_new_section_9_and_the_up_to_counts():
    s = synthesis.build_system_prompt("X", "2026-11-10", 3, LINK)
    assert DISTILLATION_SENTENCE in s
    for old in ("2–5 splits", "2–5 trade-offs", "2–4 effects", "3–7 questions", "3–6 ", "5–10 images", "Write 2 to 4"):
        assert old not in s, old
    for new in ("Up to 5 splits", "Up to 5 trade-offs", "Up to 4 effects", "Up to 7 questions", "Your views don't split here"):
        assert new in s, new
    assert "Never stretch a small difference to fill a section" in s


def test_lab_documents_carry_the_amendment_note_and_sentence():
    note = "Amended 2026-11-11 after the reconciliation with Rotor Product."
    for name in ("04-synthesis-agent.md", "05-sample-report.md"):
        t = (LAB / name).read_text(encoding="utf-8")
        assert note in t and DISTILLATION_SENTENCE in t, name


# ---------------------------------------------------------------- M2: an aligned team

def test_aligned_fixture_is_marked_fictional_and_in_exact_block_format():
    assert len(aligned.BLOCKS) == 5
    for b in aligned.BLOCKS:
        assert "(FICTIONAL)" in b.splitlines()[1]
        B.prepare_block(b, bytes(16))                              # raises if the format is wrong


def test_aligned_report_passes_every_check():
    o = check_output(aligned.aligned_output(LINK), **KW)
    assert o.passed, o.problems
    assert "Your views don't split here." in o.report
    assert checks.section(o.report, "## 9. Next step").strip()


def test_aligned_report_fills_every_section_even_when_empty():
    report = check_output(aligned.aligned_output(LINK), **KW).report
    for h in [h for h in checks.headings(synthesis.report_template()) if h.startswith("## ")]:
        assert checks.section(report, h).strip(), h


def test_aligned_report_is_delivered_not_held():
    e = Env(synth=FakeSynthesis(aligned.aligned_output(LINK)))
    c = e.company(company_name=aligned.COMPANY)
    for b in aligned.BLOCKS:
        assert e.submit(c, b).ok
    assert e.app.close_early(c.status_token).ok
    assert c.state == DELIVERED, c.held_reasons
    (m,) = e.emails_to("report")
    assert m.to == c.ceo_email
    assert not e.emails_to("held_alert")
    assert e.store.summaries(c.id) == []                           # deleted on delivery as usual


def test_aligned_report_is_not_stretched_into_a_split_by_the_checks():
    # a short report is a warning only (the plan: length is not a hold reason)
    o = check_output(aligned.aligned_output(LINK), **KW)
    assert o.passed and any("words" in w for w in o.warnings)


# ---------------------------------------------------------------- M5: link and address

def test_start_a_conversation_link_and_address_are_set():
    c = Config()
    assert c.start_conversation_link == "https://www.franklinkinetics.com/contact"
    assert c.sender_name == "Franklin Kinetics Consulting Corporation"
    assert c.sender_address == "1400-2500 Victoria Ave, Regina SK S4P 3X2"
    assert not any("sender_address" in p or "start_conversation" in p for p in c.problems())
    assert c.sender_address != PLACEHOLDER_ADDRESS


def test_checkin_email_carries_the_mailing_address():
    e = Env(); c = e.company(); e.fill(c, 3)
    e.app.close_early(c.status_token)
    e.clock.advance(days=14); e.app.process_due()
    (m,) = e.emails_to("checkin")
    assert "Franklin Kinetics Consulting Corporation" in m.body
    assert "1400-2500 Victoria Ave, Regina SK S4P 3X2" in m.body
    assert "https://www.franklinkinetics.com/contact" in m.body


# ---------------------------------------------------------------- extra leaders

@pytest.mark.parametrize("planned,got,text", [
    (6, 0, "0 of 6 received"), (6, 4, "4 of 6 received"), (5, 5, "5 of 5 received"),
    (5, 6, "6 received (5 planned)"), (3, 5, "5 received (3 planned)"),
])
def test_status_text_for_planned_and_extra_leaders(planned, got, text):
    e = Env(); c = e.company(planned_leaders=planned)
    pool = larchmere_blocks() + aligned.BLOCKS
    for b in pool[:got]:
        assert e.submit(c, b).ok
    assert e.app.status_text(c.status_token) == text


def test_drop_box_accepts_up_to_8_whatever_was_planned_and_refuses_the_ninth():
    e = Env(); c = e.company(planned_leaders=3)
    pool = larchmere_blocks() + [aligned.BLOCKS[0], aligned.BLOCKS[1], aligned.BLOCKS[2]]
    for b in pool:
        assert e.submit(c, b).ok
    assert e.app.status_text(c.status_token) == "8 received (3 planned)"
    extra = aligned.BLOCKS[3]
    r = e.submit(c, extra)
    assert not r.ok and "maximum of 8" in r.message
    assert len(e.store.summaries(c.id)) == 8


# ---------------------------------------------------------------- held reports wait

def test_held_summaries_wait_with_no_time_limit_until_brandon_acts():
    e = Env(synth=FakeSynthesis(canned_output().replace("Rush jobs hurt.", "A pilot of rush jobs.")))
    c = e.company(); e.fill(c, 5)
    e.app.close_early(c.status_token)
    assert c.state == HELD
    for _ in range(14):                                            # more than a year
        e.clock.advance(days=30); e.app.process_due()
    assert c.state == HELD
    assert len(e.store.summaries(c.id)) == 5                       # still there, nothing deleted
    assert not e.emails_to("report")
    assert e.app.release_held(c.id, canned_output()).ok and c.state == DELIVERED
    assert e.store.summaries(c.id) == []
