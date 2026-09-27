"""Per-query-class reporting — the report that actually changes decisions.

Module 4, and a hard requirement of the capstone rubric.

The story this table tells, every cohort, without fail:

    class          dense-only   +hybrid   +rerank
    identifier        0.31       0.86      0.89     <- sparse did this
    tabular           0.55       0.71      0.84     <- reranker did this
    factoid           0.82       0.84      0.91
    multi_hop         0.34       0.38      0.41     <- Module 7's problem
    aggregate         0.63       0.72      0.79     <- hides all of the above

The aggregate column moves 0.16 and tells you nothing about WHY. The identifier
row moves 0.55 and names the fix. This is why "our recall went up" is not an
engineering statement and this table is.
"""
from __future__ import annotations

from collections import defaultdict
from statistics import mean

from .retrieval_metrics import recall_at_k, ndcg_at_k, mrr


def evaluate_by_class(results: list[dict], k: int = 10, ndcg_k: int = 6) -> dict:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in results:
        buckets[r.get("query_class", "unclassified")].append(r)

    table = {}
    for cls, rows in sorted(buckets.items()):
        table[cls] = {
            "n": len(rows),
            f"recall@{k}": round(mean(recall_at_k(r["retrieved"], set(r["relevant"]), k)
                                      for r in rows), 4),
            f"ndcg@{ndcg_k}": round(mean(
                ndcg_at_k(r["retrieved"],
                          r.get("relevance") or {d: 1.0 for d in r["relevant"]}, ndcg_k)
                for r in rows), 4),
            "mrr@10": round(mean(mrr(r["retrieved"], set(r["relevant"]), 10)
                                 for r in rows), 4),
        }
    agg = {
        "n": len(results),
        f"recall@{k}": round(mean(recall_at_k(r["retrieved"], set(r["relevant"]), k)
                                  for r in results), 4) if results else 0.0,
        f"ndcg@{ndcg_k}": round(mean(
            ndcg_at_k(r["retrieved"],
                      r.get("relevance") or {d: 1.0 for d in r["relevant"]}, ndcg_k)
            for r in results), 4) if results else 0.0,
    }
    weakest = min(table, key=lambda c: table[c][f"recall@{k}"]) if table else None
    return {"by_class": table, "aggregate": agg, "weakest_class": weakest}


def render_markdown(report: dict, k: int = 10, ndcg_k: int = 6) -> str:
    rows = ["| Query class | n | recall@%d | nDCG@%d | MRR@10 |" % (k, ndcg_k),
            "|---|---:|---:|---:|---:|"]
    for cls, v in report["by_class"].items():
        rows.append(f"| {cls} | {v['n']} | {v[f'recall@{k}']:.3f} | "
                    f"{v[f'ndcg@{ndcg_k}']:.3f} | {v['mrr@10']:.3f} |")
    a = report["aggregate"]
    rows.append(f"| **aggregate** | {a['n']} | **{a[f'recall@{k}']:.3f}** | "
                f"**{a[f'ndcg@{ndcg_k}']:.3f}** | — |")
    if report.get("weakest_class"):
        rows.append(f"\nWeakest class: **{report['weakest_class']}** — fix this before "
                    f"tuning anything the aggregate rewards.")
    return "\n".join(rows)
