"""Building the AI request, and the stand-ins used on the bench.

The instructions and report template are copied word for word from
04-synthesis-agent.md (sections 3 and 4, as amended in section 7). A test
checks the copies still match that file.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PROMPT_DIR = Path(__file__).parent / "prompts"
TEMPLATE_SLOT = "[REPORT TEMPLATE goes here: see section 4]"


def _read(name: str) -> str:
    return (PROMPT_DIR / name).read_text(encoding="utf-8").rstrip("\n")


def report_template() -> str:
    return _read("report_template.md")


def instructions_box() -> str:
    return _read("synthesis_instructions.md")


def _fill(text: str, values: dict[str, str]) -> str:
    # one pass, so a value that itself contains {n} is never filled again
    return re.sub(r"\{(company|date|n|start_conversation_link)\}", lambda m: values[m.group(1)], text)


def clean_company(name: str) -> str:
    return re.sub(r"\s+", " ", name).strip()


def fill_template(company: str, date: str, n: int, link: str) -> str:
    return _fill(report_template(), {"company": clean_company(company), "date": date,
                                     "n": str(n), "start_conversation_link": link})


def build_system_prompt(company: str, date: str, n: int, link: str) -> str:
    box = instructions_box()
    assert TEMPLATE_SLOT in box, "instructions box lost its template slot"
    box = box.replace(TEMPLATE_SLOT, report_template())
    return _fill(box, {"company": clean_company(company), "date": date,
                       "n": str(n), "start_conversation_link": link})


def build_user_message(blocks: list[str]) -> str:
    return (f"Here are the {len(blocks)} summary blocks. Write the report and the check sheet.\n\n"
            + "\n\n".join(b.strip() for b in blocks))


@dataclass
class SynthesisResult:
    text: str
    stop_reason: str = "end_turn"      # anything but "end_turn" holds the report


class SynthesisAdapter:
    """Interface. synthesize(system, user) -> SynthesisResult."""
    def synthesize(self, system: str, user: str) -> SynthesisResult:
        raise NotImplementedError


class IdentifierCheckAdapter:
    """Interface. A separate call that reads ONLY the finished report and
    returns a list of flags (empty = nothing found)."""
    def check(self, report_text: str) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- bench fakes

class FakeSynthesis(SynthesisAdapter):
    """Returns a canned output (a string, or a function of (system, user) that
    returns one). Records every call so tests can see whether the agent was
    run, and what it was sent."""
    def __init__(self, output, stop_reason: str = "end_turn"):
        self.output, self.stop_reason = output, stop_reason
        self.calls: list[tuple[str, str]] = []

    def synthesize(self, system, user):
        self.calls.append((system, user))
        out = self.output(system, user) if callable(self.output) else self.output
        return SynthesisResult(out, self.stop_reason)


class FakeInsufficient(SynthesisAdapter):
    """Behaves like the agent does when given fewer than 3 valid blocks."""
    def __init__(self):
        self.calls = []

    def synthesize(self, system, user):
        self.calls.append((system, user))
        n = user.count("=== ROTOR INTERVIEW SUMMARY ===")
        return SynthesisResult(f"INSUFFICIENT: {n} valid blocks")


class FakeIdentifierCheck(IdentifierCheckAdapter):
    """Flags any planted string it is told about (case-insensitive). A real
    check is an AI call; this one lets the bench prove a flag holds a report."""
    def __init__(self, planted: list[str] | None = None):
        self.planted = planted or []
        self.seen: list[str] = []

    def check(self, report_text):
        self.seen.append(report_text)
        low = report_text.lower()
        return [f"possible identifying detail: {p!r}" for p in self.planted if p.lower() in low]
