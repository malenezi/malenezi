#!/usr/bin/env python3
"""build_index.py -- Lab 3: create the Qdrant collection and upsert chunks.

Idempotency is the checked property: running this twice must not change the
point count. If it does, the chunk ids are not stable (the classic bug is using
`enumerate()` as the id) and every re-index silently doubles the corpus.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dalil.config import settings                                     # noqa: E402
from dalil.index.collection import (load_chunks, build_collection, upsert_chunks,
                                    collection_stats, get_client)     # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chunks", type=Path, default=ROOT / "data/index/chunks.jsonl")
    ap.add_argument("--collection", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--recreate", action="store_true")
    ap.add_argument("--no-sparse", action="store_true")
    a = ap.parse_args()

    chunks = load_chunks(a.chunks)
    name = a.collection or settings.collection
    client = get_client()
    build_collection(name, recreate=a.recreate, sparse=not a.no_sparse, client=client)
    before = collection_stats(name, client)["points"] or 0
    n = upsert_chunks(chunks, name=name, model_name=a.model,
                      with_sparse=not a.no_sparse, client=client)
    after = collection_stats(name, client)["points"]
    print(f"collection {name}: {n} chunks upserted, points {before} -> {after}")
    if before and after != before and before == len(chunks):
        print("[WARN] point count changed on a re-run — your chunk ids are not stable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
