#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject_defects.py — build the TEACHING FIXTURES for SDA-DSC-214.

`generate_masar.py` writes a *plausible* raw zone with background defects.
This script writes the *staged incidents* the labs are built around: each one
is a small, self-contained batch that makes exactly one failure mode visible.

    python3 inject_defects.py --raw ../raw --out ../fixtures

Fixtures produced
-----------------
    corrections/trips_corrections_2026-06-03.csv   Lab 4  MERGE upsert source
    late_trips/trips_late_2026-06-02.csv           Lab 3  lookback-window drill
    late_pings/gps_late_2026-06-04.ndjson          Lab 5  watermark drill
    dirty_batch/trips_2026-06-05_dirty.csv         Lab 6  fail-fast vs quarantine
    currency_shift/trips_2026-06-05_currency_shift.csv
                                                   Lab 6  distribution-drift case
    erasure_request/pdpl_erasure_2026-06-10.json   Lab 4  PDPL right-to-erasure
    incident_speed_unit/gps_2026-06-05_v250.ndjson Lab 5/6/8  THE signature incident

Every folder carries a README.md: what is wrong, which lab uses it, and the
expected detection signal.

All data here is FULLY SYNTHETIC and derived from ../raw.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import hashlib
import json
import os
import random
import sys
from collections import Counter, defaultdict

FIXTURES_VERSION = "1.0.0"
DEFAULT_SEED = 20260601

TRIP_COLS = ["trip_id", "rider_id", "driver_id", "vehicle_id", "city",
             "pickup_zone_id", "dropoff_zone_id", "pickup_ts", "dropoff_ts",
             "distance_km", "duration_min", "fare_sar", "surge_multiplier",
             "payment_type", "status", "dropoff_geohash"]


# --------------------------------------------------------------------------
# IO helpers (raw GPS may be plain .ndjson or gzipped .ndjson.gz)
# --------------------------------------------------------------------------
def gps_path_for(raw: str, date_str: str) -> str:
    plain = os.path.join(raw, "gps", f"gps_{date_str}.ndjson")
    gz = plain + ".gz"
    if os.path.exists(plain):
        return plain
    if os.path.exists(gz):
        return gz
    raise FileNotFoundError(f"no GPS file for {date_str} under {os.path.join(raw, 'gps')}")


def open_ndjson(path: str):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, "r", encoding="utf-8")


