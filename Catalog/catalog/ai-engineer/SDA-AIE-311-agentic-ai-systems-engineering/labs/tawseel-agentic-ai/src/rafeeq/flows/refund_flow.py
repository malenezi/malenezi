"""Module 7 — flow engineering applied to refunds: rules are BRANCHES,
not sentences. Deterministic, testable, free. The model (when this flow
is wired into a fuller agent) is used ONLY to compose the final customer
reply — never to decide eligibility or the amount threshold.

Compare every gate here to `reasoning/refund_prompt_only.py`'s ANTI-
PATTERN: the exact same five rules, as prose there and as uncrossable
code here. `REFUND_LIMIT_SAR`/`AUTO_REFUND_LIMIT_SAR` are imported from
`core.config` — the single source of truth (SPEC §7) — never re-declared.

Three amount bands (SPEC §5's action-risk matrix, `data/policies/en/
refund_eligibility.md`'s "Autonomy thresholds"):

    amount <= AUTO_REFUND_LIMIT_SAR (50)                  -> auto_approve
    AUTO_REFUND_LIMIT_SAR < amount <= REFUND_LIMIT_SAR     -> approve (policy-controlled, logged)
    amount > REFUND_LIMIT_SAR (500)                        -> needs_human

`load_order`, `do_refund`, and `request_human_approval` call the REAL
governed tool `*_impl` callables (`tools/orders.get_order_impl`,
`tools/billing.issue_refund_impl`) — Layer A, no langgraph needed to run
the flow's LOGIC. Only `build_refund_flow()` (wiring these into a
compiled graph) needs `langgraph`/`langchain-core` and is import-guarded;
every gate function below is a plain, pure function of a dict and is
fully unit-testable without it (`tests/unit/test_refund_flow.py`).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal, TypedDict

from rafeeq.core.config import AUTO_REFUND_LIMIT_SAR, REFUND_LIMIT_SAR
from rafeeq.tools.billing import issue_refund_impl
from rafeeq.tools.orders import get_order_impl

try:  # pragma: no cover - exercised only when langgraph is installed
    from langgraph.graph import StateGraph, START, END

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    StateGraph = None  # type: ignore[assignment,misc]
    START = "__start__"  # type: ignore[assignment]
    END = "__end__"  # type: ignore[assignment]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "build_refund_flow() requires `langgraph` (SPEC §1, Layer B). Install "
    "with:\n    pip install langgraph langchain-core\n"
    "Every gate function in this module (load_order, eligibility_gate, "
    "amount_gate, do_refund, request_human_approval) runs today under "
    "plain python3 with no langgraph installed — call them directly."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


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
    """Deterministic fact-gathering — NOT a judgement call. Reads the
    order's amount, SLA-breach flag, and existing-refund flag straight
    from the order-management tool, the single source of truth every gate
    below reads from (never estimated from conversation text — the
    Delivery SLA policy's own instruction, enforced structurally here)."""
    order = get_order_impl(state["order_id"])
    if order.get("error"):
        # Fail closed: an order we cannot even load is not eligible.
        return {"amount": None, "sla_breached": False, "already_refunded": False,
                "order_error": order["error"]}
    return {
        "amount": order["amount_sar"],
        "sla_breached": order["sla_breached"],
        "already_refunded": order["refunded"],
        "order_error": None,
    }


def eligibility_gate(state: RefundState) -> Literal["reject", "decide"]:
    if state.get("already_refunded"):                    # rule -> branch (no model)
        return "reject"                                   # never refund twice (M1 ghost)
    if not state.get("sla_breached"):
        return "reject"                                    # not eligible
    return "decide"


def amount_gate(state: RefundState) -> Literal["auto_approve", "approve", "needs_human"]:
    """THE rule a prompt could not guarantee — now uncrossable structure.
    Three bands, the SPEC §5 autonomous band added on top of the package's
    original two:
        <= AUTO_REFUND_LIMIT_SAR (50)  -> fully autonomous, no gate at all
        <= REFUND_LIMIT_SAR (500)      -> autonomous, policy-controlled, logged
        >  REFUND_LIMIT_SAR (500)      -> human approval required, no exceptions
    """
    amount = state.get("amount") or 0.0
    if amount <= AUTO_REFUND_LIMIT_SAR:
        return "auto_approve"
    if amount <= REFUND_LIMIT_SAR:
        return "approve"
    return "needs_human"


def do_refund(state: RefundState) -> dict:
    """Issue the refund. NOTE — this deliberately calls ONLY
    `issue_refund_impl`, not also `mark_refunded_impl`: the real
    `BillingClient.issue_refund` (unlike the instructor package's
    simplified two-call sketch) already updates the order's refund fields
    itself; `tools/billing.py`'s own docstring is explicit that calling
    `mark_refunded` afterwards double-counts the amount on the order.
    Flow logic follows the REAL bound tool's contract, not an illustrative
    sketch that predates it (SPEC's file paths/tool contracts are
    binding)."""
    idempotency_key = f"refund-flow-{state.get('ticket_id') or state['order_id']}"
    result = issue_refund_impl(
        state["order_id"], float(state.get("amount") or 0.0),
        state.get("reason", "sla_breach"), idempotency_key,
    )
    if result.get("error"):
        return {"decision": "reject", "refund_result": result}
    band = "auto_approve" if result["amount_sar"] <= AUTO_REFUND_LIMIT_SAR else "approve"
    return {"decision": band, "refund_result": result}


def request_human_approval(state: RefundState) -> dict:
    """The `needs_human` path: record an approval request rather than
    silently stopping. This IS the escalation artefact a human approver
    reviews — order id, amount, and why it crossed the threshold — not a
    dead end (the same "escalation must carry full context" discipline
    Module 6 enforces at the supervisor level, applied here at the flow
    level for a single high-stakes action)."""
    request = {
        "order_id": state["order_id"],
        "customer_id": state.get("customer_id", ""),
        "ticket_id": state.get("ticket_id", ""),
        "amount_sar": state.get("amount"),
        "reason": state.get("reason", "sla_breach"),
        "threshold_sar": REFUND_LIMIT_SAR,
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "status": "pending_human_approval",
    }
    _log_approval_request(request)
    return {"decision": "needs_human", "approval_request": request}


def _log_approval_request(request: dict[str, Any]) -> None:
    """Best-effort audit log, same lazy-import pattern as
    `orchestration/delegate.py`'s `_log_handoff` — a missing observability
    layer must never block recording (or blocking on) an approval
    request."""
    try:
        from rafeeq.observability import audit as _audit

        log_fn = getattr(_audit, "log_approval_request", None) or getattr(_audit, "log_event", None)
        if log_fn is None:
            raise ImportError("rafeeq.observability.audit has no approval-request logging entry point yet")
        try:
            log_fn(**request)
        except TypeError:
            log_fn(request)
    except Exception:  # noqa: BLE001 - the approval request itself must still be returned
        import logging

        logging.getLogger("rafeeq.flows.refund_flow").info("refund approval request: %s", request)


def build_refund_flow() -> Any:
    _require_langgraph()
    g = StateGraph(RefundState)
    g.add_node("load", load_order)
    g.add_node("refund", do_refund)
    g.add_node("needs_human", request_human_approval)
    g.add_edge(START, "load")
    g.add_conditional_edges("load", eligibility_gate, {"reject": END, "decide": "amount_check"})
    g.add_node("amount_check", lambda s: {})              # pure branch point
    g.add_conditional_edges("amount_check", amount_gate, {
        "auto_approve": "refund", "approve": "refund", "needs_human": "needs_human",
    })
    g.add_edge("refund", END)
    g.add_edge("needs_human", END)
    return g.compile()
