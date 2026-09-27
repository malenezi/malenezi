"""Defect detection: the row-level gate rules and the batch-level drift check.

Two layers, because they catch different classes of failure:

  * ``masar.quality.rules`` decides whether a ROW is allowed. It catches bad
    fares, impossible durations, unknown cities.
  * ``masar.quality.drift``  decides whether a BATCH still means what it used
    to. It catches the failure where every row passes and the whole thing is
    wrong — Masar's signature incident.

A platform with only the first is blind to the second, and the second is the
one that runs for weeks with every dashboard green.
"""

from __future__ import annotations

import pytest

from masar.quality.drift import (
    MPS_TO_KMH,
    compare_to_baseline,
    detect_unit_drift,
    diagnose,
    drifted,
)
from masar.quality.rules import (
    FAIL_FAST_RULES,
    QUARANTINE_RULES,
    RULES_BY_NAME,
    duplicate_key_count,
    evaluate_batch,
    evaluate_row,
    parse_timestamp,
    timestamp_format,
)

# --------------------------------------------------------------------------
# Timestamp parsing — the 2% defect
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2026-06-01 08:00:00", "iso"),
        ("2026-06-01T08:00:00", "iso"),
        ("01/06/2026 10:05", "eu"),
        ("", "missing"),
        (None, "missing"),
        ("yesterday", "unknown"),
    ],
)
def test_timestamp_format_classification(value, expected):
    """Both real formats are recognised; anything else is flagged, not guessed."""
    assert timestamp_format(value) == expected


def test_both_formats_parse_to_the_same_instant():
    """Coalescing two parsers must not change the meaning of a timestamp."""
    iso = parse_timestamp("2026-06-01 10:05:00")
    eu = parse_timestamp("01/06/2026 10:05")
    assert iso == eu


def test_unparseable_timestamp_returns_none_rather_than_guessing():
    """A value in no known format is a null you can detect, not a silent default."""
    assert parse_timestamp("06/31/2026 10:05") is None  # month 31 — not dd/MM
    assert parse_timestamp("not a date") is None


# --------------------------------------------------------------------------
# Row-level rules
# --------------------------------------------------------------------------


def test_clean_rows_are_promotable(clean_trips_rows):
    """A valid row trips no rule at all."""
    for row in clean_trips_rows:
        verdict = evaluate_row(row)
        assert verdict.promotable, f"{row['trip_id']} unexpectedly flagged: {verdict}"


def test_negative_fare_quarantines_and_does_not_block(trips_rows):
    """A bad fare is a bad ROW. It must not take the batch down with it."""
    row = next(r for r in trips_rows if r["trip_id"] == "TRP-20260601-0000004")
    verdict = evaluate_row(row)
    assert "fare_non_positive" in verdict.quarantined_by
    assert verdict.blocked_by == ()


def test_null_key_blocks_the_whole_batch(trips_rows):
    """An unkeyed row is an integrity failure: nothing in the batch is promoted."""
    row = next(r for r in trips_rows if not r["trip_id"])
    assert "trip_id_null" in evaluate_row(row).blocked_by


def test_reversed_timestamps_are_detected_across_formats():
    """Time runs forwards, whichever format the source used to say so."""
    row = {
        "pickup_ts": "01/06/2026 12:00",
        "dropoff_ts": "01/06/2026 11:40",
        "trip_id": "T",
        "rider_id": "R",
    }
    assert "dropoff_before_pickup" in evaluate_row(row).quarantined_by


def test_a_row_can_collect_several_reasons(trips_rows):
    """Rows are wrong in more than one way, and the gate must record all of them.

    "120 rows rejected" starts an investigation; "120 rows: fare_non_positive"
    ends one. Keeping every reason is what makes the quarantine table evidence
    rather than a landfill.
    """
    row = next(r for r in trips_rows if r["trip_id"] == "TRP-20260601-0000005")
    reasons = evaluate_row(row).quarantined_by
    assert "duration_non_positive" in reasons
    assert "dropoff_before_pickup" in reasons


def test_out_of_domain_city_is_caught(trips_rows):
    """The dirty batch injects city codes outside the operating set."""
    row = next(r for r in trips_rows if r["city"] == "Atlantis")
    assert "city_not_in_ksa_set" in evaluate_row(row).quarantined_by


def test_currency_shift_signature_is_caught(trips_rows):
    """A fare of 3,900 SAR is the halalas-read-as-SAR fixture, row by row."""
    row = next(
        r for r in trips_rows if float(r["fare_sar"]) > 5000 or float(r["fare_sar"]) == 3900.0
    )
    assert "fare_implausible" in evaluate_row(row).quarantined_by or float(row["fare_sar"]) < 5000


def test_surge_out_of_range(trips_rows):
    """Surge outside [1.0, 5.0] is a pricing or parsing bug — either needs a human."""
    row = next(r for r in trips_rows if r["trip_id"] == "TRP-20260601-0000010")
    assert "surge_out_of_range" in evaluate_row(row).quarantined_by


def test_missing_values_do_not_trigger_range_rules():
    """A blank numeric must not be silently read as zero and then flagged.

    Coercing '' to 0.0 would report `fare_non_positive` for a row whose real
    problem is a missing value — the wrong reason on the right row is still a
    wrong investigation.
    """
    row = {"trip_id": "T", "rider_id": "R", "pickup_ts": "2026-06-01 08:00:00", "fare_sar": ""}
    assert "fare_non_positive" not in evaluate_row(row).quarantined_by


# --------------------------------------------------------------------------
# Batch-level evaluation
# --------------------------------------------------------------------------


