"""Lab 4, Tasks 2/3/5/6 — customer-scoped long-term memory + PDPL erasure.

Built on `rafeeq.memory.vector_store.get_store()` — dependency-free by
default (SimpleVectorStore, SPEC §1). Fill in the TODOs. The module's
conscience: every read below MUST filter by `customer_id` BEFORE ranking,
never as a post-hoc check — that is the entire difference between this
file and `labs/sim/sim_memory_leak.py`.
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.memory.vector_store import Document, get_store

COLLECTION = "lab04_customer_memory"
_store_cache: dict[str, Any] = {}


def _store() -> Any:
    if COLLECTION not in _store_cache:
        _store_cache[COLLECTION] = get_store(COLLECTION)
    return _store_cache[COLLECTION]


def remember(customer_id: str, summary: str, mem_type: str, locale: str) -> str:
    """TODO(lab 4.2): write ONE durable memory (a resolved-case summary,
    never a raw message dump — Module 4 mistake #3). Build a `Document`
    with `page_content=summary` and `metadata={"customer_id":
    customer_id, "type": mem_type, "locale": locale, "created_at": ...}`;
    call `_store().add_documents([doc])`; return the assigned id (the
    first element of the returned list).
    """
    raise NotImplementedError("TODO(lab 4.2): implement remember")


def recall(customer_id: str, situation: str, k: int = 3) -> list[str]:
    """TODO(lab 4.3): retrieve THIS customer's top-`k` memories relevant
    to `situation`. MUST pass `filter={"customer_id": customer_id}` to
    `_store().similarity_search(...)` — never rank first and filter
    after. Return the list of `.page_content` strings.

    Troubleshooting row this avoids: "Retrieves another customer's
    memory" -> "Missing metadata filter."
    """
    raise NotImplementedError("TODO(lab 4.3): implement recall")


def count_customer_memories(customer_id: str) -> int:
    """Provided: the erasure verification primitive."""
    return _store().count(filter={"customer_id": customer_id})


def forget_customer(customer_id: str) -> dict[str, Any]:
    """TODO(lab 4.5): PDPL erasure. Call `_store().delete(filter=
    {"customer_id": customer_id})`, then return `{"customer_id":
    customer_id, "vectors_removed": <int returned by delete>,
    "vectors_remaining": count_customer_memories(customer_id),
    "erased_at": <iso timestamp>}`. `vectors_remaining` MUST be `0` after
    a real erasure — that is the assertion Task 5 asks you to write.
    """
    raise NotImplementedError("TODO(lab 4.5): implement forget_customer")


def assert_no_leakage(customer_a: str, customer_b: str, situation: str) -> None:
    """TODO(lab 4.6): the leakage test, as a callable assertion (not a
    pytest file — keep this stdlib-runnable). Call `recall(customer_a,
    situation)` and assert NONE of the returned strings originated from
    `customer_b` — the simplest way to check this without leaking
    metadata through `recall`'s string-only return is to compare against
    `_store().similarity_search(situation, k=10, filter={"customer_id":
    customer_b})`'s content and assert the two result sets are disjoint.
    Raise `AssertionError` with a clear message on failure.
    """
    raise NotImplementedError("TODO(lab 4.6): implement assert_no_leakage")
