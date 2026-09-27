"""Module 1 — Rafeeq's agent state.

The agent's contract. Every node reads and writes THIS object.
Rules: typed fields, no hidden globals, everything inspectable.

`RafeeqState` starts as EXACTLY the shape the instructor package defines in
Module 1 (`messages`, `customer_id`, `locale`, `order_id`, `step_count`,
`resolution`) and is then extended with the fields later modules need:
multi-agent handoffs (M6), planning (M2), tool results, ticketing, cost
tracking (M9) and guardrail flags (M8). Extending a typed state is the
whole point of building it as a state machine instead of a raw message
list — later modules add fields, not a rewrite.

Import-guarded: `langgraph`/`langchain-core` are Layer-B dependencies that
are not installed in the Layer-A build/CI sandbox (SPEC §1). This module
MUST import under plain python3. When the real packages are present we use
`Annotated[list[AnyMessage], add_messages]` exactly as the instructor
package specifies, so LangGraph's message-appending reducer applies. When
they are absent we fall back to a plain `list` annotation — the TypedDict
still works as a normal dict, just without the reducer semantics, which is
fine for Layer-A code (adapters, eval harness, selfcheck) that never runs a
compiled graph.
"""
from __future__ import annotations

from typing import Any, Literal, TypedDict

try:  # pragma: no cover - exercised only when langgraph/langchain are installed
    from langchain_core.messages import AnyMessage
    from langgraph.graph.message import add_messages

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    AnyMessage = Any  # type: ignore[assignment,misc]
    add_messages = None  # type: ignore[assignment]
    LANGGRAPH_AVAILABLE = False

if LANGGRAPH_AVAILABLE:
    from typing import Annotated

    _MessagesField = Annotated[list[AnyMessage], add_messages]
else:
    # No reducer available without langgraph — a plain list. Code that only
    # ever touches state as a dict (adapters, budget checks, selfcheck,
    # TawseelBench scenarios) does not need the reducer at all.
    _MessagesField = list


class RafeeqState(TypedDict):
    # Conversation so far. `add_messages` appends rather than overwrites
    # (when langgraph is available); otherwise a plain, developer-managed list.
    messages: _MessagesField
    # The customer/session this run belongs to (drives memory in M4).
    customer_id: str
    locale: Literal["ar", "en"]
    # Progress + control fields — the difference between debuggable and opaque.
    order_id: str | None
    step_count: int
    resolution: Literal["pending", "resolved", "escalated"]

    # --- extended fields (added for later modules; see module note per field) ---
    handoff_count: int          # M6: supervisor/agents-as-tools handoff budget
    subgoal: str | None         # M2: Plan-and-Execute — current subgoal text
    route: str | None           # M6: last routing decision (which specialist)
    last_result: dict           # M3: most recent tool result, surfaced not swallowed
    ticket_id: str              # M4/M9: links state to the eval/audit ticket record
    cost_usd: float             # M9: running spend for this run, checked by RunBudget
    flags: list[str]            # M8: guardrail/security flags raised during the run


def new_state(**overrides: Any) -> dict[str, Any]:
    """Return a fully-initialised state dict — every `RafeeqState` key
    present with a sane default, then overridden by `overrides`.

    TEACHING POINT: this is the fix for the Module 1 troubleshooting row
    `KeyError: step_count` — "state not fully initialised". Never hand-roll
    a partial initial state dict; call `new_state(...)` and pass only what
    you actually know (customer_id, locale, the first message, ...).

    Example:
        initial = new_state(customer_id="CUST-4471", locale="ar",
                             messages=[HumanMessage(content="أين طلبي؟")])
    """
    base: dict[str, Any] = {
        "messages": [],
        "customer_id": "",
        "locale": "en",
        "order_id": None,
        "step_count": 0,
        "resolution": "pending",
        "handoff_count": 0,
        "subgoal": None,
        "route": None,
        "last_result": {},
        "ticket_id": "",
        "cost_usd": 0.0,
        "flags": [],
    }
    base.update(overrides)
    return base
