"""Module 5 — a specialist agent factory: scoped tools, focused prompt,
isolated context. Three specialists (orders, logistics, billing) built
from ONE factory, `make_specialist`, so a fourth specialist is a
four-line addition, not a new pattern.

`create_react_agent` (`langgraph.prebuilt`) is Layer B and import-guarded.
Prompts and tool groupings, however, are plain data — importable and
inspectable (e.g. by `tests/unit/test_scoping.py`'s tool-list assertions)
with no langgraph installed. Agent OBJECTS are built lazily, on first use
(`get_orders_agent()` etc.), never at import time (SPEC §1: "graph
construction goes inside build_*() functions, never at import time") —
the instructor package's module-level `orders_agent = make_specialist(...)`
is exactly what these lazy getters defer.
"""
from __future__ import annotations

from typing import Any, Callable

from rafeeq.tools import billing, customer, logistics, orders

try:  # pragma: no cover - exercised only when langgraph is installed
    from langgraph.prebuilt import create_react_agent
    from langchain_core.messages import SystemMessage

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    create_react_agent = None  # type: ignore[assignment,misc]
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "Building a specialist agent requires `langgraph` and `langchain-core` "
    "(SPEC §1, Layer B). Install with:\n    pip install langgraph langchain-core\n"
    "SCOPE, SPECIALIST_TOOLS and SPECIALIST_PROMPTS in this module need "
    "neither and are already importable/inspectable without them."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


# --------------------------------------------------------------------------
# Scoped toolsets. Note the Billing group never includes a
# tracking/geo/customer-PII tool, and Logistics never includes a refund
# tool — this is the "Billing agent structurally cannot touch shipping
# data" claim made concrete, checkable by `tests/unit/test_scoping.py`
# without building a single agent.
# --------------------------------------------------------------------------
SPECIALIST_TOOLS: dict[str, list[Any]] = {
    "orders": list(orders.TOOLS),
    "logistics": list(logistics.TOOLS),
    "billing": list(billing.TOOLS),
}

# Customer/CRM tools are deliberately NOT bound to any of the three
# domain specialists above (SPEC's Module-5 code block keeps them to
# orders/logistics/billing) — they belong to the customer-facing
# supervisor/scoping boundary itself (`security/authz.py`'s
# `customer_agent` policy), not to one domain specialist.
CUSTOMER_TOOLS: list[Any] = list(customer.TOOLS)

SPECIALIST_PROMPTS: dict[str, str] = {
    "orders": (
        "You are Rafeeq's Orders specialist. You handle order lookup, status, and "
        "details ONLY. Reply in the customer's language. If asked about money or "
        "delivery routing, say it is out of your scope."
    ),
    "logistics": (
        "You are Rafeeq's Logistics specialist. You handle shipment tracking, ETAs, "
        "and delivery rescheduling ONLY. Never issue refunds."
    ),
    "billing": (
        "You are Rafeeq's Billing specialist. You handle invoices and refunds within "
        "policy ONLY. You never see shipment PII. Cite the current refund policy."
    ),
}


def make_specialist(name: str, system: str, tools: list[Any]) -> Any:
    """Each specialist owns a narrow toolset and a single-domain prompt.
    `name` doubles as the routing target (Module 6's supervisor keys off
    it)."""
    _require_langgraph()
    return create_react_agent(
        model=get_model_for_specialist().bind_tools(tools),
        tools=tools,
        prompt=SystemMessage(content=system),
        name=name,                                   # name = routing target (M6)
    )


def get_model_for_specialist() -> Any:
    """A thin indirection so a future specialist can request a different
    model tier without editing `make_specialist` itself."""
    from rafeeq.core.llm import get_model

    return get_model()


_agent_cache: dict[str, Any] = {}


def _get_or_build(name: str) -> Any:
    if name not in _agent_cache:
        _agent_cache[name] = make_specialist(name, SPECIALIST_PROMPTS[name], SPECIALIST_TOOLS[name])
    return _agent_cache[name]


def get_orders_agent() -> Any:
    return _get_or_build("orders")


def get_logistics_agent() -> Any:
    return _get_or_build("logistics")


def get_billing_agent() -> Any:
    return _get_or_build("billing")


# name -> lazy builder. `rafeeq.orchestration.delegate`/`supervisor` use
# this so they only ever build (and pay the model-binding cost of) the
# specialist a given ticket actually needs.
SPECIALIST_BUILDERS: dict[str, Callable[[], Any]] = {
    "orders": get_orders_agent,
    "logistics": get_logistics_agent,
    "billing": get_billing_agent,
}
