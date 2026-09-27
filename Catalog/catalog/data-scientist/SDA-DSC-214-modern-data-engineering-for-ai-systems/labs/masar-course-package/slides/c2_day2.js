const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "DAY 2", title: "Pipelines —\nfrom ETL to ELT",
    sub: "How bronze becomes a silver table people depend on: incremental, idempotent, tested, documented.",
    items: ["ETL vs ELT on the cloud", "dbt as the transformation framework", "Idempotency and incremental models", "The late-arriving data bug", "Labs 3a and 3b — build silver.trips"] });

  K.twoCol(pres, { kicker: "Module 3 · Section 1", title: "ETL and ELT",
    left: { h: "ETL — Extract, Transform, Load", color: P.silver, sub: "Born when storage was expensive and warehouses were rigid",
      items: [
        "Transform BEFORE the data lands in the analytics store.",
        "You could not afford to keep raw, so you cleaned and shaped it in a separate engine and loaded only the finished product.",
        "Cost: raw data is discarded, so nothing can be reprocessed.",
        "Cost: transformation logic lives in a separate tool, outside the platform's version control and lineage.",
        "Cost: any logic change means re-extracting from source.",
        "Still right for: heavy transformation before a real-time sink; masking that must happen before data ever lands.",
      ] },
    right: { h: "ELT — Extract, Load, Transform", color: P.teal, sub: "Cheap storage keeps raw; elastic compute transforms in place",
      items: [
        "Land RAW first — this is bronze — then transform inside the platform with its own elastic compute.",
        "Reprocessing: raw is retained, so a fixed transformation reruns over all history.",
        "Auditability: every curated value traces back to an untouched source row.",
        "Velocity: changing logic is a code change and a rerun, never a re-ingestion.",
        "Ownership: transformations are SQL models that analysts and engineers both review.",
        "For an AI-data Lakehouse, ELT is the default. This course builds ELT.",
      ] },
    note: "The four ELT payoffs are exactly the four medallion virtues. That is not a coincidence — ELT is what the medallion is for." });

  K.table(pres, { kicker: "Module 3 · Section 2", title: "dbt layering mirrors the medallion",
    lead: "Models are SELECT statements dbt materialises; ref() and source() build the dependency graph and run order.",
    head: ["dbt layer", "Medallion", "Purpose", "Materialisation", "Masar example"],
    widths: [1.9, 1.75, 4.0, 1.9, 2.54], rowH: 0.62, fs: 11.5,
    rows: [
      ["staging (stg_)", "bronze →", "1:1 with a source: rename, cast, light clean. No joins. Isolates every source quirk in exactly one place.", "view or incremental", "stg_trips, stg_gps, stg_drivers"],
      ["intermediate (int_)", "→ silver", "Reusable joins and derivations shared by several marts. Removes duplication between models.", "ephemeral or view", "int_trips_with_driver"],
      ["marts", "silver, gold", "Conformed entities and business aggregates — the stable contract consumers read.", "table or incremental", "silver.trips, gold.zone_hourly_demand"],
    ],
    note: "Why it matters: renaming a source column touches exactly one staging model. Cast and rename in marts instead, and a single rename breaks ten models at once." });

  K.bullets(pres, { kicker: "Module 3 · Section 3", title: "Idempotency: the property that makes retries safe",
    lead: "Running the transformation twice yields the same result as running it once. This is what makes retries, backfills and disaster recovery safe.",
    rowH: 1.05, items: [
      { n: "✓", h: "MERGE on a key is idempotent", t: "Re-applying the same rows updates nothing. The second run is a no-op. This is why every layer downstream of bronze in this course merges on trip_id.", color: P.teal },
      { n: "✗", h: "A blind INSERT is not", t: "The second run duplicates everything. It is the single most common cause of an aggregate that silently doubles after a retry.", color: P.alarm },
      { n: "→", h: "Incremental processing is the other half", t: "On day 400 you do not re-transform 400 days of trips. You transform the last day and merge it in. dbt's incremental materialisation expresses exactly this.", color: P.bronze },
      { n: "!", h: "Together they make backfills boring", t: "Parameterise the date range and rerun. Idempotency guarantees correctness; incrementality guarantees it finishes. A corrected model can repair six months of history in one run.", color: P.gold },
    ] });

  K.code(pres, { kicker: "Module 3 · Section 3", title: "The single most common production pipeline bug",
    lang: "sql · dbt",
    fs: 10.5,
    code: `-- WRONG: silently drops every late-arriving trip
{{ config(materialized='incremental', unique_key='trip_id') }}

select * from {{ ref('stg_trips') }}
{% if is_incremental() %}
  where pickup_date = current_date()      -- <-- the bug
{% endif %}


-- RIGHT: lookback window + merge on the business key
{{ config(
     materialized = 'incremental',
     unique_key   = 'trip_id',
     incremental_strategy = 'merge',
     partition_by = ['pickup_date']
) }}

select * from {{ ref('stg_trips') }}
{% if is_incremental() %}
  where pickup_date >= date_sub(current_date(), 3)   -- 3-day lookback
{% endif %}

-- and in _silver__models.yml:
--   tests: [unique, not_null]  on trip_id`,
    points: [
      "A trip that ended yesterday may only reach bronze today — payment settles after midnight, a device was in a tunnel, a source retried.",
      "WHERE date = today never sees it. The row is not rejected and no error is raised. It simply never arrives.",
      "The lookback window reprocesses the last N days; the MERGE on trip_id corrects late rows without duplicating settled ones.",
      "The unique test on the key is what tells you the day the fix stops working.",
    ],
    notes: "Draw the timeline on the board: trip ends 23:50, payment settles 00:07, bronze receives it at 02:00 the next day. Then ask which run should have counted it. This is CS-03 and it cost Wusool a ~2% silent undercount for months." });

  K.cards(pres, { kicker: "Case study CS-03 · 20 minutes", title: "The silent undercount at “Wusool” Mobility",
    cols: 4, cardH: 2.5, cards: [
      { h: "The symptom", t: "Daily completed-trips is about 2% below what the operations system reports. Every individual row is valid. No test fails. No alert fires.", color: P.silver },
      { h: "The cause", t: "The daily model filters WHERE trip_date = current_date(). Trips whose payment settled after midnight arrive in bronze the next morning and are never counted.", color: P.alarm },
      { h: "The damage", t: "Driver incentives were computed from the undercount. A demand model trained on labels that systematically under-represented late-settling trips — i.e. exactly the busiest evenings.", color: P.alarm },
      { h: "The fix", t: "Three lines: a 3-day lookback window, an incremental merge on trip_id, and a unique test on the key. No re-ingestion, no new tool. The backfill corrected six months in one parameterised run.", color: P.teal },
    ],
    note: "Ask: what would have DETECTED this? Not a row-level test — a reconciliation check against the ops system, and a volume observability signal. That is Module 6, previewed." });

  K.cards(pres, { kicker: "Module 3 · Section 4", title: "Tests and docs are part of the pipeline",
    cols: 3, cardH: 2.35, cards: [
      { h: "Source freshness", t: "Assert bronze received data recently — loaded_at within N hours. Catches an upstream outage BEFORE the transform silently republishes yesterday's mart.", color: P.bronze },
      { h: "Schema and constraint tests", t: "unique, not_null, accepted_values, relationships. On silver.trips: unique + not_null on trip_id is the test that would have caught three of this course's case studies.", color: P.silver },
      { h: "Custom data tests", t: "SQL that must return zero rows: fare_sar <= 0, dropoff_ts < pickup_ts, city not in the KSA set. Cheap, specific, and they encode business rules reviewers can read.", color: P.gold },
      { h: "Lineage and docs, generated", t: "dbt docs renders the DAG and every model and column description from the same project — the audit trail that Module 6 governance and PDPL depend on.", color: P.teal },
      { h: "Run them every build", t: "Tests declared alongside models run on every dbt build. Testing and docs live WITH the transformation, so they never drift from it.", color: P.bronze },
      { h: "Order matters", t: "Schedule freshness checks BEFORE the transform. A stale source should fail loudly, not quietly produce a confident wrong number.", color: P.alarm },
    ] });

  K.bullets(pres, { kicker: "Module 3 · Section 5", title: "Six mistakes — all six are in the Lab 3 starter",
    rowH: 0.82, items: [
      { n: "1", h: "WHERE date = current_date() with no lookback", t: "Silently drops late-arriving trips. The bug you just saw.", color: P.alarm },
      { n: "2", h: "Full-refreshing a huge table every run", t: "The incremental key or filter is wrong, so every run is a rebuild — slow and expensive, and nobody notices because the answer is right.", color: P.alarm },
      { n: "3", h: "Deduplicating with DISTINCT instead of latest-row-per-key", t: "Keeps the stale version when a trip is corrected. The correction is in the table and is simply never used.", color: P.alarm },
      { n: "4", h: "Casting and renaming in marts instead of staging", t: "Source quirks leak everywhere; one upstream rename breaks ten models.", color: P.alarm },
      { n: "5", h: "No not_null or unique test on the silver key", t: "Duplicate trip_id slips through to features and BI, inflating both by the same invisible amount.", color: P.alarm },
      { n: "6", h: "Timezone drift", t: "Mixing UTC and Asia/Riyadh timestamps, so “yesterday” means two different things in two models. Store UTC, present +03.", color: P.alarm },
    ] });

  K.lab(pres, { id: "3", title: "Build the ELT pipeline to silver.trips",
    meta: [["Duration", "Two 50-minute blocks (3a staging · 3b silver)"], ["Checkpoint", "git checkout lab3-start"], ["Objective", "A conformed, tested, incremental silver.trips built from bronze with dbt on Delta"], ["Deliverable", "silver.trips + a green dbt test run + a proven backfill"]],
    tasks: [
      "3a — build stg_trips, stg_gps and stg_drivers: type, rename, isolate every source quirk here and nowhere else. Declare source freshness.",
      "3a — resolve the three date formats in drivers.csv, and the ~2% of trips carrying DD/MM/YYYY timestamps, in staging.",
      "3b — build silver.trips: dedup to one row per trip_id, join to the driver dimension, derive fare and duration features.",
      "3b — make it incremental: merge on trip_id with a 3-day lookback window; partition by pickup_date.",
      "3b — add at least six tests including unique and not_null on trip_id, then load the late-arrival fixture and prove the lookback catches it.",
    ],
    accept: [
      "dbt test is green, with ≥ 6 tests including unique + not_null on trip_id.",
      "A second identical run changes zero rows — the pipeline is idempotent.",
      "data/fixtures/late_trips lands and is merged correctly without duplicating settled rows.",
      "silver.trips holds one row per trip_id, in UTC, with conformed units.",
    ],
    notes: "Lab 3b is where pairs pay off — the SQL-strong participant leads. Publish lab3b-start so anyone stuck on staging can fast-forward." });

  K.statement(pres, { kicker: "Day 2 · close",
    text: "You now have a table.\nTomorrow you make it a transaction.",
    size: 32,
    sub: "silver.trips is conformed and tested — but it is still a folder of Parquet files that you HOPE is consistent.\nDay 3 opens the transaction log and turns it into something you can audit, correct and rewind.",
    notes: "End with the question: if two jobs wrote to silver.trips at the same time right now, what would happen? Let them sit with not knowing. That is Module 4's first slide." });
};
