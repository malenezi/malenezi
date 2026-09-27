"""The table registry and path resolution.

One module owns every path and every table name in the platform. These tests
guard the two things that break quietly when it does not: a table referenced
by a name nobody defined, and a grain declared in one place but not another.
"""

from __future__ import annotations

import pytest

from masar import config


def test_every_registered_table_lives_under_its_zone():
    """A table's path must match its name's zone prefix.

    ``silver.trips`` living under ``bronze/`` is the kind of mistake that is
    obvious in review and invisible in production until a retention job
    deletes the wrong thing.
    """
    for name, table in config.TABLES.items():
        zone = name.split(".")[0]
        assert f"/{zone}/" in table.path, f"{name} is not under {zone}/"


def test_table_path_rejects_typos_with_the_known_names():
    """A typo'd table name must not silently create an empty directory."""
    with pytest.raises(KeyError, match="unknown table"):
        config.table_path("silver.trps")


def test_silver_and_gold_tables_declare_a_grain():
    """A conformed table with no declared grain has no contract to enforce."""
    for name, table in config.TABLES.items():
        if name.startswith(("silver.", "gold.")) and "quarantine" not in name:
            assert table.keys, f"{name} declares no grain"


def test_bronze_tables_declare_no_grain():
    """Bronze is an append-only ledger; duplicates are correct there."""
    for name, table in config.TABLES.items():
        if name.startswith("bronze."):
            assert table.keys == (), f"{name} must not claim a grain"


def test_every_table_is_described():
    """A table nobody described is a table nobody owns."""
    for name, table in config.TABLES.items():
        assert table.description.strip(), f"{name} has no description"


def test_city_codes_map_to_the_accepted_city_names():
    """The staging mapping and the accepted-values test must agree.

    If they drift, every trip in the un-mapped city quarantines and the demand
    mart silently loses a city.
    """
    assert set(config.CITY_CODES.values()) == set(config.KSA_CITIES)


def test_gps_raw_path_matches_gzipped_and_plain_files():
    """The course ships GPS gzipped; the labs refer to it by the plain name."""
    assert config.raw_path("gps", "2026-06-01").endswith("gps_2026-06-01.ndjson*")


def test_unknown_feed_is_rejected():
    """An unknown feed name is a typo, not a new data source."""
    with pytest.raises(ValueError, match="unknown feed"):
        config.raw_path("telemetry")


def test_vacuum_retention_is_never_zero():
    """RETAIN 0 HOURS ends the audit trail and can break concurrent readers."""
    assert config.VACUUM_RETAIN_HOURS >= 168


def test_lookback_is_shared_by_silver_and_gold():
    """One lookback constant, or the two layers silently disagree about late data."""
    assert config.LOOKBACK_DAYS >= 1


def test_resolve_table_accepts_names_and_paths():
    """Canonical names, lakehouse-relative paths and explicit paths all resolve.

    The assessments (PA-1..PA-3) build scratch tables under
    ``lakehouse/_assessments/`` so they cannot disturb a participant's real
    lakehouse. A resolver that only understood registered names would make
    every assessment tool unusable against them.
    """
    assert config.resolve_table("gold.eta_features") == config.TABLES["gold.eta_features"].path
    assert config.resolve_table("_assessments/pa3/eta_features").endswith(
        "_assessments/pa3/eta_features"
    )
    assert config.resolve_table("./lakehouse/silver/trips") == "./lakehouse/silver/trips"


def test_resolve_table_still_rejects_a_typod_canonical_name():
    """A dotted name that is not registered is a typo, not a path."""
    with pytest.raises(KeyError, match="unknown table"):
        config.resolve_table("gold.nope")
