"""Data profiling — including the geohash null-rate trap.

The trap is worth stating plainly, because it is the reason this test exists:
bronze lands CSV as STRING, so a missing ``dropoff_geohash`` is ``''``, not
``NULL``. A profiler that counts only nulls reports Masar's 3.1% geohash
defect as 0.0%, the swamp smell is never named, and the gap reaches the
feature table as a plausible-looking zone that does not exist.
"""

from __future__ import annotations

import pytest

from masar.ingest.profiling import (
    NULL_RATE_THRESHOLDS,
    distinct_counts,
    format_report,
    is_missing,
    null_rate,
    null_rates,
    profile_rows,
    timestamp_format_mix,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (None, True),
        ("", True),
        ("   ", True),
        ("thewke6", False),
        (0, False),  # a zero fare is a data-quality problem, not a gap
        (0.0, False),
        ("0", False),
        (False, False),
    ],
)
def test_missing_definition(value, expected):
    """Only null and blank strings count as missing — never a falsy value."""
    assert is_missing(value) is expected


def test_geohash_null_rate_counts_empty_strings(trips_rows):
    """THE test. Empty-string geohashes must be counted as missing.

    The fixture has 3 blank geohashes in 10 rows. Counting only ``is None``
    would report 0.0 and the defect would profile clean.
    """
    assert null_rate(trips_rows, "dropoff_geohash") == pytest.approx(0.3)

    nulls_only = sum(1 for r in trips_rows if r["dropoff_geohash"] is None)
    assert nulls_only == 0, "the defect is '' not None — that is the whole trap"


def test_geohash_rate_breaches_its_declared_threshold(trips_rows):
    """The threshold exists so a DEGRADATION is an event, not a shrug.

    3.1% is tolerated in production; the fixture's 30% is not, and the
    profiler must say so rather than reporting a number nobody compares.
    """
    rate = null_rate(trips_rows, "dropoff_geohash")
    assert rate > NULL_RATE_THRESHOLDS["dropoff_geohash"]


def test_key_columns_have_a_zero_tolerance(trips_rows):
    """A missing business key is not a rate to monitor; it is a blocked batch."""
    assert NULL_RATE_THRESHOLDS["trip_id"] == 0.0
    assert null_rate(trips_rows, "trip_id") > 0.0  # the fixture has one blank key


def test_null_rates_cover_every_column(trips_rows):
    """Every column gets a rate, so nothing is missed by omission."""
    rates = null_rates(trips_rows)
    assert set(rates) == set(trips_rows[0])
    assert all(0.0 <= v <= 1.0 for v in rates.values())


def test_empty_batch_has_no_null_rate():
    """An empty table has no null rate; volume is a different signal.

    Returning 0.0 rather than raising matters: the profiler must not be the
    thing that breaks on the morning a feed delivers nothing.
    """
    assert null_rate([], "anything") == 0.0
    assert null_rates([]) == {}


def test_timestamp_format_mix_finds_the_two_percent(trips_rows):
    """Two formats in one column, and both must be counted."""
    mix = timestamp_format_mix(trips_rows, "pickup_ts")
    assert mix["iso"] == 9
    assert mix["eu"] == 1
    assert mix["unknown"] == 0


def test_distinct_counts_are_ordered_by_frequency(trips_rows):
    """Value frequencies, most common first — the out-of-domain value stands out."""
    counts = distinct_counts(trips_rows, "city")
    assert list(counts)[0] == "Riyadh"
    assert counts["Atlantis"] == 1


def test_profile_names_the_swamp_smells(trips_rows):
    """The report must produce FINDINGS, not just measurements."""
    report = profile_rows(trips_rows, key="trip_id")

    assert report.rows == 10
    assert report.duplicate_keys == 1  # TRP-...0007 appears twice

    smells = " | ".join(report.smells)
    assert "MISSING VALUES" in smells
    assert "dropoff_geohash" in smells
    assert "DUPLICATE KEYS" in smells
    assert "FORMAT DRIFT" in smells


def test_profile_detects_producer_version_drift(gps_rows):
    """Two producer versions in one batch is a finding in its own right."""
    report = profile_rows(gps_rows, key="event_id")
    assert any("PRODUCER DRIFT" in s for s in report.smells)


def test_format_report_renders_without_crashing(trips_rows):
    """The printed report is a deliverable; it must survive every fixture."""
    text = format_report(profile_rows(trips_rows, key="trip_id"), title="bronze/trips")
    assert "bronze/trips" in text
    assert "missing rate per column" in text
    assert "swamp smells" in text
