#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_masar.py — synthetic data generator for the Masar (مسار) Lakehouse.

Course: SDA-DSC-214 "Modern Data Engineering for AI Systems", SDAIA Academy.

Everything this script emits is FULLY SYNTHETIC. No real person, driver, rider,
vehicle, plate or trip is represented. See ../README.md for the provenance note.

Design constraints (from CONVENTIONS.md):
  * stdlib only (numpy is used opportunistically for speed but is NOT required),
  * NO Faker dependency — small internal name / plate / model pools instead,
  * fully seeded and reproducible: same --seed + same args => byte-identical output,
  * schemas are canonical; columns are never invented or renamed.

Usage
-----
    python3 generate_masar.py --start 2026-06-01 --days 30 --out ../raw --scale 1.0

    # the small sample that ships with the repo
    python3 generate_masar.py --start 2026-06-01 --days 5 --out ../raw \
        --scale 0.15 --gzip-gps

Timezone policy
---------------
Masar operates in Asia/Riyadh (UTC+3). Demand curves, Friday patterns and
congestion are modelled in LOCAL time; every timestamp is STORED IN UTC.
That mismatch is deliberate — Module 3 makes participants normalise it.

Deliberate defects (all ON by default, each behind a flag)
----------------------------------------------------------
    3.1%  of completed trips get a NULL dropoff_geohash   --null-geohash-rate
    2.0%  of trip rows use DD/MM/YYYY HH:MM timestamps    --mixed-ts-rate
    ~12/day trips get a negative duration_min             --negative-duration-per-day
    0.4%  of GPS pings duplicate an event_id              --gps-dup-rate
    1.0%  of GPS pings arrive with an out-of-order ts     --gps-ooo-rate
    drivers.csv hire_date in three different formats      --hire-date-formats
Pass --clean to switch every defect off.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict

GENERATOR_VERSION = "1.0.0"
DEFAULT_SEED = 20260601

RIYADH_UTC_OFFSET_HOURS = 3

# Rows/day at scale 1.0 — pinned by CONVENTIONS.md and the Lab 1 benchmark table.
TRIPS_PER_DAY_AT_SCALE_1 = 48_200
DRIVERS_TOTAL = 3_450  # NOT scaled: the driver dimension is fixed at 3,450 rows.
PINGS_PER_COMPLETED_TRIP = 26  # ~25 pings/trip once cancellations are averaged in

# --------------------------------------------------------------------------
# Geohash (stdlib implementation — avoids a dependency on python-geohash)
# --------------------------------------------------------------------------
_B32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def geohash_encode(lat: float, lon: float, precision: int = 7) -> str:
    """Standard Gustavo Niemeyer geohash. Precision 7 ~ 150 m cell."""
    lat_lo, lat_hi = -90.0, 90.0
    lon_lo, lon_hi = -180.0, 180.0
    out: list[str] = []
    bit = 0
    ch = 0
    even = True
    while len(out) < precision:
        if even:
            mid = (lon_lo + lon_hi) / 2
            if lon > mid:
                ch = (ch << 1) | 1
                lon_lo = mid
            else:
                ch <<= 1
                lon_hi = mid
        else:
            mid = (lat_lo + lat_hi) / 2
            if lat > mid:
                ch = (ch << 1) | 1
                lat_lo = mid
            else:
                ch <<= 1
                lat_hi = mid
        even = not even
        bit += 1
        if bit == 5:
            out.append(_B32[ch])
            bit = 0
            ch = 0
    return "".join(out)


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


