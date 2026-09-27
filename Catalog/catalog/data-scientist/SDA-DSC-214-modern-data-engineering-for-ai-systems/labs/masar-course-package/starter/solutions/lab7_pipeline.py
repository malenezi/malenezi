"""Lab 7 solution — idempotent gold writes and point-in-time windows.

Blocks completed here:
  * ``src/masar/transform/build_gold.py`` :: write_demand_replace_where
  * ``src/masar/transform/build_gold.py`` :: point_in_time_windows
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from masar.transform.feature_spec import FeatureWindow

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

LOOKBACK_DAYS = 3


# --------------------------------------------------------------------------
# TODO(lab-7) in src/masar/transform/build_gold.py :: build_zone_hourly_demand
# --------------------------------------------------------------------------
def write_demand_replace_where(
    demand: DataFrame, path: str, lookback_days: int = LOOKBACK_DAYS
) -> None:
    """Rebuild only the lookback partitions, idempotently.

    Three candidate write strategies:

      ``append``                WRONG. A retry after a transient timeout adds a
                                second row for the same (city, zone, date,
                                hour). The BI dashboard double-counts demand,
                                ``rolling_zone_demand_15m`` doubles, and surge
                                pricing fires at 2x on a normal Tuesday. The
                                data is wrong, no error is raised, and nothing
                                alerts.

      ``overwrite`` (whole)     CORRECT but O(all history) every night. Fine on
                                Day 1 of the course, unaffordable by month six.
                                This is what the starter ships.

      ``overwrite`` +           CORRECT and O(lookback). Replaces exactly the
      ``replaceWhere``          partitions recomputed and leaves the rest
                                untouched. This is the production shape.

    ``replaceWhere`` requires that the frame contains ONLY rows matching the
    predicate — otherwise Delta rejects the write. Filtering the source to the
    same window is therefore not an optimisation, it is part of the contract.
    """
    from pyspark.sql import functions as F

    windowed = demand.filter(F.col("date") >= F.date_sub(F.current_date(), lookback_days))
    (
        windowed.write.format("delta")
        .mode("overwrite")
        .partitionBy("date")  # date ONLY. Not city. Not zone.
        .option("replaceWhere", f"date >= current_date() - INTERVAL {lookback_days} DAYS")
        .option("overwriteSchema", "false")
        .save(path)
    )


# --------------------------------------------------------------------------
# TODO(lab-7) in src/masar/transform/build_gold.py :: build_trip_features
# --------------------------------------------------------------------------
def point_in_time_windows() -> dict[str, FeatureWindow]:
    """The declared, strictly-prior windows for ``gold.trip_features``.

    The ``-1`` is not cosmetic.

    ``rangeBetween`` is INCLUSIVE of both bounds. With ``orderBy(pickup_epoch)``
    and an upper bound of ``0``, the frame includes every row whose ordering
    value equals this row's — that is, every other trip that started in the
    same second. In a busy Riyadh zone at 07:14 that is several trips which,
    from the model's point of view, had not happened yet.

    It is a one-character bug that inflates a metric and survives review,
    because ``(-3600, 0)`` reads as "the last hour" to anyone who has not been
    bitten by it.

    Declaring the windows as objects rather than tuples buys the lint:
    ``assert_point_in_time()`` fails the BUILD if someone widens one later,
    which is a control that runs, unlike a comment saying "do not change this".
    """
    return {
        "zone_demand_prev_hr": FeatureWindow(
            "zone_demand_prev_hr",
            -3600,
            -1,
            "Trips in this zone in the prior hour, strictly before this trip.",
        ),
        "driver_trips_prev_24h": FeatureWindow(
            "driver_trips_prev_24h",
            -86_400,
            -1,
            "This driver's trips in the prior 24 hours, strictly before.",
        ),
    }


def build_windows(spark_window_cls, functions, bounds: dict[str, FeatureWindow]):
    """Turn declared windows into Spark window specs, asserting each first."""
    specs = {}
    for name, window in bounds.items():
        window.assert_point_in_time()  # fail the build, not the model
        partition = ["city", "pickup_zone_id"] if name.startswith("zone") else ["driver_id"]
        specs[name] = (
            spark_window_cls.partitionBy(*partition)
            .orderBy(functions.col("pickup_epoch"))
            .rangeBetween(window.start, window.end)
        )
    return specs


#: The arithmetic Lab 7 Task 3 asks participants to verify by hand.
SPOT_CHECK = """
Pick one trip and recount its feature three ways:

  feature_value            what the build wrote
  recount_strictly_prior   COUNT(*) over [feature_ts - 60min, feature_ts)
  recount_if_leaking       COUNT(*) over [feature_ts - 60min, feature_ts + 60min]

Correct output looks like:

  trip_id     feature_ts           feature_value  strictly_prior  if_leaking
  TRP-770118  2026-06-28 07:14:33  17             17              44

feature_value == recount_strictly_prior proves the window is right.
recount_if_leaking = 44 is what a careless (-3600, 3600) would have handed the
model: 2.6x the true value, and 27 of those 44 trips had not happened yet.

Do not accept the assertion as proof. Recount it yourself once — the arithmetic
is what makes the abstraction stick, and you meet it again in Lab 8.
"""

#: The recovery drill, and what each step proves.
RECOVERY_DRILL = """
  python -m masar.tools.snapshot --out /tmp/before.json
  python orchestration/run_local.py --run --inject-failure build_silver
  python -m masar.tools.snapshot --out /tmp/during.json
  diff <(jq -S . /tmp/before.json) <(jq -S . /tmp/during.json)   # EMPTY

    -> the dependency held. Gold was never built from a broken silver; it
       still holds yesterday's correct data. This is the property that makes
       a 02:30 failure a 09:00 conversation instead of a 09:00 emergency.

  python orchestration/run_local.py --run                        # full re-run
  python -m masar.tools.snapshot --out /tmp/after.json
  diff <(jq -S . /tmp/before.json) <(jq -S . /tmp/after.json)    # EMPTY

    -> a FULL re-run reproduced the exact same end state, checksums included.
       Not "the failed tasks". The whole thing. If that is safe, every
       operational problem is tractable; if it is not, every operational
       problem is an archaeology project.
"""

LAB7_ANSWERS = {
    "what stops gold using stale silver": "The declared DAG dependency edge, nothing else.",
    "why every task must be idempotent": (
        "So retries, backfills and full re-runs cannot corrupt or double-count. "
        "Idempotency is what makes 're-run everything' a safe instruction."
    ),
    "what a layer contract is": (
        "The guaranteed shape and quality a layer promises its consumers, plus "
        "the place that guarantee is enforced — a constraint, a test, or a gate."
    ),
    "what makes the feature table point-in-time correct": (
        "Every window is strictly before the event: rangeBetween(..., -1)."
    ),
}
