from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# company states
OPEN = "open"                    # drop-box accepting summaries
NOT_ENOUGH = "not_enough"        # window closed with fewer than 3; may restart
HELD = "held"                    # report held for Brandon
DELIVERED = "delivered"
DELIVERY_FAILED = "delivery_failed"


@dataclass
class OrderInput:
    order_id: str
    ceo_name: str
    ceo_email: str
    company_name: str
    province: str
    platform: str
    planned_leaders: int
    consent_keep_report: bool = False


@dataclass
class Company:
    id: str
    order_id: str
    ceo_name: str
    ceo_email: str
    company_name: str
    province: str
    platform: str
    planned_leaders: int
    consent_keep_report: bool
    drop_token: str          # private drop-box link (given to leaders by the CEO)
    status_token: str        # CEO-only status and actions
    salt: str                # per-company secret salt for name fingerprints (hex)
    purchased_at: datetime
    window_closes_at: datetime
    extended: bool = False
    restarts_used: int = 0
    state: str = OPEN
    held_reasons: list = field(default_factory=list)
    delivered_at: Optional[datetime] = None


@dataclass
class ScheduledEmail:
    company_id: str
    kind: str
    due_at: datetime
    sent: bool = False


@dataclass
class Result:
    ok: bool
    message: str
