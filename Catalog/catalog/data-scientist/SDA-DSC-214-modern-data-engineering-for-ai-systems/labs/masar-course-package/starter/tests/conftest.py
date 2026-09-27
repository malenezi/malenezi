"""Shared fixtures. Nothing here starts a JVM.

The whole test suite runs without PySpark, Kafka, Redis or Docker, in about a
second. That is deliberate: a test suite that needs the platform to be up is a
test suite that stops being run.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest

#: A trips fixture with the defects the real Masar feed carries, at a scale
#: you can count by hand. Column order matches data/raw/trips_YYYY-MM-DD.csv.
TRIPS_CSV = """\
trip_id,rider_id,driver_id,vehicle_id,city,pickup_zone_id,dropoff_zone_id,pickup_ts,dropoff_ts,distance_km,duration_min,fare_sar,surge_multiplier,payment_type,status,dropoff_geohash
TRP-20260601-0000001,RDR-000001,DRV-00001,VEH-00001,Riyadh,Z-RUH-01,Z-RUH-02,2026-06-01 08:00:00,2026-06-01 08:20:00,7.5,20.0,32.10,1.0,mada,completed,thewke6
TRP-20260601-0000002,RDR-000002,DRV-00002,VEH-00002,Jeddah,Z-JED-01,Z-JED-03,2026-06-01 09:15:00,2026-06-01 09:32:00,5.2,17.0,24.80,1.2,cash,completed,sggg6gq
TRP-20260601-0000003,RDR-000003,DRV-00003,VEH-00003,Dammam,Z-DMM-04,Z-DMM-06,01/06/2026 10:05,01/06/2026 10:31,9.1,26.0,41.55,1.0,apple_pay,completed,
TRP-20260601-0000004,RDR-000004,DRV-00004,VEH-00004,Riyadh,Z-RUH-05,Z-RUH-09,2026-06-01 11:00:00,2026-06-01 11:12:00,3.4,12.0,-5.00,1.0,mada,completed,thewkxx
TRP-20260601-0000005,RDR-000005,DRV-00005,VEH-00005,Riyadh,Z-RUH-02,Z-RUH-07,2026-06-01 12:00:00,2026-06-01 11:40:00,4.0,-20.0,18.00,1.0,wallet,completed,
TRP-20260601-0000006,RDR-000006,DRV-00006,VEH-00006,Atlantis,Z-XXX-01,Z-XXX-02,2026-06-01 13:00:00,2026-06-01 13:25:00,6.0,25.0,29.00,1.0,cash,completed,zzzzzz1
TRP-20260601-0000007,RDR-000007,DRV-00007,VEH-00007,Jeddah,Z-JED-02,Z-JED-08,2026-06-01 14:00:00,2026-06-01 14:30:00,11.0,30.0,3900.00,1.0,credit_card,completed,sggg7ab
TRP-20260601-0000007,RDR-000007,DRV-00007,VEH-00007,Jeddah,Z-JED-02,Z-JED-08,2026-06-01 14:00:00,2026-06-01 14:30:00,11.0,30.0,39.00,1.0,credit_card,completed,sggg7ab
,RDR-000009,DRV-00009,VEH-00009,Riyadh,Z-RUH-03,Z-RUH-04,2026-06-01 15:00:00,2026-06-01 15:18:00,6.2,18.0,27.40,1.0,mada,completed,thewk9z
TRP-20260601-0000010,RDR-000010,DRV-00010,VEH-00010,Dammam,Z-DMM-02,Z-DMM-05,2026-06-01 16:00:00,2026-06-01 16:22:00,8.0,22.0,35.00,7.5,cash,completed,
"""


@pytest.fixture(scope="session")
def trips_rows() -> list[dict]:
    """The trips fixture as a list of dicts, exactly as ``csv.DictReader`` gives it.

    Values are STRINGS, like bronze. Tests that pass pre-typed floats would be
    testing a code path that does not exist in the pipeline.
    """
    return list(csv.DictReader(io.StringIO(TRIPS_CSV)))


@pytest.fixture(scope="session")
def clean_trips_rows(trips_rows) -> list[dict]:
    """Only the rows that should survive the gate untouched."""
    return [
        r for r in trips_rows if r["trip_id"] in {"TRP-20260601-0000001", "TRP-20260601-0000002"}
    ]


@pytest.fixture(scope="session")
def gps_rows() -> list[dict]:
    """GPS positions from two producer versions — 2.5.0 shipping m/s.

    Means: 2.4.0 -> ~35.4 km/h (normal). 2.5.0 -> ~9.85 (the same speeds in
    metres per second). Every value individually plausible.
    """
    v240 = [
        {"event_id": f"ev-24-{i}", "producer_version": "2.4.0", "speed_kmh": s, "accuracy_m": 8.0}
        for i, s in enumerate([31.2, 35.0, 38.4, 33.1, 39.5, 35.8, 36.2, 34.0, 37.1, 34.2])
    ]
    v250 = [
        {"event_id": f"ev-25-{i}", "producer_version": "2.5.0", "speed_kmh": s, "accuracy_m": 7.0}
        for i, s in enumerate([8.7, 9.7, 10.7, 9.2, 11.0, 9.9, 10.1, 9.4, 10.3, 9.5])
    ]
    return v240 + v250


@pytest.fixture(scope="session")
def repo_root() -> Path:
    """The repository root, for tests that read shipped config files."""
    return Path(__file__).resolve().parent.parent
