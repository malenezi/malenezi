"""Lab 2, Task 1 — implement ReAct, explicitly, before any framework hides it.

Module 2's research note (SPEC §6, Yao et al.): build the thought ->
action -> observation loop BY HAND against the plain `*_impl` tool
callables — no `langgraph`, no `ToolNode`, no `bind_tools` magic — so the
control flow is visible before Module 3+ abstracts it away.

Fill in the TODOs. Everything here runs under plain python3 against the
default `StubChatModel` (SPEC §2) — zero cost, zero keys.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.llm import get_model


def default_tool_impls() -> dict[str, Callable[[dict], dict]]:
    """The dispatch table: tool name -> plain callable. Provided so you
    can focus on the LOOP, not re-deriving every domain tool signature."""
    from rafeeq.tools.logistics import track_shipment_impl
    from rafeeq.tools.billing import issue_refund_impl

    return {
        "track_shipment": lambda args: track_shipment_impl(args.get("order_id", "")),
        "issue_refund": lambda args: issue_refund_impl(
            args.get("order_id", ""), float(args.get("amount_sar", 0.0) or 0.0),
            args.get("reason", "customer_requested"),
            args.get("idempotency_key") or f"lab2-{args.get('order_id', '')}"),
    }


@dataclass
class Step:
    step: int
    action: str | None
    action_input: dict
    observation: Any


@dataclass
class Trace:
    objective: str
    steps: list[Step] = field(default_factory=list)
    final_answer: str = ""
    step_count: int = 0


def count_redundant_tool_calls(trace: Trace) -> int:
    """TODO(lab 2.1a): count tool calls that repeat an EXACT (name, args)
    pair already seen earlier in `trace.steps` — the "thrashing" failure
    mode: the same question answered twice because the first
    observation's result was never checked before acting again.

    Hint: build a `set()` of `(action, json.dumps(action_input,
    sort_keys=True))` keys as you walk `trace.steps` in order; the first
    time a key appears is legitimate, every repeat after it counts.
    """
    raise NotImplementedError("TODO(lab 2.1a): implement count_redundant_tool_calls")


def run_react(objective: str, *, max_steps: int = MAX_STEPS,
              tool_impls: dict[str, Callable[[dict], dict]] | None = None) -> Trace:
    """TODO(lab 2.1b): the interleaved loop. For each step (up to
    `max_steps`):

    1. Ask the model what to do: `model = get_model().bind_tools([{"name":
       n} for n in impls])`, then `reply = model.invoke([("system", ...),
       *messages])`.
    2. If `reply.tool_calls` is empty -> this IS the final answer. Set
       `trace.final_answer = reply.content`, `trace.step_count =
       step_no - 1`, return `trace`.
    3. Otherwise, take the FIRST tool call, dispatch it through
       `tool_impls[name](args)`, append a `Step(...)` to `trace.steps`
       recording the action/action_input/observation, and append the
       observation to `messages` as the next turn so the model sees it
       before deciding again (the troubleshooting row this fixes:
       "ReAct thrashes on one tool" — "no observation added to state").
    4. If `max_steps` is exhausted without a final answer, set
       `trace.step_count = max_steps` and return `trace` anyway (bounded,
       Module 1's discipline carried forward — never loop unbounded).
    """
    impls = tool_impls or default_tool_impls()
    trace = Trace(objective=objective)
    raise NotImplementedError("TODO(lab 2.1b): implement the interleaved loop")
