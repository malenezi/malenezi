# Modern Data Engineering for AI Systems
## هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Modern Data Engineering for AI Systems |
| **Arabic Title** | هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي |
| **Code** | SDA-DSC-214 |
| **Level** | Specialist |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Data engineers, data scientists, systems and AI architects, data-infrastructure leads |
| **Prerequisites** | SDA-FND-104; SDA-FND-103 |
| **Assessment** | Labs; Mini-Lakehouse build project |
| **Stackability** | Data-engineering badge; anchors the Data Engineering for AI specialisation. Derived from the existing Modern Data Engineering programme. Next: SDA-DSC-215 / SDA-DSC-313 |
| **Tools & Platforms** | PySpark · Delta Lake · dbt · Kafka basics · Great Expectations |

## Course Description

A comprehensive module on building modern, scalable, production-ready data architectures that feed AI and analytics. Participants trace the evolution from warehouses and lakes to the Lakehouse, master Delta Lake with ACID transactions and compute-storage separation, and work with ELT, streaming, data quality, and governance. A hands-on build of a local Mini-Lakehouse with Delta Lake and PySpark anchors the learning.

The course is built around a single evolving artefact: **"Masar" (مسار)**, the national smart-mobility data platform of a Saudi ride-hailing and public-transit operator. Across the five days participants ingest Masar's raw trip records, GPS telemetry, driver and vehicle data, and payments; land them in a medallion (bronze → silver → gold) Lakehouse on Delta Lake; harden them with ELT transformations, streaming ingestion, quality tests, and governance controls; and finally serve them to two consumers — an **ETA / demand-forecasting AI feature store** and an **operations BI dashboard**. Every lab produces a component of the Mini-Lakehouse capstone, so by Day 5 each participant owns a working, tested, governed Lakehouse feeding both an AI model and a BI layer — the same shape of platform they will scale in SDA-DSC-215 (Big Data Analytics with Spark) and SDA-DSC-313.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Compare data warehouses, data lakes, and Lakehouse architectures across use cases
2. **LO2** — Explain compute-storage separation and its impact on cost, elasticity, and scale
3. **LO3** — Design ELT pipelines suited to modern cloud data environments
4. **LO4** — Implement Delta Lake tables with ACID transactions and schema enforcement
5. **LO5** — Develop streaming and event-driven ingestion patterns for real-time data
6. **LO6** — Apply data-quality, observability, and governance controls across pipelines
7. **LO7** — Build a working Mini-Lakehouse with Delta Lake and PySpark
8. **LO8** — Connect Lakehouse components to AI, reporting, and analytics consumers

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Foundations and economics | M1: Evolution of Data Architecture · M2: Compute–Storage Separation and Cloud Economics | 55% | 45% | Architecture decision record + a cost/elasticity model comparing warehouse vs Lakehouse for Masar |
| **Day 2** | Pipelines — from ETL to ELT | M3: ETL versus ELT in Modern Stacks | 40% | 60% | ELT pipeline: raw trips landed and transformed to a conformed `silver.trips` model with dbt + Spark |
| **Day 3** | The Lakehouse table | M4: Delta Lake and ACID Transactions | 35% | 65% | Delta `silver.trips` with schema enforcement, MERGE upserts, time travel, and OPTIMIZE/VACUUM applied |
| **Day 4** | Real-time and trust | M5: Streaming and Event-Driven Architectures · M6: Data Quality, Observability, and Governance | 40% | 60% | Structured-Streaming GPS ingestion into bronze + a Great Expectations quality gate on silver |
| **Day 5** | Build and serve | M7: Building a Mini-Lakehouse · M8: Serving Data to AI and BI Workloads · Capstone | 25% | 75% | End-to-end Mini-Lakehouse feeding an AI feature table and a BI star schema + capstone demo |

## Hour-by-Hour Breakdown

### Day 1 — Foundations and Economics

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why data platforms fail AI** + course kickoff | Recognise how warehouse-only and lake-only designs starve or corrupt AI workloads; meet the Masar golden thread | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Evolution of data architecture** (M1) | Warehouse vs lake vs Lakehouse; the two-tier problem; medallion architecture; when each fits | Lecture + architecture walkthrough | 75/25 |
| 3 | **Lab 1 — Land the Masar raw feeds** | Ingest trips/GPS/drivers CSV+JSON into a bronze zone; profile schema drift and the "data swamp" smell | Guided lab (pairs) | 20/80 |
| 4 | **Compute–storage separation and cloud economics** (M2) | Why decoupling storage from compute changes cost and scale; object storage; elastic clusters; formats | Lecture + cost-model demo | 70/30 |
| 5 | **Lab 2 — Cost and elasticity model** | Build a spreadsheet + PySpark benchmark comparing a coupled warehouse vs a decoupled Lakehouse for Masar's volumes | Guided lab (pairs) | 20/80 |

### Day 2 — Pipelines: From ETL to ELT

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **ETL vs ELT in modern stacks** (M3) | Why ELT won on the cloud; EL then T-in-warehouse; idempotency; incremental models | Lecture + pipeline dissection | 70/30 |
| 2 | **Modelling with dbt on the Lakehouse** | Staging → intermediate → mart layers; sources, refs, tests, docs; SQL as transformation | Lecture + live dbt demo | 60/40 |
| 3 | **Lab 3a — Build the staging models** | dbt `stg_trips`, `stg_gps`, `stg_drivers` with typing, renaming, and source freshness tests | Guided lab | 15/85 |
| 4 | **Incremental and idempotent transforms** | Incremental materialisation, late-arriving data, backfills, partition pruning | Lecture + demo | 55/45 |
| 5 | **Lab 3b — Build `silver.trips` (incremental)** | Join trips to drivers, derive fare/duration features, incremental merge on `trip_id` | Guided lab | 10/90 |

### Day 3 — The Lakehouse Table

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Delta Lake internals** (M4) | Transaction log, ACID, optimistic concurrency, snapshot isolation, Parquet + `_delta_log` | Lecture + log-inspection demo | 65/35 |
| 2 | **Lab 4a — Convert silver to Delta** | Write `silver.trips` as Delta; enforce schema; observe the `_delta_log` JSON commits | Guided lab | 15/85 |
| 3 | **MERGE, schema evolution, constraints** | Upserts, CDC-style merges, `mergeSchema`, CHECK constraints, generated columns | Lecture + demo | 55/45 |
| 4 | **Lab 4b — Upserts, time travel, OPTIMIZE** | MERGE corrections into `silver.trips`; query `VERSION AS OF`; OPTIMIZE + ZORDER; VACUUM | Guided lab | 10/90 |
| 5 | **Table maintenance and small-files** | Compaction, ZORDER, VACUUM retention, checkpoint files, cost of over-partitioning | Micro-lecture + lab wrap | 30/70 |

### Day 4 — Real-Time and Trust

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Streaming and event-driven architectures** (M5) | Batch vs streaming; Kafka topics/partitions/offsets; event time vs processing time; delivery semantics | Lecture + Kafka walkthrough | 70/30 |
| 2 | **Lab 5 — Stream GPS pings into bronze** | Kafka producer for GPS; Spark Structured Streaming read → Delta bronze with checkpointing | Guided lab | 15/85 |
| 3 | **Data quality and observability** (M6) | Testing pyramid for data; Great Expectations; freshness/volume/schema/distribution checks; quarantine | Lecture + expectations demo | 65/35 |
| 4 | **Lab 6 — Quality gate on silver** | Great Expectations suite on `silver.trips`; fail-and-quarantine bad rows; emit a data-docs report | Guided lab | 10/90 |
| 5 | **Governance, lineage, and PDPL** | Catalogs, lineage, access control, PII classification, Saudi PDPL obligations, retention | Micro-lecture + discussion | 40/60 |

### Day 5 — Build and Serve

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Assembling the Mini-Lakehouse** (M7) | Wire bronze → silver → gold; orchestrate with a DAG; medallion contracts and idempotent runs | Lecture + orchestration demo | 40/60 |
| 2 | **Lab 7 — Build gold aggregates** | Build `gold.zone_hourly_demand` and `gold.driver_daily`; orchestrate the full DAG end-to-end | Guided lab | 10/90 |
| 3 | **Serving to AI and BI** (M8) | Feature tables, point-in-time correctness, star schema for BI, serving trade-offs | Lecture + serving demo | 55/45 |
| 4 | **Capstone assembly** | Integrate all components; complete the Mini-Lakehouse checklist; peer review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos; rubric-based peer + instructor scoring; path to SDA-DSC-215/313 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same Masar platform. Never introduce a throwaway example dataset — always evolve the Masar medallion Lakehouse. This is what makes the capstone achievable on Day 5 Hour 4; each lab is a capstone component, not a detour.
- **Pace control:** Labs 4b (Delta MERGE/OPTIMIZE) and 5 (streaming) are the most overrun-prone. Publish checkpoint tags (`lab1-start`, `lab1-solution`, `lab4b-start`, …) in the course repository so stragglers can fast-forward: `git checkout lab5-start`.
- **Pairing:** rotate pairs each day. Pair a strong-SQL participant with a strong-Python/Spark participant; the skill transfer is the point, since ELT (SQL) and streaming (Spark) reward different backgrounds.
- **Environment strategy:** primary = local Spark 3.5 + `delta-spark` + a single-broker Kafka via `docker compose`; fallback = a hosted notebook (Databricks Community Edition or a Colab + `pyspark`/`delta` install). Verify both the week before delivery; the streaming lab needs Kafka, so pre-pull the images.
- **Data volume discipline:** the shipped Masar sample is deliberately small (a few million rows) so labs run on a laptop. Teach the *concepts* at cloud scale (TB/PB) but demonstrate on the sample; the benchmarks tables extrapolate.
- **Language:** deliver in English or Arabic; keep all code, table names, column names, and commit messages in English (production convention in Saudi enterprise environments — mixed-language identifiers break SQL tooling and `grep`-based operations). City names and business terms may carry Arabic subtitles in slides.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-5 afternoon is deliberately build-heavy and light on new theory.
- **Assessment logistics:** rubric scoring happens live during Day 5 Hour 5 demos; collect repository URLs and the `mini_lakehouse/` folder at the end of Hour 4 so table counts and data-docs can be verified before demos begin.
- **Governance framing:** treat Saudi PDPL (Personal Data Protection Law) as a first-class constraint from Day 1, not a Day-4 afterthought. Rider identifiers and precise GPS are personal data; every lab handles them accordingly.

---

# Module 1 — Evolution of Data Architecture: Warehouse, Lake, Lakehouse

## Module Overview

**Purpose.** Most AI initiatives stall not on the model but on the data platform beneath it: a warehouse that cannot hold raw GPS traces, or a lake that has decayed into an ungoverned "swamp" no model can trust. This module gives participants the architectural vocabulary and decision framework to place a workload correctly — and introduces the Lakehouse as the pattern that resolves the decades-old split between warehouses (governed, fast, structured) and lakes (cheap, open, flexible).

**Business relevance.** Saudi enterprises modernising under Vision 2030 — banking, telecom, mobility, government digital services — routinely inherit a two-tier estate: an expensive warehouse for BI and a separate lake for data science, kept in sync by brittle copy jobs. This module equips participants to evaluate whether a Lakehouse consolidation reduces cost, duplication, and staleness, and to defend that recommendation in an architecture review.

**Industry use cases.**
- A mobility operator must serve both real-time ops dashboards (warehouse strength) and ETA-model training on raw GPS (lake strength) from *one* governed copy of the data.
- A bank's risk team needs auditable, ACID-correct tables for regulators *and* schema-on-read flexibility for feature experimentation — historically two systems, now one.
- A government analytics unit must retain years of raw records cheaply in open formats (no vendor lock-in) while still exposing curated, access-controlled marts.

**Expected competencies.** After this module a participant can define warehouse, lake, and Lakehouse precisely; explain the "two-tier" and "data swamp" failure modes; lay out a medallion (bronze/silver/gold) architecture; and choose the right pattern for a given workload with cost and governance justification.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Define data warehouse, data lake, and Lakehouse and contrast their storage, schema, and governance models | LO1 |
| 1.2 | Diagnose the two-tier architecture and "data swamp" failure modes with concrete symptoms | LO1 |
| 1.3 | Lay out a medallion (bronze → silver → gold) architecture for a real workload | LO1, LO7 |
| 1.4 | Select warehouse vs lake vs Lakehouse for a given use case with cost/governance rationale | LO1, LO2 |
| 1.5 | Land raw multi-format feeds into a bronze zone and profile them | LO1, LO7 |

## Technical Content

### 1. Three architectures, three eras

A **data warehouse** stores structured, modelled data optimised for SQL analytics. Schema is enforced **on write** (schema-on-write): data must conform before it lands, which guarantees quality and query speed but rejects anything messy or novel — raw GPS pings, nested JSON, images. Storage and compute are historically coupled and priced together, which is why warehouses are expensive to scale and awkward for the exploratory, high-volume, semi-structured data that machine learning feeds on.

A **data lake** stores *anything* — files of any format — in cheap object storage, with schema applied **on read** (schema-on-read). This is perfect for data science: keep everything, decide structure later. But without discipline the lake becomes a **swamp**: no schema enforcement means silent corruption, no transactions means half-written files and dirty reads, no catalog means nobody can find or trust anything. Lakes optimise for flexibility and cost at the expense of reliability and governance.

The **Lakehouse** is the synthesis: it keeps data in open formats (Parquet) on cheap object storage like a lake, then adds a **transactional metadata layer** (Delta Lake, Apache Iceberg, or Apache Hudi) that provides ACID transactions, schema enforcement, time travel, and governance *on top of the files*. You get warehouse reliability and lake economics from one copy of the data — no more copying between two systems.

| Property | Warehouse | Lake | Lakehouse |
|---|---|---|---|
| Storage | Proprietary, coupled | Object store, open files | Object store, open files (Parquet) |
| Schema | On write (enforced) | On read (optional) | On write *and* on read (enforced by table layer) |
| Transactions | Yes (ACID) | No | Yes (ACID via metadata layer) |
| Data types | Structured only | Any (structured, semi, unstructured) | Any |
| Cost model | Compute+storage coupled | Cheap storage, DIY compute | Cheap storage, elastic compute |
| Primary consumers | BI / SQL analysts | Data science / ML | BI **and** ML from one copy |
| Failure mode | Too rigid/expensive for ML | Data swamp | Requires engineering discipline |

### 2. The two-tier problem this course solves

The dominant enterprise pattern before the Lakehouse — and still the *status quo* at most Saudi organisations — is **two tiers**: a lake for raw/ML data and a warehouse for BI, connected by ETL jobs that copy curated subsets from lake to warehouse. It has four chronic costs:

- **Duplication:** the same trip data lives in both systems, doubling storage and confusing "which is the source of truth?".
- **Staleness:** the warehouse is only as fresh as the last copy job; dashboards lag reality by hours.
- **Skew:** the lake's copy and the warehouse's copy diverge as transformations drift, so the data scientist's features disagree with the analyst's KPIs — the same defect that later becomes model/serving skew.
- **Governance sprawl:** access control, lineage, and PII rules must be maintained twice, in two tools, with two audit trails.

For Masar this is concrete: the ops team's "trips completed today" in the warehouse dashboard disagrees with the data-science team's trip count in the lake because a late-arriving-trip rule was implemented in only one place. The Lakehouse removes the copy and the divergence: one governed `silver.trips` table serves both.

### 3. Medallion architecture (bronze / silver / gold)

The Lakehouse organises data into progressively refined **layers**, a pattern popularised as *medallion* architecture. This is the backbone of the Masar platform and the spine of every lab in this course.

| Layer | Also called | Contents | Schema | Consumers |
|---|---|---|---|---|
| **Bronze** | Raw / landing | Exact copy of source data, append-only, with ingestion metadata (`_ingested_at`, `_source_file`) | As-received (permissive) | Reprocessing, audit, debugging |
| **Silver** | Cleaned / conformed | Validated, typed, deduplicated, joined to conformed dimensions; one row per real-world entity | Enforced | Data science, features, ad-hoc analytics |
| **Gold** | Curated / marts | Business-level aggregates and features, often a star schema or feature table | Enforced, modelled | BI dashboards, AI feature stores, reports |

Two rules make medallion work:

1. **Never mutate bronze.** Bronze is append-only and immutable; it is your ability to reprocess everything if a silver transformation had a bug. Deleting or editing bronze destroys reproducibility.
2. **Each layer's promotion is a pure, idempotent transformation.** Re-running silver from bronze must yield the same result; this is what makes backfills and disaster recovery safe (covered deeply in M3).

### 4. Open table formats: the layer that makes it a Lakehouse

What turns a pile of Parquet files into a *table* is the **open table format** — a transaction log and metadata layer over the files. The three contenders:

- **Delta Lake** (used in this course): a `_delta_log` directory of ordered JSON commits + periodic Parquet checkpoints, giving ACID transactions, time travel, schema enforcement, and MERGE. Tightest integration with Spark.
- **Apache Iceberg:** a hidden-partitioning, snapshot-based format with strong multi-engine support (Spark, Trino, Flink); favoured where many query engines must share tables.
- **Apache Hudi:** optimised for streaming upserts and incremental pulls; strong for CDC-heavy ingestion.

All three deliver the Lakehouse promise (ACID + open files); the differences are engine ecosystem and upsert strategy. This course uses **Delta Lake** because its Spark integration is the most direct path for participants, but the *concepts* — transaction log, snapshot isolation, compaction — transfer to all three. We return to Delta internals in Module 4.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *One source of truth:* the Lakehouse exists to eliminate duplicate copies; if a design reintroduces a "reporting database" alongside the Lakehouse, ask why.
- *Raw is sacred:* bronze is immutable and append-only; all correction happens in silver/gold via reproducible logic.
- *Schema is a contract:* even in a lake-like store, enforce schema at the silver boundary — schema-on-read does not mean schema-never.
- *Layers earn trust:* consumers read the layer that matches their tolerance — data scientists may read silver, executives only gold.

**Common mistakes (each appears in the Lab 1 starter deliberately)**
1. Writing cleaned data straight into one flat zone with no bronze — losing the ability to reprocess when the cleaning logic is wrong.
2. Mutating bronze in place ("just fix that one bad row") — silently breaking reproducibility.
3. Treating the lake as a warehouse: dumping files with no catalog, no schema, no partitioning → instant swamp.
4. Over-partitioning bronze by high-cardinality keys (e.g., `trip_id`) → millions of tiny files, catastrophic read performance.
5. Copying to a warehouse "for BI" out of habit, recreating the two-tier problem the Lakehouse was chosen to remove.

**Production considerations**
- Storage layout is an *operational* interface: on-call engineers and auditors navigate your zones at 03:00. Predictable `zone/table/partition/` paths beat clever ones.
- Version everything that affects a table: source schema version, transformation code (git SHA), and (from M4) the Delta table version. This is the audit chain Saudi regulators increasingly expect.
- Design for two consumers from day one — an AI feature store and a BI layer. If both can read the same silver/gold, the architecture is right (this is exactly M8).

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides): a regional logistics firm ran a classic two-tier estate. The data-science team's "on-time delivery rate" (computed in the lake) read 91%; the executive dashboard (warehouse) read 87%. Weeks of finger-pointing revealed the warehouse copy job silently dropped deliveries whose timestamps arrived after the nightly cutoff — a late-arriving-data bug in *one* of the two pipelines. The fix was not a better ETL job; it was architectural: consolidate onto a single governed `silver.deliveries` Lakehouse table with one late-arrival rule, read by both BI and DS. Reporting divergence went to zero, storage cost dropped 38% (one copy, cheap object store), and the "which number is right?" meetings ended. This course builds that consolidation, generalised, on Masar.

## Code Examples

### Bootstrapping a local Lakehouse Spark session

```python
# src/masar/spark.py
"""One place to build the Spark session with Delta Lake enabled.

Every lab imports get_spark() — never reconfigure Spark ad hoc in a notebook.
"""
from pyspark.sql import SparkSession


def get_spark(app_name: str = "masar-lakehouse") -> SparkSession:
    """Spark 3.5 + Delta Lake session for the Masar Lakehouse.

    Storage and compute are separate even locally: data lives under
    ./lakehouse (a stand-in for object storage), compute is this JVM.
    """
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.extensions",
                "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        # local stand-in for an object-storage bucket (s3://masar-lakehouse)
        .config("spark.sql.warehouse.dir", "./lakehouse")
        .config("spark.sql.shuffle.partitions", "8")  # small = laptop-friendly
        .getOrCreate()
    )
```

### Landing raw feeds into the bronze zone (append-only, with lineage metadata)

```python
# src/masar/ingest/land_bronze.py
"""Land raw Masar source files into the bronze zone.

Bronze rules enforced here:
  - append-only (never overwrite history)
  - keep data AS-RECEIVED (no cleaning, no typing beyond the source)
  - attach ingestion lineage: when and from which file each row came
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

BRONZE = "./lakehouse/bronze"


def land_trips(source_glob: str) -> None:
    spark = get_spark()
    raw = (
        spark.read
        .option("header", True)
        .option("mode", "PERMISSIVE")   # keep malformed rows, do NOT drop
        .csv(source_glob)
    )
    bronze = (
        raw
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_file", F.input_file_name())
    )
    # append-only: bronze is an immutable ledger of what arrived
    (bronze.write
        .format("delta")
        .mode("append")
        .save(f"{BRONZE}/trips"))


def land_gps(source_glob: str) -> None:
    """GPS pings arrive as newline-delimited JSON (nested payload)."""
    spark = get_spark()
    raw = spark.read.json(source_glob)          # schema-on-read for JSON
    (raw
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_file", F.input_file_name())
        .write.format("delta").mode("append").save(f"{BRONZE}/gps_pings"))
```

### Profiling the landed data for swamp smells

```python
# src/masar/ingest/profile_bronze.py
"""Cheap data-profiling pass to surface 'swamp' smells before we trust bronze."""
from pyspark.sql import functions as F
from masar.spark import get_spark


def profile(table_path: str) -> None:
    spark = get_spark()
    df = spark.read.format("delta").load(table_path)
    n = df.count()
    print(f"rows={n:,}  columns={len(df.columns)}")

    # Null rate per column — high nulls in a key column is a swamp smell
    null_rates = df.select([
        (F.sum(F.col(c).isNull().cast("int")) / F.lit(n)).alias(c)
        for c in df.columns
    ])
    null_rates.show(truncate=False, vertical=True)

    # Duplicate primary keys — bronze allows dupes, but we must SEE them
    if "trip_id" in df.columns:
        dupes = (df.groupBy("trip_id").count()
                   .filter("count > 1").count())
        print(f"duplicate trip_id groups: {dupes:,}")
```

## Hands-on Lab 1 — Land the Masar Raw Feeds into Bronze

| | |
|---|---|
| **Objective** | Ingest the three raw Masar feeds (trips CSV, GPS JSON, drivers CSV) into an append-only bronze zone as Delta tables with lineage metadata, then profile them to name the "swamp" risks |
| **Duration** | 50 minutes |
| **Setup** | Python 3.11, Java 17, `pip install pyspark==3.5.* delta-spark==3.2.*`, course repo cloned, `git checkout lab1-start` |

**Instructions & tasks**

1. *(5 min)* Inspect `data/raw/`: `trips_2026-06-*.csv`, `gps/*.json`, `drivers.csv`. Note that trips carry SAR fares and KSA cities (Riyadh, Jeddah, Dammam), and GPS is nested JSON.
2. *(10 min)* Implement `land_trips` and `land_gps` (start from `land_bronze.py` stub): read AS-RECEIVED, add `_ingested_at` + `_source_file`, write Delta in **append** mode to `lakehouse/bronze/`.
3. *(10 min)* Run the landing for one day of data, then run it *again* for the same day. Confirm bronze **grows** (append-only) — and discuss why bronze intentionally allows the duplication that silver will later resolve.
4. *(15 min)* Run `profile_bronze.py` on `bronze/trips`. Record null rates and duplicate-`trip_id` count in `LAB1_NOTES.md`. Identify at least three swamp risks you can see.
5. *(5 min)* Add a `bronze/gps_pings` partition-count check: `spark.read...rdd.getNumPartitions()`. Note whether GPS is already over-fragmented.
6. *(5 min)* Commit: `feat(bronze): land trips/gps/drivers with lineage + profiling`.

