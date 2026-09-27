"""Lab 3 solution — the incremental, idempotent ELT to ``silver.trips``.

Blocks completed here:
  * ``src/masar/transform/build_silver.py`` :: latest-version deduplication
  * ``dbt/masar/models/marts/silver/silver_trips.sql`` :: the lookback window

The dbt model in the starter already ships correct — Lab 3 is where
participants WRITE it, and this file is the reference they are checked
against. The Spark path's TODO is the one that is naive on purpose.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame


# --------------------------------------------------------------------------
# TODO(lab-3) in src/masar/transform/build_silver.py :: build_silver_trips
# --------------------------------------------------------------------------
def dedupe_latest_per_key(
    df: DataFrame, key: str = "trip_id", order_by: tuple[str, str] = ("_ingested_at", "_batch_id")
) -> DataFrame:
    """Keep the LATEST landed row per business key.

    Why the starter's ``dropDuplicates([key])`` is wrong, and wrong in the
    worst possible way:

    ``dropDuplicates`` keeps an ARBITRARY row from each group. Most of the
    time the group has one row and nothing happens. It only matters when a
    trip was re-landed — which is exactly when a CORRECTION arrived. So the
    bug fires only on corrected trips, keeps the stale value roughly half the
    time, and is invisible in every aggregate. Run Lab 1 Task 3's deliberate
    double-landing, then diff the fares, and it appears.

    Ordering by ``_ingested_at`` then ``_batch_id`` makes it deterministic
    even when two batches land inside the same second.
    """
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    latest = Window.partitionBy(key).orderBy(*[F.col(c).desc() for c in order_by])
    return df.withColumn("_rn", F.row_number().over(latest)).filter("_rn = 1").drop("_rn")


# --------------------------------------------------------------------------
# The dbt model, for reference. Lives at
# dbt/masar/models/marts/silver/silver_trips.sql
# --------------------------------------------------------------------------
SILVER_TRIPS_INCREMENTAL_BLOCK = """
{% if is_incremental() %}
  -- LOOKBACK on pickup_ts (EVENT time), not on _ingested_at (processing time).
  --
  -- The distinction decides whether late data is corrected or lost. A trip
  -- that ENDED on Monday but ARRIVED on Wednesday has a Monday pickup_ts and
  -- a Wednesday _ingested_at. Filter on _ingested_at and it is included
  -- today, but a re-run tomorrow will not reconsider it. Filter on pickup_ts
  -- and it stays inside the window for the full lookback, so every re-run
  -- re-merges it — which is what makes the pipeline self-healing.
  where pickup_ts >= (
      select date_sub(max(pickup_ts), {{ var('lookback_days', 3) }})
      from {{ this }}
  )
{% endif %}
"""

#: Why merge + unique_key is the whole idempotency story.
IDEMPOTENCY_NOTE = """
incremental_strategy='merge' with unique_key='trip_id' means:

  * a trip seen for the first time    -> INSERT
  * a trip seen again, unchanged      -> UPDATE to the same values (no-op)
  * a trip seen again, corrected      -> UPDATE to the corrected values

Running the model twice therefore produces identical output. That single
property is what lets the answer to any incident be "re-run the whole thing"
instead of "work out which parts are safe to re-run", and the second answer
is the one that takes a week and gets it wrong.
"""

#: The four questions Lab 3's notes must answer.
LAB3_ANSWERS = {
    "why staging is a view": (
        "Staging is rename-and-cast with no expensive logic. Materialising it "
        "would cost storage and buy nothing — the work is pushed down into the "
        "silver model's scan either way."
    ),
    "why lookback on event time": (
        "A trip that ended yesterday but arrived today must fall inside the "
        "window. Processing-time filters include it once and never reconsider it."
    ),
    "why dedupe before the join": (
        "Joining first multiplies the duplicates by the driver rows, and the "
        "row_number window then has more data to sort for no benefit."
    ),
    "what silver guarantees": (
        "One row per trip_id; completed trips only; timestamps UTC; city names "
        "conformed; fare, distance and duration strictly positive. Anything "
        "excluded still exists in bronze — nothing is destroyed, only excluded "
        "from the contract."
    ),
}
