"""Print an inclusive date range, one date per line — for shell backfill loops.

    for d in $(python -m masar.tools.daterange 2026-06-01 2026-06-05); do ... done

Small on purpose. A backfill loop written with ``seq`` and ``date -d`` is
subtly different on macOS and Linux, and the day it breaks is the day someone
is backfilling under pressure.
"""

from __future__ import annotations

import argparse
from datetime import date, timedelta


def daterange(start: str, end: str) -> list[str]:
    """Inclusive list of ``YYYY-MM-DD`` strings from ``start`` to ``end``.

    Raises:
        ValueError: if ``end`` precedes ``start`` — a silently empty backfill
            is a backfill you think you ran.
    """
    d0, d1 = date.fromisoformat(start), date.fromisoformat(end)
    if d1 < d0:
        raise ValueError(f"end {end} precedes start {start}")
    return [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Print an inclusive date range")
    p.add_argument("start")
    p.add_argument("end")
    a = p.parse_args()
    print("\n".join(daterange(a.start, a.end)))


if __name__ == "__main__":
    main()
