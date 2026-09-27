#!/usr/bin/env python3
"""
run_retrieval_eval.py -- Lab 3 and Lab 4's number-producing script.

Runs the labelled query set against a chosen retrieval configuration and emits
both the aggregate table and the per-class table. Ablations are first-class
here because the labs are ablations:

    --mode sparse     BM25 only          (why identifier queries work)
    --mode dense      vectors only       (why they don't)
    --mode hybrid     RRF fusion         (Lab 4 step 1)
    --mode reranked   hybrid + rerank    (Lab 4 step 2)

    --model sentence-transformers/all-MiniLM-L6-v2   the English-only contrast
    --ef 32,64,128,256                               the Lab 3 sweep

Example
    python scripts/run_retrieval_eval.py --mode reranked --out reports/retrieval.json
    python scripts/run_retrieval_eval.py --mode dense --model .../all-MiniLM-L6-v2
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.config import settings                                    # noqa: E402
from dalil.index.collection import load_chunks                       # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext, build_backend  # noqa: E402
from dalil.retrieve.hybrid import hybrid_search                      # noqa: E402
from dalil.retrieve.rerank import rerank                             # noqa: E402
from dalil.evaluation.retrieval_metrics import evaluate_retrieval, latency_summary  # noqa: E402
from dalil.evaluation.by_class import evaluate_by_class, render_markdown  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--labels", type=Path, default=ROOT / "data/retrieval_labels.jsonl")
    ap.add_argument("--mode", choices=["sparse", "dense", "hybrid", "reranked"],
                    default="hybrid")
    ap.add_argument("--model", default=None)
    ap.add_argument("--backend", choices=["memory", "qdrant", "auto"], default="memory")
    ap.add_argument("--fetch-k", type=int, default=None)
    ap.add_argument("--top-k", type=int, default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--corpus-version", choices=["v1", "v2"], default="v1",
                    help="score only labels answerable in this corpus version")
    ap.add_argument("--out", type=Path, default=ROOT / "reports/retrieval.json")
    ap.add_argument("--by-class-out", type=Path, default=ROOT / "reports/by_class.json")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args()

    chunks = load_chunks(a.chunks)
    labels = [json.loads(l) for l in a.labels.read_text(encoding="utf-8").splitlines() if l.strip()]
    labels = [l for l in labels
              if a.corpus_version in l.get("corpus", ["v1", "v2"])]
    if a.limit:
        labels = labels[: a.limit]

    need_dense = a.mode in {"dense", "hybrid", "reranked"}
    backend = (MemoryBackend(chunks, dense=need_dense, model_name=a.model)
               if a.backend == "memory" else build_backend(chunks, kind=a.backend))
    ctx = AccessContext(max_tier="restricted")

    notes = []
    if need_dense and isinstance(backend, MemoryBackend) and not backend.dense_enabled:
        notes.append("dense leg unavailable — results are BM25-only and NOT a valid "
                     "dense/hybrid measurement. Reason: "
                     + getattr(backend, "dense_error", "unknown"))

    fetch_k = a.fetch_k or settings.fetch_k
    top_k = a.top_k or settings.top_k
    results, lat = [], []
    for row in labels:
        q = row["query"]
        t0 = time.perf_counter()
        if a.mode == "sparse":
            hits = backend.search_sparse(q, fetch_k, ctx)
        elif a.mode == "dense":
            hits = backend.search_dense(q, fetch_k, ctx)
        else:
            hits = hybrid_search(backend, q, fetch_k=fetch_k, ctx=ctx)
            if a.mode == "reranked":
                hits, _ = rerank(q, hits, top_k=max(top_k, 20))
        lat.append((time.perf_counter() - t0) * 1000)
        # dedupe to document level, preserving rank
        seen, docs = set(), []
        for h in hits:
            if h.doc_id not in seen:
                seen.add(h.doc_id)
                docs.append(h.doc_id)
        results.append({"query": q, "retrieved": docs,
                        "relevant": row["relevant_doc_ids"],
                        "query_class": row.get("query_class", "unclassified"),
                        "language": row.get("language", "en")})

    agg = evaluate_retrieval(results)
    agg["latency"] = latency_summary(lat)
    agg["config"] = {"mode": a.mode, "model": a.model or settings.embed_model,
                     "fetch_k": fetch_k, "top_k": top_k, "backend": a.backend,
                     "ef": settings.hnsw_ef_search}
    agg["notes"] = notes
    byc = evaluate_by_class(results)

    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    a.by_class_out.write_text(json.dumps(byc, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"mode={a.mode}  model={agg['config']['model']}  queries={agg['queries']}")
    for k in ("recall@1", "recall@5", "recall@10", "mrr@10", "ndcg@6"):
        print(f"  {k:12s} {agg[k]:.4f}")
    for k in sorted(x for x in agg if x.startswith("recall@10::")):
        print(f"  {k:12s} {agg[k]:.4f}  (n={agg['n::' + k.split('::')[1]]})")
    print(f"  latency      {agg['latency']}")
    print()
    print(render_markdown(byc))
    for n in notes:
        print(f"\n[warn] {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
