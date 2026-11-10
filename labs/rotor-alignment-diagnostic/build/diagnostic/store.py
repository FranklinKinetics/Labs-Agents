"""Where things are kept. The bench uses InMemoryStore; Step 2 adds a
Firestore (Montréal) version with the same methods."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from .models import Company, ScheduledEmail


class Store:
    """Interface. Everything the app keeps goes through these methods."""
    def add_company(self, c: Company): raise NotImplementedError
    def save_company(self, c: Company): raise NotImplementedError
    def get_company(self, company_id: str) -> Optional[Company]: raise NotImplementedError
    def find_by_order(self, order_id: str) -> Optional[Company]: raise NotImplementedError
    def find_by_drop_token(self, token: str) -> Optional[Company]: raise NotImplementedError
    def find_by_status_token(self, token: str) -> Optional[Company]: raise NotImplementedError
    def list_companies(self) -> list: raise NotImplementedError

    def add_summary(self, company_id: str, stripped_text: str, fingerprint: str): raise NotImplementedError
    def summaries(self, company_id: str) -> list: raise NotImplementedError
    def has_fingerprint(self, company_id: str, fp: str) -> bool: raise NotImplementedError
    def delete_summaries(self, company_id: str) -> int: raise NotImplementedError

    def log_deletion(self, date: str, count: int): raise NotImplementedError
    def deletion_log(self) -> list: raise NotImplementedError

    def save_report(self, company_id: str, text: str): raise NotImplementedError
    def get_report(self, company_id: str) -> Optional[str]: raise NotImplementedError
    def delete_report(self, company_id: str): raise NotImplementedError

    def schedule_email(self, e: ScheduledEmail): raise NotImplementedError
    def due_emails(self, now: datetime) -> list: raise NotImplementedError
    def scheduled_emails(self) -> list: raise NotImplementedError

    def reject_order(self, order_id: str, reason: str): raise NotImplementedError
    def rejected_orders(self) -> dict: raise NotImplementedError

    def unsubscribe(self, email: str): raise NotImplementedError
    def is_unsubscribed(self, email: str) -> bool: raise NotImplementedError


class InMemoryStore(Store):
    def __init__(self):
        self.companies: dict[str, Company] = {}
        self._summaries: dict[str, list] = {}      # id -> [(text, fingerprint)]
        self._deletions: list[dict] = []
        self._reports: dict[str, str] = {}
        self._emails: list[ScheduledEmail] = []
        self._rejected: dict[str, str] = {}
        self._unsub: set[str] = set()

    def add_company(self, c): self.companies[c.id] = c
    def save_company(self, c): self.companies[c.id] = c
    def get_company(self, company_id): return self.companies.get(company_id)
    def find_by_order(self, order_id):
        return next((c for c in self.companies.values() if c.order_id == order_id), None)
    def find_by_drop_token(self, token):
        return next((c for c in self.companies.values() if c.drop_token == token), None)
    def find_by_status_token(self, token):
        return next((c for c in self.companies.values() if c.status_token == token), None)
    def list_companies(self): return list(self.companies.values())

    def add_summary(self, company_id, stripped_text, fingerprint):
        self._summaries.setdefault(company_id, []).append((stripped_text, fingerprint))
    def summaries(self, company_id):
        return [t for t, _ in self._summaries.get(company_id, [])]
    def has_fingerprint(self, company_id, fp):
        return any(f == fp for _, f in self._summaries.get(company_id, []))
    def delete_summaries(self, company_id):
        n = len(self._summaries.get(company_id, []))
        self._summaries.pop(company_id, None)
        return n

    def log_deletion(self, date, count): self._deletions.append({"date": date, "count": count})
    def deletion_log(self): return list(self._deletions)

    def save_report(self, company_id, text): self._reports[company_id] = text
    def get_report(self, company_id): return self._reports.get(company_id)
    def delete_report(self, company_id): self._reports.pop(company_id, None)

    def schedule_email(self, e): self._emails.append(e)
    def due_emails(self, now): return [e for e in self._emails if not e.sent and e.due_at <= now]
    def scheduled_emails(self): return list(self._emails)

    def reject_order(self, order_id, reason): self._rejected[order_id] = reason
    def rejected_orders(self): return dict(self._rejected)

    def unsubscribe(self, email): self._unsub.add(email.strip().lower())
    def is_unsubscribed(self, email): return email.strip().lower() in self._unsub
