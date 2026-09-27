#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_sample.py — prove the shipped data matches what the labs expect.

Two jobs:

1. **Manifest check** (no pandas needed) — recompute sha256 + byte size for every
   file listed in `../raw/_MANIFEST.json` and confirm nothing drifted. Run this
   after regenerating at full scale to prove your regeneration is the real thing.

2. **Profile check** (needs pandas) — load the CSVs, print row counts, null rates,
   duplicate counts and the observed defect rates, and compare them against the
   rates the manifest documents.

    python3 verify_sample.py                       # both checks on ../raw + ../fixtures
    python3 verify_sample.py --manifest-only       # stdlib only, no pandas
    python3 verify_sample.py --raw ../raw --fixtures ../fixtures

Exit code 0 = everything matched; 1 = a mismatch worth looking at.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import sys
from collections import Counter

TOL = 0.25  # allowed relative deviation of an observed defect rate from the documented one


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_manifest(raw: str) -> tuple[int, int]:
    mpath = os.path.join(raw, "_MANIFEST.json")
    if not os.path.exists(mpath):
        print(f"MISSING {mpath} — run generate_masar.py first", file=sys.stderr)
        return (0, 1)
    man = json.load(open(mpath, encoding="utf-8"))
    print("=" * 84)
    print(f"MANIFEST CHECK  seed={man['seed']}  generator v{man['generator_version']}  "
          f"scale={man['args']['scale']}  days={man['args']['days']}")
    print("=" * 84)
    ok = bad = 0
    for f in man["files"]:
        p = os.path.join(raw, f["path"])
        if not os.path.exists(p):
            print(f"  MISSING  {f['path']}")
            bad += 1
            continue
        size = os.path.getsize(p)
        digest = sha256_of(p)
        if size == f["bytes"] and digest == f["sha256"]:
            ok += 1
        else:
            bad += 1
            print(f"  MISMATCH {f['path']}")
            print(f"           bytes  manifest={f['bytes']:,}  on disk={size:,}")
            print(f"           sha256 manifest={f['sha256'][:16]}…  "
                  f"on disk={digest[:16]}…")
    print(f"  {ok} file(s) match, {bad} mismatch/missing")
    return (ok, bad)


def open_ndjson(path: str):
    return gzip.open(path, "rt", encoding="utf-8") if path.endswith(".gz") \
        else open(path, "r", encoding="utf-8")


def gps_files(raw: str) -> list[str]:
    d = os.path.join(raw, "gps")
    if not os.path.isdir(d):
        return []
    return sorted(os.path.join(d, f) for f in os.listdir(d)
                  if f.endswith((".ndjson", ".ndjson.gz")))


def rate_row(label: str, documented, observed, unit="%") -> tuple[str, bool]:
    if documented is None:
        return (f"  {label:<52}{'—':>14}{observed:>16}", True)
    if isinstance(documented, float) and isinstance(observed, float):
        rel = abs(observed - documented) / documented if documented else 0.0
        good = rel <= TOL
        return (f"  {label:<52}{documented * 100:>13.3f}%{observed * 100:>15.3f}%"
                f"  {'OK' if good else 'DRIFT'}", good)
    good = str(documented) == str(observed)
    return (f"  {label:<52}{documented:>14}{observed:>16}  {'OK' if good else 'DIFF'}", good)


