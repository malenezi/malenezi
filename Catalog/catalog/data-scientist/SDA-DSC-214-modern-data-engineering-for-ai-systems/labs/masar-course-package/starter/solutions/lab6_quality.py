"""Lab 6 solution — the gate's reasons, the speed-unit fix, PDPL retention.

Blocks completed here:
  * ``src/masar/quality/gate.py``                  :: reason_array
  * ``src/masar/stream/build_vehicle_positions.py``:: normalise_speed
  * ``src/masar/governance/retention.py``          :: enforce_retention
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import Column, DataFrame

MPS_PRODUCER_VERSIONS = ("2.5.0",)
MPS_TO_KMH = 3.6


# --------------------------------------------------------------------------
# TODO(lab-6) in src/masar/quality/gate.py :: gate_and_promote
# --------------------------------------------------------------------------
def reason_array(predicates: dict[str, Column]) -> Column:
    """Tag each row with EVERY quarantine rule it violates.

    A quarantine table without reasons is a landfill. "120 rows rejected"
    starts an investigation; "120 rows: fare_non_positive" ends one.

    Collect ALL reasons rather than the first match: a row can be wrong in
    more than one way, and knowing that a row is both negative-fare AND
    reversed-timestamps points at a different upstream fault than either alone.

    ``array_remove(array(...), None)`` is the Spark idiom — build one slot per
    rule, ``None`` where the rule passed, then drop the nulls.
    """
    from pyspark.sql import functions as F

    return F.array_remove(
        F.array(
            *[
                F.when(predicate, F.lit(name)).otherwise(F.lit(None))
                for name, predicate in predicates.items()
            ]
        ),
        None,
    )


# --------------------------------------------------------------------------
# TODO(lab-6) in src/masar/stream/build_vehicle_positions.py :: conform
# --------------------------------------------------------------------------
def normalise_speed(flat: DataFrame) -> DataFrame:
    """Normalise ``speed_kmh`` to km/h across producer versions.

    THE incident, in one column:

        producer 2.4.0  ->  speed_kmh in km/h    (mean ~35.4)
        producer 2.5.0  ->  speed_kmh in m/s     (mean ~9.85)

    Same key. Same type. Every value individually valid — 9.85 is a perfectly
    plausible km/h. Schema validation passes, not-null passes, uniqueness
    passes, range 0..200 passes. Nothing in the row-level contract can see it.

    What it does downstream: ``rolling_avg_speed_10m`` collapses for a third of
    the fleet, the ETA model learns that those vehicles crawl, and ETAs for
    them inflate — for weeks, with every dashboard green.

    What catches it: comparing the mean PER PRODUCER VERSION against a frozen
    baseline (``masar.quality.drift.detect_unit_drift``). Grouping is what
    turns "something changed" into "2.5.0 changed", which names a deployment,
    which has an owner and a rollback.

    Where the fix belongs: HERE, at the silver conforming boundary. Fix it in
    the feature builder and every other consumer stays wrong; fix it in the
    producer only and the historical data stays wrong forever.
    """
    from pyspark.sql import functions as F

    return flat.withColumn(
        "speed_kmh",
        F.when(
            F.col("producer_version").isin(*MPS_PRODUCER_VERSIONS),
            F.col("_speed_raw") * F.lit(MPS_TO_KMH),
        ).otherwise(F.col("_speed_raw")),
    )


# --------------------------------------------------------------------------
# TODO(lab-6) in src/masar/governance/retention.py :: enforce_gps_retention
# --------------------------------------------------------------------------
def enforce_retention(spark, path: str, predicate: str, retain_hours: int = 168) -> None:
    """Delete past the retention window, then VACUUM to make it physical.

    The two-step is the whole lesson. ``DELETE`` rewrites the current version;
    the removed rows are still on disk and still reachable by time travel. Only
    ``VACUUM`` past the retention window removes the files.

    So: after the DELETE, minimisation has been RECORDED. After the VACUUM, it
    has been DONE. Telling a regulator the first is the second is worse than
    not deleting at all, because it is a false statement about a control.

    The tension is real and worth naming in GOVERNANCE.md: the time travel that
    makes the platform auditable is the same feature that makes erasure slow.
    """
    from delta.tables import DeltaTable

    DeltaTable.forPath(spark, path).delete(predicate)
    spark.sql(f"VACUUM delta.`{path}` RETAIN {retain_hours} HOURS")


#: The trap in the erasure fixture, spelled out.
ERASURE_TRAP = """
GPS pings are keyed by trip_id and vehicle_id. They have NO rider_id.

A rider-keyed erasure across silver.trips therefore does not touch
silver.vehicle_positions, and the data subject's metre-resolution location
trace survives an erasure that reported success.

The fix: resolve the subject's trip_ids first, then delete positions by
trip_id (masar.governance.retention.erase_rider_positions). Any erasure
procedure that does not enumerate every table holding a JOINABLE identifier
is incomplete, and "we deleted the rider table" is the most common form of
that mistake.
"""

LAB6_ANSWERS = {
    "which failures fail-fast": (
        "Integrity: null or duplicate business key, missing event time, missing "
        "data subject, schema change, type change. Promoting anything from such "
        "a batch is worse than promoting nothing."
    ),
    "which failures quarantine": (
        "Value-domain failures affecting specific rows: bad fares, impossible "
        "durations, unknown cities. Blocking 48,000 good trips for 120 bad rows "
        "is a control people learn to bypass."
    ),
    "what catches semantic drift": (
        "A distribution comparison against a FROZEN baseline, grouped by the "
        "dimension most likely to explain it (producer_version, city). Never a "
        "baseline recomputed from the batch under test."
    ),
    "three PDPL controls applied": (
        "1. Classification drives access and retention. "
        "2. Purpose-bound retention on precise location (180d), enforced by "
        "DELETE + VACUUM. "
        "3. Erasure that follows the trip_id join so the GPS trace is reached."
    ),
}
