"""Feature-window validity — the leakage lint, tested at the arithmetic level.

Feature leakage is the most expensive bug in applied ML because it presents as
success: the offline metric goes UP. Every version of it in this course
reduces to the two integers of a Spark ``rangeBetween``, so that is what these
tests exercise — no Spark, no data, no model.
"""

from __future__ import annotations

import pytest

from masar.transform.feature_spec import (
    DAY_S,
    ETA_FEATURE_WINDOWS,
    HOUR_S,
    UNAVAILABLE_AT_INFERENCE,
    FeatureWindow,
    LeakageError,
    audit_feature_set,
    correlation_is_suspicious,
    validate_windows,
)


@pytest.mark.parametrize(
    ("start", "end", "valid"),
    [
        (-HOUR_S, -1, True),  # prior hour, strictly before — correct
        (-DAY_S, -1, True),
        (-HOUR_S, 0, False),  # inclusive of NOW: leaks on ties
        (-450, 450, False),  # centred: half the window is the future
        (-HOUR_S, HOUR_S, False),
        (0, 0, False),
        (-1, -HOUR_S, False),  # inverted window
    ],
)
def test_point_in_time_predicate(start, end, valid):
    """A window is point-in-time correct iff end < 0 and start <= end."""
    assert FeatureWindow("f", start, end).is_point_in_time is valid


def test_end_zero_is_the_subtle_bug():
    """``rangeBetween(-3600, 0)`` reads as 'the last hour' and is not.

    ``rangeBetween`` is inclusive of BOTH bounds, so with rows ordered by
    epoch second, an upper bound of 0 admits every other event in the same
    second. In a busy zone that is several trips which had not happened yet.
    One character; a metric that lies.
    """
    window = FeatureWindow("rolling_zone_demand_15m", -HOUR_S, 0)
    assert not window.is_point_in_time
    with pytest.raises(LeakageError, match="current row's own timestamp"):
        window.assert_point_in_time()


def test_centred_window_is_named_as_direct_leakage():
    """A centred window reaches into the future, and the message must say so."""
    with pytest.raises(LeakageError, match="PAST the event"):
        FeatureWindow("rolling_zone_demand_15m", -450, 450).assert_point_in_time()


def test_inverted_window_is_reported_as_inverted():
    """start > end is a different mistake and gets a different message."""
    with pytest.raises(LeakageError, match="inverted"):
        FeatureWindow("f", -1, -HOUR_S).assert_point_in_time()


def test_correct_window_asserts_silently():
    """The happy path must not raise, or the lint gets disabled."""
    FeatureWindow("f", -HOUR_S, -1).assert_point_in_time()


def test_window_width_is_reported_in_whole_seconds():
    """Both bounds are inclusive, so the prior hour is 3,600 seconds wide."""
    assert FeatureWindow("f", -HOUR_S, -1).width_seconds == HOUR_S


def test_every_declared_eta_window_is_point_in_time():
    """The shipped feature spec is the contract; it must be sound.

    ``build_eta_features.py --fixed`` validates against these windows, so a
    leaking declaration here would make the "fixed" build leak too.
    """
    assert validate_windows(ETA_FEATURE_WINDOWS) == []
    for window in ETA_FEATURE_WINDOWS.values():
        assert window.end == -1, f"{window.name} must end strictly before the event"
        assert window.rationale.strip(), f"{window.name} has no stated rationale"


def test_validate_windows_reports_every_offender_not_just_the_first():
    """A review needs the whole list, not the first thing that failed."""
    problems = validate_windows(
        {
            "a": FeatureWindow("a", -900, 900),
            "b": FeatureWindow("b", -DAY_S, 0),
            "c": FeatureWindow("c", -HOUR_S, -1),
        }
    )
    assert len(problems) == 2
    assert any("'a'" in p for p in problems)
    assert any("'b'" in p for p in problems)


def test_audit_flags_columns_unavailable_at_inference():
    """``distance_km`` is the actual distance driven — unknown until dropoff.

    The fix keeps the column NAME (the contract is the name) and changes the
    provenance to the routed distance. Training on the actual and serving the
    routed is the same bug wearing a disguise.
    """
    audit = audit_feature_set(["trip_id", "distance_km", "rolling_zone_demand_15m"])
    assert "distance_km" in audit["unavailable_online"]
    assert "distance_km" in UNAVAILABLE_AT_INFERENCE


def test_audit_flags_the_label_itself():
    """The label must never appear in the feature list, under any name."""
    audit = audit_feature_set(["label_actual_duration_min", "duration_min"])
    assert set(audit["unavailable_online"]) == {"label_actual_duration_min", "duration_min"}


def test_audit_flags_leaking_declared_windows():
    """A declared-but-leaking window is reported against the column that uses it."""
    leaking = dict(ETA_FEATURE_WINDOWS)
    leaking["rolling_zone_demand_15m"] = FeatureWindow("rolling_zone_demand_15m", -450, 450)
    audit = audit_feature_set(["rolling_zone_demand_15m"], leaking)
    assert audit["leaking"] == ["rolling_zone_demand_15m"]


def test_audit_flags_undeclared_rolling_columns():
    """A rolling column with no declared window is not wrong — it is unreviewed."""
    audit = audit_feature_set(["zone_demand_prev_hr", "driver_recent_trip_count"])
    assert "zone_demand_prev_hr" in audit["undeclared"]
    assert "driver_recent_trip_count" not in audit["undeclared"]  # it IS declared


def test_a_clean_feature_set_produces_an_empty_audit():
    """No false positives on a well-formed feature list."""
    audit = audit_feature_set(["trip_id", "hour_of_day", "day_of_week", "rolling_zone_demand_15m"])
    assert audit == {"leaking": [], "unavailable_online": [], "undeclared": []}


@pytest.mark.parametrize(
    ("r", "suspicious"),
    [(0.947, True), (-0.95, True), (0.90, True), (0.72, False), (-0.51, False)],
)
def test_suspicious_correlation_threshold(r, suspicious):
    """|r| >= 0.90 against the label earns an explanation before the model ships.

    Not proof of leakage — distance genuinely predicts duration — but the
    correlation that must be justified rather than celebrated.
    """
    assert correlation_is_suspicious(r) is suspicious
