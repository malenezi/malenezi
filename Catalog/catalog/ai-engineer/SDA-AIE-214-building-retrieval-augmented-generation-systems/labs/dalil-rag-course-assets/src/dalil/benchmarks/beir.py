"""BEIR — the metrics lab's proving ground. Module 3 / Module 6.

BEIR's value here is structural, not competitive. Every one of its 18 datasets
ships the same three objects:

    corpus   {doc_id: {"title", "text"}}
    queries  {query_id: text}
    qrels    {query_id: {doc_id: relevance_grade}}

Because the shape never changes, recall@k / MRR / nDCG code written once for
Dalil runs unmodified across nine different IR task types. That is the exercise:
participants point THEIR metric implementations at BEIR and check the numbers
against published baselines. If their nDCG@10 on SciFact with a known model is
far off the published figure, the bug is in their metric code, and they have
just avoided grading their whole capstone with a broken ruler.

Recommended datasets for a 20-hour course (small, fast, and each teaching
something different about the metric, not the model):

    scifact     ~5k docs   claim verification; graded relevance; tiny and quick
    nfcorpus    ~3.6k      medical, heavy vocabulary mismatch -> where dense wins
    fiqa        ~57k       financial opinion QA; long queries
    trec-covid   ~171k     deeply graded judgements (0/1/2) -> nDCG vs recall
                           diverge here, which is the lesson

    python -m dalil.benchmarks.beir --dataset scifact
    python -m dalil.benchmarks.beir --dataset scifact --sparse-only   # BM25 contrast
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import evaluate_run, save
from ..config import settings

SUGGESTED = ["scifact", "nfcorpus", "fiqa", "trec-covid", "arguana", "quora"]
SAMPLE = Path(__file__).resolve().parents[3] / "data" / "benchmarks" / "beir_scifact_sample.json"


def load_beir(dataset: str, split: str = "test"):
    """Prefers the `beir` package; falls back to the HF mirror; then to sample."""
    try:
        from beir import util
        from beir.datasets.data_loader import GenericDataLoader
        url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset}.zip"
        path = util.download_and_unzip(url, "data/benchmarks/beir")
        corpus, queries, qrels = GenericDataLoader(data_folder=path).load(split=split)
        corpus = {k: f"{v.get('title','')}\n{v.get('text','')}" for k, v in corpus.items()}
        return corpus, queries, qrels, "full"
    except Exception:
        pass
    from datasets import load_dataset
    c = load_dataset(f"BeIR/{dataset}", "corpus", split="corpus")
    q = load_dataset(f"BeIR/{dataset}", "queries", split="queries")
    r = load_dataset(f"BeIR/{dataset}-qrels", split=split)
    corpus = {str(x["_id"]): f"{x.get('title','')}\n{x.get('text','')}" for x in c}
    queries = {str(x["_id"]): x["text"] for x in q}
    qrels: dict[str, dict[str, float]] = {}
    for x in r:
        qrels.setdefault(str(x["query-id"]), {})[str(x["corpus-id"])] = float(x["score"])
    return corpus, queries, qrels, "full"


def load_sample():
    d = json.loads(SAMPLE.read_text(encoding="utf-8"))
    return d["corpus"], d["queries"], d["qrels"], "sample"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dataset", default="scifact", help=f"one of {', '.join(SUGGESTED)}")
    ap.add_argument("--split", default="test")
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--sparse-only", action="store_true")
    ap.add_argument("--model", default=None)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()

    notes = []
    if a.sample:
        corpus, queries, qrels, mode = load_sample()
        notes.append("BUNDLED SAMPLE — sanity check only, not a BEIR score.")
    else:
        try:
            corpus, queries, qrels, mode = load_beir(a.dataset, a.split)
        except Exception as exc:
            corpus, queries, qrels, mode = load_sample()
            notes.append(f"falling back to bundled sample: {type(exc).__name__}: {exc}")

    qlist = []
    for qid, rel in qrels.items():
        if qid not in queries:
            continue
        qlist.append({"qid": qid, "text": queries[qid],
                      "relevant": {d: float(g) for d, g in rel.items()}})
        if a.limit and len(qlist) >= a.limit:
            break

    chunks = [{"chunk_id": k, "doc_id": k, "text": v} for k, v in corpus.items()]
    from ..retrieve.backends import MemoryBackend, AccessContext
    from ..retrieve.hybrid import hybrid_search
    backend = MemoryBackend(chunks, dense=not a.sparse_only, model_name=a.model)
    ctx = AccessContext(max_tier="restricted")
    if not a.sparse_only and not backend.dense_enabled:
        notes.append("dense leg unavailable — BM25-only numbers. Reason: "
                     + getattr(backend, "dense_error", "unknown"))

    def search(text: str, k: int) -> list[str]:
        if a.sparse_only or not backend.dense_enabled:
            return [h.doc_id for h in backend.search_sparse(text, k, ctx)]
        return [h.doc_id for h in hybrid_search(backend, text, fetch_k=k, ctx=ctx)]

    res = evaluate_run(f"BEIR/{a.dataset}", mode, qlist, search,
                       n_documents=len(corpus),
                       config={"model": a.model or settings.embed_model,
                               "sparse_only": a.sparse_only, "split": a.split},
                       notes=notes)
    print(res.render())
    out = a.out or Path(f"reports/benchmarks/beir_{a.dataset}.json")
    save(res, out)
    print(f"-> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
