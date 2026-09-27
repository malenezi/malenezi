#!/usr/bin/env python3
"""ask.py -- one question, full trace. The demo command and the debugging tool.

    python scripts/ask.py "How much is the housing allowance for Grade 11?"
    python scripts/ask.py --tier public "..."     # see access control bite
    python scripts/ask.py --json "..."            # machine-readable trace
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.index.collection import load_chunks                        # noqa: E402
from dalil.retrieve.backends import MemoryBackend, AccessContext, build_backend  # noqa: E402
from dalil.generate.pipeline import Dalil                             # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question", nargs="+")
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--backend", choices=["memory", "qdrant", "auto"], default="memory")
    ap.add_argument("--model", default=None)
    ap.add_argument("--tier", choices=["public", "internal", "restricted"],
                    default="restricted")
    ap.add_argument("--departments", help="comma-separated, e.g. hr,finance")
    ap.add_argument("--include-superseded", action="store_true")
    ap.add_argument("--tau", type=float)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    q = " ".join(a.question)
    chunks = load_chunks(a.chunks)
    backend = (MemoryBackend(chunks, dense=True, model_name=a.model)
               if a.backend == "memory" else build_backend(chunks, kind=a.backend))
    ctx = AccessContext(max_tier=a.tier,
                        departments=set(a.departments.split(",")) if a.departments else None,
                        include_superseded=a.include_superseded)
    trace = Dalil(backend, ctx=ctx).ask(q, tau=a.tau)

    if a.json:
        print(json.dumps(trace.to_dict(), ensure_ascii=False, indent=2))
        return 0

    print(f"\nQ: {q}")
    print(f"   class={trace.query_class}  path={trace.path}  "
          f"refused={trace.refused}  stub={trace.stub}")
    print(f"\nA: {trace.answer}\n")
    print(f"cited      : {trace.cited_doc_ids or '—'}")
    print(f"retrieved  : {trace.retrieved_doc_ids[:6]}")
    if trace.invented_citations:
        print(f"!! INVENTED CITATIONS: {trace.invented_citations}")
    print(f"context    : {trace.context_stats.get('blocks')} blocks, "
          f"{trace.context_stats.get('tokens_estimated')} est. tokens, "
          f"dropped {trace.context_stats.get('dropped')}")
    print(f"latency    : {trace.latency_ms}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
