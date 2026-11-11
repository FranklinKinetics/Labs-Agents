"""Orders polling. The source is read-only; the poller turns each new
diagnostic order into one company, once."""
from __future__ import annotations

from .models import OrderInput


class OrdersSource:
    """Interface. fetch_new_orders() -> list[OrderInput] of diagnostic orders."""
    def fetch_new_orders(self) -> list:
        raise NotImplementedError


class FakeOrders(OrdersSource):
    def __init__(self, orders=None):
        self.orders = list(orders or [])

    def add(self, order: OrderInput):
        self.orders.append(order)

    def fetch_new_orders(self):
        # a real API keeps returning recent orders, so the poller must be idempotent
        return list(self.orders)
