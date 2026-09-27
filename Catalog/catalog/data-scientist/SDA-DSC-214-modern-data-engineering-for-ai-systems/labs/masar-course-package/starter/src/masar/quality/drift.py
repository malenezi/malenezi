"""Semantic-drift detection — the signal that catches the incident nobody sees.

Masar's signature incident: GPS producer ``2.4.0`` emits ``speed_kmh`` in km/h.
Producer ``2.5.0`` emits the SAME KEY, the SAME TYPE — and metres per second.

Walk through what does NOT catch it:

  * schema validation      passes: the column exists and is still a double
  * not-null / uniqueness  passes: every value is present and well-formed
  * range check 0..200     passes: 9.85 m/s is a perfectly valid "km/h"
  * row-count / freshness  passes: the feed is on time and complete

Every row is individually valid. The BATCH is wrong. The only thing that sees
it is a comparison of the value DISTRIBUTION against a frozen baseline — and,
better, a per-``producer_version`` comparison, which points straight at the
cause instead of just raising an eyebrow.

One rule matters more than the code below: **the baseline is frozen.** Compute
it from a known-good period and store it. Recompute it from the batch you are
validating and you will "baseline the bug": the check passes forever, one day
later than it should have.

Pure Python. The Spark equivalents live in ``masar.quality.observe``.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

#: Frozen baselines from 2026-05-01..2026-05-31, a period with no known
#: incident. Regenerating these is a reviewed change, not a convenience.
BASELINES: dict[str, float] = {
    "silver.trips.fare_sar": 37.4,
    "silver.trips.duration_min": 17.6,
    "silver.vehicle_positions.speed_kmh": 35.45,
}

#: m/s -> km/h. If a mean is off by roughly this factor, you have found it.
MPS_TO_KMH = 3.6


@dataclass(frozen=True)
class DriftVerdict:
    """The outcome of one distribution comparison.

    Attributes:
        metric: what was measured, e.g. ``silver.vehicle_positions.speed_kmh``.
        observed: the measured statistic.
        baseline: the frozen reference value.
        deviation: signed relative deviation, ``(observed - baseline)/baseline``.
        tolerance: the band that counts as normal variation.
        group: the subgroup this verdict is about (a producer version, a city),
            or ``None`` for the whole batch.
        hint: a diagnosis when the shape of the deviation is recognisable.
    """

    metric: str
    observed: float
    baseline: float
    deviation: float
    tolerance: float
    group: str | None = None
    hint: str = ""

    @property
    def drifted(self) -> bool:
        """True when the deviation is outside tolerance."""
        return abs(self.deviation) > self.tolerance

    def render(self) -> str:
        """One line for a terminal or an alert."""
        flag = "DRIFT" if self.drifted else "ok   "
        where = f" [{self.group}]" if self.group else ""
        tail = f"  <- {self.hint}" if self.hint and self.drifted else ""
        return (
            f"[{flag}] {self.metric}{where}: {self.observed:.2f} vs "
            f"baseline {self.baseline:.2f} ({self.deviation:+.1%}){tail}"
        )


def mean(values: Iterable[float]) -> float:
    """Arithmetic mean; ``0.0`` for an empty iterable (no data is not drift)."""
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else 0.0


def compare_to_baseline(
    metric: str,
    observed: float,
    baseline: float | None = None,
    tolerance: float = 0.20,
    group: str | None = None,
) -> DriftVerdict:
    """Compare an observed statistic against a frozen baseline.

    Args:
        metric: ``table.column``; used to look the baseline up when omitted.
        observed: the statistic measured on the batch under test.
        baseline: overrides :data:`BASELINES`.
        tolerance: relative band treated as normal variation.
        group: subgroup label, when comparing per producer version or city.

    Returns:
        A :class:`DriftVerdict`, carrying a diagnostic ``hint`` when the
        deviation matches a known failure shape (a unit change, a currency
        scale-up).
    """
    baseline = BASELINES[metric] if baseline is None else baseline
    deviation = (observed - baseline) / baseline if baseline else 0.0
    return DriftVerdict(
        metric=metric,
        observed=observed,
        baseline=baseline,
        deviation=deviation,
        tolerance=tolerance,
        group=group,
        hint=diagnose(observed, baseline),
    )


def diagnose(observed: float, baseline: float, rel_tol: float = 0.15) -> str:
    """Name the failure shape when a ratio is recognisable.

    A mean that fell by exactly 3.6x is not "drift"; it is a unit change, and
    saying so turns a two-day investigation into a two-minute fix.
    """
    if not baseline or not observed:
        return ""
    ratio = observed / baseline
    candidates = (
        (1 / MPS_TO_KMH, "values look like m/s where km/h is expected (divide by 3.6)"),
        (MPS_TO_KMH, "values look like km/h where m/s is expected (multiply by 3.6)"),
        (100.0, "values look like halalas where SAR is expected (x100 currency shift)"),
        (0.01, "values look like SAR where halalas are expected (/100 currency shift)"),
        (1000.0, "values look like metres where kilometres are expected"),
    )
    for factor, message in candidates:
        if abs(ratio - factor) / factor <= rel_tol:
            return message
    return ""


def detect_unit_drift(
    rows: Sequence[Mapping[str, Any]],
    value_column: str = "speed_kmh",
    group_column: str = "producer_version",
    baseline: float | None = None,
    tolerance: float = 0.20,
) -> list[DriftVerdict]:
    """Compare a value's mean across producer versions against the baseline.

    This is the check that finds the ``2.5.0`` incident. Grouping by producer
    version is what makes the alert actionable: an aggregate drift says
    "something changed", a per-version drift says "2.5.0 changed, 2.4.0 did
    not", which is a deployment, which has an owner and a rollback.

    Args:
        rows: the batch, e.g. rows read from ``silver.vehicle_positions``.
        value_column: the numeric column to compare.
        group_column: the column to group by.
        baseline: frozen reference mean; defaults to the registered baseline
            for ``silver.vehicle_positions.<value_column>``.
        tolerance: relative band treated as normal.

    Returns:
        One :class:`DriftVerdict` per group, ordered by group name.
    """
    if baseline is None:
        baseline = BASELINES.get(f"silver.vehicle_positions.{value_column}", 1.0)

    grouped: dict[str, list[float]] = {}
    for row in rows:
        group = str(row.get(group_column, "unknown"))
        value = row.get(value_column)
        if value is None:
            continue
        try:
            grouped.setdefault(group, []).append(float(value))
        except (TypeError, ValueError):
            continue

    return [
        compare_to_baseline(
            f"silver.vehicle_positions.{value_column}",
            mean(values),
            baseline=baseline,
            tolerance=tolerance,
            group=group,
        )
        for group, values in sorted(grouped.items())
    ]


def drifted(verdicts: Sequence[DriftVerdict]) -> list[DriftVerdict]:
    """Filter to the verdicts that actually fired. Convenience for alerting."""
    return [v for v in verdicts if v.drifted]
