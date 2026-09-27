"""Lab 7 solution — thin re-export, not a fork.

The real flow lives in `src/rafeeq/flows/refund_flow.py`; the anti-pattern
it replaces lives in `src/rafeeq/reasoning/refund_prompt_only.py` (read,
run, never extend). `solution/verify.py` drives both directly.
"""
from __future__ import annotations

from rafeeq.flows.refund_flow import (
    LANGGRAPH_AVAILABLE,
    RefundState,
    amount_gate,
    build_refund_flow,
    do_refund,
    eligibility_gate,
    load_order,
    request_human_approval,
)
from rafeeq.reasoning.refund_prompt_only import REFUND_PROMPT, naive_refund_handler

__all__ = [
    "LANGGRAPH_AVAILABLE", "RefundState", "amount_gate", "build_refund_flow",
    "do_refund", "eligibility_gate", "load_order", "request_human_approval",
    "REFUND_PROMPT", "naive_refund_handler",
]