# --------------------------------------------------------------------------
# Reference data — real Riyadh / Jeddah / Dammam districts (Arabic + English)
# --------------------------------------------------------------------------
# (zone_name_en, zone_name_ar, district, centroid_lat, centroid_lon,
#  origin_weight, destination_weight, kind)
# kind ∈ {residential, business, mixed, airport, retail, transit}
CITY_ZONES: dict[str, list[tuple]] = {
    "RUH": [
        ("Olaya", "العليا", "Olaya", 24.6908, 46.6853, 9.0, 10.0, "business"),
        ("Al Sulaymaniyah", "السليمانية", "Olaya", 24.7020, 46.7100, 5.0, 4.5, "mixed"),
        ("Al Murabba", "المربع", "Al Murabba", 24.6560, 46.7100, 3.0, 3.5, "business"),
        ("Al Malaz", "الملز", "Al Malaz", 24.6690, 46.7400, 6.0, 5.0, "residential"),
        ("Al Batha", "البطحاء", "Al Batha", 24.6300, 46.7150, 4.5, 4.0, "retail"),
        ("Al Aqiq (KAFD)", "العقيق", "Al Aqiq", 24.7640, 46.6400, 6.5, 9.5, "business"),
        ("Al Nakheel", "النخيل", "Al Nakheel", 24.7460, 46.6320, 5.5, 5.0, "residential"),
        ("Hittin", "حطين", "Hittin", 24.7660, 46.6060, 5.0, 4.2, "residential"),
        ("Al Yasmin", "الياسمين", "Al Yasmin", 24.8250, 46.6420, 5.5, 4.0, "residential"),
        ("Al Narjis", "النرجس", "Al Narjis", 24.8560, 46.6600, 4.5, 3.2, "residential"),
        ("Al Sahafah", "الصحافة", "Al Sahafah", 24.8090, 46.6420, 4.8, 4.0, "residential"),
        ("Al Wurud", "الورود", "Al Wurud", 24.7130, 46.6660, 4.0, 4.0, "mixed"),
        ("Al Izdihar", "الازدهار", "Al Izdihar", 24.7660, 46.7300, 3.8, 3.2, "residential"),
        ("Qurtubah", "قرطبة", "Qurtubah", 24.8020, 46.7580, 4.2, 3.4, "residential"),
        ("Al Rawdah", "الروضة", "Al Rawdah", 24.7480, 46.7830, 4.0, 3.4, "residential"),
        ("Al Muruj", "المروج", "Al Muruj", 24.7350, 46.6580, 3.6, 3.4, "residential"),
        ("Al Hamra", "الحمراء", "Al Hamra", 24.7770, 46.7930, 3.0, 2.6, "residential"),
        ("Al Shifa", "الشفا", "Al Shifa", 24.5600, 46.7250, 3.4, 2.6, "residential"),
        ("Diriyah", "الدرعية", "Diriyah", 24.7370, 46.5760, 2.4, 4.2, "retail"),
        ("King Khalid International Airport", "مطار الملك خالد الدولي",
         "Airport", 24.9578, 46.6989, 4.5, 6.0, "airport"),
        ("Riyadh Metro - Al Bujairi", "محطة البجيري", "Diriyah", 24.7330, 46.5820, 1.8, 2.0, "transit"),
    ],
    "JED": [
        ("Al Hamra", "الحمراء", "Al Hamra", 21.5290, 39.1650, 6.5, 7.0, "business"),
        ("Al Rawdah", "الروضة", "Al Rawdah", 21.5720, 39.1550, 6.0, 5.4, "residential"),
        ("Al Shatie", "الشاطئ", "Al Shatie", 21.6420, 39.1080, 5.0, 5.6, "mixed"),
        ("Al Salamah", "السلامة", "Al Salamah", 21.5980, 39.1620, 5.4, 4.8, "residential"),
        ("Al Zahra", "الزهراء", "Al Zahra", 21.5560, 39.1720, 4.6, 4.2, "residential"),
        ("Al Naeem", "النعيم", "Al Naeem", 21.6120, 39.1420, 4.0, 3.6, "residential"),
        ("Al Balad", "البلد", "Al Balad", 21.4830, 39.1870, 4.2, 5.0, "retail"),
        ("Al Andalus", "الأندلس", "Al Andalus", 21.5390, 39.1900, 4.4, 4.0, "mixed"),
        ("Al Faisaliyah", "الفيصلية", "Al Faisaliyah", 21.5120, 39.1830, 3.6, 3.2, "residential"),
        ("Al Aziziyah", "العزيزية", "Al Aziziyah", 21.5000, 39.2100, 4.0, 3.6, "residential"),
        ("Obhur Al Shamaliyah", "أبحر الشمالية", "Obhur", 21.7350, 39.0900, 3.4, 4.4, "residential"),
        ("Al Khalidiyah", "الخالدية", "Al Khalidiyah", 21.5860, 39.1400, 3.8, 3.4, "residential"),
        ("Al Murjan", "المرجان", "Al Murjan", 21.6690, 39.1030, 3.0, 3.4, "residential"),
        ("Al Basateen", "البساتين", "Al Basateen", 21.6200, 39.1230, 3.2, 2.8, "residential"),
        ("King Abdulaziz International Airport", "مطار الملك عبدالعزيز الدولي",
         "Airport", 21.6796, 39.1565, 4.8, 6.2, "airport"),
    ],
    "DMM": [
        ("Al Faisaliyah", "الفيصلية", "Al Faisaliyah", 26.3830, 50.1560, 5.0, 4.6, "residential"),
        ("Al Shatea", "الشاطئ", "Al Shatea", 26.4560, 50.1030, 4.6, 5.0, "mixed"),
        ("Uhud", "أحد", "Uhud", 26.4040, 50.1250, 4.0, 3.6, "residential"),
        ("Al Adamah", "العدامة", "Al Adamah", 26.4290, 50.1000, 4.2, 4.0, "retail"),
        ("Al Mazruiyah", "المزروعية", "Al Mazruiyah", 26.4230, 50.0910, 3.6, 3.4, "residential"),
        ("Al Muntazah", "المنتزه", "Al Muntazah", 26.4400, 50.1130, 3.8, 4.2, "mixed"),
        ("Badr", "بدر", "Badr", 26.3520, 50.1420, 3.2, 2.8, "residential"),
        ("Al Rakah", "الراكة", "Al Rakah", 26.3220, 50.1930, 4.0, 4.4, "residential"),
        ("Al Anud", "العنود", "Al Anud", 26.4130, 50.1330, 3.4, 3.0, "residential"),
        ("Al Jalawiyah", "الجلوية", "Al Jalawiyah", 26.4180, 50.1060, 3.0, 2.8, "residential"),
        ("Al Nakheel", "النخيل", "Al Nakheel", 26.3690, 50.1830, 3.4, 3.2, "residential"),
        ("King Fahd International Airport", "مطار الملك فهد الدولي",
         "Airport", 26.4712, 49.7979, 3.6, 5.0, "airport"),
    ],
}

CITY_SHARE = {"RUH": 0.52, "JED": 0.30, "DMM": 0.18}

# Fare model per city: (base_sar, per_km_sar, per_min_sar, min_fare_sar, free_flow_kmh)
CITY_FARE = {
    "RUH": (5.00, 1.80, 0.50, 12.00, 44.0),
    "JED": (5.00, 1.75, 0.48, 11.00, 40.0),
    "DMM": (4.50, 1.70, 0.45, 10.00, 46.0),
}

CITY_NAME_EN = {"RUH": "Riyadh", "JED": "Jeddah", "DMM": "Dammam"}

# --------------------------------------------------------------------------
# Internal name / plate / vehicle pools (deliberately small — no Faker)
# --------------------------------------------------------------------------
GIVEN_NAMES = [
    "Abdullah", "Mohammed", "Ahmed", "Faisal", "Khalid", "Saud", "Turki", "Nasser",
    "Omar", "Yousef", "Ibrahim", "Sultan", "Bandar", "Majed", "Rayan", "Ziyad",
    "Hassan", "Hussein", "Salman", "Fahad", "Mishal", "Waleed", "Tariq", "Anas",
    "Mansour", "Badr", "Rakan", "Saleh", "Hamad", "Adel", "Musaed", "Naif",
    "Noura", "Sara", "Maha", "Reem", "Lama", "Hessa", "Dana", "Amal",
    "Layla", "Jawaher", "Munira", "Aisha", "Fatimah", "Ghada", "Rana", "Haya",
    "Rahul", "Imran", "Zaid", "Bilal", "Usman", "Kareem", "Samir", "Nabil",
]
FAMILY_NAMES = [
    "Al Qahtani", "Al Ghamdi", "Al Otaibi", "Al Harbi", "Al Zahrani", "Al Shehri",
    "Al Dossari", "Al Mutairi", "Al Anazi", "Al Subaie", "Al Juhani", "Al Balawi",
    "Al Amri", "Al Malki", "Al Shammari", "Al Rashidi", "Al Yami", "Al Asiri",
    "Al Faifi", "Al Hakami", "Al Sulami", "Al Bishi", "Al Khalidi", "Al Nasser",
    "Al Saeed", "Al Rajhi", "Al Turki", "Al Hamdan", "Al Moqbel", "Al Suwailem",
    "Rahman", "Siddiqui", "Farooq", "Iqbal", "Chowdhury", "Hussain",
]
PLATE_LETTERS = "ABDEGHJKLNRSTUVXZ"  # KSA plate letter set (Latin transliteration)

