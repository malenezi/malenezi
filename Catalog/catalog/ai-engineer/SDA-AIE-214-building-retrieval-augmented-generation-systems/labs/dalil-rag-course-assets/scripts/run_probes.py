#!/usr/bin/env python3
"""run_probes.py -- Lab 1's probe runner and the failure-gallery scaffold.

    make probe SET=easy
    make probe SET=failure_gallery

For the failure gallery it prints, per probe: the answer, the retrieved chunk
ids, whether the expected evidence was retrieved and whether it was cited, and
leaves the failure-class column BLANK. Participants fill that column themselves
by inspecting the retrieved chunks — the pedagogy is diagnosis, and a runner
that pre-labels the failures does the learning for them.

`--key` prints the instructor reference classification. It is a separate flag
for a reason: do not run it on the projector before the lab.
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", default="failure_gallery", dest="probe_set")
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--model", default=None)
    ap.add_argument("--backend", choices=["memory", "qdrant", "auto"], default="memory")
    ap.add_argument("--delay", type=float, default=0.0, help="seconds between probes "
                    "(use when the gateway rate-limits you)")
    ap.add_argument("--key", action="store_true", help="INSTRUCTOR ONLY: show the answer key")
    ap.add_argument("--out", type=Path, default=ROOT / "reports/probe_run.json")
    a = ap.parse_args()

    import time
    path = ROOT / f"data/probes/{a.probe_set}.jsonl"
    probes = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    chunks = load_chunks(a.chunks)
    backend = (MemoryBackend(chunks, dense=True, model_name=a.model)
               if a.backend == "memory" else build_backend(chunks, kind=a.backend))
    dalil = Dalil(backend, ctx=AccessContext(max_tier="restricted"))

    rows = []
    print(f"\n{len(probes)} probes · set={a.probe_set}\n" + "=" * 78)
    for p in probes:
        t = dalil.ask(p["question"])
        expected = set(p.get("expected_doc_ids", []))
        retrieved_ok = bool(expected & set(t.retrieved_doc_ids)) if expected else None
        cited_ok = bool(expected & set(t.cited_doc_ids)) if expected else None
        contains = [s for s in p.get("expected_answer_contains", [])
                    if s.replace(",", "") in t.answer.replace(",", "")]
        rows.append({"id": p["id"], "question": p["question"], "answer": t.answer,
                     "refused": t.refused,
                     "retrieved_doc_ids": t.retrieved_doc_ids,
                     "retrieved_chunk_ids": t.retrieved_chunk_ids[:6],
                     "cited_doc_ids": t.cited_doc_ids,
                     "expected_doc_ids": sorted(expected),
                     "expected_evidence_retrieved": retrieved_ok,
                     "expected_evidence_cited": cited_ok,
                     "expected_strings_present": contains,
                     "must_refuse": p.get("must_refuse", False),
                     "failure_class": ""})
        print(f"\n[{p['id']}] {p['question']}")
        print(f"  answer   : {t.answer[:150]}")
        print(f"  retrieved: {t.retrieved_doc_ids[:4]}")
        print(f"  expected : {sorted(expected) or '— (must refuse)'}"
              f"   in top-k: {retrieved_ok}   cited: {cited_ok}")
        if p.get("must_refuse"):
            print(f"  REFUSED  : {t.refused}   <- required")
        print("  failure class: ____   evidence: ______________________________")
        if a.key and "failure_class" in p:
            print(f"  [KEY] {p['failure_class']}: {p['why']}")
        if a.delay:
            time.sleep(a.delay)

    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n" + "=" * 78)
    print(f"{len(rows)} probes answered -> {a.out}")
    print("Now write FAILURE_GALLERY.md: one row per probe, with the failure class "
          "and one sentence of EVIDENCE from the retrieved chunks (not from the answer).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
