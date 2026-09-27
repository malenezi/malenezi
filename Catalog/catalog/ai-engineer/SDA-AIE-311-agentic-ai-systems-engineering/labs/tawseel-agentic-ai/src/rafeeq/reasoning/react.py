"""Module 2 — ReAct: reasoning and acting interleaved.

Two implementations, deliberately side by side, because the module's
research note (SPEC §6, Yao et al.) asks participants to build ReAct
EXPLICITLY before an abstraction (LangGraph) hides the control flow:

1. `build_react_agent()` — the instructor package's shape: Module 1's
   loop plus a `ToolNode`, reasoning and acting interleaved via a
   conditional edge. Layer B (needs langgraph); import-guarded.

2. `react_loop_explicit()` — a framework-free thought -> action ->
   observation loop, hand-rolled against the plain `*_impl` tool
   callables. Layer A: runs under plain python3, no langgraph required.
   Every step is a printed trace line (`Thought:` / `Action:` /
   `Observation:`) so the control flow ReAct describes is visible, not
   hidden inside a library. `count_redundant_tool_calls` measures the
   exact failure mode Module 2 calls "thrashing" — the same tool called
   with the same arguments twice, which is wasted cost a supervised ReAct
   loop should not have paid.

TEACHING POINT: build the explicit version FIRST. Only once the loop's
shape is boring and obvious should Module 3+'s `ToolNode`/`bind_tools`
abstraction feel like a convenience rather than a magic trick.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Callable

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.llm import get_model
from rafeeq.core.state import RafeeqState

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
    "build_react_agent() requires `langgraph` and `langchain-core` (SPEC §1, "
    "Layer B). Install with:\n    pip install langgraph langchain-core\n"
    "For an offline, framework-free ReAct loop that runs under plain python3, "
    "use `react_loop_explicit()` instead — it needs no third-party dependency."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


REACT_SYSTEM_TEXT = (
    "You are Rafeeq. Reason step by step. Use a tool when you need a fact you "
    "do not have; otherwise give the final answer. Never guess an order status."
)


def build_react_agent(tools: list[Any] | None = None) -> Any:
    """The instructor package's shape: Module 1 loop + a tools node,
    reasoning and acting interleaved until a final answer (no tool call)
    is produced. `tools` defaults to `rafeeq.tools.tawseel.TOOLS` — the
    package's own worked example — imported lazily so this module never
    needs `langchain_core.tools` at import time."""
    _require_langgraph()
    if tools is None:
        from rafeeq.tools.tawseel import TOOLS

        tools = TOOLS

    def reason(state: RafeeqState) -> dict:
        model = get_model().bind_tools(tools)
        reply = model.invoke([SystemMessage(content=REACT_SYSTEM_TEXT), *state["messages"]])
        return {"messages": [reply], "step_count": state["step_count"] + 1}

    def route(state: RafeeqState) -> str:
        if state["step_count"] >= MAX_STEPS:      # budget (Module 1 discipline)
            return END
        return "tools" if getattr(state["messages"][-1], "tool_calls", None) else END

    g = StateGraph(RafeeqState)
    g.add_node("reason", reason)
    g.add_node("tools", ToolNode(tools))
    g.add_edge(START, "reason")
    g.add_conditional_edges("reason", route, {"tools": "tools", END: END})
    g.add_edge("tools", "reason")                 # observation -> reason again
    return g.compile()


# --------------------------------------------------------------------------
# react_loop_explicit — the framework-free version. Layer A: no langgraph,
# no langchain-core. Drives the SAME `*_impl` tool callables every other
# Layer-A module in this repo uses, via `get_model()` (stub by default) for
# the "which tool, what args" decision, then dispatches and prints the
# thought/action/observation trace by hand.
# --------------------------------------------------------------------------

# name -> the plain callable a real ReAct step would invoke. Imported lazily
# (function body, not module level) so this module never forces a load of
# every domain tool module just to be imported.
def _default_tool_impls() -> dict[str, Callable[..., dict]]:
    from rafeeq.tools.billing import get_invoice_impl, issue_refund_impl
    from rafeeq.tools.logistics import reschedule_delivery_impl, track_shipment_impl

    return {
        "track_shipment": lambda args: track_shipment_impl(args.get("order_id", "")),
        "issue_refund": lambda args: issue_refund_impl(
            args.get("order_id", ""), float(args.get("amount_sar", 0.0) or 0.0),
            args.get("reason", "customer_requested"),
            args.get("idempotency_key") or f"react-{args.get('order_id', '')}",
        ),
        "reschedule_delivery": lambda args: reschedule_delivery_impl(
            args.get("order_id", ""), args.get("new_promised_at_iso", ""),
        ),
        "get_invoice": lambda args: get_invoice_impl(args.get("order_id", "")),
    }


def _looks_arabic(text: str) -> bool:
    return any("؀" <= ch <= "ۿ" for ch in text)


def _summarise_observation(tool_name: str, observation: dict[str, Any], arabic: bool) -> str:
    """Deterministic, bilingual final-answer composition from a
    successful tool observation — the one piece of "judgement" this
    offline loop needs, kept simple and template-based on purpose (the
    stub model, SPEC §2, cannot compose free text grounded in a dict; a
    live model tier would replace this whole branch with a real
    generation call over the same observation)."""
    order_id = observation.get("order_id", "")
    if tool_name == "track_shipment":
        status = observation.get("status", "?")
        eta = observation.get("eta") or observation.get("eta_iso")
        if arabic:
            return f"طلبك {order_id}: {status}." + (f" الوصول المتوقع: {eta}." if eta else "")
        return f"Order {order_id} status: {status}." + (f" ETA: {eta}." if eta else "")
    if tool_name == "issue_refund":
        amount = observation.get("amount_sar")
        if arabic:
            return f"تم إصدار استرداد بقيمة {amount} ريال لطلبك {order_id}."
        return f"A refund of {amount} SAR has been issued for order {order_id}."
    if tool_name == "reschedule_delivery":
        new_at = observation.get("promised_at_after")
        if arabic:
            return f"تم تأجيل موعد توصيل طلبك {order_id} إلى {new_at}."
        return f"Delivery for order {order_id} has been rescheduled to {new_at}."
    if tool_name == "get_invoice":
        amount = observation.get("amount_sar")
        if arabic:
            return f"مبلغ فاتورة طلبك {order_id} هو {amount} ريال."
        return f"Invoice for order {order_id}: {amount} SAR."
    return str(observation)


@dataclass
class ReactTraceStep:
    step: int
    thought: str
    action: str | None
    action_input: dict
    observation: Any


@dataclass
class ReactTrace:
    """The explicit loop's full record. `redundant_tool_calls` is the
    Module 2 measurement the SPEC's research note asks for — the count of
    tool calls that were unnecessary (same tool, same args, seen before)."""

    objective: str
    steps: list[ReactTraceStep] = field(default_factory=list)
    final_answer: str = ""
    step_count: int = 0
    terminated_reason: str = "final_answer"        # or "step_budget_exhausted"
    redundant_tool_calls: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "objective": self.objective,
            "steps": [
                {"step": s.step, "thought": s.thought, "action": s.action,
                 "action_input": s.action_input, "observation": s.observation}
                for s in self.steps
            ],
            "final_answer": self.final_answer,
            "step_count": self.step_count,
            "terminated_reason": self.terminated_reason,
            "redundant_tool_calls": self.redundant_tool_calls,
        }


def count_redundant_tool_calls(trace: ReactTrace | list[dict[str, Any]]) -> int:
    """Count UNNECESSARY tool calls in a trace: the same tool name called
    with the exact same arguments more than once. The first occurrence of
    any (name, args) pair is legitimate; every repeat after it is the
    "thrashing" failure mode Module 2 names — wasted cost that a
    well-behaved ReAct loop should not have paid, because the observation
    from the first call should already have answered the question.

    Accepts either a `ReactTrace` or the raw list of step dicts (so a
    trace recorded by another caller, e.g. `compare.py`, can be scored the
    same way without constructing a `ReactTrace`).
    """
    steps = trace.steps if isinstance(trace, ReactTrace) else trace
    seen: set[tuple[str, str]] = set()
    redundant = 0
    for step in steps:
        action = step.action if isinstance(step, ReactTraceStep) else step.get("action")
        args = step.action_input if isinstance(step, ReactTraceStep) else step.get("action_input")
        if not action:
            continue
        key = (action, json.dumps(args, sort_keys=True, default=str))
        if key in seen:
            redundant += 1
        else:
            seen.add(key)
    return redundant


def react_loop_explicit(
    objective: str,
    *,
    max_steps: int = MAX_STEPS,
    tool_impls: dict[str, Callable[..., dict]] | None = None,
    verbose: bool = True,
) -> ReactTrace:
    """Run ReAct BY HAND: thought -> action -> observation, repeat, against
    the plain `*_impl` tools — no langgraph, no ToolNode, no bind_tools
    magic. `objective` is the customer's message (e.g. "أين طلبي رقم
    TW-2026-88120؟"). Each step is printed when `verbose=True` so the
    control flow is visible exactly as the ReAct paper describes it,
    before Module 3+ hides it behind a graph abstraction.

    Uses `get_model()` (the `StubChatModel` by default — SPEC §2) purely
    as the "what tool, what args" decision function; the loop's shape
    (call model -> dispatch -> observe -> repeat -> stop) is entirely this
    function's own code, not delegated to any framework.
    """
    impls = tool_impls or _default_tool_impls()
    tool_specs = [{"name": name} for name in impls]   # StubChatModel only needs .name

    messages: list[Any] = [("human", objective)]
    trace = ReactTrace(objective=objective)

    for step_no in range(1, max_steps + 1):
        model = get_model().bind_tools(tool_specs)
        reply = model.invoke([("system", REACT_SYSTEM_TEXT), *messages])

        if not reply.tool_calls:
            trace.final_answer = reply.content
            trace.step_count = step_no - 1
            trace.terminated_reason = "final_answer"
            if verbose:
                print(f"[react] step {step_no}: Thought: task resolved -> final answer")
                print(f"[react] Final answer: {reply.content}")
            return _finalise(trace)

        call = reply.tool_calls[0]                    # ReAct: one action per step
        name, args = call["name"], call.get("args", {})
        thought = f"I need '{name}' to make progress on: {objective!r}"
        if verbose:
            print(f"[react] step {step_no}: Thought: {thought}")
            print(f"[react] step {step_no}: Action: {name}({args})")

        impl = impls.get(name)
        observation = impl(args) if impl is not None else {"error": "unknown_tool", "tool": name}
        if verbose:
            print(f"[react] step {step_no}: Observation: {observation}")

        trace.steps.append(ReactTraceStep(step=step_no, thought=thought, action=name,
                                           action_input=dict(args), observation=observation))
        # The observation MUST be written back into the message history —
        # this is exactly the fix for the `sim-react-thrash` failure mode
        # (Module 2's lab): an observation never added to state is why a
        # naive loop calls the same tool again believing nothing happened.
        messages.append(("ai", f"{name}({args})"))
        messages.append(("tool", json.dumps(observation, default=str)))

        if isinstance(observation, dict) and not observation.get("error"):
            # The stub model (SPEC §2) has no real judgement about whether
            # an observation answers the objective — it would otherwise
            # re-emit the SAME tool call forever (every ticket would hit
            # the step budget, which is a StubChatModel limitation, not a
            # ReAct one). A successful, error-free observation is treated
            # as sufficient to answer: this function's own code decides to
            # stop and compose the final answer, exactly the "thought:
            # task resolved" step a real reasoning model would take.
            trace.final_answer = _summarise_observation(name, observation, _looks_arabic(objective))
            trace.step_count = step_no
            trace.terminated_reason = "final_answer"
            if verbose:
                print(f"[react] step {step_no}: Thought: observation answers the objective -> final answer")
                print(f"[react] Final answer: {trace.final_answer}")
            return _finalise(trace)

    trace.step_count = max_steps
    trace.terminated_reason = "step_budget_exhausted"
    trace.final_answer = "I was not able to resolve this within the step budget."
    if verbose:
        print(f"[react] step budget ({max_steps}) exhausted — escalating, not looping forever")
    return _finalise(trace)


def _finalise(trace: ReactTrace) -> ReactTrace:
    trace.redundant_tool_calls = count_redundant_tool_calls(trace)
    return trace
