"""Lab 1 solution — Task 2.

Thin re-export, not a fork: the real, complete `RafeeqState` lives in
`src/rafeeq/core/state.py` (it is the SAME type every later lab's
solution extends, per the SPEC's canonical layout). This file exists so
`labs/lab01/solution/` is a complete, runnable answer key on its own,
without duplicating the implementation.
"""
from __future__ import annotations

from rafeeq.core.state import LANGGRAPH_AVAILABLE, RafeeqState, new_state

__all__ = ["RafeeqState", "new_state", "LANGGRAPH_AVAILABLE"]
