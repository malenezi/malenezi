"""Lab 6, Tasks 1/3 — the THIN supervisor: routes and aggregates, never
does domain work itself.

Fill in the TODOs. `route(state)` must be a PURE function of
`state["route"]` so it is unit-testable with a plain dict, no langgraph
needed — exactly the same discipline as Lab 1's `route()`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_HANDOFFS
from rafeeq.core.llm import get_model

try:
    from langchain_core.messages import SystemMessage

    LANGGRAPH_AVAILABLE = True
except ImportError:
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

ROUTER_SYSTEM_TEXT = (
    "You are Rafeeq's supervisor. Decide the next specialist (orders, logistics, "
    "billing), or finish, or escalate. State an explicit subgoal for the handoff."
)


class Route(BaseModel):
    target: Literal["orders", "logistics", "billing", "finish", "escalate"]
    subgoal: str


def supervise(state: dict) -> dict:
    """TODO(lab 6.1): decide the next hop. NO domain work here — a
    supervisor that calls a tool itself has stopped being thin (the
    troubleshooting row "supervisor calls tools itself 'to save a hop'").

    1. If `state.get("handoff_count", 0) >= MAX_HANDOFFS`: return
       `{"route": "escalate"}` IMMEDIATELY — the global budget must win
       the race even before a routing model is asked (this is what makes
       a chatter loop provably bounded, not just usually bounded).
    2. Otherwise, `router = get_model().with_structured_output(Route)`;
       `decision = router.invoke([system, *state["messages"]])`; return
       `{"route": decision.target, "subgoal": decision.subgoal}`.
    """
    raise NotImplementedError("TODO(lab 6.1): implement supervise")


def route(state: dict) -> str:
    """TODO(lab 6.3 — the conditional-edge function): trivially return
    `state["route"]`. Deliberately its OWN function (not inlined into
    `supervise`) so it is testable with a plain `{"route": "billing"}`
    dict and no langgraph installed.
    """
    raise NotImplementedError("TODO(lab 6.3): implement route")
