"""Offline == online. Compare EVERY key, not a spot check.

A serving layer that is not continuously proven consistent is not consistent;
it is merely untested. This is the check Lab 8's capstone extension wires into
CI, and it is the cheapest insurance in the whole platform: it turns "the model
behaves differently in production" from a research project into a failed build.

Exits non-zero on any mismatch, so ``make serve && python -m
masar.serve.consistency_check`` is a usable gate.

CLI::

    python -m masar.serve.consistency_check
"""

from __future__ import annotations

import argparse
import json

from masar.serve.materialize_online import GOLD, KEY, ONLINE_COLUMNS, latest_per_zone, redis_client

TOL = 1e-6


def check(verbose: bool = True) -> int:
    """Compare every zone's Redis payload against the offline gold row.

    Returns:
        The number of mismatches. Zero means offline and online agree on every
        zone and every column.
    """
    offline = {r["pickup_zone_id"]: r for r in latest_per_zone().collect()}
    client = redis_client()
    mismatches: list[tuple] = []

    for zone_id, off in offline.items():
        raw = client.get(KEY.format(zone_id=zone_id))
        if raw is None:
            mismatches.append((zone_id, "MISSING_ONLINE", None, None))
            continue
        on = json.loads(raw)
        for column in ONLINE_COLUMNS:
            ov, nv = off[column], on.get(column)
            if isinstance(ov, str) or ov is None or nv is None:
                same = ov == nv
            else:
                same = abs(float(ov) - float(nv)) <= TOL
            if not same:
                mismatches.append((zone_id, column, ov, nv))

    print(f"[consistency] source        : {GOLD}")
    print(f"[consistency] zones checked : {len(offline)}")
    print(f"[consistency] columns/zone  : {len(ONLINE_COLUMNS)}")
    print(f"[consistency] mismatches    : {len(mismatches)}")
    if verbose:
        for zone, column, ov, nv in mismatches[:10]:
            print(f"[consistency]   MISMATCH zone={zone} col={column} offline={ov} online={nv}")
    if not mismatches:
        print("[consistency] PASS — offline == online for every zone and every column")
    return len(mismatches)


def main() -> None:
    """CLI entry point. Exits 1 when offline and online disagree."""
    p = argparse.ArgumentParser(description="Prove offline == online for every zone")
    p.add_argument("--quiet", action="store_true")
    a = p.parse_args()
    raise SystemExit(1 if check(verbose=not a.quiet) else 0)


if __name__ == "__main__":
    main()
