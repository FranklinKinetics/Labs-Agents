import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

BUILD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BUILD))
LAB = BUILD.parent
REPO = LAB.parents[1]

from diagnostic import blocks as B                                   # noqa: E402
from diagnostic.config import Config                                 # noqa: E402
from diagnostic.emails import FakeMailer                             # noqa: E402
from diagnostic.models import OrderInput                             # noqa: E402
from diagnostic.service import App                                   # noqa: E402
from diagnostic.store import InMemoryStore                           # noqa: E402
from diagnostic.synthesis import FakeIdentifierCheck, FakeSynthesis  # noqa: E402

SAMPLE = (LAB / "05-sample-report.md").read_text(encoding="utf-8")
LINK = Config().start_conversation_link


def larchmere_blocks() -> list[str]:
    out = []
    for m in re.finditer(r"```\n(=== ROTOR INTERVIEW SUMMARY ===.*?=== END SUMMARY ===)\n```", SAMPLE, re.S):
        out.append(m.group(1))
    assert len(out) == 5
    return out


def canned_output(link: str = LINK) -> str:
    """The Larchmere report (sample section 3) plus its check sheet, as the agent would return it."""
    s = SAMPLE.index("# Leadership alignment report · Larchmere Fabrication")
    e = SAMPLE.index("---\n\n```\n=== CHECKS ===")
    report = SAMPLE[s:e].replace("*Fictional sample*\n", "").replace("[link]", link).rstrip()
    sheet = re.search(r"(=== CHECKS ===.*?=== END CHECKS ===)", SAMPLE, re.S).group(1)
    return report + "\n\n" + sheet + "\n"


def adaptive_output(extra=lambda t: t):
    """Canned report that says the right number of leaders for what it was sent."""
    def make(system, user):
        n = user.count(B.START)
        t = canned_output().replace("Valid blocks used: 5", f"Valid blocks used: {n}")
        t = t.replace("interviews with 5 leaders", f"interviews with {n} leaders")
        return extra(t)
    return make


class Clock:
    def __init__(self, start=None):
        self.now = start or datetime(2026, 11, 10, 15, 0, tzinfo=timezone.utc)

    def __call__(self):
        return self.now

    def advance(self, **kw):
        self.now += timedelta(**kw)


def order(**kw) -> OrderInput:
    d = dict(order_id="SQ-1001", ceo_name="Dale Kowalchuk", ceo_email="ceo@larchmere.example",
             company_name="Larchmere Fabrication", province="SK", platform="Claude",
             planned_leaders=5, consent_keep_report=False)
    d.update(kw)
    return OrderInput(**d)


class Env:
    def __init__(self, synth=None, planted=None):
        self.clock = Clock()
        self.store = InMemoryStore()
        self.mailer = FakeMailer()
        self.synth = synth or FakeSynthesis(adaptive_output())
        self.idcheck = FakeIdentifierCheck(planted)
        self.cfg = Config()
        self.app = App(self.store, self.mailer, self.synth, self.idcheck, self.cfg, self.clock)

    def company(self, **kw):
        return self.app.create_company_from_order(order(**kw))

    def submit(self, c, text, ack=True):
        return self.app.submit_summary(c.drop_token, text, ack)

    def fill(self, c, k):
        for t in larchmere_blocks()[:k]:
            assert self.submit(c, t).ok

    def emails_to(self, kind):
        return [m for m in self.mailer.sent if m.kind == kind]


@pytest.fixture
def env():
    return Env()


@pytest.fixture
def blocks5():
    return larchmere_blocks()
