"""Lab 1, Task 3 — implement `reason`, `route`, and `build_graph`.

Fill in the TODOs. `MAX_STEPS` is imported from `rafeeq.core.config` —
never re-declare the constant yourself (SPEC §7: policy numbers live in
ONE place). When you are done, `route` must satisfy BOTH termination
conditions: budget exhausted -> END, and no pending tool call -> END.
Getting only one of the two right reproduces exactly one of the two
troubleshooting rows below.

Troubleshooting (copy from the lab README, kept here for quick reference
while you code):

| Symptom | Cause | Fix |
|---|---|---|
| `GraphRecursionError` | `route` never returns `END` | budget AND goal branches must both reach `END` |
| Agent never loops | `route` always returns `END` | only terminate when no pending tool call AND budget remains |
| State update ignored | a node returns a full state instead of a partial dict | nodes return only the keys they change |

Compare your finished file against `src/rafeeq/core/graph.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.llm import get_model

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
    "build_graph() needs `langgraph` + `langchain-core` (SPEC §1, Layer B). "
    "Install with:\n    pip install langgraph langchain-core\n"
    "`route(state)` needs neither and is unit-testable on a plain dict — "
    "see labs/lab01/start/test_termination.py, Task 5."
)

_SYSTEM_TEXT = (
    "You are Rafeeq, an operations assistant for Tawseel, a Saudi last-mile "
    "delivery company. Help with orders, deliveries, and refunds. Reply in the "
    "customer's language (Arabic or English)."
)


def reason(state: dict) -> dict:
    """TODO(lab 1.3a): one reasoning step.

    1. Get a model via `get_model()`.
    2. Call `model.invoke([system, *state["messages"]])` where `system` is
       a `SystemMessage(content=_SYSTEM_TEXT)` when LANGGRAPH_AVAILABLE,
       else the tuple `("system", _SYSTEM_TEXT)` (StubChatModel accepts
       both shapes — see `rafeeq.core.llm._message_text`).
    3. Return a PARTIAL state update: `{"messages": [reply], "step_count":
       state["step_count"] + 1}` — NEVER the whole state (see the
       troubleshooting row "State update ignored" above).
    """
    raise NotImplementedError("TODO(lab 1.3a): implement reason()")


def route(state: dict) -> str:
    """TODO(lab 1.3b): the termination logic. Two conditions end the loop
    and BOTH must reach `END`:

    1. `state["step_count"] >= MAX_STEPS` -> budget exhausted -> END.
    2. The last message carries no `tool_calls` -> a final answer -> END.

    Otherwise (budget remains AND the model wants to act) -> "reason"
    (keep looping). Never rely on "the model decides when it's done" as
    the ONLY condition — that is Module 1 Mini-Exercise Q5's trap answer.
    """
    raise NotImplementedError("TODO(lab 1.3b): implement route()")


def build_graph() -> Any:
    """TODO(lab 1.3c): wire START -> reason -> (conditional via `route`) ->
    reason / END. Use `StateGraph`, `add_node`, `add_edge(START, "reason")`,
    `add_conditional_edges("reason", route)`, then `.compile()`.
    """
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)
    raise NotImplementedError("TODO(lab 1.3c): implement build_graph()")
