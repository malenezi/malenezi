"""Module 4 — short-term (working) memory via a LangGraph checkpointer.

The Module-1 `RafeeqState` IS short-term memory; a checkpointer persists
it keyed by `thread_id`, which is what turns a single call into a
resumable, inspectable, multi-turn conversation:

  - **Resumability** — a run interrupted (human handoff, crash, waiting on
    an async tool) resumes exactly where it paused.
  - **Human-in-the-loop** — pause before a high-stakes action for
    approval, then continue from the checkpoint (M8).
  - **Time-travel & audit** — every state transition is a snapshot,
    inspectable/replayable (the auditability M1 promised).
  - **Multi-turn continuity** — the same `thread_id` carries context
    across a customer's back-and-forth without re-sending the whole
    conversation as raw prompt history.

`thread_id` convention (BINDING for every caller of `handle_turn`):

    "{customer_id}:{channel}:{session_date}"
    e.g. "CUST-4471:app:2026-03-04"

  - Scoped to ONE customer and ONE channel so two concurrent
    conversations (app + call centre, say) never merge state.
  - `session_date` (YYYY-MM-DD, Riyadh local date) starts a fresh thread
    each day rather than accumulating an unbounded history forever — the
    Module 4 "confusing short-term with long-term" mistake, avoided by
    construction: durable facts belong in `memory/long_term.py`, not in
    an ever-growing checkpointed thread. A caller that genuinely wants
    one long-running thread (e.g. an internal ops console) may pass any
    other caller-chosen stable string instead; the convention above is
    the DEFAULT `thread_id_for()` builds, not a hard requirement.

Backing store: SQLite by default (`RAFEEQ_CHECKPOINT_DB`, a local file —
zero setup, what every lab runs against) or Postgres when
`RAFEEQ_CHECKPOINT_BACKEND=postgres` (`RAFEEQ_CHECKPOINT_DSN`) for a
shared, multi-process deployment. Both are Layer-B (langgraph checkpoint
savers) and import-guarded; this module always imports under plain
python3.
"""
from __future__ import annotations

import os
from typing import Any

from rafeeq.core.config import REPO_ROOT, get_settings
from rafeeq.core.graph import build_graph_with_tools

MISSING_DEP_HINT = (
    "Short-term (checkpointed) memory requires `langgraph` plus one of "
    "`langgraph-checkpoint-sqlite` (default, SPEC §1 offline-first) or "
    "`langgraph-checkpoint-postgres` (RAFEEQ_CHECKPOINT_BACKEND=postgres). "
    "Install with:\n"
    "    pip install langgraph langchain-core langgraph-checkpoint-sqlite\n"
    "or, for Postgres:\n"
    "    pip install langgraph langchain-core langgraph-checkpoint-postgres"
)

try:  # pragma: no cover - exercised only when langgraph is installed
    import langgraph  # noqa: F401

    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


def thread_id_for(customer_id: str, channel: str = "app", session_date: str | None = None) -> str:
    """Build a `thread_id` following the convention above. `session_date`
    defaults to today's UTC date (ISO, YYYY-MM-DD) when not supplied —
    callers running in a specific timezone should pass it explicitly."""
    if session_date is None:
        from datetime import datetime, timezone

        session_date = datetime.now(timezone.utc).date().isoformat()
    return f"{customer_id}:{channel}:{session_date}"


def _default_sqlite_path() -> str:
    settings = get_settings()
    override = os.environ.get("RAFEEQ_CHECKPOINT_DB")
    if override:
        return override
    checkpoints_dir = REPO_ROOT / "data" / "checkpoints"
    checkpoints_dir.mkdir(parents=True, exist_ok=True)
    return str(checkpoints_dir / f"rafeeq_checkpoints_{settings.model_mode}.sqlite")


def get_checkpointer(backend: str | None = None) -> Any:
    """Return a LangGraph checkpointer. `backend` defaults to
    `RAFEEQ_CHECKPOINT_BACKEND` (env), itself defaulting to `sqlite` — the
    zero-setup option every lab and the eval harness use. Pass
    `backend="postgres"` (and set `RAFEEQ_CHECKPOINT_DSN`) for a shared
    deployment (SPEC's Module-4 code block uses `PostgresSaver` directly;
    this factory keeps that path available while making sqlite the
    offline-friendly default)."""
    _require_langgraph()
    backend = backend or os.environ.get("RAFEEQ_CHECKPOINT_BACKEND", "sqlite")

    if backend == "postgres":
        from langgraph.checkpoint.postgres import PostgresSaver  # type: ignore[import-not-found]

        dsn = os.environ.get("RAFEEQ_CHECKPOINT_DSN", "postgresql://localhost/rafeeq")
        return PostgresSaver.from_conn_string(dsn)

    from langgraph.checkpoint.sqlite import SqliteSaver  # type: ignore[import-not-found]

    return SqliteSaver.from_conn_string(_default_sqlite_path())


_compiled_agent: Any = None


def get_checkpointed_agent(reset: bool = False) -> Any:
    """The Module-3/4 tool-using graph compiled with a checkpointer —
    lazily built once per process (rebuilding a compiled graph per turn
    would defeat the point of checkpointing: the SAME compiled graph must
    be invoked across turns for a `thread_id` to resume anything)."""
    global _compiled_agent
    _require_langgraph()
    if _compiled_agent is None or reset:
        _compiled_agent = build_graph_with_tools().compile(checkpointer=get_checkpointer())
    return _compiled_agent


def handle_turn(customer_msg: str, thread_id: str, customer_id: str, locale: str = "ar") -> str:
    """Drive one turn of the checkpointed agent. A LATER call with the
    SAME `thread_id` resumes the checkpointed state — no need to re-send
    the whole conversation as raw prompt history (that is precisely what
    short-term memory buys you)."""
    _require_langgraph()
    agent = get_checkpointed_agent()
    cfg = {"configurable": {"thread_id": thread_id}}   # thread = short-term scope
    out = agent.invoke(
        {"messages": [("user", customer_msg)], "customer_id": customer_id, "locale": locale},
        config=cfg)
    return out["messages"][-1].content
