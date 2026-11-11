"""Prompt assembly and automatic checks on the agent's output (Check C, Check D, hold rules)."""
import re

import pytest

from conftest import LAB, LINK, canned_output, larchmere_blocks
from diagnostic import checks, synthesis
from diagnostic.checks import check_output

KW = dict(company="Larchmere Fabrication", date="2026-11-10", n=5, link=LINK)


# ---------------------------------------------------------------- prompt assembly

def _box(path, start, end):
    t = (LAB / path).read_text(encoding="utf-8")
    t = t[t.index(start):t.index(end)]
    return re.search(r"```markdown\n(.*?)\n```", t, re.S).group(1)


def test_copied_prompts_still_match_the_approved_files():
    """If 04-synthesis-agent.md or 03-interviewer.md change, the copies here must change too."""
    assert synthesis.instructions_box() == _box("04-synthesis-agent.md", "## 3. The instructions", "## 4. Report template")
    assert synthesis.report_template() == _box("04-synthesis-agent.md", "## 4. Report template", "## 5. Vera's check")
    from diagnostic.emails import PROMPT_DIR
    assert (PROMPT_DIR / "interviewer_instructions.md").read_text().rstrip("\n") == _box(
        "03-interviewer.md", "## 3. The instructions", "## 4. Disclosure")


def test_system_prompt_has_template_inserted_and_all_values_filled():
    s = synthesis.build_system_prompt("Larchmere Fabrication", "2026-11-10", 5, LINK)
    assert "[REPORT TEMPLATE goes here" not in s
    assert "# Leadership alignment report · Larchmere Fabrication" in s
    assert "2026-11-10 · Based on interviews with 5 leaders" in s
    assert f"Start a conversation: {LINK}" in s
    assert "from 5 interview summaries" in s
    for token in ("{company}", "{date}", "{n}", "{start_conversation_link}"):
        assert token not in s
    assert s.index("## 9. Next step") < s.index("=== CHECKS ===")      # template sits before the check sheet
    assert "section 7" not in s.lower()


def test_section_seven_amendment_is_in_the_prompt():
    s = synthesis.build_system_prompt("X", "2026-11-10", 3, LINK)
    assert "# What these differences may lead to" in s
    assert 'Write "all" only when every block supports it' in s
    assert "You may say how many different main efforts there are" in s
    assert "Every effect in section 4 joins a split to something leaders named" in s
    assert "Every \"all\" claim supported by every block" in s


def test_values_with_braces_or_newlines_are_not_refilled():
    s = synthesis.build_system_prompt("Odd {n} Co\nLtd", "2026-11-10", 4, LINK)
    assert "Odd {n} Co Ltd" in s


def test_user_message_holds_only_the_stripped_blocks():
    msg = synthesis.build_user_message(larchmere_blocks()[:3])
    assert msg.count("=== ROTOR INTERVIEW SUMMARY ===") == 3


# ---------------------------------------------------------------- passing output

def test_canned_larchmere_output_passes_every_check():
    o = check_output(canned_output(), **KW)
    assert o.passed, o.problems
    assert o.report.startswith("# Leadership alignment report")
    assert "=== CHECKS ===" not in o.report


def test_checkC_report_length_is_in_range():
    words = len(check_output(canned_output(), **KW).report.split())
    assert 1200 <= words <= 2000, words


def test_checkD_section_9_matches_approved_wording():
    out = canned_output()
    assert check_output(out, **KW).passed
    tampered = out.replace("settling these questions is what the Rotor Beta does", "we will fix this for you")
    o = check_output(tampered, **KW)
    assert not o.passed and any("section 9" in p for p in o.problems)


def test_checkD_start_conversation_link_present_in_section_9():
    assert f"Start a conversation: {LINK}" in canned_output()
    bad = canned_output().replace(LINK, "[link]")
    assert not check_output(bad, **KW).passed


def test_checkD_no_price_in_report():
    assert not re.search(r"\$\s?\d", check_output(canned_output(), **KW).report)


# ---------------------------------------------------------------- hold rules

def test_insufficient_output_is_held():
    o = check_output("INSUFFICIENT: 2 valid blocks", **KW)
    assert not o.passed and "INSUFFICIENT" in o.problems[0]


def test_insufficient_must_be_exact_to_count_as_such():
    # extra text around it is not the exact output; it fails on structure instead
    o = check_output("INSUFFICIENT: 2 valid blocks\nSorry!", **KW)
    assert not o.passed


