"""Lab 1, Task 2 — implement `RafeeqState`.

Fill in the TODOs below so this file matches the instructor package's
Module 1 shape exactly: `messages`, `customer_id`, `locale`, `order_id`,
`step_count`, `resolution`. Once it compiles, `python3 -c "import
labs.lab01.start.state"` should succeed with NO third-party packages
installed — this file must stay Layer-A (SPEC §1): no bare `import
langgraph` or `import langchain_core` at module scope.

When you are done, compare your file field-for-field against
`src/rafeeq/core/state.py` (which additionally carries the fields Labs
2-9 add later: `handoff_count`, `subgoal`, `route`, `last_result`,
`ticket_id`, `cost_usd`, `flags` — you do not need those yet).
"""
from __future__ import annotations

from typing import Any, Literal, TypedDict

# TODO(lab 1.2a): import-guard langgraph/langchain-core exactly like the
# real module does, so this file imports under plain python3 either way:
#
#   try:
#       from langchain_core.messages import AnyMessage
#       from langgraph.graph.message import add_messages
#       LANGGRAPH_AVAILABLE = True
#   except ImportError:
#       AnyMessage = Any
#       add_messages = None
#       LANGGRAPH_AVAILABLE = False
#
# Then build `_MessagesField` as `Annotated[list[AnyMessage], add_messages]`
# when available, else plain `list`.

LANGGRAPH_AVAILABLE = False  # TODO(lab 1.2a): replace with the real try/except above
_MessagesField = list  # TODO(lab 1.2a): Annotated[list[AnyMessage], add_messages] when available


class RafeeqState(TypedDict):
    """TODO(lab 1.2b): declare the six fields the package requires:

        messages: _MessagesField
        customer_id: str
        locale: Literal["ar", "en"]
        order_id: str | None
        step_count: int
        resolution: Literal["pending", "resolved", "escalated"]

    Troubleshooting row this fixes: `KeyError: step_count` — "State not
    fully initialised. Provide every RafeeqState key in the initial dict."
    That row is about `new_state()` below, but it starts here: you cannot
    initialise every key if you never declared every key.
    """
    ...  # TODO(lab 1.2b): replace this line with the six typed fields


def new_state(**overrides: Any) -> dict[str, Any]:
    """TODO(lab 1.2c): return a dict with EVERY RafeeqState key given a
    sane default, then updated with `overrides`. This is what fixes the
    "state not fully initialised" troubleshooting row for good: callers
    should never hand-roll a partial initial state dict.

    Defaults to use: messages=[], customer_id="", locale="en",
    order_id=None, step_count=0, resolution="pending".
    """
    raise NotImplementedError("TODO(lab 1.2c): build and return the full state dict")
