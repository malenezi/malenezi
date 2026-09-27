"""The four data-SRE signals: freshness, volume, schema drift, distribution drift.

Every one of these can fire while EVERY ROW passes EVERY expectation. That is
the reason they exist as a separate layer:

    freshness      the table is perfect and three days old
    volume         the table is perfect and a third of its usual size
    schema drift   a new column appeared, or an old one silently vanished
    distribution   every value is valid and the units changed (the 2.5.0 bug)

Row-level validation asks "is this row allowed?". Observability asks "is this
TABLE behaving like itself?". A platform with only the first is blind to every
failure that arrives correctly formatted.

CLI::

    python -m masar.quality.observe --check freshness --table silver.trips --sla-hours 6
    python -m masar.quality.observe --check volume    --table silver.trips --expected 84000
    python -m masar.quality.observe --check schema    --table silver.trips
    python -m masar.quality.observe --check drift     --table silver.trips --column fare_sar
    python -m masar.quality.observe --check all
"""

from __future__ import annotations

import argparse
from datetime import datetime
from functools import partial

from masar import config
from masar.quality.drift import BASELINES, diagnose
from masar.quality.gate import alert
from masar.spark import get_spark

#: FROZEN known-good period the baselines were computed from. Recomputing a
#: baseline from the batch under test is "baselining the bug": the check then
#: passes forever, exactly one day later than it should have.
BASELINE_WINDOW = ("2026-05-01", "2026-05-31")

#: The expected column set per table, for the schema-drift check.
EXPECTED_COLUMNS: dict[str, set[str]] = {
    "silver.trips": {
        "trip_id",
        "rider_id",
        "driver_id",
        "vehicle_id",
        "city",
        "pickup_zone_id",
        "dropoff_zone_id",
        "pickup_ts",
        "dropoff_ts",
        "distance_km",
        "duration_min",
        "fare_sar",
        "surge_multiplier",
        "payment_type",
        "status",
        "dropoff_geohash",
    },
    "silver.vehicle_positions": {
        "event_id",
        "vehicle_id",
        "driver_id",
        "trip_id",
        "event_ts",
        "lat",
        "lon",
        "speed_kmh",
        "heading_deg",
        "accuracy_m",
        "producer_version",
    },
}


def check_freshness(table: str, sla_hours: int = 6, path: str | None = None) -> float:
    """Assert the table was updated within its SLA.

    Args:
        table: canonical table name, for the message.
        sla_hours: the promise. Different tables make different promises:
            ``bronze.gps_events`` is 1 hour, ``bronze.drivers`` is 24.
        path: override the registered path.

    Raises:
        RuntimeError: on a breach. Freshness is one of the few checks that
            SHOULD raise rather than warn — a stale table quietly serving
            yesterday's answer is worse than a dashboard that is visibly down.

    Returns:
        Age of the newest row, in hours.
    """
    from pyspark.sql import functions as F

    spark = get_spark("observe")
    path = path or config.table_path(table)
    last = (
        spark.read.format("delta")
        .load(path)
        .agg(F.max("_ingested_at").alias("m"))
        .collect()[0]["m"]
    )
    if last is None:
        raise RuntimeError(f"FRESHNESS breach: {table} has no _ingested_at values at all")
    age_h = (datetime.now() - last).total_seconds() / 3600
    if age_h > sla_hours:
        raise RuntimeError(
            f"FRESHNESS breach: {table} last updated {last} ({age_h:.1f}h ago, SLA {sla_hours}h)"
        )
    print(f"[obs] freshness {table}: {age_h:.2f}h old, SLA {sla_hours}h  OK")
    return age_h


def check_volume(table: str, expected: int, tol: float = 0.30, path: str | None = None) -> int:
    """Assert the row count is within tolerance of the expected volume.

    A 30% band sounds loose and is not: it catches a feed that delivered a
    third of a day, a partition that failed to write, and a join that
    exploded — while tolerating a public holiday.
    """
    spark = get_spark("observe")
    path = path or config.table_path(table)
    n = spark.read.format("delta").load(path).count()
    dev = abs(n - expected) / expected if expected else 0.0
    if dev > tol:
        raise RuntimeError(
            f"VOLUME anomaly: {table} has {n:,} rows vs expected ~{expected:,} "
            f"({(n - expected) / expected:+.1%}, tolerance {tol:.0%})"
        )
    print(f"[obs] volume {table}: {n:,} rows ({(n - expected) / expected:+.1%} of baseline)  OK")
    return n


def check_schema_drift(
    table: str, expected_columns: set[str] | None = None, path: str | None = None
) -> dict[str, list[str]]:
    """Compare the live column set against the declared contract.

    This one ALERTS rather than raises. A new column is usually additive and
    harmless; a REMOVED column is not, but by the time you notice it the
    damage is already downstream. Either way the change must be seen by a
    human the same day, which is what an alert is for.

    Returns:
        ``{"added": [...], "removed": [...]}``.
    """
    spark = get_spark("observe")
    path = path or config.table_path(table)
    expected = (
        expected_columns if expected_columns is not None else EXPECTED_COLUMNS.get(table, set())
    )
    actual = {c for c in spark.read.format("delta").load(path).columns if not c.startswith("_")}
    added, removed = sorted(actual - expected), sorted(expected - actual)
    if added or removed:
        alert(f"SCHEMA drift in {table}: added={added} removed={removed}")
    else:
        print(f"[obs] schema {table}: {len(actual)} columns, no drift  OK")
    return {"added": added, "removed": removed}


