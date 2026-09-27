#!/usr/bin/env python3
"""
run_redteam.py -- the Day-3 hallucination red-team and the Day-4 staleness drill.

    python scripts/run_redteam.py --suite unanswerable
    python scripts/run_redteam.py --suite staleness --chunks data/index/chunks_v2.jsonl
    python scripts/run_redteam.py --suite conflict  --chunks data/index/chunks_v2.jsonl
    python scripts/run_redteam.py --suite tau-sweep       # choose tau with evidence

The tau sweep is the part participants skip and then cannot defend in the
capstone. A refusal threshold is not a number you pick; it is a point you choose
on a curve between "refuses when it shouldn't" and "answers when it shouldn't",
and DECISIONS.md must show the curve.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.config import settings                                      # noqa: E402
from dalil.index.collection import load_chunks                         # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext       # noqa: E402
from dalil.generate.pipeline import Dalil                              # noqa: E402
from dalil.evaluation.staleness_redteam import compare, run_drill      # noqa: E402


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--suite", choices=["unanswerable", "staleness", "conflict", "tau-sweep"],
                    default="unanswerable")
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--model", default=None)
    ap.add_argument("--tau", type=float, default=None)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()

    chunks = load_chunks(a.chunks)
    backend = MemoryBackend(chunks, dense=True, model_name=a.model)
    dalil = Dalil(backend, ctx=AccessContext(max_tier="restricted"))

    if a.suite == "unanswerable":
        rows = load_jsonl(ROOT / "data/redteam/unanswerable.jsonl")
        results = []
        for r in rows:
            t = dalil.ask(r["question"], tau=a.tau)
            results.append({"id": r["id"], "language": r["language"], "trap": r["trap"],
                            "refused": t.refused, "answer": t.answer[:200],
                            "retrieved_doc_ids": t.retrieved_doc_ids[:3]})
        n = len(results) or 1
        refused = sum(r["refused"] for r in results)
        report = {"suite": "unanswerable", "n": len(results),
                  "refusal_rate": round(refused / n, 4),
                  "target": 0.95,
                  "verdict": "PASS" if refused / n >= 0.95 else "FAIL",
                  "by_language": {
                      lang: round(sum(r["refused"] for r in results if r["language"] == lang)
                                  / max(sum(1 for r in results if r["language"] == lang), 1), 4)
                      for lang in {r["language"] for r in results}},
                  "rows": results}
        out = a.out or ROOT / "reports/redteam_unanswerable.json"

    elif a.suite == "staleness":
        probes = load_jsonl(ROOT / "data/redteam/staleness.jsonl")
        report = compare(dalil, probes)
        report["suite"] = "staleness"
        out = a.out or ROOT / "reports/staleness.json"

    elif a.suite == "conflict":
        rows = load_jsonl(ROOT / "data/redteam/conflict.jsonl")
        ctx = AccessContext(max_tier="restricted", include_superseded=True)
        results = []
        for r in rows:
            t = dalil.ask(r["question"], ctx=ctx)
            cited = set(t.cited_doc_ids)
            both = len(cited & set(r["doc_ids"])) >= 2
            names_supersession = any(w in t.answer.lower()
                                     for w in ("supersed", "replaced", "ملغى", "يحل محل"))
            results.append({"id": r["id"], "cited_both": both,
                            "names_supersession": names_supersession,
                            "full_credit": both and names_supersession,
                            "cited_doc_ids": sorted(cited)})
        n = len(results) or 1
        report = {"suite": "conflict", "n": len(results),
                  "full_credit_rate": round(sum(r["full_credit"] for r in results) / n, 4),
                  "cited_both_rate": round(sum(r["cited_both"] for r in results) / n, 4),
                  "rows": results}
        out = a.out or ROOT / "reports/redteam_conflict.json"

    else:  # tau-sweep
        unans = load_jsonl(ROOT / "data/redteam/unanswerable.jsonl")
        golden = load_jsonl(ROOT / "data/golden/golden_qa_v1.jsonl")[:40]
        curve = []
        for tau in [0.0, 0.1, 0.2, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.8]:
            refused_bad = sum(dalil.ask(r["question"], tau=tau).refused for r in unans)
            refused_good = sum(dalil.ask(r["question"], tau=tau).refused for r in golden)
            curve.append({"tau": tau,
                          "refusal_recall": round(refused_bad / max(len(unans), 1), 4),
                          "over_refusal": round(refused_good / max(len(golden), 1), 4)})
        best = max(curve, key=lambda c: c["refusal_recall"] - c["over_refusal"])
        report = {"suite": "tau-sweep", "curve": curve, "suggested_tau": best["tau"],
                  "note": "Suggested tau maximises (refusal_recall - over_refusal). "
                          "Re-run after ANY change to the retrieval stack — the score "
                          "distribution moves and the threshold moves with it."}
        out = a.out or ROOT / "reports/tau_sweep.json"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ("rows", "curve")},
                     ensure_ascii=False, indent=2))
    if "curve" in report:
        print("  tau   refusal_recall  over_refusal")
        for c in report["curve"]:
            print(f"  {c['tau']:<5} {c['refusal_recall']:<15} {c['over_refusal']}")
    print(f"-> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
