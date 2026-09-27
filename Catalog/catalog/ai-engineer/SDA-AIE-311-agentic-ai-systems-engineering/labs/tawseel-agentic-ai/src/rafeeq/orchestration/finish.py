"""Module 6 — aggregation and clean escalation: the supervisor's two exits.

`aggregate` composes possibly-several specialist results into ONE
coherent customer-facing reply — the customer sees a single conversation,
never a stitched-together transcript of internal handoffs. `escalate` is
a FIRST-CLASS outcome (Module 6 §5), never a dead end: it carries the
full trace/state to a human queue (best-effort through
`rafeeq.observability.audit`, same lazy-import pattern as `delegate.py`)
and tells the customer plainly, bilingually, that a person is taking
over.

Layer B: both functions call `get_model()` (fine, offline-safe — the
default `StubChatModel`, SPEC §2) but are written as plain graph-node
functions; nothing here strictly requires langgraph to RUN (you can call
`aggregate({...})` directly against a dict), only `orchestration.supervisor
.build_supervisor_graph()` requires it to WIRE them into a compiled graph.
"""
from __future__ import annotations

from typing import Any

try:  # pragma: no cover - exercised only when langchain-core is installed
    from langchain_core.messages import SystemMessage, AIMessage
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    from dataclasses import dataclass as _dataclass

    @_dataclass
    class SystemMessage:  # type: ignore[no-redef]
        content: str
        type: str = "system"

    @_dataclass
    class AIMessage:  # type: ignore[no-redef]
        content: str
        type: str = "ai"

from rafeeq.core.llm import get_model

AGGREGATE_SYSTEM_TEXT = (
    "Compose ONE clear reply to the customer in their language from these "
    "specialist results."
)

ESCALATE_MESSAGE_EN = (
    "Sorry — I'm handing this to a specialist colleague who has your full "
    "case and will follow up shortly."
)
ESCALATE_MESSAGE_AR = (
    "عذرًا — سأحوّل حالتك إلى زميل مختص لديه كامل تفاصيلها وسيتابع معك قريبًا."
)


def aggregate(state: dict) -> dict:
    """One coherent reply from possibly several specialists' results."""
    summary = get_model().invoke([SystemMessage(content=AGGREGATE_SYSTEM_TEXT), *state["messages"]])
    return {"messages": [summary], "resolution": "resolved"}


def _log_escalation(ticket_id: str, state: dict) -> None:
    """Best-effort full-context log to the human queue. Lazy import of
    `rafeeq.observability.audit` (may not exist yet — see `delegate.py`
    for the identical rationale); an escalation MUST still happen even if
    logging it fails, but a logging failure here is worth surfacing
    loudly in the fallback path since an unlogged escalation is closer to
    a compliance gap than an unlogged handoff."""
    try:
        from rafeeq.observability import audit as _audit

        log_fn = getattr(_audit, "log_escalation", None) or getattr(_audit, "log_event", None)
        if log_fn is None:
            raise ImportError("rafeeq.observability.audit has no escalation logging entry point yet")
        try:
            log_fn(ticket_id=ticket_id, state=state)
        except TypeError:
            log_fn({"ticket_id": ticket_id, "state": state})
    except Exception:  # noqa: BLE001 - escalation must still complete
        import logging

        logging.getLogger("rafeeq.orchestration.finish").warning(
            "escalation (audit logging unavailable): ticket=%s state=%s", ticket_id, state,
        )


def escalate(state: dict) -> dict:
    """Hand to a human WITH the full trace and state — never a dead end."""
    _log_escalation(state.get("ticket_id", ""), state)   # full context to the human queue
    msg = ESCALATE_MESSAGE_EN if state.get("locale") == "en" else ESCALATE_MESSAGE_AR
    return {"messages": [AIMessage(content=msg)], "resolution": "escalated"}
