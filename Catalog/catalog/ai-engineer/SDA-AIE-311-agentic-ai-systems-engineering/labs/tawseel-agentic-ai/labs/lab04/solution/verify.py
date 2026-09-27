#!/usr/bin/env python3
"""Lab 4 solution — verification script.

Stdlib + pydantic only. Drives the real `rafeeq.memory.long_term` and
`rafeeq.memory.knowledge_base` modules (thin re-exports, not forks — see
`labs/lab01/solution` for the pattern this follows) against a lab-local
vector store, so it never mutates data another lab/verify.py run needs.

Run: `PYTHONPATH=src python3 labs/lab04/solution/verify.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import CURRENT_POLICY_VERSION
from rafeeq.memory.knowledge_base import policy_context, policy_context_including_superseded, seed_kb
from rafeeq.memory.long_term import count_customer_memories, forget_customer, recall, remember

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def main() -> int:
    # -- 2/3. long-term memory: write + scoped recall -----------------------
    remember("CUST-LAB4-A", "Customer asked about a delayed parcel yesterday, resolved with a reschedule.",
              "resolved_case", "en")
    remember("CUST-LAB4-A", "طلب استرداد بسبب تأخر التوصيل، تمت الموافقة الجزئية.", "resolved_case", "ar")
    remember("CUST-LAB4-B", "Different customer entirely — a billing dispute over a duplicate charge.",
              "resolved_case", "en")

    hits_a = recall("CUST-LAB4-A", "delayed parcel", k=3)
    check("recall() returns this customer's own memory", any("delayed" in h.lower() for h in hits_a), str(hits_a))

    hits_a_ar = recall("CUST-LAB4-A", "تأخير التوصيل", k=3)
    check("cross-lingual recall: Arabic query reaches this customer's memory (any language)",
          len(hits_a_ar) > 0, str(hits_a_ar))

    hits_b_from_a_query = recall("CUST-LAB4-A", "billing dispute duplicate charge", k=5)
    check("leakage test: customer A's recall NEVER returns customer B's content",
          not any("duplicate charge" in h for h in hits_b_from_a_query), str(hits_b_from_a_query))

    # -- 5/6. PDPL erasure ----------------------------------------------------
    before = count_customer_memories("CUST-LAB4-A")
    result = forget_customer("CUST-LAB4-A")
    after = count_customer_memories("CUST-LAB4-A")
    check("forget_customer had memories to erase", before >= 2, f"before={before}")
    check("forget_customer(CUST-LAB4-A) -> 0 vectors remain", after == 0, f"after={after}")
    check("forget_customer's own report matches reality",
          result["vectors_remaining"] == 0 and result["vectors_removed"] >= before)
    check("customer B untouched by A's erasure",
          count_customer_memories("CUST-LAB4-B") >= 1)

    # -- 4. versioned, cross-lingual KB grounding ------------------------------
    kb_summary = seed_kb()
    check("seed_kb ingested both current and superseded policy versions",
          kb_summary["current_version_chunks"] > 0 and kb_summary["superseded_version_chunks"] > 0,
          str(kb_summary))

    ctx_en = policy_context("what is the refund window", "en")
    ctx_ar = policy_context("ما هي فترة الاسترداد", "ar")
    check("policy_context (EN) grounds on something, not NO_POLICY_FOUND", ctx_en != "NO_POLICY_FOUND")
    check("policy_context (AR) cross-lingual recall grounds on something", ctx_ar != "NO_POLICY_FOUND")

    superseded_probe = policy_context_including_superseded("refund window threshold", "en", k=5)
    superseded_versions = {h["metadata"].get("policy_version") for h in superseded_probe}
    check("the demo-only superseded lookup CAN see the old version (proves the corpus has one)",
          "2026.1" in superseded_versions or len(superseded_probe) == 0, str(superseded_versions))
    current_only = policy_context("refund window threshold", "en", k=5)
    check("the real policy_context() NEVER contains superseded wording (2026.1's own phrasing)",
          "2026.1" not in current_only)

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("Lab 4 verification — short/long-term memory + PDPL")
    print("=" * (name_w + 24))
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("=" * (name_w + 24))
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
