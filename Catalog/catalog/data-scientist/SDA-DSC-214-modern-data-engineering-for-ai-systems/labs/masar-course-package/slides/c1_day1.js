const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "DAY 1", title: "Foundations\nand economics",
    sub: "Where data platforms come from, why the two-tier design fails AI, and how to argue about cost with numbers instead of adjectives.",
    items: ["Why data platforms fail AI", "M1 — Evolution of data architecture", "Lab 1 — Land the Masar raw feeds", "M2 — Compute–storage separation", "Lab 2 — Cost and elasticity model"],
    notes: "Day 1 sets the vocabulary and the golden thread. Protect the Lab 1 time — participants who land data on day one believe the rest." });

  K.cards(pres, { kicker: "Day 1 · Hour 1", title: "Why data platforms fail AI", dark: true,
    lead: "Three failure shapes. Each one is a real platform that ran perfectly and still starved or poisoned the model.",
    cols: 3, cardH: 2.6, cards: [
      { h: "The warehouse that could not feed the model", t: "Schema-on-write rejected the raw GPS the ETA model needed. Data science built a shadow copy on object storage. Two pipelines, two definitions, one argument that never ended.", color: P.bronze },
      { h: "The lake that became a swamp", t: "Everything landed, nothing was governed. No schema contract, no ownership, no catalog. A model trained on a renamed column and nobody noticed for six weeks.", color: P.silver },
      { h: "The platform that was right and still wrong", t: "Correct counts, fresh tables, green dashboards — and a feature that could not have been known at prediction time. Offline R² 0.94. Live: worse than the old heuristic.", color: P.alarm },
    ],
    note: "Ask the room: which of these three is happening in your organisation right now? Take three answers, write them on the board, return to them Thursday.",
    notes: "Do not rush this. The emotional hook for the whole week is that a platform can be operationally healthy and analytically fatal. The third card is the one participants underestimate; it is Module 8 and case study CS-08." });

  K.divider(pres, { eyebrow: "MODULE 1", title: "Evolution of\ndata architecture",
    sub: "Warehouse · Lake · Lakehouse — and the medallion spine that carries the rest of the course.",
    items: ["Three architectures, three eras", "The two-tier problem", "Medallion: bronze, silver, gold", "Open table formats", "Lab 1 — land the raw feeds"] });

  K.table(pres, { kicker: "Module 1 · Section 1", title: "Three architectures, three eras",
    head: ["", "Data warehouse", "Data lake", "Lakehouse"],
    widths: [1.7, 3.46, 3.46, 3.47], rowH: 0.44, fs: 11.5,
    rows: [
      ["Era / driver", "Structured BI, expensive storage", "Cheap object storage, big data, ML", "Both, on one copy"],
      ["Schema", "On write — enforced, rejects nonconforming", "On read — anything lands", "On write at the silver boundary; raw preserved in bronze"],
      ["Transactions", "ACID", "None — a folder of files", "ACID via an open table format"],
      ["Strength", "Reliability, governance, fast SQL", "Any format, any scale, cheap, ML-friendly", "Lake economics with warehouse reliability"],
      ["Failure mode", "Cannot hold raw/unstructured data AI needs", "Becomes a swamp: no contract, no trust", "None inherent — but discipline is still required"],
      ["Masar fit", "The morning ops dashboard", "Raw GPS for model training", "One platform serving both"],
    ],
    note: "The Lakehouse is not a product. It is open files plus a transaction layer plus discipline. Two of those three are free; the third is this course." });

  K.bullets(pres, { kicker: "Module 1 · Section 2", title: "The two-tier problem",
    lead: "A lake for data science, a warehouse for BI, and a fragile copy job between them. Four costs follow, always.",
    rowH: 1.05, items: [
      { n: "1", h: "Duplication", t: "The same data stored, secured and paid for twice. Two storage bills, two access-control models, two sets of infrastructure to patch.", color: P.bronze },
      { n: "2", h: "Staleness", t: "The warehouse copy is only as fresh as the last successful copy job. Every failure of that job is a silent divergence nobody sees until a number looks wrong.", color: P.silver },
      { n: "3", h: "Skew", t: "Two independently maintained pipelines compute “completed trips” from the same events and disagree — on late arrivals, on timezone, on what “completed” means. Divergence is not a risk; it is a certainty.", color: P.alarm },
      { n: "4", h: "Governance fracture", t: "PII masked in one tier and raw in the other. A PDPL erasure request must be honoured twice, and proving it was is nobody's job.", color: P.gold },
    ],
    note: "Case study CS-01 (“Naql” Logistics) is this slide with a SAR 4M incentive decision frozen on top of it. Run it now or after Lab 1." });

  K.cards(pres, { kicker: "Case study CS-01 · 25 minutes", title: "The reporting divergence at “Naql” Logistics",
    cols: 4, cardH: 2.6, cards: [
      { h: "Scenario", t: "A Saudi last-mile logistics firm runs a lake for data science and a separate warehouse for BI. The CEO dashboard shows 87% on-time. The data-science model reports 91% for the same week.", color: P.bronze },
      { h: "Stakes", t: "On-time rate drives customer SLAs and driver incentives. The divergence has frozen a SAR 4M incentive-scheme decision for a month. Trust in both numbers is collapsing.", color: P.alarm },
      { h: "Constraints", t: "Neither system can be frozen. Regulators require one auditable definition. Arabic and English address fields must survive consolidation byte-exact. Budget: one quarter.", color: P.silver },
      { h: "The move", t: "Land both feeds into an immutable bronze. Build ONE conformed silver.deliveries with a single reviewed late-arrival and timezone rule. Point BI and DS at it. Prove equivalence, then retire the copy job.", color: P.teal },
    ],
    note: "Facilitate, do not lecture. The question that unlocks the room: “How would you PROVE the consolidated number to a sceptical CFO?” — reconciliation report, reproducible silver logic, audit trail." });

  K.medallion(pres, { kicker: "Module 1 · Section 3", title: "Medallion architecture — the course spine",
    lead: "Progressive refinement. Each layer has a contract its consumers can depend on without reading the code that produced it.",
    sources: ["Raw feeds", "as received", "never edited", "at source"],
    bronze: { tables: "raw · append-only", contract: "Land AS RECEIVED. No cleaning, no dedup, no unit conversion. Add lineage only. Immutable — because it is the only thing you can reprocess from." },
    silver: { tables: "conformed · constrained", contract: "Dedup, type, conform units and timezone, enforce schema and CHECK constraints, quality-gate. One row per business key. This is the boundary where trust is created." },
    gold:   { tables: "curated · consumer-shaped", contract: "Business aggregates, star schema, feature tables. Documented grain. Point-in-time correct. PDPL-safe. Optimised for how it is read." },
    bi: "counts, revenue,\nutilisation,\nthe morning\ndecision",
    ai: "features,\ntraining sets,\nonline lookups,\nthe live ETA",
    note: "Bronze is intentionally allowed to contain the duplication that silver resolves. That is not sloppiness — it is what makes reprocessing possible." });

  K.twoCol(pres, { kicker: "Case study CS-09 · Databricks medallion", title: "Which transformations belong where?",
    lead: "Instructor question: Masar receives 15 million GPS events daily. Deliverable: a one-page Architecture Decision Record.",
    left: { h: "The rule that settles most arguments", color: P.bronze, sub: "Ask: could this transformation ever need to be undone or re-decided?",
      items: [
        "BRONZE — nothing but landing plus lineage: _ingested_at, _source_file, _batch_id. Partition by arrival date. That is the entire list.",
        "SILVER — dedup on event_id, type casting, timezone normalisation to UTC, unit conformance, PII hashing, referential joins to conformed dimensions, quality gate.",
        "GOLD — rolling windows, surrogate keys, business aggregates, feature engineering, point-in-time joins, star-schema modelling.",
      ] },
    right: { h: "NEVER before bronze persistence", color: P.alarm, sub: "Each of these destroys the only copy you could have reprocessed from.",
      items: [
        "Deduplication — you cannot prove a duplicate was real if you deleted it on arrival.",
        "Unit conversion — the very failure this course's signature incident is built on.",
        "Outlier removal — today's outlier is next quarter's fraud signal.",
        "Any join or enrichment — it embeds a second source's state at landing time, unreproducibly.",
        "Filtering by status — cancelled trips are data, not noise.",
      ] },
    note: "The ADR template and the full 20-transformation classification table are in labs/case_studies/CS-09." });

  K.flow(pres, { kicker: "Module 1 · Section 4", title: "What actually makes it a Lakehouse",
    lead: "Open files alone are a lake. One layer turns them into a table.",
    stepH: 2.5, steps: [
      { h: "Parquet files", t: "Columnar, compressed, open. Readable by Spark, Trino, DuckDB, pandas. Nothing proprietary. But: no transactions, no schema guarantee, no history.", color: P.silver },
      { h: "+ a transaction log", t: "An ordered set of atomic commit files recording which data files each transaction added and removed, plus schema and statistics.", color: P.bronze },
      { h: "= a Lakehouse table", t: "ACID · schema enforcement · MERGE upserts · time travel · concurrent readers and writers · maintenance. All on open files in object storage.", color: P.gold },
    ],
    note: "Delta Lake, Apache Iceberg and Apache Hudi are three implementations of this idea. This course uses Delta; the concepts transfer. Module 4 opens the log and reads it aloud." });

  K.bullets(pres, { kicker: "Module 1 · Section 5", title: "Principles, and the mistakes that break them",
    rowH: 0.92, items: [
      { n: "✓", h: "Bronze is immutable and append-only", t: "Corrections happen downstream, never in place. Mistake: mode(\"overwrite\") on landing — history disappears on re-run and reprocessing becomes impossible.", color: P.bronze },
      { n: "✓", h: "Enforce the schema contract at the silver boundary", t: "Schema-on-read does not mean you never enforce schema. Mistake: no contract anywhere, so a renamed source column silently under-reports a day.", color: P.silver },
      { n: "✓", h: "One definition of a business concept, in one place", t: "“A completed trip” is encoded once, in silver. Mistake: BI and DS each encode their own — the two-tier divergence, rebuilt inside one platform.", color: P.gold },
      { n: "✓", h: "Every layer has a named owner and a documented grain", t: "Mistake: gold built directly from bronze “just this once”, bypassing the gate. It is never just once.", color: P.teal },
    ],
    note: "Activity ACT-01 (architecture card-sort, 15 min) makes participants place 12 real workloads onto warehouse / lake / Lakehouse and onto bronze / silver / gold." });

  K.lab(pres, { id: "1", title: "Land the Masar raw feeds into bronze",
    meta: [["Duration", "50 minutes · pairs"], ["Checkpoint", "git checkout lab1-start"], ["Objective", "Three raw feeds landed append-only as Delta with lineage, then profiled for swamp risk"], ["Deliverable", "bronze.trips · bronze.gps_events · bronze.drivers + LAB1_NOTES.md"]],
    tasks: [
      "Inspect data/raw/ — trips CSV with SAR fares and KSA cities, GPS as nested NDJSON, drivers CSV with three different date formats.",
      "Implement land_trips and land_gps: read AS RECEIVED, add _ingested_at, _source_file and _batch_id, write Delta in append mode.",
      "Run the landing for one day. Then run it again for the same day. Confirm bronze GROWS — and discuss why bronze intentionally allows the duplication silver will resolve.",
      "Run profile_bronze on bronze.trips. Record null rates and the duplicate-trip_id count. Name at least three swamp risks you can see.",
      "Check the GPS partition count. Note whether the feed is already over-fragmented — this is Module 4's small-files problem arriving early.",
    ],
    accept: [
      "Bronze tables exist as Delta, are append-only, and carry all three lineage columns.",
      "Re-running the landing does not overwrite history (96,400 rows after two runs of a 48,200-row day).",
      "LAB1_NOTES.md lists ≥ 3 swamp risks with evidence.",
      "Nothing was cleaned, deduplicated or converted on the way in.",
    ],
    notes: "The duplicate-key issue caused by re-running is teaching moment #1: bronze SHOULD allow it; silver resolves it. Walk the room and check who spots it. Fast finishers: profile drivers.csv for the mixed date-format smell — a perfect bridge to Module 3." });

  K.divider(pres, { eyebrow: "MODULE 2", title: "Compute–storage\nseparation",
    sub: "The single design decision that made the Lakehouse economically possible — and the discipline required to actually realise the saving.",
    items: ["What decoupling physically means", "Object storage and Parquet", "The elasticity ladder", "Building a defensible cost model", "Lab 2 — cost and elasticity"] });

  K.twoCol(pres, { kicker: "Module 2 · Section 1", title: "What “decoupled” physically means",
    left: { h: "Coupled", color: P.alarm, sub: "Classic MPP warehouse or a Hadoop cluster",
      items: [
        "The machines that store the data are the machines that query it.",
        "Doubling storage means adding nodes you also pay to run, 24/7.",
        "Retaining rarely queried history is expensive: idle disks live inside always-on compute.",
        "You cannot scale one axis without the other. Capacity planning is a fixed, over-provisioned expense.",
      ] },
    right: { h: "Decoupled", color: P.teal, sub: "Object storage + stateless elastic compute",
      items: [
        "Data lives in object storage: cheap, effectively infinite, highly durable, addressed over the network.",
        "Compute is a separate stateless cluster that reads objects when a job runs, then is torn down.",
        "Store a petabyte you rarely touch for the price of the bytes; spin up 100 cores for the ten minutes a query needs them.",
        "The cost of the trade: network latency instead of local disk.",
      ] },
    note: "Three things make that latency acceptable: object-storage bandwidth is enormous and parallel; columnar formats let compute read only the columns and row-groups a query needs; and caching keeps hot data near compute." });

  K.cards(pres, { kicker: "Module 2 · Section 2", title: "Why Parquet makes decoupling affordable",
    lead: "Decoupling is only cheap because the format lets compute read a small, relevant slice of remote data instead of dragging everything across the wire.",
    cols: 3, cardH: 2.4, cards: [
      { h: "Columnar layout", t: "Values of one column are stored together. A query touching 3 of 40 columns reads roughly 3/40 of the bytes. This is column pruning, and it is free.", color: P.bronze },
      { h: "Row groups + statistics", t: "Each row group stores min/max per column, so a query skips groups that cannot match its filter. This is predicate pushdown and data skipping — a cost control, not just a speed control.", color: P.silver },
      { h: "Compression and encoding", t: "Similar values sit adjacent, so columnar data compresses far better than row data. It cuts storage cost AND bytes over the network at the same time.", color: P.gold },
      { h: "Cheap and elastic storage", t: "Priced per GB-month with no pre-provisioning. You never “run out”, and you never pay for headroom you are not using.", color: P.teal },
      { h: "Durable and open", t: "Providers replicate across facilities — 11 nines is typical. Many engines read the same bucket, so one copy serves BI and ML.", color: P.bronze },
      { h: "The pitfall to remember", t: "Objects are written whole, and huge numbers of tiny objects make LISTING slow. This is exactly why the small-files problem in Module 4 matters to your bill.", color: P.alarm },
    ] });

  K.table(pres, { kicker: "Module 2 · Section 3", title: "The elasticity ladder",
    head: ["Model", "You manage", "Scales", "Best for", "Masar example"],
    widths: [2.2, 2.35, 2.15, 2.6, 2.79], rowH: 0.5, fs: 11.5,
    rows: [
      ["Fixed / provisioned", "Cluster size, always on", "Manually", "Steady, predictable 24/7 load", "Nothing here should be fixed"],
      ["Autoscaling cluster", "Min / max bounds", "Up and down with load", "Variable batch pipelines", "Daytime ad-hoc analysis"],
      ["Ephemeral job cluster", "Nothing between jobs", "0 → N per job → 0", "Scheduled ELT, model retrains", "The nightly medallion DAG"],
      ["Serverless", "Nothing at all", "Instantly, per query", "Spiky, unpredictable, ad-hoc", "The exec dashboard endpoint"],
      ["Spot / preemptible", "Interruption tolerance", "Cheaply — 60–90% off", "Fault-tolerant, restartable jobs", "GPS backfill reprocessing"],
    ],
    note: "You pay for compute by the second it runs, and for storage by the byte you keep. A nightly ELT that runs 20 minutes should cost 20 minutes of compute — not 24 hours of an idle cluster." });

  K.chart(pres, { kicker: "Module 2 · Section 4", title: "Where the money actually goes",
    type: pres.ChartType.bar, legend: true, labelPos: "outEnd",
    colors: [P.alarm, P.teal],
    data: [
      { name: "Coupled warehouse (USD/month)", labels: ["Storage — 36 months history", "Nightly ELT compute", "Ad-hoc analyst compute", "Idle nights and weekends"], values: [4200, 1800, 1400, 3100] },
      { name: "Decoupled Lakehouse (USD/month)", labels: ["Storage — 36 months history", "Nightly ELT compute", "Ad-hoc analyst compute", "Idle nights and weekends"], values: [276, 190, 340, 0] },
    ],
    opts: { barDir: "bar", valAxisMaxVal: 5000 },
    side: { h: "How to build the model", items: [
      "Storage/month = total_GB × price_per_GB_month, plus a modest factor for the history the table format retains.",
      "Compute/month = Σ over jobs ( cores × core-hour price × runtime hours × runs per month ).",
      "12 TB of Masar raw GPS and trips at ~$0.023/GB-month ≈ $276. That is the whole storage line.",
      "Illustrative unit prices — Lab 2 has participants plug in real ones and defend the result.",
    ] },
    takeaway: "The headline that wins architecture reviews: decoupling lets you retain MORE history for LESS money, while paying for compute only when work happens." });

  K.bullets(pres, { kicker: "Module 2 · Section 5", title: "Five ways teams fail to realise the saving", dark: true,
    lead: "Decoupling ENABLES savings. Layout and elasticity discipline REALISE them. These five are why a migration bill goes up.",
    rowH: 0.9, items: [
      { n: "1", h: "Estimating a Lakehouse with warehouse intuition", t: "Assuming compute is always on, then concluding it is “not cheaper”. The elasticity is the product.", color: P.alarm },
      { n: "2", h: "Ignoring the small-files and listing cost", t: "Millions of tiny objects make jobs slow and expensive at the same time. Streaming sinks create this daily.", color: P.alarm },
      { n: "3", h: "Autoscaling with no idle-termination", t: "The classic surprise bill. Idle termination is a config line, not a project.", color: P.alarm },
      { n: "4", h: "Full-scanning because of poor layout", t: "Paying compute to read data a partition filter or a ZORDER could have skipped entirely.", color: P.alarm },
      { n: "5", h: "Forgetting egress and cross-region transfer", t: "Compute and storage in different regions turns every read into a transfer charge.", color: P.alarm },
    ],
    note: "Case study CS-02 (“Tabadul” Analytics): storage dropped 70% and the first month's total bill still ROSE — every dashboard full-scanned an unpartitioned gold table. Month two, after partitioning, ZORDER, caching and a 10-minute idle timeout: 45% below the old warehouse." });

  K.lab(pres, { id: "2", title: "Cost and elasticity model for Masar",
    meta: [["Duration", "50 minutes · pairs"], ["Checkpoint", "git checkout lab2-start"], ["Objective", "A defensible, auditable cost model comparing coupled and decoupled for Masar's real volumes"], ["Deliverable", "cost_model.py output + BENCHMARKS.md scan analysis"]],
    tasks: [
      "Measure the columnar advantage: run the same aggregation over CSV and over Parquet, and read the physical plan for PushedFilters and ReadSchema.",
      "Record bytes scanned with and without column pruning, and with and without a partition filter.",
      "Build the cost model in code, not a spreadsheet — storage and compute as separate, auditable terms.",
      "Model three elasticity strategies for the nightly ELT: always-on, autoscaling, ephemeral job cluster. Report the monthly delta.",
      "Add the idle-termination guardrail to the cluster config and state, in one sentence, what it is worth per month.",
    ],
    accept: [
      "The plan output shows PushedFilters and a pruned ReadSchema — you can point at the line.",
      "The cost model separates storage and compute and names the dominant driver for Masar.",
      "BENCHMARKS.md records bytes scanned before and after layout changes, from YOUR run.",
      "You can defend the recommendation in one sentence to a finance stakeholder.",
    ] });

  K.statement(pres, { kicker: "Day 1 · close",
    text: "Tomorrow the raw feeds become\na table someone can trust.",
    size: 32,
    sub: "You have landed three feeds into an immutable bronze and you can argue about cost with numbers.\nDay 2 is where bronze becomes silver — and where the single most common production pipeline bug lives.",
    notes: "Collect the LAB1_NOTES swamp risks and put three of them on the board for tomorrow morning. They are the agenda for Module 3." });
};
