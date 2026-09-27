"""Lab 7, Task 3 — refund logic as a typed, branching flow, not a prompt.

Compare every gate you write here against
`src/rafeeq/reasoning/refund_prompt_only.py`'s prose version of the exact
same five rules. Fill in the TODOs. Everything below is Layer A (plain
python3, no langgraph) except `build_refund_flow()` itself.
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal, TypedDict

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import AUTO_REFUND_LIMIT_SAR, REFUND_LIMIT_SAR
from rafeeq.tools.billing import issue_refund_impl
from rafeeq.tools.orders import get_order_impl


class RefundState(TypedDict, total=False):
    order_id: str
    customer_id: str
    locale: Literal["ar", "en"]
    ticket_id: str
    reason: str
    amount: float | None
    sla_breached: bool | None
    already_refunded: bool | None
    order_error: str | None
    decision: Literal["auto_approve", "approve", "needs_human", "reject", None]
    refund_result: dict[str, Any] | None
    approval_request: dict[str, Any] | None


def load_order(state: RefundState) -> dict:
    """TODO(lab 7.3a): deterministic fact-gathering, NOT judgement. Call
    `get_order_impl(state["order_id"])`. On `{"error": ...}`, fail
    CLOSED: return `{"amount": None, "sla_breached": False,
    "already_refunded": False, "order_error": <the error>}`. On success,
    return `{"amount": order["amount_sar"], "sla_breached":
    order["sla_breached"], "already_refunded": order["refunded"],
    "order_error": None}`.
    """
    raise NotImplementedError("TODO(lab 7.3a): implement load_order")


def eligibility_gate(state: RefundState) -> Literal["reject", "decide"]:
    """TODO(lab 7.3b): rule -> branch, no model call. Return `"reject"`
    if `state.get("already_refunded")` is true (never refund twice) OR
    `state.get("sla_breached")` is falsy (not eligible). Otherwise
    `"decide"`.
    """
    raise NotImplementedError("TODO(lab 7.3b): implement eligibility_gate")


def amount_gate(state: RefundState) -> Literal["auto_approve", "approve", "needs_human"]:
    """TODO(lab 7.3c): THE rule a prompt could not guarantee, now
    uncrossable. `amount = state.get("amount") or 0.0`:

        amount <= AUTO_REFUND_LIMIT_SAR (50)   -> "auto_approve"
        amount <= REFUND_LIMIT_SAR (500)       -> "approve"
        amount >  REFUND_LIMIT_SAR             -> "needs_human"

    Import BOTH constants from `rafeeq.core.config` — never re-declare
    the numbers (SPEC §7). This is the branch that makes the adversarial
    "ignore the limit" ticket from Task 1 impossible to talk past.
    """
    raise NotImplementedError("TODO(lab 7.3d): implement amount_gate")


def do_refund(state: RefundState) -> dict:
    """TODO(lab 7.3e): issue the refund via `issue_refund_impl`. Build a
    STABLE idempotency key (e.g. `f"lab7-refund-{state.get('ticket_id')
    or state['order_id']}"` — never a fresh random key on every call, or
    you defeat the idempotency protection). Call `issue_refund_impl(
    state["order_id"], float(state.get("amount") or 0.0),
    state.get("reason", "sla_breach"), idempotency_key)`. On
    `result.get("error")`, return `{"decision": "reject",
    "refund_result": result}`. Otherwise return `{"decision":
    "auto_approve" if result["amount_sar"] <= AUTO_REFUND_LIMIT_SAR else
    "approve", "refund_result": result}`.
    """
    raise NotImplementedError("TODO(lab 7.3e): implement do_refund")


def request_human_approval(state: RefundState) -> dict:
    """TODO(lab 7.3f): the `needs_human` path — an escalation ARTEFACT, not
    a dead end. Build and return `{"decision": "needs_human",
    "approval_request": {"order_id": ..., "customer_id": ...,
    "ticket_id": ..., "amount_sar": state.get("amount"), "reason": ...,
    "threshold_sar": REFUND_LIMIT_SAR, "requested_at": <iso timestamp>,
    "status": "pending_human_approval"}}`.
    """
    raise NotImplementedError("TODO(lab 7.3f): implement request_human_approval")
