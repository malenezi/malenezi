"""Render EVALUATION.md — the artefact a risk officer reads and signs.

The capstone is graded evidence-first. This module turns the five benchmark
JSON files into the five tables the rubric expects, so participants spend their
Day-4 afternoon improving numbers rather than formatting them.

Deliberately plain markdown: it has to survive being pasted into a governance
pack, printed, and read by someone who will never open the repository.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .by_class import render_markdown as render_by_class

TEMPLATE = """# EVALUATION.md — Dalil (دليل)

**System:** {system}
**Corpus:** {corpus}
**Date:** {date}
**Judge:** `{judge}` (temperature {judge_temp}) · **Config:** {config}

> How to read this document: each table below answers one question about the
> system. If you read only one thing, read Table 5 — it is the safety evidence.

---

## Table 1 — Ingestion coverage and chunk quality

{t1}

## Table 2 — Retrieval: recall and latency

{t2}

## Table 3 — Retrieval by query class

{t3}

## Table 4 — Grounding, citations and refusal

{t4}

## Table 5 — Answer quality (RAGAS) and anti-staleness

{t5}

---

## Known limits

{limits}

## What changed since the baseline

{deltas}
"""


def _kv_table(d: dict, headers=("Metric", "Value")) -> str:
    rows = [f"| {headers[0]} | {headers[1]} |", "|---|---:|"]
    for k, v in d.items():
        if isinstance(v, (dict, list)):
            continue
        rows.append(f"| {k} | {v} |")
    return "\n".join(rows)


def build(paths: dict[str, Path], *, system: str = "Dalil", corpus: str = "corpus_v2",
          limits: str = "_None recorded — this section must not be empty at submission._"
          ) -> str:
    def read(key):
        p = paths.get(key)
        return json.loads(p.read_text(encoding="utf-8")) if p and p.exists() else {}

    ingest = read("ingest")
    retrieval = read("retrieval")
    byclass = read("by_class")
    grounding = read("grounding")
    ragas = read("ragas")
    stale = read("staleness")
    gate = read("gate")

    t1 = _kv_table({
        "documents seen": ingest.get("documents_seen"),
        "parsed": ingest.get("parsed"),
        "needs OCR": ingest.get("needs_ocr"),
        "OCR completed": ingest.get("ocr_done"),
        "quarantined": len(ingest.get("quarantined", [])),
        "unsupported": len(ingest.get("unsupported", [])),
        **{f"chunk · {k}": v for k, v in (ingest.get("chunk_stats") or {}).items()},
        **{f"OCR · {k}": v for k, v in (ingest.get("ocr_eval") or {}).items()},
    })
    t2 = _kv_table(retrieval or {"note": "not run"})
    t3 = render_by_class(byclass) if byclass.get("by_class") else "_not run_"
    t4 = _kv_table(grounding or {"note": "not run"})
    t5 = _kv_table({**(ragas.get("metrics") or {}),
                    "answered_stale (filter on)":
                        (stale.get("filtering_on") or {}).get("answered_stale"),
                    "answered_stale (filter off)":
                        (stale.get("filtering_off") or {}).get("answered_stale"),
                    "staleness verdict": stale.get("verdict")})
    deltas = _kv_table(gate.get("deltas", {})) if gate.get("deltas") else "_no baseline comparison_"

    return TEMPLATE.format(
        system=system, corpus=corpus, date=date.today().isoformat(),
        judge=ragas.get("judge", "unset"),
        judge_temp=ragas.get("judge_temperature", 0),
        config=json.dumps(ragas.get("config", {}), ensure_ascii=False),
        t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, limits=limits, deltas=deltas)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reports", type=Path, default=Path("reports"))
    ap.add_argument("--out", type=Path, default=Path("EVALUATION.md"))
    a = ap.parse_args()
    paths = {
        "ingest": a.reports.parent / "data/index/ingest_report_v2.json",
        "retrieval": a.reports / "retrieval.json",
        "by_class": a.reports / "by_class.json",
        "grounding": a.reports / "grounding.json",
        "ragas": a.reports / "ragas_report.json",
        "staleness": a.reports / "staleness.json",
        "gate": a.reports / "gate.json",
    }
    a.out.write_text(build(paths), encoding="utf-8")
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
