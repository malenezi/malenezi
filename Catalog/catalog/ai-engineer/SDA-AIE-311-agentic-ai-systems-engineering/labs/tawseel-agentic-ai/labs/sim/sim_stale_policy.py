#!/usr/bin/env python3
"""sim_stale_policy — Module 4 (memory) / Module 9 (caching), `labs/lab04`
and `labs/lab09`.

Symptom:    Rafeeq answers a refund-eligibility question by quoting a
            policy that was already superseded.
Root cause: Retrieval (or a cache in front of it) is not scoped by
            `policy_version` — a semantically similar SUPERSEDED chunk
            can rank alongside, or replace, the current one. A cache
            keyed on the question string ALONE makes this worse: a
            policy edit does not invalidate the old cached answer at all.
Fix:        `rafeeq.memory.knowledge_base.policy_context` filters by
            `policy_version=CURRENT_POLICY_VERSION` BEFORE ranking, never
            after; `rafeeq.observability.optimise.cached_policy` keys its
            cache on `(question, locale, version)`, so a version bump is
            a cache-wide invalidation by construction.

Run: `PYTHONPATH=src python3 labs/sim/sim_stale_policy.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import CURRENT_POLICY_VERSION, SUPERSEDED_POLICY_VERSION
from rafeeq.memory.knowledge_base import policy_context, policy_context_including_superseded, seed_kb

QUESTION = "What are the eligible situations for a refund?"
LOCALE = "en"


def main() -> int:
    seed_kb()  # idempotent: (re)loads data/policies/** with policy_version metadata

    # -- broken: retrieval with no version filter -----------------------------
    print(f"-- broken: policy_context_including_superseded (no version filter) --  {QUESTION!r}")
    unfiltered = policy_context_including_superseded(QUESTION, LOCALE, k=5)
    versions_seen = {hit["metadata"].get("policy_version") for hit in unfiltered}
    superseded_surfaced = SUPERSEDED_POLICY_VERSION in versions_seen
    print(f"  policy_version(s) in the unfiltered result set: {sorted(versions_seen)}")
    print(f"  the SUPERSEDED version ({SUPERSEDED_POLICY_VERSION}) was surfaced "
          f"to the caller: {superseded_surfaced}\n")

    # -- fixed: the real, version-scoped retrieval -----------------------------
    print("-- fixed: policy_context (filters policy_version BEFORE ranking) --")
    scoped = policy_context(QUESTION, LOCALE)
    scoped_is_current_only = SUPERSEDED_POLICY_VERSION not in scoped and scoped != "NO_POLICY_FOUND"
    print(f"  result mentions the SUPERSEDED marker text: {'SUPERSEDED' in scoped}")
    print(f"  a real, non-empty, CURRENT-version-only answer was returned: {scoped_is_current_only}")
    print(f"  (CURRENT_POLICY_VERSION = {CURRENT_POLICY_VERSION})\n")

    ok = superseded_surfaced and scoped_is_current_only
    print("FAILURE DEMONSTRATED (stale policy surfaced) AND FIX PROVEN (version-scoped retrieval)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