@pytest.mark.parametrize("heading", [
    "## How to read this report", "## 1. Where the team agrees", "### What you each said the main effort is",
    "### Other places your views split", "## 3. Trade-offs that aren't settled",
    "## 4. What these differences may lead to", "## 5. What the plan rests on, and what would warn you",
    "## 6. Where work waits", "## 7. Your team's own words", "## 8. Questions your team needs to settle",
    "## 9. Next step",
])
def test_missing_required_heading_holds(heading):
    o = check_output(canned_output().replace(heading + "\n", ""), **KW)
    assert not o.passed and any("missing heading" in p for p in o.problems)


def test_out_of_order_headings_hold():
    t = canned_output()
    a, b = "## 6. Where work waits", "## 7. Your team's own words"
    t = t.replace(a, "@@A").replace(b, a).replace("@@A", b)
    o = check_output(t, **KW)
    assert not o.passed and any("out of order" in p for p in o.problems)


def test_extra_heading_holds():
    o = check_output(canned_output().replace("## 9. Next step", "## 9a. Bonus\n\n## 9. Next step"), **KW)
    assert not o.passed


def test_missing_check_sheet_holds():
    t = canned_output()
    o = check_output(t[:t.index("=== CHECKS ===")], **KW)
    assert not o.passed and any("check sheet" in p for p in o.problems)


def test_unclosed_check_sheet_holds():
    o = check_output(canned_output().replace("=== END CHECKS ===", ""), **KW)
    assert not o.passed


@pytest.mark.parametrize("line,wrong", [
    ("Every section filled: yes", "Every section filled: no"),
    ("Any name, role or identifying detail left: no", "Any name, role or identifying detail left: yes"),
    ("Any quote attributed or counted to one person: no", "Any quote attributed or counted to one person: yes"),
    ("Any recommendation of a main effort or advice: no", "Any recommendation of a main effort or advice: yes"),
    ("Any result, savings or ROI claim: no", "Any result, savings or ROI claim: yes"),
    ("Any banned word: no", "Any banned word: yes"),
    ('Every "all" claim supported by every block: yes', 'Every "all" claim supported by every block: no'),
    ("Every effect in section 4 joins a split to something leaders named: yes",
     "Every effect in section 4 joins a split to something leaders named: no"),
    ("Valid blocks used: 5", "Valid blocks used: 4"),
])
def test_wrong_check_sheet_answer_holds(line, wrong):
    t = canned_output()
    assert line in t
    o = check_output(t.replace(line, wrong), **KW)
    assert not o.passed


def test_missing_check_line_holds():
    t = canned_output().replace("Any banned word: no\n", "")
    assert not check_output(t, **KW).passed


@pytest.mark.parametrize("word", ["pilot", "Pilot", "SCHWERPUNKT", "Schwerpunkt", "ROI", "roi", "alignment score", "Alignment  Score"])
def test_banned_words_caught_case_insensitive(word):
    t = canned_output().replace("Rush jobs hurt.", f"Rush jobs hurt, said the {word}.")
    o = check_output(t, **KW)
    assert not o.passed and any("banned word" in p for p in o.problems)


@pytest.mark.parametrize("ok", ["pilots", "android", "avroitis", "Leadership alignment report", "a score of alignment"])
def test_banned_word_search_is_whole_word(ok):
    t = canned_output().replace("Rush jobs hurt.", f"Rush jobs hurt: {ok}.")
    assert check_output(t, **KW).passed


def test_agent_saying_banned_word_no_does_not_excuse_it():
    t = canned_output().replace("Quotes are too slow.", "Quotes are too slow: a ROI of zero.")
    assert "Any banned word: no" in t
    assert not check_output(t, **KW).passed


def test_removed_marker_in_report_holds():
    t = canned_output().replace("Quotes are too slow.", '"[removed] never signs off." Quotes are too slow.')
    o = check_output(t, **KW)
    assert not o.passed and any("[removed]" in p for p in o.problems)


def test_short_report_is_a_warning_not_a_hold():
    t = canned_output()
    t = "\n".join(l for l in t.splitlines() if not l.startswith(("- ", "| ", "1. ", "2. ", "3. ")))
    o = check_output(t, **KW)
    assert o.passed and any("words" in w for w in o.warnings)


def test_real_banned_words_absent_from_prompt_outputs_we_ship():
    # the approved template and the fixture carry none of the banned words
    assert not checks.BANNED.search(synthesis.report_template())
    assert not checks.BANNED.search(check_output(canned_output(), **KW).report)