VEHICLE_POOL = [
    # (make, model, capacity, fuel_type, weight)
    ("Toyota", "Camry", 4, "petrol", 16),
    ("Toyota", "Corolla", 4, "petrol", 12),
    ("Toyota", "Hiace", 11, "diesel", 3),
    ("Hyundai", "Sonata", 4, "petrol", 11),
    ("Hyundai", "Elantra", 4, "petrol", 9),
    ("Hyundai", "Accent", 4, "petrol", 7),
    ("Kia", "K5", 4, "petrol", 7),
    ("Kia", "Cerato", 4, "petrol", 6),
    ("Nissan", "Altima", 4, "petrol", 6),
    ("Nissan", "Sunny", 4, "petrol", 5),
    ("Chevrolet", "Malibu", 4, "petrol", 4),
    ("Honda", "Accord", 4, "petrol", 4),
    ("Lexus", "ES 300h", 4, "hybrid", 3),
    ("Toyota", "Land Cruiser", 7, "petrol", 3),
    ("GMC", "Yukon", 7, "petrol", 2),
    ("Tesla", "Model 3", 4, "electric", 1),
    ("BYD", "Han EV", 4, "electric", 1),
]

PAYMENT_TYPES = ["mada", "credit_card", "apple_pay", "stc_pay", "cash", "wallet"]
PAYMENT_TYPE_W = [0.36, 0.20, 0.14, 0.11, 0.13, 0.06]

TRIP_STATUSES = ["completed", "cancelled_rider", "cancelled_driver", "no_show"]
TRIP_STATUS_W = [0.930, 0.042, 0.019, 0.009]

WEATHER_CONDITIONS = ["clear", "cloudy", "haze", "dust", "sandstorm", "rain", "fog"]

# --------------------------------------------------------------------------
# Demand shape — LOCAL Riyadh time
# --------------------------------------------------------------------------
# Sun..Thu are the KSA working week; Fri is the main weekend day (late start,
# a post-Jumu'ah bump, and a strong evening); Sat is a softer leisure day.
_WORKDAY = [
    1.4, 0.9, 0.6, 0.5, 0.5, 0.9,   # 00-05
    2.2, 5.6, 7.4, 5.2, 4.0, 4.2,   # 06-11
    4.6, 5.0, 4.8, 4.4, 5.2, 7.6,   # 12-17
    8.4, 7.8, 6.6, 5.4, 4.2, 2.6,   # 18-23
]
_FRIDAY = [
    2.6, 1.9, 1.3, 0.8, 0.6, 0.7,   # 00-05
    0.9, 1.3, 1.8, 2.4, 3.0, 3.6,   # 06-11
    5.4, 6.8, 5.6, 4.6, 5.0, 6.4,   # 12-17
    7.6, 8.2, 7.4, 6.4, 5.2, 3.8,   # 18-23
]
_SATURDAY = [
    2.2, 1.5, 1.0, 0.7, 0.6, 0.9,
    1.8, 3.2, 4.4, 4.6, 4.6, 4.8,
    5.0, 5.2, 5.0, 4.8, 5.4, 6.8,
    7.6, 7.8, 6.8, 5.8, 4.6, 3.0,
]
# Free-flow speed multiplier by LOCAL hour (congestion).
_CONGESTION = [
    1.18, 1.20, 1.22, 1.22, 1.20, 1.12,
    0.96, 0.66, 0.60, 0.74, 0.86, 0.88,
    0.84, 0.80, 0.86, 0.88, 0.74, 0.60,
    0.58, 0.64, 0.76, 0.86, 0.98, 1.08,
]


def day_profile(local_date: dt.date) -> list[float]:
    """Python weekday(): Mon=0 .. Sun=6. Friday=4, Saturday=5."""
    wd = local_date.weekday()
    if wd == 4:
        return _FRIDAY
    if wd == 5:
        return _SATURDAY
    return _WORKDAY


def is_friday(local_date: dt.date) -> bool:
    return local_date.weekday() == 4


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def utc_from_local(local_dt: dt.datetime) -> dt.datetime:
    return local_dt - dt.timedelta(hours=RIYADH_UTC_OFFSET_HOURS)


def local_from_utc(utc_dt: dt.datetime) -> dt.datetime:
    return utc_dt + dt.timedelta(hours=RIYADH_UTC_OFFSET_HOURS)


def fmt_ts_iso(d: dt.datetime) -> str:
    """The canonical trip timestamp format: 'YYYY-MM-DD HH:MM:SS' (UTC)."""
    return d.strftime("%Y-%m-%d %H:%M:%S")


def fmt_ts_alt(d: dt.datetime) -> str:
    """The DEFECT format that appears in ~2% of trip rows: 'DD/MM/YYYY HH:MM'."""
    return d.strftime("%d/%m/%Y %H:%M")


def fmt_ts_gps(d: dt.datetime) -> str:
    """GPS event time: RFC3339 with a Z suffix."""
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def weighted_choice(rng: random.Random, items: list, weights: list[float]):
    return rng.choices(items, weights=weights, k=1)[0]


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def open_out(path: str, gz: bool):
    if gz:
        # mtime=0 and no embedded filename: the gzip header must not carry a clock,
        # or two identical runs produce different sha256s and _MANIFEST.json lies.
        raw = open(path, "wb")
        gzf = gzip.GzipFile(filename="", mode="wb", compresslevel=9, fileobj=raw, mtime=0)
        return io.TextIOWrapper(gzf, encoding="utf-8", newline="", write_through=True)
    return open(path, "w", encoding="utf-8", newline="")


# --------------------------------------------------------------------------
# Dimension builders
# --------------------------------------------------------------------------
def build_zones() -> list[dict]:
    zones: list[dict] = []
    for city, rows in CITY_ZONES.items():
        for i, (en, ar, district, lat, lon, ow, dw, kind) in enumerate(rows, start=1):
            zones.append({
                "zone_id": f"Z-{city}-{i:02d}",
                "zone_name_en": en,
                "zone_name_ar": ar,
                "city": city,
                "district": district,
                "centroid_lat": round(lat, 6),
                "centroid_lon": round(lon, 6),
                "_origin_w": ow,
                "_dest_w": dw,
                "_kind": kind,
            })
    return zones


