"""Lab 4, Task 4 — ground refund answers in the versioned bilingual KB.

`data/policies/{en,ar}/*.md` (current, `policy_version: "2026.2"`) and
`data/policies/superseded/{en,ar}/*.md` (`policy_version: "2026.1"`, a
DIFFERENT refund threshold) are both ingested by the real
`rafeeq.memory.knowledge_base.seed_kb()` — reused here so this lab starts
from real, already-seeded policy content instead of hand-built fixtures.
Fill in the TODO: retrieval that NEVER surfaces the superseded version.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import CURRENT_POLICY_VERSION
from rafeeq.memory.knowledge_base import POLICY_KB_COLLECTION, seed_kb  # provided: ingestion
from rafeeq.memory.vector_store import get_store


def policy_context_task(question: str, locale: str, k: int = 3) -> str:
    """TODO(lab 4.4): retrieve the CURRENT policy version ONLY.

    1. `store = get_store(POLICY_KB_COLLECTION)` (call `seed_kb()` first,
       once, if you have not already — it is idempotent-ish, safe to call
       more than once in a lab session).
    2. `hits = store.similarity_search(question, k=k, filter=
       {"policy_version": CURRENT_POLICY_VERSION, "locale": locale})`
    3. Return `"\\n\\n".join(h.page_content for h in hits)` or the
       sentinel string `"NO_POLICY_FOUND"` if `hits` is empty.

    Test it cross-lingually: an ARABIC question about refunds should
    retrieve the ARABIC policy chunk (not nothing, not the English one) —
    `HashingEmbeddings` (`core/embeddings.py`) bridges AR<->EN vocabulary,
    but only if you actually pass `locale` through to the filter.

    Troubleshooting row this avoids: "Agent quotes an old policy" ->
    "Retrieving all versions" -> fix: "Filter on CURRENT_POLICY_VERSION."
    """
    raise NotImplementedError("TODO(lab 4.4): implement policy_context_task")
