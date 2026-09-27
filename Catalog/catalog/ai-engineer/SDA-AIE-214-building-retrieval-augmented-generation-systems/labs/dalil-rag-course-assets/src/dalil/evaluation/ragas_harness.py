"""RAGAS evaluation with a pinned judge — and a stdlib fallback that is honest
about being one. Module 6, Lab 6.

The four metrics and what each one INDICTS when it drops:

    context_recall     retrieval  — the evidence never made it into context
    context_precision  ranking    — the evidence was there, buried under noise
    faithfulness       generation — claims not supported by the context
    answer_relevancy   generation — grounded, but not an answer to the question

That mapping is the whole reason RAG needs its own metric suite: a single
"accuracy" number cannot localise a regression, so it cannot drive a fix.

Judge discipline (non-negotiable in this course):
  * pin the judge model AND temperature=0, and record both in the report;
  * never regenerate the baseline in the same commit as a quality change;
  * treat a delta smaller than the judge's own run-to-run variance as noise —
    measure that variance once per cohort with `--repeat 3` and put the number
    in EVALUATION.md.

When `ragas` is not installed or no gateway key is present, this harness runs
`--offline`: lexical proxies for each metric, clearly flagged `judge="offline-
proxy"` in every output. The proxies are good enough to smoke-test the plumbing
and to make Lab 6 runnable on a laptop; they are NOT good enough to grade with,
and the report says so in the file itself.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from statistics import mean

from ..arabic import normalise
from ..config import settings


# --------------------------------------------------------------------------
# offline lexical proxies
# --------------------------------------------------------------------------
def _toks(text: str) -> set[str]:
    return set(normalise(text).split())


def proxy_faithfulness(answer: str, contexts: list[str]) -> float:
    """Share of answer content words that appear in the retrieved context.
    A crude but directionally correct stand-in for 'is every claim supported'."""
    a, c = _toks(answer), set().union(*(_toks(x) for x in contexts)) if contexts else set()
    a = {t for t in a if len(t) > 3}
    return round(len(a & c) / len(a), 4) if a else 0.0


def proxy_answer_relevancy(answer: str, question: str) -> float:
    q, a = _toks(question), _toks(answer)
    q = {t for t in q if len(t) > 3}
    return round(len(q & a) / len(q), 4) if q else 0.0


def proxy_context_recall(ground_truth: str, contexts: list[str]) -> float:
    g = {t for t in _toks(ground_truth) if len(t) > 3}
    c = set().union(*(_toks(x) for x in contexts)) if contexts else set()
    return round(len(g & c) / len(g), 4) if g else 0.0


def proxy_context_precision(ground_truth: str, contexts: list[str]) -> float:
    """Share of retrieved passages that overlap the reference answer at all."""
    if not contexts:
        return 0.0
    g = {t for t in _toks(ground_truth) if len(t) > 3}
    if not g:
        return 0.0
    useful = sum(1 for c in contexts if len(_toks(c) & g) >= 2)
    return round(useful / len(contexts), 4)


# --------------------------------------------------------------------------
# harness
# --------------------------------------------------------------------------
def evaluate_offline(samples: list[dict]) -> dict:
    per = []
    for s in samples:
        ctx = s.get("contexts", [])
        gt = s.get("ground_truth", "")
        per.append({
            "id": s.get("id"),
            "query_class": s.get("query_class"),
            "language": s.get("language", "en"),
            "faithfulness": proxy_faithfulness(s.get("answer", ""), ctx),
            "answer_relevancy": proxy_answer_relevancy(s.get("answer", ""),
                                                       s.get("question", "")),
            "context_recall": proxy_context_recall(gt, ctx),
            "context_precision": proxy_context_precision(gt, ctx),
        })
    metrics = {m: round(mean(p[m] for p in per), 4) for m in
               ("faithfulness", "answer_relevancy", "context_recall", "context_precision")} \
        if per else {}
    return {"judge": "offline-proxy",
            "warning": "LEXICAL PROXY METRICS — not comparable to RAGAS scores and "
                       "not valid for grading. Run with a pinned judge for real numbers.",
            "n": len(per), "metrics": metrics, "per_sample": per}


def evaluate_ragas(samples: list[dict], *, judge_model: str | None = None) -> dict:
    """Real RAGAS. Raises if unavailable so the caller can choose to go offline."""
    from ragas import evaluate
    from ragas.metrics import (faithfulness, answer_relevancy,
                               context_precision, context_recall)
    from datasets import Dataset

    judge_model = judge_model or settings.judge_model
    ds = Dataset.from_list([{
        "question": s["question"],
        "answer": s.get("answer", ""),
        "contexts": s.get("contexts", []),
        "ground_truth": s.get("ground_truth", ""),
    } for s in samples])
    result = evaluate(ds, metrics=[faithfulness, answer_relevancy,
                                   context_precision, context_recall])
    scores = {k: round(float(v), 4) for k, v in result.items()
              if isinstance(v, (int, float))}
    return {"judge": judge_model, "judge_temperature": settings.judge_temperature,
            "n": len(samples), "metrics": scores,
            "per_sample": result.to_pandas().to_dict(orient="records")}


def run(samples: list[dict], *, offline: bool = False,
        judge_model: str | None = None) -> dict:
    started = time.time()
    if not offline:
        try:
            report = evaluate_ragas(samples, judge_model=judge_model)
        except Exception as exc:
            report = evaluate_offline(samples)
            report["fallback_reason"] = f"{type(exc).__name__}: {exc}"
    else:
        report = evaluate_offline(samples)
    report["elapsed_s"] = round(time.time() - started, 1)
    report["config"] = {"embed_model": settings.embed_model,
                        "reranker": settings.reranker_model,
                        "fetch_k": settings.fetch_k, "top_k": settings.top_k,
                        "ef": settings.hnsw_ef_search,
                        "context_budget": settings.context_token_budget,
                        "refusal_tau": settings.refusal_threshold}
    # per-class and per-language breakdowns: aggregate-only RAGAS hides the
    # same regressions aggregate-only retrieval metrics do.
    per = report.get("per_sample") or []
    for dim in ("query_class", "language"):
        groups: dict[str, list] = {}
        for p in per:
            groups.setdefault(str(p.get(dim, "?")), []).append(p)
        report[f"by_{dim}"] = {
            g: {m: round(mean(x[m] for x in rows), 4)
                for m in ("faithfulness", "answer_relevancy",
                          "context_recall", "context_precision") if m in rows[0]}
            | {"n": len(rows)}
            for g, rows in sorted(groups.items()) if rows
        }
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--samples", type=Path, required=True,
                    help="JSONL produced by scripts/run_golden_set.py")
    ap.add_argument("--out", type=Path, default=Path("reports/ragas_report.json"))
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--judge-model")
    a = ap.parse_args()

    samples = [json.loads(l) for l in a.samples.read_text(encoding="utf-8").splitlines() if l.strip()]
    report = run(samples, offline=a.offline, judge_model=a.judge_model)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"judge: {report['judge']}   n={report['n']}")
    for k, v in report["metrics"].items():
        print(f"  {k:20s} {v:.4f}")
    if report.get("warning"):
        print("  " + report["warning"])
    print(f"-> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
