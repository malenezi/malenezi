"""PDPL classification and the serving boundary.

Saudi Arabia's Personal Data Protection Law is treated as an engineering
constraint here, not a policy appendix. These tests assert the two rules
people most often get wrong:

  1. a HASH is not anonymisation — pseudonymised data is still personal data;
  2. precise location is its own, stricter class than "personal".
"""

from __future__ import annotations

import pytest

from masar.governance.classification import (
    ACCESS_POLICY,
    CLASSIFICATION,
    PERSONAL,
    PERSONAL_PSEUDONYMISED,
    PUBLIC,
    RESTRICTED_AT_SERVING,
    RETENTION_DAYS,
    SENSITIVE_LOCATION,
    check_serving_boundary,
    classify,
    classify_columns,
    minimise,
    readable_by,
    retention_days,
)

SILVER_TRIPS_COLUMNS = [
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
]


@pytest.mark.parametrize(
    ("column", "expected"),
    [
        ("rider_id", PERSONAL),
        ("driver_id", PERSONAL),
        ("national_id_hash", PERSONAL_PSEUDONYMISED),
        ("phone_hash", PERSONAL_PSEUDONYMISED),
        ("lat", SENSITIVE_LOCATION),
        ("lon", SENSITIVE_LOCATION),
        ("city", PUBLIC),
        ("zone_name_ar", PUBLIC),
    ],
)
def test_column_classification(column, expected):
    """The classification is the root of access, retention and serving policy."""
    assert classify(column) == expected


def test_a_hash_is_not_anonymisation():
    """``national_id_hash`` is pseudonymised personal data, not anonymous data.

    It still belongs to a person, it is still in scope for an erasure request,
    and it still must not reach a dashboard. Treating a hash as anonymous is
    the single most common PDPL mistake in a data platform.
    """
    assert classify("national_id_hash") == PERSONAL_PSEUDONYMISED
    assert PERSONAL_PSEUDONYMISED in RESTRICTED_AT_SERVING
    assert retention_days("national_id_hash") is not None


def test_precise_location_is_stricter_than_personal():
    """lat/lon get their own class and the shortest retention window.

    Metre-resolution coordinates reveal homes, workplaces and routines. A zone
    CENTROID does not, which is why it is classified public — the resolution
    is the control.
    """
    assert retention_days("lat") == 180
    assert retention_days("lat") < retention_days("rider_id")
    assert classify("centroid_lat") == PUBLIC


def test_unknown_columns_fail_closed():
    """An unclassified column is an unreviewed column; the safe default is strict."""
    assert classify("some_new_column_nobody_reviewed") == PERSONAL
    assert classify("some_new_column_nobody_reviewed") in RESTRICTED_AT_SERVING


def test_every_class_has_a_retention_window_and_an_access_rule():
    """No class may be defined without saying who reads it and for how long."""
    for cls in set(CLASSIFICATION.values()):
        assert cls in RETENTION_DAYS, f"{cls} has no retention decision"
        assert cls in ACCESS_POLICY, f"{cls} has no access policy"


def test_commercial_retention_is_longer_and_that_is_not_a_pdpl_decision():
    """Financial records are kept 7 years because TAX law says so.

    Two different obligations with two different sources. Conflating them is
    how a team justifies keeping personal data 'because we keep everything
    seven years'.
    """
    assert retention_days("fare_sar") == 2555
    assert retention_days("trip_id") is None  # operational: no PDPL limit


def test_analyst_cannot_read_personal_data():
    """Analyst = gold only. Data scientist = silver. Precise GPS = DPO only."""
    assert readable_by("city", "analyst")
    assert readable_by("fare_sar", "analyst")
    assert not readable_by("rider_id", "analyst")
    assert not readable_by("national_id_hash", "analyst")
    assert not readable_by("lat", "data_scientist")
    assert readable_by("lat", "dpo")


def test_silver_trips_is_classified_end_to_end():
    """Every column of the silver contract has a decision recorded against it."""
    classified = classify_columns(SILVER_TRIPS_COLUMNS)
    assert len(classified) == len(SILVER_TRIPS_COLUMNS)
    assert classified["rider_id"] == PERSONAL
    assert classified["dropoff_geohash"] == "personal-coarse"


# --------------------------------------------------------------------------
# The serving boundary
# --------------------------------------------------------------------------


def test_raw_rider_id_in_a_bi_product_is_a_violation():
    """The check that must fail — and fail loudly — before a dashboard ships."""
    verdict = check_serving_boundary("gold.fact_trip", ["trip_id", "rider_id", "fare_sar"])
    assert not verdict.ok
    assert verdict.violations == ("rider_id",)
    assert "VIOLATION" in verdict.render()


def test_pseudonym_is_allowed_but_recorded():
    """A pseudonym may cross the boundary; it is still noted in the report.

    It remains in scope for an erasure request, so 'allowed' must not mean
    'forgotten'.
    """
    verdict = check_serving_boundary(
        "gold.fact_trip",
        ["trip_id", "rider_pseudonym", "fare_sar", "city"],
        allow=["rider_pseudonym"],
    )
    assert verdict.ok
    assert verdict.pseudonymised == ("rider_pseudonym",)
    assert "OK" in verdict.render()


def test_precise_coordinates_never_cross_the_boundary():
    """lat/lon in a gold product is a violation even with a good reason."""
    verdict = check_serving_boundary("gold.eta_features", ["trip_id", "lat", "lon"])
    assert not verdict.ok
    assert set(verdict.violations) == {"lat", "lon"}


def test_zone_centroids_may_cross_the_boundary():
    """Zone-resolution geography is public; it is the RESOLUTION that is the control."""
    verdict = check_serving_boundary(
        "gold.dim_zone", ["zone_key", "zone_name_en", "centroid_lat", "centroid_lon", "city"]
    )
    assert verdict.ok


def test_online_store_payload_is_clean():
    """The Redis feature payload carries no personal field, at zone grain."""
    verdict = check_serving_boundary(
        "redis masar:features:zone:*",
        [
            "rolling_zone_demand_15m",
            "rolling_avg_speed_10m",
            "historical_route_duration",
            "weather_condition",
            "feature_ts",
        ],
    )
    assert verdict.ok


def test_minimise_drops_restricted_columns_and_keeps_the_rest():
    """Minimisation: a column you did not publish cannot leak."""
    kept = minimise(SILVER_TRIPS_COLUMNS)
    assert "rider_id" not in kept
    assert "trip_id" in kept
    assert "fare_sar" in kept
    assert "dropoff_geohash" in kept  # personal-coarse is not restricted at serving


def test_minimise_honours_an_explicit_keep_list():
    """Exceptions are possible and must be explicit, so they can be reviewed."""
    kept = minimise(["trip_id", "rider_id"], keep=["rider_id"])
    assert kept == ["trip_id", "rider_id"]
