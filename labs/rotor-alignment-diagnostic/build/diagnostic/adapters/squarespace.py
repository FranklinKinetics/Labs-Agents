"""REAL adapter for the Squarespace Orders API (read-only). Not called by any
test. The API key is read from SQUARESPACE_API_KEY (Secret Manager in
production).

UNVERIFIED: how the checkout questions (company name, province, platform,
planned leaders, consent) appear in an order is not confirmed. The mapping in
_to_order is a best guess to be checked against a real test order in Step 2.
"""
from __future__ import annotations

import json
import os
import urllib.request

from ..models import OrderInput
from ..orders import OrdersSource

API = "https://api.squarespace.com/1.0/commerce/orders"
PRODUCT_NAME = "Rotor Alignment Diagnostic"


class SquarespaceOrders(OrdersSource):
    def __init__(self, api_key: str | None = None, product_name: str = PRODUCT_NAME):
        self.api_key = api_key or os.environ["SQUARESPACE_API_KEY"]
        self.product_name = product_name

    def _get(self, url: str) -> dict:
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "fk-diagnostic-orders/0.1",
        })
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)

    def fetch_new_orders(self) -> list[OrderInput]:
        out, url = [], API
        while url:
            page = self._get(url)
            for o in page.get("result", []):
                if any(self.product_name.lower() in (i.get("productName") or "").lower()
                       for i in o.get("lineItems", [])):
                    parsed = self._to_order(o)
                    if parsed:
                        out.append(parsed)
            nxt = page.get("pagination", {})
            url = nxt.get("nextPageUrl") if nxt.get("hasNextPage") else None
        return out

    @staticmethod
    def _to_order(o: dict) -> OrderInput | None:
        form = {(f.get("label") or "").strip().lower(): f.get("value")
                for f in (o.get("formSubmission") or [])}
        try:
            return OrderInput(
                order_id=o["id"],
                ceo_name=f"{o.get('billingAddress', {}).get('firstName', '')} {o.get('billingAddress', {}).get('lastName', '')}".strip(),
                ceo_email=o.get("customerEmail", ""),
                company_name=form.get("company name", ""),
                province=form.get("province of head office", ""),
                platform=form.get("ai platform", ""),
                planned_leaders=int(form.get("planned number of leaders", 0) or 0),
                consent_keep_report=str(form.get("keep our report", "")).strip().lower() in ("yes", "true", "on", "checked"),
            )
        except (KeyError, ValueError):
            return None