**Expected output**
```
$ python -m masar.ingest.land_bronze --feed trips --date 2026-06-01
Landed 48,200 rows -> lakehouse/bronze/trips  (append, total now 48,200)
$ python -m masar.ingest.land_bronze --feed trips --date 2026-06-01   # re-run
Landed 48,200 rows -> lakehouse/bronze/trips  (append, total now 96,400)
$ python -m masar.ingest.profile_bronze bronze/trips
rows=96,400  columns=14
duplicate trip_id groups: 48,200   # expected: we appended the same day twice
null rate dropoff_geohash: 0.031   # swamp smell #1 to note
```

**Acceptance criteria**
- Bronze tables exist as Delta, are append-only, and carry `_ingested_at` + `_source_file`.
- `LAB1_NOTES.md` lists ≥ 3 swamp risks (e.g., duplicate keys, null dropoff, mixed date formats).
- Re-running landing does not overwrite history.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `Delta ... is not a valid Spark SQL Data Source` | Delta extension not configured | Use `get_spark()`; verify `spark.sql.extensions` set |
| `Py4JJavaError ... UnsupportedClassVersion` | Wrong Java | Install Java 17; set `JAVA_HOME` |
| GPS JSON reads as one giant column | File is a JSON array, not NDJSON | Use `.option("multiLine", True)` or split to NDJSON |
| Second run overwrote data | Used `mode("overwrite")` | Bronze must be `mode("append")` |

