"""Module 6 — the THIN supervisor: routes and aggregates, never does
domain work itself (the "fat supervisor" mistake, named and avoided).

Bounded as a system, not just per-agent: `state["handoff_count"] >=
MAX_HANDOFFS` (the SAME global budget imported from `core.config` — never
re-declared as a bare literal, SPEC §7) forces `escalate` before the
router is even asked, so a chatter loop across specialists cannot outrun
the budget by winning the race to route first.

Layer B: `StateGraph`/`langchain_core.messages` are needed to WIRE the
graph and to call a real routing model; import-guarded. `route(state)` —
the conditional-edge function — is pure enough to unit-test directly on a
plain dict with no langgraph installed (it only reads `state["route"]`).
"""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel

from rafeeq.core.config import MAX_HANDOFFS
from rafeeq.core.llm import get_model
from rafeeq.core.state import RafeeqState

try:  # pragma: no cover - exercised only when langgraph/langchain are installed
    from langgraph.graph import StateGraph, START, END
    from langchain_core.messages import SystemMessage

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    StateGraph = None  # type: ignore[assignment,misc]
    START = "__start__"  # type: ignore[assignment]
    END = "__end__"  # type: ignore[assignment]
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "build_supervisor_graph() requires `langgraph` and `langchain-core` "
    "(SPEC §1, Layer B). Install with:\n    pip install langgraph langchain-core\n"
    "`route(state)` (the conditional-edge function) needs neither and is "
    "already unit-testable against a plain dict."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


SPECIALIST_NAMES: tuple[str, ...] = ("orders", "logistics", "billing")

ROUTER_SYSTEM_TEXT = (
    "You route Tawseel tickets. Specialists: orders (lookup/status), "
    "logistics (tracking/reschedule), billing (invoices/refunds). "
    "Choose the next specialist, or 'finish' if resolved, or 'escalate' "
    "if no specialist can help. Given prior results, avoid re-routing to "
    "an agent that already answered."
)


class Route(BaseModel):
    target: Literal["orders", "logistics", "billing", "finish", "escalate"]
    subgoal: str                                  # explicit sub-goal for the handoff


def supervise(state: RafeeqState) -> dict:
    """Decide the next specialist, or finish, or escalate. NO domain work
    here — a supervisor that calls a tool itself has stopped being thin
    (Module 6's central "common mistake")."""
    if state["handoff_count"] >= MAX_HANDOFFS:    # global budget -> escalate, never loop
        return {"route": "escalate"}
    router = get_model().with_structured_output(Route)
    system = SystemMessage(content=ROUTER_SYSTEM_TEXT) if LANGGRAPH_AVAILABLE else ("system", ROUTER_SYSTEM_TEXT)
    decision = router.invoke([system, *state["messages"]])
    return {"route": decision.target, "subgoal": decision.subgoal}


def route(state: RafeeqState) -> str:
    """The conditional-edge function. Deliberately trivial (`state["route"]`
    already holds the decision `supervise` made) — kept as its own
    function, not inlined, so `add_conditional_edges` has a name to point
    at and a test can call it directly with `{"route": "billing"}` and no
    langgraph installed."""
    return state["route"]                         # 'orders'|'logistics'|'billing'|'finish'|'escalate'


def build_supervisor_graph() -> Any:
    """Wire `supervise` -> (specialist delegate | finish | escalate) ->
    back to `supervise`, per Module 6's hub-and-spoke topology.
    Specialists never talk to each other directly — every edge in this
    graph either enters or leaves the `supervise` hub."""
    _require_langgraph()
    from rafeeq.orchestration.delegate import make_delegate
    from rafeeq.orchestration.finish import aggregate, escalate

    g = StateGraph(RafeeqState)
    g.add_node("supervise", supervise)
    for name in SPECIALIST_NAMES:
        g.add_node(name, make_delegate(name))
        g.add_edge(name, "supervise")             # specialist result -> supervisor decides again
    g.add_node("finish", aggregate)
    g.add_node("escalate", escalate)

    g.add_edge(START, "supervise")
    g.add_conditional_edges("supervise", route, {
        "orders": "orders", "logistics": "logistics", "billing": "billing",
        "finish": "finish", "escalate": "escalate",
    })
    g.add_edge("finish", END)
    g.add_edge("escalate", END)
    return g.compile()
