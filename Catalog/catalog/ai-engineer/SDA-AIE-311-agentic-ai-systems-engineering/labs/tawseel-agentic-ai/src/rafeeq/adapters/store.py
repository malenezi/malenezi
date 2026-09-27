"""Module 3 — the in-memory Tawseel data store backing every mock adapter.

TEACHING POINT: tools (M3) should never read files directly — they call an
adapter, and every adapter reads through ONE lazily-loaded, indexed,
mutable store. This is what lets `issue_refund` actually flip
`order.refunded` for the rest of a run, lets TawseelBench set up scenario
state with `snapshot()`/`restore()` without leaking between scenarios, and
lets tests call `reset()` to get back to the seed data.

Loading is lazy (first access, not import time — SPEC §1's "no network
calls / expensive work at import time" rule extends to disk I/O here) and
cached at module level, since the seed JSON is large (2000 orders) and
every adapter and the eval harness would otherwise reload it repeatedly.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from rafeeq.core.config import (
    CUSTOMERS_SEED_PATH,
    DELIVERY_EVENTS_PATH,
    ORDERS_SEED_PATH,
    PAYMENTS_SEED_PATH,
)


def _read_json(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


class TawseelStore:
    """The single in-memory source of truth for mock Tawseel data.

    Indexed by primary key for O(1) lookups, plus a few secondary indexes
    (orders by customer, events by order, payments by order) built once at
    load time. All mutation happens here so `oms.py`/`billing.py`/etc. stay
    thin — they express *intent* (mark_refunded, reschedule), the store
    holds the *state*.
    """

    def __init__(self) -> None:
        self._loaded = False
        self.customers: dict[str, dict[str, Any]] = {}
        self.orders: dict[str, dict[str, Any]] = {}
        self.payments: dict[str, dict[str, Any]] = {}
        self.events_by_order: dict[str, list[dict[str, Any]]] = {}
        self.orders_by_customer: dict[str, list[str]] = {}
        self.payment_by_order: dict[str, str] = {}
        # CRM support tickets are adapter-internal mock state (not one of
        # the required seed files) — synthesised deterministically from
        # each customer's `open_tickets` count on first load.
        self.tickets_by_customer: dict[str, list[dict[str, Any]]] = {}
        # Idempotency ledger for billing.issue_refund — keyed by
        # idempotency_key, so a retried refund request never double-pays.
        self.refund_ledger: dict[str, dict[str, Any]] = {}

    # -- loading -------------------------------------------------------
    def _ensure_loaded(self) -> None:
        if self._loaded:
            return
        self._load()
        self._loaded = True

    def _load(self) -> None:
        self.customers = {c["customer_id"]: c for c in _read_json(CUSTOMERS_SEED_PATH)}
        self.orders = {o["order_id"]: o for o in _read_json(ORDERS_SEED_PATH)}
        self.payments = {p["payment_id"]: p for p in _read_json(PAYMENTS_SEED_PATH)}

        self.orders_by_customer = {}
        for order in self.orders.values():
            self.orders_by_customer.setdefault(order["customer_id"], []).append(order["order_id"])

        self.payment_by_order = {p["order_id"]: p["payment_id"] for p in self.payments.values()}

        self.events_by_order = {}
        for event in _read_jsonl(DELIVERY_EVENTS_PATH):
            self.events_by_order.setdefault(event["order_id"], []).append(event)
        for events in self.events_by_order.values():
            events.sort(key=lambda e: e.get("seq", 0))

        self.tickets_by_customer = {}
        for cust in self.customers.values():
            n_open = int(cust.get("open_tickets", 0) or 0)
            tickets = []
            for i in range(n_open):
                tickets.append({
                    "ticket_id": f"TKT-{cust['customer_id'][-4:]}{i:02d}",
                    "customer_id": cust["customer_id"],
                    "status": "open",
                    "subject": "synthetic open ticket (seed)",
                    "notes": [],
                })
            self.tickets_by_customer[cust["customer_id"]] = tickets

        self.refund_ledger = {}

    # -- lifecycle -------------------------------------------------------
    def ensure_loaded(self) -> None:
        """Public trigger for lazy loading — adapters that need to scan
        every index directly (rather than through a keyed accessor) call
        this first so they don't accidentally iterate an empty dict."""
        self._ensure_loaded()

    def reset(self) -> None:
        """Reload from disk, discarding all in-memory mutation. Call this
        between tests/scenarios that should not see each other's writes."""
        self._loaded = False
        self._ensure_loaded()

    def snapshot(self) -> dict[str, Any]:
        """Deep-copy the full mutable state. TawseelBench calls this before
        a scenario to capture a baseline it can `restore()` afterwards,
        guaranteeing scenarios never leak state into one another."""
        self._ensure_loaded()
        return copy.deepcopy({
            "customers": self.customers,
            "orders": self.orders,
            "payments": self.payments,
            "events_by_order": self.events_by_order,
            "orders_by_customer": self.orders_by_customer,
            "payment_by_order": self.payment_by_order,
            "tickets_by_customer": self.tickets_by_customer,
            "refund_ledger": self.refund_ledger,
        })

    def restore(self, snapshot: dict[str, Any]) -> None:
        """Restore a previously captured `snapshot()`."""
        restored = copy.deepcopy(snapshot)
        self.customers = restored["customers"]
        self.orders = restored["orders"]
        self.payments = restored["payments"]
        self.events_by_order = restored["events_by_order"]
        self.orders_by_customer = restored["orders_by_customer"]
        self.payment_by_order = restored["payment_by_order"]
        self.tickets_by_customer = restored["tickets_by_customer"]
        self.refund_ledger = restored["refund_ledger"]
        self._loaded = True

    # -- read accessors ----------------------------------------------------
    def get_customer(self, customer_id: str) -> dict[str, Any] | None:
        self._ensure_loaded()
        return self.customers.get(customer_id)

    def get_order(self, order_id: str) -> dict[str, Any] | None:
        self._ensure_loaded()
        return self.orders.get(order_id)

    def list_orders_for_customer(self, customer_id: str) -> list[dict[str, Any]]:
        self._ensure_loaded()
        return [self.orders[oid] for oid in self.orders_by_customer.get(customer_id, [])]

    def get_payment(self, payment_id: str) -> dict[str, Any] | None:
        self._ensure_loaded()
        return self.payments.get(payment_id)

    def get_payment_for_order(self, order_id: str) -> dict[str, Any] | None:
        self._ensure_loaded()
        pid = self.payment_by_order.get(order_id)
        return self.payments.get(pid) if pid else None

    def get_events(self, order_id: str) -> list[dict[str, Any]]:
        self._ensure_loaded()
        return list(self.events_by_order.get(order_id, []))

    def get_tickets(self, customer_id: str) -> list[dict[str, Any]]:
        self._ensure_loaded()
        return list(self.tickets_by_customer.get(customer_id, []))

    def counts(self) -> dict[str, int]:
        self._ensure_loaded()
        return {
            "customers": len(self.customers),
            "orders": len(self.orders),
            "payments": len(self.payments),
            "orders_with_events": len(self.events_by_order),
        }


# Module-level singleton — every adapter imports THIS instance so they all
# see the same mutable state (a refund issued via billing.py is visible to
# oms.py in the same process/run).
store = TawseelStore()
