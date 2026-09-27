"""Module 4 — long-term (durable) memory: scoped semantic store.

`remember` / `recall` / `forget_customer`, built on
`rafeeq.memory.vector_store.get_store()` rather than a hard-coded Qdrant
client — this is what makes the whole module runnable offline (SPEC §1):
`get_store()` returns the dependency-free `SimpleVectorStore` by default
and only reaches for Qdrant when `RAFEEQ_VECTOR_MODE=qdrant` is set.

TEACHING POINT — metadata filter BEFORE ranking (Module 4 §3-4, repeated
here because it is this module's central lesson): EVERY read is scoped by
`customer_id` in the filter passed to `similarity_search`, never applied
as a post-hoc check on the results. `SimpleVectorStore.similarity_search_with_score`
already filters candidates before computing similarity (see its
docstring) — this module's job is to never bypass that by calling
`similarity_search` without a `customer_id` filter. A leakage test
(`tests/unit/test_scoping.py` covers the specialist-context version of
this; a memory-leakage regression test belongs in Lab 4's suite) is the
module's conscience.

`forget_customer` is Rafeeq's PDPL erasure path: it must remove a
customer's data from BOTH long-term memory (vectors) AND short-term
memory (checkpointed conversation threads) — a customer who exercises
their erasure right is not satisfied by half an erasure. Checkpoint
erasure talks to the checkpoint SQLite file directly (stdlib `sqlite3`,
best-effort table detection) rather than through langgraph, so it runs
even when `langgraph` is not installed (nothing to erase in that case
anyway, since no checkpointed thread could have been created without it)
and never becomes the reason PDPL erasure fails to import.
"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rafeeq.memory.vector_store import Document, get_store

CUSTOMER_MEMORY_COLLECTION = "rafeeq_customer_memory"

_store_cache: dict[str, Any] = {}


def _customer_store() -> Any:
    """Lazily fetch (and cache for this process) the vector store backing
    customer long-term memory. A single collection, kept SEPARATE from
    the policy knowledge base (`knowledge_base.py`'s own collection) so
    PII-bearing customer memory and non-personal policy content can be
    governed differently (Module 4 production note)."""
    store = _store_cache.get(CUSTOMER_MEMORY_COLLECTION)
    if store is None:
        store = get_store(CUSTOMER_MEMORY_COLLECTION)
        _store_cache[CUSTOMER_MEMORY_COLLECTION] = store
    return store


def remember(customer_id: str, summary: str, mem_type: str, locale: str) -> str:
    """Deliberate write of a DURABLE fact (e.g. a resolved-case summary,
    a stable preference) — never a raw message dump (Module 4 mistake
    #3). Returns the assigned document id. `mem_type` is a free-text tag
    (`"resolved_case"`, `"preference"`, ...) callers use to filter recall
    further if needed."""
    store = _customer_store()
    [doc_id] = store.add_documents([Document(page_content=summary, metadata={
        "customer_id": customer_id, "type": mem_type, "locale": locale,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })])
    return doc_id


def recall(customer_id: str, situation: str, k: int = 3) -> list[str]:
    """Retrieve THIS customer's most relevant memories — filtered by
    `customer_id` BEFORE ranking, then ranked by semantic similarity to
    `situation`. Cross-lingual by construction: `HashingEmbeddings`
    bridges the AR<->EN domain vocabulary (see `core/embeddings.py`), so
    an Arabic `situation` can retrieve an English memory and vice versa."""
    store = _customer_store()
    hits = store.similarity_search(
        situation, k=k, filter={"customer_id": customer_id})
    return [h.page_content for h in hits]


def recall_with_metadata(customer_id: str, situation: str, k: int = 3) -> list[dict[str, Any]]:
    """Like `recall`, but returns the full `{content, metadata}` record —
    useful for audit/trace display where `created_at`/`type` matter, not
    just the text a prompt would consume."""
    store = _customer_store()
    hits = store.similarity_search(
        situation, k=k, filter={"customer_id": customer_id})
    return [{"content": h.page_content, "metadata": h.metadata} for h in hits]


def count_customer_memories(customer_id: str) -> int:
    """Non-ranked count of a customer's stored memories — the erasure
    verification primitive (`forget_customer` should drive this to zero)."""
    return _customer_store().count(filter={"customer_id": customer_id})


# --------------------------------------------------------------------------
# PDPL erasure: vectors AND checkpoints.
# --------------------------------------------------------------------------
_CHECKPOINT_TABLES = ("checkpoints", "checkpoint_blobs", "checkpoint_writes", "writes")


def _erase_checkpoints_for_customer(customer_id: str) -> int:
    """Best-effort deletion of every checkpointed thread belonging to
    `customer_id` from the SQLite checkpoint database, by `thread_id`
    prefix (see `memory/short_term.py`'s `thread_id_for` convention:
    `"{customer_id}:{channel}:{session_date}"`, so a `LIKE` prefix match
    on `thread_id` scopes correctly to this customer and no other).

    Talks to the SQLite file directly via stdlib `sqlite3` rather than
    through a langgraph checkpointer object, so this runs whether or not
    `langgraph` is installed — and if the checkpoint DB file does not
    exist (no langgraph session has ever run), there is nothing to erase,
    which is not an error.
    """
    from rafeeq.memory.short_term import _default_sqlite_path

    db_path = Path(_default_sqlite_path())
    if not db_path.exists():
        return 0

    removed = 0
    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        existing_tables = {row[0] for row in cur.fetchall()}
        pattern = f"{customer_id}:%"
        for table in _CHECKPOINT_TABLES:
            if table not in existing_tables:
                continue
            cur.execute(f"PRAGMA table_info({table})")
            columns = {row[1] for row in cur.fetchall()}
            if "thread_id" not in columns:
                continue
            cur.execute(f"DELETE FROM {table} WHERE thread_id LIKE ?", (pattern,))  # noqa: S608 - table from a fixed allowlist
            removed += max(cur.rowcount, 0)
        conn.commit()
    finally:
        conn.close()
    return removed


def forget_customer(customer_id: str, also_checkpoints: bool = True) -> dict[str, Any]:
    """PDPL erasure: remove ALL of `customer_id`'s durable memory
    (vectors), and — by default — their short-term checkpointed
    conversation threads too. A partial erasure (vectors only) is not a
    real erasure from the customer's point of view; `also_checkpoints`
    exists only so a caller that has already erased checkpoints via
    another path (or is calling from a context with no checkpoint DB at
    all) can skip redundant work, never as a way to silently ship a
    vectors-only "forget".

    Returns a small audit-friendly summary rather than `None` (unlike the
    instructor package's minimal sketch) so the erasure is itself a
    logged, verifiable event — exactly Module 4's "erasure completeness"
    benchmark (100% of a customer's data removed) needs something to
    check against.
    """
    store = _customer_store()
    vectors_removed = store.delete(filter={"customer_id": customer_id})

    checkpoints_removed = 0
    checkpoints_error: str | None = None
    if also_checkpoints:
        try:
            checkpoints_removed = _erase_checkpoints_for_customer(customer_id)
        except Exception as exc:  # noqa: BLE001 - erasure of vectors must still be reported
            checkpoints_error = str(exc)

    return {
        "customer_id": customer_id,
        "vectors_removed": vectors_removed,
        "vectors_remaining": count_customer_memories(customer_id),
        "checkpoints_removed": checkpoints_removed,
        "checkpoints_error": checkpoints_error,
        "erased_at": datetime.now(timezone.utc).isoformat(),
    }
