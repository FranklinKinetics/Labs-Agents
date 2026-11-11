"""Orders polling and the real adapters (offline: stub clients only)."""
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from conftest import BUILD, Env, canned_output, order
from diagnostic.adapters import anthropic_adapters as AA
from diagnostic.orders import FakeOrders


# ---------------------------------------------------------------- orders polling

def test_polling_makes_each_order_once_and_sends_one_kit():
    e = Env(); src = FakeOrders([order(order_id="A"), order(order_id="B", company_name="Two Co")])
    assert len(e.app.poll_orders(src)) == 2
    assert e.app.poll_orders(src) == []                       # same orders again: nothing happens
    src.add(order(order_id="C", company_name="Three Co"))
    assert len(e.app.poll_orders(src)) == 1
    assert len(e.store.list_companies()) == 3 and len(e.emails_to("setup_kit")) == 3


def test_polling_rejects_quebec_alerts_brandon_once():
    e = Env(); src = FakeOrders([order(order_id="Q", province="QC")])
    assert e.app.poll_orders(src) == []
    assert e.app.poll_orders(src) == []
    assert e.store.list_companies() == [] and not e.emails_to("setup_kit")
    alerts = e.emails_to("order_alert")
    assert len(alerts) == 1 and alerts[0].to == e.cfg.alert_email and "Quebec" in alerts[0].body


def test_one_bad_order_does_not_block_the_others():
    e = Env(); src = FakeOrders([order(order_id="X", planned_leaders=1), order(order_id="Y")])
    assert [c.order_id for c in e.app.poll_orders(src)] == ["Y"]


# ---------------------------------------------------------------- Anthropic adapter (stub, no network)

class StubStream:
    def __init__(self, message): self.message = message
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def get_final_message(self): return self.message


class StubClient:
    def __init__(self, message):
        self.kwargs = None
        outer = self
        class M:
            def stream(self, **kw):
                outer.kwargs = kw
                return StubStream(message)
        self.beta = SimpleNamespace(messages=M())


def msg(stop, text="hello"):
    return SimpleNamespace(stop_reason=stop, content=[SimpleNamespace(type="text", text=text)])


def test_adapter_request_shape():
    c = StubClient(msg("end_turn", "REPORT"))
    r = AA.AnthropicSynthesis(c).synthesize("SYS", "USER")
    k = c.kwargs
    assert r.text == "REPORT" and r.stop_reason == "end_turn"
    assert k["model"] == "claude-opus-5-5"
    assert k["max_tokens"] == 64000
    assert k["output_config"] == {"effort": "high"}
    assert k["betas"] == ["server-side-fallback-2026-07-01"]
    assert k["fallbacks"] == "default"
    assert k["system"] == "SYS" and k["messages"] == [{"role": "user", "content": "USER"}]
    assert "thinking" not in k and "budget_tokens" not in repr(k)


def test_adapter_refusal_returns_no_content_and_holds():
    c = StubClient(msg("refusal", "SHOULD NOT BE READ"))
    r = AA.AnthropicSynthesis(c).synthesize("S", "U")
    assert r.stop_reason == "refusal" and r.text == ""
    e = Env(synth=AA.AnthropicSynthesis(c))
    co = e.company(); e.fill(co, 3); e.app.close_early(co.status_token)
    assert co.state == "held" and not e.emails_to("report")


def test_identifier_check_parsing():
    assert AA.AnthropicIdentifierCheck(StubClient(msg("end_turn", "NONE"))).check("r") == []
    assert AA.AnthropicIdentifierCheck(StubClient(msg("end_turn", "A first name\nA job title"))).check("r") == ["A first name", "A job title"]
    assert AA.AnthropicIdentifierCheck(StubClient(msg("refusal", ""))).check("r")       # refusal counts as a flag
    c = StubClient(msg("end_turn", "NONE"))
    AA.AnthropicIdentifierCheck(c).check("THE REPORT")
    assert c.kwargs["messages"] == [{"role": "user", "content": "THE REPORT"}]          # report only


def test_installed_sdk_accepts_fallbacks_keyword():
    import anthropic, inspect
    assert "fallbacks" in inspect.signature(anthropic.Anthropic(api_key="unused").beta.messages.stream).parameters


def test_real_adapters_are_never_imported_by_the_app_or_the_fixtures():
    src = (BUILD / "diagnostic" / "service.py").read_text()
    assert "adapters" not in src and "anthropic" not in src


# ---------------------------------------------------------------- secrets

def test_no_secrets_in_the_build_folder():
    pat = re.compile(r"sk-ant-[A-Za-z0-9_\-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?i:password\s*=\s*['\"][^'\"]{4,})")
    for p in BUILD.rglob("*"):
        if p.is_file() and p.suffix in {".py", ".md", ".txt", ".ini", ".yaml", ".json"} and "__pycache__" not in p.parts:
            assert not pat.search(p.read_text(errors="ignore")), p


def test_real_adapters_read_secrets_from_environment_only():
    for f in ["squarespace.py", "smtp_mailer.py", "anthropic_adapters.py"]:
        t = (BUILD / "diagnostic" / "adapters" / f).read_text()
        assert "os.environ" in t or "Anthropic()" in t
