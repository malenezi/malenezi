const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "DAY 5", title: "Build and serve",
    sub: "Everything from Modules 1–6 becomes one orchestrated, idempotent, observable platform — and then it is consumed.",
    items: ["M7 — Assembling the Mini-Lakehouse", "Lab 7 — orchestrate the full DAG", "M8 — Serving AI and BI", "Lab 8 — the leakage drill", "Capstone build and demos"] });

  K.divider(pres, { eyebrow: "MODULE 7", title: "Building a\nMini-Lakehouse",
    sub: "The integration module. The new work here is not logic — it is wiring, contracts and orchestration.",
    items: ["The architecture, assembled", "Layer contracts", "DAGs, dependencies, idempotency", "Building gold for two consumers"] });

  K.medallion(pres, { kicker: "Module 7 · Section 1", title: "The Masar Mini-Lakehouse, assembled",
    lead: "Every node here is something you already built. M7 wires them together and makes the whole thing runnable by one command.",
    sources: ["trips CSV (M1)", "drivers / vehicles", "payments", "GPS via Kafka (M5)", "zones + weather"],
    bronze: { tables: "land_bronze.py (M1) · ingest_gps_stream.py (M5)", contract: "Append-only, lineage columns, as-received. Batch and stream land side by side into the same layer." },
    silver: { tables: "silver.trips (M3, M4) · silver.vehicle_positions (M5)", contract: "Quality gate (M6) then ELT: one row per trip_id, constrained Delta, conformed units and timezone." },
    gold:   { tables: "zone_hourly_demand · driver_daily · fact_trip + dims · eta_features", contract: "Documented grain. Idempotent. Point-in-time correct. Maintained (OPTIMIZE/ZORDER) as a DAG task." },
    bi: "morning ops review\nstar schema\nconformed dims",
    ai: "offline training\nRedis online store\nlive ETA service",
    note: "One idempotent DAG:  land >> gate >> silver >> [gold…] >> maintain.  Observability: freshness · volume · drift.  Governance: classification · access · PDPL retention." });

  K.table(pres, { kicker: "Module 7 · Section 2", title: "Layer contracts — what lets teams work independently",
    lead: "A contract is the guaranteed shape and quality a layer promises. Breaking one is a breaking change requiring versioning and communication — exactly like an API.",
    head: ["Layer", "Guarantees", "Grain", "Owner decides"],
    widths: [1.5, 5.6, 2.6, 2.39], rowH: 0.72, fs: 11.5,
    rows: [
      ["Bronze", "Append-only · carries _ingested_at, _source_file, _batch_id · schema as-received · never mutated", "One row per source record, per landing", "Retention of raw history"],
      ["Silver", "One row per trip_id · enforced schema and CHECK constraints · quality-gated · conformed timezone and units · completed valid trips only", "One row per business key", "The definition of “a completed trip”"],
      ["Gold", "Business-modelled · documented grain · feature table is point-in-time correct · PDPL-safe at the boundary", "Stated explicitly per table — e.g. one row per zone per hour", "What each consumer is promised"],
    ],
    note: "A BI developer builds on gold's documented grain without reading the ELT code, trusting the contract. That is the whole point — and it is why “gold built straight from bronze, just this once” is a rubric flag." });

  K.cards(pres, { kicker: "Module 7 · Section 3", title: "Orchestration is a guarantee, not a scheduler",
    cols: 3, cardH: 2.4, cards: [
      { n: "1", h: "Dependency ordering", t: "Gold never builds from a silver that has not refreshed. The DAG makes “I ran step 7 before step 4” structurally impossible.", color: P.bronze },
      { n: "2", h: "Idempotency", t: "Every task reruns safely — bronze appends, everything downstream merges. Retries and backfills cannot corrupt data.", color: P.silver },
      { n: "3", h: "Atomicity per task", t: "Delta commits mean a failed task leaves no half-written table behind for the next run to trip over.", color: P.gold },
      { n: "4", h: "Observability", t: "Freshness, volume and quality signals gate promotion and feed alerts — they are DAG tasks, not a separate monitoring project.", color: P.teal },
      { n: "5", h: "Recoverability", t: "Because tasks are idempotent and Delta is transactional, a full rerun recovers from any failure with no duplicates and no manual cleanup.", color: P.bronze },
      { n: "6", h: "One command", t: "make pipeline, or one DAG trigger. That is the team's public interface. If recovery requires knowing which notebook to run, you do not have a platform.", color: P.alarm },
    ],
    note: "CS-07 (“Rakeez” Data): twelve notebooks run by hand each morning in a remembered order. A new engineer ran step 7 before step 4; gold rebuilt from stale silver; the exec dashboard showed last week's demand. No failure, no alert — just a wrong number and a lost morning." });

  K.lab(pres, { id: "7", title: "Assemble and orchestrate the Mini-Lakehouse",
    meta: [["Duration", "50 minutes"], ["Checkpoint", "git checkout lab7-start"], ["Objective", "The full medallion as one dependency-ordered, idempotent, recoverable DAG"], ["Deliverable", "make pipeline runs end to end + a proven recovery from an injected failure"]],
    tasks: [
      "Wire land >> gate >> silver >> [gold…] >> maintain as one dependency-ordered DAG with explicit upstreams.",
      "Build gold.zone_hourly_demand and gold.driver_daily idempotently, and document the grain of each in DATA_CONTRACTS.md.",
      "Run the whole pipeline with one command. Then run it AGAIN and prove row counts are unchanged.",
      "Inject a mid-DAG failure with --inject-failure, observe which downstream tasks are skipped, then recover by rerunning the whole DAG.",
      "Add OPTIMIZE and VACUUM as scheduled DAG tasks, and emit per-task run metadata: rows processed, duration, quality result.",
    ],
    accept: [
      "One command runs the whole medallion; no manual step is required anywhere.",
      "A second run is a no-op — counts identical, no duplicates.",
      "Recovery from the injected failure needs no cleanup, only a rerun.",
      "Every gold table's grain is documented, and no gold table reads from bronze.",
    ] });

  K.divider(pres, { eyebrow: "MODULE 8", title: "Serving data to\nAI and BI",
    sub: "A Lakehouse exists to be consumed. Two customers, two contracts, one governed gold layer — and one cardinal sin.",
    items: ["Two consumers, two contracts", "Point-in-time correctness", "Feature leakage and the four classes", "Offline and online consistency", "The star schema and conformed dimensions"] });

  K.table(pres, { kicker: "Module 8 · Section 1", title: "Two consumers, two contracts",
    lead: "Which is exactly why they get different tables — derived from the same silver, sharing the same feature logic.",
    head: ["Concern", "AI / feature store", "BI / analytics"],
    widths: [2.2, 4.95, 4.94], rowH: 0.5, fs: 12,
    rows: [
      ["Grain", "Entity × time — per trip, per zone-hour", "Business dimensions — per city, per day"],
      ["Correctness", "Point-in-time, no leakage", "Consistent definitions, conformed dimensions"],
      ["Latency", "Training in batch, inference in milliseconds", "Interactive dashboard, sub-second"],
      ["Schema", "Model-ready features, versioned", "Human-readable star schema"],
      ["Freshness", "As fresh as the model needs", "As fresh as the decision needs"],
    ],
    note: "One source of truth, two contracts — so the analyst's “trips per zone” and the model's “zone demand feature” cannot silently disagree. This is Day 1's two-tier lesson, arriving at the consumption boundary." });

  K.statement(pres, { kicker: "Module 8 · the cardinal sin", size: 31,
    text: "Feature leakage:\nletting a feature see information that\nwould not exist at prediction time.",
    sub: "It inflates offline metrics and collapses in production — and it is the single hardest defect to catch in review,\nbecause the pipeline is correct, the tests pass, and the model looks brilliant.\n\nThe defence is structural, not vigilant: point-in-time correctness, enforced by construction.",
    notes: "CS-08 (“Wojhah”): 0.93 R² offline, worse than the old heuristic live. The culprit was a “current zone demand” feature computed from the WHOLE hour containing the trip — including trips that started after the one being predicted." });

  K.cards(pres, { kicker: "Module 8 · the classification", title: "Four classes. One question. Every feature gets exactly one.",
    lead: "“Could this feature value have been known at prediction time?” — asked of every column, every time, with a written justification.",
    cols: 4, cardH: 3.15, cards: [
      { n: "✓", h: "VALID", t: "Known before the prediction moment, and computable in the online path with the same logic.\n\nMasar: pickup_zone_id, hour_of_day, day_of_week, distance_km at request time, driver_recent_trip_count over strictly prior trips.", color: P.teal },
      { n: "≈", h: "STALE", t: "Known at prediction time, but the online value lags the offline one — computed on a schedule, cached, or refreshed hourly.\n\nUsable, but the training set must reflect the SAME staleness or you have manufactured skew.", color: P.gold },
      { n: "✗", h: "LEAKAGE", t: "Includes information from at or after the prediction moment. A centred window, a same-hour aggregate, a post-trip GPS ping, anything derived from the label.\n\nMasar: rolling_zone_demand_15m if the window is centred rather than trailing.", color: P.alarm },
      { n: "!", h: "UNAVAILABLE ONLINE", t: "Legitimately known at prediction time, but not retrievable within the serving latency budget.\n\nThe feature is honest and unusable. Either materialise it into the online store, or drop it — do not train on it and hope.", color: P.silver },
    ],
    note: "That one exercise connects data engineering directly to production AI reliability. It is Activity ACT-09, Lab 8's mandatory drill, and PA-3." });

  K.code(pres, { kicker: "Module 8 · Section 2", title: "Point-in-time correctness, enforced by construction",
    lang: "python · pyspark", fs: 10,
    code: `# WRONG: the window is centred on the trip, so it sees the future
w_bad = (Window.partitionBy("pickup_zone_id").orderBy("event_ts")
               .rangeBetween(-450, 450))          # ±7.5 min

# RIGHT: strictly prior, and the boundary is exclusive
w_ok  = (Window.partitionBy("pickup_zone_id").orderBy("event_ts")
               .rangeBetween(-900, -1))           # [t-15min , t)

features = (events
    .withColumn("rolling_zone_demand_15m", count("*").over(w_ok))
    .withColumn("rolling_avg_speed_10m",   avg("speed_kmh").over(w_ok10))
    .withColumn("feature_ts",              col("event_ts")))

# training join: features AS OF each label's timestamp, never after
train = labels.join(features,
    (labels.trip_id == features.trip_id) &
    (features.feature_ts < labels.pickup_ts), "left")`,
    points: [
      "rangeBetween(-900, -1) — the -1 is the whole defence. An inclusive upper bound lets the row see itself.",
      "The same feature module computes offline and online values. Re-implementing for the online path is skew by construction.",
      "Delta time travel makes the training snapshot exact: record the version in the model card and the run is reproducible forever.",
      "A leakage-lint that fails the pipeline when a feature window includes non-prior data is a capstone extension — and worth the hour.",
    ] });

  K.chart(pres, { kicker: "Module 8 · Lab 8 drill", title: "What honesty costs, and why it is worth paying",
    type: pres.ChartType.bar, showValue: true, labelPos: "outEnd", fmt: "0.000",
    colors: [P.alarm, P.teal],
    data: [{ name: "Offline R² on the ETA model", labels: ["With leaking features", "Point-in-time correct"], values: [0.943, 0.712] }],
    opts: { valAxisMaxVal: 1, valAxisMinVal: 0, valAxisMajorUnit: 0.2, barGapWidthPct: 110, varyColors: true },
    side: { h: "Read this chart correctly", items: [
      "Offline MAE moves the same way: 1.81 minutes → 4.58 minutes. The model did not get worse; the measurement got honest.",
      "The leaking version would have scored far worse than 0.712 in production — CS-08's model lost to the heuristic it replaced.",
      "A feature that looks too good is usually leaking. Suspicion is a professional skill, not pessimism.",
      "The number you defend at a capstone demo is the honest one, with the drill transcript behind it.",
    ] },
    takeaway: "Reserve the leakage drill even if you compress everything else on Day 5. It is the single most memorable lesson and it directly protects the capstone." });

  K.twoCol(pres, { kicker: "Module 8 · Section 3", title: "Offline and online serving must agree",
    left: { h: "Offline — batch", color: P.bronze, sub: "Training and batch scoring",
      items: [
        "Features read directly from the gold Delta feature table.",
        "High throughput, latency-insensitive; the Lakehouse serves this natively.",
        "The nightly demand forecast reads here.",
        "Reproducible via Delta time travel: version pinned in the model card.",
      ] },
    right: { h: "Online — real-time", color: P.teal, sub: "A single entity, in milliseconds",
      items: [
        "A columnar Lakehouse scan is too slow for a single-row point lookup, so the latest slice is materialised into a low-latency store — Redis, keyed masar:features:zone:{zone_id}.",
        "MATERIALISE, never re-implement. Compute the features once in the Lakehouse, then copy the latest slice out.",
        "Refresh the online store as a DAG task with its own freshness monitoring.",
        "Prove consistency: every key in the online store must match the offline table it was derived from.",
      ] },
    note: "Re-implementing feature logic for the online path is training/serving skew by construction — the single most common way a correct pipeline produces a broken model." });

  K.flow(pres, { kicker: "Module 8 · Section 4", title: "Serving BI: the star schema and why it reconciles",
    stepH: 2.35, steps: [
      { h: "gold.fact_trip", t: "One row per trip: fare_sar, distance_km, duration_min, surge_multiplier, plus foreign keys. The measurable events, at a fine grain.", color: P.gold },
      { h: "Conformed dimensions", t: "dim_driver · dim_vehicle · dim_zone · dim_date. ONE of each, shared by every fact. Denormalised, named for humans.", color: P.silver },
      { h: "Pre-aggregated marts", t: "gold.zone_hourly_demand and gold.driver_daily sit on top for the hottest dashboards — partitioned, ZORDERed, compacted.", color: P.bronze },
      { h: "PDPL-safe views", t: "The serving boundary masks or aggregates personal data. Raw rider_id and precise GPS never leave gold.", color: P.teal },
    ],
    note: "Conformed dimensions are what make numbers reconcile ACROSS dashboards — one dim_date, one dim_driver. A second, non-conformed dim_date is the Day 1 two-tier divergence, rebuilt inside the gold layer." });

  K.table(pres, { kicker: "Module 8 · Section 5", title: "Three serving patterns",
    head: ["Pattern", "How", "Best for", "The trade-off"],
    widths: [2.3, 3.5, 3.1, 3.19], rowH: 0.62, fs: 11.5,
    rows: [
      ["Direct Lakehouse", "Query gold Delta with Spark, Trino or Databricks SQL", "Analysts, batch ML, moderate concurrency", "Simple, one copy; may lag at very high concurrency"],
      ["Materialised mart", "Pre-aggregated and ZORDERed gold tables", "Hot dashboards", "Fast; must be refreshed as a DAG task"],
      ["External serving store", "Copy the latest slice to Redis, a warehouse or an OLAP engine", "Millisecond online features; thousands of concurrent BI users", "Fastest — but a SECOND COPY, with consistency and cost implications"],
    ],
    note: "Do not reintroduce the two-tier problem casually. An external store is justified by a measured latency or concurrency requirement, and when used it must be a derived, consistently refreshed copy of gold — never an independently transformed one." });

  K.bullets(pres, { kicker: "Module 8 · Section 6", title: "Six mistakes — each one is in the Lab 8 starter",
    rowH: 0.8, items: [
      { n: "1", h: "Feature leakage", t: "The current or future hour's demand as a feature. Great offline, terrible live.", color: P.alarm },
      { n: "2", h: "Re-implementing features in the online path", t: "Offline/online skew, guaranteed, and invisible until production.", color: P.alarm },
      { n: "3", h: "Serving raw rider IDs or precise GPS to a dashboard", t: "A PDPL violation at the boundary — and an automatic rubric flag.", color: P.alarm },
      { n: "4", h: "A non-conformed second dim_date", t: "Dashboards disagree; the two-tier divergence returns wearing a gold badge.", color: P.alarm },
      { n: "5", h: "An external serving copy with its own transformations", t: "The copy diverges from gold, and nobody can say which one is right.", color: P.alarm },
      { n: "6", h: "Dashboards querying an unoptimised gold table", t: "Slow and expensive — the Day 1 and Day 3 lessons, unlearned at the last step.", color: P.alarm },
    ] });

  K.lab(pres, { id: "8", title: "Serve Masar gold to AI and BI",
    meta: [["Duration", "50 minutes"], ["Checkpoint", "git checkout lab8-start"], ["Objective", "Two gold products from one silver: a leakage-free feature table and a conformed star schema"], ["Deliverable", "gold.eta_features + the BI star + an offline==online proof + the leakage drill"]],
    tasks: [
      "Build gold.eta_features at the trip grain with all 13 contract columns, using strictly-prior windows.",
      "MANDATORY DRILL — classify every column as VALID / STALE / LEAKAGE / UNAVAILABLE ONLINE and write one line of justification for each.",
      "Fix the leaking features, retrain, and report the honest metric alongside the inflated one.",
      "Build the BI star: gold.fact_trip with conformed dim_driver, dim_vehicle, dim_zone and dim_date; reconcile it against gold.zone_hourly_demand.",
      "Materialise the latest feature slice to Redis and prove offline == online for every key — then inject a divergence and prove the check catches it.",
    ],
    accept: [
      "Every feature column carries a class and a written justification.",
      "No feature window includes non-prior data — demonstrated, not asserted.",
      "The BI star reconciles against the demand mart with zero relative difference.",
      "Offline and online values match across every Redis key, and the consistency check fails when a divergence is injected.",
    ],
    notes: "The drill is the assessed part, not the code. A participant who ships a leakage-free table but cannot justify each classification has not met the objective." });
};
