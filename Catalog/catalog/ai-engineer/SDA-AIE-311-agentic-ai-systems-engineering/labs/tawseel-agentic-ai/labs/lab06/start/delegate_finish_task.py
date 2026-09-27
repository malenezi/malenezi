"""Lab 6, Tasks 2/5 — scoped handoff with mandatory write-back, and clean escalation.

Simplified for offline testability: instead of invoking a real LangGraph
specialist agent, `make_delegate` here takes a plain `specialist_fn(payload)
-> str` callable (a stand-in for "the specialist ran and said this").
The CONTRACT it must enforce is identical to the real
`rafeeq.orchestration.delegate.make_delegate`: scoped input, a logged
handoff, and — the one that matters most — the specialist's result MUST
be written back into state before returning, never dropped.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.agents.scoping import scoped_input

try:
    from langchain_core.messages import AIMessage, SystemMessage
except ImportError:
    from dataclasses import dataclass as _dataclass

    @_dataclass
    class AIMessage:  # type: ignore[no-redef]
        content: str
        type: str = "ai"

    @_dataclass
    class SystemMessage:  # type: ignore[no-redef]
        content: str
        type: str = "system"

from rafeeq.core.llm import get_model

ESCALATE_MESSAGE_EN = ("Sorry — I'm handing this to a specialist colleague who has your "
                        "full case and will follow up shortly.")
ESCALATE_MESSAGE_AR = "عذرًا — سأحوّل حالتك إلى زميل مختص لديه كامل تفاصيلها وسيتابع معك قريبًا."


def make_delegate(name: str, specialist_fn: Callable[[dict], str]) -> Callable[[dict], dict]:
    """TODO(lab 6.2): build and return the delegate NODE (a closure over
    `name` and `specialist_fn`). The returned function must, given
    `state`:

    1. `payload = scoped_input(state, name)` — PDPL-scoped context only.
    2. `result_text = specialist_fn(payload)` — "the specialist ran".
    3. Return a state update that WRITES BACK the result:
       `{"messages": [AIMessage(content=result_text)],
       "last_result": {**state.get("last_result", {}), name: result_text},
       "handoff_count": state.get("handoff_count", 0) + 1}`.

    Troubleshooting row this fixes: "Customer told 'nothing happened'" ->
    "Lost handoff (no write-back)" -> "Specialist result MUST be written
    to last_result/messages." Skip step 3's write-back to reproduce that
    failure on purpose — see `labs/sim/sim_lost_handoff.py`.
    """
    raise NotImplementedError("TODO(lab 6.2): implement make_delegate")


def aggregate(state: dict) -> dict:
    """Provided: one coherent reply composed from (possibly several)
    specialist results already in `state["messages"]`."""
    summary = get_model().invoke([SystemMessage(content="Compose ONE clear reply to the "
                                                          "customer in their language from "
                                                          "these specialist results."),
                                   *state["messages"]])
    return {"messages": [summary], "resolution": "resolved"}


def escalate(state: dict) -> dict:
    """TODO(lab 6.5): hand to a human WITH the full trace/state — never a
    dead end. Pick `ESCALATE_MESSAGE_EN`/`_AR` by `state.get("locale")`,
    return `{"messages": [AIMessage(content=msg)], "resolution":
    "escalated"}`. (Logging the full context to a human queue is
    `rafeeq.orchestration.finish._log_escalation`'s job in the real
    module — out of scope for this simplified version, but note in your
    own comment where you WOULD call it.)
    """
    raise NotImplementedError("TODO(lab 6.5): implement escalate")