def read_trips(raw: str, date_str: str) -> list[dict]:
    path = os.path.join(raw, f"trips_{date_str}.csv")
    with open(path, "r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_trips(path: str, rows: list[dict]) -> int:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=TRIP_COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return len(rows)


def write_readme(folder: str, text: str) -> None:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(text.strip() + "\n")


def fnum(x, nd=2):
    return f"{float(x):.{nd}f}"


# --------------------------------------------------------------------------
# 1. corrections/  — Lab 4 MERGE upsert source
# --------------------------------------------------------------------------
def make_corrections(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["corrections_date"]
    src = read_trips(raw, date_str)
    completed = [r for r in src if r["status"] == "completed" and r["fare_sar"]]
    picked = rng.sample(completed, 4)

    rows = []
    notes = []
    # (a) a surge dispute resolved in the rider's favour -> surge back to 1.0
    r0 = dict(picked[0])
    old = float(r0["fare_sar"])
    r0["surge_multiplier"] = "1.0"
    r0["fare_sar"] = fnum(old / max(1.0, float(picked[0]["surge_multiplier"])))
    notes.append(f"{r0['trip_id']}: surge dispute upheld, {fnum(old)} -> {r0['fare_sar']} SAR")
    rows.append(r0)

    # (b) a re-measured route: distance and duration corrected, fare re-scored
    r1 = dict(picked[1])
    old_d = float(r1["distance_km"])
    new_d = round(old_d * 0.78, 2)
    new_t = round(float(r1["duration_min"]) * 0.83, 1)
    r1["distance_km"] = fnum(new_d)
    r1["duration_min"] = fnum(new_t, 1)
    r1["fare_sar"] = fnum(max(10.0, float(r1["fare_sar"]) * 0.80))
    notes.append(f"{r1['trip_id']}: GPS route re-snapped, {old_d} -> {new_d} km, fare re-scored")
    rows.append(r1)

    # (c) a trip reclassified from completed to no_show after a support review
    r2 = dict(picked[2])
    r2["status"] = "no_show"
    r2["dropoff_ts"] = ""
    r2["distance_km"] = ""
    r2["duration_min"] = ""
    r2["dropoff_geohash"] = ""
    r2["fare_sar"] = "8.00"
    notes.append(f"{r2['trip_id']}: reclassified completed -> no_show, cancellation fee only")
    rows.append(r2)

    # (d) a payment-type correction (cash actually paid by mada)
    r3 = dict(picked[3])
    r3["payment_type"] = "mada" if r3["payment_type"] != "mada" else "credit_card"
    notes.append(f"{r3['trip_id']}: payment_type corrected to {r3['payment_type']}")
    rows.append(r3)

    # (e) a trip that NEVER reached bronze -> exercises the MERGE INSERT branch
    template = dict(rng.choice(completed))
    template["trip_id"] = f"TRP-{date_str.replace('-', '')}-9000001"
    template["fare_sar"] = fnum(float(template["fare_sar"]))
    notes.append(f"{template['trip_id']}: previously missing trip, must INSERT (not update)")
    rows.append(template)

    folder = os.path.join(out, "corrections")
    path = os.path.join(folder, f"trips_corrections_{date_str}.csv")
    n = write_trips(path, rows)

    write_readme(folder, f"""
# Fixture — `corrections/`

**File:** `trips_corrections_{date_str}.csv` ({n} rows, canonical `trips` schema)
**Used by:** Lab 4 (Delta Lake and ACID) — MERGE / upsert idempotency drill.
**Also referenced by:** Module 4 instructor demo ("upsert twice, second run updates 0 rows").

## What this is

A batch of **re-scored trips** issued by Masar's support and pricing team two days
after `{date_str}` settled. It is *not* corrupt data — it is a legitimate correction
feed, and it is the reason `silver.trips` must be an idempotent MERGE on `trip_id`
rather than an append.

| trip_id | correction |
|---|---|
""" + "\n".join(f"| `{n_.split(':')[0]}` | {n_.split(': ', 1)[1]} |" for n_ in notes) + f"""

Four rows **match** an existing `trip_id` in `bronze.trips` / `silver.trips` for
`{date_str}` and must UPDATE. One row (`TRP-{date_str.replace('-', '')}-9000001`)
does **not** exist upstream and must INSERT — so a `WHEN MATCHED` -only MERGE
silently loses it.

## Expected detection signal

* First `MERGE` run: **4 rows updated, 1 row inserted**.
* Second `MERGE` run with the same file: **0 updated, 0 inserted** — this is the
  idempotency proof. If the second run reports non-zero, the merge condition is
  not on the true key.
* `DESCRIBE HISTORY silver.trips` shows two commits; `VERSION AS OF` the first
  reproduces the pre-correction fares.
* A naive `INSERT INTO` instead of `MERGE` shows up as duplicate `trip_id`s —
  the dbt `unique` test on `trip_id` fails.

## Failure mode it teaches

> "What happens to Masar's AI system if this part of the platform fails?"
> Corrections applied by append double-count revenue and feed the ETA model two
> contradictory labels for the same trip.
""")
    return {"folder": "corrections", "rows": n, "path": path}


# --------------------------------------------------------------------------
# 2. late_trips/ — Lab 3 lookback window
# --------------------------------------------------------------------------
def make_late_trips(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["late_trips_date"]          # event date
    arrival = cfg["late_trips_arrival"]        # the day the file actually lands
    src = read_trips(raw, date_str)
    completed = [r for r in src if r["status"] == "completed"]

    rows = []
    n_new = 120
    for i in range(n_new):
        base = dict(rng.choice(completed))
        base["trip_id"] = f"TRP-{date_str.replace('-', '')}-9{i:06d}"
        base["rider_id"] = f"RDR-{rng.randrange(120_000):06d}"
        rows.append(base)

    # 6 rows that ALREADY exist upstream, byte-identical: a correct MERGE must
    # treat them as no-ops; an append duplicates them.
    dupes = rng.sample(completed, 6)
    rows.extend(dict(d) for d in dupes)
    rng.shuffle(rows)

    folder = os.path.join(out, "late_trips")
    path = os.path.join(folder, f"trips_late_{date_str}.csv")
    n = write_trips(path, rows)

    write_readme(folder, f"""
# Fixture — `late_trips/`

**File:** `trips_late_{date_str}.csv` ({n} rows, canonical `trips` schema)
**Used by:** Lab 3 (ETL vs ELT / dbt incremental) — the **lookback-window** drill.
**Also referenced by:** Module 1 "two-tier divergence" simulation, Module 3 case study.

## What this is

Trips whose `pickup_ts` falls on **{date_str}** but whose records only reached
bronze on **{arrival}** — two days late. In the real system this happens when a
payment settles after the nightly cutoff, or a driver's device syncs after a
tunnel/roaming gap.

* **{n_new} rows** carry `trip_id`s that have **never** been seen upstream
  (prefix `TRP-{date_str.replace('-', '')}-9……`). These are the genuinely missing trips.
* **6 rows** are byte-identical re-sends of `trip_id`s that are already in bronze
  for {date_str}. They exist to prove the MERGE is idempotent.

## How to use it

Land it as if it arrived on {arrival}:

```bash
cp trips_late_{date_str}.csv ../../raw/trips_{date_str}.late.csv   # or a second bronze batch
```

## Expected detection signal

| Pipeline | Result |
|---|---|
| `WHERE trip_date = current_date()` (the bug) | the {n_new} late trips are **never counted** — a silent ~2% undercount for {date_str} |
| 3-day lookback + `MERGE ON trip_id` (the fix) | {n_new} inserted, 6 matched no-ops, count for {date_str} corrects itself |
| Lookback but `INSERT INTO` instead of MERGE | 6 duplicate `trip_id`s — the dbt `unique` test fails |
| 1-day lookback | still misses everything: the file is **2 days** late — the window must exceed the observed lateness |

Verify with: `SELECT count(*) FROM silver.trips WHERE date(pickup_ts) = '{date_str}'`
before and after. The delta must be exactly **{n_new}**.

## Failure mode it teaches

A silent correctness bug. No error, no failed test, no alert — just a daily
number that is quietly low, which then trains the demand model and pays driver
incentives on an undercount.
""")
    return {"folder": "late_trips", "rows": n, "new_trip_ids": n_new, "path": path}


# --------------------------------------------------------------------------
# 3. late_pings/ — Lab 5 watermark drill
# --------------------------------------------------------------------------
def make_late_pings(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["late_pings_date"]
    src_path = gps_path_for(raw, date_str)

    # Sample from a mid-day window so "how late" is unambiguous.
    pool: list[dict] = []
    with open_ndjson(src_path) as fh:
        for i, line in enumerate(fh):
            if i % 37:
                continue
            ev = json.loads(line)
            if ev["ts"][11:13] in ("09", "10", "11", "12"):
                pool.append(ev)
            if len(pool) >= 4000:
                break

    picked = rng.sample(pool, min(500, len(pool)))
    within, beyond = 0, 0
    rows = []
    for ev in picked:
        e = json.loads(json.dumps(ev))  # deep copy
        # Within a 3-minute watermark (counted correctly) vs far beyond it (dropped).
        if rng.random() < 0.55:
            delay_s = rng.randrange(20, 170)
            within += 1
        else:
            delay_s = rng.randrange(11 * 60, 47 * 60)
            beyond += 1
        e["_note_delay_seconds"] = delay_s   # informational only; drop before Kafka if strict
        e["event_id"] = e["event_id"][:-4] + f"{rng.randrange(0x10000):04x}"
        rows.append(e)

    # ~4% duplicate event_ids inside the late batch itself
    n_dupes = max(4, int(len(rows) * 0.04))
    for e in rng.sample(rows, n_dupes):
        rows.append(json.loads(json.dumps(e)))

    # deliberately NOT sorted by ts — the batch is out of order on arrival
    rng.shuffle(rows)

    folder = os.path.join(out, "late_pings")
    path = os.path.join(folder, f"gps_late_{date_str}.ndjson")
    os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for e in rows:
            fh.write(json.dumps(e, ensure_ascii=False, separators=(",", ":")))
            fh.write("\n")

    write_readme(folder, f"""
# Fixture — `late_pings/`

**File:** `gps_late_{date_str}.ndjson` ({len(rows)} events, canonical `gps_events` schema
plus one extra informational key, see below)
**Used by:** Lab 5 (Streaming and Event-Driven Architectures) — the **watermark** drill.

## What this is

GPS pings with **event times on {date_str} that arrive after the stream has already
moved past them**. This is the normal condition for a mobility fleet: devices
lose signal in tunnels, underground parking and roaming gaps, then flush a
backlog when they reconnect.

| property | value |
|---|---|
| total events | {len(rows)} |
| late by < 3 minutes (inside a 3-min watermark) | ~{within} |
| late by 11–47 minutes (outside a 3-min watermark) | ~{beyond} |
| duplicated `event_id`s within the batch | {n_dupes} |
| ordering | **shuffled** — the file is deliberately not sorted by `ts` |

Each record carries an extra `_note_delay_seconds` key stating how late it is.
That key is **instructional metadata, not part of the contract** — strip it before
producing to Kafka (`emit_gps_stream.py --inject late` does this for you), or keep
it to grade the exercise.

## Expected detection signal

Replay `{date_str}`'s normal pings, then this file, into
`masar.gps.raw` and run the event-time windowed aggregation:

```python
.withWatermark("event_ts", "3 minutes")
.groupBy(window("event_ts", "5 minutes"), "pickup_zone_id")
```

* Events late by **< 3 min** land in their **correct** 5-minute window; the window's
  count increases after it looked final. This is the point: watermarks let late
  data still be correct.
* Events late by **> 3 min** are **dropped** — `numRowsDroppedByWatermark` in the
  streaming progress log is non-zero. Widen to `withWatermark("event_ts", "60 minutes")`
  and they reappear, at the cost of held state.
* With **no watermark at all**, nothing is dropped but state grows without bound —
  watch `stateOperators[0].numRowsTotal` climb and never fall.
* Duplicate `event_id`s prove that the watermark is about *lateness*, not
  *deduplication*: you still need `dropDuplicates(["event_id"])` (bounded by the
  same watermark) or a MERGE on `event_id`.

## Failure mode it teaches

Choosing a watermark is a trade-off, not a default. Too short silently discards
real trips' telemetry (the ETA model's speed features go stale for exactly the
vehicles that had connectivity problems); too long inflates state and delays
every downstream result.
""")
    return {"folder": "late_pings", "rows": len(rows), "within": within,
            "beyond": beyond, "dupes": n_dupes, "path": path}


# --------------------------------------------------------------------------
# 4. dirty_batch/ — Lab 6 fail-fast vs quarantine
# --------------------------------------------------------------------------
BAD_CITY_CODES = ["RIYADH", "Jeddah", "ruh", "DMM ", "XX", "", "RUH-01", "0"]


def make_dirty_batch(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["dirty_date"]
    rows = [dict(r) for r in read_trips(raw, date_str)]
    n = len(rows)
    # Only mutate rows that can carry the fault, so the counts in the README are exact.
    idx = [i for i in range(n)
           if rows[i]["status"] == "completed" and float(rows[i]["fare_sar"] or 0) > 0]
    rng.shuffle(idx)

    counts = Counter()
    cursor = 0

    def take(k: int) -> list[int]:
        nonlocal cursor
        chunk = idx[cursor:cursor + k]
        cursor += k
        if len(chunk) < k:
            raise SystemExit(f"ERROR: {date_str} has too few eligible rows "
                             f"({len(idx)}) to inject the dirty-batch faults. "
                             f"Regenerate at a larger --scale.")
        return chunk

    # (A) INTEGRITY failures -> fail-fast. 40 rows with a null primary/foreign key.
    for j, i in enumerate(take(40)):
        if j % 2 == 0:
            rows[i]["trip_id"] = ""
            counts["null_trip_id"] += 1
        else:
            rows[i]["rider_id"] = ""
            counts["null_rider_id"] += 1

    # (B) PARTIAL failures -> quarantine. 120 rows with out-of-range fares.
    for j, i in enumerate(take(120)):
        r = j % 3
        if r == 0:
            rows[i]["fare_sar"] = fnum(-abs(float(rows[i]["fare_sar"])))
            counts["negative_fare"] += 1
        elif r == 1:
            rows[i]["fare_sar"] = fnum(float(rows[i]["fare_sar"]) * 4200.0)
            counts["absurd_fare"] += 1
        else:
            rows[i]["fare_sar"] = "0.00"      # a completed trip that charged nothing
            counts["zero_fare_completed"] += 1

    # (C) REFERENTIAL / domain failures -> quarantine. 25 rows with a bad city code.
    for j, i in enumerate(take(25)):
        rows[i]["city"] = BAD_CITY_CODES[j % len(BAD_CITY_CODES)]
        counts["bad_city_code"] += 1

    # (D) 8 duplicate trip_ids -> integrity, fail-fast alongside the null keys.
    for i in take(8):
        clone = dict(rows[i])
        clone["fare_sar"] = fnum(float(clone["fare_sar"]) + 3.0)
        rows.append(clone)
        counts["duplicate_trip_id"] += 1

    # (E) 15 impossible timestamps: dropoff BEFORE pickup.
    for i in take(15):
        rows[i]["dropoff_ts"], rows[i]["pickup_ts"] = rows[i]["pickup_ts"], rows[i]["dropoff_ts"]
        counts["dropoff_before_pickup"] += 1

    rng.shuffle(rows)
    folder = os.path.join(out, "dirty_batch")
    path = os.path.join(folder, f"trips_{date_str}_dirty.csv")
    total = write_trips(path, rows)

    good = total - sum(counts.values())
    write_readme(folder, f"""
# Fixture — `dirty_batch/`

**File:** `trips_{date_str}_dirty.csv` ({total} rows, canonical `trips` schema)
**Used by:** Lab 6 (Data Quality, Observability, Governance) — the
**fail-fast vs quarantine** decision.

## What this is

One day's trips (`{date_str}`) with a mixed bag of injected faults. The mix is the
whole point: a mature quality gate does **not** apply one policy to everything.

| class | fault | rows | correct gate action |
|---|---|---|---|
| Integrity | `trip_id` is NULL | {counts['null_trip_id']} | **fail-fast — block the batch** |
| Integrity | `rider_id` is NULL | {counts['null_rider_id']} | **fail-fast — block the batch** |
| Integrity | duplicate `trip_id` | {counts['duplicate_trip_id']} | **fail-fast — block the batch** |
| Range | `fare_sar` negative | {counts['negative_fare']} | quarantine the rows, promote the rest |
| Range | `fare_sar` ~4200× too large | {counts['absurd_fare']} | quarantine the rows, promote the rest |
| Business rule | `fare_sar = 0` on a `completed` trip | {counts['zero_fare_completed']} | quarantine the rows, promote the rest |
| Domain | `city` not in {{RUH, JED, DMM}} (`RIYADH`, `ruh`, `DMM `, `XX`, empty, …) | {counts['bad_city_code']} | quarantine the rows, promote the rest |
| Temporal | `dropoff_ts` **before** `pickup_ts` | {counts['dropoff_before_pickup']} | quarantine the rows, promote the rest |
| — | clean rows | ~{good} | promote to `silver.trips` |

## Expected detection signal

Run the Great Expectations suite `quality/suites/silver_trips_suite.py` against
this file at the bronze → silver promotion point:

1. `expect_column_values_to_not_be_null("trip_id")` → **fails**, `unexpected_count = {counts['null_trip_id']}`
2. `expect_column_values_to_be_unique("trip_id")` → **fails**, `unexpected_count = {counts['duplicate_trip_id']}`
   → the gate **blocks**: 0 rows promoted, 0 quarantined, an alert is raised.
   This is the *fail-fast* branch: you cannot dedupe or repair a missing key, and a
   partially-keyed batch corrupts every downstream MERGE.
3. Fix or drop the key faults, re-run. Now only *partial* expectations fail:
   `expect_column_values_to_be_between("fare_sar", 0, 2000)`,
   `expect_column_values_to_be_in_set("city", ["RUH","JED","DMM"])`,
   and the pickup/dropoff ordering rule.
   → the gate **quarantines** ~{sum(counts[k] for k in ('negative_fare', 'absurd_fare', 'zero_fare_completed', 'bad_city_code', 'dropoff_before_pickup'))}
   rows into `silver.trips_quarantine` and promotes ~{good}.

Benchmark table to fill in during the lab:

| batch | rows in | promoted | quarantined | gate action |
|---|---|---|---|---|
| clean (`../../raw/trips_{date_str}.csv`) | | | 0 | promote |
| dirty (this file) | {total} | 0 | 0 | fail-fast (blocked) |
| dirty, keys repaired | {total - counts['duplicate_trip_id']} | ~{good} | ~{sum(counts[k] for k in ('negative_fare', 'absurd_fare', 'zero_fare_completed', 'bad_city_code', 'dropoff_before_pickup'))} | quarantine |

## Failure mode it teaches

A gate that only alerts is not a gate. If this batch is promoted with a warning,
`gold.fact_trip` reports a negative revenue day, `gold.eta_features` trains on
trips that ended before they started, and the city dimension grows four spellings
of Riyadh.
""")
    return {"folder": "dirty_batch", "rows": total, "counts": dict(counts), "path": path}


# --------------------------------------------------------------------------
# 5. currency_shift/ — Lab 6 distribution drift
# --------------------------------------------------------------------------
def make_currency_shift(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["currency_date"]
    city = cfg["currency_city"]
    rows = [dict(r) for r in read_trips(raw, date_str)]
    shifted = 0
    before, after = [], []
    for r in rows:
        if r["city"] == city and r["fare_sar"]:
            v = float(r["fare_sar"])
            before.append(v)
            r["fare_sar"] = fnum(v * 100.0)      # SAR silently became halalas
            after.append(v * 100.0)
            shifted += 1

    folder = os.path.join(out, "currency_shift")
    path = os.path.join(folder, f"trips_{date_str}_currency_shift.csv")
    total = write_trips(path, rows)

    baseline = read_trips(raw, cfg["currency_baseline_date"])
    base_vals = [float(r["fare_sar"]) for r in baseline
                 if r["city"] == city and r["fare_sar"]]
    mean_base = sum(base_vals) / max(1, len(base_vals))
    mean_before = sum(before) / max(1, len(before))
    mean_after = sum(after) / max(1, len(after))

    write_readme(folder, f"""
# Fixture — `currency_shift/`

**File:** `trips_{date_str}_currency_shift.csv` ({total} rows, canonical `trips` schema)
**Used by:** Lab 6 (Data Quality and Observability) — **distribution-drift** detection.
**Case study:** "The Silent Currency Bug at Muqeem Analytics" (Module 6).

## What this is

An upstream fare service was redeployed and, **for `{city}` only**, started
reporting `fare_sar` in **halalas** instead of riyals — a silent ×100 unit change.
Every row is still a valid row. Nothing about the schema changed. No key is null.
No value is negative.

| metric | value |
|---|---|
| rows in file | {total} |
| rows affected (`city = '{city}'`) | {shifted} |
| other cities | untouched — this is scoped drift, not a whole-batch failure |
| mean `fare_sar`, {city}, baseline day {cfg['currency_baseline_date']} | {mean_base:.2f} |
| mean `fare_sar`, {city}, this file **before** the shift | {mean_before:.2f} |
| mean `fare_sar`, {city}, this file **as shipped** | {mean_after:.2f} |

## Expected detection signal

* **Row-level checks pass.** `expect_column_values_to_be_between("fare_sar", 0, 100000)`
  is satisfied; so is every not-null, uniqueness and type check. That is the lesson.
* A **per-city mean-fare drift check against a frozen baseline** fires:
  `{city}` mean moves from ~{mean_base:.0f} SAR to ~{mean_after:.0f} SAR — roughly **100×**,
  far outside any sane tolerance (e.g. ±25% or a 3σ / PSI > 0.25 threshold).
* `RUH` and `DMM` do **not** drift, which is what tells you the cause is
  *source-scoped*, not a platform-wide bug — and points the investigation straight
  at the `{city}` vendor feed.

Baseline hygiene: freeze the baseline on a **known-good** window
(`{cfg['currency_baseline_date']}`, before the deployment). If you compute the baseline
*after* ingesting this batch you "baseline the bug" and the check never fires again —
that is the `sim-baselinebug` simulation in Module 6.

## Correct response

1. **Quarantine `{city}` only** — do not block RUH and DMM; they are fine.
2. Alert with the evidence (baseline mean, observed mean, ratio, affected city).
3. Correct with a `MERGE` (Module 4) once the unit is normalised — bronze stays
   immutable, silver is repaired, and `DESCRIBE HISTORY` records who fixed what.
4. Record lineage from `silver.trips` back to the vendor feed so the *next*
   redeployment is caught in a day, not a fortnight.

## Failure mode it teaches

Schema validation is type-checking, not meaning-checking. A `double` that is 100×
wrong is still a `double`. Only a distribution check compares the data to what the
business *expects*, and only a frozen baseline gives it something honest to compare to.
""")
    return {"folder": "currency_shift", "rows": total, "shifted": shifted,
            "mean_before": round(mean_before, 2), "mean_after": round(mean_after, 2),
            "path": path}


# --------------------------------------------------------------------------
# 6. erasure_request/ — Lab 4 PDPL right to erasure
# --------------------------------------------------------------------------
def make_erasure_request(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    counts: Counter = Counter()
    day_seen: dict[str, set] = defaultdict(set)
    for date_str in cfg["all_dates"]:
        for r in read_trips(raw, date_str):
            counts[r["rider_id"]] += 1
            day_seen[r["rider_id"]].add(date_str)

    # Riders with a real footprint, so the erasure MERGE actually deletes something.
    candidates = sorted([rid for rid, c in counts.items() if c >= 3])
    picked = rng.sample(candidates, min(7, len(candidates)))
    picked.sort()

    req_date = cfg["erasure_date"]
    doc = {
        "request_id": "PDPL-ER-2026-0417",
        "regulation": "Saudi Personal Data Protection Law (PDPL), Article 18 — right to erasure",
        "received_utc": f"{req_date}T08:12:00Z",
        "sla_days": 30,
        "due_utc": (dt.date.fromisoformat(req_date) + dt.timedelta(days=30)).isoformat() + "T23:59:59Z",
        "requested_by": "Masar Data Protection Office",
        "controller": "Masar (مسار) — synthetic training entity, SDA-DSC-214",
        "lawful_basis_withdrawn": True,
        "scope": {
            "subject_key": "rider_id",
            "rider_ids": picked,
            "tables_in_scope": [
                "bronze.trips", "silver.trips", "gold.fact_trip",
                "gold.trip_features", "gold.eta_features",
            ],
            "columns_in_scope": [
                "rider_id", "dropoff_geohash", "pickup_ts", "dropoff_ts",
            ],
            "note": ("GPS pings are keyed by trip_id/vehicle_id, not rider_id. "
                     "Erasure must follow the trip_id join, or precise location "
                     "for the data subject survives the delete."),
        },
        "expected_effect": {
            "rider_trip_counts_in_sample": {rid: counts[rid] for rid in picked},
            "total_rows_to_delete_from_silver_trips": sum(counts[rid] for rid in picked),
            "dates_touched": sorted({d for rid in picked for d in day_seen[rid]}),
        },
        "retention_note": ("After the MERGE DELETE, run VACUUM with a retention "
                           "shorter than the audit window only if the retention "
                           "policy permits: VACUUM removes time-travel history and "
                           "is what makes the erasure physical."),
        "synthetic": True,
    }

    folder = os.path.join(out, "erasure_request")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"pdpl_erasure_{req_date}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    rows_to_delete = doc["expected_effect"]["total_rows_to_delete_from_silver_trips"]
    write_readme(folder, f"""
# Fixture — `erasure_request/`

**File:** `pdpl_erasure_{req_date}.json`
**Used by:** Lab 4 (Delta Lake and ACID) — the **compliant-delete** drill.
**Also referenced by:** Module 6 PDPL clinic, Module 4 case study (reproduce a
filing while honouring an erasure).

## What this is

A data-subject erasure request under the **Saudi Personal Data Protection Law
(PDPL)**, naming **{len(picked)} `rider_id`s** that appear across the shipped sample.
It is the input to the "right to be forgotten" exercise.

* rider_ids in scope: {", ".join('`' + r + '`' for r in picked)}
* rows to delete from `silver.trips` in the shipped sample: **{rows_to_delete}**
* dates touched: {", ".join(doc['expected_effect']['dates_touched'])}

**All rider_ids are synthetic.** No real person is represented.

## Expected detection signal

```sql
-- before
SELECT count(*) FROM silver.trips WHERE rider_id IN (…);   -- {rows_to_delete}

DELETE FROM silver.trips WHERE rider_id IN (…);            -- atomic, one commit

-- after
SELECT count(*) FROM silver.trips WHERE rider_id IN (…);   -- 0
DESCRIBE HISTORY silver.trips;                             -- operation = DELETE, with metrics
SELECT count(*) FROM silver.trips VERSION AS OF <v-1>
  WHERE rider_id IN (…);                                   -- {rows_to_delete}  <- still there!
```

That last line is the teaching moment: **the rows are gone from the current
version but still present in time travel.** The erasure is not complete until
`VACUUM` removes the unreferenced files, and `VACUUM` is therefore a *governance*
decision, not a storage chore.

The second trap: GPS. `gps_events` has no `rider_id`, so `WHERE rider_id IN (…)`
matches nothing there — yet the pings are precise location data for the same trips.
A correct erasure joins through `trip_id`. A team that forgets this passes their
own test and fails an audit.

## Failure mode it teaches

Compliance is a data-engineering property. Without ACID deletes, an erasure means
rewriting a whole partition and hoping no reader saw the intermediate state; with
no lineage, you cannot even enumerate where the subject's data went.
""")
    return {"folder": "erasure_request", "riders": len(picked),
            "rows_to_delete": rows_to_delete, "path": path}


# --------------------------------------------------------------------------
# 7. incident_speed_unit/ — THE signature incident
# --------------------------------------------------------------------------
def make_speed_unit_incident(raw: str, out: str, rng: random.Random, cfg: dict) -> dict:
    date_str = cfg["incident_date"]
    from_hour = cfg["incident_from_hour_utc"]
    src_path = gps_path_for(raw, date_str)

    folder = os.path.join(out, "incident_speed_unit")
    os.makedirs(folder, exist_ok=True)
    # Mirror the raw zone's compression choice so loaders need one code path.
    gz = src_path.endswith(".gz")
    path = os.path.join(folder, f"gps_{date_str}_v250.ndjson" + (".gz" if gz else ""))

    # A firmware rollout hits a subset of the fleet, from a point in time onwards.
    def affected(vehicle_id: str) -> bool:
        return int(hashlib.md5(vehicle_id.encode()).hexdigest(), 16) % 100 < cfg["incident_fleet_pct"]

    n_in = n_out = 0
    sum_before = sum_after = 0.0
    vehicles = set()
    open_dst = ((lambda p_: gzip.open(p_, "wt", encoding="utf-8", compresslevel=9))
                if gz else (lambda p_: open(p_, "w", encoding="utf-8")))
    with open_ndjson(src_path) as fh, open_dst(path) as of:
        for line in fh:
            n_in += 1
            ev = json.loads(line)
            if int(ev["ts"][11:13]) < from_hour:
                continue
            if not affected(ev["vehicle_id"]):
                continue
            kmh = float(ev["payload"]["speed_kmh"])
            sum_before += kmh
            # SAME KEY, SAME TYPE, DIFFERENT UNIT. This is the whole incident.
            ms = round(kmh / 3.6, 2)
            sum_after += ms
            ev["payload"]["speed_kmh"] = ms
            ev["producer_version"] = "2.5.0"
            ev["event_id"] = "ev_" + hashlib.md5(
                (ev["event_id"] + "|v250").encode()).hexdigest()[:16]
            vehicles.add(ev["vehicle_id"])
            of.write(json.dumps(ev, ensure_ascii=False, separators=(",", ":")))
            of.write("\n")
            n_out += 1

    mean_before = sum_before / max(1, n_out)
    mean_after = sum_after / max(1, n_out)

    write_readme(folder, f"""
# Fixture — `incident_speed_unit/` — **THE signature incident**

**File:** `{os.path.basename(path)}` ({n_out:,} events, canonical `gps_events` schema —
**byte-for-byte schema-compatible with the {date_str} raw feed**)
**Used by:** Lab 5 (streaming ingest), Lab 6 (observability / drift), Lab 8 (AI serving),
Module 8 ETA-model degradation narrative. This is the incident the whole course
keeps coming back to.

## What is wrong

On {date_str}, a device-firmware rollout moved **{cfg['incident_fleet_pct']}% of the fleet**
({len(vehicles):,} vehicles) from `producer_version` **2.4.0** to **2.5.0**, starting at
**{from_hour:02d}:00 UTC** ({(from_hour + 3) % 24:02d}:00 Riyadh).

The new firmware kept the field name `speed_kmh` and its type (`double`) —
and started writing **metres per second**.

```json
{{"...":"...","payload":{{"lat":24.71,"lon":46.68,"speed_kmh":11.2, ...}},"producer_version":"2.5.0"}}
                                                     ^^^^^^^^^^^^^^
                                         40.3 km/h reported as 11.2 — same key, same type
```

| | value |
|---|---|
| events in this batch | {n_out:,} |
| distinct vehicles affected | {len(vehicles):,} |
| mean `speed_kmh` if the field were km/h | {mean_before:.2f} |
| mean `speed_kmh` **as shipped** (m/s) | {mean_after:.2f} |
| ratio | **{(mean_before / max(0.001, mean_after)):.2f}×** (i.e. 3.6, the m/s → km/h factor) |

## Why nothing catches it

* **Schema validation passes.** Same keys, same JSON types, same nesting. A
  `StructType` check, an Avro/Protobuf compatibility check and a `MERGE SCHEMA`
  all say "compatible".
* **Range checks pass.** 11.2 is a perfectly plausible speed. So is 0.5. So is 38.
  Any `expect_column_values_to_be_between("speed_kmh", 0, 200)` is satisfied — in
  fact the corrupted data is *further inside* the range than the good data.
* **Row counts, freshness and volume are all normal.** The feed is healthy by every
  operational signal.
* **No error is ever raised.** Not at ingest, not in the stream, not in dbt.

## What it actually breaks

`gold.eta_features.rolling_avg_speed_10m` is computed from `payload.speed_kmh`.
For the affected vehicles it silently falls by 3.6×. The ETA model then learns
"this zone is crawling" for a third of the fleet and starts over-predicting
journey times — the ride-hailing symptom is quoted ETAs drifting long, riders
cancelling, and a demand model that under-serves the affected zones. The model
metrics degrade slowly; nobody links it to a firmware note in a device changelog.

## Expected detection signal

The **only** things that catch this, in order of how fast they would have:

1. **Distribution drift on `speed_kmh`, segmented by `producer_version`.**
   `mean(speed_kmh) WHERE producer_version='2.5.0'` ≈ {mean_after:.1f} vs
   `≈ {mean_before:.1f}` for `2.4.0` on the same zones and hours. PSI/KS between the two
   version cohorts blows past any threshold. **Always segment drift by producer version.**
2. **A cross-field physical-plausibility check**: reconcile
   `distance_km / duration_min` from `silver.trips` against the mean ping speed for
   the same `trip_id`. The two disagree by 3.6× only for v2.5.0 trips. This is a
   *reconciliation* check — the top of the data-quality pyramid, and the only tier
   that compares two independent measurements of the same physical fact.
3. **A unit-carrying contract.** If the field were `speed_mps` or the payload
   carried `"speed_unit":"km/h"`, the producer change would have been a *breaking*
   schema change and the pipeline would have failed loudly on day one.
4. **Lineage + a producer_version dimension.** Once drift fires, `producer_version`
   is the first column to group by; without it in bronze, the investigation has
   nothing to correlate against.

## How to run it

```bash
# baseline: ingest the clean day
python3 generators/emit_gps_stream.py --file data/raw/gps/gps_{date_str}.ndjson.gz

# then the incident batch
python3 generators/emit_gps_stream.py --file data/fixtures/incident_speed_unit/{os.path.basename(path)}
# or, equivalently, synthesise it live:
python3 generators/emit_gps_stream.py --file data/raw/gps/gps_{date_str}.ndjson.gz --inject unit-shift
```

Then compute `rolling_avg_speed_10m` over the combined bronze and plot it by hour:
the break is at {from_hour:02d}:00 UTC and it is obvious *once you know to look*.
That gap — between "obvious in hindsight" and "invisible in flight" — is the point
of the whole module.

## The unifying question

> "What happens to Masar's AI system if THIS part of the data platform fails?"

Here nothing *failed*. Every component did exactly what it was told. The platform
was healthy, the schema was valid, the tests were green, and the model got worse
anyway — because type-compatibility is not semantic compatibility.
""")
    return {"folder": "incident_speed_unit", "rows": n_out,
            "vehicles": len(vehicles),
            "mean_kmh_if_kmh": round(mean_before, 2),
            "mean_as_shipped_mps": round(mean_after, 2), "path": path}


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Build SDA-DSC-214 teaching fixtures from the Masar raw zone.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--raw", default="../raw")
    p.add_argument("--out", default="../fixtures")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--start", default="2026-06-01")
    p.add_argument("--days", type=int, default=5)
    p.add_argument("--incident-fleet-pct", type=int, default=34,
                   help="percent of the fleet upgraded to the faulty firmware 2.5.0")
    p.add_argument("--incident-from-hour-utc", type=int, default=9,
                   help="UTC hour from which producer_version 2.5.0 appears")
    args = p.parse_args(argv)

    start = dt.date.fromisoformat(args.start)
    all_dates = [(start + dt.timedelta(days=i)).isoformat() for i in range(args.days)]

    cfg = {
        "all_dates": all_dates,
        "corrections_date": "2026-06-03",
        "late_trips_date": "2026-06-02",
        "late_trips_arrival": "2026-06-04",
        "late_pings_date": "2026-06-04",
        "dirty_date": "2026-06-05",
        "currency_date": "2026-06-05",
        "currency_city": "JED",
        "currency_baseline_date": "2026-06-03",
        "erasure_date": "2026-06-10",
        "incident_date": "2026-06-05",
        "incident_fleet_pct": args.incident_fleet_pct,
        "incident_from_hour_utc": args.incident_from_hour_utc,
    }

    needed = {cfg["corrections_date"], cfg["late_trips_date"], cfg["late_pings_date"],
              cfg["dirty_date"], cfg["currency_date"], cfg["currency_baseline_date"],
              cfg["incident_date"]}
    missing = sorted(d for d in needed if not os.path.exists(
        os.path.join(args.raw, f"trips_{d}.csv")))
    if missing:
        print(f"ERROR: raw zone {args.raw} is missing days: {', '.join(missing)}\n"
              f"Run generate_masar.py first.", file=sys.stderr)
        return 2

    os.makedirs(args.out, exist_ok=True)
    results = []
    steps = [
        ("corrections", make_corrections),
        ("late_trips", make_late_trips),
        ("late_pings", make_late_pings),
        ("dirty_batch", make_dirty_batch),
        ("currency_shift", make_currency_shift),
        ("erasure_request", make_erasure_request),
        ("incident_speed_unit", make_speed_unit_incident),
    ]
    for i, (name, fn) in enumerate(steps):
        rng = random.Random(args.seed * 7919 + i)
        results.append(fn(args.raw, args.out, rng, cfg))

    index = """# Masar teaching fixtures — SDA-DSC-214

These are **staged incidents**, not background noise. `../raw/` already carries
realistic low-level defects (null geohashes, mixed date formats, a few duplicate
GPS events). The folders here each isolate **one** failure mode so a lab can
detect it, decide on it, and prove the fix.

| folder | file | lab | the failure |
|---|---|---|---|
| `corrections/` | `trips_corrections_2026-06-03.csv` | Lab 4 | corrections applied by append instead of MERGE |
| `late_trips/` | `trips_late_2026-06-02.csv` | Lab 3 | late-arriving data missed by `date = today` |
| `late_pings/` | `gps_late_2026-06-04.ndjson` | Lab 5 | late + out-of-order events vs the watermark |
| `dirty_batch/` | `trips_2026-06-05_dirty.csv` | Lab 6 | fail-fast (integrity) vs quarantine (partial) |
| `currency_shift/` | `trips_2026-06-05_currency_shift.csv` | Lab 6 | a ×100 unit change every row-level check passes |
| `erasure_request/` | `pdpl_erasure_2026-06-10.json` | Lab 4 | PDPL erasure, time travel, and VACUUM |
| `incident_speed_unit/` | `gps_2026-06-05_v250.ndjson` | Lab 5/6/8 | **the signature incident** — `speed_kmh` carrying m/s |

Every folder has its own `README.md` with the exact expected detection signal and
the numbers to check against.

Regenerate all of them with:

```bash
cd generators
python3 inject_defects.py --raw ../raw --out ../fixtures
```

All content is fully synthetic and derived from `../raw`.
"""
    with open(os.path.join(args.out, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(index)

    summary = {
        "generator": "inject_defects.py",
        "version": FIXTURES_VERSION,
        "seed": args.seed,
        "raw_source": os.path.normpath(args.raw),
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fixtures": results,
    }
    with open(os.path.join(args.out, "_FIXTURES.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print("=" * 86)
    print(f"MASAR FIXTURES WRITTEN -> {os.path.abspath(args.out)}")
    print("=" * 86)
    print(f"{'fixture':<24}{'file':<44}{'rows':>8}{'size':>10}")
    print("-" * 86)
    for r in results:
        sz = os.path.getsize(r["path"])
        print(f"{r['folder']:<24}{os.path.basename(r['path']):<44}"
              f"{r.get('rows', r.get('riders', 0)):>8,}{sz / 1024:>9,.0f}K")
    print("-" * 86)
    print("each folder carries a README.md (what is wrong / which lab / detection signal)")
    print("=" * 86)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