def profile(raw: str, fixtures: str) -> int:
    import pandas as pd

    man = json.load(open(os.path.join(raw, "_MANIFEST.json"), encoding="utf-8"))
    doc = man["documented_defect_rates"]

    trip_files = sorted(f for f in os.listdir(raw)
                        if f.startswith("trips_") and f.endswith(".csv"))
    frames = []
    for f in trip_files:
        df = pd.read_csv(os.path.join(raw, f), dtype=str, keep_default_na=False)
        df["_file"] = f
        frames.append(df)
    trips = pd.concat(frames, ignore_index=True)
    n = len(trips)

    print()
    print("=" * 84)
    print(f"TRIPS PROFILE — {len(trip_files)} file(s), {n:,} rows")
    print("=" * 84)
    print(f"  {'column':<24}{'nulls':>12}{'null %':>10}{'distinct':>12}")
    for c in trips.columns:
        if c.startswith("_"):
            continue
        nulls = int((trips[c] == "").sum())
        print(f"  {c:<24}{nulls:>12,}{100 * nulls / n:>9.3f}%{trips[c].nunique():>12,}")

    dup_trip = int(n - trips["trip_id"].nunique())
    print(f"\n  duplicate trip_id rows: {dup_trip:,}")
    print(f"  status mix: "
          + ", ".join(f"{k}={v / n:.4f}" for k, v in trips['status'].value_counts().items()))

    completed = trips[trips["status"] == "completed"]
    nc = len(completed)
    inj_null_geo = int((completed["dropoff_geohash"] == "").sum())
    mixed_ts = int(trips["pickup_ts"].str.contains("/", regex=False).sum())
    neg_dur = int(sum(1 for v in trips["duration_min"] if v and float(v) < 0))

    # ---- GPS -----------------------------------------------------------
    gfiles = gps_files(raw)
    gps_total = 0
    ids: Counter = Counter()
    ooo = 0
    versions: Counter = Counter()
    per_trip_last: dict[str, str] = {}
    speeds = []
    for p in gfiles:
        with open_ndjson(p) as fh:
            for line in fh:
                ev = json.loads(line)
                gps_total += 1
                ids[ev["event_id"]] += 1
                versions[ev["producer_version"]] += 1
                t = ev["trip_id"]
                ts = ev["ts"]
                if t in per_trip_last and ts < per_trip_last[t]:
                    ooo += 1
                per_trip_last[t] = max(ts, per_trip_last.get(t, ts))
                if len(speeds) < 400_000:
                    speeds.append(ev["payload"]["speed_kmh"])
    dup_events = sum(c - 1 for c in ids.values() if c > 1)

    print()
    print("=" * 84)
    print(f"GPS PROFILE — {len(gfiles)} file(s), {gps_total:,} pings, "
          f"{len(per_trip_last):,} distinct trips")
    print("=" * 84)
    print(f"  pings per trip (mean)      {gps_total / max(1, len(per_trip_last)):>10.2f}")
    print(f"  distinct event_id          {len(ids):>10,}")
    print(f"  duplicate event_id rows    {dup_events:>10,}")
    print(f"  out-of-order ts (per trip) {ooo:>10,}")
    print(f"  producer_version mix       "
          + ", ".join(f"{k}={v:,}" for k, v in sorted(versions.items())))
    print(f"  mean speed_kmh             {sum(speeds) / max(1, len(speeds)):>10.2f}")

    # ---- drivers -------------------------------------------------------
    drv = pd.read_csv(os.path.join(raw, "drivers.csv"), dtype=str, keep_default_na=False)
    fmts: Counter = Counter()
    for v in drv["hire_date"]:
        fmts["DD/MM/YYYY" if "/" in v else ("Mon DD, YYYY" if "," in v else "YYYY-MM-DD")] += 1
    print()
    print("=" * 84)
    print(f"DIMENSIONS")
    print("=" * 84)
    print(f"  {'drivers.csv':<20}rows={len(drv):,}  duplicate driver_id="
          f"{len(drv) - drv['driver_id'].nunique()}")
    print(f"                hire_date formats: "
          + ", ".join(f"{k}={v:,}" for k, v in sorted(fmts.items())))
    for name in ("vehicles.csv", "zones.csv", "weather_hourly.csv"):
        d = pd.read_csv(os.path.join(raw, name), dtype=str, keep_default_na=False)
        print(f"  {name:<20}rows={len(d):,}  cols={len(d.columns)}")

    pay_files = sorted(f for f in os.listdir(raw)
                       if f.startswith("payments_") and f.endswith(".csv"))
    pays = pd.concat([pd.read_csv(os.path.join(raw, f), dtype=str, keep_default_na=False)
                      for f in pay_files], ignore_index=True)
    orphan = int((~pays["trip_id"].isin(set(trips["trip_id"]))).sum())
    print(f"  {'payments_*.csv':<20}rows={len(pays):,}  duplicate payment_id="
          f"{len(pays) - pays['payment_id'].nunique()}  orphan trip_id={orphan}")

    # ---- defect-rate comparison ---------------------------------------
    print()
    print("=" * 84)
    print("DEFECT RATES — documented (manifest) vs observed (recomputed from the files)")
    print("=" * 84)
    print(f"  {'defect':<52}{'documented':>14}{'observed':>16}")
    checks = [
        rate_row("trips.dropoff_geohash NULL (of completed rows)",
                 doc["trips.dropoff_geohash_null_rate_of_completed"], inj_null_geo / nc),
        rate_row("trips mixed timestamp format (of all rows)",
                 doc["trips.mixed_timestamp_format_rate"], mixed_ts / n),
        rate_row("gps duplicate event_id (of all pings)",
                 doc["gps.duplicate_event_id_rate"], dup_events / gps_total),
        rate_row("gps out-of-order ts (of all pings)",
                 doc["gps.out_of_order_ts_rate"], ooo / gps_total),
        rate_row("drivers.hire_date distinct formats",
                 doc["drivers.hire_date_formats"], len(fmts)),
        rate_row("trips negative duration_min (absolute count)", None, f"{neg_dur:,} rows"),
        rate_row("trips duplicate trip_id in raw (absolute count)", None, f"{dup_trip:,} rows"),
    ]
    failures = 0
    for line, good in checks:
        print(line)
        if not good:
            failures += 1

    # ---- fixtures ------------------------------------------------------
    if os.path.isdir(fixtures):
        print()
        print("=" * 84)
        print("FIXTURES")
        print("=" * 84)
        fx = os.path.join(fixtures, "dirty_batch", "trips_2026-06-05_dirty.csv")
        if os.path.exists(fx):
            d = pd.read_csv(fx, dtype=str, keep_default_na=False)
            print(f"  dirty_batch      rows={len(d):,}  null trip_id="
                  f"{int((d['trip_id'] == '').sum())}  null rider_id="
                  f"{int((d['rider_id'] == '').sum())}  dup trip_id="
                  f"{int((d['trip_id'] != '').sum()) - d.loc[d['trip_id'] != '', 'trip_id'].nunique()}  "
                  f"bad city={int((~d['city'].isin(['RUH', 'JED', 'DMM'])).sum())}  "
                  f"fare<0={int(sum(1 for v in d['fare_sar'] if v and float(v) < 0))}  "
                  f"fare>2000={int(sum(1 for v in d['fare_sar'] if v and float(v) > 2000))}")
        cs = os.path.join(fixtures, "currency_shift", "trips_2026-06-05_currency_shift.csv")
        if os.path.exists(cs):
            d = pd.read_csv(cs)
            base = pd.read_csv(os.path.join(raw, "trips_2026-06-05.csv"))
            for city in ("RUH", "JED", "DMM"):
                a = base.loc[base.city == city, "fare_sar"].mean()
                b = d.loc[d.city == city, "fare_sar"].mean()
                print(f"  currency_shift   {city}: raw mean fare {a:>10.2f} -> "
                      f"fixture {b:>12.2f}   ratio {b / a:>7.2f}x")
        inc = None
        for cand in ("gps_2026-06-05_v250.ndjson.gz", "gps_2026-06-05_v250.ndjson"):
            p = os.path.join(fixtures, "incident_speed_unit", cand)
            if os.path.exists(p):
                inc = p
        if inc:
            sp, vers = [], Counter()
            with open_ndjson(inc) as fh:
                for line in fh:
                    ev = json.loads(line)
                    sp.append(ev["payload"]["speed_kmh"])
                    vers[ev["producer_version"]] += 1
            print(f"  incident v2.5.0  events={len(sp):,}  versions={dict(vers)}  "
                  f"mean speed_kmh={sum(sp) / len(sp):.2f}  "
                  f"(raw baseline {sum(speeds) / len(speeds):.2f}, "
                  f"ratio {(sum(speeds) / len(speeds)) / (sum(sp) / len(sp)):.2f}x)")
        lt = os.path.join(fixtures, "late_trips", "trips_late_2026-06-02.csv")
        if os.path.exists(lt):
            d = pd.read_csv(lt, dtype=str, keep_default_na=False)
            known = set(pd.read_csv(os.path.join(raw, "trips_2026-06-02.csv"),
                                    dtype=str)["trip_id"])
            newn = int((~d["trip_id"].isin(known)).sum())
            print(f"  late_trips       rows={len(d)}  never-seen trip_id={newn}  "
                  f"already-in-bronze={len(d) - newn}")
        er = os.path.join(fixtures, "erasure_request", "pdpl_erasure_2026-06-10.json")
        if os.path.exists(er):
            j = json.load(open(er, encoding="utf-8"))
            rid = set(j["scope"]["rider_ids"])
            actual = int(trips["rider_id"].isin(rid).sum())
            claimed = j["expected_effect"]["total_rows_to_delete_from_silver_trips"]
            ok = actual == claimed
            print(f"  erasure_request  riders={len(rid)}  rows in raw={actual}  "
                  f"claimed={claimed}  {'OK' if ok else 'MISMATCH'}")
            failures += 0 if ok else 1

    print()
    print("=" * 84)
    print("ALL DEFECT RATES WITHIN TOLERANCE" if failures == 0
          else f"{failures} CHECK(S) OUT OF TOLERANCE")
    print("=" * 84)
    return failures


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Verify the shipped Masar sample.")
    p.add_argument("--raw", default="../raw")
    p.add_argument("--fixtures", default="../fixtures")
    p.add_argument("--manifest-only", action="store_true")
    args = p.parse_args(argv)

    _, bad = check_manifest(args.raw)
    if args.manifest_only:
        return 1 if bad else 0
    try:
        import pandas  # noqa: F401
    except ImportError:
        print("\npandas not installed — manifest check only "
              "(pip install pandas to profile).", file=sys.stderr)
        return 1 if bad else 0
    fails = profile(args.raw, args.fixtures)
    return 1 if (bad or fails) else 0


if __name__ == "__main__":
    raise SystemExit(main())
