"""Lab 1 solution — Task 3.

Thin re-export: the real `reason`/`route`/`build_graph` live in
`src/rafeeq/core/graph.py`. Read that file, not this one, for the
implementation — this module just re-exposes it under the lab's own
import path so `labs/lab01/solution/` is self-contained.
"""
from __future__ import annotations

from rafeeq.core.graph import (
    LANGGRAPH_AVAILABLE,
    MISSING_DEP_HINT,
    build_graph,
    build_graph_with_tools,
    reason,
    route,
    route_with_tools,
)

__all__ = [
    "LANGGRAPH_AVAILABLE", "MISSING_DEP_HINT", "build_graph",
    "build_graph_with_tools", "reason", "route", "route_with_tools",
]
