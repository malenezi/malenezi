"""Paths, environment and the canonical table registry.

One module owns every filesystem path and every table name in the platform.
Hard-coding ``./lakehouse/silver/trips`` in nine modules is how a rename
becomes a two-day outage; here it is one constant.

``LAKEHOUSE_ROOT`` is a local stand-in for an object-storage bucket
(``s3://masar-lakehouse/``). The directory layout is deliberately identical to
the bucket layout — ``zone/table/partition=.../part-*.parquet`` — so moving to
S3 or ADLS is a configuration change, not a rewrite. That is what
compute-storage separation buys you (Module 2).

This module is pure Python: no PySpark, no network, no side effects beyond
reading ``.env``.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# .env is optional. Its absence is normal (CI, graders, a fresh clone) and
# must never be an error.
try:  # pragma: no cover - trivial optional dependency shim
    from dotenv import load_dotenv

    load_dotenv(override=False)
except Exception:  # pragma: no cover
    pass


def _env(name: str, default: str) -> str:
    """Read an environment variable, falling back to the documented default."""
    value = os.environ.get(name, "").strip()
    return value or default


def _env_int(name: str, default: int) -> int:
    """Read an integer environment variable, tolerating junk in .env."""
    try:
        return int(_env(name, str(default)))
    except ValueError:
        return default


# --------------------------------------------------------------- storage --

LAKEHOUSE_ROOT = _env("MASAR_LAKEHOUSE_ROOT", "./lakehouse")
RAW_ROOT = _env("MASAR_RAW_ROOT", "./data/raw")
FIXTURES_ROOT = _env("MASAR_FIXTURES_ROOT", "./data/fixtures")

BRONZE = f"{LAKEHOUSE_ROOT}/bronze"
SILVER = f"{LAKEHOUSE_ROOT}/silver"
GOLD = f"{LAKEHOUSE_ROOT}/gold"
QUARANTINE_ROOT = f"{LAKEHOUSE_ROOT}/quarantine"
CHECKPOINTS = f"{LAKEHOUSE_ROOT}/_checkpoints"
GOVERNANCE_ROOT = f"{LAKEHOUSE_ROOT}/governance"

# --------------------------------------------------------------- runtime --

SPARK_APP_NAME = _env("MASAR_SPARK_APP_NAME", "masar-lakehouse")
SPARK_SHUFFLE_PARTITIONS = _env_int("MASAR_SPARK_SHUFFLE_PARTITIONS", 8)

KAFKA_BOOTSTRAP = _env("MASAR_KAFKA_BOOTSTRAP", "localhost:9092")
KAFKA_TOPIC = _env("MASAR_KAFKA_TOPIC", "masar.gps.pings")

REDIS_HOST = _env("MASAR_REDIS_HOST", "localhost")
REDIS_PORT = _env_int("MASAR_REDIS_PORT", 6379)
REDIS_DB = _env_int("MASAR_REDIS_DB", 0)
REDIS_ZONE_KEY = "masar:features:zone:{zone_id}"

BUSINESS_DATE = _env("MASAR_BUSINESS_DATE", "2026-06-01")

# ------------------------------------------------------------ governance --

VACUUM_RETAIN_HOURS = _env_int("MASAR_VACUUM_RETAIN_HOURS", 168)  # 7 days. Never 0.
GPS_RETENTION_DAYS = _env_int("MASAR_GPS_RETENTION_DAYS", 180)

# --------------------------------------------------------- business rules --

# The raw feeds carry city CODES; the conformed layers carry city NAMES.
# The mapping is applied exactly once, at the staging boundary (Lab 3).
CITY_CODES: dict[str, str] = {
    "RUH": "Riyadh",
    "JED": "Jeddah",
    "DMM": "Dammam",
    "MKK": "Mecca",
    "MED": "Medina",
}
KSA_CITIES: list[str] = ["Riyadh", "Jeddah", "Dammam", "Mecca", "Medina"]
TRIP_STATUS: list[str] = ["completed", "cancelled_rider", "cancelled_driver", "no_show"]
PAYMENT_TYPES: list[str] = ["mada", "credit_card", "apple_pay", "cash", "wallet"]

# Lookback window shared by silver (dbt) and gold (Spark). Late-arriving trips
# inside this window are corrected by MERGE; beyond it they are missed. Change
# it in ONE place or the two layers silently disagree.
LOOKBACK_DAYS = 3


# ------------------------------------------------------ table registry ----


@dataclass(frozen=True)
class Table:
    """A canonical lakehouse table: its name, its path, its business key.

    ``name`` is what dbt, Spark SQL, the slides and the labs all call it.
    ``path`` is where it physically lives. ``keys`` is the declared grain —
    ``masar.transform.build_gold._assert_grain`` enforces it on every write.
    """

    name: str
    path: str
    keys: tuple[str, ...] = ()
    description: str = ""


TABLES: dict[str, Table] = {
    # ---- bronze: append-only ledger of what ARRIVED ----------------------
    "bronze.trips": Table(
        "bronze.trips",
        f"{BRONZE}/trips",
        (),
        "Raw trips as received; duplicates and defects preserved on purpose.",
    ),
    "bronze.gps_events": Table(
        "bronze.gps_events",
        f"{BRONZE}/gps_events",
        (),
        "Raw GPS pings with the payload struct exactly as the device sent it.",
    ),
    "bronze.drivers": Table(
        "bronze.drivers",
        f"{BRONZE}/drivers",
        (),
        "Raw driver roster; hire_date arrives in mixed formats.",
    ),
    "bronze.payments": Table(
        "bronze.payments",
        f"{BRONZE}/payments",
        (),
        "Raw payment settlements, one row per payment_id as received.",
    ),
    "bronze.vehicles": Table("bronze.vehicles", f"{BRONZE}/vehicles", (), "Raw vehicle roster."),
    "bronze.zones": Table("bronze.zones", f"{BRONZE}/zones", (), "Raw zone reference data."),
    # ---- silver: conformed, validated, one row per business key ----------
    "silver.trips": Table(
        "silver.trips",
        f"{SILVER}/trips",
        ("trip_id",),
        "Conformed completed trips. THE contract for every AI and BI consumer.",
    ),
    "silver.vehicle_positions": Table(
        "silver.vehicle_positions",
        f"{SILVER}/vehicle_positions",
        ("event_id",),
        "Deduplicated GPS positions, speed always km/h, accuracy <= 50 m.",
    ),
    "silver.drivers": Table(
        "silver.drivers", f"{SILVER}/drivers", ("driver_id",), "Conformed driver roster."
    ),
    "silver.payments": Table(
        "silver.payments", f"{SILVER}/payments", ("payment_id",), "Conformed settlements."
    ),
    "silver.trips_quarantine": Table(
        "silver.trips_quarantine",
        f"{SILVER}/trips_quarantine",
        (),
        "Rows the gate refused to promote, each tagged with WHY.",
    ),
    # ---- gold (BI): conformed star schema --------------------------------
    "gold.fact_trip": Table(
        "gold.fact_trip", f"{GOLD}/fact_trip", ("trip_id",), "Trip-grain fact."
    ),
    "gold.dim_driver": Table(
        "gold.dim_driver", f"{GOLD}/dim_driver", ("driver_key",), "Type-1 driver dimension."
    ),
    "gold.dim_vehicle": Table(
        "gold.dim_vehicle", f"{GOLD}/dim_vehicle", ("vehicle_key",), "Vehicle dimension."
    ),
    "gold.dim_zone": Table(
        "gold.dim_zone", f"{GOLD}/dim_zone", ("zone_key",), "Zone dimension, bilingual labels."
    ),
    "gold.dim_date": Table(
        "gold.dim_date", f"{GOLD}/dim_date", ("date_key",), "THE conformed date dimension."
    ),
    "gold.bi_trips_safe": Table(
        "gold.bi_trips_safe",
        f"{GOLD}/bi_trips_safe",
        ("trip_id",),
        "PDPL-safe analyst view: pseudonymised rider, no precise location.",
    ),
    # ---- gold (AI): features and marts -----------------------------------
    "gold.eta_features": Table(
        "gold.eta_features",
        f"{GOLD}/eta_features",
        ("trip_id",),
        "The AI product. Point-in-time correct ETA features + label.",
    ),
    "gold.trip_features": Table(
        "gold.trip_features",
        f"{GOLD}/trip_features",
        ("trip_id",),
        "General trip features, strictly-prior windows only.",
    ),
    "gold.zone_hourly_demand": Table(
        "gold.zone_hourly_demand",
        f"{GOLD}/zone_hourly_demand",
        ("city", "pickup_zone_id", "date", "hour"),
        "BI demand mart.",
    ),
    "gold.driver_daily": Table(
        "gold.driver_daily", f"{GOLD}/driver_daily", ("driver_id", "date"), "BI driver mart."
    ),
}


def table_path(name: str) -> str:
    """Resolve a canonical table name (``silver.trips``) to its storage path.

    Raises:
        KeyError: with the full list of known names, because a typo'd table
            name that silently creates an empty directory is the single most
            expensive five-minute bug in this course.
    """
    try:
        return TABLES[name].path
    except KeyError:
        known = ", ".join(sorted(TABLES))
        raise KeyError(f"unknown table {name!r}; known tables: {known}") from None


def resolve_table(name_or_path: str) -> str:
    """Resolve a canonical table name OR a path to a storage path.

    Accepts all three of the forms the labs and assessments use:

        ``gold.eta_features``            a registered canonical name
        ``_assessments/pa3/eta_features`` a path relative to the lakehouse root
        ``./lakehouse/gold/eta_features`` an explicit path

    The assessments write scratch tables outside the registry on purpose (they
    must not disturb the participant's real lakehouse), so a resolver that only
    understood registered names would make every assessment tool unusable.
    """
    if name_or_path in TABLES:
        return TABLES[name_or_path].path
    if name_or_path.startswith(("./", "/", "../")) or name_or_path.startswith(LAKEHOUSE_ROOT):
        return name_or_path
    if "." in name_or_path and "/" not in name_or_path:
        # Looks like a canonical name but is not registered — say so clearly
        # rather than silently inventing an empty directory.
        return table_path(name_or_path)
    return f"{LAKEHOUSE_ROOT}/{name_or_path.lstrip('/')}"


def ensure_dirs() -> None:
    """Create the lakehouse zone directories. Idempotent; safe to call anywhere."""
    for d in (BRONZE, SILVER, GOLD, QUARANTINE_ROOT, CHECKPOINTS, GOVERNANCE_ROOT):
        Path(d).mkdir(parents=True, exist_ok=True)


def raw_path(feed: str, business_date: str | None = None) -> str:
    """Path of a raw feed file.

    Args:
        feed: one of ``trips``, ``gps``, ``drivers``, ``vehicles``, ``zones``,
            ``payments``, ``weather``.
        business_date: ``YYYY-MM-DD`` for the dated feeds; ignored otherwise.

    Returns:
        The path as a string. GPS files may be gzipped — Spark reads
        ``.ndjson`` and ``.ndjson.gz`` through the same glob.
    """
    d = business_date or BUSINESS_DATE
    match feed:
        case "trips":
            return f"{RAW_ROOT}/trips_{d}.csv"
        case "gps":
            return f"{RAW_ROOT}/gps/gps_{d}.ndjson*"
        case "payments":
            return f"{RAW_ROOT}/payments_{d}.csv"
        case "drivers" | "vehicles" | "zones":
            return f"{RAW_ROOT}/{feed}.csv"
        case "weather":
            return f"{RAW_ROOT}/weather_hourly.csv"
        case _:
            raise ValueError(f"unknown feed {feed!r}")
