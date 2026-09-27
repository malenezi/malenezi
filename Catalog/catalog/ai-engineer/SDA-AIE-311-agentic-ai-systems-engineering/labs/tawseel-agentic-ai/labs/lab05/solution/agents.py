"""Lab 5 solution — thin re-export, not a fork.

The real specialist factory, scoping module, and monolith baseline live
in `src/rafeeq/agents/{specialist,scoping,baseline}.py`. Building actual
LangGraph specialist agents (`get_orders_agent()` etc.) needs `langgraph`;
`SCOPE`/`scoped_input`/`SPECIALIST_TOOLS` need nothing and are what
`solution/verify.py` exercises.
"""
from __future__ import annotations

from rafeeq.agents.scoping import (
    FORBIDDEN_FIELDS,
    SCOPE,
    assert_no_forbidden_leak,
    known_specialists,
    scoped_input,
)
from rafeeq.agents.specialist import (
    LANGGRAPH_AVAILABLE,
    SPECIALIST_PROMPTS,
    SPECIALIST_TOOLS,
    get_billing_agent,
    get_logistics_agent,
    get_orders_agent,
    make_specialist,
)
from rafeeq.agents.baseline import get_monolith

__all__ = [
    "FORBIDDEN_FIELDS", "SCOPE", "assert_no_forbidden_leak", "known_specialists", "scoped_input",
    "LANGGRAPH_AVAILABLE", "SPECIALIST_PROMPTS", "SPECIALIST_TOOLS",
    "get_billing_agent", "get_logistics_agent", "get_orders_agent", "make_specialist",
    "get_monolith",
]
