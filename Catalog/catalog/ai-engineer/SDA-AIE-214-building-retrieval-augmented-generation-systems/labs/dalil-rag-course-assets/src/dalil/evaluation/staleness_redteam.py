"""The staleness red-team — the F8 verdict, in numbers. Module 6 / Day 4.

The drill:
  1. Index corpus_v1. Ask the 12 supersession questions. Record the answers.
  2. Layer corpus_v2 on top and re-index. The v1 circulars are now superseded
     and their v2 editions are current.
  3. Ask the SAME 12 questions.

Three outcomes, and only one of them is passing:

  answered_current    cites the v2 figure                       <- required
  answered_stale      cites the superseded v1 figure            <- F8, the bug
  refused             says it cannot tell                       <- honest, but
                                                                   a helpfulness
                                                                   failure here

Then the toggle: run once with lifecycle filtering ON and once OFF. A system
that scores identically both ways is not filtering — it got lucky on ranking,
and it will serve a stale policy the first week the corpus grows. The capstone
requires the toggle demonstrated live for exactly this reason.

Target: answered_stale <= 0.02 with filtering on.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from ..retrieve.backends import AccessContext


def score_answer(answer: str, current_value: str, stale_value: str,
                 refused: bool) -> str:
    if refused:
        return "refused"
    a = answer.replace(",", "")
    has_cur = str(current_value) in a
    has_stale = str(stale_value) in a
    if has_cur and not has_stale:
        return "answered_current"
    if has_stale and not has_cur:
        return "answered_stale"
    if has_cur and has_stale:
        return "answered_both"          # acceptable only if it names the supersession
    return "answered_neither"


def run_drill(dalil, probes: list[dict], *, include_superseded: bool = False) -> dict:
    ctx = AccessContext(max_tier="restricted", include_superseded=include_superseded)
    rows = []
    for p in probes:
        trace = dalil.ask(p["question"], ctx=ctx)
        verdict = score_answer(trace.answer, p["current_value"], p["stale_value"],
                               trace.refused)
        rows.append({
            "id": p["id"], "question": p["question"], "verdict": verdict,
            "cited_doc_ids": trace.cited_doc_ids,
            "retrieved_doc_ids": trace.retrieved_doc_ids,
            "cited_superseded": any(d.endswith("-v1") for d in trace.cited_doc_ids),
            "stub": trace.stub,
        })
    n = len(rows) or 1
    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    return {
        "lifecycle_filtering": "off" if include_superseded else "on",
        "n": len(rows),
        "counts": counts,
        "answered_stale": round(counts.get("answered_stale", 0) / n, 4),
        "answered_current": round(counts.get("answered_current", 0) / n, 4),
        "refused": round(counts.get("refused", 0) / n, 4),
        "cited_superseded_rate": round(sum(r["cited_superseded"] for r in rows) / n, 4),
        "rows": rows,
    }


def compare(dalil, probes: list[dict]) -> dict:
    on = run_drill(dalil, probes, include_superseded=False)
    off = run_drill(dalil, probes, include_superseded=True)
    delta = round(off["answered_stale"] - on["answered_stale"], 4)
    stub = any(r.get("stub") for r in on["rows"])
    neither = on["counts"].get("answered_neither", 0) / max(on["n"], 1)

    # A low answered_stale is only evidence if the system was ANSWERING. A run
    # where nothing was answered scores a perfect 0.00 and proves nothing, and a
    # run where the filter changes nothing means the filter is not the reason.
    # Both are reported as INCONCLUSIVE rather than PASS, because a false PASS
    # here is exactly the failure the drill exists to catch.
    if stub:
        verdict = "INCONCLUSIVE"
        why = ("answers came from the offline stub model — the drill measured the "
               "plumbing, not the behaviour. Re-run with a gateway key.")
    elif neither > 0.3:
        verdict = "INCONCLUSIVE"
        why = (f"{neither:.0%} of probes produced neither figure — the system is not "
               f"answering these questions at all, so a low answered_stale is not "
               f"evidence of freshness. Fix retrieval first.")
    elif delta <= 0.01:
        verdict = "INCONCLUSIVE"
        why = ("turning lifecycle filtering off changed nothing, so the filter is not "
               "what is keeping you fresh — you got lucky on ranking. Check that "
               "lifecycle is populated on every chunk and that the filter is applied.")
    elif on["answered_stale"] <= 0.02:
        verdict = "PASS"
        why = "stale answers suppressed with filtering on, and the toggle demonstrably matters."
    else:
        verdict = "FAIL"
        why = f"answered_stale = {on['answered_stale']:.3f} exceeds the 0.02 gate."

    return {
        "filtering_on": on, "filtering_off": off,
        "delta_answered_stale": delta,
        "answered_neither_rate": round(neither, 4),
        "stub_run": stub,
        "verdict": verdict,
        "why": why,
    }