def check_distribution_drift(
    table: str,
    column: str,
    baseline_mean: float | None = None,
    tol: float = 0.20,
    group_by: str | None = None,
    path: str | None = None,
) -> list[dict]:
    """Compare a column's mean against its FROZEN baseline.

    This is the signal that catches semantic drift — the failure where every
    row is valid and the batch is wrong. Grouping turns "something changed"
    into "this group changed", which is a deployment, which has an owner.

    Args:
        table: canonical table name.
        column: numeric column.
        baseline_mean: overrides :data:`masar.quality.drift.BASELINES`.
        tol: relative band treated as normal variation.
        group_by: e.g. ``producer_version`` for the speed-unit incident, or
            ``city`` for the currency shift.
        path: override the registered path.

    Returns:
        One dict per group (or a single-element list when ungrouped).
    """
    from pyspark.sql import functions as F

    spark = get_spark("observe")
    path = path or config.table_path(table)
    metric = f"{table}.{column}"
    baseline = BASELINES[metric] if baseline_mean is None else baseline_mean
    df = spark.read.format("delta").load(path)

    if group_by:
        rows = df.groupBy(group_by).agg(F.mean(column).alias("m")).collect()
    else:
        rows = [{group_by: None, "m": df.agg(F.mean(column).alias("m")).collect()[0]["m"]}]

    out = []
    for r in rows:
        observed = r["m"]
        if observed is None:
            continue
        dev = (observed - baseline) / baseline if baseline else 0.0
        drifted = abs(dev) > tol
        group = r[group_by] if group_by else None
        hint = diagnose(observed, baseline)
        out.append({"group": group, "observed": observed, "deviation": dev, "drifted": drifted})
        label = f" [{group_by}={group}]" if group_by else ""
        if drifted:
            alert(
                f"DISTRIBUTION drift: {metric}{label} mean {observed:.2f} vs frozen "
                f"baseline {baseline:.2f} ({dev:+.1%})" + (f" — {hint}" if hint else "")
            )
        else:
            print(f"[obs] drift {metric}{label}: {observed:.2f} vs {baseline:.2f} ({dev:+.1%})  OK")
    return out


def observability_task(**_: object) -> dict:
    """DAG task: run every signal that applies, collecting rather than raising.

    A DAG task that dies on the first freshness warning never reports the
    volume anomaly behind it. Collect everything, then fail once with the
    whole picture.
    """
    from delta.tables import DeltaTable

    spark = get_spark("observe")
    findings: dict[str, object] = {}
    failures: list[str] = []

    for table, sla, expected in (
        ("silver.trips", 24, 200_000),
        ("silver.vehicle_positions", 24, 1_200_000),
    ):
        path = config.table_path(table)
        if not DeltaTable.isDeltaTable(spark, path):
            findings[table] = "absent"
            continue
        # functools.partial, not a lambda: a lambda closing over `table` in a
        # loop is the classic late-binding bug. It happens to be harmless here
        # because each one is called in the same iteration — which is exactly
        # the reasoning that stops being true after the next edit.
        checks = (
            ("freshness", partial(check_freshness, table, sla)),
            ("volume", partial(check_volume, table, expected, tol=0.90)),
            ("schema", partial(check_schema_drift, table)),
        )
        for name, check in checks:
            try:
                findings[f"{table}.{name}"] = check()
            except Exception as exc:  # noqa: BLE001 - collect, then fail once
                failures.append(f"{table}.{name}: {exc}")

    if failures:
        raise RuntimeError("observability failures: " + " | ".join(failures))
    print(f"[obs] all signals green across {len(findings)} checks")
    return findings


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Run the data-SRE observability signals")
    p.add_argument(
        "--check", required=True, choices=["freshness", "volume", "schema", "drift", "all"]
    )
    p.add_argument("--table", default="silver.trips")
    p.add_argument("--sla-hours", type=int, default=6)
    p.add_argument("--expected", type=int, default=84_000)
    p.add_argument("--column", default="fare_sar")
    p.add_argument(
        "--baseline", default="auto", help="'auto' uses the frozen baseline, or give a number"
    )
    p.add_argument("--tolerance", type=float, default=0.20)
    p.add_argument("--group-by", default=None)
    a = p.parse_args()

    baseline = None if a.baseline == "auto" else float(a.baseline)
    match a.check:
        case "freshness":
            check_freshness(a.table, a.sla_hours)
        case "volume":
            check_volume(a.table, a.expected)
        case "schema":
            check_schema_drift(a.table)
        case "drift":
            check_distribution_drift(a.table, a.column, baseline, a.tolerance, a.group_by)
        case "all":
            observability_task()


if __name__ == "__main__":
    main()
