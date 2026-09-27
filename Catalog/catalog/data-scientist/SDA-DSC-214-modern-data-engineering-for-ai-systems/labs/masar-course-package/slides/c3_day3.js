const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "DAY 3", title: "The Lakehouse\ntable",
    sub: "Delta Lake is the technical heart of the course: the transaction layer that turns Masar's Parquet files into a table you can trust, audit and rewind.",
    items: ["The transaction log", "Schema enforcement and evolution", "MERGE: upserts, CDC, compliant deletes", "Time travel", "Maintenance and the small-files problem"] });

  K.flow(pres, { kicker: "Module 4 · Section 1", title: "A Delta table is Parquet plus an ordered log",
    lead: "Each commit is an atomic record of ACTIONS: which files were added, which were removed, plus schema and statistics.",
    stepH: 2.45, steps: [
      { h: "Data files", t: "part-0000….snappy.parquet\npart-0001….snappy.parquet\n\nOrdinary Parquet. Any engine can read them. Nothing here says which of them are current.", color: P.silver },
      { h: "_delta_log/", t: "00000000000000000000.json\n00000000000000000001.json\n…\n\nOrdered commit files. Each one lists add and remove actions for exactly one transaction.", color: P.bronze },
      { h: "Checkpoints", t: "00000000000000000010.checkpoint.parquet\n\nPeriodic snapshots of the replayed state so readers do not replay thousands of JSON commits.", color: P.gold },
      { h: "The table state", t: "= replay the log to version v.\n\nThat single sentence is the whole trick. Everything else in this module follows from it.", color: P.teal },
    ],
    note: "Instructor demo: open a real _delta_log/*.json live and read the add and remove actions aloud. Six minutes here saves twenty later — seeing the log demystifies the entire module." });

  K.cards(pres, { kicker: "Module 4 · Section 1", title: "How the log delivers ACID on object storage",
    cols: 4, cardH: 2.55, cards: [
      { n: "A", h: "Atomicity", t: "A write is ONE commit. Either the commit file appears — and all of its file-adds become visible at once — or it does not. There is no half-written table, ever.", color: P.bronze },
      { n: "C", h: "Consistency", t: "Schema and CHECK constraints are validated before a commit is accepted. A source that suddenly sends fare_sar as a string fails loudly at the silver boundary.", color: P.silver },
      { n: "I", h: "Isolation", t: "Readers see a consistent snapshot — the log up to version v. A concurrent writer adding v+1 does not disturb them. This is snapshot isolation.", color: P.gold },
      { n: "D", h: "Durability", t: "Commits and data both live in durable object storage. There is no separate metadata service to lose, and no state that exists only in a running process.", color: P.teal },
    ],
    note: "Concurrency is optimistic: a writer reads the current version, prepares its changes, then attempts to commit as the next version. If someone got there first, it retries against the new state. That is why concurrent streaming and batch writes to Masar's trips table do not corrupt it." });

  K.twoCol(pres, { kicker: "Module 4 · Section 2", title: "Enforce by default. Evolve on purpose.",
    left: { h: "Schema enforcement — the default", color: P.teal, sub: "The guarantee a raw lake lacks",
      items: [
        "A write whose columns or types do not match the table is REJECTED, not silently coerced.",
        "This is the single property that stops a lake becoming a swamp.",
        "For Masar: a source that starts sending fare_sar as a string fails at the silver boundary instead of poisoning every downstream feature.",
        "Add CHECK constraints (fare_sar > 0, dropoff_ts >= pickup_ts) so the table validates itself on every write.",
      ] },
    right: { h: "Schema evolution — opt-in and audited", color: P.bronze, sub: "When change is intended, not discovered",
      items: [
        "mergeSchema / on_schema_change='append_new_columns' adds genuinely new columns.",
        "Type widening and column renames are explicit operations, logged as metadata commits.",
        "The principle: schema changes are EVENTS you decide and record — never accidents you find in production.",
        "The limit you must remember: enforcement checks TYPES. It cannot see that the meaning of a value changed. Hold that thought until tomorrow afternoon.",
      ] },
    note: "That last bullet is the seed of the signature incident. Plant it here on Day 3; harvest it in CS-11.",
    notes: "Deliberately foreshadow CS-11 here. When participants reach the incident and realise the schema check passed, this slide is what they will remember." });

  K.bullets(pres, { kicker: "Module 4 · Section 3", title: "MERGE — three Masar patterns, one operation",
    lead: "MERGE INTO … USING … ON … WHEN MATCHED … WHEN NOT MATCHED. Atomic, idempotent on a key, and therefore safe to retry.",
    rowH: 1.15, items: [
      { n: "1", h: "Correction upsert", t: "A re-scored or corrected trip updates its row in place, keyed on trip_id. Running the correction batch twice changes nothing the second time — that is the definition of a safe retry.", color: P.bronze },
      { n: "2", h: "CDC apply", t: "A stream of change events carrying insert / update / delete flags is merged to keep silver in sync with an operational source, without ever rebuilding the table.", color: P.silver },
      { n: "3", h: "Compliant delete (PDPL)", t: "DELETE FROM silver.trips WHERE rider_id = :id removes a data subject's rows atomically, with an auditable commit — and, after VACUUM passes the retention window, physically from history too.", color: P.gold },
    ],
    note: "Because MERGE is atomic and keyed, it is the backbone of every idempotent pipeline in this course. Module 3's dbt incremental merge is this operation, seen from above." });

  K.code(pres, { kicker: "Module 4 · Section 4", title: "Time travel — audit, reproducibility, recovery",
    lang: "sql / python",
    fs: 11,
    code: `-- what did this table contain when the report was filed?
SELECT * FROM silver_trips VERSION   AS OF 42;
SELECT * FROM silver_trips TIMESTAMP AS OF '2026-06-15';

-- what changed, and who changed it?
DESCRIBE HISTORY silver_trips;

-- undo a bad MERGE
RESTORE TABLE silver_trips TO VERSION AS OF 41;

# reproduce a training set exactly
df = (spark.read.format("delta")
        .option("versionAsOf", model_card["delta_version"])
        .load("lakehouse/gold/eta_features"))`,
    points: [
      "AUDIT — prove what a regulatory report was computed from on its filing date. For many compliance teams this alone justifies Delta.",
      "REPRODUCIBILITY — retrain a model on the exact feature-table version used originally. The antidote to “the numbers changed and we do not know why”.",
      "RECOVERY — a bad MERGE is undone with one statement, against the version you can name.",
      "Bounded by retention: you can travel back only as far as VACUUM has not pruned. That makes retention a governance decision, not a storage one.",
    ] });

  K.chart(pres, { kicker: "Module 4 · Section 5", title: "The small-files problem, and what OPTIMIZE does to it",
    type: pres.ChartType.bar, showValue: true, labelPos: "outEnd",
    colors: [P.alarm, P.teal],
    data: [{ name: "Files in silver.trips", labels: ["Before OPTIMIZE", "After OPTIMIZE + ZORDER"], values: [214, 9] }],
    opts: { valAxisMaxVal: 240, valAxisMinVal: 0, valAxisMajorUnit: 40, barGapWidthPct: 110, varyColors: true },
    side: { h: "Three maintenance tools", items: [
      "OPTIMIZE — compacts many small files into fewer right-sized ones (roughly 128 MB–1 GB). Average file size on this table: 3 MB → 71 MB.",
      "ZORDER BY (city, pickup_ts) — co-locates related data within files so data skipping prunes more aggressively. Query time: 18 s → 4 s.",
      "VACUUM — physically deletes files no longer referenced by the log and older than the retention window (default 7 days).",
      "Streaming sinks recreate this problem every day. Schedule OPTIMIZE as a DAG task, not as a heroic intervention.",
    ] },
    takeaway: "Measured on the Masar silver.trips lab table. Record YOUR numbers in BENCHMARKS.md — the capstone rubric asks for the file-count reduction you achieved." });

  K.twoCol(pres, { kicker: "Module 4 · Section 5", title: "The retention tension",
    lead: "VACUUM reclaims storage by destroying the history behind it. Both directions have a real cost.",
    left: { h: "Vacuum aggressively", color: P.alarm, sub: "RETAIN 24 HOURS, or the notorious RETAIN 0",
      items: [
        "Saves storage immediately.",
        "Destroys the audit trail: you can no longer prove what the table contained last week.",
        "Breaks reproducibility: model cards pointing at a version become unreadable.",
        "RETAIN 0 HOURS can break concurrent readers mid-query — which is why the safety check exists and why disabling it is an anti-pattern flag on the capstone rubric.",
      ] },
    right: { h: "Vacuum conservatively", color: P.gold, sub: "RETAIN 30 DAYS or more",
      items: [
        "Preserves audit and reproducibility.",
        "Costs storage — though at object-storage prices this is usually the smaller number.",
        "Can retain personal data a PDPL erasure was supposed to remove: a DELETE only tombstones until VACUUM passes the retention window.",
        "The obligation and the audit trail pull in opposite directions. Document the decision and its owner.",
      ] },
    note: "What the rubric asks for is not a particular number. It asks for a JUSTIFIED number: retention chosen, reasoning written down, owner named." });

  K.bullets(pres, { kicker: "Module 4 · Section 6", title: "Six mistakes — each one is in the Lab 4 starter",
    rowH: 0.8, items: [
      { n: "1", h: "VACUUM … RETAIN 0 HOURS to “save space”", t: "Destroys time travel, can break concurrent readers, and is blocked by default for good reason.", color: P.alarm },
      { n: "2", h: "Over-partitioning by trip_id", t: "Millions of one-row files — the small-files problem, self-inflicted, on the primary key.", color: P.alarm },
      { n: "3", h: "Writing raw Parquet next to a Delta table's files", t: "The log no longer describes reality. Never hand-edit files under a Delta table.", color: P.alarm },
      { n: "4", h: "overwrite where a MERGE was needed", t: "Silently loses rows a concurrent writer had committed.", color: P.alarm },
      { n: "5", h: "Assuming DELETE frees storage or erases history", t: "It tombstones. Nothing is physically gone until VACUUM passes retention — which matters for both cost and PDPL.", color: P.alarm },
      { n: "6", h: "Ignoring OPTIMIZE on a streaming sink", t: "Read performance decays a little every day until one morning the dashboard times out.", color: P.alarm },
    ],
    note: "Activity ACT-05: participants physically enact the transaction log — commits, two concurrent writers, and a time-travel read. It is the fastest way to make optimistic concurrency intuitive." });

  K.lab(pres, { id: "4", title: "Delta Lake — ACID, MERGE, time travel, maintenance",
    meta: [["Duration", "Two 50-minute blocks (4a convert · 4b operate)"], ["Checkpoint", "git checkout lab4-start / lab4b-start"], ["Objective", "silver.trips as a constrained Delta table you can correct, audit and maintain"], ["Deliverable", "Constrained Delta table + time-travel evidence + OPTIMIZE benchmark"]],
    tasks: [
      "4a — write silver.trips as Delta with an enforced schema and CHECK constraints; then try to write a violating row and read the error.",
      "4a — open _delta_log/00000000000000000000.json and identify the add actions, the schema, and the statistics.",
      "4b — MERGE the corrections fixture on trip_id. Run it twice and prove the second run changes zero rows.",
      "4b — query VERSION AS OF the pre-correction version and diff the two; then demonstrate one PDPL erasure with an auditable commit.",
      "4b — run OPTIMIZE with ZORDER, record the file-count reduction, and set a VACUUM retention you can defend in one sentence.",
    ],
    accept: [
      "The table rejects a schema violation and a CHECK violation, and you can show both errors.",
      "The MERGE is idempotent — a second identical run reports zero rows affected.",
      "You can name the version number that a specific report was computed from.",
      "OPTIMIZE reduced file count measurably and the number is recorded in BENCHMARKS.md.",
    ],
    notes: "Lab 4b is one of the two most overrun-prone labs. Publish lab4b-start and hold the line on time; the OPTIMIZE step is the one people skip, and it is the one the rubric measures." });

  K.cards(pres, { kicker: "Case study CS-04 + PA-1", title: "Day 3 assessment: reproduce a disputed report",
    cols: 3, cardH: 2.45, cards: [
      { h: "CS-04 — “Aman” Payments", t: "A regulator asks what a settlement table contained three weeks ago. The team can produce the report but cannot prove the data behind it. Time travel exists — but VACUUM ran with a 24-hour retention every night to save storage.", color: P.bronze },
      { h: "PA-1 — 30 minutes, scored", t: "You are given a Delta table VACUUMed with RETAIN 0 HOURS and a non-idempotent MERGE. Restore correctness: fix retention, make the upsert idempotent, and prove time travel plus a clean second run.", color: P.teal },
      { h: "How it is scored", t: "Diagnosis notes 40% · fixes 40% · verification evidence 20%. The evidence is the part people forget: a claim without a transcript scores nothing.", color: P.gold },
    ],
    note: "PA-1 is deliberately a diagnosis exercise, not a coding exercise. Participants who start typing before reading DESCRIBE HISTORY lose the band." });

  K.statement(pres, { kicker: "Day 3 · close",
    text: "The table can now defend itself.\nTomorrow the data arrives faster than you can batch it.",
    size: 30,
    sub: "You have ACID, constraints, idempotent corrections and an audit trail.\nDay 4 adds the two things that break all of it: continuous arrival, and data that is wrong in ways no constraint can see." });
};
