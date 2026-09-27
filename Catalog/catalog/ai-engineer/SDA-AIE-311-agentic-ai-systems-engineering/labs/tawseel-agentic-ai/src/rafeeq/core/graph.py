"""Module 1/3/4 — Rafeeq's core loop as an explicit state machine.

The canonical bounded loop from the instructor package, verbatim in
spirit: `reason` -> conditional `route` -> `reason` again or `END`. No
tools in `build_graph()` (Module 1's skeleton); `build_graph_with_tools()`
adds a `ToolNode` over the governed catalogue (Module 3) and is the graph
Module 4's checkpointer (`memory/short_term.py`) compiles.

TEACHING POINT — bounded by construction: `route` checks BOTH the model's
own "I am done" signal (no more tool calls) AND the step budget. Relying
on the model alone to decide when to stop is not a termination condition,
it is the absence of one (Module 1 mistake #1, the broken-agent postmortem
this whole repo opens with).

LangGraph/langchain-core are Layer-B dependencies (SPEC §1) and are NOT
installed in this build/CI sandbox. This module imports cleanly under
plain python3 regardless: the third-party imports are attempted once at
module load (so `LANGGRAPH_AVAILABLE` can be introspected), but graph
CONSTRUCTION only happens inside `build_graph()` / `build_graph_with_tools()`
— never at import time — and `_require_langgraph()` raises a clear,
actionable error naming the exact pip install line if those functions are
called without the dependency present.
"""
from __future__ import annotations

from typing import Any, Literal

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.state import RafeeqState
from rafeeq.core.llm import get_model

try:  # pragma: no cover - exercised only when langgraph/langchain are installed
    from langgraph.graph import StateGraph, START, END
    from langgraph.prebuilt import ToolNode
    from langchain_core.messages import SystemMessage

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    StateGraph = None  # type: ignore[assignment,misc]
    START = "__start__"  # type: ignore[assignment]
    END = "__end__"  # type: ignore[assignment]
    ToolNode = None  # type: ignore[assignment,misc]
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "This function builds a LangGraph graph and requires `langgraph` and "
    "`langchain-core` (SPEC §1, Layer B). Install them with:\n"
    "    pip install langgraph langchain-core langchain-openai\n"
    "Layer-A code (adapters, tools' *_impl callables, flows/*.py gate "
    "functions, routing.py, fastpath.py) needs none of this and already "
    "runs under plain python3 — see docs/OFFLINE_MODE.md."
)


def _require_langgraph() -> None:
    """Call at the top of every `build_*()` function in this repo's graph
    layer. Raises a clear, actionable `ImportError` instead of a bare
    `ModuleNotFoundError` deep in a third-party import when `langgraph`
    is absent — the whole point of the import-guard rule (SPEC §1)."""
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


_SYSTEM_TEXT = (
    "You are Rafeeq, an operations assistant for Tawseel, a Saudi last-mile "
    "delivery company. Help with orders, deliveries, and refunds. Reply in the "
    "customer's language (Arabic or English)."
)


def reason(state: RafeeqState) -> dict:
    """One reasoning step: ask the model what to do next. Pure at the
    Python level (no graph machinery here) — only the model call and the
    step-count increment, so this function is unit-testable by handing it
    a plain dict (langgraph's TypedDict works as a normal dict) and a
    monkeypatched `get_model`."""
    model = get_model()
    system = SystemMessage(content=_SYSTEM_TEXT) if LANGGRAPH_AVAILABLE else ("system", _SYSTEM_TEXT)
    reply = model.invoke([system, *state["messages"]])
    return {"messages": [reply], "step_count": state["step_count"] + 1}


def route(state: RafeeqState) -> str:
    """Termination logic, explicit and testable — NEVER 'the model
    decides'. Two conditions end the loop: the step budget is exhausted,
    or the last message carries no tool call (a final answer). Both are
    checked here, in code, not hoped for in a prompt."""
    if state["step_count"] >= MAX_STEPS:          # step budget exhausted
        return END
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):         # wants to act -> keep looping
        return "reason"                           # (routes to tools in build_graph_with_tools)
    return END                                    # produced a final answer


def build_graph() -> Any:
    """Module 1's skeleton: reason <-> route, no tools. The buildable
    target of Lab 1."""
    _require_langgraph()
    g = StateGraph(RafeeqState)
    g.add_node("reason", reason)
    g.add_edge(START, "reason")
    g.add_conditional_edges("reason", route)      # the conditional edge = agency
    return g.compile()


def route_with_tools(state: RafeeqState) -> str:
    """Same termination logic as `route`, but names the "tools" branch
    explicitly for `add_conditional_edges`'s mapping — Module 3's ReAct
    shape reused as Rafeeq's default tool-using graph (Module 4 compiles
    this with a checkpointer)."""
    if state["step_count"] >= MAX_STEPS:
        return END
    last = state["messages"][-1]
    return "tools" if getattr(last, "tool_calls", None) else END


def build_graph_with_tools(tools: list[Any] | None = None) -> Any:
    """Module 3/4 — the loop with a `ToolNode` bound over Rafeeq's
    governed tool catalogue. `tools` defaults to
    `rafeeq.tools.registry.ALL_TOOLS` (imported lazily so this module
    never needs the tool modules' own `langchain_core.tools` dependency
    at import time). This is the graph `memory/short_term.py` compiles
    with a checkpointer — compiling with `checkpointer=...` is the caller's
    job (SPEC's Module-4 pattern), not this function's, so the same graph
    definition serves both a synchronous call and a checkpointed thread.
    """
    _require_langgraph()
    if tools is None:
        from rafeeq.tools.registry import ALL_TOOLS

        tools = ALL_TOOLS

    def reason_with_tools(state: RafeeqState) -> dict:
        model = get_model().bind_tools(tools)
        reply = model.invoke([SystemMessage(content=_SYSTEM_TEXT), *state["messages"]])
        return {"messages": [reply], "step_count": state["step_count"] + 1}

    g = StateGraph(RafeeqState)
    g.add_node("reason", reason_with_tools)
    g.add_node("tools", ToolNode(tools))
    g.add_edge(START, "reason")
    g.add_conditional_edges("reason", route_with_tools, {"tools": "tools", END: END})
    g.add_edge("tools", "reason")                 # observation -> reason again
    return g.compile()
