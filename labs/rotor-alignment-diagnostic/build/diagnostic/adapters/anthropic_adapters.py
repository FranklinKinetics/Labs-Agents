"""REAL adapters for the Claude API. NOT used by any test that touches the
network, and not run during the bench build. The key is read from the
ANTHROPIC_API_KEY environment variable (Secret Manager fills it in on Cloud
Run). It is never written in this repo.
"""
from __future__ import annotations

from ..synthesis import IdentifierCheckAdapter, SynthesisAdapter, SynthesisResult

MODEL = "claude-opus-5-5"
FALLBACK_BETA = "server-side-fallback-2026-07-01"


def make_client():
    import anthropic  # imported here so the bench never needs a key
    return anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from the environment


def _text_of(message) -> str:
    return "".join(getattr(b, "text", "") for b in message.content if getattr(b, "type", "") == "text")


class AnthropicSynthesis(SynthesisAdapter):
    def __init__(self, client=None, model: str = MODEL):
        self.client = client or make_client()
        self.model = model

    def synthesize(self, system: str, user: str) -> SynthesisResult:
        # Thinking is left at the model's default (adaptive). Do NOT send
        # budget_tokens or {"type": "disabled"}: both return 400 on this model.
        with self.client.beta.messages.stream(
            model=self.model,
            max_tokens=64000,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": "high"},
            betas=[FALLBACK_BETA],
            fallbacks="default",       # server-side retry on another model if declined
        ) as stream:
            message = stream.get_final_message()
        # Check stop_reason BEFORE reading content.
        if message.stop_reason != "end_turn":
            return SynthesisResult("", message.stop_reason or "unknown")   # "refusal" => the report is held
        return SynthesisResult(_text_of(message), "end_turn")


CHECK_SYSTEM = """You check a finished report for anonymity. You will be given a leadership report written from anonymous interview summaries.
List any personal name, any job title or role, any team or department tied to a person, and any detail that could point to one individual.
If you find nothing, reply with exactly: NONE
Otherwise reply with one short line per finding, describing it without repeating the name. Reply with nothing else."""


class AnthropicIdentifierCheck(IdentifierCheckAdapter):
    """Second, separate call. It sees only the finished report, never the summaries."""
    def __init__(self, client=None, model: str = MODEL):
        self.client = client or make_client()
        self.model = model

    def check(self, report_text: str) -> list[str]:
        with self.client.beta.messages.stream(
            model=self.model,
            max_tokens=2000,
            system=CHECK_SYSTEM,
            messages=[{"role": "user", "content": report_text}],
            betas=[FALLBACK_BETA],
            fallbacks="default",
        ) as stream:
            message = stream.get_final_message()
        if message.stop_reason != "end_turn":
            return [f"second check did not finish (stop reason: {message.stop_reason})"]
        answer = _text_of(message).strip()
        if answer == "NONE":
            return []
        return [l.strip() for l in answer.splitlines() if l.strip()] or ["second check gave an unreadable answer"]
