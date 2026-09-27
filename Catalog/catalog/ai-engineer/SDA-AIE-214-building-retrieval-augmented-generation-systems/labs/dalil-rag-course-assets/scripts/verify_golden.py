#!/usr/bin/env python3
"""
verify_golden.py -- resolve the Layer A golden questions against the fetched PDFs.

Questions about real SDAIA documents ship with `verify: true` and an
`evidence_hint` instead of a literal answer, because the shipped repository
cannot know the wording or pagination of a PDF that is downloaded at delivery
time. This script closes that loop:

  1. locate the passage in the fetched document that answers each question;
  2. print it for the instructor to approve or correct;
  3. write the approved ground truth back into golden_qa_v1.jsonl.

Run it ONCE per delivery, after `make corpus-fetch`, and commit the result. An
unverified golden set is not a measuring instrument — it is a list of hopes.

    python scripts/verify_golden.py --report      # what still needs verifying
    python scripts/verify_golden.py --interactive # approve passages one by one
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.index.collection import load_chunks                       # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext     # noqa: E402
from dalil.retrieve.hybrid import hybrid_search                      # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--golden", type=Path, default=ROOT / "data/golden/golden_qa_v1.jsonl")
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--interactive", action="store_true")
    ap.add_argument("--top", type=int, default=3)
    a = ap.parse_args()

    rows = [json.loads(l) for l in a.golden.read_text(encoding="utf-8").splitlines() if l.strip()]
    pending = [r for r in rows if r.get("verify") and not r.get("ground_truth")]

    if a.report or not a.interactive:
        print(f"golden set: {len(rows)} questions")
        print(f"  verified            {len(rows) - len(pending)}")
        print(f"  awaiting verification {len(pending)}")
        by_doc: dict[str, int] = {}
        for r in pending:
            for d in r["relevant_doc_ids"]:
                by_doc[d] = by_doc.get(d, 0) + 1
        for d, n in sorted(by_doc.items(), key=lambda kv: -kv[1]):
            print(f"    {n:3d}  {d}")
        if pending:
            print("\nRun with --interactive after `make corpus-fetch && make ingest` "
                  "to resolve them against the real documents.")
        return 0

    if not a.chunks.exists():
        print("No index. Run: make corpus-fetch && make ingest")
        return 1
    chunks = load_chunks(a.chunks)
    backend = MemoryBackend(chunks, dense=False)
    ctx = AccessContext(max_tier="restricted")

    changed = 0
    for r in pending:
        hits = hybrid_search(backend, r["question"], fetch_k=a.top, ctx=ctx)
        print("\n" + "=" * 78)
        print(f"[{r['id']}] {r['question']}")
        print(f"hint: {r.get('evidence_hint', '')}")
        if not hits:
            print("  no candidate passage found — is the document fetched and ingested?")
            continue
        for i, h in enumerate(hits[: a.top], 1):
            print(f"\n  ({i}) {h.doc_id}\n      {h.text[:500]}")
        choice = input("\n  ground truth: paste text, or 1-%d to accept a passage, "
                       "or ENTER to skip: " % min(a.top, len(hits))).strip()
        if not choice:
            continue
        if choice.isdigit() and 1 <= int(choice) <= len(hits):
            r["ground_truth"] = hits[int(choice) - 1].text[:800]
        else:
            r["ground_truth"] = choice
        r["verify"] = False
        r["verified_against"] = hits[0].doc_id
        changed += 1

    if changed:
        with a.golden.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"\n{changed} answers verified and written back to {a.golden}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