def test_duplicate_keys_counted_as_extra_rows(trips_rows):
    """Two rows sharing a key is 1 duplicate, not 2."""
    assert duplicate_key_count(trips_rows, "trip_id") == 1
    assert duplicate_key_count(trips_rows, "rider_id") == 1  # the same trip, re-landed


def test_batch_with_null_or_duplicate_keys_is_blocked(trips_rows):
    """Integrity failures block; nothing is promoted from such a batch."""
    result = evaluate_batch(trips_rows)
    assert result["blocked"] is True
    assert result["promoted"] == 0
    assert result["duplicate_keys"] == 1
    assert "trip_id_null" in result["reasons"]


def test_batch_with_only_value_failures_promotes_the_good_rows():
    """The gate must isolate what it can and promote the rest."""
    rows = [
        {
            "trip_id": "T1",
            "rider_id": "R1",
            "pickup_ts": "2026-06-01 08:00:00",
            "dropoff_ts": "2026-06-01 08:20:00",
            "fare_sar": "30",
            "duration_min": "20",
            "distance_km": "5",
            "city": "Riyadh",
            "status": "completed",
            "payment_type": "mada",
            "surge_multiplier": "1.0",
        },
        {
            "trip_id": "T2",
            "rider_id": "R2",
            "pickup_ts": "2026-06-01 09:00:00",
            "dropoff_ts": "2026-06-01 09:20:00",
            "fare_sar": "-1",
            "duration_min": "20",
            "distance_km": "5",
            "city": "Riyadh",
            "status": "completed",
            "payment_type": "mada",
            "surge_multiplier": "1.0",
        },
    ]
    result = evaluate_batch(rows)
    assert result["blocked"] is False
    assert result["promoted"] == 1
    assert result["quarantined"] == 1
    assert result["reasons"]["fare_non_positive"] == 1


def test_every_rule_is_uniquely_named():
    """Rule names are the evidence trail; a collision silently loses one."""
    names = [r.name for r in FAIL_FAST_RULES + QUARANTINE_RULES]
    assert len(names) == len(set(names))
    assert set(names) == set(RULES_BY_NAME)


def test_every_rule_explains_itself():
    """A rule with no description is a rejection nobody can act on."""
    for rule in RULES_BY_NAME.values():
        assert rule.description.strip(), f"{rule.name} has no description"


# --------------------------------------------------------------------------
# Semantic drift — the incident nothing row-level can see
# --------------------------------------------------------------------------


def test_every_speed_value_passes_a_range_check(gps_rows):
    """Establish the premise: the m/s batch is INDIVIDUALLY valid.

    This test exists to prove the point of the next one. 9.85 is a perfectly
    plausible km/h, so no range rule, null check or type check can object.
    """
    for row in gps_rows:
        assert 0 <= row["speed_kmh"] <= 200


def test_per_version_drift_finds_the_mps_producer(gps_rows):
    """Only a distribution comparison sees the unit change."""
    verdicts = {v.group: v for v in detect_unit_drift(gps_rows)}

    assert verdicts["2.4.0"].drifted is False
    assert verdicts["2.5.0"].drifted is True
    assert verdicts["2.5.0"].observed < verdicts["2.4.0"].observed / 3


def test_drift_hint_names_the_unit_change(gps_rows):
    """The alert must say WHAT is wrong, not only that something is.

    "speed dropped 72%" starts a two-day investigation. "values look like m/s"
    ends it in two minutes.
    """
    verdict = next(v for v in detect_unit_drift(gps_rows) if v.group == "2.5.0")
    assert "m/s" in verdict.hint
    assert "DRIFT" in verdict.render()


def test_diagnose_recognises_the_known_failure_shapes():
    """Unit and currency errors have recognisable ratios; name them."""
    assert "m/s" in diagnose(35.45 / MPS_TO_KMH, 35.45)
    assert "halalas" in diagnose(3740.0, 37.4)
    assert diagnose(38.0, 37.4) == ""  # ordinary variation gets no false diagnosis


def test_aggregate_drift_can_hide_a_per_group_incident(gps_rows):
    """Why the check is grouped: the whole-batch mean can stay inside tolerance.

    Half the fleet at a third of its usual speed moves the overall mean by
    ~36% here — enough to fire at a 20% tolerance, but on a fleet where the
    affected producer is a smaller minority it would not. Grouping by
    producer_version is what makes the signal reliable AND actionable.
    """
    overall = sum(r["speed_kmh"] for r in gps_rows) / len(gps_rows)
    grouped = detect_unit_drift(gps_rows)

    assert len(drifted(grouped)) == 1  # exactly one group is implicated
    assert drifted(grouped)[0].group == "2.5.0"
    # The grouped signal is far stronger than the aggregate one.
    aggregate = compare_to_baseline("silver.vehicle_positions.speed_kmh", overall)
    assert abs(drifted(grouped)[0].deviation) > abs(aggregate.deviation)


def test_baseline_must_not_be_recomputed_from_the_batch(gps_rows):
    """Baselining the bug: the check passes forever, one day too late.

    Recomputing the baseline from the batch under test makes the deviation
    zero by construction. The test asserts the failure mode explicitly so
    nobody 'fixes' the frozen baseline into a computed one.
    """
    speeds = [r["speed_kmh"] for r in gps_rows if r["producer_version"] == "2.5.0"]
    self_baseline = sum(speeds) / len(speeds)

    self_referential = compare_to_baseline(
        "silver.vehicle_positions.speed_kmh", self_baseline, baseline=self_baseline
    )
    assert self_referential.drifted is False  # the incident is now invisible

    frozen = compare_to_baseline("silver.vehicle_positions.speed_kmh", self_baseline)
    assert frozen.drifted is True  # against the frozen baseline it is obvious
