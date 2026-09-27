#!/usr/bin/env python3
"""demo.py -- `make demo`: the six-minute capstone demo, scripted.

Runs, in order, the five things the rubric asks a participant to show:
  1. one English question answered with verifiable citations
  2. one Arabic question answered with verifiable citations
  3. one unanswerable question correctly refused
  4. the staleness toggle: same question, lifecycle filtering on then off
  5. the access-control check: the same question as two different roles

If any stage cannot run, it says why and continues. A demo that dies on stage 1
tells the grader nothing about stages 2-5.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.index.collection import load_chunks                        # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext, build_backend  # noqa: E402
from dalil.generate.pipeline import Dalil                             # noqa: E402

BAR = "─" * 78


def show(title: str, trace):
    print(f"\n{BAR}\n{title}\n{BAR}")
    print(f"Q: {trace.question}")
    print(f"A: {trace.answer[:400]}")
    print(f"   class={trace.query_class} refused={trace.refused} "
          f"cited={trace.cited_doc_ids or '—'}")
    if trace.invented_citations:
        print(f"   !! invented citations: {trace.invented_citations}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks_v2.jsonl")
    ap.add_argument("--model", default=None)
    ap.add_argument("--backend", choices=["memory", "qdrant", "auto"], default="memory")
    a = ap.parse_args()

    path = a.chunks if a.chunks.exists() else ROOT / "data/index/chunks.jsonl"
    if not path.exists():
        print("No index found. Run:  make corpus && make eval-sets && make ingest")
        return 1
    chunks = load_chunks(path)
    backend = (MemoryBackend(chunks, dense=True, model_name=a.model)
               if a.backend == "memory" else build_backend(chunks, kind=a.backend))
    d = Dalil(backend, ctx=AccessContext(max_tier="restricted"))
    print(f"Dalil demo · {len(chunks)} chunks · {path.name}")

    show("1 · English question with citations",
         d.ask("What is the monthly housing allowance for Grade 11?"))
    show("2 · Arabic question with citations",
         d.ask("ما الحد الأقصى لاستحقاق بدل السكن وفق سياسة بدل السكن؟"))
    show("3 · Unanswerable question — must refuse",
         d.ask("What is the parental leave entitlement for contractors on secondment?"))

    stale = ROOT / "data/redteam/staleness.jsonl"
    if stale.exists():
        probe = json.loads(stale.read_text(encoding="utf-8").splitlines()[0])
        show("4a · Staleness — lifecycle filtering ON (correct)",
             d.ask(probe["question"], ctx=AccessContext(max_tier="restricted")))
        show("4b · Staleness — filtering OFF (F8 returns)",
             d.ask(probe["question"],
                   ctx=AccessContext(max_tier="restricted", include_superseded=True)))
        print(f"\n  current value: {probe['current_value']}   "
              f"superseded value: {probe['stale_value']}")

    q = "What is the monthly housing allowance for Grade 11?"
    show("5a · Access control — finance role", d.ask(q, ctx=AccessContext(
        max_tier="restricted", departments={"finance"})))
    show("5b · Access control — public role (must not see restricted pay data)",
         d.ask(q, ctx=AccessContext(max_tier="public")))
    print(f"\n{BAR}\nDemo complete. Open EVALUATION.md next — the numbers are the argument.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
