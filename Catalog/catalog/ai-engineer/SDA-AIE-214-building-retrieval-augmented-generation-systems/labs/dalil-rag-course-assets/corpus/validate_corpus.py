#!/usr/bin/env python3
"""
validate_corpus.py -- does the corpus, as actually assembled, still support the labs?

Run after `fetch_corpus.py` (Layer A) and `build_layer_b.py` (Layer B).

The question this answers is not "did every download succeed" — some will not,
because government publication URLs move. It is the operationally useful one:
**given what we actually have, which labs still work and which are degraded?**
It prints a per-lab verdict so an instructor discovers a gap a week out rather
than at 09:05 on Day 2.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load(p: Path, default=None):
    if not p.exists():
        return default
    return (json.loads(p.read_text(encoding="utf-8")) if p.suffix == ".json"
            else yaml.safe_load(p.read_text(encoding="utf-8")))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, default=ROOT / "corpus/manifest/sdaia_layer_a.yaml")
    ap.add_argument("--lock", type=Path, default=ROOT / "corpus/LOCK.json")
    ap.add_argument("--layer-b", type=Path, default=ROOT / "data/corpus/layer_b_index.json")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on any degradation")
    a = ap.parse_args()

    man = load(a.manifest, {}) or {}
    lock = load(a.lock, {}) or {}
    lb = load(a.layer_b, {}) or {}

    a_ok = [d for d in lock.get("documents", []) if d.get("status") == "OK"]
    a_missing = [d["id"] for d in lock.get("documents", []) if d.get("status") != "OK"]
    b_docs = lb.get("documents", [])
    fmt = Counter(d["format"] for d in b_docs)
    tiers = Counter(d.get("access_tier") for d in b_docs)
    superseded = sum(1 for d in b_docs
                     if (d.get("lifecycle_by_corpus") or {}).get("v2") == "superseded")

    print("LAYER A — real SDAIA documents")
    print(f"  resolved            {len(a_ok)} / {len(man.get('documents', []))}")
    if a_missing:
        print(f"  unresolved          {', '.join(a_missing)}")
    print("\nLAYER B — synthetic internal overlay")
    print(f"  documents           {len(b_docs)}")
    print(f"  formats             {dict(fmt)}")
    print(f"  access tiers        {dict(tiers)}")
    print(f"  superseded pairs    {superseded}")

    # ---- per-lab verdicts -------------------------------------------------
    checks = [
        ("Lab 1  naive baseline + failure gallery",
         len(b_docs) >= 25, "needs >= 25 documents of any kind"),
        ("Lab 2  ingestion / OCR / chunking",
         fmt.get("pdf_scanned", 0) >= 15 and fmt.get("xlsx", 0) >= 5,
         "needs scanned Arabic PDFs and XLSX tables"),
        ("Lab 2  OCR CER gate",
         (ROOT / "data/corpus/ocr_gold").exists(),
         "needs ocr_gold transcripts"),
        ("Lab 3  bilingual recall",
         sum(1 for d in b_docs if d.get("language") in {"ar", "bilingual"}) >= 30,
         "needs a substantial Arabic subset"),
        ("Lab 4  identifier / hybrid retrieval",
         sum(1 for d in b_docs if d.get("circular_id")) >= 20,
         "needs identifier-bearing circulars"),
        ("Lab 5  access control",
         tiers.get("restricted", 0) >= 30,
         "needs restricted-tier documents to filter"),
        ("Lab 6  RAGAS golden set",
         (ROOT / "data/golden/golden_qa_v1.jsonl").exists(),
         "run scripts/build_eval_sets.py"),
        ("Lab 7  multi-hop across layers",
         len(a_ok) >= 6,
         "cross-layer multi-hop questions need real SDAIA documents fetched"),
        ("Day 4 staleness drill",
         superseded >= 10, "needs >= 10 superseded/current pairs"),
        ("Near-duplicate reranking demo",
         {"open-data-policy", "data-sharing-policy"} <= {d["id"] for d in a_ok},
         "needs BOTH the Open Data and Data Sharing policies"),
    ]
    print("\nPER-LAB READINESS")
    degraded = 0
    for name, ok, why in checks:
        print(f"  [{'ok ' if ok else 'GAP'}] {name}" + ("" if ok else f"  <- {why}"))
        degraded += (not ok)

    targets = man.get("targets", {})
    if len(a_ok) < targets.get("min_documents_resolved", 10):
        print(f"\n[warn] Layer A below its target of "
              f"{targets.get('min_documents_resolved')} resolved documents. The labs "
              f"still run on Layer B, but the corpus loses its authority — participants "
              f"are no longer debugging retrieval over regulation their organisation "
              f"is actually bound by. Re-run corpus/fetch_corpus.py from a networked "
              f"machine and refresh corpus/LOCK.json.")

    print(f"\n{len(checks) - degraded}/{len(checks)} labs fully supported")
    return 1 if (a.strict and degraded) else 0


if __name__ == "__main__":
    raise SystemExit(main())
