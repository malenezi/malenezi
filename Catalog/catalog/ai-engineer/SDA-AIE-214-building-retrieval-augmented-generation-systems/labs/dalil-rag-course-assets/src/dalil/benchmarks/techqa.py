"""TechQA / eManual (RAGBench) — the enterprise support assistant, and the only
public set in this course that grades REFUSAL.

Why it earns a place beside MIRACL and BEIR: TechQA is built from real technical
support questions against real product documentation, and a substantial share of
its questions are DELIBERATELY UNANSWERABLE from the supplied corpus. Every
other benchmark rewards retrieving something. This one punishes answering when
you should not — which is the exact behaviour the capstone requires (>= 95%
correct refusal) and the exact behaviour a support assistant fails at in
production.

It also mirrors the shape of the assistant most participants will actually be
asked to build at work: heterogeneous manuals, jargon-dense queries, an
audience that will act on the answer.

Metrics reported here:
    retrieval        recall@k / nDCG@10 on the answerable subset only
    refusal_recall   share of unanswerable questions the system refused
    false_answer     share of unanswerable questions it answered anyway  <- F7
    over_refusal     share of ANSWERABLE questions it wrongly refused

The last one matters as much as the third. A system that refuses everything
scores perfectly on refusal and is worthless — that is the gaming pattern the
capstone rubric caps at 70%.

    python -m dalil.benchmarks.techqa --sample
    python -m dalil.benchmarks.techqa --dataset rungalileo/ragbench --config techqa
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import BenchmarkResult, evaluate_run, save
from ..config import settings

SAMPLE = Path(__file__).resolve().parents[3] / "data" / "benchmarks" / "techqa_sample.json"


def load_ragbench(dataset: str, config: str, split: str = "test", limit: int = 200):
    from datasets import load_dataset
    ds = load_dataset(dataset, config, split=split)
    corpus: dict[str, str] = {}
    queries = []
    for i, row in enumerate(ds):
        if limit and i >= limit:
            break
        docs = row.get("documents") or []
        ids = []
        for j, d in enumerate(docs):
            did = f"{i}-{j}"
            corpus[did] = d if isinstance(d, str) else str(d)
            ids.append(did)
        answerable = bool(str(row.get("response", "")).strip()) and \
            not row.get("unanswerable", False)
        queries.append({
            "qid": str(i), "text": row.get("question", ""),
            "relevant": {d: 1.0 for d in ids} if answerable else {},
            "answerable": answerable,
            "reference": row.get("response", ""),
        })
    return corpus, queries, "full"


def load_sample():
    d = json.loads(SAMPLE.read_text(encoding="utf-8"))
    return d["corpus"], d["queries"], "sample"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dataset", default="rungalileo/ragbench")
    ap.add_argument("--config", default="techqa")
    ap.add_argument("--split", default="test")
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--tau", type=float, default=None,
                    help="refusal threshold to evaluate (sweep this!)")
    ap.add_argument("--out", type=Path, default=Path("reports/benchmarks/techqa.json"))
    a = ap.parse_args()

    notes = []
    if a.sample:
        corpus, queries, mode = load_sample()
        notes.append("BUNDLED SAMPLE — plumbing check only.")
    else:
        try:
            corpus, queries, mode = load_ragbench(a.dataset, a.config, a.split, a.limit)
        except Exception as exc:
            corpus, queries, mode = load_sample()
            notes.append(f"falling back to bundled sample: {type(exc).__name__}: {exc}")

    chunks = [{"chunk_id": k, "doc_id": k, "text": v} for k, v in corpus.items()]
    from ..retrieve.backends import MemoryBackend, AccessContext
    from ..retrieve.hybrid import hybrid_search
    from ..generate.context import assemble_context
    from ..generate.answer import evidence_strength

    backend = MemoryBackend(chunks, dense=False)
    ctx = AccessContext(max_tier="restricted")
    tau = settings.refusal_threshold if a.tau is None else a.tau

    def search(text: str, k: int) -> list[str]:
        return [h.doc_id for h in hybrid_search(backend, text, fetch_k=k, ctx=ctx)]

    answerable = [q for q in queries if q["relevant"]]
    res = evaluate_run(f"TechQA/{a.config}", mode, answerable, search,
                       n_documents=len(corpus),
                       config={"tau": tau, "model": settings.embed_model}, notes=notes)

    # --- the refusal half of the benchmark --------------------------------
    refused_unanswerable = wrongly_answered = over_refused = 0
    n_unans = sum(1 for q in queries if not q["relevant"])
    for q in queries:
        hits = hybrid_search(backend, q["text"], fetch_k=settings.fetch_k, ctx=ctx)
        blocks, _ = assemble_context(hits, ctx=ctx)
        would_refuse = (not blocks) or evidence_strength(blocks) < tau
        if not q["relevant"]:
            refused_unanswerable += int(would_refuse)
            wrongly_answered += int(not would_refuse)
        else:
            over_refused += int(would_refuse)

    res.metrics["refusal_recall"] = round(refused_unanswerable / max(n_unans, 1), 4)
    res.metrics["false_answer_rate"] = round(wrongly_answered / max(n_unans, 1), 4)
    res.metrics["over_refusal_rate"] = round(over_refused / max(len(answerable), 1), 4)
    res.notes.append(f"unanswerable questions: {n_unans} / {len(queries)}")
    res.notes.append("Sweep --tau and plot refusal_recall against over_refusal_rate: "
                     "that curve, not a single number, is how a refusal threshold is chosen.")
    print(res.render())
    save(res, a.out)
    print(f"-> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
