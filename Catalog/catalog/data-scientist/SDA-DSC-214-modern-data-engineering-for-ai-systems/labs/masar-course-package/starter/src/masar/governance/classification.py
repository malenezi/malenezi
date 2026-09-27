"""PDPL data classification — which columns are personal, and what follows.

Saudi Arabia's Personal Data Protection Law is treated here as a first-class
engineering constraint, not a slide at the end of the deck. Classification is
the root of everything downstream: access control, retention windows, what may
cross the serving boundary, and what an erasure request has to touch.

The classes, from least to most restricted:

    ``public``                  no restriction (city, zone name)
    ``operational``             internal identifiers with no data subject
    ``commercial``              financial values; retained for tax law, not PDPL
    ``personal-coarse``         indirectly identifying at low resolution
    ``personal-pseudonymised``  hashed at source; still personal data
    ``personal``                directly identifies a data subject
    ``sensitive-location``      precise coordinates; the strictest class here

The two rules that trip people up:

  1. A HASH IS NOT ANONYMISATION. ``national_id_hash`` is pseudonymised
     personal data. It still belongs to a person, it is still in scope for an
     erasure request, and it still must not reach a dashboard.
  2. PRECISE LOCATION IS SPECIAL. lat/lon at metre resolution reveals homes,
     workplaces and routines. It gets its own class, a shorter retention
     window, and it never leaves silver.

Pure Python: importable anywhere, testable in milliseconds, and usable by
``masar.serve.pdpl_boundary_check`` before a single Spark session exists.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

PUBLIC = "public"
OPERATIONAL = "operational"
COMMERCIAL = "commercial"
PERSONAL_COARSE = "personal-coarse"
PERSONAL_PSEUDONYMISED = "personal-pseudonymised"
PERSONAL = "personal"
SENSITIVE_LOCATION = "sensitive-location"

#: Classes that may never appear in a BI product or the online feature store.
RESTRICTED_AT_SERVING: frozenset[str] = frozenset(
    {PERSONAL, PERSONAL_PSEUDONYMISED, SENSITIVE_LOCATION}
)

#: The column classification for the whole Masar platform. One dict, because
#: two dicts become two policies and then a leak.
CLASSIFICATION: dict[str, str] = {
    # --- direct identifiers of a data subject --------------------------
    "rider_id": PERSONAL,
    "driver_id": PERSONAL,
    "full_name_en": PERSONAL,
    # --- pseudonymised at source, still personal data -------------------
    "national_id_hash": PERSONAL_PSEUDONYMISED,
    "phone_hash": PERSONAL_PSEUDONYMISED,
    "plate_hash": PERSONAL_PSEUDONYMISED,
    "rider_pseudonym": PERSONAL_PSEUDONYMISED,
    # --- precise location -----------------------------------------------
    "lat": SENSITIVE_LOCATION,
    "lon": SENSITIVE_LOCATION,
    "centroid_lat": PUBLIC,  # zone centroid: a district, not a doorstep
    "centroid_lon": PUBLIC,
    # --- indirectly identifying at low resolution ------------------------
    "dropoff_geohash": PERSONAL_COARSE,
    "pickup_zone_id": OPERATIONAL,
    "dropoff_zone_id": OPERATIONAL,
    # --- operational -----------------------------------------------------
    "trip_id": OPERATIONAL,
    "vehicle_id": OPERATIONAL,
    "event_id": OPERATIONAL,
    "payment_id": OPERATIONAL,
    "speed_kmh": OPERATIONAL,
    "heading_deg": OPERATIONAL,
    "accuracy_m": OPERATIONAL,
    "pickup_ts": OPERATIONAL,
    "dropoff_ts": OPERATIONAL,
    "status": OPERATIONAL,
    # --- commercial -------------------------------------------------------
    "fare_sar": COMMERCIAL,
    "amount_sar": COMMERCIAL,
    "surge_multiplier": COMMERCIAL,
    "payment_type": COMMERCIAL,
    # --- public ------------------------------------------------------------
    "city": PUBLIC,
    "zone_name_en": PUBLIC,
    "zone_name_ar": PUBLIC,
    "district": PUBLIC,
    "distance_km": PUBLIC,
    "duration_min": PUBLIC,
    "weather_condition": PUBLIC,
    # --- derived features and mart columns ---------------------------------
    # Aggregates ABOUT a zone or an hour, never about a person. They are
    # listed explicitly rather than pattern-matched, because `classify()`
    # fails closed: an unlisted column is treated as personal until somebody
    # has actually looked at it. That is the intended friction — adding a
    # feature should require a one-line classification decision.
    "rolling_zone_demand_15m": OPERATIONAL,
    "rolling_avg_speed_10m": OPERATIONAL,
    "historical_route_duration": OPERATIONAL,
    "zone_demand_prev_hr": OPERATIONAL,
    "zone_avg_fare_prev_hr": COMMERCIAL,
    "driver_trips_prev_24h": OPERATIONAL,
    "driver_recent_trip_count": OPERATIONAL,
    "hour_of_day": PUBLIC,
    "day_of_week": PUBLIC,
    "start_hour": PUBLIC,
    "pickup_hour": PUBLIC,
    "is_night": PUBLIC,
    "is_weekend": PUBLIC,
    "feature_ts": OPERATIONAL,
    "trip_date": OPERATIONAL,
    "pickup_date": OPERATIONAL,
    "label_actual_duration_min": PUBLIC,
    "fare_per_km": COMMERCIAL,
    "fare_per_km_sar": COMMERCIAL,
    "revenue_sar": COMMERCIAL,
    "gross_earnings_sar": COMMERCIAL,
    "trips": OPERATIONAL,
    "trips_completed": OPERATIONAL,
    "trips_cancelled": OPERATIONAL,
    "active_drivers": OPERATIONAL,
    "completion_rate": OPERATIONAL,
    # --- dimension keys ------------------------------------------------------
    # A surrogate key that IS the natural key inherits its class. `driver_key`
    # is `driver_id` with a new name, so it is personal data, and exposing it
    # to BI is a documented exception (see docs/GOVERNANCE_TEMPLATE.md), not
    # an accident of naming.
    "driver_key": PERSONAL,
    "vehicle_key": OPERATIONAL,
    "zone_key": OPERATIONAL,
    "date_key": PUBLIC,
    "pickup_zone_key": OPERATIONAL,
    "dropoff_zone_key": OPERATIONAL,
    "full_date": PUBLIC,
}

#: Retention windows in days, per class. ``None`` means "no PDPL limit" —
#: which is not the same as "keep forever": financial records are kept for
#: seven years because tax law says so, and that is a different obligation.
RETENTION_DAYS: dict[str, int | None] = {
    SENSITIVE_LOCATION: 180,
    PERSONAL: 730,
    PERSONAL_PSEUDONYMISED: 730,
    PERSONAL_COARSE: 730,
    COMMERCIAL: 2555,  # 7 years, financial record
    OPERATIONAL: None,
    PUBLIC: None,
}

#: Who may read what. Analysts get gold only; data scientists get silver;
#: precise GPS is restricted to a named role with a logged purpose.
ACCESS_POLICY: dict[str, tuple[str, ...]] = {
    PUBLIC: ("analyst", "data_scientist", "engineer", "dpo"),
    OPERATIONAL: ("analyst", "data_scientist", "engineer", "dpo"),
    COMMERCIAL: ("analyst", "data_scientist", "engineer", "dpo"),
    PERSONAL_COARSE: ("data_scientist", "engineer", "dpo"),
    PERSONAL_PSEUDONYMISED: ("engineer", "dpo"),
    PERSONAL: ("engineer", "dpo"),
    SENSITIVE_LOCATION: ("dpo",),
}


def classify(column: str) -> str:
    """Classify one column.

    Unknown columns are classified ``personal`` on purpose: an unclassified
    column is an unreviewed column, and the safe default for unreviewed data
    is the restricted one. Fail closed, not open.
    """
    return CLASSIFICATION.get(column, PERSONAL)


def classify_columns(columns: Iterable[str]) -> dict[str, str]:
    """Classify a whole column list, e.g. ``df.columns``."""
    return {c: classify(c) for c in columns}


@dataclass(frozen=True)
class BoundaryVerdict:
    """The result of checking a dataset against the serving boundary.

    Attributes:
        dataset: what was checked (``gold.fact_trip``, ``redis:masar:features:*``).
        columns: the columns examined.
        violations: columns whose class may not cross the boundary.
        pseudonymised: pseudonymised columns present — allowed, but recorded,
            because a pseudonym is still in scope for an erasure request.
    """

    dataset: str
    columns: tuple[str, ...]
    violations: tuple[str, ...]
    pseudonymised: tuple[str, ...]

    @property
    def ok(self) -> bool:
        """True when nothing restricted crossed the boundary."""
        return not self.violations

    def render(self) -> str:
        """One line per dataset, in the shape Lab 8 Task 5 expects."""
        status = "OK" if self.ok else "VIOLATION"
        personal = list(self.violations)
        return (
            f"[pdpl] {self.dataset:<28} columns={len(self.columns):<3} "
            f"personal={personal}  pseudonymised={list(self.pseudonymised)}  {status}"
        )


def check_serving_boundary(
    dataset: str, columns: Iterable[str], *, allow: Iterable[str] = ()
) -> BoundaryVerdict:
    """Assert that no restricted column crosses into a BI or online product.

    Args:
        dataset: the thing being checked, for the report line.
        columns: its column names.
        allow: explicit exceptions, each of which should be justified in
            ``docs/GOVERNANCE_TEMPLATE.md``. ``rider_pseudonym`` is the usual
            one: pseudonymised, cohort-analysis-only, never re-identified.

    Returns:
        A :class:`BoundaryVerdict`. ``ok`` is False if anything personal or
        precisely locational is present without an allow-list entry.
    """
    allowed = set(allow)
    cols = tuple(columns)
    violations, pseudonymised = [], []
    for column in cols:
        cls = classify(column)
        if cls == PERSONAL_PSEUDONYMISED:
            pseudonymised.append(column)
        if column in allowed:
            continue
        if cls in RESTRICTED_AT_SERVING:
            violations.append(column)
    return BoundaryVerdict(dataset, cols, tuple(violations), tuple(pseudonymised))


def retention_days(column: str) -> int | None:
    """Retention window in days for a column, or ``None`` if PDPL sets none."""
    return RETENTION_DAYS[classify(column)]


def readable_by(column: str, role: str) -> bool:
    """True when ``role`` is permitted to read ``column``."""
    return role in ACCESS_POLICY[classify(column)]


def minimise(columns: Iterable[str], *, keep: Iterable[str] = ()) -> list[str]:
    """Return the columns that may be published, dropping the restricted ones.

    Data minimisation is the cheapest PDPL control there is: a column you did
    not publish cannot leak, cannot be subpoenaed, and does not have to be
    found again when an erasure request arrives.
    """
    keep_set = set(keep)
    return [c for c in columns if c in keep_set or classify(c) not in RESTRICTED_AT_SERVING]
