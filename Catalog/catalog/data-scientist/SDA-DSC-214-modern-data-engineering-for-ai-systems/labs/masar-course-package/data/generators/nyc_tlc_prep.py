#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nyc_tlc_prep.py — OPTIONAL real-world benchmark dataset for SDA-DSC-214.

Downloads one month of **NYC TLC yellow-taxi** trip records and maps them onto
the canonical Masar `trips` schema, writing `../raw_nyc/`. Nothing in the course
*requires* it — the labs run entirely on the synthetic Masar data — but it gives
participants a large, genuinely messy, publicly documented dataset to benchmark
against, and it is the dataset a lot of the reference material assumes.

    python3 nyc_tlc_prep.py --month 2024-01 --out ../raw_nyc
    python3 nyc_tlc_prep.py --month 2024-01 --limit 200000        # a smaller slice
    python3 nyc_tlc_prep.py --month 2024-01 --format parquet      # keep it columnar
    python3 nyc_tlc_prep.py --months 2023-11,2023-12,2024-01      # a schema-drift set

Why NYC TLC?
------------
It is the benchmark dataset used by the **DataTalksClub Data Engineering
Zoomcamp** — and it earns that place for reasons that matter to this course:

* **It is large.** ~3 million yellow-taxi trips *per month*, ~40 GB across the
  full history. Big enough that partitioning, file sizing, predicate pushdown
  and data skipping stop being theoretical (Module 2) and start being the
  difference between a 4-second and a 4-minute query.
* **It is messy.** Real production mess, not injected mess: negative
  `total_amount` on disputed fares, zero-distance trips, passenger counts of 0
  and of 9, pickup timestamps outside the file's own month, `store_and_fwd_flag`
  values that arrive as `Y`/`N`/null, and location IDs that reference retired
  zones. Every quality check in Module 6 finds real work to do here.
* **It has had real schema changes.** The TLC has changed the feed more than
  once, in exactly the ways this course teaches you to survive:
    - **2016-07**: precise `pickup_longitude`/`pickup_latitude` columns were
      REPLACED by `PULocationID`/`DOLocationID` zone references — a privacy-driven
      change that silently broke every geospatial pipeline built on the old columns.
      (Compare Module 6's data-minimisation discussion: dropping precise location
      is exactly what PDPL asks of Masar.)
    - **2019 → 2021**: `congestion_surcharge`, then `airport_fee`, were added
      mid-stream; older files simply do not have the column.
    - **2022-05**: the distribution format moved from CSV to **Parquet**, and
      column *types* moved with it (`int64` vs `float64` for `passenger_count`,
      `VendorID`), so a naive `spark.read.parquet("*.parquet")` across a
      multi-year range hits `Parquet column cannot be converted` errors.
    - The column naming is itself inconsistent: `VendorID` and `RatecodeID`
      (PascalCase) sit next to `tpep_pickup_datetime` and `trip_distance`.
  That is the whole "schema evolution is a runtime problem, not a design
  problem" lesson, in a dataset nobody synthesised.

Official source
---------------
Landing page:
    https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
File URL pattern (CloudFront, the official distribution endpoint):
    https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{YYYY}-{MM}.parquet
    https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{YYYY}-{MM}.parquet
    https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_{YYYY}-{MM}.parquet
Zone lookup (LocationID -> borough/zone name):
    https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

Licence / terms: the TLC publishes these as public trip records for open use;
they contain **no rider identifiers** and, since 2016-07, no precise coordinates.
Cite the TLC landing page above in anything you publish.

Offline behaviour
-----------------
Lab machines in a classroom often have no egress. This script **degrades
gracefully**: it reports exactly which URL it wanted, how to fetch it by hand,
and where to drop the file so a re-run finds it locally. It never fails silently
and it never blocks a lab.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import socket
import sys
import urllib.error
import urllib.request

CLOUDFRONT = "https://d37ci6vzurychx.cloudfront.net"
TRIP_URL = CLOUDFRONT + "/trip-data/{service}_tripdata_{month}.parquet"
ZONE_URL = CLOUDFRONT + "/misc/taxi_zone_lookup.csv"
LANDING_PAGE = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

MASAR_TRIP_COLS = ["trip_id", "rider_id", "driver_id", "vehicle_id", "city",
                   "pickup_zone_id", "dropoff_zone_id", "pickup_ts", "dropoff_ts",
                   "distance_km", "duration_min", "fare_sar", "surge_multiplier",
                   "payment_type", "status", "dropoff_geohash"]

MILES_TO_KM = 1.609344
# Illustrative, fixed conversion so the benchmark is reproducible. This is a
# teaching constant, NOT a market rate — the point is unit discipline, which is
# the same lesson as the speed_kmh incident.
USD_TO_SAR = 3.75

