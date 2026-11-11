"""Settings. Secrets come from environment variables only (in production,
Secret Manager fills them in). Nothing secret is ever written in this repo."""
from __future__ import annotations

import os
from dataclasses import dataclass, field

PLACEHOLDER_ADDRESS = "[MAILING ADDRESS: Brandon to supply before launch]"


@dataclass
class Config:
    app_base_url: str = "http://localhost:8080"          # decided before Release
    start_conversation_link: str = "https://www.franklinkinetics.com/contact"           # confirmed 2026-11-11
    privacy_url: str = "https://www.franklinkinetics.com/alignment-diagnostic/privacy"
    terms_url: str = "https://www.franklinkinetics.com/alignment-diagnostic/terms"
    sender_name: str = "Franklin Kinetics Consulting Corporation"
    sender_address: str = "1400-2500 Victoria Ave, Regina SK S4P 3X2"   # CASL mailing address, decided 2026-11-11
    contact_email: str = "contact@franklinkinetics.com"
    alert_email: str = "contact@franklinkinetics.com"       # held-report alerts go here
    window_days: int = 21
    extension_days: int = 14
    min_leaders: int = 3
    max_leaders: int = 8
    checkin_days: int = 14
    restart_months: int = 12
    model: str = "claude-opus-5-5"

    @classmethod
    def from_env(cls, env=os.environ) -> "Config":
        c = cls()
        for attr, var in [
            ("app_base_url", "DIAG_APP_BASE_URL"),
            ("start_conversation_link", "DIAG_START_CONVERSATION_LINK"),
            ("sender_address", "DIAG_SENDER_ADDRESS"),
            ("alert_email", "DIAG_ALERT_EMAIL"),
        ]:
            if env.get(var):
                setattr(c, attr, env[var])
        return c

    def problems(self) -> list[str]:
        """Things that must be filled in before real use."""
        out = []
        if self.sender_address == PLACEHOLDER_ADDRESS:
            out.append("sender_address (DIAG_SENDER_ADDRESS) is still a placeholder")
        if self.app_base_url.startswith("http://localhost"):
            out.append("app_base_url (DIAG_APP_BASE_URL) is still localhost")
        return out
