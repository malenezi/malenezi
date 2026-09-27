"""Pure-Python data profiling — the swamp detector, with no JVM attached.

``masar.ingest.profile_bronze`` runs the same analysis over a Delta table with
Spark. This module runs it over an in-memory batch (a CSV fixture, a test
sample, a few thousand rows in a notebook) so that:

  * the profiling logic is unit-testable in milliseconds,
  * a participant can profile a raw file BEFORE Spark is working,
  * the definition of "missing" is written down exactly once.

The definition matters more than it looks. Bronze lands CSV as STRING, so a
missing ``dropoff_geohash`` is the empty string, not ``NULL``. Count only
``NULL`` and Masar's 3.1% geohash defect reports as 0.0% — and a defect that
profiles clean is a defect that reaches the feature table as a plausible zero.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

from masar.quality.rules import timestamp_format


def is_missing(value: object) -> bool:
    """True when a value is absent for profiling purposes.

    ``None``, the empty string and whitespace-only strings all count as
    missing. Everything else — including ``0``, ``0.0`` and ``"0"`` — is a
    present value, because a zero fare is a data-quality problem, not a gap.
    """
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    return False


def null_rate(rows: Sequence[Mapping[str, Any]], column: str) -> float:
    """Fraction of rows where ``column`` is missing, in ``[0.0, 1.0]``.

    Returns ``0.0`` for an empty batch — an empty table has no null rate, and
    raising here would make the profiler the thing that breaks on a bad day.
    Volume is a separate signal (``masar.quality.observe.check_volume``); do
    not overload this one with it.
    """
    if not rows:
        return 0.0
    missing = sum(1 for row in rows if is_missing(row.get(column)))
    return missing / len(rows)


def null_rates(rows: Sequence[Mapping[str, Any]]) -> dict[str, float]:
    """Missing rate for every column seen anywhere in the batch."""
    columns: list[str] = []
    for row in rows:
        for key in row:
            if key not in columns:
                columns.append(key)
    return {c: null_rate(rows, c) for c in columns}


def distinct_counts(rows: Sequence[Mapping[str, Any]], column: str) -> dict[Any, int]:
    """Value frequencies for a low-cardinality column, most common first.

    Used on ``city``, ``status``, ``payment_type`` and ``producer_version`` —
    the columns where an unexpected value is the whole story.
    """
    counts: dict[Any, int] = {}
    for row in rows:
        value = row.get(column)
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], str(kv[0]))))


def timestamp_format_mix(rows: Sequence[Mapping[str, Any]], column: str) -> dict[str, int]:
    """Count how many rows use each timestamp format in one column.

    A column that is 98% ``iso`` and 2% ``eu`` is not "mostly fine": it is a
    column where a naive parse silently discards 2% of the business.
    """
    mix: dict[str, int] = {"iso": 0, "eu": 0, "missing": 0, "unknown": 0}
    for row in rows:
        mix[timestamp_format(row.get(column))] += 1
    return mix


@dataclass
class ProfileReport:
    """The result of profiling one batch.

    Attributes:
        rows: row count.
        columns: column names, in first-seen order.
        null_rates: missing rate per column.
        duplicate_keys: extra rows sharing the business key.
        timestamp_mix: format mix per timestamp-ish column.
        domains: value frequencies per low-cardinality column.
        smells: human-readable findings — what goes in LAB1_NOTES.md.
    """

    rows: int
    columns: list[str]
    null_rates: dict[str, float]
    duplicate_keys: int = 0
    timestamp_mix: dict[str, dict[str, int]] = field(default_factory=dict)
    domains: dict[str, dict[Any, int]] = field(default_factory=dict)
    smells: list[str] = field(default_factory=list)


# Columns whose missing rate is a red flag rather than a fact of life, and the
# rate above which we say so. `dropoff_geohash` is known-bad at 3.1%: it is
# tolerated and MONITORED, never silently accepted.
NULL_RATE_THRESHOLDS: dict[str, float] = {
    "trip_id": 0.0,
    "rider_id": 0.0,
    "driver_id": 0.0,
    "pickup_ts": 0.0,
    "dropoff_ts": 0.0,
    "fare_sar": 0.0,
    "dropoff_geohash": 0.05,
}

TIMESTAMP_COLUMNS = ("pickup_ts", "dropoff_ts", "hire_date", "settled_ts", "ts")
DOMAIN_COLUMNS = ("city", "status", "payment_type", "producer_version", "fuel_type")


def profile_rows(rows: Sequence[Mapping[str, Any]], key: str | None = None) -> ProfileReport:
    """Profile an in-memory batch and name its swamp smells.

    Args:
        rows: the batch, as mappings (``csv.DictReader`` output works directly).
        key: business key to check for duplicates, e.g. ``"trip_id"``.

    Returns:
        A :class:`ProfileReport`. ``smells`` is the part participants paste
        into their lab notes; everything else is the evidence behind it.
    """
    from masar.quality.rules import duplicate_key_count

    rates = null_rates(rows)
    report = ProfileReport(
        rows=len(rows),
        columns=list(rates),
        null_rates=rates,
        duplicate_keys=duplicate_key_count(list(rows), key) if key else 0,
    )

    for column in TIMESTAMP_COLUMNS:
        if column in rates:
            report.timestamp_mix[column] = timestamp_format_mix(rows, column)
    for column in DOMAIN_COLUMNS:
        if column in rates:
            report.domains[column] = distinct_counts(rows, column)

    report.smells = _name_the_smells(report)
    return report


def _name_the_smells(report: ProfileReport) -> list[str]:
    """Turn measurements into findings. A number nobody reads is not a finding."""
    smells: list[str] = []

    for column, rate in report.null_rates.items():
        threshold = NULL_RATE_THRESHOLDS.get(column)
        if threshold is not None and rate > threshold:
            smells.append(
                f"MISSING VALUES: {column} is {rate:.2%} missing "
                f"(tolerated up to {threshold:.0%}); downstream this becomes a "
                f"plausible-looking default nobody questions."
            )

    if report.duplicate_keys:
        smells.append(
            f"DUPLICATE KEYS: {report.duplicate_keys:,} extra rows share a business key. "
            f"Bronze may hold them; silver must not, and a MERGE against an "
            f"ambiguous source is undefined behaviour."
        )

    for column, mix in report.timestamp_mix.items():
        variants = {k: v for k, v in mix.items() if v and k != "missing"}
        if len(variants) > 1:
            smells.append(
                f"FORMAT DRIFT: {column} carries {len(variants)} timestamp formats {variants}. "
                f"A single-format parse nulls the minority silently."
            )
        if mix.get("unknown"):
            smells.append(
                f"UNPARSEABLE: {column} has {mix['unknown']:,} values in no known format."
            )

    versions = report.domains.get("producer_version", {})
    if len(versions) > 1:
        smells.append(
            f"PRODUCER DRIFT: {len(versions)} producer versions present {versions}. "
            f"A new version can change a field's MEANING while keeping its type — "
            f"schema validation will not see it."
        )

    return smells


def format_report(report: ProfileReport, title: str = "batch") -> str:
    """Render a report for a terminal. Same shape as the Spark profiler's output."""
    lines = [f"=== {title} ===", f"rows={report.rows:,}  columns={len(report.columns)}"]
    lines.append("-- missing rate per column --")
    for column, rate in report.null_rates.items():
        flag = " <-- SMELL" if rate > NULL_RATE_THRESHOLDS.get(column, 1.0) else ""
        lines.append(f"  {column:<22} {rate:6.2%}{flag}")
    if report.duplicate_keys:
        lines.append(f"duplicate business keys: {report.duplicate_keys:,}")
    for column, mix in report.timestamp_mix.items():
        lines.append(f"{column}: " + "  ".join(f"{k}={v:,}" for k, v in mix.items() if v))
    for column, counts in report.domains.items():
        lines.append(f"-- distinct {column} --")
        for value, count in list(counts.items())[:10]:
            lines.append(f"  {str(value):<22} {count:,}")
    if report.smells:
        lines.append("-- swamp smells --")
        lines.extend(f"  * {s}" for s in report.smells)
    return "\n".join(lines)
