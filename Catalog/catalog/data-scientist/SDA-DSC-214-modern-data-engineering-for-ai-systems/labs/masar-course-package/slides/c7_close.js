const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "CAPSTONE", title: "The Masar\nMini-Lakehouse",
    sub: "A production data platform for a Saudi mobility operator. Everything you built in Labs 1–8 is a component; the capstone is the integration plus your own extensions.",
    items: ["The mandate", "Eight mandatory requirements", "Milestones M-A to M-E", "The rubric", "Six-minute demo"] });

  K.statement(pres, { kicker: "Capstone · the mandate", size: 28,
    text: "Deliver a Mini-Lakehouse that\nboth teams can trust —\nbecause the platform proves its own\nquality, freshness and governance.",
    sub: "You are the data platform engineer for Masar. The analytics team hands you raw feeds — batch trips and drivers, streaming GPS —\nand two demands: an AI feature service for an ETA and demand model, and an operations BI dashboard leadership reviews every morning." });

  K.table(pres, { kicker: "Capstone · mandatory scope", title: "Eight requirements, eight outcomes",
    head: ["#", "Requirement", "Evidence the grader looks for", "LO"],
    widths: [0.5, 3.5, 7.0, 1.09], rowH: 0.5, fs: 11,
    rows: [
      ["1", "Medallion architecture", "Bronze append-only with lineage → silver conformed → gold marts and features. Contracts documented and enforced. No layer bypassed.", "1, 7"],
      ["2", "Compute–storage discipline", "Object-storage-style layout · BENCHMARKS.md scan and cost analysis · gold OPTIMIZEd and ZORDERed with measured file-count reduction.", "2"],
      ["3", "ELT pipeline", "Staging → silver, incremental merge on trip_id with a lookback window · source freshness + ≥ 6 tests · a demonstrated late-arrival backfill.", "3"],
      ["4", "Delta Lake", "Constrained Delta · idempotent MERGE · time-travel audit · OPTIMIZE/VACUUM with justified retention · one PDPL erasure demonstrated.", "4"],
      ["5", "Streaming", "Kafka → Structured Streaming → Delta bronze, exactly-once with a dedicated checkpoint · kill/restart proof · event-time window with a watermark.", "5"],
      ["6", "Quality, observability, governance", "GX suite with fail-fast AND quarantine · freshness/volume/drift checks · PII classification + retention job · data docs as evidence.", "6"],
      ["7", "Orchestration", "The full medallion as one dependency-ordered idempotent DAG, one command, with a demonstrated recovery from an injected mid-DAG failure.", "7"],
      ["8", "Serving", "Point-in-time-correct features served offline and materialised online (consistency proven) · conformed star schema that reconciles · PDPL-safe serving view.", "8"],
    ],
    note: "Choose at least one extension: offline/online consistency in CI · a leakage-lint that fails the pipeline · a 7-day multi-city backfill · a second streaming consumer group · a Trino/Databricks-SQL direct-serve benchmark." });

  K.table(pres, { kicker: "Capstone · rubric", title: "100 points, platform graded first",
    head: ["Criterion", "Weight", "90–100%", "70–89%", "Below 70%"],
    widths: [2.85, 0.8, 3.15, 2.75, 2.54], rowH: 0.5, fs: 10,
    rows: [
      ["Architecture & contracts", "15", "Clean layers, contracts documented and enforced, no bypass", "Minor contract gap or one bypass", "Layers muddled, gold from bronze"],
      ["ELT & incrementality", "15", "Incremental merge + lookback, ≥ 6 tests, backfill proven", "Incremental works; thin tests", "Full-refresh only; late-arrival bug"],
      ["Delta Lake mastery", "15", "Constraints, idempotent MERGE, time travel, justified VACUUM, erasure", "Most present; retention thin", "No constraints; VACUUM misused"],
      ["Streaming", "15", "Exactly-once proven by kill/restart, watermark, checkpoint discipline", "Streams but dedup/watermark weak", "Duplicates on restart"],
      ["Quality & governance", "15", "Gate acts, observability fires, PII + PDPL retention", "Some gaps — alert-only, partial", "Alerts only; raw PII kept forever"],
      ["Orchestration & recovery", "15", "One-command idempotent DAG, clean failure recovery", "Runs; recovery partial", "Hand-run steps; no recovery"],
      ["Serving (AI + BI) & demo", "10", "PIT-correct, offline==online, conformed BI, PDPL-safe, crisp demo", "Works; leakage or reconciliation thin", "Leakage; online ≠ offline"],
    ],
    note: "Pass ≥ 70 · Distinction ≥ 90. Anti-pattern flags cap a criterion at 70%.",
    notes: "The six anti-pattern flags: feature leakage; non-idempotent gold; VACUUM RETAIN 0; alert-only quality gate; raw rider IDs in BI output; streaming without a dedicated checkpoint. Grade from the running platform and repository evidence first, demo second. Verify one claim live." });

  K.flow(pres, { kicker: "Capstone · the six-minute demo", title: "Five things to show, in this order",
    stepH: 2.5, steps: [
      { h: "1 · One command", t: "make pipeline. Show it run end to end. Say nothing while it runs — let the platform speak.", color: P.bronze },
      { h: "2 · Kill the stream", t: "Restart it. Show the row count is unchanged. This is the claim graders verify live most often.", color: P.silver },
      { h: "3 · Quarantine", t: "Push the dirty batch through the gate. Good rows promote, bad rows land in quarantine, both recorded.", color: P.gold },
      { h: "4 · Time travel", t: "Name a version, show what the table contained, and show the erasure commit.", color: P.teal },
      { h: "5 · Two consumers", t: "The BI star reconciling, and the feature table matching its online copy. Then the honest metric.", color: P.alarm },
    ],
    note: "Milestones: M-A bronze (end Day 2) · M-B silver + Delta (end Day 3) · M-C streaming + gate + governance (end Day 4) · M-D DAG + gold + serving (Day 5 H2–H3) · M-E demo (Day 5 H5)." });

  K.cards(pres, { kicker: "Wrap-up", title: "Every requirement traces to a module",
    cols: 4, cardH: 1.85, cards: [
      { h: "M1 → Medallion", t: "Layer contracts, bronze immutability, no bypass.", color: P.bronze },
      { h: "M2 → Economics", t: "BENCHMARKS.md, layout as a cost control.", color: P.bronze },
      { h: "M3 → ELT", t: "Incremental merge, lookback, tests, backfill.", color: P.silver },
      { h: "M4 → Delta", t: "Constraints, MERGE, time travel, maintenance, erasure.", color: P.silver },
      { h: "M5 → Streaming", t: "Exactly-once, checkpoints, watermarks.", color: P.teal },
      { h: "M6 → Trust", t: "Gate that acts, four observability signals, PDPL.", color: P.teal },
      { h: "M7 → Orchestration", t: "One idempotent DAG, recoverable, observable.", color: P.gold },
      { h: "M8 → Serving", t: "PIT correctness, offline==online, conformed BI.", color: P.gold },
    ],
    note: "Forward pointer: SDA-DSC-215 (Big Data Analytics with Spark) scales exactly this Lakehouse to enterprise volumes; SDA-DSC-313 builds advanced pipelines on the same substrate." });

  K.table(pres, { kicker: "Resources", title: "The core resource package",
    head: ["Resource", "What it is for", "Where it is used"],
    widths: [3.5, 5.6, 2.99], rowH: 0.48, fs: 11.5,
    rows: [
      ["DataTalksClub Data Engineering Zoomcamp", "The open-course benchmark: integrates dbt, Spark, Kafka, ingestion and project-based learning", "Reference for the whole course design"],
      ["NYC TLC Trip Record Data", "The real-world dataset behind the benchmark — large, messy, with anomalies and genuine schema changes over time; recent months in Parquet", "Optional real-data track; data/generators/nyc_tlc_prep.py"],
      ["Chicago TNP Trips", "Secondary rideshare dataset with an explicit privacy/aggregation story", "M6 governance discussion"],
      ["Delta Lake official tutorials and docs", "Authoritative reference for the transaction log, MERGE, time travel and maintenance", "Day 3"],
      ["LinkedIn's Kafka origin story", "The real-time architecture case: a central messaging backbone for loosely coupled systems at extreme volume", "CS-10, Day 4"],
      ["Great Expectations", "Quality as code — suites, validation results, data docs", "M6 and Lab 6"],
      ["Databricks / Microsoft medallion references", "The architecture benchmark for progressive refinement", "CS-09, Day 1"],
    ],
    note: "The Masar synthetic dataset is primary because it is controllable: every defect is injected deliberately, documented, and reproducible from a pinned seed. NYC TLC is the reality check." });

  K.statement(pres, { kicker: "Where we started, and where we finish", size: 30,
    text: "“What happens to Masar’s AI system\nif this part of the data platform fails?”",
    sub: "You can now answer that question for every layer: for landing, for the transform, for the table, for the stream, for the gate,\nfor the orchestration, and for the serving boundary.\n\nThat — not five tools — is what distinguishes SDA-DSC-214 from a generic data-engineering course.",
    notes: "Close by collecting: repository URLs, BENCHMARKS.md, GOVERNANCE.md, DECISIONS.md and the mini_lakehouse/ folder. Badge recommendations within five working days." });

  // ---------- appendix ----------
  K.divider(pres, { eyebrow: "APPENDIX", title: "Instructor\nreference",
    sub: "Timing, risk, and the numbers to expect from a healthy run.",
    items: ["Timing and pace control", "The ten most common participant issues", "Benchmark targets", "Discussion prompts"] });

  K.bullets(pres, { kicker: "Appendix", title: "Pace control — what to protect and what to cut",
    rowH: 0.86, items: [
      { n: "1", h: "Protect Lab 4 (Delta) and Lab 5 (streaming) at full length", t: "They are the two most overrun-prone sessions and the two the rubric weights most heavily. Compress M2 theory instead — the cost model lands through the lab.", color: P.gold },
      { n: "2", h: "Publish checkpoint tags before Day 1", t: "lab1-start … lab8-start, plus bad-batch and the sim-* branches. Anyone stuck fast-forwards with one command instead of losing a session.", color: P.bronze },
      { n: "3", h: "Hard rule: Mini-Lakehouse assembly starts on time", t: "Day 5 Hour 4 is immovable. Cut discussion, never build time.", color: P.alarm },
      { n: "4", h: "Reserve the leakage drill even when compressing", t: "It is the single most memorable lesson and it directly protects the capstone score.", color: P.teal },
      { n: "5", h: "If the cohort is weak", t: "Run streaming exactly-once as a guided demo rather than a solo lab — but never skip the kill/restart observation. It is the module's thesis made visible.", color: P.silver },
    ] });

  K.table(pres, { kicker: "Appendix", title: "The ten issues that actually happen",
    head: ["Issue", "Frequency", "Resolution"],
    widths: [4.3, 1.5, 6.29], rowH: 0.42, fs: 11,
    rows: [
      ["Java version / JAVA_HOME wrong for Spark", "High", "Pin Java 17; staff a floater in the first hour; hosted-notebook fallback ready"],
      ["Delta extension not configured", "High", "Always use get_spark(); verify spark.sql.extensions is set"],
      ["Kafka container will not start / port clash", "High", "Pre-pull images; free 9092; ship a compose healthcheck"],
      ["Streaming duplicates on restart", "Medium", "One dedicated checkpointLocation per query — the Module 5 lesson, learned the hard way"],
      ["Small files after streaming", "Medium", "Scheduled OPTIMIZE; teach it as maintenance, not as a fix"],
      ["dbt-spark connection / profile errors", "Medium", "Provide a working profiles.yml; run dbt debug before anything else"],
      ["Feature leakage passes unnoticed", "Medium", "Make the leakage drill mandatory; add the leakage-lint extension"],
      ["PySpark on Apple Silicon quirks", "Medium", "Use the provided arm64-compatible images; document JAVA_HOME"],
      ["Event time vs processing time confusion", "Medium", "Run the Human Kafka activity and the watermark clinic — physical, not verbal"],
      ["VACUUM removes nothing / RETAIN 0 blocked", "Low", "Explain the 7-day safety window; never disable it in production"],
    ] });

  K.cards(pres, { kicker: "Appendix", title: "Discussion prompts for the transitions",
    cols: 3, cardH: 2.3, cards: [
      { h: "After Module 1", t: "“Your BI dashboard and your data scientist report different completed-trips numbers. Which architecture decision caused it — and which one fixes it?”", color: P.bronze },
      { h: "After Module 2", t: "“Storage is cheap and compute is elastic. So why did the migration bill go UP? What discipline did they skip?”", color: P.silver },
      { h: "After Module 4", t: "“A regulator asks what a table contained three weeks ago. Can your platform answer — and what must be true about VACUUM for it to?”", color: P.gold },
      { h: "After Module 8", t: "“A model scores 0.95 offline. Are you excited or suspicious — and what do you check first?”", color: P.teal },
      { h: "After CS-11", t: "“Which of your current pipelines would have caught a unit change? Be honest. What would you add on Sunday morning?”", color: P.alarm },
      { h: "Closing", t: "“If the platform is both the audit evidence and the morning decision, what does your current pipeline testify about your team's reliability?”", color: P.bronze },
    ] });

  K.statement(pres, { kicker: "SDA-DSC-214", size: 34,
    text: "Thank you.",
    sub: "Instructor package · labs · case studies · activities · assessments · starter repository · synthetic Masar dataset\nSDAIA Academy · Capacity Building Sector" });
};
