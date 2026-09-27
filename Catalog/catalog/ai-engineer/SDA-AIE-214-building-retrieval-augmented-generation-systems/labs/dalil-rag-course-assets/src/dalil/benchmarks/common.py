"""Shared benchmark plumbing: one corpus/queries/qrels shape, one scorer."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, Iterable

from ..evaluation.retrieval_metrics import (recall_at_k, mrr, ndcg_at_k,
                                            latency_summary)


@dataclass
class BenchmarkResult:
    name: str
    mode: str                      # "full" | "sample"
    n_queries: int
    n_documents: int
    metrics: dict = field(default_factory=dict)
    latency: dict = field(default_factory=dict)
    config: dict = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    def render(self) -> str:
        head = (f"{self.name}  [{self.mode}]  queries={self.n_queries} "
                f"docs={self.n_documents}")
        rows = "\n".join(f"  {k:14s} {v:.4f}" if isinstance(v, float) else f"  {k:14s} {v}"
                         for k, v in self.metrics.items())
        lat = ("  latency " + json.dumps(self.latency)) if self.latency else ""
        notes = "\n".join(f"  ! {n}" for n in self.notes)
        return "\n".join(x for x in (head, rows, lat, notes) if x)


def evaluate_run(name: str, mode: str, queries: list[dict], search: Callable,
                 *, ks: Iterable[int] = (1, 5, 10, 100), n_documents: int = 0,
                 config: dict | None = None, notes: list[str] | None = None
                 ) -> BenchmarkResult:
    """`queries`: [{qid, text, relevant: {docid: gain}}]
    `search(text, k) -> [docid, ...]`"""
    ks = tuple(ks)
    top = max(ks)
    per_recall = {k: [] for k in ks}
    per_ndcg10, per_mrr10, lat = [], [], []

    for q in queries:
        t0 = time.perf_counter()
        ranked = search(q["text"], top)
        lat.append((time.perf_counter() - t0) * 1000)
        rel = q["relevant"]
        relevant_set = {d for d, g in rel.items() if g > 0}
        for k in ks:
            per_recall[k].append(recall_at_k(ranked, relevant_set, k))
        per_ndcg10.append(ndcg_at_k(ranked, rel, 10))
        per_mrr10.append(mrr(ranked, relevant_set, 10))

    n = len(queries) or 1
    metrics = {f"recall@{k}": round(sum(v) / n, 4) for k, v in per_recall.items()}
    metrics["ndcg@10"] = round(sum(per_ndcg10) / n, 4)
    metrics["mrr@10"] = round(sum(per_mrr10) / n, 4)
    return BenchmarkResult(name=name, mode=mode, n_queries=len(queries),
                           n_documents=n_documents, metrics=metrics,
                           latency=latency_summary(lat), config=config or {},
                           notes=notes or [])


def save(result: BenchmarkResult, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result.to_dict(), ensure_ascii=False, indent=2),
                   encoding="utf-8")