# TLC payment_type is an integer code; this is the documented mapping.
TLC_PAYMENT = {1: "credit_card", 2: "cash", 3: "no_charge", 4: "dispute",
               5: "unknown", 6: "voided"}
MASAR_PAYMENT = {"credit_card": "credit_card", "cash": "cash",
                 "no_charge": "wallet", "dispute": "credit_card",
                 "unknown": "wallet", "voided": "wallet"}


# --------------------------------------------------------------------------
def offline_notice(url: str, dest: str, reason: str) -> None:
    print("", file=sys.stderr)
    print("=" * 78, file=sys.stderr)
    print("NYC TLC DOWNLOAD UNAVAILABLE — this is OPTIONAL, the course continues.",
          file=sys.stderr)
    print("=" * 78, file=sys.stderr)
    print(f"  reason : {reason}", file=sys.stderr)
    print(f"  wanted : {url}", file=sys.stderr)
    print(f"  save to: {os.path.abspath(dest)}", file=sys.stderr)
    print("", file=sys.stderr)
    print("  On a machine with internet, fetch it and copy it across:", file=sys.stderr)
    print(f"      curl -L -o {os.path.basename(dest)} '{url}'", file=sys.stderr)
    print("  then re-run this script; it will find the local file and skip the download.",
          file=sys.stderr)
    print("", file=sys.stderr)
    print(f"  Landing page: {LANDING_PAGE}", file=sys.stderr)
    print("", file=sys.stderr)
    print("  NOTE: every SDA-DSC-214 lab runs on the synthetic Masar data in", file=sys.stderr)
    print("        ../raw and ../fixtures. NYC TLC is a benchmark only.", file=sys.stderr)
    print("=" * 78, file=sys.stderr)


