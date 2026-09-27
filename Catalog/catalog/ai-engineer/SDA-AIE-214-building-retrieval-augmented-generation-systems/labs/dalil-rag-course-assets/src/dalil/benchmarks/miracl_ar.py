"""MIRACL Arabic — the reality check on the course's Arabic retrieval claims.

MIRACL (Multilingual Information Retrieval Across a Continuum of Languages) is
a human-annotated multilingual retrieval benchmark; its Arabic split gives
queries, a Wikipedia-derived passage corpus, and human relevance judgements.

WHY IT IS IN THIS COURSE
------------------------
Module 3 shows bge-m3 beating an English-only model on the Arabic subset of the
Dalil corpus, ~0.88 vs ~0.29. That is a compelling number and a self-graded
one: we wrote the corpus and we wrote the labels. MIRACL-ar is the independent
instrument. When a participant's Arabic recall on Dalil is high and their
MIRACL-ar recall@100 is in the published range for their model, the pipeline is
sound. When Dalil looks great and MIRACL-ar looks broken, the corpus was
flattering them — usually because their queries and passages share vocabulary
that a real user's phrasing would not.

Run it on Day 2 as a 15-minute sidebar, not as a lab. The goal is calibration,
not a leaderboard.

    python -m dalil.benchmarks.miracl_ar --limit 200
    python -m dalil.benchmarks.miracl_ar --sample        # offline, bundled rows
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import evaluate_run, save
from ..config import settings

HF_CORPUS = "miracl/miracl-corpus"       # config: "ar"
HF_QRELS = "miracl/miracl"               # config: "ar", split: "dev"
SAMPLE = Path(__file__).resolve().parents[3] / "data" / "benchmarks" / "miracl_ar_sample.json"


def load_full(limit_queries: int | None = None, limit_docs: int | None = 50000):
    from datasets import load_dataset
    corpus_ds = load_dataset(HF_CORPUS, "ar", split="train", streaming=limit_docs is not None)
    corpus: dict[str, str] = {}
    for i, row in enumerate(corpus_ds):
        if limit_docs and i >= limit_docs:
            break
        corpus[str(row["docid"])] = f"{row.get('title','')}\n{row['text']}"
    qrels_ds = load_dataset(HF_QRELS, "ar", split="dev")
    queries = []
    for row in qrels_ds:
        rel = {str(p["docid"]): 1.0 for p in row.get("positive_passages", [])}
        if limit_docs:
            rel = {d: g for d, g in rel.items() if d in corpus}
        if not rel:
            continue
        queries.append({"qid": str(row["query_id"]), "text": row["query"], "relevant": rel})
        if limit_queries and len(queries) >= limit_queries:
            break
    return corpus, queries, "full"


def load_sample():
    data = json.loads(SAMPLE.read_text(encoding="utf-8"))
    return data["corpus"], data["queries"], "sample"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=200, help="number of queries")
    ap.add_argument("--limit-docs", type=int, default=50000)
    ap.add_argument("--sample", action="store_true", help="offline bundled subset")
    ap.add_argument("--model", default=None, help="embedding model (default: bge-m3)")
    ap.add_argument("--sparse-only", action="store_true",
                    help="BM25 baseline — the contrast that makes the dense number mean something")
    ap.add_argument("--out", type=Path, default=Path("reports/benchmarks/miracl_ar.json"))
    a = ap.parse_args()

    notes = []
    if a.sample:
        corpus, queries, mode = load_sample()
        notes.append("BUNDLED SAMPLE — indicative only; not comparable to published "
                     "MIRACL numbers. Use --limit with network access for a real run.")
    else:
        try:
            corpus, queries, mode = load_full(a.limit, a.limit_docs)
            if a.limit_docs:
                notes.append(f"corpus truncated to {a.limit_docs} passages — recall is an "
                             f"UPPER bound versus the full MIRACL-ar corpus")
        except Exception as exc:
            corpus, queries, mode = load_sample()
            notes.append(f"falling back to bundled sample: {type(exc).__name__}: {exc}")

    chunks = [{"chunk_id": did, "doc_id": did, "text": text} for did, text in corpus.items()]
    from ..retrieve.backends import MemoryBackend, AccessContext
    backend = MemoryBackend(chunks, dense=not a.sparse_only, model_name=a.model)
    ctx = AccessContext(max_tier="restricted")
    if not a.sparse_only and not backend.dense_enabled:
        notes.append("dense leg unavailable — BM25-only numbers. Reason: "
                     + getattr(backend, "dense_error", "unknown"))

    def search(text: str, k: int) -> list[str]:
        if a.sparse_only or not backend.dense_enabled:
            return [h.doc_id for h in backend.search_sparse(text, k, ctx)]
        from ..retrieve.hybrid import hybrid_search
        return [h.doc_id for h in hybrid_search(backend, text, fetch_k=k, ctx=ctx)]

    res = evaluate_run("MIRACL-ar", mode, queries, search, n_documents=len(corpus),
                       config={"model": a.model or settings.embed_model,
                               "sparse_only": a.sparse_only}, notes=notes)
    print(res.render())
    save(res, a.out)
    print(f"-> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
