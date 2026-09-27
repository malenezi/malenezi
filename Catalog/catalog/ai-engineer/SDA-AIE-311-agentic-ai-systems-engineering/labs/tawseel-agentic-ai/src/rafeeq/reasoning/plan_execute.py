"""Module 2 — Plan-and-Execute: decide the whole approach first.

A planner produces an explicit, LOGGABLE `Plan`; an executor carries out
each step. The plan is the enterprise control point (module overview,
"business relevance"): log it before any step runs, and gate execution on
`plan_approval_gate` — the one function in this file a human-in-the-loop
integration replaces to turn "auto-approve" into "wait for a person".

Layer split: `make_plan` / `plan_node` / `execute_step` / `more_steps` /
`plan_approval_gate` / `log_plan` need only `pydantic` and
`rafeeq.core.llm.get_model` — they run under plain python3 with the
default `StubChatModel` (SPEC §2), no langgraph required. Only
`build_plan_execute_graph()` (wiring these into a compiled LangGraph
graph) needs `langgraph`/`langchain-core`, and is import-guarded.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from rafeeq.core.llm import get_model

try:  # pragma: no cover - exercised only when langgraph/langchain are installed
    from langchain_core.messages import SystemMessage, HumanMessage

    _MESSAGES_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    from dataclasses import dataclass as _dataclass

    @_dataclass
    class SystemMessage:  # type: ignore[no-redef]
        content: str
        type: str = "system"

    @_dataclass
    class HumanMessage:  # type: ignore[no-redef]
        content: str
        type: str = "human"

    _MESSAGES_AVAILABLE = False

try:  # pragma: no cover - exercised only when langgraph is installed
    from langgraph.graph import StateGraph, START, END

    LANGGRAPH_AVAILABLE = True
except ImportError:
    StateGraph = None  # type: ignore[assignment,misc]
    START = "__start__"  # type: ignore[assignment]
    END = "__end__"  # type: ignore[assignment]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "build_plan_execute_graph() requires `langgraph` and `langchain-core` "
    "(SPEC §1, Layer B). Install with:\n    pip install langgraph langchain-core\n"
    "make_plan/plan_node/execute_step/more_steps/plan_approval_gate need "
    "neither — they run today, offline, against the stub or replay model."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


class Plan(BaseModel):
    """The inspectable artefact. Module 2's whole enterprise argument for
    Plan-and-Execute is that THIS can be logged, shown to a human, and
    approved before a single tool runs — never skip surfacing it."""

    steps: list[str] = Field(description="Ordered, concrete sub-tasks")


_FALLBACK_PLANS: dict[str, list[str]] = {
    "refund": [
        "Look up the order and confirm SLA breach / refund eligibility",
        "Determine the refund amount and the applicable autonomy band",
        "Issue the refund, or record an approval request if above the limit",
        "Notify the customer in their language",
    ],
    "reschedule": [
        "Confirm the order is in a reschedulable status",
        "Confirm the new delivery time with the customer",
        "Reschedule the delivery",
        "Report the new estimated arrival to the customer",
    ],
    "track": ["Look up the order's current delivery status", "Report the status and ETA to the customer"],
    "order_status": ["Look up the order's current status", "Report the status to the customer"],
    "invoice": ["Look up the order's invoice", "Send the invoice summary to the customer"],
}
_DEFAULT_FALLBACK_PLAN = [
    "Look up the order referenced in the request",
    "Determine the appropriate action from policy",
    "Respond to the customer in their language",
]


def _fallback_plan_steps(objective: str) -> list[str]:
    """Deterministic plan used when the model tier cannot itself populate
    `Plan.steps` (notably the default `StubChatModel`, SPEC §2: its
    generic `with_structured_output` wrapper only fills fields it knows
    how to infer — `order_id`/`intent`/`locale`/`confidence` — and has no
    generic notion of "steps"). Reuses `orchestration.routing.classify_intent`
    (Layer A, no extra dependency) so the fallback plan is still grounded
    in the objective's actual intent rather than a single generic
    placeholder."""
    from rafeeq.orchestration.routing import classify_intent

    intent, _confidence = classify_intent(objective)
    return list(_FALLBACK_PLANS.get(intent, _DEFAULT_FALLBACK_PLAN))


def make_plan(objective: str) -> Plan:
    planner = get_model().with_structured_output(Plan)   # structured, inspectable
    result = planner.invoke([
        SystemMessage(content="Break the objective into 2-5 concrete, ordered "
                              "steps a support agent can execute."),
        HumanMessage(content=objective)])
    if not getattr(result, "steps", None):
        # A live/frontier model tier populates `steps` directly; degrade
        # gracefully to the deterministic fallback rather than returning
        # an empty, useless plan.
        result = Plan(steps=_fallback_plan_steps(objective))
    return result


# --------------------------------------------------------------------------
# The enterprise control point (module overview: "the plan is an
# inspectable artefact ... show it to a human, gate execution on
# approval"). Default behaviour is auto-approve for short, low-risk plans
# — a real HITL integration replaces the body of this ONE function with an
# actual approval queue; every other function in this module is unchanged
# by that swap, because they only ever see the gate's decision, not how it
# was reached.
# --------------------------------------------------------------------------
_HIGH_RISK_KEYWORDS = ("refund", "استرداد", "استرجاع", "delete", "override", "fraud")


def plan_approval_gate(plan: Plan, *, auto_approve_threshold: int = 5) -> dict[str, Any]:
    """Decide whether `plan` may execute without a human in the loop.

    Pure function of the plan text — no model call, no side effect beyond
    the caller choosing to log the result (see `log_plan`). Flags a plan
    for human approval when it is unusually long (more steps than
    `auto_approve_threshold` suggests the planner is improvising rather
    than following a known workflow) or when any step's wording touches a
    high-stakes action (refund/fraud/override/delete) — the same
    money/identity boundary the action-risk matrix (SPEC §5) draws
    everywhere else in this repo. Returns a decision object, never raises.
    """
    steps = plan.steps
    flagged = [s for s in steps if any(kw in s.lower() or kw in s for kw in _HIGH_RISK_KEYWORDS)]
    too_long = len(steps) > auto_approve_threshold
    requires_human = bool(flagged) or too_long
    return {
        "approved": not requires_human,
        "requires_human": requires_human,
        "reason": (
            "high_risk_step" if flagged else "plan_too_long" if too_long else "auto_approved"
        ),
        "flagged_steps": flagged,
        "step_count": len(steps),
    }


def log_plan(objective: str, plan: Plan, gate_decision: dict[str, Any] | None = None) -> dict[str, Any]:
    """AUDIT: the plan is logged BEFORE any step executes — the plan is
    the control point, not an afterthought. Best-effort through
    `rafeeq.observability.audit` when that module exists (owned by a
    later part of this build); falls back to stdlib `logging` so a
    missing observability layer never blocks planning. Returns the log
    record either way, so callers/tests can assert on it without a real
    logging backend."""
    record = {
        "event": "plan_logged",
        "objective": objective,
        "steps": plan.steps,
        "gate_decision": gate_decision,
        "ts": datetime.now(timezone.utc).isoformat(),
    }
    try:
        from rafeeq.observability import audit as _audit  # lazy: may not exist yet

        log_fn = getattr(_audit, "log_plan", None) or getattr(_audit, "log_event", None)
        if log_fn is not None:
            try:
                log_fn(**record)
            except TypeError:
                log_fn(record)
    except Exception:  # noqa: BLE001 - logging must never break planning
        import logging

        logging.getLogger("rafeeq.reasoning.plan_execute").info(
            "plan: objective=%s steps=%s gate=%s", objective, plan.steps, gate_decision,
        )
    return record


def plan_node(state: dict) -> dict:
    plan = make_plan(state["objective"])
    gate = plan_approval_gate(plan)
    log_plan(state["objective"], plan, gate)     # AUDIT: logged before ANY step executes
    return {
        "plan": plan.steps, "remaining": list(plan.steps), "past": [],
        "plan_gate": gate,
    }


def execute_step(state: dict) -> dict:
    step = state["remaining"][0]
    result = get_model().invoke([                # cheap executor per step
        SystemMessage(content="Execute this single step and report the result."),
        HumanMessage(content=f"Step: {step}\nContext: {state['past']}")])
    return {"remaining": state["remaining"][1:],
            "past": state["past"] + [(step, result.content)]}


def more_steps(state: dict) -> str:
    return "execute" if state["remaining"] else END if LANGGRAPH_AVAILABLE else "__end__"


def run_plan_execute(objective: str, *, verbose: bool = True) -> dict[str, Any]:
    """Framework-free driver over `plan_node`/`execute_step`/`more_steps` —
    runs the whole Plan-and-Execute pattern under plain python3 (no
    langgraph needed) so it is usable by `compare.py` and any lab that
    wants the pattern's behaviour without compiling a graph. Mirrors what
    `build_plan_execute_graph()` does once compiled."""
    state: dict[str, Any] = {"objective": objective}
    state.update(plan_node(state))
    if verbose:
        print(f"[plan-execute] Plan for {objective!r}: {state['plan']}")
        print(f"[plan-execute] Approval gate: {state['plan_gate']}")
    if state["plan_gate"]["requires_human"]:
        if verbose:
            print("[plan-execute] Plan requires human approval — not executing autonomously.")
        return {**state, "executed": False}
    while state["remaining"]:
        state.update(execute_step(state))
        if verbose:
            step, result = state["past"][-1]
            print(f"[plan-execute] Executed: {step!r} -> {result[:120]}")
    return {**state, "executed": True}


def build_plan_execute_graph() -> Any:
    """Wire `plan_node` -> `execute_step` (looped via `more_steps`) -> END
    into a compiled LangGraph graph. Layer B; import-guarded."""
    _require_langgraph()

    g = StateGraph(dict)
    g.add_node("plan", plan_node)
    g.add_node("execute", execute_step)
    g.add_edge(START, "plan")
    g.add_conditional_edges("plan", lambda s: "execute" if not s["plan_gate"]["requires_human"] else END,
                             {"execute": "execute", END: END})
    g.add_conditional_edges("execute", more_steps, {"execute": "execute", END: END})
    return g.compile()