def write_zones(zones: list[dict], out_dir: str) -> str:
    path = os.path.join(out_dir, "zones.csv")
    cols = ["zone_id", "zone_name_en", "zone_name_ar", "city", "district",
            "centroid_lat", "centroid_lon"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for z in zones:
            w.writerow([z[c] for c in cols])
    return path


def _hire_date_formats(rng: random.Random, d: dt.date, mixed: bool) -> str:
    """drivers.csv ships hire_date in THREE formats on purpose (Lab 3 cast drill)."""
    if not mixed:
        return d.strftime("%Y-%m-%d")
    r = rng.random()
    if r < 0.60:
        return d.strftime("%Y-%m-%d")          # ISO
    if r < 0.85:
        return d.strftime("%d/%m/%Y")          # European
    return d.strftime("%b %d, %Y")             # "Mar 04, 2024"


def build_drivers(rng: random.Random, n: int, mixed_dates: bool) -> list[dict]:
    drivers = []
    city_ids = list(CITY_SHARE)
    city_w = [CITY_SHARE[c] for c in city_ids]
    start_window = dt.date(2019, 1, 1)
    span_days = (dt.date(2026, 5, 20) - start_window).days
    for i in range(1, n + 1):
        city = weighted_choice(rng, city_ids, city_w)
        name = f"{rng.choice(GIVEN_NAMES)} {rng.choice(FAMILY_NAMES)}"
        # Recent hires are more common than 2019 hires -> skew toward "now".
        hire = start_window + dt.timedelta(days=int(span_days * rng.random() ** 0.6))
        rating = min(5.0, max(3.2, rng.gauss(4.72, 0.22)))
        status = weighted_choice(
            rng, ["active", "inactive", "suspended"], [0.90, 0.085, 0.015])
        seed_txt = f"masar-driver-{i:06d}"
        drivers.append({
            "driver_id": f"DRV-{i:05d}",
            "full_name_en": name,
            "city": city,
            "hire_date": _hire_date_formats(rng, hire, mixed_dates),
            "rating": round(rating, 2),
            "status": status,
            # Hashed, never reversible: synthetic identifiers only.
            "national_id_hash": hashlib.sha256((seed_txt + "-nid").encode()).hexdigest()[:32],
            "phone_hash": hashlib.sha256((seed_txt + "-tel").encode()).hexdigest()[:32],
            "_hire_date_obj": hire,
        })
    return drivers


def write_drivers(drivers: list[dict], out_dir: str) -> str:
    path = os.path.join(out_dir, "drivers.csv")
    cols = ["driver_id", "full_name_en", "city", "hire_date", "rating",
            "status", "national_id_hash", "phone_hash"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for d in drivers:
            w.writerow([d[c] for c in cols])
    return path


def build_vehicles(rng: random.Random, drivers: list[dict]) -> list[dict]:
    """One vehicle per driver plus ~12% spare fleet vehicles."""
    n = int(len(drivers) * 1.12)
    models = [(m, mo, cap, fuel) for (m, mo, cap, fuel, _w) in VEHICLE_POOL]
    weights = [w for (*_x, w) in VEHICLE_POOL]
    city_ids = list(CITY_SHARE)
    city_w = [CITY_SHARE[c] for c in city_ids]
    vehicles = []
    for i in range(1, n + 1):
        make, model, cap, fuel = weighted_choice(rng, models, weights)
        year = weighted_choice(
            rng, [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
            [0.03, 0.05, 0.08, 0.11, 0.14, 0.17, 0.19, 0.15, 0.08])
        city = drivers[i - 1]["city"] if i <= len(drivers) else weighted_choice(rng, city_ids, city_w)
        plate = (f"{rng.choice(PLATE_LETTERS)}{rng.choice(PLATE_LETTERS)}"
                 f"{rng.choice(PLATE_LETTERS)}-{rng.randrange(1000, 9999)}")
        vehicles.append({
            "vehicle_id": f"VEH-{i:05d}",
            "plate_hash": hashlib.sha256(f"masar-plate-{plate}".encode()).hexdigest()[:32],
            "make": make,
            "model": model,
            "model_year": year,
            "capacity": cap,
            "fuel_type": fuel,
            "city": city,
        })
    return vehicles


def write_vehicles(vehicles: list[dict], out_dir: str) -> str:
    path = os.path.join(out_dir, "vehicles.csv")
    cols = ["vehicle_id", "plate_hash", "make", "model", "model_year",
            "capacity", "fuel_type", "city"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for v in vehicles:
            w.writerow([v[c] for c in cols])
    return path


# --------------------------------------------------------------------------
# Weather — drives surge and (mildly) speed
# --------------------------------------------------------------------------
def build_weather(rng: random.Random, start: dt.date, days: int) -> list[dict]:
    """Hourly weather per city over [start, start+days) in LOCAL hours, stored UTC."""
    rows: list[dict] = []
    base_temp = {"RUH": 38.0, "JED": 34.0, "DMM": 37.0}
    humid_city = {"RUH": 0.0, "JED": 1.4, "DMM": 1.0}
    for city in CITY_SHARE:
        # A slow-moving "weather state" so dust events last several hours.
        state = "clear"
        state_left = 0
        for d in range(days):
            local_day = start + dt.timedelta(days=d)
            day_amp = rng.uniform(6.5, 9.5)
            day_mean = base_temp[city] + rng.gauss(0, 2.2)
            for h in range(24):
                if state_left <= 0:
                    r = rng.random()
                    if r < 0.60:
                        state, state_left = "clear", rng.randint(4, 14)
                    elif r < 0.72:
                        state, state_left = "cloudy", rng.randint(3, 8)
                    elif r < 0.84:
                        state, state_left = "haze", rng.randint(3, 9)
                    elif r < 0.925:
                        state, state_left = "dust", rng.randint(2, 7)
                    elif r < 0.960:
                        state, state_left = "sandstorm", rng.randint(1, 4)
                    elif r < 0.980:
                        state, state_left = "fog", rng.randint(1, 3)
                    else:
                        state, state_left = "rain", rng.randint(1, 4)
                state_left -= 1
                # June in KSA: hottest ~15:00 local, coolest ~05:00 local.
                temp = day_mean + day_amp * math.sin((h - 9) / 24 * 2 * math.pi) - humid_city[city]
                if state in ("dust", "sandstorm"):
                    temp += 1.5
                if state == "rain":
                    temp -= 3.5
                vis = {"clear": 10.0, "cloudy": 10.0, "haze": 6.0, "dust": 2.5,
                       "sandstorm": 0.8, "fog": 1.2, "rain": 4.0}[state]
                vis = max(0.2, vis * rng.uniform(0.75, 1.25))
                # Keep temperatures inside a plausible KSA June envelope.
                temp = max(20.0, min(48.0, temp))
                local_dt = dt.datetime.combine(local_day, dt.time(hour=h))
                rows.append({
                    "city": city,
                    "hour_ts": fmt_ts_iso(utc_from_local(local_dt)),
                    "temp_c": round(temp, 1),
                    "condition": state,
                    "visibility_km": round(min(10.0, vis), 1),
                })
    rows.sort(key=lambda r: (r["hour_ts"], r["city"]))
    return rows


def write_weather(rows: list[dict], out_dir: str) -> str:
    path = os.path.join(out_dir, "weather_hourly.csv")
    cols = ["city", "hour_ts", "temp_c", "condition", "visibility_km"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])
    return path


WEATHER_SURGE_BOOST = {
    "clear": 0.00, "cloudy": 0.02, "haze": 0.05,
    "dust": 0.18, "sandstorm": 0.42, "fog": 0.22, "rain": 0.35,
}
WEATHER_SPEED_FACTOR = {
    "clear": 1.00, "cloudy": 1.00, "haze": 0.97,
    "dust": 0.90, "sandstorm": 0.74, "fog": 0.80, "rain": 0.85,
}


# --------------------------------------------------------------------------
# Zone-to-zone flow matrix (non-uniform on purpose)
# --------------------------------------------------------------------------
def build_flow_matrix(zones: list[dict]) -> dict[str, dict]:
    """Gravity model: destination attractiveness / distance^1.35, with
    kind-specific boosts, so flows are strongly non-uniform."""
    by_city: dict[str, list[dict]] = defaultdict(list)
    for z in zones:
        by_city[z["city"]].append(z)

    flows: dict[str, dict] = {}
    for city, zs in by_city.items():
        origins = [z["zone_id"] for z in zs]
        origin_w = [z["_origin_w"] for z in zs]
        dest_w_by_origin: dict[str, list[float]] = {}
        for o in zs:
            ws = []
            for d in zs:
                if d["zone_id"] == o["zone_id"]:
                    ws.append(o["_dest_w"] * 0.08)  # intra-zone trips are rare but real
                    continue
                km = max(1.0, haversine_km(o["centroid_lat"], o["centroid_lon"],
                                           d["centroid_lat"], d["centroid_lon"]))
                w = d["_dest_w"] / (km ** 1.35)
                if d["_kind"] == "airport":
                    w *= 3.4          # airports pull hard from everywhere
                if o["_kind"] == "airport" and d["_kind"] == "residential":
                    w *= 2.2          # arrivals go home
                if o["_kind"] == "residential" and d["_kind"] == "business":
                    w *= 1.8          # commute
                if d["_kind"] == "retail":
                    w *= 1.3
                ws.append(w)
            dest_w_by_origin[o["zone_id"]] = ws
        flows[city] = {
            "zones": zs,
            "zone_ids": origins,
            "origin_w": origin_w,
            "dest_w": dest_w_by_origin,
            "by_id": {z["zone_id"]: z for z in zs},
        }
    return flows


# --------------------------------------------------------------------------
# The day generator
# --------------------------------------------------------------------------
class DayStats:
    def __init__(self) -> None:
        self.counter: Counter = Counter()

    def bump(self, key: str, n: int = 1) -> None:
        self.counter[key] += n


def jitter_point(rng: random.Random, lat: float, lon: float, km: float) -> tuple[float, float]:
    dlat = (rng.uniform(-1, 1) * km) / 110.574
    dlon = (rng.uniform(-1, 1) * km) / (111.320 * math.cos(math.radians(lat)))
    return lat + dlat, lon + dlon


def generate_day(
    day_index: int,
    local_date: dt.date,
    args,
    zones: list[dict],
    flows: dict,
    drivers: list[dict],
    vehicles: list[dict],
    weather_lookup: dict,
    stats: DayStats,
) -> dict:
    """Write trips_<date>.csv, gps/gps_<date>.ndjson[.gz] and payments_<date>.csv."""
    rng = random.Random(args.seed * 1_000_003 + day_index)

    n_trips = max(1, int(round(TRIPS_PER_DAY_AT_SCALE_1 * args.scale)))
    profile = day_profile(local_date)
    prof_sum = sum(profile)

    drivers_by_city: dict[str, list[int]] = defaultdict(list)
    for idx, d in enumerate(drivers):
        if d["status"] != "suspended":
            drivers_by_city[d["city"]].append(idx)
    vehicles_by_city: dict[str, list[int]] = defaultdict(list)
    for idx, v in enumerate(vehicles):
        vehicles_by_city[v["city"]].append(idx)

    n_riders = max(2_000, int(120_000 * args.scale))

    date_str = local_date.isoformat()
    trips_path = os.path.join(args.out, f"trips_{date_str}.csv")
    pay_path = os.path.join(args.out, f"payments_{date_str}.csv")
    gps_name = f"gps_{date_str}.ndjson" + (".gz" if args.gzip_gps else "")
    gps_path = os.path.join(args.out, "gps", gps_name)

    trip_cols = ["trip_id", "rider_id", "driver_id", "vehicle_id", "city",
                 "pickup_zone_id", "dropoff_zone_id", "pickup_ts", "dropoff_ts",
                 "distance_km", "duration_min", "fare_sar", "surge_multiplier",
                 "payment_type", "status", "dropoff_geohash"]
    pay_cols = ["payment_id", "trip_id", "amount_sar", "method", "status", "settled_ts"]

    # Rows earmarked for the "negative duration_min" defect.
    n_neg = 0
    if args.defects and args.negative_duration_per_day > 0:
        n_neg = max(3, int(round(args.negative_duration_per_day * args.scale)))
    neg_rows = set(rng.sample(range(n_trips), min(n_neg, n_trips))) if n_neg else set()

    city_ids = list(CITY_SHARE)
    city_w = [CITY_SHARE[c] for c in city_ids]

    gps_seq = 0
    trip_rows = 0
    pay_rows = 0
    gps_rows = 0

    tf = open(trips_path, "w", encoding="utf-8", newline="")
    pf = open(pay_path, "w", encoding="utf-8", newline="")
    gf = open_out(gps_path, args.gzip_gps)
    try:
        tw = csv.writer(tf)
        tw.writerow(trip_cols)
        pw = csv.writer(pf)
        pw.writerow(pay_cols)
        gbuf = io.StringIO()

        for i in range(n_trips):
            # ---- when (local hour sampled from the demand profile) -------
            r = rng.random() * prof_sum
            acc = 0.0
            hour = 23
            for h, wgt in enumerate(profile):
                acc += wgt
                if r <= acc:
                    hour = h
                    break
            local_pick = dt.datetime.combine(local_date, dt.time(hour=hour)) + \
                dt.timedelta(seconds=rng.randrange(3600))
            pickup_utc = utc_from_local(local_pick)

            # ---- where -----------------------------------------------------
            city = weighted_choice(rng, city_ids, city_w)
            fl = flows[city]
            pz_id = weighted_choice(rng, fl["zone_ids"], fl["origin_w"])
            dz_id = weighted_choice(rng, fl["zone_ids"], fl["dest_w"][pz_id])
            pz = fl["by_id"][pz_id]
            dz = fl["by_id"][dz_id]

            p_lat, p_lon = jitter_point(rng, pz["centroid_lat"], pz["centroid_lon"], 1.6)
            d_lat, d_lon = jitter_point(rng, dz["centroid_lat"], dz["centroid_lon"], 1.6)

            straight = haversine_km(p_lat, p_lon, d_lat, d_lon)
            if pz_id == dz_id:
                straight = max(0.6, rng.uniform(0.7, 3.2))
            detour = rng.uniform(1.18, 1.55)
            distance_km = round(max(0.5, straight * detour), 2)

            # ---- weather + congestion --------------------------------------
            wx = weather_lookup.get((city, local_pick.replace(minute=0, second=0)),
                                    ("clear", 10.0))
            condition, visibility = wx

            base, per_km, per_min, min_fare, free_flow = CITY_FARE[city]
            speed = free_flow * _CONGESTION[hour] * WEATHER_SPEED_FACTOR[condition]
            speed *= rng.uniform(0.88, 1.14)
            speed = max(8.0, speed)
            duration_min = round(distance_km / speed * 60.0 + rng.uniform(1.0, 4.5), 1)

            # ---- surge -----------------------------------------------------
            demand_ratio = profile[hour] / (prof_sum / 24.0)
            surge = 1.0
            if demand_ratio > 1.25:
                surge += min(0.9, (demand_ratio - 1.25) * 0.55)
            surge += WEATHER_SURGE_BOOST[condition]
            if is_friday(local_date) and 12 <= hour <= 15:
                surge += 0.12
            if pz["_kind"] == "airport":
                surge += 0.05
            surge += rng.gauss(0, 0.05)
            surge = max(1.0, min(3.0, surge))
            surge = round(round(surge * 10) / 10, 1)

            # ---- who -------------------------------------------------------
            didx = rng.choice(drivers_by_city[city])
            vidx = rng.choice(vehicles_by_city[city])
            driver_id = drivers[didx]["driver_id"]
            vehicle_id = vehicles[vidx]["vehicle_id"]
            rider_id = f"RDR-{rng.randrange(n_riders):06d}"
            trip_id = f"TRP-{local_date.strftime('%Y%m%d')}-{i:07d}"

            status = weighted_choice(rng, TRIP_STATUSES, TRIP_STATUS_W)
            payment_type = weighted_choice(rng, PAYMENT_TYPES, PAYMENT_TYPE_W)

            if status == "completed":
                fare = (base + per_km * distance_km + per_min * duration_min) * surge
                fare = round(max(min_fare, fare), 2)
                dropoff_utc = pickup_utc + dt.timedelta(minutes=duration_min)
                geohash = geohash_encode(d_lat, d_lon, 7)
                out_distance = f"{distance_km:.2f}"
                out_duration = f"{duration_min:.1f}"
                out_dropoff = fmt_ts_iso(dropoff_utc)
            else:
                # Cancelled / no-show: no dropoff happened, so the dropoff fields
                # are structurally NULL. A small cancellation fee may still apply.
                fare = round(rng.choice([0.0, 0.0, 0.0, 6.0, 8.0, 10.0]), 2)
                dropoff_utc = None
                geohash = ""
                out_distance = ""
                out_duration = ""
                out_dropoff = ""
                stats.bump("trips_non_completed")

            # ---------------- DELIBERATE DEFECTS ---------------------------
            if args.defects and status == "completed" and rng.random() < args.null_geohash_rate:
                geohash = ""
                stats.bump("defect_null_geohash_injected")

            if args.defects and i in neg_rows and status == "completed":
                out_duration = f"{-abs(duration_min):.1f}"
                stats.bump("defect_negative_duration")

            pickup_str = fmt_ts_iso(pickup_utc)
            if args.defects and rng.random() < args.mixed_ts_rate:
                pickup_str = fmt_ts_alt(pickup_utc)
                if out_dropoff:
                    out_dropoff = fmt_ts_alt(dropoff_utc)
                stats.bump("defect_mixed_timestamp_rows")
            # ---------------------------------------------------------------

            tw.writerow([trip_id, rider_id, driver_id, vehicle_id, city,
                         pz_id, dz_id, pickup_str, out_dropoff,
                         out_distance, out_duration, f"{fare:.2f}", f"{surge:.1f}",
                         payment_type, status, geohash])
            trip_rows += 1
            stats.bump(f"status_{status}")

            # ---- payments --------------------------------------------------
            if fare > 0:
                settle_base = dropoff_utc or (pickup_utc + dt.timedelta(minutes=4))
                if payment_type == "cash":
                    settled = settle_base + dt.timedelta(seconds=rng.randrange(30, 300))
                    pstatus = "settled"
                else:
                    lag = rng.choice([rng.randrange(60, 900),
                                      rng.randrange(900, 7200),
                                      rng.randrange(7200, 90000)])  # some settle next day
                    settled = settle_base + dt.timedelta(seconds=lag)
                    pstatus = weighted_choice(
                        rng, ["settled", "pending", "failed", "refunded"],
                        [0.955, 0.028, 0.011, 0.006])
                pw.writerow([
                    f"PAY-{local_date.strftime('%Y%m%d')}-{i:07d}", trip_id,
                    f"{fare:.2f}", payment_type, pstatus, fmt_ts_iso(settled),
                ])
                pay_rows += 1

            # ---- GPS pings --------------------------------------------------
            if status == "completed":
                n_pings = max(4, int(rng.gauss(PINGS_PER_COMPLETED_TRIP, 4)))
                total_min = abs(duration_min)
            else:
                n_pings = rng.randint(2, 7)
                total_min = rng.uniform(1.5, 6.0)

            prev_line_parts = []
            for k in range(n_pings):
                frac = k / max(1, n_pings - 1)
                # slight curvature so the trace is not a straight line
                bend = math.sin(frac * math.pi) * 0.004
                lat = p_lat + (d_lat - p_lat) * frac + bend * rng.uniform(-1, 1)
                lon = p_lon + (d_lon - p_lon) * frac + bend * rng.uniform(-1, 1)
                # speed profile: accelerate, cruise, decelerate; congestion-aware
                shape = math.sin(min(1.0, max(0.0, frac)) * math.pi) ** 0.55
                spd = speed * (0.35 + 0.95 * shape) * rng.uniform(0.85, 1.15)
                spd = max(0.0, min(140.0, spd))
                ts = pickup_utc + dt.timedelta(minutes=total_min * frac,
                                               seconds=rng.uniform(-6, 6))
                if args.defects and rng.random() < args.gps_ooo_rate:
                    ts -= dt.timedelta(seconds=rng.randrange(45, 900))
                    stats.bump("defect_gps_out_of_order")
                gps_seq += 1
                event_id = f"ev_{(args.seed ^ (day_index << 24) ^ (gps_seq * 2654435761)) & 0xFFFFFFFFFFFF:012x}{gps_seq & 0xFFFF:04x}"
                heading = int(rng.randrange(0, 360))
                acc = round(rng.uniform(3.0, 18.0), 1)
                line = (
                    '{"event_id":"%s","vehicle_id":"%s","driver_id":"%s","trip_id":"%s",'
                    '"ts":"%s","payload":{"lat":%.5f,"lon":%.5f,"speed_kmh":%.1f,'
                    '"heading_deg":%d,"accuracy_m":%.1f},"producer_version":"2.4.0"}'
                    % (event_id, vehicle_id, driver_id, trip_id, fmt_ts_gps(ts),
                       lat, lon, spd, heading, acc)
                )
                gbuf.write(line)
                gbuf.write("\n")
                gps_rows += 1
                prev_line_parts.append(line)

                # duplicate event_id defect: re-emit the SAME event_id verbatim
                if args.defects and rng.random() < args.gps_dup_rate:
                    gbuf.write(line)
                    gbuf.write("\n")
                    gps_rows += 1
                    stats.bump("defect_gps_duplicate_event_id")

            if gbuf.tell() > 4_000_000:
                gf.write(gbuf.getvalue())
                gbuf = io.StringIO()

        gf.write(gbuf.getvalue())
    finally:
        tf.close()
        pf.close()
        gf.close()

    return {
        "date": date_str,
        "trips_path": trips_path,
        "trips_rows": trip_rows,
        "payments_path": pay_path,
        "payments_rows": pay_rows,
        "gps_path": gps_path,
        "gps_rows": gps_rows,
    }


# --------------------------------------------------------------------------
# Manifest + summary
# --------------------------------------------------------------------------
def human_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:,.1f} {unit}" if unit != "B" else f"{n:,} B"
        n /= 1024.0
    return f"{n:.1f} GB"


def build_manifest(args, files: list[dict], stats: DayStats) -> dict:
    return {
        "generator": "generate_masar.py",
        "generator_version": GENERATOR_VERSION,
        "course": "SDA-DSC-214",
        "dataset": "Masar (مسار) synthetic mobility lakehouse — raw zone",
        "synthetic": True,
        "personal_data": "none — all identifiers are synthetic or hashed",
        "seed": args.seed,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "args": {
            "start": args.start, "days": args.days, "scale": args.scale,
            "out": os.path.normpath(args.out), "gzip_gps": bool(args.gzip_gps),
            "defects": bool(args.defects),
            "null_geohash_rate": args.null_geohash_rate,
            "mixed_ts_rate": args.mixed_ts_rate,
            "gps_dup_rate": args.gps_dup_rate,
            "gps_ooo_rate": args.gps_ooo_rate,
            "negative_duration_per_day": args.negative_duration_per_day,
            "hire_date_formats": bool(args.hire_date_formats),
        },
        "timezone": {"business": "Asia/Riyadh (UTC+3)", "stored": "UTC"},
        "currency": "SAR",
        "documented_defect_rates": {
            "trips.dropoff_geohash_null_rate_of_completed": args.null_geohash_rate,
            "trips.mixed_timestamp_format_rate": args.mixed_ts_rate,
            "trips.negative_duration_rows_per_day_at_scale_1": args.negative_duration_per_day,
            "gps.duplicate_event_id_rate": args.gps_dup_rate,
            "gps.out_of_order_ts_rate": args.gps_ooo_rate,
            "drivers.hire_date_formats": 3 if args.hire_date_formats else 1,
        },
        "observed_defect_counts": dict(sorted(stats.counter.items())),
        "files": files,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Generate the synthetic Masar raw zone (SDA-DSC-214).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--start", default="2026-06-01", help="first LOCAL (Asia/Riyadh) date")
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--out", default="../raw")
    p.add_argument("--scale", type=float, default=1.0,
                   help="1.0 => ~48,200 trips/day; 0.15 => the shipped sample")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--gzip-gps", action="store_true",
                   help="write gps/*.ndjson.gz instead of *.ndjson (used for the shipped sample)")

    d = p.add_argument_group("deliberate defects")
    d.add_argument("--clean", action="store_true", help="turn EVERY deliberate defect off")
    d.add_argument("--null-geohash-rate", type=float, default=0.031)
    d.add_argument("--mixed-ts-rate", type=float, default=0.020)
    d.add_argument("--negative-duration-per-day", type=int, default=12)
    d.add_argument("--gps-dup-rate", type=float, default=0.004)
    d.add_argument("--gps-ooo-rate", type=float, default=0.010)
    d.add_argument("--no-hire-date-formats", dest="hire_date_formats",
                   action="store_false", default=True,
                   help="emit drivers.hire_date in ISO only")

    args = p.parse_args(argv)
    args.defects = not args.clean
    if args.clean:
        args.hire_date_formats = False

    start = dt.date.fromisoformat(args.start)
    os.makedirs(args.out, exist_ok=True)
    os.makedirs(os.path.join(args.out, "gps"), exist_ok=True)

    stats = DayStats()
    dim_rng = random.Random(args.seed)

    print(f"Masar generator v{GENERATOR_VERSION}  seed={args.seed}  scale={args.scale}  "
          f"days={args.days}  start={args.start}", file=sys.stderr)

    zones = build_zones()
    drivers = build_drivers(dim_rng, DRIVERS_TOTAL, args.hire_date_formats)
    vehicles = build_vehicles(dim_rng, drivers)
    weather = build_weather(dim_rng, start, args.days)

    zones_path = write_zones(zones, args.out)
    drivers_path = write_drivers(drivers, args.out)
    vehicles_path = write_vehicles(vehicles, args.out)
    weather_path = write_weather(weather, args.out)

    if args.hire_date_formats:
        fmt_counter: Counter = Counter()
        for dr in drivers:
            hd = dr["hire_date"]
            if "/" in hd:
                fmt_counter["DD/MM/YYYY"] += 1
            elif "," in hd:
                fmt_counter["Mon DD, YYYY"] += 1
            else:
                fmt_counter["YYYY-MM-DD"] += 1
        for k, v in fmt_counter.items():
            stats.bump(f"drivers_hire_date_{k}", v)

    weather_lookup = {}
    for row in weather:
        utc_dt = dt.datetime.strptime(row["hour_ts"], "%Y-%m-%d %H:%M:%S")
        weather_lookup[(row["city"], local_from_utc(utc_dt))] = (
            row["condition"], row["visibility_km"])

    flows = build_flow_matrix(zones)

    files: list[dict] = []

    def record(path: str, rows: int, kind: str) -> None:
        files.append({
            "path": os.path.relpath(path, args.out).replace(os.sep, "/"),
            "kind": kind,
            "rows": rows,
            "bytes": os.path.getsize(path),
            "sha256": sha256_of(path),
        })

    record(zones_path, len(zones), "dimension")
    record(drivers_path, len(drivers), "dimension")
    record(vehicles_path, len(vehicles), "dimension")
    record(weather_path, len(weather), "reference")

    for i in range(args.days):
        local_date = start + dt.timedelta(days=i)
        res = generate_day(i, local_date, args, zones, flows, drivers, vehicles,
                           weather_lookup, stats)
        record(res["trips_path"], res["trips_rows"], "fact_trips")
        record(res["gps_path"], res["gps_rows"], "fact_gps")
        record(res["payments_path"], res["payments_rows"], "fact_payments")
        print(f"  {local_date}  trips={res['trips_rows']:>8,}  "
              f"gps={res['gps_rows']:>9,}  payments={res['payments_rows']:>8,}",
              file=sys.stderr)

    manifest = build_manifest(args, files, stats)
    manifest_path = os.path.join(args.out, "_MANIFEST.json")
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    # ---------------- summary table ------------------------------------
    total_bytes = sum(f["bytes"] for f in files)
    total_rows = sum(f["rows"] for f in files)
    print()
    print("=" * 86)
    print(f"MASAR RAW ZONE WRITTEN -> {os.path.abspath(args.out)}")
    print("=" * 86)
    print(f"{'file':<42}{'kind':<16}{'rows':>12}{'size':>14}")
    print("-" * 86)
    for f in files:
        print(f"{f['path']:<42}{f['kind']:<16}{f['rows']:>12,}{human_bytes(f['bytes']):>14}")
    print("-" * 86)
    print(f"{'TOTAL':<42}{len(files):<16}{total_rows:>12,}{human_bytes(total_bytes):>14}")
    print()
    print("DELIBERATE DEFECTS (documented -> observed)")
    print("-" * 86)
    trips_total = sum(f["rows"] for f in files if f["kind"] == "fact_trips")
    gps_total = sum(f["rows"] for f in files if f["kind"] == "fact_gps")
    completed = stats.counter.get("status_completed", 0)

    def pct(n: int, d: int) -> str:
        return f"{(100.0 * n / d):.3f}%" if d else "n/a"

    rows = [
        ("trips.dropoff_geohash NULL (injected, of completed)",
         f"{args.null_geohash_rate:.3%}",
         pct(stats.counter.get("defect_null_geohash_injected", 0), completed)),
        ("trips mixed timestamp format (of all rows)",
         f"{args.mixed_ts_rate:.3%}",
         pct(stats.counter.get("defect_mixed_timestamp_rows", 0), trips_total)),
        ("trips negative duration_min (count)",
         f"~{args.negative_duration_per_day}/day @scale1",
         f"{stats.counter.get('defect_negative_duration', 0):,} rows"),
        ("gps duplicate event_id (of all pings)",
         f"{args.gps_dup_rate:.3%}",
         pct(stats.counter.get("defect_gps_duplicate_event_id", 0), gps_total)),
        ("gps out-of-order ts (of all pings)",
         f"{args.gps_ooo_rate:.3%}",
         pct(stats.counter.get("defect_gps_out_of_order", 0), gps_total)),
        ("drivers.hire_date distinct formats", "3",
         str(sum(1 for k in stats.counter if k.startswith("drivers_hire_date_")))),
    ]
    print(f"{'defect':<52}{'documented':>16}{'observed':>18}")
    for name, doc, obs in rows:
        print(f"{name:<52}{doc:>16}{obs:>18}")
    print("-" * 86)
    print("STRUCTURAL NULLS (not defects): cancelled_rider / cancelled_driver / no_show")
    print(f"  rows carry NULL dropoff_ts, distance_km, duration_min, dropoff_geohash: "
          f"{stats.counter.get('trips_non_completed', 0):,} "
          f"({pct(stats.counter.get('trips_non_completed', 0), trips_total)})")
    print(f"  => OVERALL dropoff_geohash null rate = "
          f"{pct(stats.counter.get('trips_non_completed', 0) + stats.counter.get('defect_null_geohash_injected', 0), trips_total)}")
    print("-" * 86)
    print(f"manifest: {manifest_path}")
    print("verify a regeneration with:  python3 -c \"import json,hashlib,sys;...\"  "
          "or ../README.md#verifying-a-regeneration")
    print("=" * 86)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
