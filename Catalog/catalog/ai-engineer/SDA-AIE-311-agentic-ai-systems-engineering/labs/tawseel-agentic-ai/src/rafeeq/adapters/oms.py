"""Module 3 — Order Management System (OMS) mock adapter.

One of four separate mock backends (SPEC §6: MCP servers should be one per
trust boundary, not one mega-server — orders, logistics, billing, customer
each get their own adapter here and their own MCP server later in
mcp_servers/). `OrderManagementClient` is the only thing tools/orders.py
should ever import; it never touches the JSON files directly — everything
goes through the shared `rafeeq.adapters.store.store` singleton.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rafeeq.adapters.store import store
from rafeeq.core.errors import ToolError


@dataclass(frozen=True)
class OrderRecord:
    """Mirrors the order record shape in SPEC §4 exactly — field names are
    binding, other modules pattern-match on them."""

    order_id: str
    customer_id: str
    city: str
    city_ar: str
    status: str
    placed_at: str
    promised_at: str
    delivered_at: str | None
    eta_iso: str | None
    sla_breached: bool
    amount_sar: float
    currency: str
    items: int
    courier_id: str | None
    refunded: bool
    refund_amount_sar: float
    payment_id: str
    channel: str
    fragile: bool
    delivery_note: str | None
    delivery_note_ar: str | None

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "OrderRecord":
        return cls(**{f: d.get(f) for f in cls.__dataclass_fields__})


class OrderManagementClient:
    """Mock of Tawseel's Order Management System."""

    def get_order(self, order_id: str) -> OrderRecord:
        raw = store.get_order(order_id)
        if raw is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        return OrderRecord.from_dict(raw)

    def list_orders_for_customer(self, customer_id: str) -> list[OrderRecord]:
        return [OrderRecord.from_dict(o) for o in store.list_orders_for_customer(customer_id)]

    def set_status(self, order_id: str, status: str) -> OrderRecord:
        raw = store.get_order(order_id)
        if raw is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        raw["status"] = status
        return OrderRecord.from_dict(raw)

    def mark_refunded(self, order_id: str, refund_amount_sar: float) -> OrderRecord:
        """Flip the order's refund flags. Called by billing.issue_refund
        AFTER the payment side has recorded the refund — order state and
        payment state must move together or a partial-failure leaves an
        order marked refunded with no matching payment record (or vice
        versa), which is exactly the kind of silent-wrongness bug M4/M8
        teach participants to design against."""
        raw = store.get_order(order_id)
        if raw is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        raw["refunded"] = True
        raw["refund_amount_sar"] = round(float(raw.get("refund_amount_sar", 0.0)) + refund_amount_sar, 2)
        return OrderRecord.from_dict(raw)
