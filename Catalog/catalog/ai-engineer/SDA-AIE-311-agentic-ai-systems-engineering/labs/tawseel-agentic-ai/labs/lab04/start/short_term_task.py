"""Lab 4, Task 1 — thread-scoped short-term memory via a SQLite checkpointer.

Layer B: `langgraph.checkpoint.sqlite.SqliteSaver` is required. This file
import-guards it exactly like every other graph-layer module in this
repo (SPEC §1) — it still IMPORTS cleanly under plain python3; only
`get_checkpointed_agent`/`handle_turn` need the real dependency.

Prove the point with TWO turns on the SAME `thread_id`: the second turn
refers to "it" without repeating the order id, and the agent still
resolves it — because the checkpointer resumed the conversation instead
of starting from nothing.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import REPO_ROOT, get_settings

try:
    from rafeeq.core.graph import build_graph_with_tools, LANGGRAPH_AVAILABLE
except ImportError:
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "This task needs `langgraph` (SqliteSaver) — install with:\n"
    "    pip install langgraph langchain-core langgraph-checkpoint-sqlite\n"
    "The memory/PDPL logic itself (long_term_task.py, knowledge_base_task.py) "
    "needs none of this and already runs offline."
)


def thread_id_for(customer_id: str, channel: str = "app", session_date: str | None = None) -> str:
    """Provided: the thread-id convention `"{customer_id}:{channel}:{date}"`
    — `long_term_task.py`'s `forget_customer` companion in the real
    module (`memory/long_term.py::_erase_checkpoints_for_customer`) scopes
    erasure by matching THIS exact prefix, so keep the format stable."""
    if session_date is None:
        session_date = datetime.now(timezone.utc).date().isoformat()
    return f"{customer_id}:{channel}:{session_date}"


def get_checkpointer() -> Any:
    """TODO(lab 4.1a): return a `SqliteSaver` pointed at a lab-local file
    (e.g. `REPO_ROOT / "data" / "checkpoints" / "lab04_checkpoints.sqlite"`,
    creating the parent directory). `from langgraph.checkpoint.sqlite
    import SqliteSaver`, then `SqliteSaver.from_conn_string(path)`.
    """
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)
    raise NotImplementedError("TODO(lab 4.1a): implement get_checkpointer")


_compiled_agent: Any = None


def get_checkpointed_agent(reset: bool = False) -> Any:
    """TODO(lab 4.1b): compile `build_graph_with_tools()` WITH
    `checkpointer=get_checkpointer()`, caching the result in the module
    global `_compiled_agent` so repeated turns reuse the SAME compiled
    graph (recompiling per turn would defeat checkpointing)."""
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)
    raise NotImplementedError("TODO(lab 4.1b): implement get_checkpointed_agent")


def handle_turn(customer_msg: str, thread_id: str, customer_id: str, locale: str = "ar") -> str:
    """TODO(lab 4.1c): invoke `get_checkpointed_agent()` with
    `config={"configurable": {"thread_id": thread_id}}` and the usual
    initial-state dict; return the last message's `.content`. Call this
    TWICE with the SAME `thread_id` to prove Task 1's continuity claim.
    """
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)
    raise NotImplementedError("TODO(lab 4.1c): implement handle_turn")