**Instructor notes.** The starter data contains exactly the swamp smells from the content section — walk the room and check who spots the duplicate-key issue caused by re-running (#1 teaching moment: bronze *should* allow it; silver resolves it). Fast finishers: add a `_batch_id` column and profile `drivers.csv` for the mixed date-format smell — a perfect bridge to Module 3's typing work.

## Mini Exercises

**Quiz (5 questions)**
1. Which architecture enforces schema on write and rejects nonconforming data? → **warehouse**.
2. Name the two failure modes this module contrasts. → two-tier duplication/staleness; data-swamp (ungoverned lake).
3. What single property turns a folder of Parquet into a Lakehouse table? → a transactional metadata/table layer (e.g., Delta `_delta_log`).
4. Why must bronze be immutable and append-only? → to preserve reproducibility/audit; all corrections happen downstream.
5. True/False: schema-on-read means you never enforce schema. → **False** — you enforce it at the silver boundary.

**Debugging exercise.** Give participants a branch where `land_trips` uses `mode("overwrite")`. Symptom: history disappears on re-run. Discuss why append + downstream dedup is the correct medallion pattern rather than overwrite.

**Design exercise.** Given three Masar workloads — an executive daily KPI dashboard, ETA-model training on raw GPS, and an ad-hoc fraud investigation — state which medallion layer each should read and why.

**Discussion questions.**
- Your BI vendor insists on copying gold into a separate warehouse "for performance." When is that justified, and when is it just recreating the two-tier problem?
- Who owns the definition of "a completed trip" — engineering, data science, or operations? What does your answer imply about which layer encodes it?

## Case Study — The Reporting Divergence at "Naql" Logistics

**Scenario.** "Naql" (نقل), a Saudi last-mile logistics firm, runs a lake (Spark on object storage) for data science and a separate cloud warehouse for BI. The CEO dashboard shows 87% on-time deliveries; the data-science on-time model reports 91% on the same week. Trust in *both* numbers is collapsing.

**Business context.** On-time rate drives customer SLAs and driver incentives. The divergence has frozen a SAR 4M incentive-scheme decision for a month.

**Technical challenge.** Two independently maintained pipelines compute "on-time" from the same events but disagree on late-arriving deliveries and timezone handling.

**Constraints.** Cannot freeze either system; regulators require an auditable single definition; Arabic and English address fields must survive any consolidation byte-exact; migration budget is one quarter.

**Solution approach (facilitate, don't lecture).** Consolidate onto a Lakehouse: (1) land both source feeds into an immutable bronze; (2) implement one conformed `silver.deliveries` with a single, reviewed late-arrival + timezone rule; (3) point *both* BI and DS at silver/gold; (4) retire the warehouse copy job. Prove equivalence with a reconciliation report before cutover.

**Discussion questions.**
1. Why does having two pipelines almost guarantee eventual divergence?
2. Which of the four two-tier costs (duplication, staleness, skew, governance) is most expensive here, and why?
3. How would you *prove* the consolidated number is correct to a skeptical CFO? (reconciliation report + reproducible silver logic + audit trail)
4. What would you keep the warehouse for, if anything, after consolidation?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Feeds landed to bronze | Coverage | 3/3 (trips, gps, drivers) | table existence + row counts |
| Bronze immutability | Correctness | append-only, re-run grows history | two runs, compare counts |
| Lineage columns present | Governance | `_ingested_at` + `_source_file` on every bronze table | schema check |
| Swamp risks identified | Analysis | ≥ 3 documented in LAB1_NOTES | instructor review |
| Bronze landing throughput | Performance | ≥ 200k rows/s on lab laptop (CSV) | landing job timing |

**Example benchmark table (filled during lab):**

| Feed | Format | Rows landed | Landing time | Null-rate flag | Files written |
|---|---|---|---|---|---|
| trips | CSV | 48,200 / day | 0.4 s | dropoff_geohash 3.1% | 8 |
| gps_pings | JSON | 1,210,000 / day | 3.9 s | none > 1% | 8 |
| drivers | CSV | 3,450 | 0.1 s | hire_date mixed format | 1 |

## Required Visuals and Training Assets

### Diagrams
1. **Warehouse → Lake → Lakehouse timeline** — *Purpose:* anchor image for the module. *Elements:* three stacked architectures with their schema/transaction/cost properties as callouts; the Lakehouse shown as "open files + transaction layer". *Style:* flat vector, three-colour palette, English labels with Arabic subtitles. *Designer description:* "Left-to-right evolution: a rigid warehouse box, a murky lake, then a Lakehouse combining a clean table icon over water."
2. **The two-tier problem** — *Purpose:* make the failure mode visceral. *Elements:* a lake and a warehouse connected by a fragile copy arrow, with two divergent "on-time %" numbers and a red skew bolt between them. *Style:* before/after split; "after" shows one consolidated Lakehouse.
3. **Medallion architecture for Masar** — *Purpose:* the spine of the whole course. *Elements:* bronze (raw trips/gps/drivers) → silver (conformed `silver.trips`) → gold (`zone_hourly_demand`, feature table), with consumer icons (BI, AI). *Style:* three-lane pipeline, colour-coded, reused in every module. *Designer description:* "Three horizontal bands bronze/silver/gold, arrows left-to-right, source icons feeding bronze, BI + AI icons drawing from gold."
4. **Open table format layer** — *Purpose:* explain what makes it a Lakehouse. *Elements:* Parquet file icons with a `_delta_log` transaction-log ribbon over them granting ACID/time-travel/schema. *Style:* exploded-layer diagram.

### Images (screenshots)
1. **Object-storage bucket layout** — expanded `lakehouse/bronze|silver|gold/` tree; *why:* participants mirror it in Lab 1; *content:* exact zone/table folders.
2. **Bronze profiling output** — the `profile_bronze` terminal output with null rates and duplicate-key count highlighted.
3. **`_delta_log` folder listing** — a bronze table's `_delta_log/00000000000000000000.json` visible; *why:* foreshadows M4.

### Simulations
1. **Swamp-in-fast-forward** — *Setup:* branch `sim-swamp` lands 5 days of trips with no schema notes, mixed date formats, and one renamed column. *Expected behaviour:* a naive downstream `count by day` silently under-reports the renamed day. *Learning objective:* lakes without discipline decay; schema contracts matter.
2. **Two-tier divergence** — *Setup:* two provided notebooks compute "completed trips" with different late-arrival rules. *Expected behaviour:* counts differ by ~2%. *Learning objective:* duplicate pipelines guarantee eventual skew.

### Interactive Activities
- **Architecture card-sort (15 min):** 12 workload cards (executive KPI, GPS-model training, fraud audit, real-time surge…) sorted onto warehouse / lake / Lakehouse and onto bronze/silver/gold.
- **"Spot the swamp" gallery walk (10 min):** four printed folder listings; teams flag which is a swamp and why.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_2026-06-*.csv` | Synthetic Masar generator (Faker + trip-pattern injector; SAR fares, KSA cities, surge) | CSV | ~48k rows/day × 30 days | Bronze landing; reused across all modules |
| `gps/*.json` | Synthetic GPS emitter (nested payload, ~25 pings/trip) | NDJSON | ~1.2M rows/day | GPS bronze; streaming source in M5 |
| `drivers.csv` | Synthetic driver dimension (mixed date formats deliberately) | CSV | 3,450 rows | Conformed dimension from M3 |

### Demo Requirements
- **Instructor demo:** land one day of trips, re-run it, and show bronze growing (append-only) then reconcile the duplicate in a 6-minute live walk — the append-then-dedup rhythm *is* the medallion lesson.

---

# Module 2 — Compute–Storage Separation and Cloud Economics

## Module Overview

**Purpose.** The single design decision that made the Lakehouse economically possible is the **decoupling of storage from compute**. This module explains what that means physically, why it collapses the cost of retaining raw data, and how it turns capacity planning from a fixed, over-provisioned expense into an elastic, pay-for-what-you-use model. Participants leave able to reason quantitatively about the cost and scale of a data platform — the language every architecture review and budget defence requires.

**Business relevance.** In the coupled world, keeping three years of Masar GPS meant paying for a cluster sized to *store* it, running 24/7. Decoupled, the same data sits in cheap object storage at a fraction of the price while compute spins up only for the minutes a job runs. For Saudi organisations under cost scrutiny, this is often the headline number that justifies a Lakehouse migration — and getting the estimate right is a career-relevant skill.

**Industry use cases.**
- A telecom retains years of raw call-detail records for AI at object-storage prices, querying them only when a model retrains.
- A bank runs heavy month-end risk jobs on a large transient cluster, then scales to near-zero the rest of the month — impossible when compute and storage were one bill.
- A government portal isolates an ad-hoc analyst's runaway query onto its own ephemeral compute so it cannot slow the production ingestion cluster reading the *same* data.

**Expected competencies.** After this module a participant can explain compute–storage separation and its consequences; describe object storage, columnar formats, and elastic/serverless compute; and build a defensible cost-and-elasticity model comparing a coupled warehouse to a decoupled Lakehouse for a real workload.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Explain compute–storage separation physically and its effect on cost and scale | LO2 |
| 2.2 | Describe object storage, columnar (Parquet) formats, and their role in the decoupled stack | LO2 |
| 2.3 | Contrast fixed/provisioned compute with elastic and serverless models | LO2 |
| 2.4 | Quantify storage vs compute cost for a workload and identify the dominant driver | LO2 |
| 2.5 | Recommend an elasticity strategy (autoscale, spot, serverless) for a given job pattern | LO2 |

## Technical Content

### 1. What "decoupled" physically means

In a **coupled** system (a classic MPP warehouse or a Hadoop cluster), the machines that store the data are the machines that query it. Doubling storage means adding nodes you also pay to run; you cannot scale one without the other. Retaining rarely queried history is expensive because idle disks live inside always-on compute nodes.

In a **decoupled** system, data lives in **object storage** (Amazon S3, Azure Data Lake Storage, Google Cloud Storage) — a cheap, effectively infinite, highly durable store addressed over the network. **Compute** is a separate, stateless cluster that *reads* those objects when a job runs and is torn down after. The two scale independently: store a petabyte you rarely touch for the price of the bytes, and spin up 100 cores for the ten minutes a query needs them.

The trade-off is **network latency**: compute must fetch objects over the network rather than from a local disk. Three things make this acceptable: (1) object storage bandwidth is enormous and parallel; (2) **columnar formats** (Parquet) let compute read only the columns and row-groups a query needs; and (3) **caching** keeps hot data near compute. The result is that decoupling's economic win overwhelmingly outweighs its latency cost for analytics and ML workloads.

### 2. Object storage and columnar formats

**Object storage** is the storage substrate of the Lakehouse. Key properties to teach:
- **Cheap and elastic:** priced per GB-month with no pre-provisioning; you never "run out".
- **Durable:** cloud providers replicate objects across facilities (11 nines of durability is typical).
- **Immutable objects, cheap listing pitfalls:** objects are written whole; huge numbers of tiny objects make *listing* slow — which is exactly why the **small-files problem** (M4) matters.
- **Open access:** many engines can read the same bucket, enabling one copy for BI *and* ML.

**Parquet**, the columnar file format underneath Delta, is what makes reading over the network efficient:
- **Columnar layout:** values of one column are stored together, so a query touching 3 of 40 columns reads ~3/40 of the bytes (*column pruning*).
- **Row groups + statistics:** each row group stores min/max per column, so queries skip groups that cannot match a filter (*predicate pushdown / data skipping*).
- **Compression + encoding:** columnar data compresses far better than row data (similar values adjacent), cutting both storage cost and bytes-over-network.

The lesson: decoupling is only cheap *because* the format lets compute read a small, relevant slice of remote data rather than dragging everything across the wire.

### 3. Elastic, serverless, and the shape of compute cost

Decoupled compute comes in escalating levels of elasticity:

| Model | You manage | Scales | Best for |
|---|---|---|---|
| **Fixed / provisioned** | Cluster size, always on | Manually | Steady, predictable 24/7 load |
| **Autoscaling cluster** | Min/max bounds | Up/down with load | Variable batch pipelines |
| **Ephemeral / job cluster** | Nothing between jobs | 0 → N per job → 0 | Scheduled ELT, retrains |
| **Serverless** | Nothing at all | Instantly, per query | Spiky, unpredictable, ad-hoc |
| **Spot / preemptible** | Interruption tolerance | Cheaply (60–90% off) | Fault-tolerant, restartable jobs |

The cost mantra: **you pay for compute by the second it runs; you pay for storage by the byte you keep.** For most AI-data platforms, storage is a small, steady line and compute is the large, controllable one — so *elasticity of compute* is where the money is saved or wasted. A nightly Masar ELT that runs 20 minutes should cost 20 minutes of compute, not 24 hours of an idle cluster.

### 4. Building a cost model

A defensible estimate separates the two axes explicitly. For Masar's raw + curated data:

**Storage cost/month** = `total_GB × price_per_GB_month` (add a modest factor for time-travel/history retained by the table format).

**Compute cost/month** = `Σ over jobs ( cluster_cores × core_hour_price × runtime_hours × runs_per_month )`.

Two Masar scenarios make the point (illustrative unit prices; participants plug real ones in Lab 2):

| Item | Coupled warehouse | Decoupled Lakehouse |
|---|---|---|
| 36 months raw GPS + trips (~12 TB) | Stored on always-on nodes: expensive | Object storage @ ~$0.023/GB-mo ≈ **$276/mo** |
| Nightly ELT (20 min) | Part of the always-on bill | 16 cores × 0.33 h × 30 × price → **minutes only** |
| Ad-hoc analyst queries | Contends with production nodes | Separate serverless endpoint, isolated |
| Idle overnight/weekend | Paid for | ~$0 compute |

The headline that wins reviews: decoupling lets you retain *more* history for *less* money while paying for compute only when work happens. But the model must be honest about the caveats in §5.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Right-size per job, not per platform:* different jobs want different cluster shapes; decoupling lets each pick.
- *Storage is cheap, scans are not:* the bill often comes from repeatedly scanning too much data — layout (partitioning, Parquet, data skipping) is a cost control, not just a speed control.
- *Isolation is a feature:* separate compute per workload prevents a rogue query from starving production.
- *Elasticity needs governance:* infinite scale means an infinite bill — quotas and auto-termination are mandatory.

**Common mistakes**
1. Estimating a Lakehouse using warehouse intuition (assuming compute is always on) and concluding it's "not cheaper".
2. Ignoring the small-files / listing cost of object storage — millions of tiny objects make jobs slow *and* pricey.
3. Leaving autoscaling clusters with no idle-termination — the classic surprise bill.
4. Scanning full tables because of poor partitioning/formatting — paying compute to read data a filter could have skipped.
5. Forgetting egress and cross-region transfer costs when compute and storage sit in different regions.

**Production considerations**
- Tag every cluster/job with a cost centre; unattributed compute is unmanageable at scale.
- Prefer spot/preemptible for restartable jobs; keep a small on-demand core for the driver.
- Cache hot gold tables near compute; the latency and cost win is largest on repeatedly read marts (the BI layer in M8).
- Model *data-scan* cost, not just cluster time, on serverless engines that bill per TB scanned.

### 6. Real-world example walkthrough

Narrate this (5 minutes): a Saudi retailer migrated a coupled MPP warehouse (sized for three years of history, running 24/7) to a decoupled Lakehouse. Storage of the same three years dropped ~70% by moving cold history to object storage. But the *first* month's compute bill actually rose — because every dashboard query full-scanned an unpartitioned gold table. The fix was pure §5: partition by date, ZORDER by store, cache the top marts, and set a 10-minute idle-termination. Month two's total bill was 45% below the old warehouse. The lesson participants take: decoupling *enables* savings; layout and elasticity discipline *realise* them.

## Code Examples

### Measuring the columnar / data-skipping advantage

```python
# src/masar/econ/scan_cost.py
"""Demonstrate that columnar + partitioned reads scan far less data.

The cost of decoupled compute is dominated by BYTES SCANNED, so we
measure it directly rather than trusting intuition.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark


def compare_scans(silver_path: str) -> None:
    spark = get_spark()

    # Naive: read all columns, filter after -> reads everything
    df_all = spark.read.format("delta").load(silver_path)
    wide = df_all.filter(F.col("city") == "Riyadh").count()

    # Pruned: select only needed columns; filter pushes down to Parquet
    narrow = (df_all
              .select("trip_id", "city", "fare_sar")
              .filter(F.col("city") == "Riyadh")
              .count())

    # Inspect the physical plan to SEE pushdown + column pruning
    (df_all.select("trip_id", "city", "fare_sar")
           .filter(F.col("city") == "Riyadh")
           .explain("formatted"))
    print(f"riyadh trips (all cols)={wide:,}  (pruned)={narrow:,}")
    # Same answer; the pruned plan reads a fraction of the bytes.
```

### A tiny cost model in code (auditable, not a black-box spreadsheet)

```python
# src/masar/econ/cost_model.py
"""Transparent storage-vs-compute cost model for the Masar platform.

All prices are inputs; the point is to SEE which axis dominates.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Prices:
    storage_gb_month: float = 0.023      # object storage $/GB-month
    core_hour: float = 0.06              # compute $/core-hour


@dataclass(frozen=True)
class Job:
    name: str
    cores: int
    runtime_hours: float
    runs_per_month: int

    def monthly_compute(self, p: Prices) -> float:
        return self.cores * self.runtime_hours * self.runs_per_month * p.core_hour


def platform_monthly_cost(total_gb: float, jobs: list[Job],
                          p: Prices = Prices()) -> dict[str, float]:
    storage = total_gb * p.storage_gb_month
    compute = sum(j.monthly_compute(p) for j in jobs)
    return {"storage": round(storage, 2),
            "compute": round(compute, 2),
            "total": round(storage + compute, 2),
            "compute_share": round(compute / (storage + compute), 3)}


if __name__ == "__main__":
    jobs = [
        Job("nightly_elt", cores=16, runtime_hours=0.33, runs_per_month=30),
        Job("hourly_stream_compact", cores=4, runtime_hours=0.1, runs_per_month=720),
        Job("weekly_feature_build", cores=32, runtime_hours=0.5, runs_per_month=4),
    ]
    print(platform_monthly_cost(total_gb=12_000, jobs=jobs))
    # -> storage steady & small; compute is the lever you actually pull.
```

### Idle-termination guardrail (config, not code — the cheapest safety net)

```yaml
# infra/cluster/masar-elt-cluster.yaml
# Ephemeral job cluster: exists only for the ELT run, then dies.
cluster:
  name: masar-elt
  spark_version: "3.5"
  autoscale:
    min_workers: 2
    max_workers: 8          # bounded elasticity: no runaway bill
  autotermination_minutes: 10   # MANDATORY: kill idle compute
  node_type: general-4core
  spot:
    enabled: true           # restartable ELT tolerates preemption
    on_demand_driver: true  # keep the driver stable
  tags:
    cost_center: masar-data-platform
    workload: elt-nightly
```

## Hands-on Lab 2 — Cost and Elasticity Model for Masar

| | |
|---|---|
| **Objective** | Produce a defensible model comparing a coupled warehouse to a decoupled Lakehouse for Masar's data, backed by a measured Spark benchmark of data-skipping |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab2-start`; `silver.trips` sample from the solution branch available under `lakehouse/silver/trips` |

**Instructions & tasks**

1. *(10 min)* Fill `PRICES` in `cost_model.py` with your chosen cloud's real object-storage and core-hour prices (cite the source in `LAB2_NOTES.md`).
2. *(10 min)* Model Masar's storage: estimate 36 months of raw + curated data in GB and compute storage cost. Model three jobs (nightly ELT, hourly stream compaction, weekly feature build) and compute the compute cost. Record the `compute_share`.
3. *(10 min)* Run `scan_cost.py`. Capture the two `explain("formatted")` plans; confirm the pruned query shows `PushedFilters` and fewer columns. Record bytes/partitions read if surfaced.
4. *(10 min)* Build a one-page comparison table: coupled warehouse (always-on, sized for storage) vs decoupled Lakehouse (object storage + ephemeral compute). State the break-even and the dominant cost driver.
5. *(5 min)* Write the `autotermination_minutes` and `spot` guardrail rationale in `LAB2_NOTES.md`.
6. *(5 min)* Commit: `feat(econ): cost model + data-skipping benchmark for Masar`.

**Expected output**
```
$ python -m masar.econ.cost_model
{'storage': 276.0, 'compute': 118.4, 'total': 394.4, 'compute_share': 0.3}
$ python -m masar.econ.scan_cost lakehouse/silver/trips
riyadh trips (all cols)=? (pruned)=?   # equal counts
# plan shows: PushedFilters: [EqualTo(city, Riyadh)], ReadSchema: 3 cols
```

**Acceptance criteria**
- Cost model runs and separates storage vs compute with a stated dominant driver.
- Data-skipping benchmark shows pushdown + column pruning in the physical plan.
- `LAB2_NOTES.md` states a break-even and justifies the elasticity guardrails.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Pruned and naive plans look identical | Filtered after collecting; no pushdown | Filter on the DataFrame before actions; keep Delta stats |
| `compute_share` ~1.0 unexpectedly | Storage GB under-estimated | Recount history months × daily volume |
| Prices "feel wrong" | Mixed per-GB vs per-TB units | Normalise all prices to per-GB-month / per-core-hour |
| No `PushedFilters` in plan | Column not in Parquet stats | Ensure filter column is native, not derived |

**Instructor notes.** The aha-moment is `compute_share`: participants usually expect storage to dominate and are surprised it's the smaller, steady line. Fast finishers: model a spot-vs-on-demand comparison for the weekly feature build and quantify the 60–90% spot saving against interruption risk.

## Mini Exercises

**Quiz (5 questions)**
1. In a decoupled architecture, what physically holds the data? → object storage.
2. Name two Parquet properties that make remote reads cheap. → columnar/column-pruning; row-group min/max stats for data skipping (also compression).
3. Which cost axis is usually the controllable lever in an AI-data platform? → compute (elastic), not storage.
4. Why is idle-termination mandatory on autoscaling clusters? → elastic scale means an unbounded bill for idle compute.
5. True/False: decoupling always lowers the total bill regardless of table layout. → **False** — poor partitioning can raise compute (scan) cost.

**Debugging exercise.** Give a plan where a filter is applied *after* a `collect()`; the scan reads the whole table. Fix by pushing the filter into the DataFrame and confirm `PushedFilters` appears.

**Estimation exercise.** Masar adds a new city doubling daily GPS volume. Which line item grows, by how much, and does it change the compute/storage balance?

**Discussion questions.**
- When is a *coupled* warehouse still the right call? (ultra-low-latency, high-concurrency BI with tiny data)
- Your ad-hoc analysts occasionally run runaway queries. How does decoupling turn that from a platform-wide outage into a contained cost?

## Case Study — The Surprise Cloud Bill at "Tabadul" Analytics

**Scenario.** "Tabadul" (تبادل), a data-analytics unit, migrated to a Lakehouse expecting savings. The first month's bill *rose* 20%. Leadership is questioning the migration.

**Business context.** The unit serves 40 BI dashboards refreshing every 15 minutes plus a nightly ML feature build. The migration business case promised 40% savings.

**Technical challenge.** Every dashboard query full-scans an unpartitioned, uncompacted gold table; autoscaling clusters never idle-terminate; jobs run on-demand where spot would do.

**Constraints.** Cannot change the dashboards' refresh cadence; must show savings within 60 days; data volumes are growing 8%/month.

**Solution approach (facilitate, don't lecture).** Attack scan cost and idle cost: (1) partition/ZORDER + compact the gold marts so dashboards scan a fraction of the data; (2) cache the hottest marts near the BI engine; (3) set idle-termination and move restartable jobs to spot; (4) attribute cost per dashboard with tags to find the worst offenders.

**Discussion questions.**
1. Why did decoupling *alone* not deliver savings?
2. Which fix yields the most savings per engineering hour — compaction, caching, or idle-termination?
3. How would you present month-two numbers to rebuild leadership trust?
4. What guardrail prevents this recurring as data grows 8%/month?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Cost model completeness | Analysis | separates storage vs compute, states driver | model output + notes |
| Data-skipping proven | Performance | pruned plan shows `PushedFilters` + fewer cols | `explain("formatted")` |
| Bytes scanned reduction | Performance | pruned query reads ≤ 25% of naive columns | column count in plan |
| Elasticity guardrails | Governance | idle-termination + bounded autoscale specified | cluster YAML |
| Break-even identified | Analysis | stated with assumptions | LAB2_NOTES |

**Example benchmark table (filled during lab):**

| Query | Columns read | Filter pushdown | Relative bytes scanned |
|---|---|---|---|
| naive full read | 14 / 14 | no | 1.00 |
| column-pruned | 3 / 14 | no | 0.28 |
| pruned + partition filter | 3 / 14 | yes (city, date) | 0.06 |

## Required Visuals and Training Assets

### Diagrams
1. **Coupled vs decoupled** — *Purpose:* the module's core mental model. *Elements:* left, one box where storage disks and compute cores are fused; right, a storage bucket and a separate elastic cluster connected by a network line, each with its own scaling arrow. *Style:* side-by-side, English labels + Arabic subtitles.
2. **Parquet anatomy** — *Purpose:* explain why remote reads are cheap. *Elements:* a Parquet file split into row groups with per-column min/max stats; a query highlighting only 3 columns and skipping 2 row groups. *Style:* exploded file diagram.
3. **Elasticity spectrum** — *Purpose:* map job patterns to compute models. *Elements:* a line from fixed → autoscale → ephemeral → serverless with a Masar job placed on each. *Style:* horizontal spectrum with icons.
4. **Cost-driver bar** — *Purpose:* make `compute_share` visceral. *Elements:* stacked bar of storage (small, steady) vs compute (large, variable) for Masar. *Style:* single annotated stacked bar.

### Images (screenshots)
1. **`explain("formatted")` output** — the physical plan with `PushedFilters` and reduced `ReadSchema` highlighted; *why:* proof of data skipping.
2. **Cluster config UI** — an autoscaling cluster showing idle-termination and spot settings; *why:* the guardrails made real.
3. **Cost dashboard** — a tagged cost breakdown by workload; *why:* attribution enables control.

### Simulations
1. **Runaway idle cluster** — *Setup:* a cluster with no idle-termination left "on" for a simulated weekend. *Expected behaviour:* the cost model shows a large idle-compute charge. *Learning objective:* elasticity without termination is a liability.
2. **Full-scan tax** — *Setup:* an unpartitioned gold table queried 40 times. *Expected behaviour:* scan bytes (and cost) 15× a partitioned equivalent. *Learning objective:* layout is a cost control.

### Interactive Activities
- **Cost-model clinic (20 min):** teams swap cost models and stress-test each other's assumptions (history months, run frequency, idle time).
- **"Fixed, elastic, or serverless?" sort (10 min):** ten job patterns matched to the cheapest compute model with justification.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `silver/trips` (sample) | Solution branch of Masar | Delta | ~1.4M rows | Data-skipping benchmark |
| `prices_reference.csv` | Curated public cloud list prices (as-of date noted) | CSV | ~30 rows | Cost-model inputs |

### Demo Requirements
- **Instructor demo:** run the same query naive vs pruned vs partition-filtered and read the shrinking `ReadSchema`/scan in the plan live — watching bytes-scanned fall is the module's payoff.

---

# Module 3 — ETL versus ELT in Modern Stacks

## Module Overview

**Purpose.** How data moves from raw to usable is the daily work of data engineering. This module teaches the shift from **ETL** (transform before loading) to **ELT** (load raw, then transform inside the platform) that the Lakehouse enables, and equips participants to build ELT pipelines that are **incremental, idempotent, tested, and documented** using dbt over the Spark/Delta Lakehouse. This is where Masar's bronze becomes a trustworthy `silver.trips`.

**Business relevance.** ELT is now the default for cloud analytics because storage is cheap enough to keep raw data and compute is elastic enough to transform on demand. For Saudi teams this means faster iteration (transform logic changes without re-ingesting), full auditability (raw is retained), and transformations expressed as reviewable, tested SQL that analysts — not only engineers — can own.

**Industry use cases.**
- A bank lands raw transactions untouched (regulatory retention) and derives risk features as versioned dbt models rerun whenever logic changes.
- A telecom backfills three months of a corrected churn feature by re-running one incremental model, no re-ingestion.
- A government analytics unit exposes a self-documenting dbt project so auditors can trace every KPI to its raw source.

**Expected competencies.** After this module a participant can contrast ETL and ELT and justify ELT on a Lakehouse; structure a dbt project into staging/intermediate/mart layers; write incremental, idempotent models; add source-freshness and data tests; and produce a conformed `silver.trips` from bronze.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Contrast ETL and ELT and justify ELT for cloud Lakehouse environments | LO3 |
| 3.2 | Structure a transformation project into staging → intermediate → mart layers | LO3 |
| 3.3 | Implement incremental, idempotent transformations that support safe backfills | LO3 |
| 3.4 | Add source-freshness, schema, and data-quality tests to a pipeline | LO3, LO6 |
| 3.5 | Produce a conformed `silver.trips` model from bronze feeds | LO3, LO7 |

## Technical Content

### 1. ETL vs ELT — and why ELT won on the cloud

**ETL** (Extract → Transform → Load) transforms data *before* it lands in the analytics store. It was born when storage was expensive and warehouses rigid: you could not afford to keep raw data, so you cleaned and shaped it in a separate engine first, loading only the finished product. The cost: raw data is discarded (no reprocessing), transformation logic lives in a separate tool, and any logic change means re-extracting from source.

**ELT** (Extract → Load → Transform) lands **raw** data first (this is bronze) and transforms it **inside** the platform using its own elastic compute (Spark/SQL producing silver and gold). Cheap object storage makes keeping raw affordable; elastic compute makes in-platform transformation practical. The payoffs are exactly the medallion virtues:

- **Reprocessing:** raw is retained, so a fixed transformation can be rerun over all history.
- **Auditability:** every curated value traces back to an untouched source row.
- **Velocity:** changing logic is a code change + rerun, never a re-ingestion.
- **Ownership:** transformations are SQL/dbt models reviewable by analysts and engineers alike.

ETL still has its place — heavy transformation before a real-time sink, or when a source must be masked before it ever lands (some PII cases). But for an AI-data Lakehouse, **ELT is the default**, and this course builds ELT.

### 2. dbt as the transformation framework

**dbt** (data build tool) organises SQL transformations into a dependency graph of **models**. Each model is a `SELECT` that dbt materialises as a table/view; models reference each other with `ref()`, and sources with `source()`, so dbt builds a DAG and runs models in the right order. On this course dbt runs against the Spark/Delta Lakehouse (`dbt-spark`), transforming bronze Delta into silver/gold Delta.

The conventional layering (which mirrors medallion):

| dbt layer | Medallion | Purpose | Materialisation |
|---|---|---|---|
| **staging** (`stg_`) | bronze → | 1:1 with a source: rename, cast, light clean; no joins | view or incremental |
| **intermediate** (`int_`) | → silver | reusable joins/derivations shared by marts | ephemeral/view |
| **marts** (`silver.` / `gold.`) | silver, gold | conformed entities and business aggregates | table / incremental |

Why this matters: staging isolates source quirks in one place, intermediate removes duplication, and marts are the stable contract consumers read. Renaming a source column touches exactly one staging model.

### 3. Idempotency and incremental models

Two properties separate a hobby pipeline from a production one:

**Idempotency** — running the transformation twice yields the same result as running it once. This is what makes retries, backfills, and disaster recovery safe. A `MERGE` keyed on `trip_id` is idempotent (re-applying the same rows changes nothing); a blind `INSERT` is not (it duplicates). Everything downstream of bronze in this course is idempotent by design.

**Incremental processing** — reprocessing only new/changed data instead of the whole table. On day 400 you do not re-transform 400 days of trips; you transform the last day and merge it in. dbt's `incremental` materialisation expresses this: on first run it builds the full table; on later runs it processes only rows passing an `is_incremental()` filter and merges them on a unique key.

The subtlety the module drills: **late-arriving data**. A trip that ended yesterday may only reach bronze today. A naive `WHERE event_date = today` misses it. The fix is a **lookback window** (reprocess the last N days) plus a merge on `trip_id`, so late rows are corrected without duplicating settled ones. This is the single most common real-world pipeline bug.

### 4. Testing and documentation as part of the pipeline

In ELT, tests are not an afterthought — they are declared alongside the models and run every build:

- **Source freshness:** assert bronze received data recently (`loaded_at` within N hours) — catches upstream outages.
- **Schema/constraint tests:** `unique`, `not_null`, `accepted_values`, `relationships` (referential integrity to a dimension).
- **Custom data tests:** SQL that must return zero rows (e.g., `fare_sar <= 0` or `end_ts < start_ts`).

dbt also generates **documentation and lineage** from the same project: `dbt docs` renders the DAG and every model/column description, giving the audit trail M6 and Saudi PDPL governance depend on. Testing and docs live *with* the transformation, so they never drift from it.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Raw in, logic on top:* never mutate bronze; all shaping is a downstream model.
- *One responsibility per model:* staging cleans, intermediate joins, marts aggregate — do not collapse them.
- *Idempotent by construction:* prefer MERGE-on-key over INSERT; a rerun must be a no-op.
- *Test at the boundary:* enforce the schema contract where silver is produced, not scattered downstream.

**Common mistakes (each appears in the Lab 3 starter deliberately)**
1. `WHERE date = current_date` with no lookback → silently drops late-arriving trips.
2. Full-refreshing a huge table every run because the incremental key/filter is wrong → slow and expensive.
3. Deduplicating with `DISTINCT` instead of "latest row per key" → keeps stale versions when a trip is corrected.
4. Casting/renaming in marts instead of staging → source quirks leak everywhere; a rename breaks ten models.
5. No `not_null`/`unique` test on the silver key → duplicate `trip_id` slips through to features and BI.
6. Timezone drift: mixing UTC and Asia/Riyadh timestamps → "yesterday" means different things in two models.

**Production considerations**
- Schedule freshness checks *before* the transform; a stale source should fail loudly, not silently produce yesterday's mart.
- Backfills are first-class: parameterise the date range so a corrected model can rerun over history safely (idempotency guarantees correctness).
- Keep transformation code in version control with the same review gates as application code; the DAG is production infrastructure.

### 6. Real-world example walkthrough

Narrate this (5 minutes): a mobility team's daily "trips completed" model used `WHERE trip_date = current_date()`. Trips whose payment settled after midnight arrived in bronze the next morning and were never counted — a ~2% silent undercount that skewed driver incentives and a demand model's training labels for months. The fix was three lines: a 3-day lookback window, an incremental merge on `trip_id`, and a `unique` test on the key. No re-ingestion, no new tool — just idempotent, incremental ELT done correctly. The undercount went to zero and the backfill corrected six months of history in one parameterised run. Masar's `silver.trips` is built to avoid exactly this.

## Code Examples

### dbt sources and a staging model (isolate source quirks)

```sql
-- models/staging/masar/_masar__sources.yml
-- Declares bronze Delta tables as dbt sources + a freshness SLA.
version: 2
sources:
  - name: bronze
    schema: bronze
    tables:
      - name: trips
        loaded_at_field: _ingested_at
        freshness:                 # fail the build if bronze is stale
          warn_after:  {count: 6,  period: hour}
          error_after: {count: 24, period: hour}
      - name: drivers
```

```sql
-- models/staging/masar/stg_trips.sql
-- Staging: 1:1 with source. Rename, cast, light clean. NO joins, NO business logic.
with source as (
    select * from {{ source('bronze', 'trips') }}
),
renamed as (
    select
        cast(trip_id as string)                      as trip_id,
        cast(rider_id as string)                     as rider_id,
        cast(driver_id as string)                    as driver_id,
        initcap(trim(city))                          as city,
        -- normalise every timestamp to Asia/Riyadh ONCE, here
        to_timestamp(request_ts)                     as requested_at,
        to_timestamp(start_ts)                       as started_at,
        to_timestamp(end_ts)                         as ended_at,
        cast(distance_km as double)                  as distance_km,
        cast(fare_sar as double)                     as fare_sar,
        cast(surge_multiplier as double)             as surge_multiplier,
        lower(trim(payment_method))                  as payment_method,
        lower(trim(status))                          as status,
        _ingested_at
    from source
    where trip_id is not null           -- drop unkeyed garbage at the boundary
)
select * from renamed
```

### Incremental, idempotent `silver.trips` with a lookback window

```sql
-- models/marts/silver/silver_trips.sql
{{ config(
    materialized='incremental',
    incremental_strategy='merge',
    unique_key='trip_id',
    file_format='delta',
    on_schema_change='append_new_columns'
) }}

with trips as (
    select * from {{ ref('stg_trips') }}

    {% if is_incremental() %}
      -- LOOKBACK: reprocess a 3-day window so late-arriving trips are
      -- corrected (merged), not missed. Merge-on-trip_id => idempotent.
      where started_at >= (
        select dateadd(day, -3, max(started_at)) from {{ this }}
      )
    {% endif %}
),
drivers as (
    select * from {{ ref('stg_drivers') }}
),
joined as (
    select
        t.trip_id, t.rider_id, t.driver_id, t.city,
        t.requested_at, t.started_at, t.ended_at,
        t.distance_km, t.fare_sar, t.surge_multiplier,
        t.payment_method, t.status,
        d.vehicle_type, d.driver_rating,
        -- derived features (single source of truth for downstream AI/BI)
        (unix_timestamp(t.ended_at) - unix_timestamp(t.started_at)) / 60.0
            as duration_min,
        t.fare_sar / nullif(t.distance_km, 0)          as fare_per_km,
        hour(t.started_at)                             as start_hour,
        case when hour(t.started_at) < 6 then 1 else 0 end as is_night
    from trips t
    left join drivers d on t.driver_id = d.driver_id
    where t.status = 'completed'          -- silver = conformed, valid trips
      and t.ended_at > t.started_at       -- reject impossible durations
)
select * from joined
```

### Tests and freshness declared with the model (governance-as-code)

```yaml
# models/marts/silver/_silver__models.yml
version: 2
models:
  - name: silver_trips
    description: "Conformed, completed Masar trips. One row per trip_id."
    columns:
      - name: trip_id
        description: "Business key. Unique, non-null."
        tests: [unique, not_null]
      - name: fare_sar
        tests:
          - dbt_utils.accepted_range: {min_value: 0, inclusive: false}
      - name: city
        tests:
          - accepted_values:
              values: ['Riyadh', 'Jeddah', 'Dammam', 'Mecca', 'Medina']
      - name: driver_id
        tests:
          - relationships:
              to: ref('stg_drivers')
              field: driver_id
```

## Hands-on Lab 3 — Build the ELT Pipeline to `silver.trips`

| | |
|---|---|
| **Objective** | Build a dbt (on Spark/Delta) pipeline transforming bronze into a tested, incremental, conformed `silver.trips`, and prove it handles a late-arriving-data backfill correctly |
| **Duration** | 90 minutes (Labs 3a + 3b across two sessions) |
| **Setup** | `pip install dbt-core dbt-spark`; `git checkout lab3-start`; bronze from Lab 1 present; `dbt debug` green |

**Instructions & tasks**

1. *(15 min, 3a)* Declare bronze `trips`/`drivers`/`gps` as dbt sources with a 6h/24h freshness SLA. Run `dbt source freshness`.
2. *(15 min, 3a)* Write `stg_trips` and `stg_drivers`: rename, cast, normalise timestamps to Asia/Riyadh, drop null keys. Materialise as views. Run `dbt run --select staging`.
3. *(20 min, 3b)* Write `silver_trips` as an **incremental merge** on `trip_id` with a 3-day lookback; join drivers; derive `duration_min`, `fare_per_km`, `start_hour`, `is_night`; keep only completed, valid trips.
4. *(15 min, 3b)* Add the `unique`/`not_null`/`accepted_values`/`relationships`/range tests. Run `dbt test`; fix any failures by correcting logic (not by deleting the test).
5. *(15 min, 3b)* **Backfill drill:** land a late-arriving trip (ended yesterday, arriving today) into bronze; run `dbt run` incrementally; confirm the trip is merged **once**, not missed and not duplicated.
6. *(5 min)* Run `dbt docs generate`; open the lineage graph. Commit: `feat(silver): incremental conformed trips with tests + freshness`.
7. *(5 min)* Record row counts and test results in `LAB3_NOTES.md`.

**Expected output**
```
$ dbt run --select silver_trips
1 of 1 OK created incremental model silver.silver_trips ... [MERGE 1,203 in 4.1s]
$ dbt test --select silver_trips
Completed successfully. PASS=7 WARN=0 ERROR=0 SKIP=0
$ dbt run --select silver_trips   # after landing 1 late trip
1 of 1 OK ... [MERGE 1 in 1.8s]        # late trip merged once
```

**Acceptance criteria**
- `silver.trips` is incremental, merge-on-`trip_id`, with a working lookback window.
- All declared tests pass; the schema contract (unique/not-null key) is enforced.
- The backfill drill shows the late trip counted exactly once (idempotent).

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Late trip missing after run | Lookback too short / filter on wrong column | Widen window; filter on `started_at`, not ingest time |
| Duplicate `trip_id` in silver | INSERT strategy, not MERGE | Set `incremental_strategy='merge'`, `unique_key` |
| Full refresh every run | `is_incremental()` block skipped | Confirm the model already exists; check `{% if is_incremental() %}` |
| `relationships` test fails | Trips reference unknown driver | Left-join + flag orphan drivers; discuss whether to quarantine |
| Timezone off by 3h | Mixed UTC/Riyadh | Normalise in staging only, once |

**Instructor notes.** The backfill drill (task 5) is the module's whole point — do not let pairs skip it. Walk the room during it and confirm each pair *sees* the merge count = 1. Fast finishers: add an `int_trip_payments` intermediate model and refactor a duplicated join into it.

## Mini Exercises

**Quiz (5 questions)**
1. What does ELT keep that ETL discards, enabling reprocessing? → raw data (bronze).
2. Which dbt function creates the model dependency DAG? → `ref()` (and `source()`).
3. Why is MERGE-on-key idempotent but INSERT is not? → re-applying the same rows via MERGE changes nothing; INSERT duplicates.
4. What bug does a lookback window fix? → late-arriving data being missed by a `date = today` filter.
5. True/False: staging models should contain business joins. → **False** — staging is 1:1 with a source; joins belong in intermediate/marts.

**Debugging exercise.** Give a `silver_trips` with `WHERE started_at = current_date()` and no merge. Symptom: yesterday's late trips vanish and counts drift. Fix with lookback + merge; verify with the backfill drill.

**Refactor exercise.** A mart casts and renames 20 columns inline. Move all casting/renaming into staging and show that a source rename now touches one model.

**Discussion questions.**
- When is ETL (transform-before-load) still the right choice? (mask PII before landing; heavy pre-aggregation for a low-latency sink)
- Who should own dbt models — a central data-engineering team or embedded analysts? What governance makes the answer safe?

## Case Study — The Silent Undercount at "Wusool" Mobility

**Scenario.** "Wusool" (وصول) pays driver incentives from a daily "completed trips" figure. Drivers complain the count is low; finance insists it is right.

**Business context.** Incentives total SAR 2M/month; a systematic undercount underpays drivers and, worse, feeds skewed labels into a demand-forecasting model.

**Technical challenge.** The daily model filters `trip_date = current_date()`; trips settling after midnight arrive next-day in bronze and are never counted.

**Constraints.** Cannot re-ingest source (retention/immutability); must correct six months of history; the fix must be auditable for a labour-relations review.

**Solution approach (facilitate, don't lecture).** Convert the model to incremental merge-on-`trip_id` with a 3-day lookback; parameterise a full backfill over six months; add a `unique` test and a "no future timestamps" data test; regenerate docs so the labour review can trace the corrected number to raw.

**Discussion questions.**
1. Why did the original filter feel correct yet undercount?
2. How does idempotency make the six-month backfill safe to run (even twice)?
3. What downstream AI harm did the label skew cause, and how would you detect it?
4. What test, added earlier, would have caught this in week one?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Silver conformance | Correctness | 1 row per `trip_id`, key tests pass | `dbt test` |
| Incrementality | Performance | rerun processes only lookback window | run log MERGE count |
| Backfill correctness | Correctness | late trip counted exactly once | backfill drill |
| Test coverage | Quality | ≥ 6 tests incl. unique/not_null/relationships | dbt test summary |
| Freshness SLA | Observability | bronze freshness enforced (6h warn/24h error) | `dbt source freshness` |

**Example benchmark table (filled during lab):**

| Run | Rows processed | Strategy | Duration | Duplicate keys |
|---|---|---|---|---|
| initial full build | 1,410,000 | create | 22 s | 0 |
| incremental (1 day) | 48,200 | merge | 4.1 s | 0 |
| incremental (1 late trip) | 1 | merge | 1.8 s | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **ETL vs ELT** — *Purpose:* the module's headline contrast. *Elements:* two pipelines; ETL transforms before a warehouse (raw discarded), ELT loads raw to bronze then transforms in-platform (raw retained). *Style:* stacked comparison, English + Arabic subtitles.
2. **dbt DAG for Masar** — *Purpose:* show layering. *Elements:* sources → `stg_*` → `int_*` → `silver_trips` → gold, with test icons on edges. *Style:* left-to-right graph matching medallion colours.
3. **Late-arriving-data lookback** — *Purpose:* make the core bug/fix visual. *Elements:* a timeline where a trip lands a day late; a naive `=today` filter misses it; a lookback window catches and merges it. *Style:* annotated timeline, before/after.
4. **Idempotent merge** — *Purpose:* show why reruns are safe. *Elements:* the same batch applied twice with MERGE → identical table; with INSERT → duplicates. *Style:* two side-by-side outcomes.

### Images (screenshots)
1. **`dbt docs` lineage graph** — the rendered DAG; *why:* audit/lineage evidence for governance.
2. **`dbt test` summary** — PASS/WARN/ERROR counts; *why:* tests-as-part-of-pipeline made concrete.
3. **Backfill run log** — the MERGE-count = 1 line for the late trip; *why:* proof of idempotency.

### Simulations
1. **Late-arrival undercount** — *Setup:* branch `sim-undercount` uses `=current_date()`; a late trip is injected. *Expected behaviour:* daily count is ~2% low with no error. *Learning objective:* silent correctness bugs need tests + lookback.
2. **Non-idempotent rerun** — *Setup:* branch swaps MERGE for INSERT. *Expected behaviour:* rerunning doubles rows. *Learning objective:* idempotency is a design property, not luck.

### Interactive Activities
- **DAG-building on the wall (15 min):** teams arrange model cards (sources, staging, intermediate, marts) into a valid dbt DAG and mark where tests attach.
- **"Where does this logic live?" sort (10 min):** 12 snippets (rename, timezone cast, driver join, night flag, KPI aggregate) placed on staging/intermediate/mart.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `bronze/trips`, `bronze/drivers` | From Lab 1 landing | Delta | ~1.4M / 3.4k rows | ELT source |
| `late_trip_2026-06-15.csv` | Injected late-arrival fixture | CSV | 1 row | Backfill drill |
| `drivers.csv` (mixed date formats) | Masar dimension | CSV | 3,450 rows | Staging cast exercise |

### Demo Requirements
- **Instructor demo:** run `dbt run` twice and land a late trip between runs, narrating the MERGE count — the "processes only what changed, corrects late data, never duplicates" rhythm is the module in 6 minutes.

---

# Module 4 — Delta Lake and ACID Transactions

## Module Overview

**Purpose.** This is the technical heart of the course. Delta Lake is the transaction layer that turns Masar's Parquet files into a reliable **Lakehouse table**: ACID transactions, schema enforcement, upserts (MERGE), time travel, and maintenance (OPTIMIZE/VACUUM). Participants stop treating tables as "folders of files you hope are consistent" and start treating them as transactional objects with a durable, auditable history.

**Business relevance.** ACID on the lake is what lets a Saudi bank or mobility operator trust a single copy of data for both regulators and data scientists. No half-written files, no dirty reads during a concurrent write, no silent schema corruption, and — critically for audit and PDPL — a complete, queryable version history of every change. Time travel alone justifies Delta for many compliance teams: you can prove exactly what a table contained on any past date.

**Industry use cases.**
- A payments firm applies GDPR/PDPL "right to erasure" by MERGE-deleting a rider's rows and VACUUMing history, with an auditable commit.
- A risk team reproduces last quarter's model by reading the exact table `VERSION AS OF` the training date.
- An ops pipeline ingests concurrent streaming and batch writes to the same trips table without corruption, thanks to optimistic concurrency.

**Expected competencies.** After this module a participant can explain the Delta transaction log and ACID guarantees; create Delta tables with enforced/evolving schema and constraints; perform MERGE upserts and deletes; use time travel; and run OPTIMIZE/ZORDER/VACUUM maintenance with correct retention reasoning.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Explain the Delta transaction log and how it delivers ACID on object storage | LO4 |
| 4.2 | Create Delta tables with schema enforcement, evolution, and CHECK constraints | LO4 |
| 4.3 | Perform idempotent MERGE upserts and compliant deletes | LO4 |
| 4.4 | Use time travel to audit and reproduce historical table states | LO4 |
| 4.5 | Maintain tables with OPTIMIZE, ZORDER, and VACUUM using correct retention | LO4, LO2 |

## Technical Content

### 1. The transaction log: how Delta delivers ACID on files

A Delta table is a directory of Parquet data files plus a `_delta_log/` directory of ordered **commit files** (`00000000000000000000.json`, `...001.json`, …). Each commit is an atomic record of *actions*: which Parquet files were **added** and which were **removed** by that transaction, plus metadata (schema, stats). The current table state is the result of replaying the log; periodically Delta writes a **checkpoint** (Parquet) so readers don't replay thousands of JSON commits.

This log is the whole trick. It delivers **ACID**:
- **Atomicity:** a write is one commit — either the commit file appears (all its file-adds visible) or it doesn't. No half-written table.
- **Consistency:** schema and constraints are checked before a commit is accepted.
- **Isolation:** readers see a consistent **snapshot** (the log up to version *v*); a concurrent writer adding version *v+1* does not affect them (*snapshot isolation*).
- **Durability:** commits and data live in durable object storage.

Concurrency uses **optimistic concurrency control**: a writer reads the current version, prepares its changes, then attempts to commit as the next version; if another writer got there first, it retries against the new state. This is why concurrent streaming + batch writes to Masar's trips table don't corrupt it.

**Instructor note:** open `_delta_log/*.json` live and read the `add`/`remove` actions aloud — seeing the log demystifies everything else in the module.

### 2. Schema enforcement and evolution

By default Delta **enforces schema on write**: a write whose columns/types don't match the table is rejected, not silently coerced. This is the guarantee a raw lake lacks — the reason a lake becomes a swamp. For Masar it means a source that suddenly sends `fare_sar` as a string fails loudly at the silver boundary instead of poisoning features.

When schema change is *intended*, Delta supports controlled **evolution**:
- `mergeSchema` / `on_schema_change='append_new_columns'` adds genuinely new columns.
- Type-widening and column renames are explicit operations, logged as metadata commits.

The principle: **schema changes are events you decide and record**, never accidents you discover in production. Enforcement is the default; evolution is opt-in and audited.

### 3. MERGE: upserts, CDC, and compliant deletes

`MERGE INTO ... USING ... ON ... WHEN MATCHED ... WHEN NOT MATCHED` is Delta's workhorse. It expresses **upserts** (insert new, update existing) atomically and idempotently on a key — the same operation dbt used in M3, now understood at the storage layer. Three Masar patterns:

- **Correction upsert:** a re-scored or corrected trip updates its row in place, keyed on `trip_id`.
- **CDC apply:** a stream of change events (insert/update/delete flags) is merged to keep silver in sync with a source.
- **Compliant delete:** `DELETE FROM silver_trips WHERE rider_id = :id` removes a rider's data for a PDPL erasure request — atomically, with an auditable commit, and (after VACUUM) physically gone from history.

Because MERGE is atomic and keyed, it is safe to retry — the backbone of idempotent pipelines.

### 4. Time travel: audit and reproducibility

Every commit is a version, so Delta can read the table **as of** any past version or timestamp:

```sql
SELECT * FROM silver_trips VERSION AS OF 42;
SELECT * FROM silver_trips TIMESTAMP AS OF '2026-06-15';
```

Uses that matter in Saudi enterprise contexts:
- **Audit:** prove what a regulatory report was computed from on its filing date.
- **Reproducibility:** retrain a model on the *exact* feature table version used originally — the antidote to "the numbers changed and we don't know why".
- **Recovery:** a bad MERGE is undone by `RESTORE TABLE ... TO VERSION AS OF n`.

Time travel is bounded by retention (VACUUM, §5) — you can travel back only as far as history has not been vacuumed.

### 5. Table maintenance: OPTIMIZE, ZORDER, VACUUM, small files

Streaming and frequent writes create the **small-files problem**: thousands of tiny Parquet files that make object-storage *listing* and reads slow and costly (the very cost M2 warned about). Delta's maintenance tools:

- **OPTIMIZE** — compacts many small files into fewer right-sized ones (~128MB–1GB). Dramatically speeds reads.
- **ZORDER BY (cols)** — co-locates related data (e.g., `city`, `started_at`) within files so data-skipping prunes more aggressively; multi-dimensional clustering.
- **VACUUM** — physically deletes data files no longer referenced by the log **older than a retention window** (default 7 days). This reclaims storage — but it also **removes time-travel history** beyond that window, so retention is a governance decision balancing cost, audit, and PDPL erasure obligations.

The retention tension is a key teaching point: aggressive VACUUM saves storage but destroys the audit trail; conservative VACUUM preserves history but costs storage and can retain data a PDPL erasure was supposed to remove. There is no universal right answer — only a documented, defensible one.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *The log is the source of truth:* never hand-edit Parquet files under a Delta table; go through the API so commits stay consistent.
- *Enforce by default, evolve on purpose:* schema surprises are bugs; schema changes are reviewed events.
- *Idempotent writes:* MERGE-on-key everywhere corrections happen.
- *Maintenance is not optional:* OPTIMIZE/VACUUM are scheduled operations, like backups.

**Common mistakes (each appears in the Lab 4 starter deliberately)**
1. `VACUUM ... RETAIN 0 HOURS` to "save space" — destroys time travel and can break concurrent readers; also blocked by default safety.
2. Over-partitioning by `trip_id` → millions of one-row files; the small-files problem self-inflicted.
3. Writing raw Parquet next to a Delta table's files, corrupting the log's view of reality.
4. Relying on `overwrite` where a MERGE was needed → losing concurrent writers' rows.
5. Assuming a `DELETE` immediately frees storage or erases history — it only tombstones until VACUUM.
6. Ignoring OPTIMIZE on a streaming sink → read performance decays daily.

**Production considerations**
- Schedule OPTIMIZE/ZORDER on hot tables (nightly) and VACUUM with a retention that satisfies both audit and PDPL.
- Use CHECK constraints (`fare_sar > 0`) and generated columns for partition keys to keep the table self-validating.
- Record the Delta version alongside model artefacts so any training run is reproducible via time travel.
- Monitor file counts and sizes; a rising small-file count is an early warning.

## Code Examples

### Creating an enforced Delta table with constraints

```python
# src/masar/delta/create_silver.py
"""Create silver.trips as a managed Delta table with enforced schema,
CHECK constraints, and partitioning chosen to AVOID the small-files trap.
"""
from delta.tables import DeltaTable
from masar.spark import get_spark

SILVER = "./lakehouse/silver/trips"


def create_silver_trips(staged_df) -> None:
    spark = get_spark()
    (staged_df.write
        .format("delta")
        .partitionBy("city")          # low-cardinality: 5 cities, not trip_id
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(SILVER))

    # Constraints are enforced on EVERY future write => self-validating table
    spark.sql(f"ALTER TABLE delta.`{SILVER}` "
              "ADD CONSTRAINT positive_fare CHECK (fare_sar > 0)")
    spark.sql(f"ALTER TABLE delta.`{SILVER}` "
              "ADD CONSTRAINT valid_duration CHECK (ended_at > started_at)")
```

### Idempotent MERGE upsert (corrections) and a PDPL-compliant delete

```python
# src/masar/delta/merge_ops.py
"""Upsert corrected trips and apply a PDPL right-to-erasure delete.

Both are atomic Delta commits: auditable, retryable, isolated from readers.
"""
from delta.tables import DeltaTable
from masar.spark import get_spark

SILVER = "./lakehouse/silver/trips"


def upsert_corrections(corrections_df) -> None:
    """MERGE keyed on trip_id => re-running is a no-op (idempotent)."""
    spark = get_spark()
    target = DeltaTable.forPath(spark, SILVER)
    (target.alias("t")
        .merge(corrections_df.alias("s"), "t.trip_id = s.trip_id")
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute())


def erase_rider(rider_id: str) -> None:
    """PDPL Article: erase a data subject's rows. Atomic, logged commit.
    Physical removal from history completes at the next VACUUM.
    """
    spark = get_spark()
    target = DeltaTable.forPath(spark, SILVER)
    target.delete(f"rider_id = '{rider_id}'")
    print(f"erasure committed for {rider_id}; run VACUUM to purge history")
```

### Time travel for audit + reproducibility

```python
# src/masar/delta/time_travel.py
"""Read a past table state for audit or to reproduce a model's training set."""
from masar.spark import get_spark

SILVER = "./lakehouse/silver/trips"


def history() -> None:
    spark = get_spark()
    # Full audit trail: who/what/when for every commit
    spark.sql(f"DESCRIBE HISTORY delta.`{SILVER}`").show(truncate=False)


def as_of_version(v: int):
    spark = get_spark()
    return (spark.read.format("delta")
            .option("versionAsOf", v)
            .load(SILVER))


def as_of_date(ts: str):
    spark = get_spark()
    return (spark.read.format("delta")
            .option("timestampAsOf", ts)   # e.g. '2026-06-15 00:00:00'
            .load(SILVER))
```

### Maintenance: OPTIMIZE + ZORDER + VACUUM

```sql
-- src/masar/delta/maintain.sql  (run on a schedule, e.g. nightly)

-- 1) Compact small files and cluster by common filter columns
OPTIMIZE delta.`./lakehouse/silver/trips`
  ZORDER BY (city, started_at);

-- 2) Reclaim storage older than the retention window.
--    RETENTION IS A GOVERNANCE DECISION: 168h keeps 7 days of time travel.
--    Do NOT set 0 hours: it destroys audit history and can break readers.
VACUUM delta.`./lakehouse/silver/trips` RETAIN 168 HOURS;

-- 3) Verify: file count should drop sharply after OPTIMIZE
DESCRIBE DETAIL delta.`./lakehouse/silver/trips`;
```

## Hands-on Lab 4 — Delta Lake: ACID, MERGE, Time Travel, Maintenance

| | |
|---|---|
| **Objective** | Convert `silver.trips` to a constrained Delta table; perform idempotent MERGE upserts and a compliant delete; audit via time travel; and run OPTIMIZE/ZORDER/VACUUM, measuring the small-files improvement |
| **Duration** | 90 minutes (Labs 4a + 4b) |
| **Setup** | `git checkout lab4-start`; `silver_trips` from Lab 3 available; Delta enabled via `get_spark()` |

**Instructions & tasks**

1. *(15 min, 4a)* Write `silver.trips` as Delta partitioned by `city`; add `positive_fare` and `valid_duration` CHECK constraints. Open `_delta_log/` and read the first commit JSON's `add` actions aloud.
2. *(10 min, 4a)* Attempt to write a row with `fare_sar = -5`; confirm the constraint **rejects** it. Attempt a wrong-type write; confirm schema enforcement rejects it.
3. *(20 min, 4b)* Prepare a `corrections` DataFrame (5 trips with fixed fares). Run `upsert_corrections` **twice**; confirm the second run changes nothing (idempotent). Verify with `DESCRIBE HISTORY`.
4. *(10 min, 4b)* Time travel: read the table `VERSION AS OF` before the upsert; diff the corrected trips old vs new. Then `RESTORE` to that version and back to demonstrate recovery.
5. *(10 min, 4b)* PDPL drill: `erase_rider('rider_00042')`; confirm the rows are gone from the current version but still visible in the pre-delete version until VACUUM.
6. *(15 min, 4b)* Run `OPTIMIZE ... ZORDER BY (city, started_at)`, then `DESCRIBE DETAIL` before/after to record `numFiles`. Run `VACUUM ... RETAIN 168 HOURS`; explain in `LAB4_NOTES.md` why not 0.
7. *(10 min)* Commit: `feat(delta): constrained silver + merge/erasure + optimize/vacuum`.

**Expected output**
```
$ python -m masar.delta.merge_ops --corrections corrections.csv   # 2nd run
MERGE ... matched=5 updated=0   # idempotent: nothing changed second time
$ spark-sql -e "DESCRIBE DETAIL delta.\`.../silver/trips\`"
numFiles BEFORE optimize: 214    AFTER optimize: 9
$ python -m masar.delta.time_travel --version 6
rider_00042 present at v6 ; absent at current after erasure
```

**Acceptance criteria**
- Delta table enforces schema + CHECK constraints (bad writes rejected).
- MERGE is idempotent (second run: 0 updates); history recorded.
- Time travel reproduces a prior state; erasure removes current rows.
- OPTIMIZE reduces `numFiles` sharply; VACUUM retention justified.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `ConcurrentModificationException` | Two writers, optimistic conflict | Retry the commit; discuss OCC |
| VACUUM removes nothing | Files within retention window | Expected; explain default 7-day safety |
| `VACUUM RETAIN 0` blocked | Delta safety check | Keep it; do not disable the check in prod |
| Constraint not enforced | Added after bad rows exist | Constraints check future writes; clean existing first |
| Millions of tiny files | Partitioned by `trip_id` | Repartition by `city`; OPTIMIZE |

**Instructor notes.** The two showstopper moments: reading `_delta_log` JSON aloud (task 1) and the idempotent second MERGE showing 0 updates (task 3). Reserve time for both. Fast finishers: simulate a concurrent write from a second Spark session to trigger and observe optimistic-concurrency retry.

## Mini Exercises

**Quiz (5 questions)**
1. What directory makes a folder of Parquet a Delta table? → `_delta_log/`.
2. Which ACID property does snapshot isolation provide? → Isolation (readers see a consistent version).
3. Why is MERGE-on-key idempotent? → re-applying matched rows updates nothing new.
4. What does VACUUM trade away when it reclaims storage? → time-travel history beyond the retention window.
5. True/False: partitioning by `trip_id` improves performance. → **False** — it causes the small-files problem.

**Debugging exercise.** Give a table someone VACUUMed with `RETAIN 0 HOURS`; time travel now fails. Discuss the audit and concurrency damage and the correct retention policy.

**Concurrency exercise.** Two sessions MERGE into the same table simultaneously; observe the optimistic-concurrency retry. Explain why no corruption occurs.

**Discussion questions.**
- How long should Masar retain time-travel history? Balance audit needs against PDPL erasure (data should not live forever) and storage cost.
- A regulator asks "what did this table contain on 1 June?" How does Delta answer, and what must be true about VACUUM for the answer to exist?

## Case Study — Reproducing a Disputed Report at "Aman" Payments

**Scenario.** "Aman" (أمان) filed a regulatory settlement report from a Lakehouse table. Three weeks later the regulator disputes a figure; the table has since been updated by dozens of pipeline runs.

**Business context.** The dispute carries a potential penalty; Aman must prove exactly what the table held on the filing date.

**Technical challenge.** Reconstruct the table's state on the filing date and show the report is reproducible from it — without a manual backup.

**Constraints.** No separate snapshot was taken; VACUUM runs weekly with a 30-day retention; a rider erasure occurred after filing and must be honoured in current data but explained in the historical view.

**Solution approach (facilitate, don't lecture).** Use `TIMESTAMP AS OF` the filing date to read the exact historical table (retention covers it); recompute the report and match it; use `DESCRIBE HISTORY` to show the commit timeline; document how the post-filing erasure is reflected. Recommend a policy of tagging/pinning the version used for every regulatory filing.

**Discussion questions.**
1. Why is time travel superior to manual snapshot backups for audit?
2. What VACUUM retention would have made this impossible, and why?
3. How do you reconcile "reproduce the past" with "honour a PDPL erasure"?
4. What operational habit (versioning filings) prevents future disputes?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Schema/constraint enforcement | Correctness | bad writes rejected | negative-write test |
| MERGE idempotency | Correctness | 2nd run: 0 updates | run log + history |
| Small-files reduction | Performance | `numFiles` down ≥ 10× post-OPTIMIZE | `DESCRIBE DETAIL` |
| Data-skipping via ZORDER | Performance | city+time filtered query scans fewer files | query metrics |
| Time-travel audit | Governance | prior version reproducible | `VERSION AS OF` diff |
| VACUUM retention documented | Governance | ≥ 168h, justified vs PDPL | LAB4_NOTES |

**Example benchmark table (filled during lab):**

| Operation | Before | After | Note |
|---|---|---|---|
| `numFiles` | 214 | 9 | after OPTIMIZE |
| filtered read (Riyadh, June) | 1.9 s | 0.4 s | after ZORDER |
| MERGE (5 corrections) run 1 / run 2 | 5 updated / 0 updated | — | idempotent |
| storage reclaimed by VACUUM | — | 1.1 GB | retention 168h |

## Required Visuals and Training Assets

### Diagrams
1. **Delta transaction log** — *Purpose:* the module's core mental model. *Elements:* Parquet data files + a `_delta_log` stack of JSON commits (add/remove actions) + a checkpoint; an arrow showing "replay log → current state". *Style:* layered diagram, English + Arabic subtitles.
2. **ACID on the lake** — *Purpose:* map the four properties to Delta mechanisms. *Elements:* four labelled callouts (Atomic=one commit, Consistent=constraints, Isolated=snapshot, Durable=object store). *Style:* four-quadrant.
3. **Optimistic concurrency** — *Purpose:* show why concurrent writes don't corrupt. *Elements:* two writers reading v5, one commits v6, the other retries against v6. *Style:* sequence diagram.
4. **OPTIMIZE + VACUUM** — *Purpose:* small-files and retention. *Elements:* many tiny files compacting into few; a retention window past which VACUUM deletes and time travel ends. *Style:* before/after + timeline.

### Images (screenshots)
1. **`_delta_log/*.json` open in an editor** — the `add`/`remove` actions visible; *why:* demystifies ACID.
2. **`DESCRIBE HISTORY` output** — the commit timeline with operation types; *why:* audit trail made real.
3. **`DESCRIBE DETAIL` before/after OPTIMIZE** — `numFiles` dropping; *why:* small-files fix quantified.

### Simulations
1. **VACUUM-0 disaster** — *Setup:* branch `sim-vacuum0` sets `RETAIN 0`. *Expected behaviour:* time travel and a concurrent reader break. *Learning objective:* retention is governance, not a space hack.
2. **Small-files decay** — *Setup:* a streaming sink writes for "30 days" without OPTIMIZE. *Expected behaviour:* read latency climbs with file count. *Learning objective:* maintenance is scheduled, not optional.

### Interactive Activities
- **Log-replay by hand (15 min):** teams are given a stack of add/remove commit cards and reconstruct the current file set — becoming the Delta reader.
- **Retention debate (15 min):** two teams argue aggressive vs conservative VACUUM for Masar, judged on balancing audit, PDPL, and cost.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `silver/trips` (from M3) | dbt output | Delta | ~1.4M rows | Convert to constrained Delta |
| `corrections.csv` | Fixture of re-scored trips | CSV | 5 rows | MERGE idempotency drill |
| `erasure_request.json` | PDPL erasure fixture | JSON | 1 rider | Compliant-delete drill |

### Demo Requirements
- **Instructor demo:** upsert corrections twice showing 0 second-run updates, then `DESCRIBE HISTORY` and a `VERSION AS OF` diff — the "atomic, idempotent, auditable, reproducible" story in one 8-minute live flow. Rehearse opening `_delta_log`.

---

# Module 5 — Streaming Data and Event-Driven Architectures

## Module Overview

**Purpose.** Not all data arrives in nightly batches. Masar's GPS pings, trip-state events, and surge signals are continuous streams that power real-time decisions — ETAs, driver dispatch, live ops dashboards. This module teaches event-driven ingestion: **Kafka** as the event backbone and **Spark Structured Streaming** writing continuously into the Delta Lakehouse, with the correctness concerns unique to streaming — event time, late data, delivery semantics, and checkpointing.

**Business relevance.** Real-time capability separates a reactive platform from a proactive one. A Saudi mobility operator that ingests GPS and trip events in seconds can rebalance drivers before a demand spike and show riders accurate ETAs; one that batches overnight cannot. The same streaming substrate underlies fraud alerting, live network monitoring, and any AI that must act on fresh signals.

**Industry use cases.**
- A ride-hailing platform streams GPS to compute live zone demand and surge, feeding a dispatch model.
- A bank streams card authorisations into a fraud-scoring pipeline with sub-second latency.
- A telecom streams network telemetry to detect outages as they form, not in the morning report.

**Expected competencies.** After this module a participant can explain Kafka's topic/partition/offset model and delivery semantics; distinguish event time from processing time and handle late data with watermarks; and build an exactly-once Structured Streaming job that ingests events into Delta bronze with checkpointing.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Contrast batch and streaming processing and choose between them per workload | LO5 |
| 5.2 | Explain Kafka topics, partitions, offsets, consumer groups, and delivery semantics | LO5 |
| 5.3 | Distinguish event time from processing time and handle late data with watermarks | LO5 |
| 5.4 | Build a Structured Streaming job ingesting events into Delta with checkpointing | LO5, LO4, LO7 |
| 5.5 | Reason about exactly-once guarantees end to end (source → processing → sink) | LO5 |

## Technical Content

### 1. Batch vs streaming — and when each fits

**Batch** processing operates on a bounded dataset at a scheduled time (Masar's nightly ELT). **Streaming** processes an unbounded, continuous flow, emitting results with low latency (seconds). They are not rivals; they are tools for different latency requirements:

| | Batch | Streaming |
|---|---|---|
| Data | Bounded, at rest | Unbounded, in motion |
| Latency | Minutes–hours | Milliseconds–seconds |
| Cost/complexity | Lower | Higher (state, ordering, failures) |
| Masar fit | Historical trips, feature builds, reports | GPS, trip-state events, live demand |

A pragmatic rule: **default to batch; reach for streaming only when a decision genuinely needs fresh data.** Streaming adds real operational complexity (state, checkpoints, exactly-once), so its latency benefit must be worth it. Structured Streaming lets the *same* Spark/Delta code serve both, which is why this course teaches one engine for both paths.

### 2. Kafka: the event backbone

**Apache Kafka** is a distributed, durable, append-only **log** of events organised into **topics**. Core concepts:

- **Topic:** a named stream of events (e.g., `masar.gps.pings`, `masar.trip.events`).
- **Partition:** a topic is split into partitions for parallelism; events within a partition are strictly ordered; across partitions, not. The **partition key** (e.g., `trip_id`) decides which partition an event lands in — same key → same partition → ordered per trip.
- **Offset:** each event's position in its partition; consumers track offsets to know what they've read.
- **Producer / consumer / consumer group:** producers append events; consumers read them; a consumer group shares partitions so members process in parallel without overlap.
- **Retention:** Kafka keeps events for a configured window (time or size), so consumers can replay — a stream you can rewind, much like Delta history.

Kafka decouples producers from consumers: the GPS emitter doesn't know or care who consumes pings; the streaming ingest, a live-demand service, and an alerting job can all read the same topic independently. This decoupling is the essence of **event-driven architecture**.

### 3. Delivery semantics — and why exactly-once is hard

Distributed messaging offers three guarantees:

- **At-most-once:** events may be lost, never duplicated (fire and forget).
- **At-least-once:** events never lost, but may be duplicated (retry after a failure that already succeeded).
- **Exactly-once:** each event effectively processed once — no loss, no duplication.

Exactly-once is the hard, desirable one. It is achieved end-to-end by combining an **at-least-once source** (Kafka replays from offsets) with an **idempotent, transactional sink**. Here is the elegant part for this course: **Structured Streaming + Delta gives exactly-once** because Spark records the exact Kafka offsets processed in each **checkpoint**, and Delta commits the output **atomically** for that batch. If the job crashes and restarts, it resumes from the checkpointed offset and the half-done Delta batch either committed fully or not at all — no duplicates, no loss. Idempotency and ACID (M3, M4) pay off again.

### 4. Event time, processing time, and watermarks

Two clocks matter in streaming:
- **Event time:** when the event actually happened (the GPS ping's timestamp).
- **Processing time:** when the system received it.

They differ because of network delay, device buffering, and retries — a phone in a tunnel may deliver pings minutes late. Aggregations that care about *when things happened* (e.g., "trips per zone per 5-minute window") must use **event time**, or a batch of late pings will be misattributed to the wrong window.

**Watermarks** manage late data: a watermark declares "I will wait up to N minutes for late events; beyond that, I finalise the window and drop stragglers." It bounds the state Spark must keep (you can't hold every window open forever) while tolerating realistic lateness. Choosing the watermark is a trade-off: longer tolerates more lateness but holds more state and delays results; shorter is cheaper but drops more late data. For Masar GPS a few minutes is typical.

### 5. Structured Streaming mechanics

Spark **Structured Streaming** treats a stream as an unbounded table that grows; you write (almost) the same DataFrame code as for batch, and Spark runs it incrementally as micro-batches (or continuously). Essentials:

- **readStream / writeStream:** the streaming analogues of read/write.
- **Trigger:** how often to process (`processingTime='30 seconds'`, `availableNow` for backfill-then-stop).
- **Checkpoint location:** where Spark durably stores offsets + state — **mandatory** and the key to exactly-once and restartability. Never share one checkpoint between two queries.
- **Output mode:** `append` (new rows), `update`, or `complete` (full aggregate) — chosen by the query shape.

For ingestion into bronze the pattern is simple and robust: `readStream` from Kafka → light parse → `writeStream` to Delta in `append` mode with a checkpoint. Aggregations (windowed demand) add watermarks and event-time windows.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Idempotent + transactional sink = exactly-once:* don't chase exactly-once in the source alone.
- *Event time for correctness:* aggregate on when it happened, not when it arrived.
- *Checkpoints are sacred:* one per query, durable, backed up; losing it means reprocessing or duplication.
- *Stream into bronze, refine in batch:* land raw events cheaply; heavy transforms can stay batch (Lambda/Kappa trade-offs).

**Common mistakes (each appears in the Lab 5 starter deliberately)**
1. No checkpoint (or a shared one) → duplicates or state corruption on restart.
2. Aggregating on processing time → late pings land in the wrong window and demand looks wrong.
3. No watermark on an event-time aggregation → unbounded state growth, eventual OOM.
4. Partitioning the Kafka topic without a key → per-trip ordering lost.
5. Tiny trigger interval writing thousands of micro-files → the small-files problem (needs OPTIMIZE from M4).
6. Treating at-least-once as exactly-once → duplicate GPS rows skew demand counts.

**Production considerations**
- Size Kafka partitions for target parallelism and key by the entity that needs ordering (`trip_id`).
- Schedule OPTIMIZE on the streaming Delta sink (M4) to counter micro-files.
- Monitor consumer **lag** (how far behind real time) as the headline streaming health metric.
- Plan replay: because Kafka retains and Delta is idempotent, you can reprocess a bad window by resetting offsets.

## Code Examples

### A Kafka producer for Masar GPS pings

```python
# src/masar/stream/gps_producer.py
"""Emit Masar GPS pings to Kafka, keyed by trip_id so each trip's pings
stay ordered within one partition.
"""
import json, time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    key_serializer=lambda k: k.encode("utf-8"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    acks="all",          # durability: wait for replicas
)

def emit(ping: dict) -> None:
    # key = trip_id => same partition => ordered pings per trip
    producer.send("masar.gps.pings", key=ping["trip_id"], value=ping)

if __name__ == "__main__":
    # replay a sample file at ~real-time to feed the streaming lab
    with open("data/raw/gps/sample.ndjson") as f:
        for line in f:
            emit(json.loads(line))
            time.sleep(0.01)
    producer.flush()
```

### Structured Streaming ingest into Delta bronze (exactly-once)

```python
# src/masar/stream/ingest_gps_stream.py
"""Read GPS pings from Kafka and append to Delta bronze exactly-once.

Exactly-once = Kafka offsets recorded in the checkpoint + Delta's atomic
per-batch commit. Crash/restart resumes with no loss and no duplicates.
"""
from pyspark.sql import functions as F
from pyspark.sql.types import (StructType, StructField, StringType,
                               DoubleType, TimestampType)
from masar.spark import get_spark

PING_SCHEMA = StructType([
    StructField("trip_id", StringType()),
    StructField("device_id", StringType()),
    StructField("lat", DoubleType()),
    StructField("lon", DoubleType()),
    StructField("speed_kmh", DoubleType()),
    StructField("event_ts", TimestampType()),   # EVENT time, from the device
])

def run() -> None:
    spark = get_spark("masar-gps-ingest")
    raw = (spark.readStream
           .format("kafka")
           .option("kafka.bootstrap.servers", "localhost:9092")
           .option("subscribe", "masar.gps.pings")
           .option("startingOffsets", "latest")
           .load())

    parsed = (raw
        .select(F.from_json(F.col("value").cast("string"), PING_SCHEMA).alias("p"),
                F.col("timestamp").alias("_processing_ts"))   # keep both clocks
        .select("p.*", "_processing_ts")
        .withColumn("_ingested_at", F.current_timestamp()))

    (parsed.writeStream
        .format("delta")
        .outputMode("append")
        # ONE dedicated checkpoint per query — the exactly-once anchor
        .option("checkpointLocation", "./lakehouse/_checkpoints/gps_bronze")
        .trigger(processingTime="30 seconds")     # micro-batch every 30s
        .start("./lakehouse/bronze/gps_pings")
        .awaitTermination())
```

### Event-time windowed demand with a watermark

```python
# src/masar/stream/zone_demand.py
"""Live zone demand: trips STARTED per 5-min event-time window per city.

Watermark tolerates 3 minutes of late GPS/trip events, then finalises
the window and bounds state growth.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

def run() -> None:
    spark = get_spark("masar-zone-demand")
    events = (spark.readStream.format("delta")
              .load("./lakehouse/bronze/trip_events"))

    demand = (events
        .withWatermark("event_ts", "3 minutes")     # late-data tolerance
        .groupBy(
            F.window("event_ts", "5 minutes"),        # EVENT-time window
            F.col("city"))
        .agg(F.count("*").alias("trips_started")))

    (demand.writeStream
        .format("delta")
        .outputMode("append")
        .option("checkpointLocation", "./lakehouse/_checkpoints/zone_demand")
        .start("./lakehouse/gold/zone_demand_5m")
        .awaitTermination())
```

## Hands-on Lab 5 — Stream GPS Pings into the Lakehouse

| | |
|---|---|
| **Objective** | Run a single-broker Kafka, produce Masar GPS pings, and ingest them exactly-once into Delta bronze with Structured Streaming + checkpointing; then prove restart-safety (no duplicates) |
| **Duration** | 60 minutes |
| **Setup** | `docker compose up kafka` (single broker); `pip install kafka-python`; Spark with Kafka connector; `git checkout lab5-start` |

**Instructions & tasks**

1. *(10 min)* Start Kafka via compose; create topic `masar.gps.pings` (3 partitions). Run `gps_producer.py` to emit the sample stream; confirm messages with a console consumer.
2. *(15 min)* Implement `ingest_gps_stream.py`: read from Kafka, parse with `PING_SCHEMA`, write to `bronze/gps_pings` Delta in append with a **dedicated checkpoint**. Start it; watch bronze row count grow every 30s.
3. *(10 min)* **Restart-safety drill:** kill the streaming job mid-batch (Ctrl-C), note the current bronze count, restart it. Confirm counts continue with **no duplicates** (checkpoint resumed from committed offsets).
4. *(10 min)* Add `zone_demand.py`: event-time 5-min windows with a 3-min watermark. Inject a deliberately late event; observe it counted in the correct window (within tolerance) and dropped when beyond it.
5. *(5 min)* Run `OPTIMIZE` on `bronze/gps_pings` (M4 callback); record `numFiles` before/after to show the streaming small-files effect.
6. *(5 min)* Record consumer lag and throughput in `LAB5_NOTES.md`. Commit: `feat(stream): exactly-once GPS ingest + windowed demand`.
7. *(5 min)* Answer in notes: where exactly is exactly-once guaranteed, and by which two mechanisms?

**Expected output**
```
$ python -m masar.stream.ingest_gps_stream
Batch 0: appended 4,120 pings  (bronze total 4,120)
Batch 1: appended 3,980 pings  (bronze total 8,100)
^C   # killed mid-run
$ python -m masar.stream.ingest_gps_stream   # restart
Resumed from checkpoint offset; Batch 2 appended 3,900 (total 12,000) # no dupes
```

**Acceptance criteria**
- Streaming job ingests Kafka → Delta bronze with a dedicated checkpoint.
- Restart resumes with no duplicate rows (exactly-once demonstrated).
- Windowed demand uses event time + watermark; late-event behaviour observed.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Duplicates after restart | No/shared checkpoint | One dedicated `checkpointLocation` per query |
| `Failed to construct kafka consumer` | Connector jar missing | Add `spark-sql-kafka` package to session |
| Late events dropped unexpectedly | Watermark too short | Widen `withWatermark`; discuss state trade-off |
| Demand attributed to wrong window | Aggregating on processing time | Aggregate on `event_ts` |
| Thousands of tiny files | Small trigger interval | Larger trigger + scheduled OPTIMIZE |

**Instructor notes.** The restart drill (task 3) is the module's proof — make every pair kill and restart the job and *count*. It is the moment exactly-once stops being a slogan. Fast finishers: add a second consumer group reading the same topic for a live console dashboard, demonstrating producer/consumer decoupling.

## Mini Exercises

**Quiz (5 questions)**
1. What guarantees ordering within a Kafka topic? → per-partition order (with a stable partition key).
2. Which two mechanisms give Structured Streaming + Delta exactly-once? → checkpointed Kafka offsets + Delta atomic per-batch commit.
3. Why aggregate on event time, not processing time? → so late events count in the window they actually belong to.
4. What does a watermark bound? → how long late data is awaited / state kept before finalising a window.
5. True/False: two queries can safely share one checkpoint location. → **False**.

**Debugging exercise.** Give a job with no checkpoint; on restart it reprocesses and duplicates. Add a dedicated checkpoint; show restart continuity.

**Design exercise.** Masar wants live surge pricing per zone updated every minute. Specify: topic + key, trigger, window, watermark, and where exactly-once is enforced.

**Discussion questions.**
- When is streaming *not* worth it for Masar, and batch is the right call?
- Consumer lag is climbing during rush hour. What are your first three diagnostic steps?

## Case Study — Live Dispatch at "Sareea" Ride-Hailing

**Scenario.** "Sareea" (سريع) wants to rebalance idle drivers toward forming demand. Their current pipeline batches GPS overnight, so dispatch reacts a day late.

**Business context.** Faster rebalancing raises trip acceptance and cuts rider wait times — directly tied to revenue and rider retention.

**Technical challenge.** Move from nightly batch to a streaming pipeline computing zone demand within a minute, without losing or double-counting events (double-counting inflates surge and angers riders).

**Constraints.** Devices in tunnels/basements deliver pings minutes late; the platform must be restart-safe during deploys; costs must stay bounded (no unbounded state).

**Solution approach (facilitate, don't lecture).** Kafka topic keyed by `trip_id`; Structured Streaming into Delta bronze exactly-once; event-time 1-min windows with a short watermark for late pings; scheduled OPTIMIZE on the sink; monitor consumer lag. Keep the heavy historical feature build in batch (Kappa-lite: stream to bronze, refine downstream).

**Discussion questions.**
1. Why would at-least-once (duplicates) directly harm the business here?
2. How do you pick the watermark given tunnel-delayed pings vs cost of state?
3. What single metric tells you the stream is keeping up? (consumer lag)
4. What stays batch, and why not stream everything?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Exactly-once on restart | Correctness | 0 duplicate pings after kill/restart | before/after row count + key dedup |
| End-to-end latency | Performance | ping → bronze ≤ 60 s at 30s trigger | timestamp delta |
| Late-data handling | Correctness | late event within watermark counted correctly | injected-event test |
| Consumer lag | Observability | steady, not growing, under load | Kafka lag metric |
| Streaming file hygiene | Performance | OPTIMIZE reduces sink `numFiles` | `DESCRIBE DETAIL` |

**Example benchmark table (filled during lab):**

| Scenario | Pings in | Rows in bronze | Duplicates | Notes |
|---|---|---|---|---|
| clean run | 50,000 | 50,000 | 0 | baseline |
| kill mid-batch + restart | 50,000 | 50,000 | 0 | checkpoint resumed |
| no-checkpoint (sim) | 50,000 | 57,300 | 7,300 | at-least-once, dupes |

## Required Visuals and Training Assets

### Diagrams
1. **Kafka topic/partition/offset** — *Purpose:* the event-log mental model. *Elements:* a topic split into partitions, ordered offsets, a producer keying by `trip_id`, two consumer groups reading independently. *Style:* log-and-arrows, English + Arabic subtitles.
2. **Exactly-once = at-least-once source + idempotent sink** — *Purpose:* the module's key idea. *Elements:* Kafka replay + checkpointed offsets + Delta atomic commit combining into one "exactly-once" seal. *Style:* equation-style diagram.
3. **Event time vs processing time + watermark** — *Purpose:* late-data correctness. *Elements:* a timeline with events arriving out of order, a watermark line finalising a window, one straggler dropped. *Style:* dual-timeline.
4. **Kappa-lite for Masar** — *Purpose:* stream-to-bronze, refine-in-batch. *Elements:* Kafka → streaming bronze → batch silver/gold, with the boundary marked. *Style:* pipeline with a batch/stream divider.

### Images (screenshots)
1. **Streaming query progress** — the Spark micro-batch log with input rows/batch and processing rate; *why:* observability of a live stream.
2. **Kafka consumer lag** — a lag chart; *why:* the headline health metric.
3. **Restart continuity** — two terminal runs showing counts continuing without duplicates; *why:* proof of exactly-once.

### Simulations
1. **No-checkpoint duplication** — *Setup:* branch `sim-nocheckpoint` omits the checkpoint. *Expected behaviour:* restart duplicates rows. *Learning objective:* checkpoints are the exactly-once anchor.
2. **Processing-time misattribution** — *Setup:* branch aggregates on `_processing_ts`. *Expected behaviour:* a burst of late pings inflates the wrong window. *Learning objective:* event time is correctness.

### Interactive Activities
- **Human Kafka (15 min):** participants role-play producer/partitions/consumer-group, passing keyed cards; visualises ordering and parallel consumption.
- **Watermark tuning clinic (15 min):** teams pick a watermark for tunnel-delayed pings and defend the state-vs-lateness trade-off.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `gps/sample.ndjson` | Masar GPS emitter (replayable) | NDJSON | ~1.2M pings | Kafka producer source |
| `trip_events/*.json` | Trip-state change events | NDJSON | ~150k events | Windowed demand |
| `late_pings.ndjson` | Deliberately delayed events | NDJSON | ~500 pings | Watermark drill |

### Demo Requirements
- **Instructor demo:** start the stream, show bronze growing, kill it mid-batch, restart, and show counts continue with zero duplicates — the restart-safety proof in a 6-minute live run. Pre-start Kafka to avoid boot delay.

---

# Module 6 — Data Quality, Observability, and Governance

## Module Overview

**Purpose.** A pipeline that runs is not the same as a pipeline you can trust. This module makes trust explicit: **data quality** (automated expectations that catch bad data before it reaches AI/BI), **observability** (freshness, volume, and schema monitoring so you *know* when something breaks), and **governance** (catalogs, lineage, access control, PII classification, and Saudi PDPL obligations). Masar's `silver.trips` gets a quality gate; the platform gets a governance posture.

**Business relevance.** For Saudi organisations, governance is not optional polish — the **Personal Data Protection Law (PDPL)** imposes concrete obligations on rider identifiers, precise GPS, and payment data: lawful basis, minimisation, retention limits, and data-subject rights (access, erasure). Meanwhile, an unmonitored pipeline that silently ingests corrupt data trains a bad model and misinforms executives. Quality + observability + governance is what lets a platform feed AI *and* pass an audit.

**Industry use cases.**
- A bank quarantines out-of-range transactions before they corrupt a fraud model's features, and proves lineage to a regulator.
- A mobility operator classifies GPS and rider IDs as personal data, enforces column-level access, and honours PDPL erasure requests with an auditable trail.
- A government analytics unit monitors source freshness so a stalled feed raises an alert instead of silently producing yesterday's report.

**Expected competencies.** After this module a participant can design a data-quality suite (Great Expectations) with fail-and-quarantine semantics; instrument freshness/volume/schema observability; and apply governance controls — catalog, lineage, PII classification, access control, and PDPL-aligned retention.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Design a data-quality suite and choose fail-fast vs quarantine per check | LO6 |
| 6.2 | Implement freshness, volume, schema, and distribution monitoring | LO6 |
| 6.3 | Establish lineage and a catalog so any value traces to its source | LO6 |
| 6.4 | Classify PII and apply access controls and PDPL-aligned retention | LO6 |
| 6.5 | Integrate a quality gate into the medallion promotion (bronze→silver) | LO6, LO7 |

## Technical Content

### 1. The data-quality testing pyramid

Just as code has a test pyramid, data has one. From cheap/frequent to expensive/rare:

| Level | Checks | Example (Masar) | When |
|---|---|---|---|
| **Schema** | columns, types, nullability | `trip_id` present, `fare_sar` numeric | every load |
| **Constraint / range** | value bounds, sets, uniqueness | `fare_sar > 0`, `city` in KSA set, unique `trip_id` | every load |
| **Referential** | keys resolve to dimensions | every `driver_id` exists in drivers | every load |
| **Distribution** | statistical shape vs baseline | mean fare within ±20% of last week | daily |
| **Reconciliation** | totals match a source of truth | daily trip count matches ops system | daily |

The principle: **cheap checks run on every batch at the boundary; expensive statistical checks run on a schedule.** Quality is enforced where data is promoted (bronze → silver), so bad data never reaches consumers.

### 2. Great Expectations: quality as code

**Great Expectations (GX)** expresses data quality as declarative **expectations** grouped into a **suite**, validated against a batch, producing a pass/fail **validation result** and human-readable **data docs**. Key ideas:

- An *expectation* is a testable assertion: `expect_column_values_to_be_between("fare_sar", min_value=0, strict_min=True)`.
- A *suite* is a versioned collection of expectations for a dataset — the data contract, in code, reviewable like any PR.
- *Validation* runs the suite against a batch and yields per-expectation results with observed values.
- *Data docs* render results as a shareable report — the evidence auditors and stakeholders read.

Because the suite is code, it lives in version control beside the pipeline, evolves via review, and never drifts from the data it guards.

### 3. Fail-fast vs quarantine

When a batch fails expectations, two responses exist, chosen per severity:

- **Fail-fast (block):** stop the pipeline; do not promote. Correct for integrity-critical failures — a null `trip_id`, a wrong schema — where promoting anything is worse than promoting nothing.
- **Quarantine (isolate):** route the failing rows to a `quarantine/` zone, promote the good rows, and alert. Correct for partial, recoverable issues — a small fraction of trips with a bad `dropoff_geohash` — where blocking the whole batch would needlessly starve consumers.

The teaching point: **quality gates are decisions, not just alarms.** A mature gate quarantines bad rows, promotes good ones, records both, and raises a proportionate alert — rather than either silently dropping data or halting the whole platform for a handful of bad rows.

### 4. Observability: freshness, volume, schema, drift

Quality checks the *content*; observability checks the *pipeline's health* over time:

- **Freshness:** when did this table last update? A stale `silver.trips` means an upstream break — alert if `max(_ingested_at)` is older than the SLA (M3's freshness, escalated to monitoring).
- **Volume:** how many rows arrived vs expected? A sudden drop (feed outage) or spike (duplication) is an anomaly even if every row is individually valid.
- **Schema drift:** did a source add/rename/retype a column? Detect and alert before enforcement rejects a whole batch.
- **Distribution drift:** did the statistical shape shift (mean fare, null rates, category mix)? Drift often signals an upstream change that no hard rule catches — and it is the leading indicator of model degradation downstream.

These four are the "data SRE" signals; together they turn "the model got worse and we don't know why" into "the `fare_sar` distribution shifted on 12 June when the source changed currency handling."

### 5. Governance: catalog, lineage, access, PDPL

Governance answers *who can use what data, where it came from, and under what rules*:

- **Catalog:** a searchable registry of tables, owners, descriptions, and classifications (Unity Catalog, Glue, or dbt's catalog). Nobody should have to ask "does this table exist and can I trust it?"
- **Lineage:** the end-to-end map from source → bronze → silver → gold → dashboard/feature. Essential for impact analysis ("if I change `stg_trips`, what breaks?") and audit ("where did this KPI come from?"). dbt docs (M3) and Delta history (M4) supply much of this.
- **Access control:** least-privilege at table and ideally column level — analysts see gold, data scientists see silver, and raw PII (rider IDs, precise GPS) is restricted or masked.
- **PII classification & PDPL:** classify columns (rider_id, device_id, lat/lon are personal data). Saudi **PDPL** obligations to design for: lawful basis and purpose limitation, **data minimisation** (don't keep precise GPS if a geohash suffices), **retention limits** (delete when the purpose ends — tie to VACUUM), **data-subject rights** (access and erasure — the M4 MERGE-delete), and controls on **cross-border transfer**. Governance is where PDPL stops being a legal abstraction and becomes table policies, masking, and retention jobs.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Gate at promotion:* enforce quality where bronze becomes silver; never let unchecked data reach consumers.
- *Proportionate response:* fail-fast on integrity, quarantine on partial, always alert.
- *Observe trends, not just rows:* volume/freshness/drift catch what row-level rules miss.
- *Governance is data-in, not paperwork:* classification and access are table properties, enforced automatically.
- *Minimise by default:* the safest personal data is the data you never collected or already deleted.

**Common mistakes (each appears in the Lab 6 starter deliberately)**
1. Alerting without acting — a failing check emails someone but still promotes the bad data.
2. Blocking the whole batch for a few bad rows when quarantine was appropriate (or vice versa).
3. Row-level checks only, no volume/freshness monitoring — a silent feed outage goes unnoticed.
4. Storing raw rider IDs and precise GPS in gold "just in case" — a PDPL minimisation violation.
5. No lineage — a source change breaks a dashboard and nobody can trace why.
6. Retention "forever" — keeping personal data past its purpose, undeletable because history was never designed to be pruned.

**Production considerations**
- Version quality suites and review changes; loosening an expectation is a decision with an owner.
- Wire validation results and observability signals into the same alerting as application monitoring.
- Automate retention: a scheduled job that MERGE-deletes expired personal data and VACUUMs, with an audit record.
- Keep a data catalog current automatically from the pipeline metadata, not by hand.

## Code Examples

### A Great Expectations suite for `silver.trips`

```python
# quality/suites/silver_trips_suite.py
"""Data contract for silver.trips as executable expectations.

Lives in version control; changes go through review like any code.
"""
import great_expectations as gx

def build_suite(context) -> None:
    suite = context.add_or_update_expectation_suite("silver_trips.warning")

    validator = context.get_validator(
        batch_request=context.get_datasource("masar_lakehouse")
            .get_asset("silver_trips").build_batch_request(),
        expectation_suite=suite,
    )

    # Schema / integrity — fail-fast candidates
    validator.expect_column_values_to_not_be_null("trip_id")
    validator.expect_column_values_to_be_unique("trip_id")
    validator.expect_column_values_to_be_of_type("fare_sar", "DoubleType")

    # Range / set — mixed fail/quarantine
    validator.expect_column_values_to_be_between(
        "fare_sar", min_value=0, strict_min=True)
    validator.expect_column_values_to_be_in_set(
        "city", ["Riyadh", "Jeddah", "Dammam", "Mecca", "Medina"])
    validator.expect_column_values_to_be_between(
        "duration_min", min_value=0, max_value=600)   # 10h max sanity

    # Distribution — scheduled drift guard
    validator.expect_column_mean_to_be_between(
        "fare_sar", min_value=15, max_value=120)

    validator.save_expectation_suite(discard_failed_expectations=False)
```

### Quality gate at promotion: fail-fast + quarantine

```python
# src/masar/quality/gate.py
"""Run the GX suite at bronze->silver promotion.

Integrity failures => FAIL FAST (block). Partial value failures =>
QUARANTINE bad rows, promote the good ones, always alert.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

QUARANTINE = "./lakehouse/quarantine/trips"

def gate_and_promote(candidate_df, gx_result) -> None:
    spark = get_spark()

    # 1) Integrity failures (null/duplicate key) => block entire batch
    integrity_ok = gx_result.results_for(["trip_id_not_null",
                                          "trip_id_unique"]).all_passed()
    if not integrity_ok:
        raise RuntimeError("FAIL-FAST: integrity expectations failed; "
                           "batch blocked, nothing promoted")

    # 2) Partial value failures => quarantine bad rows, promote good rows
    bad = candidate_df.filter(
        (F.col("fare_sar") <= 0) |
        (~F.col("city").isin("Riyadh", "Jeddah", "Dammam", "Mecca", "Medina")))
    good = candidate_df.subtract(bad)

    if bad.count() > 0:
        (bad.withColumn("_quarantined_at", F.current_timestamp())
            .write.format("delta").mode("append").save(QUARANTINE))
        alert(f"quarantined {bad.count()} rows to {QUARANTINE}")

    (good.write.format("delta").mode("append")
        .save("./lakehouse/silver/trips"))

def alert(msg: str) -> None:
    print(f"[DATA-ALERT] {msg}")   # wire to Slack/email in production
```

### Observability: freshness, volume, and drift checks

```python
# src/masar/quality/observe.py
"""Pipeline-health signals independent of row-level content."""
from datetime import datetime, timedelta
from pyspark.sql import functions as F
from masar.spark import get_spark

def check_freshness(path: str, sla_hours: int = 6) -> None:
    spark = get_spark()
    last = (spark.read.format("delta").load(path)
            .agg(F.max("_ingested_at").alias("m")).collect()[0]["m"])
    if last is None or last < datetime.now() - timedelta(hours=sla_hours):
        raise RuntimeError(f"FRESHNESS breach: {path} last updated {last}")

def check_volume(path: str, expected: int, tol: float = 0.3) -> None:
    spark = get_spark()
    n = spark.read.format("delta").load(path).count()
    if abs(n - expected) / expected > tol:
        alert = f"VOLUME anomaly: {n} vs expected ~{expected}"
        raise RuntimeError(alert)

def check_fare_drift(path: str, baseline_mean: float, tol: float = 0.2) -> None:
    spark = get_spark()
    m = (spark.read.format("delta").load(path)
         .agg(F.mean("fare_sar").alias("m")).collect()[0]["m"])
    if abs(m - baseline_mean) / baseline_mean > tol:
        print(f"[DRIFT] fare mean {m:.1f} vs baseline {baseline_mean:.1f}")
```

### PII classification + PDPL retention job

```python
# src/masar/governance/retention.py
"""PDPL-aligned retention: delete personal data past its purpose window.

Runs on a schedule; every deletion is an auditable Delta commit.
"""
from delta.tables import DeltaTable
from masar.spark import get_spark

# Column classification drives access + retention policy
PII_COLUMNS = {"rider_id": "personal", "device_id": "personal",
               "lat": "sensitive-location", "lon": "sensitive-location"}
RETENTION_DAYS = 180   # purpose-bound: raw precise GPS not kept beyond 180d

def enforce_gps_retention() -> None:
    spark = get_spark()
    t = DeltaTable.forPath(spark, "./lakehouse/bronze/gps_pings")
    t.delete(f"event_ts < current_date() - INTERVAL {RETENTION_DAYS} DAYS")
    # follow with VACUUM (M4) to physically purge and satisfy minimisation
    spark.sql("VACUUM delta.`./lakehouse/bronze/gps_pings` RETAIN 168 HOURS")
```

## Hands-on Lab 6 — Quality Gate and Governance on `silver.trips`

| | |
|---|---|
| **Objective** | Build a Great Expectations suite for `silver.trips`, wire a fail-fast + quarantine gate at promotion, add freshness/volume/drift observability, and classify PII with a PDPL retention job |
| **Duration** | 50 minutes |
| **Setup** | `pip install great-expectations`; `git checkout lab6-start`; `silver.trips` Delta from Lab 4; a "dirty batch" fixture provided |

**Instructions & tasks**

1. *(10 min)* Build the GX suite (`silver_trips_suite.py`): schema, unique/not-null key, `fare_sar > 0`, `city` in KSA set, `duration_min` bounds, mean-fare range. Run it against a clean batch; generate data docs.
2. *(15 min)* Wire `gate_and_promote`: run the suite on the provided **dirty batch** (contains 40 null-key rows and 120 negative fares). Confirm integrity failure **fail-fasts** if keys are null; then, on a batch with only bad fares, confirm those rows **quarantine** while good rows promote.
3. *(10 min)* Add `check_freshness`, `check_volume`, `check_fare_drift`. Simulate a stale table and a volume drop; confirm each raises. Compute a baseline fare mean and detect an injected drift.
4. *(10 min)* Classify PII columns; document access policy (analyst=gold only, DS=silver, raw GPS restricted). Run `enforce_gps_retention` on a copy; confirm old GPS deleted + VACUUM.
5. *(5 min)* Open the GX data docs report; save it as the lab's quality evidence. Record quarantine counts in `LAB6_NOTES.md`.
6. Commit: `feat(quality): GX gate + observability + PDPL retention`.

**Expected output**
```
$ python -m masar.quality.gate --batch dirty_batch_keys_null.parquet
RuntimeError: FAIL-FAST: integrity expectations failed; batch blocked
$ python -m masar.quality.gate --batch dirty_batch_bad_fares.parquet
[DATA-ALERT] quarantined 120 rows to lakehouse/quarantine/trips
promoted 47,ISO good rows to silver.trips
$ python -m masar.quality.observe --check drift
[DRIFT] fare mean 78.4 vs baseline 61.0   # injected shift detected
```

**Acceptance criteria**
- GX suite runs and produces data docs.
- Gate fail-fasts on integrity failures and quarantines partial value failures.
- Freshness/volume/drift checks each fire on their injected fault.
- PII classified; retention job deletes + VACUUMs old personal data.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Gate promotes bad rows | Alert-only, no branch/action | Split good/bad; write quarantine; raise on integrity |
| Whole batch blocked for a few bad fares | Fail-fast applied too broadly | Reserve fail-fast for integrity; quarantine the rest |
| Drift never fires | Baseline recomputed from dirty data | Freeze baseline from a known-good period |
| GX datasource errors | Delta asset not registered | Configure the Spark/Delta datasource in GX context |

**Instructor notes.** The pedagogical crux is task 2: participants must *choose* fail-fast vs quarantine and justify it. Push back on any team that fail-fasts on a few bad fares or quarantines a null key. Fast finishers: add a `relationships`-style check that every `driver_id` exists and decide its response class.

## Mini Exercises

**Quiz (5 questions)**
1. Where in the medallion should the quality gate run? → at promotion (bronze → silver).
2. Give one failure that warrants fail-fast and one that warrants quarantine. → null/duplicate key (fail-fast); a few out-of-range fares (quarantine).
3. Name two observability signals that row-level checks miss. → freshness and volume (also distribution drift).
4. Which PDPL principle argues against keeping precise GPS forever? → data minimisation (and retention limits).
5. True/False: alerting on bad data is sufficient governance. → **False** — the gate must also act (block/quarantine).

**Debugging exercise.** Give a gate that emails on failure but still promotes. Refactor to act (block integrity, quarantine partial) and prove bad rows no longer reach silver.

**Governance exercise.** Classify all `silver.trips` columns as public / personal / sensitive; propose access levels and a retention window for each class with a one-line PDPL justification.

**Discussion questions.**
- Your model degraded but every row passes validation. Which observability signal do you check first, and why? (distribution drift)
- A stakeholder wants raw rider IDs in a shared dashboard "for convenience." How do you say no in PDPL terms and still meet their need? (masking / pseudonymisation / gold-only aggregates)

## Case Study — The Silent Currency Bug at "Muqeem" Analytics

**Scenario.** "Muqeem" (مقيم) ingests trips from a vendor that, on 12 June, silently switched a fare field from halalas to riyals (a 100× change) for one city. Every row is individually "valid"; a demand-pricing model degrades over the next two weeks.

**Business context.** The mispriced city skews surge and a revenue forecast; the error is invisible to row-level rules.

**Technical challenge.** No hard constraint catches a 100× shift that stays within a generous range; only a distribution check would.

**Constraints.** Cannot re-ingest (immutable bronze — good); must detect, quarantine, and backfill-correct without blocking the other cities.

**Solution approach (facilitate, don't lecture).** Add a per-city mean-fare drift check against a frozen baseline; on breach, quarantine the affected city's batch and alert; correct with a MERGE (M4) once the unit is normalised; add lineage so the vendor-source change is traceable; document the retention/audit trail.

**Discussion questions.**
1. Why did every schema/range check pass while the data was wrong?
2. What baseline period do you freeze, and how do you avoid "baselining the bug"?
3. Fail-fast or quarantine here, and scoped to what?
4. What lineage would have shortened detection from two weeks to one day?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Quality suite coverage | Quality | ≥ 7 expectations incl. schema/range/set/drift | GX suite |
| Gate correctness | Correctness | integrity → block; partial → quarantine | dirty-batch drills |
| Quarantine capture | Correctness | 100% of bad rows isolated, good rows promoted | row counts |
| Observability firing | Observability | freshness/volume/drift each detect fault | injected-fault tests |
| PII classified | Governance | all personal/sensitive columns labelled + policy | classification doc |
| Retention enforced | Governance | old personal data deleted + VACUUMed | retention job run |

**Example benchmark table (filled during lab):**

| Batch | Rows in | Promoted | Quarantined | Gate action |
|---|---|---|---|---|
| clean | 48,200 | 48,200 | 0 | promote |
| bad fares | 48,200 | 48,080 | 120 | quarantine |
| null keys | 48,240 | 0 | 0 | fail-fast (blocked) |

## Required Visuals and Training Assets

### Diagrams
1. **Data-quality pyramid** — *Purpose:* prioritise checks. *Elements:* schema → constraint → referential → distribution → reconciliation, cheap/frequent at the base. *Style:* pyramid, English + Arabic subtitles.
2. **Quality gate: fail-fast vs quarantine** — *Purpose:* the module's decision. *Elements:* a batch hitting the gate; integrity fail → blocked; partial fail → split to quarantine + promote good; both → alert. *Style:* decision flow.
3. **Four observability signals** — *Purpose:* pipeline health. *Elements:* freshness, volume, schema drift, distribution drift as four gauges over a timeline. *Style:* dashboard-style panel.
4. **Governance & PDPL map** — *Purpose:* governance as table policy. *Elements:* catalog + lineage + access levels + PII classification + retention/erasure, annotated with PDPL principles. *Style:* layered governance diagram.

### Images (screenshots)
1. **GX data docs report** — pass/fail expectations with observed values; *why:* the audit evidence artefact.
2. **Quarantine zone listing** — bad rows in `quarantine/trips`; *why:* the gate's action made concrete.
3. **Drift alert** — the drift check output flagging the currency shift; *why:* what row rules miss.

### Simulations
1. **Alert-but-promote** — *Setup:* branch `sim-alertonly` alerts yet still promotes bad rows. *Expected behaviour:* corrupt data reaches silver despite the "alarm". *Learning objective:* gates must act, not just notify.
2. **Baseline-the-bug** — *Setup:* drift baseline computed after the currency change. *Expected behaviour:* drift never fires. *Learning objective:* baselines must come from a known-good period.

### Interactive Activities
- **Fail-fast or quarantine? (15 min):** 12 failure cards sorted into block/quarantine/alert-only with justification.
- **PDPL clinic (15 min):** teams classify Masar columns and draft a retention + access policy, defended against a mock auditor.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `dirty_batch_keys_null.parquet` | Fixture (40 null keys) | Parquet | 48k rows | Fail-fast drill |
| `dirty_batch_bad_fares.parquet` | Fixture (120 negative fares) | Parquet | 48k rows | Quarantine drill |
| `currency_shift_city.parquet` | Fixture (100× fare on one city) | Parquet | 48k rows | Drift-detection case |

### Demo Requirements
- **Instructor demo:** run the gate on a dirty batch — fail-fast on null keys, then quarantine bad fares while promoting good rows, then open the GX data docs — the "gates decide, and they leave evidence" story in 7 minutes.

---

# Module 7 — Hands-on: Building a Mini-Lakehouse

## Module Overview

**Purpose.** This is the integration module: everything from M1–M6 becomes one coherent, orchestrated **Mini-Lakehouse**. Participants assemble the Masar medallion end-to-end — bronze landing (batch + streaming), silver ELT with Delta and quality gates, gold aggregates and features — wired into an orchestrated, idempotent, observable pipeline they can run with one command. It is the direct precursor to the capstone (which extends this build) and the shape of a real production platform in miniature.

**Business relevance.** A platform is not its individual parts but their reliable composition. The skill that distinguishes a senior data engineer is making bronze → silver → gold run **repeatably, in order, idempotently, with quality gates and observability**, recoverable after failure. For Saudi organisations moving from proofs-of-concept to production, this orchestrated, self-checking pipeline *is* the deliverable.

**Industry use cases.**
- A mobility operator runs a nightly DAG that lands the day's trips, promotes them through quality gates, and refreshes demand marts before the morning ops review.
- A bank orchestrates ingest → feature-build → validation so a failed step halts promotion and pages on-call, never shipping partial data.
- A government platform re-runs its entire medallion idempotently to recover from an outage with no duplicates and no manual cleanup.

**Expected competencies.** After this module a participant can compose a medallion Lakehouse; define layer **contracts**; orchestrate the pipeline as a dependency-ordered DAG (Airflow-style) with idempotent, retryable tasks; and build gold aggregates/features that serve AI and BI.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Compose bronze → silver → gold into one coherent Lakehouse | LO7 |
| 7.2 | Define and enforce medallion layer contracts | LO7, LO6 |
| 7.3 | Orchestrate the pipeline as a dependency-ordered, idempotent DAG | LO7 |
| 7.4 | Build gold aggregates and a feature table serving AI and BI | LO7, LO8 |
| 7.5 | Make the full pipeline recoverable and observable end to end | LO7, LO6 |

## Technical Content

### 1. The Mini-Lakehouse architecture

The Masar Mini-Lakehouse is the assembly of every prior module into one storage-and-compute system:

```
sources ──► BRONZE (raw, append-only, Delta)
   trips CSV, drivers CSV        land_bronze.py        (M1)
   GPS via Kafka                 ingest_gps_stream.py  (M5)
              │
              ▼   quality gate + ELT (M3, M4, M6)
           SILVER (conformed, constrained Delta)
              silver.trips  (incremental merge, tested, quality-gated)
              │
              ▼   aggregate + feature engineering
            GOLD (marts + feature table, Delta)
              gold.zone_hourly_demand   → BI dashboard  (M8)
              gold.driver_daily         → BI dashboard  (M8)
              gold.trip_features        → AI feature store (M8)
```

Everything the course built is a node here. The *new* work in M7 is the wiring, the contracts between layers, and the orchestration that makes it run as one reliable unit.

### 2. Layer contracts

A **contract** is the guaranteed shape and quality a layer promises its consumers, so downstream code can depend on it:

| Layer | Contract (guarantees) |
|---|---|
| **Bronze** | Append-only; carries `_ingested_at`, `_source_file`; schema as-received; never mutated |
| **Silver** | One row per `trip_id`; enforced schema + CHECK constraints; quality-gated; conformed timezone/units; completed valid trips only |
| **Gold** | Business-modelled; documented grain (e.g., "one row per zone per hour"); feature table is point-in-time correct (M8) |

Contracts are what let teams work independently: a BI developer builds on gold's documented grain without reading the ELT code, trusting the contract. Breaking a contract is a breaking change requiring versioning and communication — exactly like an API.

### 3. Orchestration: DAGs, dependencies, idempotency

The pipeline is a **DAG** (directed acyclic graph) of tasks with explicit dependencies: land bronze → run quality gate → build silver → build gold, where each task runs only after its upstreams succeed. An orchestrator (Airflow, Dagster, or Databricks Workflows) schedules the DAG, retries failed tasks, and surfaces status.

The properties that make orchestration production-grade — all already built in earlier modules — are:
- **Dependency ordering:** gold never builds from a silver that hasn't refreshed.
- **Idempotency:** every task can rerun safely (bronze append + downstream MERGE), so retries and backfills don't corrupt data.
- **Atomicity per task:** Delta commits mean a failed task leaves no half-written table.
- **Observability:** freshness/volume/quality signals (M6) gate promotion and feed alerts.
- **Recoverability:** because tasks are idempotent and Delta is transactional, a full re-run recovers from any failure with no duplicates.

The lesson: orchestration is not "a scheduler" — it is the guarantee that the medallion runs *in order, exactly, and recoverably*.

### 4. Building gold: aggregates and features

Gold serves two very different consumers, and the difference matters (developed fully in M8):

- **BI marts** — human-readable aggregates at a documented grain: `gold.zone_hourly_demand` (trips per zone per hour with avg fare, avg wait), `gold.driver_daily` (trips, earnings, rating per driver per day). Optimised for dashboard queries (partitioned, ZORDERed, compacted).
- **Feature table** — model-ready features at the entity/time grain the AI needs: `gold.trip_features` (per trip or per zone-time), engineered from silver with the *same* logic training and serving will share — the training/serving-skew defence, now at platform scale.

Both are Delta gold tables; both derive purely and idempotently from silver; both carry the contract their consumer depends on.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Compose, don't rewrite:* the Mini-Lakehouse reuses the modules' code; integration is wiring + contracts, not new logic.
- *Contracts over coupling:* consumers depend on a layer's documented contract, not its implementation.
- *Idempotent DAG:* a full rerun must be safe — this is what makes recovery trivial.
- *One command to run it all:* a `make pipeline` / single DAG trigger is the team's public interface, like M1's Makefile lesson generalised to the platform.

**Common mistakes (each appears in the Lab 7 starter deliberately)**
1. Building gold directly from bronze, bypassing silver's contract and quality gate.
2. A task with no dependency declared → gold builds from stale silver.
3. Non-idempotent gold (INSERT aggregates) → reruns double-count.
4. No orchestration — a hand-run sequence of notebooks that nobody can reliably reproduce.
5. Over-partitioned gold (by hour and city and driver) → small-files, slow dashboards.
6. Feature logic in gold that diverges from what serving uses → reintroduced skew.

**Production considerations**
- Schedule maintenance (OPTIMIZE/VACUUM from M4) as DAG tasks, not manual afterthoughts.
- Emit run metadata (rows processed, duration, quality results) per task for observability and cost attribution.
- Make backfills a parameter (date range) so history can be recomputed idempotently.
- Keep the DAG in version control and review changes; the pipeline is production infrastructure.

### 6. Real-world example walkthrough

Narrate this (5 minutes): a data team ran their "platform" as twelve notebooks executed by hand each morning in a remembered order. A new engineer ran step 7 before step 4; gold rebuilt from stale silver and the exec dashboard showed last week's demand. There was no failure, no alert — just a wrong number and a lost morning. The fix was not more notebooks; it was orchestration: one DAG with declared dependencies, idempotent tasks, and quality gates, runnable by anyone with one command and recoverable after any failure. The Mini-Lakehouse participants build here is that fix, embodied.

## Code Examples

### The pipeline as an Airflow-style DAG

```python
# orchestration/dags/masar_medallion.py
"""Masar Mini-Lakehouse DAG: bronze -> gate -> silver -> gold -> maintain.

Dependencies are explicit; every task is idempotent and retryable, so a
full re-run recovers from any failure with no duplicates.
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from masar.ingest.land_bronze import land_trips, land_drivers
from masar.quality.gate import gate_and_promote_task
from masar.transform.build_silver import build_silver_trips
from masar.transform.build_gold import (build_zone_hourly_demand,
                                        build_driver_daily, build_trip_features)
from masar.delta.maintain import optimize_and_vacuum

default_args = {"retries": 2, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="masar_medallion",
    schedule="0 2 * * *",          # nightly at 02:00 Asia/Riyadh
    start_date=datetime(2026, 6, 1),
    catchup=False,                 # backfills are explicit, parameterised
    default_args=default_args,
    tags=["masar", "lakehouse"],
) as dag:

    t_land = PythonOperator(task_id="land_bronze",
                            python_callable=lambda **_: (land_trips(), land_drivers()))
    t_gate = PythonOperator(task_id="quality_gate",
                            python_callable=gate_and_promote_task)
    t_silver = PythonOperator(task_id="build_silver",
                              python_callable=build_silver_trips)
    t_demand = PythonOperator(task_id="gold_zone_demand",
                              python_callable=build_zone_hourly_demand)
    t_driver = PythonOperator(task_id="gold_driver_daily",
                              python_callable=build_driver_daily)
    t_feats = PythonOperator(task_id="gold_trip_features",
                             python_callable=build_trip_features)
    t_maint = PythonOperator(task_id="optimize_vacuum",
                             python_callable=optimize_and_vacuum)

    # dependency ordering: gold never builds from unrefreshed silver
    t_land >> t_gate >> t_silver >> [t_demand, t_driver, t_feats] >> t_maint
```

### Idempotent gold aggregate (documented grain)

```python
# src/masar/transform/build_gold.py
"""Gold marts + feature table. Pure, idempotent transforms from silver.

Grain is DOCUMENTED and enforced by the write (overwrite of a partition
or merge on the grain key) so reruns never double-count.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

SILVER = "./lakehouse/silver/trips"
GOLD = "./lakehouse/gold"

def build_zone_hourly_demand() -> None:
    """Grain: one row per (city, date, hour). BI-facing."""
    spark = get_spark()
    silver = spark.read.format("delta").load(SILVER)
    demand = (silver
        .withColumn("date", F.to_date("started_at"))
        .withColumn("hour", F.hour("started_at"))
        .groupBy("city", "date", "hour")
        .agg(F.count("*").alias("trips"),
             F.avg("fare_sar").alias("avg_fare_sar"),
             F.avg("duration_min").alias("avg_duration_min"),
             F.avg("surge_multiplier").alias("avg_surge")))
    # overwrite by partition => idempotent rebuild, no double counting
    (demand.write.format("delta")
        .partitionBy("date")
        .mode("overwrite")
        .option("replaceWhere", "date >= current_date() - INTERVAL 3 DAYS")
        .save(f"{GOLD}/zone_hourly_demand"))
```

### Point-in-time-correct feature table (skew defence at scale)

```python
# src/masar/transform/build_gold.py  (continued)
def build_trip_features() -> None:
    """AI-facing feature table. SAME feature logic training & serving share.

    Point-in-time correct: features use only data available AT trip start,
    never future information (no label leakage).
    """
    spark = get_spark()
    silver = spark.read.format("delta").load(SILVER)

    # rolling zone demand KNOWN at trip start (prior hour), not the current one
    from pyspark.sql import Window
    w = (Window.partitionBy("city")
         .orderBy(F.col("started_at").cast("long"))
         .rangeBetween(-3600, -1))   # prior 1 hour, strictly before this trip

    features = (silver
        .withColumn("zone_demand_prev_hr", F.count("*").over(w))
        .select("trip_id", "city", "started_at",
                "start_hour", "is_night", "fare_per_km",
                "surge_multiplier", "zone_demand_prev_hr")
        .withColumn("_feature_version", F.lit("v1")))

    (features.write.format("delta").mode("overwrite")
        .save(f"{GOLD}/trip_features"))
```

## Hands-on Lab 7 — Assemble and Orchestrate the Mini-Lakehouse

| | |
|---|---|
| **Objective** | Wire bronze → gate → silver → gold into one orchestrated, idempotent DAG; build the two BI marts and the AI feature table; and prove the whole pipeline recovers from a mid-DAG failure with no duplicates |
| **Duration** | 90 minutes |
| **Setup** | `pip install apache-airflow` (or use the provided Dagster/Workflows stub); `git checkout lab7-start`; all prior labs' code available as modules |

**Instructions & tasks**

1. *(15 min)* Wire the DAG (`masar_medallion.py`): declare tasks and the `land >> gate >> silver >> [gold...] >> maintain` dependency chain. Confirm the graph renders with correct ordering.
2. *(20 min)* Implement `build_zone_hourly_demand` and `build_driver_daily` with **documented grain** and idempotent writes (`replaceWhere`/merge). Rerun each twice; confirm counts are stable (no double-count).
3. *(15 min)* Implement `build_trip_features` with a **point-in-time-correct** rolling feature (prior-hour zone demand, strictly before each trip — no leakage). Verify a spot-check trip's feature uses only prior data.
4. *(15 min)* Trigger the full DAG. Then **inject a failure** in `build_silver` (raise mid-task); confirm gold does not build (dependency held) and the DAG surfaces the failure. Fix and re-run the whole DAG; confirm end state is correct with **no duplicates** (idempotent recovery).
5. *(10 min)* Add `optimize_and_vacuum` as the final task. Record per-table row counts and grains in `MINI_LAKEHOUSE.md`.
6. *(10 min)* Run `make pipeline` (single-command trigger). Commit: `feat(pipeline): orchestrated idempotent Masar medallion`.
7. *(5 min)* In notes: identify each layer's contract and where it is enforced.

**Expected output**
```
$ make pipeline
[land_bronze]   OK  appended 48,200 trips, 1.2M pings
[quality_gate]  OK  promoted 48,080, quarantined 120
[build_silver]  OK  merged 48,080 (unique trip_id)
[gold_zone_demand] OK  1 row per city/date/hour  (720 rows)
[gold_driver_daily] OK  1 row per driver/day
[gold_trip_features] OK  point-in-time features v1
[optimize_vacuum] OK  numFiles 214 -> 11
DAG masar_medallion: success
```

**Acceptance criteria**
- DAG enforces dependency ordering (gold waits for silver).
- BI marts and feature table build idempotently at documented grains.
- Feature table is point-in-time correct (no future leakage).
- Injected failure halts promotion; full re-run recovers with no duplicates.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Gold double-counts on rerun | INSERT aggregate | Use overwrite `replaceWhere` or merge on grain |
| Gold built from stale silver | Missing dependency edge | Declare `silver >> gold` |
| Feature leakage detected | Window includes current/future rows | `rangeBetween(-3600, -1)`: strictly prior |
| DAG import error | Callable signatures mismatch | Align task callables to `**context` |
| Small-files on gold | Over-partitioned | Partition by date only; OPTIMIZE |

**Instructor notes.** Task 4 (inject failure, recover with a full re-run) is the module's thesis and the capstone rehearsal — budget time for every pair to *see* the clean recovery. Fast finishers: add a `backfill` DAG run over a 7-day range and confirm idempotent correctness across the window.

## Mini Exercises

**Quiz (5 questions)**
1. What guarantees gold never builds from unrefreshed silver? → declared DAG dependency ordering.
2. Why must every DAG task be idempotent? → so retries/backfills/full re-runs don't corrupt or duplicate data.
3. What is a "layer contract"? → the guaranteed shape/quality a layer promises consumers.
4. What makes the feature table point-in-time correct? → it uses only data available before each event (no future/label leakage).
5. True/False: the Mini-Lakehouse mostly requires new logic. → **False** — it composes the prior modules; the work is wiring + contracts.

**Debugging exercise.** Give a DAG missing the `silver >> gold` edge; gold shows stale numbers. Add the dependency and re-run; confirm freshness.

**Recovery drill.** Kill the DAG after silver but before gold; re-run the whole DAG; prove the end state is identical to an uninterrupted run (no duplicates).

**Discussion questions.**
- Which orchestrator fits Masar and why — Airflow, Dagster, or Databricks Workflows? What criteria decide?
- Where should backfills live — in the same DAG (parameterised) or a separate one? Trade-offs?

## Case Study — From Twelve Notebooks to One DAG at "Rakeez" Data

**Scenario.** "Rakeez" (ركيز) runs its analytics platform as twelve notebooks executed by hand each morning in a remembered order. A new hire runs them out of order; the exec dashboard shows stale demand with no error.

**Business context.** The morning ops review drives driver allocation; a stale dashboard misallocates drivers for the day.

**Technical challenge.** Convert an implicit, human-ordered, non-idempotent sequence into an explicit, ordered, idempotent, recoverable pipeline — without a rewrite.

**Constraints.** Same logic must be preserved (validated by reconciliation); the team is small; runs must be reproducible by anyone and recoverable after failure.

**Solution approach (facilitate, don't lecture).** Wrap each notebook's logic as an idempotent task; declare dependencies as a DAG; add the quality gate and maintenance as tasks; make every task rerun-safe (append/merge/overwrite-partition); trigger with one command; prove equivalence by reconciliation before cutover.

**Discussion questions.**
1. Why is "run these in order" a latent production incident?
2. Which property — ordering, idempotency, or observability — would have prevented the stale dashboard, and how?
3. How do you migrate incrementally without a big-bang rewrite?
4. What does "one command runs the platform" buy the team culturally, not just technically?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| End-to-end DAG success | Integration | full medallion runs green in one trigger | DAG run |
| Dependency correctness | Correctness | gold waits for silver (no stale builds) | dependency test |
| Idempotent recovery | Reliability | full re-run after failure = no duplicates | kill/re-run drill |
| Feature correctness | Correctness | 0 future-leakage in feature table | window audit |
| Gold grains documented | Governance | each mart's grain stated + enforced | MINI_LAKEHOUSE.md |
| Maintenance in pipeline | Performance | OPTIMIZE/VACUUM run as DAG tasks | run log |

**Example benchmark table (filled during lab):**

| Task | Rows out | Grain | Idempotent? | Duration |
|---|---|---|---|---|
| build_silver | 48,080 | 1 / trip_id | yes (merge) | 6 s |
| gold_zone_demand | 720 | 1 / city·date·hour | yes (replaceWhere) | 3 s |
| gold_driver_daily | 3,450 | 1 / driver·day | yes (merge) | 2 s |
| gold_trip_features | 48,080 | 1 / trip | yes (overwrite) | 5 s |

## Required Visuals and Training Assets

### Diagrams
1. **Mini-Lakehouse architecture** — *Purpose:* the whole course on one page. *Elements:* sources → bronze (batch+stream) → gate → silver → gold (2 marts + feature table) → BI + AI consumers, colour-coded by layer. *Style:* full-pipeline poster, English + Arabic subtitles. *Designer description:* "One end-to-end medallion flow with orchestrator badge and consumer icons."
2. **The DAG** — *Purpose:* orchestration and dependencies. *Elements:* task nodes with edges (`land >> gate >> silver >> [gold...] >> maintain`), retry/idempotency annotations. *Style:* graph.
3. **Layer contracts** — *Purpose:* what each layer guarantees. *Elements:* three cards (bronze/silver/gold) listing contract bullets; a consumer depending on gold's grain. *Style:* contract cards.
4. **Idempotent recovery** — *Purpose:* the recovery thesis. *Elements:* a DAG failing at silver, then a full re-run producing an identical end state. *Style:* before/after with a "no duplicates" seal.

### Images (screenshots)
1. **Airflow DAG graph view** — the rendered dependency graph, all-green; *why:* orchestration made real.
2. **`make pipeline` output** — the per-task log with row counts/grains; *why:* one-command reproducibility.
3. **Gold marts sample** — `zone_hourly_demand` rows; *why:* the BI-facing contract.

### Simulations
1. **Out-of-order run** — *Setup:* branch runs gold before silver refresh. *Expected behaviour:* stale numbers, no error. *Learning objective:* implicit ordering is a latent incident.
2. **Non-idempotent gold** — *Setup:* INSERT-based aggregate. *Expected behaviour:* rerun doubles counts. *Learning objective:* idempotency enables recovery.

### Interactive Activities
- **Build-the-DAG on the wall (20 min):** teams arrange task cards into a valid dependency graph and mark idempotency/retry on each.
- **Contract-writing (15 min):** each team writes the formal contract for one gold table and another team tries to break an assumption.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| All prior `bronze/*`, `silver/trips` | From Labs 1–6 | Delta | full Masar sample | Pipeline inputs |
| `gold/*` (built in lab) | This lab's output | Delta | 720 / 3.4k / 48k rows | Serving inputs for M8 |

### Demo Requirements
- **Instructor demo:** trigger the full DAG, inject a silver failure, show gold held back, then re-run the whole DAG to a clean identical state — the "orchestrated, idempotent, recoverable" story in 8 minutes; this is the capstone in miniature.

---

# Module 8 — Serving Data to AI and BI Workloads

## Module Overview

**Purpose.** A Lakehouse exists to be *consumed*. This final module connects the Masar gold layer to its two customers with different needs: **AI** (a feature table that is point-in-time correct and available for both training and low-latency serving, defending against training/serving skew) and **BI** (a dimensional model that analysts and dashboards query fast). Participants learn the serving patterns, the correctness traps unique to each, and the trade-offs of serving from the Lakehouse directly versus through a specialised store.

**Business relevance.** This is where the platform pays off: an ETA/demand model that trains and serves on identical features, and an ops dashboard executives trust. For Saudi organisations, getting serving right is the difference between a data platform that is a cost centre and one that visibly drives decisions — accurate ETAs, efficient driver allocation, reliable KPIs — while still honouring PDPL at the point of consumption.

**Industry use cases.**
- A mobility operator serves the *same* `trip_features` to a training job and an online ETA service, eliminating skew.
- A bank exposes a governed star schema so hundreds of analysts self-serve without touching raw data.
- A retailer serves a feature store for recommendations while a separate BI mart powers merchandising dashboards — from one Lakehouse.

**Expected competencies.** After this module a participant can design a point-in-time-correct feature table for AI and reason about offline vs online serving; model a star schema for BI; choose serving patterns (direct Lakehouse, materialised mart, external store) by workload; and apply PDPL controls at the serving boundary.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 8.1 | Design a point-in-time-correct feature table serving training and inference | LO8 |
| 8.2 | Contrast offline and online feature serving and their consistency requirements | LO8 |
| 8.3 | Model a star schema (facts/dimensions) for BI consumption | LO8 |
| 8.4 | Select serving patterns per workload (direct, materialised, external store) | LO8, LO2 |
| 8.5 | Apply governance/PDPL controls at the serving boundary | LO8, LO6 |

## Technical Content

### 1. Two consumers, two contracts

Gold serves two audiences whose needs conflict, which is why they get different tables:

| Concern | AI / feature store | BI / analytics |
|---|---|---|
| Grain | entity × time (per trip, per zone-hour) | business dimensions (per city, per day) |
| Correctness | point-in-time, no leakage | consistent definitions, conformed dimensions |
| Latency | training (batch) + inference (ms) | interactive dashboard (sub-second) |
| Schema | model-ready features, versioned | human-readable star schema |
| Freshness | as fresh as the model needs | as fresh as the decision needs |

The unifying idea from the whole course: **both consume the same governed gold, derived from the same silver, with shared feature logic** — so the analyst's "trips per zone" and the model's "zone demand feature" cannot silently disagree. One source of truth, two contracts.

### 2. Serving AI: feature tables and point-in-time correctness

The cardinal sin in ML feature engineering is **leakage** — letting a feature "see" information that would not exist at prediction time, inflating offline metrics and collapsing in production. The defence is **point-in-time correctness**: every feature value reflects only what was known at the event's timestamp. Masar's `zone_demand_prev_hr` uses the *prior* hour strictly before each trip (M7's window) — never the current or future hour.

This matters twice:
- **Training:** join labels to features **as of** each event's time (a point-in-time join), so the model learns on the information it will actually have. Delta time travel (M4) makes reproducing a training snapshot exact.
- **Serving:** the online path must compute/lookup the *same* features the same way. Skew appears when training uses one computation and serving another — the exact failure the shared feature module prevents.

### 3. Offline vs online feature serving

Two serving modes, chosen by latency need:

- **Offline (batch):** features read from the gold Delta feature table for training and for batch scoring (e.g., nightly demand forecast). High throughput, latency-insensitive; the Lakehouse serves this directly.
- **Online (real-time):** an inference service needs a feature for a single entity in milliseconds (live ETA). A columnar Lakehouse scan is too slow for a single-row point lookup, so online serving typically copies the latest features into a **low-latency store** (Redis, DynamoDB, a feature-store online layer) keyed by entity.

The critical requirement is **offline/online consistency**: the online store must hold the *same values*, computed the *same way*, as the offline table used for training. The pattern: compute features once in the Lakehouse (offline), then **materialise** the latest slice to the online store — never re-implement the feature logic separately for online (that is skew by construction).

### 4. Serving BI: the star schema

BI consumers want fast, intuitive queries over consistent business concepts. The proven model is the **star schema**:

- A central **fact table** of measurable events at a fine grain — `fact_trips` (one row per trip: fare, distance, duration, surge) with foreign keys to dimensions.
- **Dimension tables** describing the entities — `dim_driver`, `dim_city`/`dim_zone`, `dim_date`, `dim_payment_method` — with descriptive attributes analysts filter and group by.

Why star (denormalised dimensions) beats a fully normalised model for analytics: fewer joins, predictable query shapes, and columns named for humans. Masar's `gold.zone_hourly_demand` and `gold.driver_daily` are pre-aggregated marts on top of this model for the hottest dashboards. **Conformed dimensions** (one `dim_date`, one `dim_driver` shared across facts) are what make numbers reconcile across dashboards — the antidote to the M1 two-tier divergence.

### 5. Serving patterns and trade-offs

Where should a consumer read from? Three patterns, chosen by latency, concurrency, and cost:

| Pattern | How | Best for | Trade-off |
|---|---|---|---|
| **Direct Lakehouse** | Query gold Delta with a SQL engine (Spark, Trino, Databricks SQL) | Analysts, batch ML, moderate concurrency | Simple, one copy; may lag on very high concurrency |
| **Materialised mart** | Pre-aggregated/ZORDERed gold tables (M4) | Hot dashboards | Fast; must refresh (a DAG task) |
| **External serving store** | Copy latest slice to Redis/warehouse/OLAP | Millisecond online features; thousands of concurrent BI users | Fastest; a *second copy* → consistency + cost (mind the two-tier trap) |

The judgement to teach: **do not reintroduce the two-tier problem casually.** An external store is justified by a real latency/concurrency requirement, and when used it must be a *derived, consistently refreshed* copy of gold — not an independently transformed one. Prefer serving from the Lakehouse until a measured requirement forces otherwise.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *One truth, two contracts:* AI and BI consume the same governed gold, shaped differently.
- *Point-in-time or nothing:* leakage-free features are non-negotiable; enforce it structurally.
- *Consistency across offline/online:* materialise, never re-implement, online features.
- *Serve, don't fork:* external stores are derived copies, not new pipelines.
- *Govern at the boundary:* PDPL applies where humans/models read — mask, aggregate, restrict.

**Common mistakes (each appears in the Lab 8 starter deliberately)**
1. Feature leakage — using the current/future hour's demand as a feature; great offline, terrible live.
2. Re-implementing features in the online path → offline/online skew.
3. Serving raw rider IDs / precise GPS to a dashboard → PDPL violation at the boundary.
4. A non-conformed second `dim_date` → dashboards disagree (two-tier divergence returns).
5. Building an external serving copy with its own transformations → the copy diverges from gold.
6. Dashboards querying an unoptimised gold table → slow, expensive (M2/M4 callback).

**Production considerations**
- Version features (`_feature_version`) and reproduce training sets via Delta time travel.
- Refresh the online store as a DAG task with freshness monitoring (M6/M7).
- Enforce column-level access and masking at the serving layer; expose gold aggregates, not raw PII.
- Measure serving SLAs (dashboard p95 latency, online feature p99) and treat them as gates.

### 6b. Real-world example walkthrough

Narrate this (5 minutes): a team's ETA model scored 0.93 R² offline and flopped live. The culprit: a "current zone demand" feature computed from the *whole* hour containing the trip — including trips that started *after* the one being predicted. Offline it looked prophetic; online that information didn't exist yet. The fix was point-in-time correctness (prior hour only) plus serving the *same* feature table offline and online. Offline R² dropped to a realistic 0.78 — and live performance finally matched it. The lesson participants carry into the capstone: a feature that looks too good is usually leaking.

## Code Examples

### Point-in-time-correct training join (no leakage)

```python
# src/masar/serve/training_join.py
"""Build a training set by joining labels to features AS OF event time.

Each row's features reflect only what was known at started_at — the
point-in-time join that prevents leakage and matches serving.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

def build_training_set(label_col: str = "duration_min"):
    spark = get_spark()
    feats = spark.read.format("delta").load("./lakehouse/gold/trip_features")
    # label lives in silver; features already point-in-time (prior hour)
    labels = (spark.read.format("delta").load("./lakehouse/silver/trips")
              .select("trip_id", F.col(label_col).alias("label")))
    return (feats.join(labels, "trip_id", "inner")
                 .withColumn("_trained_on_feature_version",
                             F.col("_feature_version")))
```

### Materialising the online feature slice (offline/online consistency)

```python
# src/masar/serve/materialize_online.py
"""Push the LATEST feature per entity to a low-latency online store.

Values are COPIED from the offline gold table — never recomputed — so
online and offline are consistent by construction (no skew).
"""
import redis, json
from pyspark.sql import functions as F, Window
from masar.spark import get_spark

def materialize_zone_features() -> None:
    spark = get_spark()
    feats = spark.read.format("delta").load("./lakehouse/gold/trip_features")

    # latest feature row per city (the online lookup key)
    w = Window.partitionBy("city").orderBy(F.col("started_at").desc())
    latest = (feats.withColumn("rn", F.row_number().over(w))
                   .filter("rn = 1")
                   .select("city", "zone_demand_prev_hr", "_feature_version"))

    r = redis.Redis(host="localhost", port=6379)
    for row in latest.collect():
        # same value the model trained on; keyed for ms lookup at inference
        r.set(f"feat:zone:{row['city']}",
              json.dumps({"zone_demand_prev_hr": row["zone_demand_prev_hr"],
                          "v": row["_feature_version"]}))
```

### Star schema for BI (conformed dimensions)

```sql
-- models/marts/bi/fact_trips.sql   (dbt, gold layer)
-- Central fact at trip grain with FKs to CONFORMED dimensions.
{{ config(materialized='table', file_format='delta') }}
select
    t.trip_id,
    d_date.date_key,
    d_driver.driver_key,
    d_city.city_key,
    d_pay.payment_key,
    t.fare_sar,          -- measures
    t.distance_km,
    t.duration_min,
    t.surge_multiplier
from {{ ref('silver_trips') }} t
join {{ ref('dim_date') }}    d_date  on to_date(t.started_at) = d_date.date
join {{ ref('dim_driver') }}  d_driver on t.driver_id = d_driver.driver_id
join {{ ref('dim_city') }}    d_city  on t.city = d_city.city
join {{ ref('dim_payment') }} d_pay   on t.payment_method = d_pay.payment_method
```

```sql
-- serving/queries/exec_demand_dashboard.sql
-- Analyst-facing query over the star schema + hot mart.
select c.city, d.date, sum(f.fare_sar) as revenue_sar,
       count(*) as trips, avg(f.duration_min) as avg_duration
from fact_trips f
join dim_city c on f.city_key = c.city_key
join dim_date d on f.date_key = d.date_key
where d.date >= current_date() - interval 7 days
group by c.city, d.date
order by d.date, revenue_sar desc;
```

### Governing the serving boundary (PDPL)

```python
# src/masar/serve/bi_view.py
"""BI view exposes AGGREGATES and masked identifiers only — no raw PII.

Analysts get gold; rider_id/precise GPS never cross the serving boundary.
"""
from pyspark.sql import functions as F
from masar.spark import get_spark

def build_bi_safe_view() -> None:
    spark = get_spark()
    silver = spark.read.format("delta").load("./lakehouse/silver/trips")
    safe = (silver
        .withColumn("rider_pseudonym", F.sha2(F.col("rider_id"), 256))  # pseudonymise
        .drop("rider_id")                       # minimisation: drop raw PII
        # geohash granularity instead of precise lat/lon
        .select("trip_id", "city", "rider_pseudonym", "fare_sar",
                "duration_min", "started_at"))
    safe.write.format("delta").mode("overwrite").save("./lakehouse/gold/bi_trips_safe")
```

## Hands-on Lab 8 — Serve Masar Gold to AI and BI

| | |
|---|---|
| **Objective** | Serve the Masar gold layer to both consumers: a leakage-free training set + a consistent online feature slice for AI, and a conformed star schema + PDPL-safe BI view for analytics; then prove offline/online consistency and no leakage |
| **Duration** | 60 minutes |
| **Setup** | `git checkout lab8-start`; `gold/*` from Lab 7; `docker compose up redis`; dbt configured |

**Instructions & tasks**

1. *(10 min)* Build the training set with `training_join.py`; confirm every feature is point-in-time (spot-check a trip: its `zone_demand_prev_hr` uses only prior-hour trips). Record the (realistic, not inflated) baseline metric.
2. *(10 min)* **Leakage drill:** switch the feature window to include the current hour; retrain; observe the offline metric jump *unrealistically*. Revert and explain why the jump is a red flag.
3. *(15 min)* Run `materialize_online.py` to push the latest per-city feature to Redis. Verify the Redis value **equals** the offline gold value for the same city (offline/online consistency).
4. *(10 min)* Build the star schema (`fact_trips` + conformed `dim_*`); run `exec_demand_dashboard.sql`. Confirm one conformed `dim_date`/`dim_city` and that revenue reconciles with `gold.zone_hourly_demand`.
5. *(10 min)* Build `bi_trips_safe`: pseudonymise `rider_id`, drop precise GPS. Confirm no raw PII crosses the serving boundary. Note the PDPL controls applied in `LAB8_NOTES.md`.
6. *(5 min)* Commit: `feat(serve): AI feature serving + BI star schema + PDPL-safe view`.

**Expected output**
```
$ python -m masar.serve.materialize_online
pushed 5 city feature keys to redis
$ redis-cli get feat:zone:Riyadh
{"zone_demand_prev_hr": 142, "v": "v1"}   # == offline gold value for Riyadh
$ spark-sql -f serving/queries/exec_demand_dashboard.sql
Riyadh  2026-06-30  318450.0  4120  13.7
# leakage drill:
offline metric with prior-hour feature: R2=0.78   (realistic)
offline metric with current-hour feature: R2=0.95 (LEAKING — red flag)
```

**Acceptance criteria**
- Training set is point-in-time correct; leakage drill demonstrates the inflated-metric trap.
- Online Redis feature equals the offline gold value (consistency).
- Star schema uses conformed dimensions; BI revenue reconciles with the demand mart.
- BI-safe view exposes no raw rider IDs or precise GPS.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Offline metric suspiciously high | Feature leakage (current/future window) | Restrict window to strictly prior; audit |
| Online ≠ offline value | Feature recomputed for online | Materialise/copy from gold, never recompute |
| Dashboards disagree | Non-conformed dimension | Share one `dim_date`/`dim_city` |
| Raw rider_id in BI output | PII not masked | Pseudonymise + drop precise fields |
| Slow dashboard | Unoptimised gold | OPTIMIZE/ZORDER (M4) the mart |

**Instructor notes.** The leakage drill (task 2) is the emotional peak — watching a metric jump to "too good" and recognising it as a bug is the lesson that sticks. Reserve time for it. Fast finishers: add an online/offline consistency test to CI (compare Redis vs gold for all cities) — a perfect capstone extension.

## Mini Exercises

**Quiz (5 questions)**
1. What is feature leakage and why is it worse than it looks? → using info unavailable at prediction time; inflates offline metrics, collapses live.
2. How do you keep online and offline features consistent? → materialise/copy from the offline table; never re-implement.
3. What makes numbers reconcile across dashboards? → conformed dimensions (one shared `dim_date`, `dim_driver`).
4. When is an external serving store justified? → a measured millisecond-latency / high-concurrency requirement, as a derived copy.
5. True/False: BI dashboards should read raw rider IDs for flexibility. → **False** — PDPL: aggregate/pseudonymise at the boundary.

**Debugging exercise.** Give a feature table using the current-hour window; the model overfits live. Fix to strictly-prior and show the realistic metric.

**Modelling exercise.** Design the star schema for a "driver earnings" dashboard: name the fact grain, the dimensions, and one conformed dimension shared with `fact_trips`.

**Discussion questions.**
- Masar wants a live surge feature at inference in <50ms. Direct Lakehouse or external store? Justify and describe how you keep it consistent with training.
- Where do PDPL controls belong — in gold, in the serving view, or both? Why?

## Case Study — The ETA Model That Won Offline and Lost Live at "Wojhah"

**Scenario.** "Wojhah" (وجهة) shipped an ETA model scoring 0.93 R² offline; live it performed no better than the old heuristic. Trust in the data-science team is at risk.

**Business context.** Accurate ETAs drive rider retention; a model that looks great in review but fails live wastes a quarter and erodes credibility.

**Technical challenge.** Diagnose why offline and live diverge and fix it structurally, not with a patch.

**Constraints.** Cannot retrain endlessly; the fix must generalise (prevent the whole class of bug); the online path must stay under 50ms; PDPL still applies.

**Solution approach (facilitate, don't lecture).** Audit features for point-in-time correctness; find the current-hour-demand leak; restrict to prior-hour; serve the *same* feature table offline and materialise it online; add an offline/online consistency check and a leakage lint to CI; re-baseline the honest metric.

**Discussion questions.**
1. Why did the leaking feature score so well offline?
2. How does serving the same table offline and online prevent recurrence?
3. What automated check catches leakage before a model ships?
4. How do you rebuild stakeholder trust after an inflated metric is corrected downward?

## Benchmarks and Evaluation

| Metric | Category | Target after M8 | How measured |
|---|---|---|---|
| Point-in-time correctness | Correctness | 0 leaking features | window audit / leakage drill |
| Offline/online consistency | Correctness | online == offline value for all keys | Redis vs gold compare |
| Dimensional reconciliation | Correctness | BI revenue matches demand mart | cross-query check |
| PDPL at boundary | Governance | no raw PII in BI outputs | view schema audit |
| Dashboard latency | Performance | p95 ≤ 2 s on hot mart | query timing |
| Online feature latency | Performance | p99 ≤ 50 ms lookup | Redis benchmark |

**Example benchmark table (filled during lab):**

| Consumer | Serving path | Value/metric | Latency | Consistent? |
|---|---|---|---|---|
| training | offline gold | R²=0.78 (honest) | batch | — |
| leakage (sim) | offline gold, current-hr | R²=0.95 (fake) | batch | leaking |
| inference | Redis online | zone_demand_prev_hr=142 | 3 ms | == offline |
| exec dashboard | star schema mart | revenue reconciles | 0.6 s | conformed |

## Required Visuals and Training Assets

### Diagrams
1. **One truth, two contracts** — *Purpose:* the module's frame. *Elements:* gold feeding an AI feature table (entity×time) and a BI star schema (dims/facts) from the same source. *Style:* fork diagram, English + Arabic subtitles.
2. **Point-in-time correctness** — *Purpose:* leakage vs correct. *Elements:* a timeline where a correct feature uses only prior data and a leaking one peeks at the current/future window. *Style:* before/after timeline with a red "leak" marker.
3. **Offline/online consistency** — *Purpose:* the materialise-not-recompute pattern. *Elements:* one feature computed in the Lakehouse, materialised to an online store, both feeding a model. *Style:* flow with a "same value" seal.
4. **Star schema** — *Purpose:* BI modelling. *Elements:* `fact_trips` centre with `dim_date/driver/city/payment` points; a conformed dimension highlighted. *Style:* classic star.

### Images (screenshots)
1. **Leakage drill metrics** — the inflated vs honest metric side by side; *why:* makes "too good is a bug" visceral.
2. **Redis == gold** — the online value matching the offline table; *why:* consistency proof.
3. **Executive dashboard** — a rendered demand/revenue dashboard on the star schema; *why:* the BI payoff.

### Simulations
1. **Leakage overfit** — *Setup:* branch `sim-leak` uses the current-hour window. *Expected behaviour:* offline metric jumps, live would fail. *Learning objective:* point-in-time correctness is non-negotiable.
2. **Divergent online store** — *Setup:* online features recomputed independently. *Expected behaviour:* online ≠ offline for some keys. *Learning objective:* materialise, don't re-implement.

### Interactive Activities
- **Spot-the-leak (15 min):** eight feature definitions; teams flag which leak and why.
- **Star-schema design sprint (20 min):** teams model a new dashboard's star schema and identify conformed dimensions shared with `fact_trips`.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `gold/trip_features` | From Lab 7 | Delta | 48k rows | Training + online serving |
| `gold/zone_hourly_demand` | From Lab 7 | Delta | 720 rows | Reconciliation baseline |
| `dim_*` seeds | Course seeds (date/city/payment) | CSV | small | Star schema dimensions |

### Demo Requirements
- **Instructor demo:** run the leakage drill live — show the metric jump to "too good", diagnose the current-hour peek, fix to prior-hour, and show online==offline — the "one truth, two contracts, no leaks" close in 8 minutes.

---

# Final Capstone Project

## Title: The Masar Mini-Lakehouse — Production Data Platform for a Saudi Mobility Operator

## Project Scenario

You are the data platform engineer for **Masar (مسار)**, the national smart-mobility operator. The analytics team hands you raw feeds — batch trips and drivers, streaming GPS — and two demands: an **AI feature service** for an ETA/demand model, and an **operations BI dashboard** the leadership reviews every morning. Your mandate: deliver a production-grade Mini-Lakehouse that both teams can *trust* — because the platform proves its own quality, freshness, and governance. Everything you built in Labs 1–8 is a component; the capstone is the integration plus your own extensions.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Medallion architecture (LO1, LO7):** bronze (append-only, lineage) → silver (conformed) → gold (marts + feature table); documented layer contracts; no layer bypassed.
2. **Compute–storage discipline (LO2):** data in an object-storage-style layout; a short `BENCHMARKS.md` cost/scan analysis; gold marts OPTIMIZEd/ZORDERed with measured file-count reduction.
3. **ELT pipeline (LO3):** dbt (or Spark) staging → silver, incremental merge on `trip_id` with a lookback window; source-freshness + ≥ 6 data tests; a demonstrated late-arrival backfill.
4. **Delta Lake (LO4):** silver as constrained Delta (schema + CHECK); idempotent MERGE upserts; time-travel audit; OPTIMIZE/VACUUM with justified retention; one PDPL erasure demonstrated.
5. **Streaming (LO5):** Kafka GPS topic → Structured Streaming → Delta bronze, exactly-once with a dedicated checkpoint; a kill/restart proof of no duplicates; event-time windowed demand with a watermark.
6. **Quality, observability, governance (LO6):** Great Expectations suite with fail-fast + quarantine; freshness/volume/drift checks; PII classification + retention job; data docs as evidence.
7. **Orchestration (LO7):** the full medallion as one dependency-ordered, idempotent DAG, runnable by one command, with a demonstrated idempotent recovery from an injected mid-DAG failure.
8. **Serving (LO8):** a point-in-time-correct feature table served offline + materialised online (consistency proven); a conformed star schema BI mart that reconciles; a PDPL-safe serving view.

**One extension (choose at least one):**
- Offline/online consistency check wired into CI (Redis vs gold for all keys)
- A leakage-lint that fails the pipeline if a feature window includes non-prior data
- Multi-city backfill (7 days) proving idempotent correctness across the window
- A second streaming consumer group powering a live console demand view
- Trino/Databricks-SQL direct-serve endpoint benchmarked against the materialised mart

## Architecture (target state)

```
sources                         BRONZE            SILVER             GOLD                 consumers
 trips/drivers CSV ─batch─┐                                   ┌─ zone_hourly_demand ─┐
 GPS ─Kafka─stream────────┼─► append-only ─gate─► conformed ──┤  driver_daily        ├─► BI star schema
                          │   (Delta,       (GX  (Delta,       │                      │   (dashboard)
                          │    lineage)      +    constraints, └─ trip_features ──────┼─► AI feature svc
                          │                 quar) merge, TT)      (point-in-time)      │   (offline+online)
   orchestrated by ONE idempotent DAG:  land >> gate >> silver >> [gold...] >> maintain
   observability: freshness · volume · drift   |   governance: PII class · access · PDPL retention
```

## Deliverables

1. Git repository URL with full history and a one-command `make pipeline` (or DAG trigger).
2. A runnable Mini-Lakehouse producing all bronze/silver/gold tables with documented grains/contracts.
3. `BENCHMARKS.md` with the course benchmark tables filled from *your* runs (scan/cost, small-files, streaming dedup, serving latency).
4. `GOVERNANCE.md`: PII classification, access levels, retention policy with PDPL justification, and a demonstrated erasure.
5. 6-minute demo: one-command pipeline run, a streaming kill/restart (no dupes), a quality-gate quarantine, a time-travel audit, and the AI + BI consumers reading gold.
6. `DECISIONS.md`: five one-paragraph engineering decisions with rationale (e.g., partition key choice, VACUUM retention, stream vs batch boundary, online store yes/no, feature window).

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: bronze landing (batch+stream) + profiling | End Day 2 | instructor spot-check |
| M-B: ELT silver + Delta constraints + tests | End Day 3 | `dbt test` green + constrained Delta |
| M-C: streaming exactly-once + quality gate + governance | End Day 4 | kill/restart + quarantine demo |
| M-D: orchestrated DAG + gold + serving | Day 5 H2–H3 | one-command run + idempotent recovery |
| M-E: demo + submission | Day 5 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Architecture & medallion contracts | 15 | Clean bronze/silver/gold, contracts documented + enforced, no bypass | Minor contract gap or one bypass | Layers muddled, gold from bronze, no contracts |
| ELT & incrementality | 15 | Incremental merge + lookback; ≥ 6 tests; backfill proven | Incremental works; thin tests or shaky backfill | Full-refresh only; late-arrival bug; no tests |
| Delta Lake mastery | 15 | Constraints, idempotent MERGE, time travel, justified VACUUM, erasure | Most present; retention/erasure thin | No constraints, non-idempotent, VACUUM misused |
| Streaming | 15 | Exactly-once proven (kill/restart), watermark, checkpoint discipline | Streams but dedup/watermark weak | Duplicates on restart; processing-time aggregation |
| Quality, observability, governance | 15 | Gate acts (fail-fast+quarantine), obs signals fire, PII+PDPL retention | Some gaps (alert-only, partial obs) | Alerts only; no quarantine; raw PII kept forever |
| Orchestration & recovery | 15 | One-command idempotent DAG; clean failure recovery | Runs but recovery/idempotency partial | Hand-run steps; non-idempotent; no recovery |
| Serving (AI + BI) & demo | 10 | PIT-correct features, offline==online, conformed BI, PDPL-safe; crisp demo | Works; leakage or reconciliation thin | Leakage; online≠offline; raw PII served |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the running platform and repository evidence first* (one-command run, DAG recovery, data docs, benchmarks), demo second — the point of the course is that the platform speaks.
- Anti-pattern flags that cap a criterion at 70%: feature leakage; non-idempotent gold; VACUUM RETAIN 0; alert-only quality gate; raw rider IDs in BI outputs; streaming without a dedicated checkpoint.
- Verify one claim live: ask the participant to kill the stream and restart it and show zero duplicates, or to run the leakage drill and explain the inflated metric.

## Bonus Tasks (for early finishers / distinction seekers)

1. Wire an offline/online consistency test into CI and show it fail on an injected divergence.
2. Add a Trino/Databricks-SQL direct-serve path and benchmark it against the materialised mart.
3. Implement a data-contract test that fails the DAG when a gold grain is violated.
4. Add multi-city 7-day backfill and prove idempotent equivalence to incremental runs.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Which architecture combines lake economics with warehouse reliability? → Lakehouse.
**Q2.** What single property turns Parquet files into a Delta table? → the `_delta_log` transaction log.
**Q3.** In a decoupled platform, which cost axis is usually the controllable lever? → compute (elastic), not storage.
**Q4.** Two Parquet features that make remote reads cheap? → column pruning; row-group min/max stats (data skipping).
**Q5.** Why did ELT win on the cloud over ETL? → cheap storage keeps raw; elastic compute transforms in-platform (reprocessable, auditable).
**Q6.** What bug does a lookback window fix in an incremental model? → late-arriving data missed by a `date = today` filter.
**Q7.** Why is MERGE-on-key idempotent but INSERT is not? → re-applying matched rows updates nothing; INSERT duplicates.
**Q8.** Which ACID property does Delta snapshot isolation provide? → Isolation (readers see a consistent version).
**Q9.** What does VACUUM trade away to reclaim storage? → time-travel history beyond the retention window.
**Q10.** Why is partitioning by `trip_id` a mistake? → millions of tiny files (the small-files problem).
**Q11.** Which two mechanisms give Structured Streaming + Delta exactly-once? → checkpointed Kafka offsets + Delta atomic per-batch commit.
**Q12.** Event time vs processing time — which must windowed aggregations use, and why? → event time, so late events count in the right window.
**Q13.** What does a streaming watermark bound? → how long late data is awaited / state kept before finalising a window.
**Q14.** Where in the medallion should the quality gate run? → at promotion (bronze → silver).
**Q15.** Give one failure warranting fail-fast and one warranting quarantine. → null/duplicate key (fail-fast); a few out-of-range values (quarantine).
**Q16.** Name two observability signals that row-level checks miss. → freshness, volume (also distribution drift).
**Q17.** Which PDPL principle argues against keeping precise GPS forever? → data minimisation / retention limits.
**Q18.** What is feature leakage and why does it fool reviewers? → using info unavailable at prediction time; inflates offline metrics, fails live.
**Q19.** How do you keep online and offline features consistent? → materialise/copy from the offline table; never re-implement.
**Q20.** What makes numbers reconcile across dashboards? → conformed dimensions (one shared `dim_date`/`dim_driver`).

## Practical Assessments

**PA-1 (30 min, Day 3):** Given a Delta table VACUUMed with `RETAIN 0` and a non-idempotent MERGE, restore correctness: fix retention, make the upsert idempotent, and prove time travel + a clean second run. Scored on diagnosis notes (40%), fixes (40%), verification evidence (20%).

**PA-2 (30 min, Day 4):** Given a streaming job with no checkpoint and a processing-time aggregation, produce exactly-once ingestion and an event-time windowed demand with a watermark; prove no duplicates on restart. Scored on correctness of fix (50%), evidence (30%), reasoning about semantics (20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (8 labs) | 30% | checkpoint commits + expected outputs |
| PA-1 + PA-2 | 20% | artefacts + notes |
| Quiz | 10% | 10-question selection |
| Capstone (Mini-Lakehouse) | 40% | rubric, platform-first |

Badge issuance (Data-engineering badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical quarantine/benchmark artefacts across repos are checked) **and** no PDPL red flags (raw personal data served or retained beyond policy).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone course org repos; push checkpoint tags (`lab1-start` … `lab8-start`, `bad-batch`, all `sim-*` branches)
- [ ] Regenerate the Masar synthetic dataset (trips, GPS NDJSON, drivers) with the pinned generator seed; verify row counts match the lab specs
- [ ] Dry-run all 8 labs end-to-end on a clean machine **and** on the hosted-notebook fallback (Databricks CE / Colab)
- [ ] Bring up the single-broker Kafka + Redis `docker compose` stack and pre-pull images (streaming lab is the boot-time risk)
- [ ] Verify Spark 3.5 + `delta-spark` 3.2 + `dbt-spark` + `great-expectations` install cleanly from the pinned lock file
- [ ] Print A4 posters: medallion architecture, Delta transaction log, exactly-once diagram, quality-gate flow, Mini-Lakehouse full pipeline
- [ ] Load fixtures into the shared drive: dirty batches, late trip, currency-shift city, late pings, erasure request
- [ ] Prepare the shared leaderboard (small-files reduction, streaming dedup, serving latency)
- [ ] Confirm classroom network allows the package index and Kafka/Redis containers; in restricted environments pre-pull to a local registry

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.11 + Java 17 + git + a GitHub account
- [ ] `pip install pyspark==3.5.* delta-spark==3.2.* dbt-core dbt-spark great-expectations kafka-python redis apache-airflow`
- [ ] Docker Desktop (WSL2 on Windows) or Colima; verify `docker run hello-world`
- [ ] `docker compose up` the provided `kafka` + `redis` stack; verify a test produce/consume
- [ ] VS Code + Python + Spark/Jupyter extensions (or preferred IDE)
- [ ] Clone course repo; run `make doctor` (validates Java, Spark, Delta, Kafka, Redis, dbt and prints ✓/✗)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Java version / `JAVA_HOME` wrong for Spark | High | Pin Java 17; first-hour floater support; hosted-notebook fallback |
| Delta extension not configured | High | Always use `get_spark()`; verify `spark.sql.extensions` |
| Kafka container won't start / port clash | High | Pre-pull images; free 9092; provide a compose healthcheck |
| Streaming duplicates on restart | Medium | One dedicated `checkpointLocation` per query (the M5 lesson) |
| Small-files / slow reads after streaming | Medium | Scheduled OPTIMIZE; teach it as maintenance, not a fix |
| dbt-spark connection/profile errors | Medium | Provide a working `profiles.yml`; run `dbt debug` first |
| Feature leakage passes unnoticed | Medium | Make the leakage drill mandatory; add the leakage-lint bonus |
| PySpark on Apple Silicon quirks | Medium | Use the provided arm64-compatible images; document `JAVA_HOME` |
| Confusion between event vs processing time | Medium | Human-Kafka activity + the watermark clinic |
| VACUUM removes nothing / RETAIN 0 blocked | Low | Explain the 7-day safety window; never disable in prod |

## Timing Recommendations

- Protect Lab 4 (Delta) and Lab 5 (streaming) at full length; compress M2 theory (cost model lands through the lab) if behind.
- If a cohort is strong: pull the offline/online CI check and multi-city backfill into main scope on Day 5.
- If a cohort is weak: run the streaming exactly-once as a guided demo rather than a solo lab, but never skip the kill/restart *observation* — it is the module's thesis made visible.
- Hard rule: the Mini-Lakehouse assembly (Day 5 H4) must start on time; cut discussion, not build time.
- Reserve the leakage drill (M8) even if compressing — it is the single most memorable lesson and directly protects the capstone.

## Discussion Prompts (use during transitions)

1. "Your BI dashboard and your data scientist report different 'completed trips' numbers. Which architecture decision caused it, and which one fixes it?"
2. "Storage is cheap and compute is elastic — so why did the migration bill go *up*? What discipline did they skip?"
3. "A regulator asks what a table contained three weeks ago. Can your platform answer, and what must be true about VACUUM for it to?"
4. "A model scores 0.95 offline. Are you excited or suspicious — and what do you check first?"
5. "If the platform is the audit evidence and the morning decision, what does *your* current pipeline testify about your team's reliability?"

## Wrap-up (Day 5 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it (one slide): medallion (M1), economics (M2), ELT (M3), Delta (M4), streaming (M5), quality/governance (M6), orchestration (M7), serving (M8).
- Forward pointer: SDA-DSC-215 (Big Data Analytics with Spark) scales *exactly* this Lakehouse to enterprise volumes with distributed execution, partitioning, and MLlib; SDA-DSC-313 builds advanced pipelines on this same substrate.
- Collect: repo URLs, `BENCHMARKS.md`, `GOVERNANCE.md`, `DECISIONS.md`, and the `mini_lakehouse/` folder; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.11, Spark 3.5, Delta Lake 3.2, dbt 1.7+, Great Expectations 0.18+, and a single-broker Kafka. Verify pinned versions in the course lock file before each delivery. City names and business terms carry Arabic subtitles in slides; all code, table names, and identifiers remain in English per Saudi enterprise convention. PDPL obligations are treated as first-class constraints throughout.*
