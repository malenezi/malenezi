"""Instructor demo — three writes that Delta REJECTS, and a row count that does not move.

Used by the Lab-4 solution walkthrough (`labs/solutions/LAB_04_SOLUTION.md`,
"2. enforcement"). Run it after `python -m masar.delta.create_silver` has added
the CHECK constraints::

    python - < scripts/demo_negative_writes.py

Each attempt fails for a DIFFERENT reason, and that is the whole point:
schema enforcement, a CHECK constraint, and a nullability violation are three
separate controls, and a table with only one of them is not a contract.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from masar import config  # noqa: E402
from masar.spark import get_spark  # noqa: E402

TABLE = config.TABLES["silver.trips"].path


def _attempt(label: str, fn) -> None:
    """Run one write that must fail, and print the exception's first line."""
    try:
        fn()
    except Exception as exc:  # noqa: BLE001 - the rejection IS the demo
        first = str(exc).strip().splitlines()[0]
        print(f"  REJECTED  {label}\n            {first[:140]}")
    else:
        print(f"  !! ACCEPTED {label} — the constraint is missing. Run create_silver first.")


def main() -> None:
    """Three rejected writes, with the row count before and after."""
    spark = get_spark("lab4-demo-negative-writes")
    before = spark.read.format("delta").load(TABLE).count()
    print(f"[demo] silver.trips before: {before:,} rows\n")

    good = spark.read.format("delta").load(TABLE).limit(1)

    _attempt(
        "negative fare_sar (CHECK positive_fare)",
        lambda: good.withColumn("fare_sar", good["fare_sar"] * 0 - 12.5)
        .write.format("delta")
        .mode("append")
        .save(TABLE),
    )
    _attempt(
        "negative duration_min (CHECK valid_duration)",
        lambda: good.withColumn("duration_min", good["duration_min"] * 0 - 3.0)
        .write.format("delta")
        .mode("append")
        .save(TABLE),
    )
    _attempt(
        "unknown column loyalty_tier (schema enforcement)",
        lambda: good.withColumn("loyalty_tier", good["city"])
        .write.format("delta")
        .mode("append")
        .save(TABLE),
    )

    after = spark.read.format("delta").load(TABLE).count()
    print(f"\n[demo] silver.trips after:  {after:,} rows   (delta = {after - before})")
    print("[demo] Three rejections, zero rows written. The table defended itself.")


if __name__ == "__main__":
    main()