def download(url: str, dest: str, timeout: int = 60) -> bool:
    """True if `dest` exists afterwards. Never raises for a network problem."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"[cache] {dest} already present ({os.path.getsize(dest) / 1e6:,.1f} MB)",
              file=sys.stderr)
        return True
    os.makedirs(os.path.dirname(os.path.abspath(dest)) or ".", exist_ok=True)
    tmp = dest + ".part"
    try:
        print(f"[get  ] {url}", file=sys.stderr)
        req = urllib.request.Request(url, headers={"User-Agent": "SDA-DSC-214/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp, open(tmp, "wb") as fh:
            total = int(resp.headers.get("Content-Length") or 0)
            got = 0
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                fh.write(chunk)
                got += len(chunk)
                if total:
                    print(f"\r[get  ] {got / 1e6:,.0f} / {total / 1e6:,.0f} MB",
                          end="", file=sys.stderr)
        print("", file=sys.stderr)
        shutil.move(tmp, dest)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, socket.timeout,
            TimeoutError, ConnectionError, OSError) as exc:
        if os.path.exists(tmp):
            os.remove(tmp)
        offline_notice(url, dest, f"{type(exc).__name__}: {exc}")
        return False


# --------------------------------------------------------------------------
def map_to_masar(df, month: str, limit: int):
    """Map TLC yellow-taxi columns onto the canonical Masar `trips` schema.

    The mapping is lossy and deliberately explicit — write down what you cannot
    map. Half the value of this exercise is discovering that a "trip" in one
    system is not a "trip" in another.
    """
    import numpy as np
    import pandas as pd

    if limit:
        df = df.head(limit).copy()
    else:
        df = df.copy()

    # Column names have drifted over the years; normalise the two known spellings.
    ren = {}
    for a, b in (("tpep_pickup_datetime", "pickup"), ("tpep_dropoff_datetime", "dropoff"),
                 ("lpep_pickup_datetime", "pickup"), ("lpep_dropoff_datetime", "dropoff"),
                 ("pickup_datetime", "pickup"), ("dropoff_datetime", "dropoff")):
        if a in df.columns:
            ren[a] = b
    df = df.rename(columns=ren)
    if "pickup" not in df.columns or "dropoff" not in df.columns:
        raise SystemExit(f"ERROR: cannot find pickup/dropoff datetime columns in "
                         f"{list(df.columns)[:12]}… — the TLC schema changed again. "
                         f"That is the lesson; extend the mapping above.")

    pickup = pd.to_datetime(df["pickup"], errors="coerce")
    dropoff = pd.to_datetime(df["dropoff"], errors="coerce")
    duration_min = (dropoff - pickup).dt.total_seconds() / 60.0

    dist_mi = pd.to_numeric(df.get("trip_distance"), errors="coerce")
    total = pd.to_numeric(df.get("total_amount"), errors="coerce")
    fare = pd.to_numeric(df.get("fare_amount"), errors="coerce")

    pu = pd.to_numeric(df.get("PULocationID", df.get("pulocationid")), errors="coerce")
    do = pd.to_numeric(df.get("DOLocationID", df.get("dolocationid")), errors="coerce")

    pay_code = pd.to_numeric(df.get("payment_type"), errors="coerce").fillna(5).astype(int)
    pay = pay_code.map(lambda c: MASAR_PAYMENT.get(TLC_PAYMENT.get(c, "unknown"), "wallet"))

    # TLC has no rider identity at all (that is the privacy design) and no driver
    # or vehicle identity in the public feed. We keep those columns present but
    # NULL rather than fabricating them: a NULL you can explain beats a value you
    # cannot. Document this in the lineage notes.
    n = len(df)
    out = pd.DataFrame({
        "trip_id": [f"NYC-{month.replace('-', '')}-{i:08d}" for i in range(n)],
        "rider_id": pd.Series([None] * n, dtype="object"),
        "driver_id": pd.Series([None] * n, dtype="object"),
        "vehicle_id": df.get("VendorID", pd.Series([None] * n)).map(
            lambda v: f"NYCVEN-{int(v):02d}" if pd.notna(v) else None),
        "city": "NYC",
        "pickup_zone_id": pu.map(lambda v: f"Z-NYC-{int(v):03d}" if pd.notna(v) else None),
        "dropoff_zone_id": do.map(lambda v: f"Z-NYC-{int(v):03d}" if pd.notna(v) else None),
        "pickup_ts": pickup.dt.strftime("%Y-%m-%d %H:%M:%S"),
        "dropoff_ts": dropoff.dt.strftime("%Y-%m-%d %H:%M:%S"),
        "distance_km": (dist_mi * MILES_TO_KM).round(2),
        "duration_min": duration_min.round(1),
        "fare_sar": (total.fillna(fare) * USD_TO_SAR).round(2),
        # TLC has no surge column; the closest analogue is the RatecodeID==5
        # "negotiated fare". Anything else is 1.0 — an honest NULL-equivalent.
        "surge_multiplier": np.where(
            pd.to_numeric(df.get("RatecodeID"), errors="coerce") == 5, 1.5, 1.0),
        "payment_type": pay,
        # TLC records no cancellations at all: only completed trips are published.
        # A zero-distance, zero-duration row is the closest thing to a no-show.
        "status": np.where((dist_mi.fillna(0) <= 0) & (duration_min.fillna(0) <= 1),
                           "no_show", "completed"),
        # No coordinates since 2016-07 -> no geohash is derivable. NULL, and say why.
        "dropoff_geohash": pd.Series([None] * n, dtype="object"),
    })
    return out[MASAR_TRIP_COLS], {
        "rows": int(n),
        "negative_total_amount": int((total < 0).sum()),
        "zero_distance": int((dist_mi <= 0).sum()),
        "null_pu_location": int(pu.isna().sum()),
        "duration_le_zero": int((duration_min <= 0).sum()),
        "pickup_outside_month": int((pickup.dt.strftime("%Y-%m") != month).sum()),
        "passenger_count_zero": int(
            (pd.to_numeric(df.get("passenger_count"), errors="coerce") == 0).sum())
        if "passenger_count" in df.columns else None,
        "columns_present": list(df.columns),
    }


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Fetch NYC TLC trip records and map them onto the Masar schema.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Official source: {LANDING_PAGE}")
    p.add_argument("--month", default="2024-01", help="YYYY-MM")
    p.add_argument("--months", default=None,
                   help="comma-separated YYYY-MM list; overrides --month. Use a range "
                        "that spans 2022-05 or 2016-07 to see a real schema change.")
    p.add_argument("--service", default="yellow", choices=["yellow", "green", "fhvhv"])
    p.add_argument("--out", default="../raw_nyc")
    p.add_argument("--cache", default="../raw_nyc/_download_cache")
    p.add_argument("--limit", type=int, default=0, help="rows to keep per month (0 = all)")
    p.add_argument("--format", default="csv", choices=["csv", "parquet"],
                   help="output format for the mapped Masar-shaped file")
    p.add_argument("--keep-raw", action="store_true",
                   help="keep the downloaded TLC parquet in --cache (default: keep)")
    p.add_argument("--timeout", type=int, default=90)
    args = p.parse_args(argv)

    months = [m.strip() for m in (args.months or args.month).split(",") if m.strip()]
    for m in months:
        try:
            dt.datetime.strptime(m, "%Y-%m")
        except ValueError:
            raise SystemExit(f"ERROR: --month/--months must be YYYY-MM, got '{m}'")

    os.makedirs(args.out, exist_ok=True)
    os.makedirs(args.cache, exist_ok=True)

    # pandas + a parquet engine are only needed once a file is actually on disk.
    try:
        import pandas as pd  # noqa: F401
    except ImportError:
        print("ERROR: pandas is required to map TLC data "
              "(pip install pandas pyarrow). The download step alone still works.",
              file=sys.stderr)
        return 3

    downloaded, mapped, failed = [], [], []
    report = {"source": LANDING_PAGE, "url_pattern": TRIP_URL,
              "usd_to_sar_teaching_constant": USD_TO_SAR,
              "miles_to_km": MILES_TO_KM, "months": {}}

    # The zone lookup is small and makes PULocationID readable.
    zone_dest = os.path.join(args.cache, "taxi_zone_lookup.csv")
    if download(ZONE_URL, zone_dest, args.timeout):
        shutil.copy(zone_dest, os.path.join(args.out, "zones_nyc.csv"))

    for month in months:
        url = TRIP_URL.format(service=args.service, month=month)
        dest = os.path.join(args.cache, f"{args.service}_tripdata_{month}.parquet")
        if not download(url, dest, args.timeout):
            failed.append(month)
            continue
        downloaded.append(dest)

        import pandas as pd
        try:
            df = pd.read_parquet(dest)
        except ImportError:
            print("ERROR: reading Parquet needs a parquet engine: "
                  "pip install pyarrow  (or fastparquet)", file=sys.stderr)
            print(f"       the raw file is downloaded and kept at {dest}", file=sys.stderr)
            return 4
        except Exception as exc:
            print(f"ERROR: could not read {dest}: {type(exc).__name__}: {exc}",
                  file=sys.stderr)
            failed.append(month)
            continue

        masar_df, profile = map_to_masar(df, month, args.limit)
        report["months"][month] = profile

        if args.format == "parquet":
            out_path = os.path.join(args.out, f"trips_nyc_{month}.parquet")
            masar_df.to_parquet(out_path, index=False)
        else:
            out_path = os.path.join(args.out, f"trips_nyc_{month}.csv")
            masar_df.to_csv(out_path, index=False)
        mapped.append(out_path)

        print(f"[map  ] {month}: {profile['rows']:,} rows -> {out_path}", file=sys.stderr)
        print(f"         real mess found: negative total_amount={profile['negative_total_amount']:,}"
              f"  zero_distance={profile['zero_distance']:,}"
              f"  duration<=0={profile['duration_le_zero']:,}"
              f"  pickup outside {month}={profile['pickup_outside_month']:,}",
              file=sys.stderr)
        if not args.keep_raw:
            pass  # cache is kept by default; --keep-raw is accepted for symmetry

    if mapped:
        with open(os.path.join(args.out, "_NYC_PROFILE.json"), "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2)
            fh.write("\n")
        with open(os.path.join(args.out, "README.md"), "w", encoding="utf-8") as fh:
            fh.write(f"""# NYC TLC benchmark (optional) — SDA-DSC-214

