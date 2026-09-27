"""Lab 9, Tasks 1/2 — instrument a ticket run with tracing, then attribute
its cost by model, component, and intent.

Fill in the TODOs. Every real building block already exists in
`rafeeq.observability.*` (Layer A — stdlib only, no langgraph): you are
WIRING tracing spans around the existing deterministic routing/tool
layer, not writing a tracer from scratch.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import get_settings
from rafeeq.core.llm import estimate_tokens
from rafeeq.observability.tracing import Run, start_run, start_span
from rafeeq.orchestration.routing import classify_intent, specialist_for_intent
from rafeeq.tools.billing import get_invoice_impl
from rafeeq.tools.logistics import track_shipment_impl
from rafeeq.tools.orders import get_order_impl

# Domain -> tool impl a ticket's specialist would actually call, keyed the
# same way `agents/specialist.py::SPECIALIST_TOOLS` is.
_TOOL_FOR_SPECIALIST = {
    "logistics": ("track_shipment", track_shipment_impl),
    "billing": ("get_invoice", get_invoice_impl),
}

_ASSUMED_REPLY_TOKENS = 120  # a representative composed-reply length


def run_traced_ticket(ticket: dict[str, Any], *, always_frontier: bool = True) -> Run:
    """TODO(lab 9.1): instrument ONE ticket end to end.

    1. `intent, confidence = classify_intent(ticket["text"])`.
    2. Open `with start_run(f"ticket:{ticket['ticket_id']}", intent=intent,
       ticket_id=ticket['ticket_id'], locale=ticket['locale']) as run:` —
       everything below happens INSIDE this block, and `run` is what you
       return.
    3. Inside it, open `with start_span("classify_intent", run_type="llm",
       model=get_settings().cheap_model_name, tokens_in=estimate_tokens(
       ticket['text']), tokens_out=estimate_tokens(intent)):` — an empty
       body is fine, the span itself is the point (the classification
       step is cheap-model-shaped work, M2's fastpath router).
    4. specialist = `specialist_for_intent(intent)`; if it is one of
       `_TOOL_FOR_SPECIALIST` AND `ticket.get("order_id")`, open
       `with start_span(f"specialist:{specialist}", run_type="tool",
       tool_name=tool_name, args={"order_id": ticket["order_id"]}):` and
       call the tool impl inside it (its own cost is 0 — tools do not
       bill tokens, only spans with a `model` do).
    5. Compose the reply: TODO(lab 9.1b) — see `optimise_retry_task.py`
       for WHICH model tier this should use; for Task 1 just always use
       the frontier model (`get_settings().frontier_model_name`) inside
       `with start_span("compose_reply", run_type="llm", model=...,
       tokens_in=estimate_tokens(ticket["text"]),
       tokens_out=_ASSUMED_REPLY_TOKENS):`.
    """
    raise NotImplementedError("TODO(lab 9.1): implement run_traced_ticket")


def cost_report_for(tickets: list[dict[str, Any]]) -> tuple[list[Run], str]:
    """TODO(lab 9.2): run every ticket through `run_traced_ticket`,
    collect the `Run`s, and return `(runs, rafeeq.observability.cost.
    cost_report(runs))`. This IS the cost-attribution reveal: read the
    report's `by_model`/`by_component` breakdown and find the single
    biggest cost bar before moving on to Task 3."""
    raise NotImplementedError("TODO(lab 9.2): implement cost_report_for")
