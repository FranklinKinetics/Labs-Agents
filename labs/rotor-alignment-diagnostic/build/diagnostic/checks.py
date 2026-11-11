"""Automatic checks on the agent's output. A report that fails ANY check is held."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .synthesis import fill_template

CHECKS_START = "=== CHECKS ==="
CHECKS_END = "=== END CHECKS ==="

# line label -> required answer (None for the block count, checked against n)
EXPECTED_CHECKS = [
    ("Valid blocks used", None),
    ("Every section filled", "yes"),
    ("Any name, role or identifying detail left", "no"),
    ("Any quote attributed or counted to one person", "no"),
    ("Any recommendation of a main effort or advice", "no"),
    ("Any result, savings or ROI claim", "no"),
    ("Any banned word", "no"),
    ('Every "all" claim supported by every block', "yes"),
    ("Every effect in section 4 joins a split to something leaders named", "yes"),
]

# Fenn's sentence, added to section 9 on 2026-11-11 (reconciliation M1). The full section is
# still compared word for word against the template; this names the missing piece plainly.
DISTILLATION_SENTENCE = "If there's little to settle, the Rotor Distillation takes your strategy into your AI tools."

BANNED = re.compile(r"(?<!\w)(pilot|schwerpunkt|roi|alignment\s+score)(?!\w)", re.IGNORECASE)
INSUFFICIENT = re.compile(r"^\s*INSUFFICIENT:\s*(\d+)\s+valid blocks\s*$")


@dataclass
class CheckOutcome:
    passed: bool
    report: str = ""
    problems: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


def headings(text: str) -> list[str]:
    return [l.strip() for l in text.splitlines() if re.match(r"^#{1,3} ", l)]


def section(text: str, heading: str) -> str:
    """Body of a heading, up to the next heading of the same or higher level."""
    lines = text.splitlines()
    level = len(heading) - len(heading.lstrip("#"))
    for i, l in enumerate(lines):
        if l.strip() == heading:
            body = []
            for m in lines[i + 1:]:
                if re.match(r"^#{1,%d} " % level, m):
                    break
                body.append(m)
            return "\n".join(body)
    return ""


def _squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def split_output(output: str) -> tuple[str, str | None]:
    """(report, check sheet text or None)."""
    if CHECKS_START not in output:
        return output.strip(), None
    report, _, rest = output.partition(CHECKS_START)
    if CHECKS_END not in rest:
        return report.strip(), None
    sheet, _, _ = rest.partition(CHECKS_END)
    return report.strip(), sheet.strip()


def check_output(output: str, *, company: str, date: str, n: int, link: str) -> CheckOutcome:
    problems: list[str] = []
    warnings: list[str] = []

    m = INSUFFICIENT.match(output.strip())
    if m:
        return CheckOutcome(False, "", [f"agent reported INSUFFICIENT: {m.group(1)} valid blocks"])

    report, sheet = split_output(output)

    # 1. headings, in order
    template = fill_template(company, date, n, link)
    want = headings(template)
    got = headings(report)
    for h in want:
        if h not in got:
            problems.append(f"missing heading: {h}")
    if not any(p.startswith("missing heading") for p in problems):
        if [h for h in got if h in want] != want:
            problems.append("headings are out of order")
        extra = [h for h in got if h not in want]
        if extra:
            problems.append(f"unexpected heading: {extra[0]}")

    # 2. fixed text of section 9
    nine = "## 9. Next step"
    if nine in want and _squash(section(report, nine)) != _squash(section(template, nine)):
        problems.append("section 9 (Next step) does not match the approved wording")
    if nine in want and DISTILLATION_SENTENCE not in _squash(section(report, nine)):
        problems.append("section 9 (Next step) is missing the Rotor Distillation sentence")

    # 3. check sheet
    if sheet is None:
        problems.append("check sheet missing or not closed")
    else:
        seen: dict[str, str] = {}
        for line in sheet.splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                seen.setdefault(k.strip(), v.strip().lower())
        for label, want_ans in EXPECTED_CHECKS:
            got_ans = seen.get(label)
            if got_ans is None:
                problems.append(f"check sheet line missing: {label}")
            elif label == "Valid blocks used":
                if got_ans != str(n):
                    problems.append(f"check sheet says {got_ans} valid blocks; {n} were sent")
            elif got_ans != want_ans:
                problems.append(f"check sheet line answered '{got_ans}': {label}")

    # 4. plain word search on the report (the agent's own say-so is not trusted).
    #    Not on the check sheet: its own line "Any result, savings or ROI claim" has to say ROI.
    hits = sorted({h.group(1).lower() for h in BANNED.finditer(report)})
    if hits:
        problems.append("banned word found: " + ", ".join(hits))

    # 5. a name stripped from a quote must not reach the CEO
    if "[removed]" in report:
        problems.append('the report contains "[removed]" (a stripped name inside a quote)')

    # soft: length
    words = len(report.split())
    if not 1200 <= words <= 2000:
        warnings.append(f"report is {words} words (target 1,200 to 2,000)")

    return CheckOutcome(not problems, report, problems, warnings)
