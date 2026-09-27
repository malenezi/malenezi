"""Lab 6 solution — thin re-export, not a fork.

The real supervisor/delegate/finish/agents-as-tools modules live in
`src/rafeeq/orchestration/*.py`. `solution/verify.py` drives `supervise`/
`route` (Layer A) by hand; the full compiled graph
(`build_supervisor_graph()`) needs `langgraph`.
"""
from __future__ import annotations

from rafeeq.orchestration.supervisor import LANGGRAPH_AVAILABLE, Route, build_supervisor_graph, route, supervise
from rafeeq.orchestration.finish import aggregate, escalate
from rafeeq.orchestration.routing import classify_intent, specialist_for_intent
from rafeeq.orchestration.fastpath import fastpath_route

try:
    from rafeeq.orchestration.delegate import make_delegate
except ImportError:
    make_delegate = None  # type: ignore[assignment]

try:
    from rafeeq.orchestration.agents_as_tools import (
        billing_agent,
        billing_agent_impl,
        logistics_agent,
        logistics_agent_impl,
        orders_agent,
        orders_agent_impl,
    )
except ImportError:
    orders_agent = logistics_agent = billing_agent = None  # type: ignore[assignment]
    orders_agent_impl = logistics_agent_impl = billing_agent_impl = None  # type: ignore[assignment]

__all__ = [
    "LANGGRAPH_AVAILABLE", "Route", "build_supervisor_graph", "route", "supervise",
    "aggregate", "escalate", "classify_intent", "specialist_for_intent", "fastpath_route",
    "make_delegate", "orders_agent", "logistics_agent", "billing_agent",
    "orders_agent_impl", "logistics_agent_impl", "billing_agent_impl",
]
