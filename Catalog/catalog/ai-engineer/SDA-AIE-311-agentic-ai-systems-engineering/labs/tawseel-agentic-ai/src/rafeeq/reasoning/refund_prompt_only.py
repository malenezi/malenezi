"""Module 7 — ANTI-PATTERN. Lab 7's starting point. DO NOT copy this shape.

# ANTI-PATTERN: every business rule here is a SENTENCE the model must
choose to honour on every single request. Untestable (you cannot unit
test a paragraph), non-deterministic (the same input can get a different
answer on a different day), re-billed every request (a model call decides
a fixed rule), and — the reason this file exists — talk-around-able: a
crafted customer message can argue the model past "never refund more than
500 SAR" the same way `data/orders/INJECTION_NOTES.md` documents for the
authorisation layer. `flows/refund_flow.py` is the fix: the SAME rules,
each moved from a sentence into a deterministic, uncrossable graph branch.

This module exists to be run, watched fail on the adversarial ticket, and
then abandoned — never extended. See Module 7 Lab, task 1.
"""
from __future__ import annotations

from typing import Any

from rafeeq.core.llm import get_model

try:  # pragma: no cover - exercised only when langchain-core is installed
    from langchain_core.messages import SystemMessage, HumanMessage
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


# ANTI-PATTERN: the whole business-rule surface lives in prose. Compare
# every clause here to its counterpart in `flows/refund_flow.py`
# (`eligibility_gate`, `amount_gate`, `REFUND_LIMIT_SAR`) — same rule,
# opposite engineering.
REFUND_PROMPT = SystemMessage(content=(
    "You are Rafeeq's refund handler. Rules you MUST follow:\n"
    "- Only refund orders delivered late per the SLA.\n"
    "- Never refund more than 500 SAR without human approval.\n"
    "- Always verify the order id before refunding.\n"
    "- Never refund the same order twice.\n"
    "- Reply in the customer's language and cite the refund policy.\n"
    "Decide everything above yourself for each request."))   # <-- the whole problem


def naive_refund_handler(customer_message: str) -> dict[str, Any]:
    """Run the anti-pattern end to end: one model call, the whole
    decision made by prompt. Returns the model's raw response plus any
    tool call it chose to emit, so a caller (e.g. `reasoning/compare.py`
    or Lab 7's adversarial-ticket test) can inspect whether the rule held
    — including a `requested_amount_sar` field extracted from the message
    when present, purely so the demo can show the 500 SAR limit being
    argued past without wiring a real tool call.

    # SMELL: there is no gate here. If the model decides to comply with an
    # instruction embedded in `customer_message` ("ignore the limit"), this
    # function has no code-level mechanism to stop it — that IS the bug
    # Module 7 exists to fix, left intact on purpose.
    """
    model = get_model()
    reply = model.invoke([REFUND_PROMPT, HumanMessage(content=customer_message)])
    return {
        "content": reply.content,
        "tool_calls": list(getattr(reply, "tool_calls", []) or []),
    }
