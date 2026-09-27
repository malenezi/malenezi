#!/usr/bin/env python3
"""
run_golden_set.py -- run Dalil over the golden Q&A set and emit RAGAS-ready
samples plus the grounding/citation/refusal table.

Lab 6 step 1, and the source of Table 4 and Table 5 in EVALUATION.md.

    python scripts/run_golden_set.py --out reports/golden_run.jsonl
    python -m dalil.evaluation.ragas_harness --samples reports/golden_run.jsonl --offline
    python -m dalil.evaluation.gate --current reports/ragas_report.json

Note on `--allow-stub`: with no gateway key the answer model is a deterministic
stub. That exercises every piece of plumbing -- retrieval, context assembly,
citation resolution, refusal -- and produces a grounding table that is REAL
(citations either resolve or they don't). It does NOT produce meaningful answer
quality, and every output row is stamped `stub: true` so no one mistakes it for
an evaluation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.index.collection import load_chunks                      # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext, build_backend  # noqa: E402
from dalil.generate.pipeline import Dalil                            # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--golden", type=Path, default=ROOT / "data/golden/golden_qa_v1.jsonl")
    ap.add_argument("--backend", choices=["memory", "qdrant", "auto"], default="memory")
    ap.add_argument("--model", default=None, help="embedding model")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--skip-verify", action="store_true",
                    help="skip Layer A rows whose ground truth is not yet resolved")
    ap.add_argument("--out", type=Path, default=ROOT / "reports/golden_run.jsonl")
    ap.add_argument("--grounding-out", type=Path, default=ROOT / "reports/grounding.json")
    a = ap.parse_args()

    chunks = load_chunks(a.chunks)
    rows = [json.loads(l) for l in a.golden.read_text(encoding="utf-8").splitlines() if l.strip()]
    if a.skip_verify:
        rows = [r for r in rows if not r.get("verify")]
    if a.limit:
        rows = rows[: a.limit]

    backend = (MemoryBackend(chunks, dense=True, model_name=a.model)
               if a.backend == "memory" else build_backend(chunks, kind=a.backend))
    dalil = Dalil(backend, ctx=AccessContext(max_tier="restricted"))

    samples, traces = [], []
    for r in rows:
        t = dalil.ask(r["question"])
        traces.append((r, t))
        samples.append({
            "id": r["id"], "question": r["question"], "answer": t.answer,
            "contexts": [c for c in _context_texts(t, chunks)],
            "ground_truth": r.get("ground_truth", ""),
            "query_class": r.get("query_class"), "language": r.get("language", "en"),
            "refused": t.refused, "stub": t.stub,
            "cited_doc_ids": t.cited_doc_ids,
            "relevant_doc_ids": r.get("relevant_doc_ids", []),
        })

    a.out.parent.mkdir(parents=True, exist_ok=True)
    with a.out.open("w", encoding="utf-8") as fh:
        for s in samples:
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")

    # ---- grounding / citation / refusal table (Table 4) -------------------
    n = len(traces) or 1
    answered = [t for _, t in traces if not t.refused]
    must_refuse = [(r, t) for r, t in traces if not r.get("relevant_doc_ids")]
    grounding = {
        "n": len(traces),
        "answered": len(answered),
        "refused": len(traces) - len(answered),
        "answers_with_citations": round(
            sum(1 for t in answered if t.citations) / max(len(answered), 1), 4),
        "invented_citation_rate": round(
            sum(1 for t in answered if t.invented_citations) / max(len(answered), 1), 4),
        "citation_resolves_to_retrieved": round(
            mean([1.0 if set(t.cited_chunk_ids) <= set(t.retrieved_chunk_ids) else 0.0
                  for t in answered] or [0.0]), 4),
        "correct_doc_in_retrieved": round(
            mean([1.0 if set(r.get("relevant_doc_ids", [])) & set(t.retrieved_doc_ids)
                  else 0.0 for r, t in traces if r.get("relevant_doc_ids")] or [0.0]), 4),
        "cited_correct_doc": round(
            mean([1.0 if set(r.get("relevant_doc_ids", [])) & set(t.cited_doc_ids)
                  else 0.0 for r, t in traces if r.get("relevant_doc_ids")] or [0.0]), 4),
        "refusal_on_unanswerable": round(
            mean([1.0 if t.refused else 0.0 for _, t in must_refuse] or [0.0]), 4),
        "latency_ms_p50": sorted(t.latency_ms["total_ms"] for _, t in traces)[len(traces)//2]
        if traces else 0,
        "stub_run": any(t.stub for _, t in traces),
    }
    if grounding["stub_run"]:
        grounding["warning"] = ("answers came from the offline stub model — citation and "
                                "refusal plumbing is real, answer quality is not measured")
    a.grounding_out.write_text(json.dumps(grounding, ensure_ascii=False, indent=2),
                               encoding="utf-8")

    print(f"golden set: {len(traces)} questions")
    for k, v in grounding.items():
        print(f"  {k:34s} {v}")
    print(f"-> {a.out}\n-> {a.grounding_out}")
    return 0


def _context_texts(trace, chunks) -> list[str]:
    by_id = {c["chunk_id"]: c["text"] for c in chunks}
    return [by_id.get(cid, "") for cid in trace.retrieved_chunk_ids]


if __name__ == "__main__":
    raise SystemExit(main())
