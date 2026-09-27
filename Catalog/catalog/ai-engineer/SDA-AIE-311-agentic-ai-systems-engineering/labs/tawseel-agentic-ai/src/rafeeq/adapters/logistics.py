"""Module 3 — Logistics/Tracking mock adapter.

LaDe-shaped (SPEC §6): `status`, `events`, `estimate_eta`, `reschedule`,
`driver_status`, `find_exception` mirror the LaDe last-mile dataset's
tool shape (`get_delivery_status`, `get_driver_status`, `estimate_eta`,
`get_delivery_events`, `find_delivery_exception`) without shipping any of
its actual data — everything here is synthetic Saudi data (data/generate.py).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

from rafeeq.adapters.store import store
from rafeeq.core.errors import ToolError


@dataclass(frozen=True)
class DeliveryEvent:
    order_id: str
    seq: int
    event: str
    ts: str
    courier_id: str | None
    lat: float
    lng: float
    city: str
    note: str | None
    exception_code: str | None

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "DeliveryEvent":
        return cls(**{f: d.get(f) for f in cls.__dataclass_fields__})


class LogisticsClient:
    """Mock of Tawseel's logistics/tracking system."""

    def status(self, order_id: str) -> dict[str, Any]:
        order = store.get_order(order_id)
        if order is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        return {
            "order_id": order_id,
            "status": order["status"],
            "eta_iso": order.get("eta_iso"),
            "sla_breached": order.get("sla_breached", False),
            "courier_id": order.get("courier_id"),
        }

    def events(self, order_id: str) -> list[DeliveryEvent]:
        if store.get_order(order_id) is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        return [DeliveryEvent.from_dict(e) for e in store.get_events(order_id)]

    def estimate_eta(self, order_id: str) -> dict[str, Any]:
        order = store.get_order(order_id)
        if order is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        eta = order.get("eta_iso")
        if order["status"] == "delivered":
            return {"order_id": order_id, "eta_iso": order.get("delivered_at"), "delivered": True}
        return {"order_id": order_id, "eta_iso": eta, "delivered": False}

    def reschedule(self, order_id: str, new_promised_at_iso: str) -> dict[str, Any]:
        """Autonomous-within-policy action (SPEC §5 action-risk matrix):
        allowed without human approval, but always logged with before/after
        so it is auditable."""
        order = store.get_order(order_id)
        if order is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        if order["status"] in ("delivered", "exception"):
            raise ToolError(
                f"Cannot reschedule order {order_id} in status '{order['status']}'",
                order_id=order_id, status=order["status"],
            )
        before = order.get("promised_at")
        order["promised_at"] = new_promised_at_iso
        # ETA follows the new promise, clamped to a plausible window before it.
        try:
            promised = datetime.fromisoformat(new_promised_at_iso)
            order["eta_iso"] = (promised - timedelta(hours=2)).isoformat()
        except ValueError:  # pragma: no cover - defensive, bad caller input
            pass
        order["sla_breached"] = False
        return {
            "order_id": order_id, "rescheduled": True,
            "promised_at_before": before, "promised_at_after": order["promised_at"],
            "eta_iso": order["eta_iso"],
        }

    def driver_status(self, courier_id: str) -> dict[str, Any]:
        # Derived from the most recent event for that courier across all
        # orders in memory — a thin mock, sufficient for lab tooling.
        store.ensure_loaded()
        latest: dict[str, Any] | None = None
        for events in store.events_by_order.values():
            for e in events:
                if e.get("courier_id") == courier_id:
                    if latest is None or e["ts"] > latest["ts"]:
                        latest = e
        if latest is None:
            raise ToolError(f"No activity found for courier {courier_id}", courier_id=courier_id)
        return {
            "courier_id": courier_id, "last_event": latest["event"], "last_seen": latest["ts"],
            "city": latest.get("city"), "lat": latest.get("lat"), "lng": latest.get("lng"),
        }

    def find_exception(self, order_id: str) -> dict[str, Any] | None:
        events = store.get_events(order_id)
        for e in reversed(events):
            if e.get("exception_code"):
                return {
                    "order_id": order_id, "exception_code": e["exception_code"],
                    "ts": e["ts"], "note": e.get("note"),
                }
        order = store.get_order(order_id)
        if order and order.get("status") == "exception":
            return {"order_id": order_id, "exception_code": "unspecified", "ts": None, "note": None}
        return None
