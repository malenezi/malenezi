"""The contract for ``bronze.gps_events`` / ``silver.vehicle_positions``.

Read the LAST expectation first, because it is the reason this file is
interesting.

Producer ``2.4.0`` emits ``speed_kmh`` in km/h. Producer ``2.5.0`` emits the
SAME KEY, the SAME TYPE, and metres per second. Walk the suite from the top
and watch every other expectation pass:

    not-null            passes — the values are all there
    unique              passes — the ids are fine
    type check          passes — still a double
    range 0..200        passes — 9.85 m/s is a perfectly valid "km/h"

Only ``expect_column_mean_to_be_between`` sees it. That is the lesson: schema
validation checks that a field is SHAPED right; nothing but a distribution
check tests whether it MEANS what it used to.

Run::

    python quality/suites/gps_events_suite.py
"""

from __future__ import annotations

SUITE_NAME = "gps_events.contract"

# Saudi Arabia's bounding box. A fix outside it is a bug, not a journey.
KSA_LAT = (16.0, 33.0)
KSA_LON = (34.0, 56.0)

#: Frozen from 2026-05-01..2026-05-31, when every producer was 2.4.0.
#: A batch in m/s has a mean near 9.9 and falls straight out of this band.
SPEED_MEAN_MIN = 24.0
SPEED_MEAN_MAX = 46.0

FAIL_FAST = {"response_class": "FAIL_FAST"}
QUARANTINE = {"response_class": "QUARANTINE"}


def build_suite(context, asset: str = "silver_vehicle_positions") -> object:
    """Create or replace the ``gps_events.contract`` suite.

    Args:
        context: a Great Expectations 0.18 DataContext.
        asset: the registered asset to attach the suite to.

    Returns:
        The saved expectation suite.
    """
    suite = context.add_or_update_expectation_suite(SUITE_NAME)
    validator = context.get_validator(
        batch_request=(
            context.get_datasource("masar_lakehouse").get_asset(asset).build_batch_request()
        ),
        expectation_suite=suite,
    )

    # ---- integrity ------------------------------------------------ FAIL_FAST
    validator.expect_column_values_to_not_be_null("event_id", meta=FAIL_FAST)
    validator.expect_column_values_to_be_unique("event_id", meta=FAIL_FAST)
    validator.expect_column_values_to_not_be_null("event_ts", meta=FAIL_FAST)

    # ---- geography and fix quality --------------------------------- QUARANTINE
    validator.expect_column_values_to_be_between("lat", *KSA_LAT, meta=QUARANTINE)
    validator.expect_column_values_to_be_between("lon", *KSA_LON, meta=QUARANTINE)
    validator.expect_column_values_to_be_between("accuracy_m", 0, 50, meta=QUARANTINE)
    validator.expect_column_values_to_be_between("heading_deg", 0, 360, meta=QUARANTINE)

    # A version we have never seen is a deployment nobody told us about.
    validator.expect_column_values_to_be_in_set(
        "producer_version", ["2.4.0", "2.5.0"], meta=QUARANTINE
    )

    # A hard range rule passes on m/s values, so it proves nothing here.
    # Kept anyway: it catches the OTHER failure, a sensor reporting 4,000 km/h.
    validator.expect_column_values_to_be_between("speed_kmh", 0, 200, meta=QUARANTINE)

    # THE expectation. This mean check is the only rule in the suite that can
    # catch producer 2.5.0's unit change, because it is the only one that
    # compares the batch to what the batch USED to look like.
    validator.expect_column_mean_to_be_between(
        "speed_kmh", min_value=SPEED_MEAN_MIN, max_value=SPEED_MEAN_MAX, meta=QUARANTINE
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
