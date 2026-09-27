"""Retrieval metrics, implemented rather than imported. Module 3, Lab 3.

Three metrics, three different questions — and knowing which one to quote is
half of Module 4:

  recall@k   Did the right document make the shortlist AT ALL?
             This is the retriever's job. If recall@40 is low, nothing
             downstream can save the answer: reranking cannot promote a chunk
             that was never fetched, and the LLM cannot cite what it never saw.

  MRR        How high was the FIRST correct result?
             Right metric when exactly one document answers the question
             (identifier lookups). Blind to the second and third results.

  nDCG@k     How good is the WHOLE ordering, discounted by position?
             The right headline metric for the reranker, because the reranker's
             entire job is ordering. Supports graded relevance, which matters
             on this corpus where an Arabic edition of the same policy is
             partially relevant rather than wrong.

Aggregate-only reporting is the anti-pattern the capstone rubric punishes: a
mean of 0.71 across classes routinely hides an identifier class at 0.31. Always
pair these with by_class.evaluate_by_class.
"""
from __future__ import annotations

import math
from statistics import mean


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    hits = len(set(retrieved[:k]) & relevant)
    return hits / len(relevant)


def hit_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    return 1.0 if set(retrieved[:k]) & relevant else 0.0


def mrr(retrieved: list[str], relevant: set[str], k: int | None = None) -> float:
    seq = retrieved[:k] if k else retrieved
    for i, r in enumerate(seq, start=1):
        if r in relevant:
            return 1.0 / i
    return 0.0


def dcg(gains: list[float]) -> float:
    return sum(g / math.log2(i + 1) for i, g in enumerate(gains, start=1))


def ndcg_at_k(retrieved: list[str], relevance: dict[str, float], k: int) -> float:
    """Graded nDCG. `relevance` maps id -> gain (0, 1, 2, ...)."""
    gains = [relevance.get(r, 0.0) for r in retrieved[:k]]
    ideal = sorted(relevance.values(), reverse=True)[:k]
    idcg = dcg(ideal)
    return (dcg(gains) / idcg) if idcg > 0 else 0.0


def evaluate_retrieval(results: list[dict], ks: tuple[int, ...] = (1, 5, 10, 20)) -> dict:
    """`results`: [{query, retrieved:[doc_id...], relevant:[doc_id...],
                    relevance:{doc_id:gain}, query_class, language}, ...]"""
    if not results:
        return {"queries": 0}
    out: dict = {"queries": len(results)}
    for k in ks:
        out[f"recall@{k}"] = round(mean(
            recall_at_k(r["retrieved"], set(r["relevant"]), k) for r in results), 4)
        out[f"hit@{k}"] = round(mean(
            hit_at_k(r["retrieved"], set(r["relevant"]), k) for r in results), 4)
    out["mrr@10"] = round(mean(mrr(r["retrieved"], set(r["relevant"]), 10)
                               for r in results), 4)
    for k in (6, 10):
        out[f"ndcg@{k}"] = round(mean(
            ndcg_at_k(r["retrieved"],
                      r.get("relevance") or {d: 1.0 for d in r["relevant"]}, k)
            for r in results), 4)
    langs = {r.get("language", "en") for r in results}
    for lang in sorted(langs):
        subset = [r for r in results if r.get("language", "en") == lang]
        out[f"recall@10::{lang}"] = round(mean(
            recall_at_k(r["retrieved"], set(r["relevant"]), 10) for r in subset), 4)
        out[f"n::{lang}"] = len(subset)
    return out


def latency_summary(latencies_ms: list[float]) -> dict:
    if not latencies_ms:
        return {}
    s = sorted(latencies_ms)
    return {"p50_ms": round(s[len(s) // 2], 1),
            "p95_ms": round(s[max(int(len(s) * 0.95) - 1, 0)], 1),
            "max_ms": round(s[-1], 1), "n": len(s)}
