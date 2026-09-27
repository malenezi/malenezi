"""Module 6 — Architecture B: agents-as-tools.

SPEC §6 asks for BOTH multi-agent shapes, compared on the same metrics:

  - **Architecture A** (`orchestration.supervisor`) — a graph with a
    routing hub and specialist nodes as separate graph participants,
    coordinated by conditional edges.
  - **Architecture B** (this file) — ONE agent (Rafeeq itself) whose tool
    belt is three FUNCTIONS, `orders_agent()`, `logistics_agent()`,
    `billing_agent()`, each of which internally runs the corresponding
    specialist and returns a small, typed result. There is no separate
    routing node and no `route`/`handoff_count` graph machinery — routing
    IS tool selection, the same mechanism Rafeeq already uses for every
    other tool call.

WHY this can give GREATER CONTROL and STRONGER TYPING than a generic
supervisor (this is the module's required teaching point, not a stylistic
preference): LangGraph's own multi-agent guidance notes that wrapping a
sub-agent as a tool forces its interface through a typed, validated
function signature — arguments and return value are both schema-checked
the same way any other tool call is, before and after the sub-agent runs.
A supervisor's routing decision, by contrast, is a free-form `target`
string plus a free-form `subgoal` string threaded through shared state;
nothing stops a routing bug from sending `billing`'s subgoal to
`logistics` and only a test (or a human reading the trace) catches it.
Agents-as-tools also composes naturally with everything else in Rafeeq's
tool-calling machinery for free: the same per-tool authorisation check
(`security/authz.py`), the same idempotency/retry policy
(`tools/registry.py`'s `WRITE_TOOLS`/`IDEMPOTENT`), and the same
tool-call tracing a plain tool call gets — a supervisor's handoff is a
DIFFERENT kind of event the rest of the system must learn to recognise
separately. The trade-off going the other way (why Architecture A still
exists, SPEC's honest comparison): a supervisor makes the multi-hop
CONTROL FLOW itself inspectable as graph structure (you can literally
draw the routing decision tree), where agents-as-tools hides that
sequencing inside one agent's own reasoning trace — harder to bound with
a `handoff_count`-style global budget, because "how many sub-agent calls
will this one ReAct loop make" is the model's call, step-budgeted the
same way any other tool-using loop is (`core.config.MAX_STEPS`), not a
dedicated cross-agent counter. `docs/ARCHITECTURE.md` carries the full
comparison table for students to fill in from the eval harness.

Layer B: sub-agent invocation needs the specialists built in
`agents/specialist.py`, themselves LangGraph agents; import-guarded.
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from rafeeq.agents.scoping import scoped_input

try:  # pragma: no cover - exercised only when langgraph/langchain are installed
    from langgraph.prebuilt import create_react_agent
    from langchain_core.messages import SystemMessage
    from langchain_core.tools import tool

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    create_react_agent = None  # type: ignore[assignment,misc]
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

    def tool(func=None, *, return_direct: bool = False):  # type: ignore[no-redef]
        """Fallback stand-in for `langchain_core.tools.tool` (see
        `tools/tawseel.py` for the full rationale) — preserves the plain
        callable so the `*_impl`-shaped functions below stay directly
        invokable without langchain-core installed."""
        def _decorate(f):
            f.name = f.__name__
            f.description = (f.__doc__ or "").strip()
            return f
        return _decorate(func) if func is not None else _decorate

MISSING_DEP_HINT = (
    "build_rafeeq_single_agent() requires `langgraph` and `langchain-core` "
    "(SPEC §1, Layer B). Install with:\n    pip install langgraph langchain-core\n"
    "The *_impl sub-agent-tool functions in this module still need the "
    "specialist agents from agents/specialist.py, which themselves need "
    "langgraph — there is no pure-Layer-A path through THIS file, unlike "
    "orchestration/routing.py and fastpath.py."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


class SpecialistToolInput(BaseModel):
    """The typed contract every sub-agent tool call is validated against
    — the "stronger typing" half of this file's teaching point. Compare
    to a supervisor handoff's free-form `subgoal: str` in shared state."""

    subgoal: str = Field(description="The concrete sub-task for this specialist to perform.")
    customer_id: str
    locale: str = "en"
    order_id: str | None = None


class SpecialistToolOutput(BaseModel):
    specialist: str
    answer: str


