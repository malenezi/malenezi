"""Module 3 — CRM mock adapter (customer profile + support tickets)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rafeeq.adapters.store import store
from rafeeq.core.errors import ToolError


@dataclass(frozen=True)
class CustomerRecord:
    """Mirrors the customer record shape in SPEC §4 exactly."""

    customer_id: str
    name: str
    name_ar: str
    locale: str
    city: str
    tier: str
    joined: str
    phone_last4: str
    national_id_masked: str
    lifetime_orders: int
    open_tickets: int
    fraud_flag: bool

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CustomerRecord":
        return cls(**{f: d.get(f) for f in cls.__dataclass_fields__})


class CRMClient:
    """Mock of Tawseel's CRM system."""

    def get_customer(self, customer_id: str) -> CustomerRecord:
        raw = store.get_customer(customer_id)
        if raw is None:
            raise ToolError(f"Customer {customer_id} not found", customer_id=customer_id)
        return CustomerRecord.from_dict(raw)

    def get_tickets(self, customer_id: str) -> list[dict[str, Any]]:
        if store.get_customer(customer_id) is None:
            raise ToolError(f"Customer {customer_id} not found", customer_id=customer_id)
        return store.get_tickets(customer_id)

    def add_note(self, customer_id: str, ticket_id: str, note: str) -> dict[str, Any]:
        """Append a note to a ticket. TEACHING POINT (M4): this is a
        DELIBERATE memory write, not a side effect — every write here is a
        candidate for long-term memory (M4) and must stay scoped to this
        customer_id, never leaking into another customer's record."""
        if store.get_customer(customer_id) is None:
            raise ToolError(f"Customer {customer_id} not found", customer_id=customer_id)
        tickets = store.tickets_by_customer.setdefault(customer_id, [])
        for t in tickets:
            if t["ticket_id"] == ticket_id:
                t["notes"].append(note)
                return {"ticket_id": ticket_id, "customer_id": customer_id, "notes": list(t["notes"])}
        raise ToolError(
            f"Ticket {ticket_id} not found for customer {customer_id}",
            customer_id=customer_id, ticket_id=ticket_id,
        )
