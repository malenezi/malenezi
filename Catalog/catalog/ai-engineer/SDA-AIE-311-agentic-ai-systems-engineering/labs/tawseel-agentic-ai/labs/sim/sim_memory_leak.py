#!/usr/bin/env python3
"""sim_memory_leak — Module 4, `labs/lab04`.

Symptom:    A retrieval meant for one customer returns another customer's
            private note.
Root cause: Querying the underlying vector store DIRECTLY, without a
            `customer_id` metadata filter applied BEFORE ranking — the
            store will happily return the semantically-closest chunk
            across EVERY customer's memories.
Fix:        `rafeeq.memory.long_term.recall()` always filters by
            `customer_id` BEFORE ranking (Module 4's metadata-filter-
            first rule) — never after, never optionally.

Run: `PYTHONPATH=src python3 labs/sim/sim_memory_leak.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.memory.long_term import _customer_store, recall, remember

CUSTOMER_A = "CUST-SIM-LEAK-A"
CUSTOMER_B = "CUST-SIM-LEAK-B"
SECRET_NOTE_A = "Customer requested all future refunds go to a NEW card ending 4471, kept confidential."


def unfiltered_recall(situation: str, k: int = 3) -> list[str]:
    """THE ANTI-PATTERN: query the store directly, no customer_id filter
    — exactly what a developer who forgot the filter (or "optimised" it
    away) would write."""
    store = _customer_store()
    hits = store.similarity_search(situation, k=k)  # no filter= argument at all
    return [h.page_content for h in hits]


def main() -> int:
    remember(CUSTOMER_A, SECRET_NOTE_A, "preference", "en")
    remember(CUSTOMER_B, "Customer prefers delivery notifications by SMS.", "preference", "en")

    query = "what card should refunds go to?"

    print(f"-- broken: unfiltered_recall(customer B's situation) --  query={query!r}")
    leaked = unfiltered_recall(query)
    leak_found = any(SECRET_NOTE_A in text for text in leaked)
    for text in leaked:
        print(f"  hit: {text}")
    print(f"  customer A's private note leaked into an UNSCOPED query: {leak_found}\n")

    print(f"-- fixed: recall(customer_id={CUSTOMER_B!r}, ...) --")
    scoped = recall(CUSTOMER_B, query)
    leak_blocked = not any(SECRET_NOTE_A in text for text in scoped)
    for text in scoped:
        print(f"  hit: {text}")
    print(f"  customer A's note excluded from customer B's scoped recall: {leak_blocked}\n")

    ok = leak_found and leak_blocked
    print("FAILURE DEMONSTRATED (unscoped leak) AND FIX PROVEN (scoped recall)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