def _run_specialist_as_tool(name: str, payload: SpecialistToolInput) -> dict[str, Any]:
    """Shared implementation for the three `*_agent` tools below: build a
    SCOPED input (the same `agents.scoping.scoped_input` PDPL control
    Architecture A's `delegate.py` uses — scoping is not unique to the
    supervisor shape) from the typed `payload`, run the specialist, and
    return a typed, small result — never the specialist's raw internal
    message list."""
    _require_langgraph()
    from rafeeq.agents.specialist import SPECIALIST_BUILDERS

    build_agent = SPECIALIST_BUILDERS[name]
    state = {
        "messages": [("human", payload.subgoal)],
        "customer_id": payload.customer_id,
        "locale": payload.locale,
        "order_id": payload.order_id,
    }
    scoped = scoped_input(state, name)
    result = build_agent().invoke(scoped)
    answer = result["messages"][-1]
    return SpecialistToolOutput(specialist=name, answer=answer.content).model_dump()


def orders_agent_impl(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Run Rafeeq's Orders specialist as a single typed tool call.

    Use for order lookup, status, and details ONLY — the specialist
    itself refuses money/routing questions out of scope. Never call this
    for tracking (see `logistics_agent`) or refunds (see `billing_agent`).
    """
    payload = SpecialistToolInput(subgoal=subgoal, customer_id=customer_id, locale=locale, order_id=order_id)
    return _run_specialist_as_tool("orders", payload)


def logistics_agent_impl(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Run Rafeeq's Logistics specialist as a single typed tool call.

    Use for shipment tracking, ETAs, and delivery rescheduling ONLY.
    Never issues refunds — see `billing_agent` for that.
    """
    payload = SpecialistToolInput(subgoal=subgoal, customer_id=customer_id, locale=locale, order_id=order_id)
    return _run_specialist_as_tool("logistics", payload)


def billing_agent_impl(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Run Rafeeq's Billing specialist as a single typed tool call.

    Use for invoices and refunds within policy ONLY. Never sees shipment
    PII — `_run_specialist_as_tool` scopes the payload the same way
    Architecture A's handoffs do.
    """
    payload = SpecialistToolInput(subgoal=subgoal, customer_id=customer_id, locale=locale, order_id=order_id)
    return _run_specialist_as_tool("billing", payload)


@tool
def orders_agent(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Delegate a sub-task to Rafeeq's Orders specialist (lookup/status/
    details only). Returns {"specialist": "orders", "answer": ...}."""
    return orders_agent_impl(subgoal, customer_id, locale, order_id)


@tool
def logistics_agent(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Delegate a sub-task to Rafeeq's Logistics specialist (tracking/
    ETA/reschedule only). Returns {"specialist": "logistics", "answer": ...}."""
    return logistics_agent_impl(subgoal, customer_id, locale, order_id)


@tool
def billing_agent(subgoal: str, customer_id: str, locale: str = "en", order_id: str | None = None) -> dict:
    """Delegate a sub-task to Rafeeq's Billing specialist (invoices/
    refunds within policy only). Returns {"specialist": "billing", "answer": ...}."""
    return billing_agent_impl(subgoal, customer_id, locale, order_id)


SUB_AGENT_TOOLS: list[Any] = [orders_agent, logistics_agent, billing_agent]

TOP_LEVEL_PROMPT = (
    "You are Rafeeq. You do not handle orders, logistics, or billing "
    "directly — delegate each sub-task to the matching specialist tool "
    "(orders_agent, logistics_agent, billing_agent) and compose the "
    "customer's final reply from their typed results. Reply in the "
    "customer's language."
)

_single_agent_cache: Any = None


def get_rafeeq_single_agent(reset: bool = False) -> Any:
    """Lazily build (and cache) Architecture B: one Rafeeq agent whose
    tool belt is the three sub-agent tools above, plus the ordinary
    read-only orders/logistics/billing tools for anything that does not
    need a full specialist round-trip. Never built at import time."""
    global _single_agent_cache
    _require_langgraph()
    if _single_agent_cache is None or reset:
        from rafeeq.core.llm import get_model
        from rafeeq.tools.registry import ALL_TOOLS

        tools = [*SUB_AGENT_TOOLS, *ALL_TOOLS]
        _single_agent_cache = create_react_agent(
            model=get_model().bind_tools(tools),
            tools=tools,
            prompt=SystemMessage(content=TOP_LEVEL_PROMPT),
            name="rafeeq_single_agent",
        )
    return _single_agent_cache


# Alias matching the SPEC's own naming for the graph-builder convention
# used elsewhere in this repo (`build_*`) — same object, same cache.
def build_rafeeq_single_agent(reset: bool = False) -> Any:
    return get_rafeeq_single_agent(reset=reset)
