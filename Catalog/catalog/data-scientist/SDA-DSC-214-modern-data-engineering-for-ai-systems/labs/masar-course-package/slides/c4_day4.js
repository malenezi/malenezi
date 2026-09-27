const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "DAY 4", title: "Real-time\nand trust",
    sub: "Continuous arrival, and the controls that decide whether what arrives can be believed.",
    items: ["M5 — Streaming and event-driven architectures", "CS-10 — LinkedIn and Kafka: a design exercise", "Lab 5 — stream GPS into the Lakehouse", "M6 — Quality, observability, governance", "Lab 6 — the quality gate"] });

  K.table(pres, { kicker: "Module 5 · Section 1", title: "Batch and streaming are not rivals",
    lead: "They are tools for different latency requirements. Default to batch; reach for streaming only when a decision genuinely needs fresh data.",
    head: ["", "Batch", "Streaming"],
    widths: [2.4, 4.85, 4.84], rowH: 0.5, fs: 12,
    rows: [
      ["Data", "Bounded, at rest", "Unbounded, in motion"],
      ["Latency", "Minutes to hours", "Milliseconds to seconds"],
      ["Cost and complexity", "Lower — no state, no ordering, no checkpoints", "Higher — state, ordering, failure semantics, checkpoints"],
      ["Masar fit", "Historical trips, feature builds, the morning report", "GPS pings, trip-state events, live zone demand and surge"],
      ["What goes wrong", "You find out tomorrow", "You find out in production, at 3 a.m., after a restart"],
    ],
    note: "Structured Streaming lets the SAME Spark and Delta code serve both paths — which is why this course teaches one engine for both, and why the streaming lab reuses the bronze table you already built." });

  K.bullets(pres, { kicker: "Module 5 · Section 2", title: "Kafka is a durable, append-only log",
    lead: "Not a queue. A log you can rewind — much like Delta history, for events in motion.",
    rowH: 0.86, items: [
      { n: "T", h: "Topic", t: "A named stream of events: masar.gps.raw, masar.trip.events.", color: P.bronze },
      { n: "P", h: "Partition", t: "A topic is split for parallelism. Events within a partition are strictly ordered; across partitions they are not. The partition KEY decides where an event lands — key by vehicle_id or trip_id and you get per-entity ordering.", color: P.silver },
      { n: "O", h: "Offset", t: "Each event's position in its partition. Consumers track offsets to know what they have read — and Spark checkpoints them, which is where exactly-once comes from.", color: P.gold },
      { n: "G", h: "Consumer group", t: "Members share partitions so they process in parallel without overlap. Add a second group and you get a second independent reader of the same events, at no cost to the first.", color: P.teal },
      { n: "R", h: "Retention", t: "Kafka keeps events for a configured window, so consumers can replay. A bad window can be reprocessed rather than lost.", color: P.bronze },
    ],
    note: "The point is decoupling: the GPS emitter does not know or care who consumes pings. Streaming ingest, a live-demand service and an alerting job all read the same topic independently. That is event-driven architecture in one sentence." });

  K.cards(pres, { kicker: "Case study CS-10 · design exercise · 45 minutes", title: "LinkedIn and Kafka — design it, do not demo it",
    lead: "Kafka originated at LinkedIn as a central messaging backbone connecting loosely coupled systems, at extreme volume. Teams design Masar's equivalent; they do not write producers and consumers.",
    cols: 4, cardH: 2.55, cards: [
      { h: "The payload", t: "Every Masar vehicle emits every 5 seconds:\nvehicle_id · latitude · longitude · speed · heading · timestamp · trip_id", color: P.bronze },
      { h: "Round 1 — late events", t: "A phone was in a tunnel for four minutes. What is your watermark, and what does it cost you in state and in delay?", color: P.silver },
      { h: "Round 2 — duplicates", t: "The producer retried after a timeout that had actually succeeded. What is your dedup key, over what window, and where in the pipeline does it run?", color: P.gold },
      { h: "Round 3 — out of order", t: "Events arrive with timestamps that go backwards. Which aggregations break, and which clock were you using without realising it?", color: P.alarm },
    ],
    note: "This is pedagogically far stronger than teaching Kafka producers and consumers. Teams present a design; the scoring sheet in CS-10 rewards explicit trade-offs, not correct answers." });

  K.flow(pres, { kicker: "Case study CS-10", title: "The target architecture teams must justify",
    stepH: 2.6, steps: [
      { h: "Vehicles", t: "~1 ping / 5 s / vehicle\n15M events per day\nKeyed by vehicle_id", color: P.silver },
      { h: "Kafka", t: "masar.gps.raw\nPartitioned by vehicle_id → per-vehicle ordering\nRetention long enough to replay a bad day", color: P.bronze },
      { h: "Structured Streaming", t: "readStream → parse → writeStream\nOne dedicated checkpoint\nTrigger sized against the small-files cost", color: P.teal },
      { h: "bronze.gps_events", t: "Delta, append-only\nAS RECEIVED\nNo dedup, no unit conversion — that is the rule from CS-09", color: P.bronze },
      { h: "silver.vehicle_positions", t: "Dedup on event_id\nEvent-time watermark\nConformed units\nQuality-gated", color: P.silver },
    ],
    note: "…then the fan-out: silver.vehicle_positions feeds BOTH the ETA feature pipeline and the operations alerting consumer. Two consumers, one governed source — the Module 8 principle, arriving early." });

  K.cards(pres, { kicker: "Module 5 · Section 3", title: "Delivery semantics — and why exactly-once is the hard one",
    cols: 3, cardH: 2.3, cards: [
      { h: "At-most-once", t: "Events may be lost, never duplicated. Fire and forget. Acceptable for a metrics ping; unacceptable for a trip record.", color: P.silver },
      { h: "At-least-once", t: "Events are never lost, but may be duplicated — a retry after a failure that had actually succeeded. This is what Kafka gives you on its own.", color: P.bronze },
      { h: "Exactly-once", t: "Each event effectively processed once: no loss, no duplication. Not a source property — an END-TO-END property.", color: P.teal },
    ],
    note: "Do not chase exactly-once in the source alone. It is achieved by combining an at-least-once, replayable source with an idempotent, transactional sink." });

  K.statement(pres, { kicker: "Module 5 · the elegant part", size: 29,
    text: "Structured Streaming + Delta\ngives you exactly-once for free.",
    sub: "Spark records the exact Kafka offsets processed in each CHECKPOINT.\nDelta commits that batch's output ATOMICALLY.\n\nIf the job crashes and restarts, it resumes from the checkpointed offset, and the half-done Delta batch either committed fully or not at all.\nNo duplicates. No loss. Idempotency (Day 2) and ACID (Day 3) paying off again.",
    notes: "This is the module's thesis. In Lab 5 participants kill the job mid-stream and restart it, then count rows. The count is unchanged. Never skip that observation, even if you have to run the lab as a guided demo." });

  K.twoCol(pres, { kicker: "Module 5 · Section 4", title: "Two clocks, and the one that is correct",
    left: { h: "Processing time", color: P.alarm, sub: "When the system received it",
      items: [
        "Easy: it is always available, and it never goes backwards.",
        "Wrong for anything that asks WHEN SOMETHING HAPPENED.",
        "A batch of pings released from a tunnel all carry the same processing time — so a five-minute demand window shows a spike that never occurred.",
        "Aggregating on processing time is mistake #2 in the Lab 5 starter, and it is deliberately invisible until you look at a specific window.",
      ] },
    right: { h: "Event time", color: P.teal, sub: "When the event actually happened",
      items: [
        "The GPS ping's own timestamp. What every business question is actually about.",
        "Requires handling lateness: network delay, device buffering, retries.",
        "WATERMARK = “I will wait up to N minutes for late events; beyond that I finalise the window and drop stragglers.”",
        "It bounds the state Spark must keep — you cannot hold every window open forever — while tolerating realistic lateness.",
      ] },
    note: "Choosing the watermark is a trade-off with no default answer: longer tolerates more lateness but holds more state and delays results; shorter is cheaper and drops more data. For Masar GPS a few minutes is typical. Activity ACT-07 makes teams triage twelve late events against a watermark they chose themselves." });

  K.code(pres, { kicker: "Module 5 · Section 5", title: "The ingestion pattern — simple, and robust because of it",
    lang: "python · pyspark", fs: 10,
    code: `raw = (spark.readStream.format("kafka")
       .option("kafka.bootstrap.servers", BROKER)
       .option("subscribe", "masar.gps.raw")
       .option("startingOffsets", "earliest")
       .load())

parsed = raw.select(
    from_json(col("value").cast("string"), GPS_SCHEMA).alias("e"))

events = (parsed.select("e.*")
     .withColumn("_ingested_at", current_timestamp())
     .withColumn("_source_topic", lit("masar.gps.raw")))

(events.writeStream
   .format("delta")
   .outputMode("append")
   .option("checkpointLocation",
           "lakehouse/_checkpoints/gps_bronze")   # ONE per query
   .trigger(processingTime="30 seconds")
   .start("lakehouse/bronze/gps_events"))`,
    points: [
      "readStream / writeStream are the streaming analogues of read / write — almost the same DataFrame code as batch.",
      "checkpointLocation is MANDATORY and must be dedicated. Never share one between two queries; losing it means reprocessing or duplication.",
      "Trigger sizes the micro-batch. Too small and you manufacture the small-files problem from Day 3 — schedule OPTIMIZE on the sink.",
      "Land raw into bronze, refine in batch. Heavy transforms do not have to be streaming just because the arrival is.",
    ] });

  K.lab(pres, { id: "5", title: "Stream GPS pings into the Lakehouse",
    meta: [["Duration", "50 minutes"], ["Checkpoint", "git checkout lab5-start"], ["Objective", "Exactly-once GPS ingestion into Delta bronze, then event-time demand with a watermark"], ["Deliverable", "bronze.gps_events + silver.vehicle_positions + a kill/restart proof"]],
    tasks: [
      "docker compose up -d kafka redis, then run the GPS producer against masar.gps.raw keyed by vehicle_id.",
      "Build the Structured Streaming ingest into bronze.gps_events with its own dedicated checkpoint.",
      "KILL the job mid-stream. Restart it. Count rows. Prove zero duplicates — this is the module's thesis made visible.",
      "Build silver.vehicle_positions: dedup on event_id within the watermark, conform units, and handle the out-of-order and late fixtures in data/fixtures/late_pings/.",
      "Compute event-time windowed zone demand with a watermark, then re-run it on processing time and compare the two windows side by side.",
    ],
    accept: [
      "Restarting the query produces zero duplicate rows, and you have the row counts to show it.",
      "The event-time aggregation attributes late pings to the correct window; the processing-time version does not.",
      "One dedicated checkpoint per query — no sharing.",
      "You can state your watermark and defend the number.",
    ],
    notes: "Lab 5 is the boot-time risk of the whole week: pre-pull the Kafka image, free port 9092, and have the compose healthcheck ready. If the cohort is weak, run the exactly-once step as a guided demo — but never skip the kill/restart OBSERVATION." });

  K.divider(pres, { eyebrow: "MODULE 6", title: "Quality, observability\nand governance",
    sub: "A pipeline that runs is not the same as a pipeline you can trust. This module makes trust explicit.",
    items: ["The data-quality pyramid", "Quality as code", "Fail-fast vs quarantine", "The four observability signals", "PDPL as a first-class constraint"] });

  K.table(pres, { kicker: "Module 6 · Section 1", title: "The data-quality testing pyramid",
    lead: "Cheap checks run on every batch at the promotion boundary. Expensive statistical checks run on a schedule.",
    head: ["Level", "What it checks", "Masar example", "When"],
    widths: [2.1, 3.3, 4.6, 2.09], rowH: 0.5, fs: 11.5,
    rows: [
      ["Schema", "Columns, types, nullability", "trip_id present; fare_sar numeric", "Every load"],
      ["Constraint / range", "Value bounds, sets, uniqueness", "fare_sar > 0 · city in the KSA set · unique trip_id", "Every load"],
      ["Referential", "Keys resolve to dimensions", "Every driver_id exists in silver.drivers", "Every load"],
      ["Distribution", "Statistical shape versus a baseline", "Mean fare within ±20% of last week; null rates stable", "Daily"],
      ["Reconciliation", "Totals match a source of truth", "Daily trip count matches the operations system", "Daily"],
    ],
    note: "Enforce quality where data is PROMOTED — bronze to silver — so bad data never reaches a consumer. The bottom three catch broken rows; the top two catch broken meaning. Remember which is which." });

  K.twoCol(pres, { kicker: "Module 6 · Section 3", title: "Quality gates are decisions, not alarms",
    lead: "When a batch fails expectations there are two correct responses, chosen by severity. Choosing neither is the actual mistake.",
    left: { h: "Fail-fast — block the batch", color: P.alarm, sub: "Promoting anything is worse than promoting nothing",
      items: [
        "Null or duplicate trip_id — the business key is unusable.",
        "The schema does not match the contract.",
        "Volume collapsed to a fraction of expectation — the feed is broken, not the data.",
        "Reconciliation against the operations system fails by more than tolerance.",
      ] },
    right: { h: "Quarantine — isolate the rows", color: P.gold, sub: "Blocking the batch would needlessly starve consumers",
      items: [
        "A small fraction of trips with a bad dropoff_geohash.",
        "A handful of out-of-range fares among 42,000 valid ones.",
        "Route failures to silver.trips_quarantine, promote the good rows, record both, alert proportionately.",
        "Quarantine is not a bin. Somebody owns it, and unresolved rows age into an alert of their own.",
      ] },
    note: "The anti-pattern that fails the capstone rubric: alerting without acting — a failing check emails somebody and promotes the bad data anyway. Activity ACT-08 has teams rule on ten real defect scenarios from the shipped fixtures." });

  K.cards(pres, { kicker: "Module 6 · Section 4", title: "Four signals row-level checks cannot see",
    lead: "Quality checks the content. Observability checks the pipeline's health over time.",
    cols: 4, cardH: 2.65, cards: [
      { n: "1", h: "Freshness", t: "When did this table last update? Alert when max(_ingested_at) is older than the SLA. A stale silver.trips means an upstream break — and every row in it is still individually valid.", color: P.bronze },
      { n: "2", h: "Volume", t: "How many rows arrived versus expected? A sudden drop is a feed outage; a spike is duplication. Both are invisible to every row-level test you have.", color: P.silver },
      { n: "3", h: "Schema drift", t: "Did a source add, rename or retype a column? Detect and alert BEFORE enforcement rejects a whole batch at 3 a.m.", color: P.gold },
      { n: "4", h: "Distribution drift", t: "Did the statistical shape shift — mean fare, null rates, category mix? Drift is the leading indicator of model degradation, and the only one of the four that catches a change in MEANING.", color: P.alarm },
    ],
    note: "Together these turn “the model got worse and we do not know why” into “the fare_sar distribution shifted on 12 June when the source changed currency handling.” Hold on to signal 4. You will need it this afternoon." });

  K.bullets(pres, { kicker: "Module 6 · Section 5", title: "Governance in four parts",
    rowH: 0.94, items: [
      { n: "1", h: "Catalog", t: "A searchable registry of tables, owners, descriptions and classifications. Nobody should have to ask “does this table exist and can I trust it?”", color: P.bronze },
      { n: "2", h: "Lineage", t: "Source → bronze → silver → gold → dashboard and feature. Needed for impact analysis (“if I change stg_trips, what breaks?”) and for audit (“where did this KPI come from?”). dbt docs and Delta history supply most of it for free.", color: P.silver },
      { n: "3", h: "Access control", t: "Least privilege at table and ideally column level: analysts see gold, data scientists see silver, raw rider IDs and precise GPS are restricted or masked.", color: P.gold },
      { n: "4", h: "Classification", t: "rider_id, device_id and lat/lon are personal data. Classification is a table property enforced automatically — not a spreadsheet somebody maintains.", color: P.teal },
    ],
    note: "Most of this comes free from what you already built: dbt docs supplies lineage, Delta history supplies the audit trail, and the medallion contracts supply the access boundaries. Governance is data-in, not paperwork." });

  K.cards(pres, { kicker: "Module 6 · Section 5", title: "Saudi PDPL as a first-class engineering constraint",
    lead: "Governance is where PDPL stops being a legal abstraction and becomes table policies, masking, and a retention job on a schedule.",
    cols: 3, cardH: 2.4, cards: [
      { h: "Lawful basis and purpose limitation", t: "Personal data is collected for a stated purpose. “We might need it later” is not a purpose. This is an architecture constraint, applied at ingestion design time.", color: P.bronze },
      { h: "Data minimisation", t: "Do not keep precise GPS if a geohash suffices for the feature. The safest personal data is the data you never collected — or already deleted.", color: P.silver },
      { h: "Retention limits", t: "Delete when the purpose ends. This ties directly to VACUUM retention from Day 3, which is why retention is one decision, not two.", color: P.gold },
      { h: "Data-subject rights", t: "Access and erasure. Erasure is the MERGE DELETE from Module 4 plus a VACUUM that actually passes the retention window — with an auditable commit as the evidence.", color: P.teal },
      { h: "Cross-border transfer", t: "Controls on where data physically goes. Relevant the moment a managed service or an online store sits in another region.", color: P.bronze },
      { h: "The rule for this course", t: "Rider identifiers and precise GPS are personal data from Day 1, not a Day 4 afterthought. Never emit raw rider_id into BI output or the online store — it is an automatic rubric flag.", color: P.alarm },
    ] });

  K.lab(pres, { id: "6", title: "Quality gate and governance on silver.trips",
    meta: [["Duration", "50 minutes"], ["Checkpoint", "git checkout lab6-start"], ["Objective", "A gate that ACTS: fail-fast on integrity, quarantine on partial, with governance controls applied"], ["Deliverable", "GX suite + quarantine table + data docs + a PDPL retention job"]],
    tasks: [
      "Write a Great Expectations suite for silver.trips: schema, ranges, uniqueness, referential integrity to silver.drivers.",
      "Wire the gate into promotion: fail-fast on null or duplicate trip_id, quarantine out-of-range rows into silver.trips_quarantine.",
      "Run the dirty batch fixture through it. Confirm the good rows promote, the bad rows quarantine, and both are recorded.",
      "Add the four observability checks — freshness, volume, schema drift, distribution drift — and make one of them fire.",
      "Classify every column as public / internal / personal / sensitive-personal, then run the PDPL retention and erasure job and keep the commit as evidence.",
    ],
    accept: [
      "The gate BLOCKS on an integrity failure and QUARANTINES on a partial one — demonstrated, not described.",
      "Data docs are generated and readable by a non-engineer.",
      "The erasure request in data/fixtures/erasure_request/ is honoured with an auditable Delta commit.",
      "A drift check fires on a batch where every individual row is valid.",
    ] });

  K.statement(pres, { kicker: "Day 4 · before we close", size: 30,
    text: "Every control you built today\nchecks that values are well-formed.",
    sub: "Schema enforcement checks types. Range checks check bounds. Referential checks check keys.\n\nNone of them checks whether a number still MEANS what it meant yesterday.\n\nTomorrow morning starts with an incident.",
    notes: "End Day 4 here. Do not explain further. The overnight gap is deliberate — participants should arrive on Day 5 already suspicious." });
};
