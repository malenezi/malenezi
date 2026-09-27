"""Module 5 — the monolith. Kept ALIVE in the eval harness so we can
always answer: 'is the multi-agent version actually better on THIS ticket
class?' Never delete this file to "clean up" after Module 6 ships the
supervisor — the whole point of Module 5's benchmark table is a live,
ongoing comparison, not a one-time before/after screenshot.

Same import-guard discipline as `agents/specialist.py`: the 18-tool list
(`ALL_TOOLS`) is plain data, importable with no langgraph installed; the
`monolith` agent OBJECT is built lazily via `get_monolith()`, never at
import time.
"""
from __future__ import annotations

from typing import Any

from rafeeq.tools import billing, logistics, orders

try:  # pragma: no cover - exercised only when langgraph is installed
    from langgraph.prebuilt import create_react_agent
    from langchain_core.messages import SystemMessage

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    create_react_agent = None  # type: ignore[assignment,misc]
    SystemMessage = None  # type: ignore[assignment,misc]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "Building the monolith baseline agent requires `langgraph` and "
    "`langchain-core` (SPEC §1, Layer B). Install with:\n"
    "    pip install langgraph langchain-core\n"
    "ALL_TOOLS in this module needs neither."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


# Orders + Logistics + Billing tools, ALL bound to one agent, one prompt
# — deliberately the opposite of Module 5's specialist decomposition.
# Customer/CRM tools are excluded here too (same reasoning as
# `specialist.py`), so the monolith/specialist comparison is apples to
# apples on the same 15-tool surface, not skewed by an extra domain.
ALL_TOOLS: list[Any] = list(orders.TOOLS) + list(logistics.TOOLS) + list(billing.TOOLS)

MONOLITH_PROMPT = (
    "You are Rafeeq. You handle orders, logistics, AND billing. "
    "Choose the right tool carefully."
)

_monolith_cache: Any = None


def get_monolith(reset: bool = False) -> Any:
    """Lazily build (and cache) the single-agent baseline. Benchmark
    note (Module 5): expect HIGHER selection accuracy from specialists on
    mixed tickets, but the monolith may be CHEAPER on trivial single-
    domain ones — report both regimes honestly, never just the one that
    favours the design you already picked."""
    global _monolith_cache
    _require_langgraph()
    if _monolith_cache is None or reset:
        from rafeeq.core.llm import get_model

        _monolith_cache = create_react_agent(
            model=get_model().bind_tools(ALL_TOOLS),
            tools=ALL_TOOLS,
            prompt=SystemMessage(content=MONOLITH_PROMPT),
        )
    return _monolith_cache
