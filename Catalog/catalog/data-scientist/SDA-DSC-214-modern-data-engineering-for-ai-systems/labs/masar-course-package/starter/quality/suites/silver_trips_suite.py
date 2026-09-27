"""The ``silver.trips`` data contract, expressed as executable expectations.

Great Expectations 0.18. The suite lives in version control and changes go
through review like any other code — which is the whole point: a data contract
that lives in a wiki is a data contract nobody enforces.

Column set is EXACTLY ``data/raw/trips_YYYY-MM-DD.csv`` conformed to silver::

    trip_id, rider_id, driver_id, vehicle_id, city, pickup_zone_id,
    dropoff_zone_id, pickup_ts, dropoff_ts, distance_km, duration_min,
    fare_sar, surge_multiplier, payment_type, status, dropoff_geohash

Every expectation carries ``meta.response_class``, which
``masar.quality.gate`` reads to decide what to do with a failure:

    FAIL_FAST   integrity. Promoting anything is worse than promoting nothing.
    QUARANTINE  partial. Isolate the bad rows, promote the good ones, alert.

That classification is the interesting engineering decision in this file. The
expectations themselves are almost mechanical; deciding which failures may
pass with a warning and which must stop the pipeline is not.

Run::

    python quality/suites/silver_trips_suite.py
"""

from __future__ import annotations

SUITE_NAME = "silver_trips.contract"

KSA_CITIES = ["Riyadh", "Jeddah", "Dammam", "Mecca", "Medina"]
TRIP_STATUS = ["completed", "cancelled_rider", "cancelled_driver", "no_show"]
PAYMENT_TYPES = ["mada", "credit_card", "apple_pay", "cash", "wallet"]

SILVER_COLUMNS = [
    "trip_id", "rider_id", "driver_id", "vehicle_id", "city", "pickup_zone_id",
    "dropoff_zone_id", "pickup_ts", "dropoff_ts", "distance_km", "duration_min",
    "fare_sar", "surge_multiplier", "payment_type", "status", "dropoff_geohash",
]

FAIL_FAST = {"response_class": "FAIL_FAST"}
QUARANTINE = {"response_class": "QUARANTINE"}


def build_suite(context) -> object:
    """Create or replace the ``silver_trips.contract`` suite.

    Args:
        context: a Great Expectations 0.18 DataContext, from
            ``masar.quality.bootstrap.get_context()``.

    Returns:
        The saved expectation suite.
    """
    suite = context.add_or_update_expectation_suite(SUITE_NAME)
    validator = context.get_validator(
        batch_request=(
            context.get_datasource("masar_lakehouse")
            .get_asset("silver_trips")
            .build_batch_request()
        ),
        expectation_suite=suite,
    )

    # ---- Level 1: schema ---------------------------------------------- FAIL_FAST
    # A missing or renamed column breaks every consumer at once, and no amount
    # of row-level filtering repairs it.
    validator.expect_table_columns_to_match_set(
        column_set=SILVER_COLUMNS, exact_match=False, meta=FAIL_FAST
    )
    validator.expect_column_values_to_be_of_type("fare_sar", "DoubleType", meta=FAIL_FAST)
    validator.expect_column_values_to_be_of_type("pickup_ts", "TimestampType", meta=FAIL_FAST)

    # ---- Level 2: key integrity --------------------------------------- FAIL_FAST
    # An unkeyed row cannot be merged, deduplicated or erased. A duplicated key
    # makes MERGE ambiguous — which is not "slightly wrong", it is undefined.
    validator.expect_column_values_to_not_be_null("trip_id", meta=FAIL_FAST)
    validator.expect_column_values_to_be_unique("trip_id", meta=FAIL_FAST)
    validator.expect_column_values_to_not_be_null("pickup_ts", meta=FAIL_FAST)
    validator.expect_column_values_to_not_be_null("rider_id", meta=FAIL_FAST)

    # ---- Level 3: value constraints ----------------------------------- QUARANTINE
    # These are wrong ROWS in an otherwise sound batch. Blocking 48,000 good
    # trips because 120 fares are negative is a control people switch off.
    validator.expect_column_values_to_be_between(
        "fare_sar", min_value=0, strict_min=True, max_value=5000, meta=QUARANTINE
    )
    validator.expect_column_values_to_be_between(
        "duration_min", min_value=0, strict_min=True, max_value=600, meta=QUARANTINE
    )
    validator.expect_column_values_to_be_between(
        "distance_km", min_value=0, strict_min=True, max_value=400, meta=QUARANTINE
    )
    validator.expect_column_values_to_be_between(
        "surge_multiplier", min_value=1.0, max_value=5.0, meta=QUARANTINE
    )
    validator.expect_column_values_to_be_in_set("city", KSA_CITIES, meta=QUARANTINE)
    validator.expect_column_values_to_be_in_set("status", TRIP_STATUS, meta=QUARANTINE)
    validator.expect_column_values_to_be_in_set("payment_type", PAYMENT_TYPES, meta=QUARANTINE)
    validator.expect_column_pair_values_A_to_be_greater_than_B(
        "dropoff_ts", "pickup_ts", or_equal=False, meta=QUARANTINE
    )

    # Known 3.1% null rate on dropoff_geohash: TOLERATED, MONITORED, and not
    # silently accepted. `mostly=0.95` fails when the rate degrades, which is
    # the event worth knowing about.
    validator.expect_column_values_to_not_be_null(
        "dropoff_geohash", mostly=0.95, meta=QUARANTINE
    )

    # ---- Level 4: distribution ------------------------ QUARANTINE (scheduled)
    # The only expectations that can catch a batch where every row is valid.
    # Baselines are FROZEN from a known-good period (2026-05-01..2026-05-31).
    # Never recompute a baseline from the batch you are validating.
    validator.expect_column_mean_to_be_between(
        "fare_sar", min_value=28.0, max_value=52.0, meta=QUARANTINE
    )
    validator.expect_column_median_to_be_between(
        "duration_min", min_value=9.0, max_value=26.0, meta=QUARANTINE
    )

    validator.save_expectation_suite(discard_failed_expectations=False)
    print(f"[gx] saved suite {SUITE_NAME} with {len(suite.expectations)} expectations")
    return suite


def main() -> None:
    """CLI entry point."""
    from masar.quality.bootstrap import get_context

    build_suite(get_context())


if __name__ == "__main__":
    main()
