"""Module 6 — the delegation node: scoped handoff + mandatory write-back.

Every handoff is scoped (`agents.scoping.scoped_input` — a PDPL control,
Module 5) and LOGGED (best-effort through `rafeeq.observability.audit`,
which may not exist yet in this build — see the lazy-import fallback
below, the same pattern `security/authz.py` uses for its own denial log).
Every specialist result is written back into shared state before the
supervisor is asked to decide again — the fix for the classic "lost
handoff" bug (Module 6 §3): a specialist that ran and produced a result
the customer never sees is worse than not delegating at all.

Layer B (the specialist agents this delegates to are LangGraph agents);
import-guarded. `make_delegate`'s returned closure is the graph NODE;
nothing in this file can usefully run without langgraph, since there is
no specialist agent to invoke without it.
"""
from __future__ import annotations

from typing import Any, Callable

from rafeeq.agents.scoping import scoped_input

try:  # pragma: no cover - exercised only when langgraph is installed
    import langgraph  # noqa: F401

    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "make_delegate() builds a node that invokes a LangGraph specialist "
    "agent and requires `langgraph` + `langchain-core` (SPEC §1, Layer B). "
    "Install with:\n    pip install langgraph langchain-core"
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


def _log_handoff(ticket_id: str, to: str, subgoal: str) -> None:
    """Best-effort attributable-event log. `rafeeq.observability.audit`
    is owned by a different part of this build and may not exist yet (or
    may expose a different function name) — this import is LAZY and
    broadly caught, exactly like `security/authz.py`'s `_log_denial`, so a
    missing observability layer never blocks a handoff from happening."""
    try:
        from rafeeq.observability import audit as _audit

        log_fn = getattr(_audit, "log_handoff", None) or getattr(_audit, "log_event", None)
        if log_fn is None:
            raise ImportError("rafeeq.observability.audit has no handoff logging entry point yet")
        try:
            log_fn(ticket_id=ticket_id, to=to, subgoal=subgoal)
        except TypeError:
            log_fn({"ticket_id": ticket_id, "to": to, "subgoal": subgoal})
    except Exception:  # noqa: BLE001 - logging must never break a handoff
        import logging

        logging.getLogger("rafeeq.orchestration.delegate").info(
            "handoff: ticket=%s to=%s subgoal=%s", ticket_id, to, subgoal,
        )


def make_delegate(name: str) -> Callable[[dict], dict]:
    """Build the delegate node for specialist `name`. Returns a closure
    (the graph node function) rather than a bound method so
    `build_supervisor_graph` can register one per specialist without a
    class hierarchy — a plain function is enough structure here."""
    _require_langgraph()
    from rafeeq.agents.specialist import SPECIALIST_BUILDERS

    if name not in SPECIALIST_BUILDERS:
        raise KeyError(f"no specialist builder registered for {name!r}")
    build_agent = SPECIALIST_BUILDERS[name]

    def delegate(state: dict) -> dict:
        payload = scoped_input(state, name)          # PDPL-scoped context only
        _log_handoff(state.get("ticket_id", ""), to=name, subgoal=state.get("subgoal", ""))
        agent = build_agent()                        # built once, cached (specialist.py)
        result = agent.invoke(payload)                # the specialist runs
        answer = result["messages"][-1]
        # MANDATORY write-back — without this the handoff is 'lost'. The
        # specialist's answer becomes part of shared state (so `finish.py`
        # can aggregate it) AND `last_result` (so a caller can inspect
        # exactly what each specialist said, per-name, not just the last
        # message in a merged stream).
        return {
            "messages": [answer],
            "last_result": {**state.get("last_result", {}), name: answer.content},
            "handoff_count": state.get("handoff_count", 0) + 1,
        }

    return delegate