Mapped onto the canonical Masar `trips` schema by `generators/nyc_tlc_prep.py`.

* Source: {LANDING_PAGE}
* URL pattern: `{TRIP_URL}`
* Months here: {", ".join(sorted(report["months"]))}
* Currency: `fare_sar` = `total_amount` USD x {USD_TO_SAR} (a fixed **teaching
  constant**, not a market rate — see the module on unit discipline).
* Distance: miles x {MILES_TO_KM} = km.

## What is deliberately NULL

| Masar column | why it is NULL for TLC |
|---|---|
| `rider_id` | the TLC feed carries no rider identity at all — by design |
| `driver_id` | not published in the yellow-taxi feed |
| `dropoff_geohash` | precise coordinates were **removed from the feed in 2016-07** and replaced by `PULocationID`/`DOLocationID` |

A NULL you can explain beats a value you invented. Record this in lineage.

## Why this dataset is the benchmark

It is the dataset the DataTalksClub Data Engineering Zoomcamp is built on,
because it is large (~3M rows/month), genuinely messy (negative fares, zero-distance
trips, timestamps outside their own file's month) and has had **real schema
changes** — coordinates dropped in 2016-07, `congestion_surcharge` and
`airport_fee` added mid-stream, and CSV → Parquet with type changes in 2022-05.
Read `_NYC_PROFILE.json` for the mess counts found in the months you downloaded.

Everything in SDA-DSC-214 runs without this dataset. It is a benchmark, not a
dependency.
""")

    print("", file=sys.stderr)
    print("=" * 78, file=sys.stderr)
    print(f"NYC TLC PREP: {len(mapped)} month(s) mapped, {len(failed)} unavailable",
          file=sys.stderr)
    for m in mapped:
        print(f"  wrote  {os.path.abspath(m)}", file=sys.stderr)
    for m in failed:
        print(f"  MISSED {m}  (see the notice above for the exact URL)", file=sys.stderr)
    print("=" * 78, file=sys.stderr)
    return 0 if mapped or not months else 1


if __name__ == "__main__":
    raise SystemExit(main())
