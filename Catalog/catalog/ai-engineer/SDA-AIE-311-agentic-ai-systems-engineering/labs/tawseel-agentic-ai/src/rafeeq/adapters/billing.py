"""Module 3/7/8 — Billing mock adapter.

`issue_refund` is the single most important method in this repo's mock
backends: it is deliberately IDEMPOTENT BY KEY and records every attempt,
because the double-refund lesson (Module 1's case study, Module 7's flow
gates) depends on the tool itself refusing to pay twice — not on the agent
"remembering" it already refunded. An agent architecture can still be
buggy and re-enter the refund branch; the backend must be the last line of
defence, exactly like a real payments API's idempotency-key contract.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from rafeeq.adapters.store import store
from rafeeq.core.config import REFUND_LIMIT_SAR
from rafeeq.core.errors import ToolError


@dataclass(frozen=True)
class PaymentRecord:
    """Mirrors the payment record shape in SPEC §4 exactly."""

    payment_id: str
    order_id: str
    customer_id: str
    amount_sar: float
    method: str
    status: str
    captured_at: str | None
    refunds: list[dict[str, Any]]

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "PaymentRecord":
        return cls(**{f: d.get(f) for f in cls.__dataclass_fields__})


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    order_id: str
    customer_id: str
    issued_at: str
    amount_sar: float
    currency: str
    items: int
    payment_status: str
    method: str


class BillingClient:
    """Mock of Tawseel's billing/payments system."""

    def get_payment(self, payment_id: str) -> PaymentRecord:
        raw = store.get_payment(payment_id)
        if raw is None:
            raise ToolError(f"Payment {payment_id} not found", payment_id=payment_id)
        return PaymentRecord.from_dict(raw)

    def get_invoice(self, order_id: str) -> Invoice:
        order = store.get_order(order_id)
        if order is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        payment = store.get_payment_for_order(order_id)
        return Invoice(
            invoice_id=f"INV-{order_id.split('-')[-1]}",
            order_id=order_id,
            customer_id=order["customer_id"],
            issued_at=order["placed_at"],
            amount_sar=order["amount_sar"],
            currency=order.get("currency", "SAR"),
            items=order.get("items", 1),
            payment_status=payment["status"] if payment else "unknown",
            method=payment["method"] if payment else "unknown",
        )

    def issue_refund(
        self,
        order_id: str,
        amount_sar: float,
        reason: str,
        idempotency_key: str,
    ) -> dict[str, Any]:
        """Refund `amount_sar` for `order_id`. Calling this twice with the
        SAME `idempotency_key` returns the ORIGINAL result and issues no
        second payment — this is the control, not the agent's judgement.
        A different `idempotency_key` for the same order is a genuinely new
        refund attempt (e.g. a second, separate goodwill credit) and is
        allowed, subject to the order's remaining refundable balance.

        Autonomy per SPEC §5's action-risk matrix is enforced by the
        CALLER (security/action_risk.py + flows/refund_flow.py) — this
        adapter enforces only backend-level invariants: idempotency and
        "cannot refund more than was paid".
        """
        # 1. Idempotency check FIRST — before touching any state.
        existing = store.refund_ledger.get(idempotency_key)
        if existing is not None:
            return {**existing, "idempotent_replay": True}

        order = store.get_order(order_id)
        if order is None:
            raise ToolError(f"Order {order_id} not found", order_id=order_id)
        payment = store.get_payment_for_order(order_id)
        if payment is None:
            raise ToolError(f"No payment found for order {order_id}", order_id=order_id)

        already_refunded = float(order.get("refund_amount_sar", 0.0) or 0.0)
        remaining = round(float(payment["amount_sar"]) - already_refunded, 2)
        if amount_sar <= 0:
            raise ToolError("Refund amount must be positive", order_id=order_id, amount_sar=amount_sar)
        if amount_sar > remaining + 1e-6:
            raise ToolError(
                f"Refund amount {amount_sar} exceeds remaining refundable balance {remaining}",
                order_id=order_id, amount_sar=amount_sar, remaining_sar=remaining,
            )

        now = datetime.now(timezone.utc).isoformat()
        refund_event = {
            "amount_sar": round(amount_sar, 2), "reason": reason,
            "idempotency_key": idempotency_key, "issued_at": now,
            "requires_human_approval": amount_sar > REFUND_LIMIT_SAR,
        }
        payment.setdefault("refunds", []).append(refund_event)
        new_total_refunded = round(already_refunded + amount_sar, 2)
        payment["status"] = "refunded" if abs(new_total_refunded - payment["amount_sar"]) < 1e-6 else "partially_refunded"

        # Order-side mirror (kept consistent with the payment side here so
        # a caller inspecting either sees the same truth).
        order["refunded"] = True
        order["refund_amount_sar"] = new_total_refunded

        result = {
            "order_id": order_id,
            "payment_id": payment["payment_id"],
            "amount_sar": round(amount_sar, 2),
            "reason": reason,
            "idempotency_key": idempotency_key,
            "issued_at": now,
            "total_refunded_sar": new_total_refunded,
            "payment_status": payment["status"],
            "idempotent_replay": False,
        }
        store.refund_ledger[idempotency_key] = result
        return result
