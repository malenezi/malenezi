"""Count rows (and optionally distinct keys) in a lakehouse table.

Used constantly in the labs, because almost every property in this course is
proved by counting: append-only landing, exactly-once streaming, idempotent
gold, grain assertions.

CLI::

    python -m masar.tools.count --table bronze.gps_events
    python -m masar.tools.count --table bronze.gps_events --distinct event_id
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark


def count(table: str, distinct: str | None = None) -> dict[str, int]:
    """Count rows in ``table``; optionally count distinct values of a column.

    Returns:
        ``{"rows": n}`` plus ``{"distinct_<col>": m}`` when requested.
    """
    from delta.tables import DeltaTable

    spark = get_spark("tools-count")
    path = config.table_path(table)
    if not DeltaTable.isDeltaTable(spark, path):
        print(f"table={table}  (does not exist at {path})")
        return {"rows": 0}

    df = spark.read.format("delta").load(path)
    out = {"rows": df.count()}
    line = f"table={table}  rows={out['rows']:,}"
    if distinct:
        out[f"distinct_{distinct}"] = df.select(distinct).distinct().count()
        line += f"  distinct_{distinct}={out[f'distinct_{distinct}']:,}"
        if out[f"distinct_{distinct}"] != out["rows"]:
            line += f"  (delta {out['rows'] - out[f'distinct_{distinct}']:,})"
    print(line)
    return out


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Count rows in a Masar table")
    p.add_argument("--table", required=True, help="canonical name, e.g. silver.trips")
    p.add_argument("--distinct", default=None, help="also count distinct values of this column")
    a = p.parse_args()
    count(a.table, a.distinct)


if __name__ == "__main__":
    main()
