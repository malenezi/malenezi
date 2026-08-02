# Big Data Analytics with Spark
## تحليلات البيانات الضخمة باستخدام Spark

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Big Data Analytics with Spark |
| **Arabic Title** | تحليلات البيانات الضخمة باستخدام Spark |
| **Code** | SDA-DSC-215 |
| **Level** | Specialist |
| **Duration** | 3 days × 5 learning hours = **15 hours** |
| **Audience** | Data scientists and engineers working with large-scale data |
| **Prerequisites** | SDA-DSC-214 or equivalent Spark exposure |
| **Assessment** | Labs; large-scale analytics project |
| **Stackability** | Big-data badge · Part of the Data Engineering for AI specialisation · Next: SDA-DSC-313 |
| **Tools & Platforms** | PySpark · Spark SQL · MLlib · Delta Lake |

## Course Description

A specialist module on analysing datasets too large for a single machine. Participants master distributed computing concepts, write performant Spark transformations and SQL, and tune jobs through partitioning and caching. The module scales every prior analytics skill to enterprise data volumes.

The course is built around a single evolving artefact: **"Masar" (مسار), a national mobility and logistics analytics platform**. Participants work against a Saudi-scale ride-hailing and delivery dataset — roughly 2.1 billion trip events per year (~180 GB of Delta-formatted data), plus driver, rider, weather, and city dimension tables. Every lab processes this same golden dataset: Day 1 reads and queries it, Day 2 makes those queries fast, Day 3 trains a distributed ML model on it and packages an end-to-end batch analytics workflow. By the final capstone each participant owns a tuned, query-plan-optimised, MLlib-powered analytics job on Lakehouse storage — the same shape of workload they will extend into streaming in SDA-DSC-313.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Explain distributed execution: partitions, shuffles, and lazy evaluation
2. **LO2** — Develop analytical workloads with Spark DataFrames and Spark SQL
3. **LO3** — Optimize job performance through partitioning, caching, and join strategies
4. **LO4** — Implement scalable feature-engineering and ML pipelines with Spark MLlib
5. **LO5** — Analyze query plans to diagnose and resolve performance bottlenecks
6. **LO6** — Design batch analytics workflows on Lakehouse storage

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Think distributed, query at scale | M1: Distributed Computing Fundamentals · M2: Spark DataFrames & Spark SQL | 50% | 50% | Working Spark session over the Masar Delta lake + a city-revenue analytics query set |
| **Day 2** | Make it fast, prove it with the plan | M3: Shuffles, Partitioning & Caching · M4: Performance Tuning & Query Plans | 45% | 55% | A slow job re-engineered: broadcast join + repartition + AQE, with before/after query plans and runtimes |
| **Day 3** | Learn at scale, ship the pipeline | M5: Spark MLlib Pipelines at Scale · M6: Big-Data Analytics Project · Capstone | 35% | 65% | Distributed cancellation-prediction pipeline + a productionised batch analytics job on the Lakehouse |

## Hour-by-Hour Breakdown

### Day 1 — Think Distributed, Query at Scale

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why single-machine analytics breaks** + course kickoff | Recognise the volume/velocity wall; map the 6 modules; meet the Masar dataset and cluster | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Distributed execution model** (M1) | Driver/executors, partitions, tasks, stages, lazy evaluation, DAG, Lakehouse storage | Lecture + Spark UI walkthrough | 70/30 |
| 3 | **Lab 1 — First distributed job** | Start a session, read the Masar Delta table, inspect partitions, read the DAG in the Spark UI | Guided lab (pairs) | 15/85 |
| 4 | **DataFrames and Spark SQL** (M2) | DataFrame API, transformations vs actions, Spark SQL, Catalyst, windows, joins | Lecture + live query demo | 65/35 |
| 5 | **Lab 2 — City revenue analytics** | Build revenue/cancellation analytics with DataFrames + Spark SQL over `trips` | Guided lab (pairs) | 15/85 |

### Day 2 — Make It Fast, Prove It With the Plan

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Shuffles and partitioning** (M3) | Wide vs narrow transformations, the shuffle, partition sizing, repartition vs coalesce, bucketing | Lecture + shuffle-in-the-UI demo | 65/35 |
| 2 | **Lab 3 — Diagnose and fix a shuffle** | Cut a shuffle-heavy join; apply partitioning + caching; measure shuffle read/write | Guided lab | 15/85 |
| 3 | **Query plans and performance tuning** (M4) | `explain()`, Catalyst + Tungsten, AQE, join strategies, skew, pushdown, spill | Lecture + plan-reading clinic | 70/30 |
| 4 | **Lab 4 — Read the plan, kill the bottleneck** | Broadcast join, AQE skew handling, partition pruning; before/after physical plans | Guided lab | 10/90 |
| 5 | **Tuning clinic + benchmark board** | Consolidate tuning wins; fill the shared benchmark leaderboard; config review | Lab + discussion | 20/80 |

### Day 3 — Learn at Scale, Ship the Pipeline

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **MLlib pipelines at scale** (M5) | Transformers/Estimators, Pipeline, distributed feature engineering, evaluation, persistence | Lecture + pipeline demo | 65/35 |
| 2 | **Lab 5 — Cancellation-prediction pipeline** | Build a Spark ML `Pipeline`: assemble features, train, cross-validate, evaluate at scale | Guided lab | 10/90 |
| 3 | **Batch analytics on the Lakehouse** (M6) + **Lab 6** | Idempotent Delta writes, incremental processing, partition layout, job structure | Micro-lecture + lab | 30/70 |
| 4 | **Capstone assembly** | Integrate query + tuning + ML + batch job into one analytics workflow; peer plan review | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric-based scoring; path to SDA-DSC-313 (streaming) | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module runs against the same **Masar** mobility dataset. Never introduce a throwaway `range(100)` toy example except for a 60-second concept demo — always return to `trips`, `drivers`, `riders`, `weather`. This is what makes the Day-3 capstone achievable: the data, schema, and helper functions are already familiar by then.
- **Two data scales.** The narrative uses the *full* dataset (2.1 B rows / 180 GB) for realism; the classroom runs a **sampled 50 M-row / ~4.2 GB Delta subset** that fits a 16 GB laptop or a small 3-node cluster. Always state which scale a number refers to. Publish both `masar_sample` (laptop) and `masar_full` (cluster, optional) so numbers are reproducible.
- **Environment strategy:** primary = local PySpark 3.5 in a `uv`/conda env with Delta Lake 3.x (`--packages io.delta:delta-spark_2.12:3.2.0`); fallback = a managed Spark notebook (Databricks Community / Google Dataproc / a shared 3-node cluster). Verify both the week before delivery; the Spark UI must be reachable (port 4040) in whichever environment wins.
- **Pace control:** Labs 3 and 4 are the most overrun-prone because plan-reading is new. Publish checkpoint notebooks (`lab3_start`, `lab3_solution`, `lab4_start`, ...) so stragglers can fast-forward. Keep every lab's dataset path in one `config.py` so a path change is one edit.
- **Pairing:** rotate pairs each day; pair a strong-SQL participant with a strong-Python/ML participant. Reading a physical plan together out loud is the single highest-value activity of Day 2.
- **Language:** deliver in English or Arabic; keep all code, column names, and table identifiers in English (production convention in Saudi enterprise data platforms — mixed-language column names break Spark SQL and downstream BI).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Kick off any full-dataset cluster job *before* a break so the run completes while people are away — big-data waits are a teaching reality, use them deliberately.
- **Assessment logistics:** collect notebook/repo URLs and the `BENCHMARKS.md` table at the end of Day 3 Hour 4; verify each capstone job actually runs against the sample lake before demos begin in Hour 5.

---

# Module 1 — Distributed Computing Fundamentals

## Module Overview

**Purpose.** Before writing a single fast Spark query, participants must hold an accurate mental model of what happens when they call `.count()` on two billion rows. This module builds that model: how Spark splits data into partitions, distributes work across executors as tasks, defers computation until an action forces it, and assembles the whole job as a DAG of stages separated by shuffles. Every optimisation later in the course is an application of this one mental model.

**Business relevance.** Saudi organisations — a national mobility platform, a telecom operator's CDR lake, a bank's transaction history, a ministry's service-usage records — routinely hold datasets that no single server can process. The difference between an analyst who "runs pandas until it OOMs" and one who reasons in partitions and stages is the difference between a query that never finishes and one that returns in seconds against the same data. Distributed literacy is the price of admission to enterprise-scale analytics under Vision 2030 data programmes.

**Industry use cases.**
- A mobility platform computes daily completed-trip revenue per city across 2.1 billion yearly trips — impossible in memory on one machine, trivial as a partitioned Spark aggregation.
- A telecom fraud team scans a year of call-detail records to flag SIM-box patterns; the scan only finishes because it is parallelised across dozens of executors reading independent partitions.
- A government analytics unit joins service-usage logs to a citizen dimension table nightly; understanding the shuffle that join triggers is what keeps the nightly window under two hours.

**Expected competencies.** After this module a participant can describe the driver/executor architecture, explain why `read` then `filter` then `count` runs nothing until `count`, count and reason about partitions, read a job's stages in the Spark UI, and identify where a shuffle boundary falls.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain the driver/executor/cluster-manager architecture and where user code runs | LO1 |
| 1.2 | Distinguish transformations from actions and explain lazy evaluation and the DAG | LO1 |
| 1.3 | Reason about partitions: how data is split, how many tasks run, why size matters | LO1 |
| 1.4 | Identify stage boundaries and shuffles by reading the Spark UI DAG | LO1, LO5 |
| 1.5 | Position Spark over Lakehouse (Delta) storage and explain compute–storage separation | LO1, LO6 |

## Technical Content

### 1. The scale wall: why one machine is not enough

A single 32 GB laptop can hold maybe 10–15 GB of pandas DataFrame before it thrashes and dies. The Masar `trips` table is ~180 GB in compressed Delta/Parquet — several terabytes uncompressed in memory. Three responses exist: sample (lose fidelity), buy a bigger machine (vertical scaling — hits a hard ceiling and a huge bill), or **split the work across many machines** (horizontal scaling). Spark is the mature, ubiquitous engine for the third option.

The key idea participants must internalise: **the data is divided into independent chunks (partitions), and the same function runs on each chunk in parallel, on different cores and different machines.** Analytics that are "embarrassingly parallel per row" (filter, map, most aggregations) scale almost linearly. The expensive operations are the ones that require data to *move between machines* — the shuffle — which is the theme of Modules 3 and 4.

**Instructor note:** open the lesson by trying `pd.read_csv` (or `pd.read_parquet`) on the full Masar export live. Let it either OOM or take minutes. The visceral failure earns you the next three days.

### 2. Spark's execution architecture

Spark is a **driver–executor** system coordinated by a **cluster manager**:

| Component | Role | Where your code runs |
|---|---|---|
| **Driver** | Runs your program, builds the logical/physical plan, schedules tasks, collects results. Holds the `SparkSession`. | Your `main`/notebook and the *plan* live here |
| **Cluster manager** | Grants executors (YARN, Kubernetes, Standalone, or `local[*]`) | — |
| **Executors** | JVM processes on worker nodes; each has cores (task slots) and memory; run tasks and cache data | Your *per-partition* logic runs here |
| **Task** | The unit of work: one function applied to one partition on one core | The smallest schedulable piece |

A job with 200 partitions and 25 executor cores runs 25 tasks at a time, in 8 waves. The single most common beginner mistake is calling `.collect()` and pulling all 2 billion rows back to the driver — which promptly OOMs. The driver is a coordinator, not a data sink; only ever collect aggregated or sampled results.

**Compute–storage separation (Lakehouse).** In the modern stack — the one taught in the prerequisite SDA-DSC-214 — executors read from object storage (S3-compatible, HDFS, ADLS) holding **Delta Lake** tables, not from disks welded to the compute. Compute is elastic and ephemeral; storage is durable and cheap. Masar's lake lives at `s3a://masar-lakehouse/curated/` and any size of cluster can be pointed at it. This is why the same query runs on a laptop (sample) and a 40-node cluster (full).

### 3. Partitions: the atom of parallelism

A **partition** is a contiguous chunk of the dataset that a single task processes. Partitioning determines parallelism: *N partitions ⇒ up to N tasks in parallel.* Where partitions come from:

- **On read**, Spark derives partitions from the files. Parquet/Delta files are typically ~128 MB each; 180 GB ≈ ~1,400 file-based partitions. One badly written 40 GB file = one giant partition = one core doing all the work while 39 sit idle.
- **After a shuffle**, the number is set by `spark.sql.shuffle.partitions` (default 200) or chosen by Adaptive Query Execution (Module 4).
- **Explicitly**, via `repartition(n)` / `coalesce(n)` (Module 3).

Healthy partition size is roughly **128–256 MB** / a few hundred thousand to a few million rows. Too few → poor parallelism and out-of-memory tasks. Too many tiny partitions → scheduling overhead dominates (the "small files problem"). Inspect with:

```python
df.rdd.getNumPartitions()   # how many partitions right now
```

### 4. Lazy evaluation, transformations, actions, and the DAG

Spark separates *describing* work from *doing* work:

- **Transformations** (`select`, `filter`, `join`, `groupBy`, `withColumn`) are **lazy** — they build up a plan and return a new DataFrame; nothing executes.
- **Actions** (`count`, `collect`, `show`, `write`, `take`) are **eager** — they trigger execution of the whole accumulated plan.

```python
trips = spark.read.format("delta").load(TRIPS_PATH)   # lazy: no rows read
completed = trips.filter(trips.status == "completed")  # lazy
riyadh = completed.filter(trips.city == "Riyadh")      # lazy
riyadh.count()                                          # ACTION: now it runs
```

Laziness is not a quirk — it is the optimiser's opportunity. Because Spark sees the *whole* chain before running, Catalyst (Module 2/4) can push the two filters down to the file scan, read only Riyadh's completed trips, and never materialise the intermediate DataFrames. The mental model: **transformations write the recipe; the action cooks the meal; the optimiser rewrites the recipe first.**

**Jobs, stages, tasks.** An action launches a **job**. The job is broken into **stages** at every **shuffle boundary** (wide transformation). Each stage is a set of **tasks**, one per partition, that can all run without moving data. Reading the Spark UI, participants see: 1 action → 1 job → N stages → many tasks. Stage boundaries are where the data reshuffles — and where the time goes.

### 5. Narrow vs wide dependencies (the shuffle preview)

- **Narrow** transformation: each output partition depends on one input partition (`filter`, `select`, `withColumn`). No data movement; pipelined within a stage.
- **Wide** transformation: each output partition depends on *many* input partitions (`groupBy`, `join`, `distinct`, `orderBy`). Data must be **shuffled** across the network so that all rows with the same key land together. This creates a new stage.

This distinction — foreshadowed here, developed fully in Module 3 — is the root of nearly all Spark performance work. Every wide transformation is a network-and-disk cost; every optimisation is about doing fewer, smaller, or cheaper shuffles.

### 6. Common mistakes & production considerations

**Common mistakes (each appears in the Lab 1 starter):**
1. `.collect()` on a huge DataFrame — pulls everything to the driver and OOMs. Use `.show(20)`, `.take(n)`, or aggregate first.
2. Treating a DataFrame like it re-runs cheaply — calling an action inside a Python loop re-executes the *entire* lineage each time (fix: cache, Module 3).
3. Reading a single monster CSV instead of partitioned Parquet/Delta — no parallelism, no column pruning, no predicate pushdown.
4. Assuming a transformation "did something" because it returned instantly — it was lazy; the cost lands at the next action.
5. Setting `local[1]` and concluding "Spark is slow" — one core, no parallelism.
6. Ignoring partition count after a filter that drops 99% of rows — 200 nearly empty partitions waste scheduling (fix: `coalesce`, Module 3).

**Production considerations.**
- **Right-size the cluster to the data and the shuffle**, not to a habit. Cores × memory-per-core should match partition size and count.
- **Prefer columnar Lakehouse formats** (Delta/Parquet). They give column pruning, predicate pushdown, and statistics for free — the single biggest, cheapest win before any tuning.
- **Version what the job depends on**: Spark version, Delta version, table snapshot (Delta time-travel version), and config. A "slow job" is often a config drift.
- **Observe every job in the Spark UI.** The UI is not optional; it is the primary instrument for the rest of this course.

## Code Examples

### Session bootstrap over the Masar Delta lake

```python
# src/masar/session.py
"""One place to build the SparkSession for the whole course.
Delta Lake wired in; sensible defaults for a small classroom cluster."""
from pyspark.sql import SparkSession


def build_session(app_name: str = "masar-analytics", local: bool = True) -> SparkSession:
    builder = (
        SparkSession.builder.appName(app_name)
        # Delta Lake catalog + SQL extensions
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        # Adaptive Query Execution on from the start (Module 4 explains it)
        .config("spark.sql.adaptive.enabled", "true")
        # Default post-shuffle partitions; AQE will coalesce down as needed
        .config("spark.sql.shuffle.partitions", "200")
    )
    if local:
        # Use every core on the laptop; give the driver room for the sample data
        builder = builder.master("local[*]").config("spark.driver.memory", "8g")
    return builder.getOrCreate()


# Canonical dataset paths — the ONE source of truth for every lab
TRIPS_PATH   = "s3a://masar-lakehouse/curated/trips"      # cluster
TRIPS_SAMPLE = "./lakehouse/trips_sample"                 # laptop (50M rows)
DRIVERS_PATH = "./lakehouse/drivers"
RIDERS_PATH  = "./lakehouse/riders"
WEATHER_PATH = "./lakehouse/weather"
```

### Lazy evaluation made visible

```python
# notebooks/01_lazy_demo.py
from masar.session import build_session, TRIPS_SAMPLE

spark = build_session("lazy-demo")

# Each line below is LAZY — returns instantly, reads nothing.
trips = spark.read.format("delta").load(TRIPS_SAMPLE)
completed = trips.filter("status = 'completed'")
riyadh = completed.filter("city = 'Riyadh'")
revenue = riyadh.selectExpr("fare_sar")

print("Nothing has executed yet. Partitions:",
      trips.rdd.getNumPartitions())          # metadata only, still no scan

# The ACTION. Watch the Spark UI (http://localhost:4040) light up now.
total = revenue.agg({"fare_sar": "sum"}).collect()[0][0]  # aggregated => safe to collect
print(f"Riyadh completed-trip revenue (sample): {total:,.0f} SAR")

# See what Spark WILL do before it does it (full treatment in Module 4)
revenue.explain(mode="formatted")
```

### Inspecting partitions and the physical scan

```python
# notebooks/01_partitions.py
trips = spark.read.format("delta").load(TRIPS_SAMPLE)

print("Partitions on read:", trips.rdd.getNumPartitions())   # e.g. 34

# Rows per partition — reveals skew early (one fat partition = one slow task)
from pyspark.sql.functions import spark_partition_id, count as _count
(trips.groupBy(spark_partition_id().alias("pid"))
      .agg(_count("*").alias("rows"))
      .orderBy("pid")
      .show(50, truncate=False))

# A filter is a NARROW transformation: same partition count, no shuffle, no new stage
completed = trips.filter("status = 'completed'")
print("Partitions after filter:", completed.rdd.getNumPartitions())  # unchanged
```

## Hands-on Lab 1 — Your First Distributed Job on Masar

| | |
|---|---|
| **Objective** | Start a Delta-enabled Spark session, read the Masar `trips` sample, reason about partitions, run a first action, and read the resulting job/stages/tasks in the Spark UI |
| **Duration** | 50 minutes |
| **Setup** | Python 3.11, PySpark 3.5, `delta-spark` 3.2, sample lake extracted to `./lakehouse/`, `git checkout lab1_start` |

**Instructions & tasks**

1. *(5 min)* Launch a session with `build_session()`; confirm the Spark UI is reachable at `http://localhost:4040`.
2. *(10 min)* Read `trips_sample` as Delta. Print the schema, the row count, and `getNumPartitions()`. Record the partition count in your notes.
3. *(10 min)* Run the rows-per-partition query from the code examples. Identify whether partitions are balanced. Screenshot the distribution.
4. *(10 min)* Build the lazy chain `filter(status='completed') → filter(city='Riyadh') → sum(fare_sar)`. Before the action, predict how many stages you will see. Then run `.collect()` on the aggregate and check the Spark UI Jobs tab.
5. *(10 min)* In the SQL/DataFrame tab of the UI, open the query and locate the file scan, the filter, and the aggregate exchange. Count the stages; confirm your prediction.
6. *(5 min)* Deliberately mis-collect: run `trips.collect()` with a 5-second patience limit, cancel it, and write one sentence explaining why it is dangerous.

**Expected output**
```
Schema: trip_id, rider_id, driver_id, city, service_type, distance_km,
        fare_sar, surge_multiplier, payment_method, status, request_ts,
        pickup_ts, dropoff_ts, event_date
Rows (sample): 50,000,000
Partitions on read: 34
Riyadh completed-trip revenue (sample): 41,382,905 SAR
Jobs for the aggregate: 1 job, 2 stages (scan+partial-agg -> shuffle -> final-agg)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `Delta ... is not a valid Spark SQL Data Source` | Delta jars not on the classpath | Launch with `--packages io.delta:delta-spark_2.12:3.2.0` or set the two Delta configs in `build_session` |
| Spark UI 404 at :4040 | Port taken by another session; UI moves to 4041 | Check the driver log line "Bound SparkUI to ..."; open that port |
| `count()` takes minutes on a laptop | Reading full lake, not the sample | Confirm `TRIPS_SAMPLE` path; verify ~4.2 GB not 180 GB |
| Notebook freezes on `collect()` | Pulling all rows to the driver | Kill the job in the UI; aggregate or `.show()` instead — the lesson landed |

**Instructor notes.** Task 6 is the emotional anchor of the day — the frozen `collect()` teaches "the driver is not a data sink" more effectively than any slide. Fast finishers: have them repartition the DataFrame to 8 and re-run the rows-per-partition query to preview Module 3.

## Mini Exercises

**Quiz (5 questions)**
1. Which runs the job: `df.filter(...)` or `df.count()`? → `count()` (action); filter is a lazy transformation.
2. Where does `.collect()` send data, and why is that dangerous at scale? → to the driver; it can OOM the coordinator.
3. You read a 180 GB Delta table stored as ~1,400 files of ~128 MB. Roughly how many read partitions? → ~1,400.
4. A `groupBy(...).count()` — narrow or wide? What does it create? → wide; a shuffle and a new stage.
5. True/False: more partitions is always faster. → False (tiny partitions add scheduling overhead — the small-files problem).

**Debugging exercise.** Give participants a snippet that loops over 12 cities, filtering and counting inside a Python `for` loop off an uncached DataFrame. Ask them to explain why the Spark UI shows 12 full re-scans of the table, then propose the fix (cache — full treatment in Module 3).

**Prediction exercise.** Before running, have pairs predict the number of stages for: (a) `read → filter → count`, (b) `read → groupBy(city).sum → collect`, (c) `read → join(drivers) → count`. Then verify in the UI.

**Discussion questions.**
- Your analyst says "just give me a bigger laptop." When is vertical scaling the right answer, and where is its ceiling for Masar's 180 GB?
- Compute and storage are separated in the Lakehouse. What does that let you do operationally that a fixed HDFS cluster does not?

## Case Study — The Overnight Report That Never Finished

**Scenario.** "Masar" analytics runs a nightly "city performance" report: revenue, completion rate, and average fare per city for the previous day. A new analyst, comfortable in pandas, rewrote it to `toPandas()` the day's trips and compute in memory on the driver. It worked in staging (one small city) and OOM-killed the driver every night in production once Riyadh and Jeddah volumes were included.

**Business context.** The report feeds the 07:00 operations standup. Three consecutive nights of missing numbers escalated to the data platform lead. Each failed run also blocked the shared cluster for 40 minutes before the OOM.

**Technical challenge.** Rewrite the report to stay distributed end-to-end: never materialise all rows on the driver, aggregate in Spark, and collect only the ~40-row city summary.

**Constraints.** Same cluster, same nightly window (must finish < 20 min); output is a Delta table `curated/daily_city_report` partitioned by `event_date`; no change to upstream ingestion.

**Solution approach (facilitate, don't lecture).** (1) Locate the `toPandas()` — the single line that abandons distribution. (2) Replace with a Spark `groupBy("city").agg(...)`. (3) Only `.collect()`/write the 40-row result. (4) Confirm in the UI that the scan is filtered by `event_date` (partition pruning, Module 4) and no stage moves all rows to the driver. (5) Add a row-count guardrail so a future in-memory regression is caught in review.

**Discussion questions.**
1. Why did it pass in staging but fail in production? (data-volume-dependent bug — the worst kind)
2. Which single line abandoned distribution, and how would a code reviewer spot it? (`toPandas()` / `collect()` before aggregation)
3. The report is 40 rows. Where is it safe to `collect()`, and where is it not? (only after the aggregation reduces to summary size)
4. How would partitioning the output by `event_date` help tomorrow's incremental run? (prunes and enables idempotent overwrite of one partition)

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Read partition count (sample) | Correctness | 30–40 (balanced) | `df.rdd.getNumPartitions()` |
| Driver memory stability on report | Reliability | No driver OOM; peak < 4 GB | Spark UI Executors tab |
| Stages identified for a groupBy | Understanding | Learner names 2 stages correctly | UI DAG walkthrough |
| Full-scan avoidance on filtered read | Performance | Only matching files scanned | UI SQL tab "files read" |
| Time-to-first-result (sample count) | Performance | < 20 s on lab laptop | wall-clock / UI job duration |

**Example benchmark table (filled during lab):**

| Operation (50 M sample) | Wall time | Stages | Shuffle read |
|---|---|---|---|
| `trips.count()` | 6.3 s | 1 | 0 |
| `filter(city).sum(fare)` | 8.1 s | 2 | 12 MB |
| `groupBy(city).agg(...)` | 11.4 s | 2 | 240 MB |

## Required Visuals and Training Assets

### Diagrams
1. **Spark cluster anatomy** — *Purpose:* anchor image for the whole course. *Elements:* driver box (holds SparkSession + plan), cluster manager, 3–4 executor boxes each with cores and cache, arrows showing task dispatch and result return; a red crossed-out fat arrow labelled "collect() of all rows → driver". *Style:* flat vector, English labels with Arabic subtitles.
2. **Lazy DAG build-up** — *Purpose:* make laziness concrete. *Elements:* a chain of transformation nodes greyed-out ("planned, not run") then an action node that turns the whole chain green. *Style:* left-to-right flow, before/after shading.
3. **Job → stages → tasks decomposition** — *Purpose:* map the Spark UI vocabulary. *Elements:* one action fanning to 1 job → 2 stages split by a shuffle → many task boxes per stage. *Style:* nested-bracket diagram matching the UI colours.
4. **Partition-to-task mapping** — *Purpose:* explain parallelism. *Elements:* 8 partitions mapped onto 4 cores in 2 waves; a skewed variant where one fat partition serialises the whole stage. *Style:* grid with a "skew" warning panel.

### Images (screenshots)
1. **Spark UI Jobs tab** for the Riyadh-revenue query — *why:* participants must locate jobs; *content:* one job, two stages, durations visible.
2. **Spark UI SQL/DataFrame tab** showing the filtered scan + exchange + aggregate — *why:* first exposure to a plan graph.
3. **Executors tab** during a healthy run — *why:* shows cores, memory, and no OOM.
4. **Rows-per-partition bar output** — *why:* visualising balance vs skew.

### Simulations
1. **Driver OOM on collect()** — *Setup:* notebook `sim_collect_oom` collects the full sample. *Expected behaviour:* driver memory climbs then the job dies. *Learning objective:* the driver coordinates, it does not hold the data.
2. **Single-giant-file read** — *Setup:* `sim_one_big_file` points at an un-split 4 GB CSV. *Expected behaviour:* one partition, one core busy, 39 idle. *Learning objective:* file layout dictates parallelism.

### Interactive Activities
- **"Predict the stages" card game (10 min):** each pair receives 6 query cards and places a "shuffle here?" token where a stage boundary falls; reveal in the UI.
- **Cluster-sizing round-table (10 min):** given the 180 GB table and a target 20-minute window, groups propose cores/memory/partitions and defend the arithmetic.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_sample` | Synthetic, generated by course tooling (Saudi cities, SAR fares, realistic cancellation patterns) | Delta | 50 M rows / ~4.2 GB | Every lab; laptop scale |
| `trips` (full) | Same generator, full year | Delta | 2.1 B rows / ~180 GB | Cluster demos; realism numbers |
| `drivers` | Synthetic | Delta | 450 K rows | Joins from Module 2 onward |
| `riders` | Synthetic | Delta | 12 M rows | Joins and segmentation |
| `weather` / `cities` | Synthetic dims | Delta | small | Enrichment + broadcast-join demos |

### Demo Requirements
- **Instructor demo:** the live pandas-OOM vs Spark-aggregate contrast on the same data, under 6 minutes — the failure is the message.
- **Student demo:** one pair narrates their Spark UI DAG for the Riyadh-revenue query at end of Hour 3; class identifies the shuffle boundary.
- **Expected outputs:** reachable Spark UI, correct sample row count, correctly identified stage count.

---

# Module 2 — Spark DataFrames and Spark SQL

## Module Overview

**Purpose.** The DataFrame is the workhorse of modern Spark, and Spark SQL is the same engine wearing a different syntax. This module teaches participants to express real analytics — filtering, aggregating, joining, windowing — fluently in both the DataFrame API and Spark SQL, and to understand that both compile through the **Catalyst optimiser** into the same physical plan. The goal is productive, correct, idiomatic analytical code over the Masar lake.

**Business relevance.** Ninety percent of enterprise big-data work is not machine learning — it is aggregation and joining at scale: revenue by segment, cohort retention, funnel conversion, per-city KPIs. A data scientist who can translate a business question into an efficient Spark SQL query is immediately productive on any Saudi organisation's data platform, whether the data sits in Delta on a national cloud or in a managed lakehouse. Spark SQL is also the lingua franca that lets analysts, engineers, and BI tools share one query surface.

**Industry use cases.**
- A mobility operations team asks "which cities have completion rate below 85% during evening peak?" — a group-by-window-filter query.
- A finance team reconciles daily revenue by payment method and service type across all cities — a multi-dimensional aggregation over a partitioned table.
- A growth team computes 7-day rider retention cohorts — a self-join / window query that must run over 12 million riders without collapsing.

**Expected competencies.** Participants can select/filter/aggregate with the DataFrame API, write equivalent Spark SQL, join dimension tables, apply window functions (running totals, rankings, lag), use built-in functions over user-defined ones, and register views for SQL access — all while reasoning about which operations trigger shuffles.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Express filter/select/aggregate analytics with the DataFrame API | LO2 |
| 2.2 | Write equivalent analytics in Spark SQL and register temp views | LO2 |
| 2.3 | Explain that DataFrame and SQL share one Catalyst plan | LO2, LO5 |
| 2.4 | Join fact and dimension tables and reason about the join's shuffle | LO2, LO3 |
| 2.5 | Apply window functions for rankings, running totals, and lag/lead | LO2 |
| 2.6 | Prefer built-in functions over Python UDFs and explain why | LO2, LO5 |

## Technical Content

### 1. The DataFrame API: structured, typed, optimised

A Spark DataFrame is a distributed table with a schema. Unlike raw RDDs, DataFrames carry column types and go through Catalyst, so Spark can reorder, prune, and push down operations. The core verbs mirror SQL:

- `select`, `withColumn`, `drop` — projection
- `filter` / `where` — selection
- `groupBy(...).agg(...)` — aggregation (wide)
- `join(other, on, how)` — joins (wide)
- `orderBy` / `sort` — ordering (wide)
- `withColumn(..., F.window/rank/...)` — derived columns

Always import functions namespaced: `from pyspark.sql import functions as F`. Reference columns as `F.col("fare_sar")` or `df["fare_sar"]`; never compute on Python-side values you have pulled out of the DataFrame.

### 2. Spark SQL: the same engine, a different door

Register a DataFrame as a view and query it with ANSI SQL:

```python
trips.createOrReplaceTempView("trips")
spark.sql("""
  SELECT city, COUNT(*) AS trips, ROUND(SUM(fare_sar), 0) AS revenue_sar
  FROM trips WHERE status = 'completed'
  GROUP BY city ORDER BY revenue_sar DESC
""")
```

The critical teaching point: **`spark.sql(...)` and the DataFrame API produce the identical physical plan.** They are two front-ends to one Catalyst backend. Choose SQL for declarative analytics and BI familiarity; choose the DataFrame API for programmatic composition (building queries in a loop, parameterising, unit-testing). Mixing them freely is idiomatic — read a Delta table into a DataFrame, register a view, run SQL, get a DataFrame back.

### 3. Catalyst: how a query becomes a plan

Every query — SQL or DataFrame — flows through four Catalyst phases:

1. **Parsed logical plan** — syntax only, columns unresolved.
2. **Analysed logical plan** — columns/tables resolved against the catalog; types checked.
3. **Optimised logical plan** — rule-based rewrites: predicate pushdown, projection pruning, constant folding, filter reordering.
4. **Physical plan** — concrete operators chosen (which join algorithm, which exchange), cost-informed; then executed as RDD stages.

Participants do not need to memorise the phases, but they must know **that the two filters they wrote get pushed into the Parquet scan**, and that this is why column and predicate design matters. `df.explain(mode="extended")` prints all four plans; `explain("formatted")` prints a readable physical plan (Module 4's core skill).

### 4. Joins: fact meets dimension

Analytics joins the big `trips` fact table to small dimensions (`drivers`, `cities`, `weather`). Join mechanics:

```python
enriched = (trips.filter("status = 'completed'")
            .join(drivers.select("driver_id", "vehicle_type", "rating"),
                  on="driver_id", how="inner"))
```

A join is a **wide** transformation: by default Spark **shuffles both sides** on the join key so matching keys co-locate (a *sort-merge join*). But when one side is small (drivers = 450 K rows, a few MB), Spark can **broadcast** the small side to every executor and avoid shuffling the big side entirely — a **broadcast hash join**, often 10× faster. Catalyst does this automatically when the small side is under `spark.sql.autoBroadcastJoinThreshold` (default 10 MB), or you force it with `F.broadcast(drivers)`. Join strategy is the single highest-leverage tuning decision, developed fully in Module 4; introduce it here so joins are never naive.

Join hygiene to teach: pick `how` deliberately (`inner` drops non-matches — sometimes silently losing rows); deduplicate the dimension on the key before joining or a one-to-many blowup doubles your fact table; select only needed columns from the dimension *before* the join to shrink the shuffle.

### 5. Window functions: analytics without collapsing rows

Group-by collapses rows; **window functions** compute across a group while *keeping every row*. Essential for ranking, running totals, and period-over-period comparisons:

```python
from pyspark.sql import Window

w = Window.partitionBy("city").orderBy(F.col("day"))
daily = (completed
    .groupBy("city", F.to_date("pickup_ts").alias("day"))
    .agg(F.sum("fare_sar").alias("rev"))
    .withColumn("rev_7d", F.sum("rev").over(w.rowsBetween(-6, 0)))   # 7-day rolling
    .withColumn("prev_day_rev", F.lag("rev", 1).over(w))            # yesterday
    .withColumn("rank_in_city", F.rank().over(
        Window.partitionBy("city").orderBy(F.col("rev").desc()))))
```

Teach the cost: a window `partitionBy` triggers a shuffle to co-locate each partition's rows, plus a sort. Windows are powerful but not free — an unpartitioned window (`Window.orderBy(...)` with no `partitionBy`) forces **all data into one partition** and is a classic performance disaster on big data. Always partition windows unless the dataset is genuinely small.

### 6. Built-in functions vs UDFs; common mistakes

**Prefer built-in functions.** Spark ships hundreds of SQL functions (`F.when`, `F.regexp_extract`, `F.date_trunc`, `F.percentile_approx`, `F.coalesce`). These run inside the JVM/Tungsten engine, are Catalyst-visible, and are fast. A **Python UDF** serialises every row to a Python process and back — often 10–100× slower and opaque to the optimiser. Rule: reach for a UDF only when no built-in and no `pandas_udf` (vectorised, much faster) can express the logic.

**Common mistakes (each seeded in the Lab 2 starter):**
1. `groupBy` then forgetting only aggregated/grouping columns survive — selecting a non-grouped column errors or requires an aggregate.
2. An unpartitioned window function that funnels the whole dataset into one task.
3. A Python UDF for something `F.when(...)` does natively — silent 20× slowdown.
4. `join` without deduplicating the dimension → row explosion → wrong revenue totals.
5. `count(col)` vs `count(*)`: `count(col)` skips nulls; using it on a nullable column silently undercounts.
6. `orderBy` on the full DataFrame just to `show(20)` — sorts 50 M rows to display 20; use `orderBy(...).limit(20)` so Catalyst does a top-N, not a full sort.

**Production considerations.** Push filters as early as possible (Catalyst usually does, but explicit is clearer and helps partition pruning). Select only needed columns from Delta — columnar storage means unread columns are never scanned. Prefer `limit` + `show` for inspection. Register stable views for BI tools rather than re-deriving logic per consumer.

## Code Examples

### City performance analytics — DataFrame API

```python
# src/masar/analytics/city_report.py
"""Daily city performance: revenue, completion rate, avg fare.
Pure DataFrame API; framework-free business logic; reusable in the capstone."""
from pyspark.sql import DataFrame, functions as F


def city_performance(trips: DataFrame) -> DataFrame:
    total = trips.groupBy("city").agg(
        F.count("*").alias("requests"),
        F.sum(F.when(F.col("status") == "completed", 1).otherwise(0)).alias("completed"),
        F.sum(F.when(F.col("status") == "completed", F.col("fare_sar"))
              .otherwise(0.0)).alias("revenue_sar"),
    )
    return (total
        .withColumn("completion_rate",
                    F.round(F.col("completed") / F.col("requests"), 4))
        .withColumn("avg_fare_sar",
                    F.round(F.col("revenue_sar") /
                            F.greatest(F.col("completed"), F.lit(1)), 2))
        .orderBy(F.col("revenue_sar").desc()))
```

### The same analytics — Spark SQL (identical plan)

```python
# notebooks/02_city_report_sql.py
trips.createOrReplaceTempView("trips")

city_sql = spark.sql("""
  SELECT
    city,
    COUNT(*)                                             AS requests,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
    ROUND(SUM(CASE WHEN status = 'completed'
                   THEN fare_sar ELSE 0 END), 0)          AS revenue_sar,
    ROUND(AVG(CASE WHEN status = 'completed'
                   THEN fare_sar END), 2)                 AS avg_fare_sar,
    ROUND(SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END)
          / COUNT(*), 4)                                  AS completion_rate
  FROM trips
  GROUP BY city
  ORDER BY revenue_sar DESC
""")

# Prove equivalence: both compile to the same physical plan
city_sql.explain(mode="formatted")
```

### Enriching with a broadcast dimension join + window

```python
# src/masar/analytics/driver_leaderboard.py
from pyspark.sql import Window, functions as F

def top_drivers_per_city(trips, drivers, top_n: int = 10):
    dim = drivers.select("driver_id", "city", "vehicle_type", "rating").dropDuplicates(["driver_id"])
    completed = trips.filter("status = 'completed'").select("driver_id", "fare_sar")

    # drivers is small -> broadcast it; the 50M-row fact side is NOT shuffled
    agg = (completed.join(F.broadcast(dim), on="driver_id", how="inner")
           .groupBy("city", "driver_id", "vehicle_type")
           .agg(F.sum("fare_sar").alias("driver_revenue"),
                F.count("*").alias("driver_trips")))

    ranked = agg.withColumn(
        "rank",
        F.row_number().over(
            Window.partitionBy("city").orderBy(F.col("driver_revenue").desc())))
    return ranked.filter(F.col("rank") <= top_n).orderBy("city", "rank")
```

### Why a UDF hurts — measured

```python
# notebooks/02_udf_vs_builtin.py
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

# BAD: Python UDF — serialises every row to Python
@F.udf(returnType=StringType())
def fare_band_udf(fare):
    return "high" if fare and fare > 100 else "low"

# GOOD: native expression — stays in the JVM, Catalyst-visible
fare_band = F.when(F.col("fare_sar") > 100, "high").otherwise("low")

import time
for label, expr in [("udf", fare_band_udf("fare_sar")), ("builtin", fare_band)]:
    t0 = time.perf_counter()
    trips.withColumn("band", expr).groupBy("band").count().collect()
    print(f"{label}: {time.perf_counter() - t0:.1f}s")   # udf ~4-8x slower on sample
```

## Hands-on Lab 2 — City Revenue and Cancellation Analytics

| | |
|---|---|
| **Objective** | Build a suite of analytics over Masar `trips` in both DataFrame API and Spark SQL: city revenue, completion/cancellation rates, top drivers, and a 7-day revenue trend — proving both front-ends yield the same plan |
| **Duration** | 50 minutes |
| **Setup** | Lab 1 complete, `git checkout lab2_start`; `trips_sample`, `drivers` loaded |

**Instructions & tasks**

1. *(8 min)* Implement `city_performance()` (DataFrame API). Run it; record the top-5 cities by revenue.
2. *(8 min)* Write the equivalent Spark SQL. Diff the two result sets — they must match row-for-row.
3. *(6 min)* Run `.explain("formatted")` on both. Confirm the physical plans are identical; note the exchange (shuffle) for the group-by.
4. *(10 min)* Implement `top_drivers_per_city()` using a **broadcast** join and a `row_number` window. Verify in the UI that the big side is not shuffled (look for `BroadcastHashJoin`).
5. *(8 min)* Add a 7-day rolling revenue per city using a partitioned window; plot the top-3 cities' trend (collect only the aggregated ~280 rows).
6. *(6 min)* Replace one `F.when` with a Python UDF, measure the slowdown, then revert. Record both timings in `BENCHMARKS.md`.
7. *(4 min)* Commit: `feat(analytics): city + driver + trend analytics (DataFrame & SQL)`.

**Expected output**
```
Top cities by completed revenue (sample):
  Riyadh   41,382,905 SAR   completion 0.883
  Jeddah   28,904,110 SAR   completion 0.871
  Dammam   11,220,540 SAR   completion 0.865
  Makkah    9,870,233 SAR   completion 0.858
  Madinah   6,540,912 SAR   completion 0.861

DataFrame plan == SQL plan: TRUE (identical physical plan)
Join strategy for top_drivers: BroadcastHashJoin (drivers broadcast, trips not shuffled)
UDF fare-band: 5.9s   |  built-in fare-band: 1.2s
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Non-grouped column error in group-by | Selecting a column that is neither grouped nor aggregated | Wrap it in an aggregate or add to `groupBy` |
| Revenue totals doubled after join | Dimension not deduplicated on key | `.dropDuplicates(["driver_id"])` before join |
| Join shows `SortMergeJoin` not broadcast | Small side over threshold / not hinted | Wrap with `F.broadcast(...)` or select fewer columns |
| Window query extremely slow | `Window` without `partitionBy` funnels all rows to one task | Always `partitionBy` on a real key |

**Instructor notes.** The DataFrame-vs-SQL plan equivalence (task 3) is the "aha" that dissolves the false dichotomy students bring in. Fast finishers: express the completion-rate metric as a reusable SQL view and query it from a second notebook to preview shared BI surfaces.

## Mini Exercises

**Quiz (5 questions)**
1. Do `spark.sql(...)` and the DataFrame API produce different physical plans? → No — same Catalyst plan.
2. Which join avoids shuffling the big table, and when is it chosen? → broadcast hash join; when the other side is under the broadcast threshold.
3. Why prefer `F.when` over a Python UDF? → UDF serialises each row to Python and is opaque to Catalyst; built-ins run in the JVM.
4. What's the danger of `Window.orderBy(...)` with no `partitionBy`? → all rows funnel into one partition/task.
5. `count(col)` vs `count(*)` — when do they differ? → `count(col)` ignores nulls.

**Debugging exercise.** Give a query that under-reports revenue because a `count(fare_sar)` skips null fares on cancelled trips; have participants find and fix it.

**Refactor exercise.** Provide a query that sorts the full 50 M-row DataFrame then `show(10)`; ask participants to rewrite with `orderBy(...).limit(10)` and explain the top-N optimisation in the plan.

**Discussion questions.**
- When would your team standardise on Spark SQL views vs a DataFrame library of functions? What are the maintainability trade-offs?
- A junior writes every transformation as a UDF "because it's clearer." How do you make the performance cost visible in review?

## Case Study — The Cancellation-Rate Query That Lied

**Scenario.** A Masar product manager reports that Dammam's cancellation rate "jumped to 40%." The underlying query joined `trips` to a `driver_shifts` table to attribute cancellations to drivers — but `driver_shifts` had multiple rows per driver per day, so the inner join fanned each cancelled trip into several rows, inflating the numerator.

**Business context.** The inflated figure triggered an emergency driver-incentive spend proposal for Dammam. A skeptical analyst re-derived the rate directly from `trips` (no join) and got 14% — closer to every other city.

**Technical challenge.** Diagnose the row-explosion join, and establish a correct, defensible cancellation-rate definition computed at the right grain.

**Constraints.** Numbers must reconcile to the finance team's completed-trip counts; the fix must run in the nightly window; the definition must be documented so BI dashboards stop diverging.

**Solution approach (facilitate, don't lecture).** (1) Show the join blows up row counts — `trips` count before vs after the join. (2) Establish the grain: cancellation rate is a property of `trips`, one row per trip; do not join a one-to-many table into the denominator. (3) If shift attribution is needed, aggregate `driver_shifts` to one row per driver-day *first*, or compute the rate on `trips` alone and join summaries afterward. (4) Register the corrected metric as a view so every dashboard shares one definition.

**Discussion questions.**
1. How does an inner join to a one-to-many table silently corrupt an aggregate?
2. What quick check (one line) would have caught the row explosion? (`count` before/after join)
3. Where should the canonical metric definition live so BI tools cannot diverge? (a shared view / semantic layer)
4. Why is "compute the rate at the trip grain, then join summaries" the safe pattern?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| DataFrame vs SQL plan match | Correctness | Identical physical plan | `explain("formatted")` diff |
| Join strategy for driver enrich | Performance | `BroadcastHashJoin` (no big-side shuffle) | UI SQL tab |
| UDF vs built-in speedup | Performance | Built-in ≥ 4× faster | timed comparison |
| Revenue reconciliation | Correctness | Matches finance completed-trip totals | row/sum check |
| Window query partitioned | Correctness | No single-partition funnel | UI task distribution |

**Example benchmark table (filled during lab):**

| Query (50 M sample) | Wall time | Shuffle read | Join type |
|---|---|---|---|
| City performance (SQL) | 12.1 s | 240 MB | n/a |
| Driver leaderboard (broadcast) | 15.8 s | 41 MB | BroadcastHashJoin |
| Driver leaderboard (no broadcast) | 47.3 s | 1.9 GB | SortMergeJoin |
| 7-day rolling revenue | 18.4 s | 260 MB | n/a |

## Required Visuals and Training Assets

### Diagrams
1. **Two doors, one engine** — *Purpose:* dissolve the SQL-vs-DataFrame dichotomy. *Elements:* "Spark SQL" and "DataFrame API" boxes both flowing into one "Catalyst" funnel that emits a single physical plan. *Style:* Y-merge diagram.
2. **Catalyst four-phase pipeline** — *Purpose:* demystify optimisation. *Elements:* Parsed → Analysed → Optimised → Physical, with a callout showing a filter being pushed down into the scan. *Style:* left-to-right pipeline with one annotated rewrite.
3. **Broadcast vs sort-merge join** — *Purpose:* the join decision. *Elements:* top panel shuffles both sides; bottom panel broadcasts the small dim to every executor while the fact stays put. *Style:* two-panel comparison with data-movement arrows.
4. **Window function anatomy** — *Purpose:* windows keep rows. *Elements:* a partitioned, ordered frame with a sliding 7-row window and `lag` arrow. *Style:* table with highlighted frame.

### Images (screenshots)
1. **Formatted physical plan** for the city report — *why:* first real plan read; *content:* HashAggregate → Exchange → HashAggregate → scan.
2. **UI SQL graph showing BroadcastExchange** — *why:* recognise a broadcast join visually.
3. **Side-by-side result sets** (DataFrame vs SQL) proving equality.
4. **UDF vs built-in timing** in the notebook output.

### Simulations
1. **Row-explosion join** — *Setup:* `sim_join_blowup` joins a one-to-many `driver_shifts`. *Expected behaviour:* inflated counts. *Learning objective:* grain discipline before aggregation.
2. **Unpartitioned window** — *Setup:* `sim_window_single_partition` runs a window with no `partitionBy`. *Expected behaviour:* one task processes everything, huge spill. *Learning objective:* always partition windows.

### Interactive Activities
- **"Translate it" relay (12 min):** instructor shows a business question; pairs race to write it once in SQL and once in DataFrame API, then diff plans.
- **Join-strategy prediction (8 min):** for five joins, teams predict broadcast vs sort-merge and verify in the UI.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_sample` | Course tooling | Delta | 50 M rows | All analytics |
| `drivers` | Course tooling | Delta | 450 K rows | Broadcast-join dimension |
| `driver_shifts` | Course tooling (intentionally one-to-many) | Delta | 3 M rows | Row-explosion case study |
| `cities` | Course tooling | Delta | 40 rows | Enrichment |

### Demo Requirements
- **Instructor demo:** write the city report in SQL, then re-express in DataFrame API, and reveal the identical plan — under 7 minutes.
- **Student demo:** one pair explains their broadcast join in the UI at end of Hour 4.
- **Expected outputs:** matching result sets, `BroadcastHashJoin` confirmed, UDF slowdown quantified.

---

# Module 3 — Shuffles, Partitioning, and Caching

## Module Overview

**Purpose.** This is the module where participants stop writing merely *correct* Spark and start writing *fast* Spark. The three levers are the shuffle (understand it, minimise it), partitioning (size and lay out data so parallelism is real and skew is tamed), and caching (stop recomputing the same lineage). Everything here is applied directly to the Masar queries built on Day 1.

**Business relevance.** The gap between a naive and a tuned Spark job is routinely 5–20× in runtime and cluster cost. On a national-scale dataset, that is the difference between a nightly report finishing at 02:00 versus 09:00, and between a cluster bill of thousands versus tens of thousands of riyals per month. Shuffle and partition literacy is the core competency that distinguishes a "Spark user" from a "Spark engineer" in every Saudi data platform team.

**Industry use cases.**
- A mobility platform's daily driver-earnings job shuffles 180 GB three times because of chained joins; collapsing to one shuffle halves the cluster bill.
- A telecom aggregates a year of records by subscriber; a single skewed "corporate mega-account" key makes one task run 40× longer than the rest until it is salted.
- A repeated interactive analysis over the same filtered dataset re-scans 180 GB on every question until it is cached, turning a 3-minute wait into 3 seconds.

**Expected competencies.** Participants can identify shuffles in the plan and UI, size and set `shuffle.partitions`, choose `repartition` vs `coalesce` correctly, apply bucketing for repeated joins, cache/persist deliberately with the right storage level, and detect and mitigate partition skew.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Explain the shuffle: what moves, why, and its network/disk cost | LO1, LO3 |
| 3.2 | Size post-shuffle partitions and set `spark.sql.shuffle.partitions` sensibly | LO3 |
| 3.3 | Choose `repartition` vs `coalesce` and justify the choice | LO3 |
| 3.4 | Cache/persist with the correct storage level and know when NOT to | LO3 |
| 3.5 | Detect partition skew and mitigate it (salting, AQE) | LO3, LO5 |
| 3.6 | Apply bucketing to eliminate repeated join shuffles | LO3 |

## Technical Content

### 1. Anatomy of a shuffle

A **shuffle** is Spark redistributing data across partitions and machines so that all rows sharing a key end up together — required by every wide transformation (`groupBy`, `join`, `distinct`, `orderBy`, window `partitionBy`). Mechanically:

1. **Map side:** each task writes its output to local disk, bucketed by the target partition (hash of the key mod N).
2. **Network:** reduce-side tasks fetch their bucket from every map output across the cluster.
3. **Reduce side:** each task processes all rows for its keys.

Shuffle is the most expensive thing Spark does — it hits **disk (write + read), network, and serialisation**. The optimisation philosophy is therefore blunt: **shuffle less data, less often.** Filter and project *before* the shuffle (less data crosses the wire); avoid redundant shuffles (chained joins on the same key can share one); replace a shuffle join with a broadcast join when a side is small (Module 2/4).

Participants must be able to *see* the shuffle: in the plan it is an **`Exchange`** node; in the UI it is the boundary between two stages, with "Shuffle Read" and "Shuffle Write" columns quantifying the bytes moved.

### 2. Partition sizing and `shuffle.partitions`

After a shuffle, the number of partitions is controlled by `spark.sql.shuffle.partitions` (default **200**). This default is wrong for most workloads:

- **Sample (4 GB) with 200 partitions:** ~20 MB each — too small, scheduling overhead dominates.
- **Full (180 GB) with 200 partitions:** ~900 MB each — too big, tasks spill to disk and risk OOM.

The heuristic: target **~128–200 MB per post-shuffle partition**. For 180 GB of shuffled data that is roughly 900–1,400 partitions. Set it per workload:

```python
spark.conf.set("spark.sql.shuffle.partitions", 1024)   # full dataset
spark.conf.set("spark.sql.shuffle.partitions", 64)     # 4 GB sample
```

The modern answer is to let **Adaptive Query Execution (AQE)** coalesce partitions at runtime based on actual shuffle-output size — covered in Module 4. But participants must first understand the manual lever to understand what AQE automates.

### 3. `repartition` vs `coalesce`

Two tools change the partition count deliberately:

| | `repartition(n [, cols])` | `coalesce(n)` |
|---|---|---|
| Shuffle? | **Yes** (full shuffle) | **No** (merges adjacent partitions) |
| Can increase partitions? | Yes | No (only decrease) |
| Balances partitions? | Yes (even, or hash by cols) | No (can create uneven, large partitions) |
| Use when | Increasing parallelism; repartitioning by a key before repeated joins; fixing skew | Reducing partition count cheaply after a heavy filter, before write |

Canonical use: after `filter` drops 95% of rows you have 200 near-empty partitions — `coalesce(20)` merges them without a shuffle. Before writing one file per day-partition, `repartition("event_date")` co-locates each day's rows. **Do not `repartition` when `coalesce` suffices** — you pay a needless shuffle.

### 4. Caching and persistence

By default Spark **recomputes** a DataFrame's entire lineage every time an action touches it. If you query the same filtered/joined DataFrame repeatedly (interactive analysis, iterative ML, multi-output jobs), that is wasteful. `cache()` / `persist(level)` materialises it once:

```python
completed = trips.filter("status = 'completed'").select("city", "fare_sar", "pickup_ts")
completed.cache()               # marks it; nothing happens yet (lazy)
completed.count()               # ACTION: now it materialises and stays in memory
# subsequent queries read from cache, not from the 180 GB scan
```

**Storage levels** (via `persist`): `MEMORY_ONLY` (fast, drops partitions that don't fit — recomputed on demand), `MEMORY_AND_DISK` (default for `cache()` on DataFrames — spills to disk instead of recomputing), `DISK_ONLY`, and `_SER` variants (serialised, smaller, more CPU). Rules to teach:

- Cache only what is **reused** and **expensive to recompute** and **fits** — caching everything evicts everything.
- Always trigger with an action, and `unpersist()` when done to free memory.
- If the source is already a cheap Delta scan used once, caching is pure overhead.
- Cache the *narrowed* DataFrame (after filter/select), never the raw 180 GB table.

### 5. Partition skew — the silent job-killer

**Skew** is when one key has vastly more rows than others, so one shuffle partition is enormous while the rest are small. That one task runs for minutes while 999 finish in seconds — the stage is only as fast as its slowest task. In Masar, `city = 'Riyadh'` holds ~35% of all trips; a `groupBy("city")` or a join on a skewed key produces one giant partition.

Detection: in the UI stage view, the max task duration and shuffle-read bytes are many times the median. Mitigations:

- **AQE skew join handling** (`spark.sql.adaptive.skewJoin.enabled=true`) — Spark splits the oversized partition automatically. First line of defence (Module 4).
- **Salting** — append a random bucket to the hot key so it spreads across partitions, then aggregate twice:

```python
from pyspark.sql import functions as F
SALT = 16
salted = trips.withColumn("salt", (F.rand() * SALT).cast("int"))
stage1 = salted.groupBy("city", "salt").agg(F.sum("fare_sar").alias("rev"))
result = stage1.groupBy("city").agg(F.sum("rev").alias("rev"))   # de-salt
```

- **Broadcast** the other side (skew in a join often vanishes if the join becomes broadcast — no shuffle at all).

### 6. Bucketing and common mistakes

**Bucketing** pre-shuffles a table on a key at write time into a fixed number of buckets, stored in the table metadata. Two bucketed tables joined on the bucketing key skip the shuffle entirely on every future join — you pay the shuffle once at write, save it forever at read. Ideal for a dimension repeatedly joined to facts. (Delta/lakehouse note: bucketing support varies by engine; teach it as a concept and show Spark's `bucketBy` on managed tables, while flagging that Z-ordering/liquid clustering is the Delta-native analogue.)

**Common mistakes (seeded in Lab 3):**
1. Caching the raw table "to be safe" — evicts useful data, adds no value.
2. `repartition(1)` to write a single file — funnels all data through one task; use `coalesce` or accept multiple files.
3. Leaving `shuffle.partitions=200` on a 180 GB job — 900 MB partitions, spill, OOM.
4. Ignoring skew — blaming "Spark is slow" when one task is the whole problem.
5. Caching without an action, then wondering why it's not cached.
6. Never calling `unpersist()` — memory leaks across a long notebook session.

**Production considerations.** Measure shuffle bytes before and after every change — it is the truest proxy for cost. Prefer AQE on by default; reach for manual salting only when AQE's skew handling is insufficient. Lay out written data (partition by low-cardinality date, Z-order/cluster by high-selectivity filter columns) so the *next* job reads less.

## Code Examples

### Seeing and shrinking a shuffle

```python
# notebooks/03_shuffle_diet.py
from pyspark.sql import functions as F

# BEFORE: join first, filter later -> shuffles the whole fact table
bad = (trips.join(drivers, "driver_id")
            .filter("status = 'completed'")
            .groupBy("city").agg(F.sum("fare_sar").alias("rev")))
bad.explain(mode="formatted")     # note the large Exchange feeding the join

# AFTER: filter + project BEFORE the join -> far less data shuffled
slim_trips = (trips.filter("status = 'completed'")
                   .select("driver_id", "city", "fare_sar"))
good = (slim_trips.join(F.broadcast(drivers.select("driver_id")), "driver_id")
                  .groupBy("city").agg(F.sum("fare_sar").alias("rev")))
good.explain(mode="formatted")    # broadcast join, tiny exchange
```

### Right-sizing partitions and coalescing after a filter

```python
# notebooks/03_partition_sizing.py
spark.conf.set("spark.sql.shuffle.partitions", 64)      # match the 4 GB sample

completed = trips.filter("status = 'completed'")         # ~88% survive on sample
print("after filter:", completed.rdd.getNumPartitions()) # still 34 (narrow op)

# We are about to WRITE per-day files; coalesce to avoid tiny-file spray.
# coalesce = no shuffle, cheap. repartition("event_date") = shuffle, balanced.
to_write = completed.coalesce(16)
print("after coalesce:", to_write.rdd.getNumPartitions()) # 16
```

### Cache the narrowed DataFrame for repeated interactive queries

```python
# notebooks/03_cache.py
from pyspark import StorageLevel

hot = (trips.filter("status = 'completed'")
            .select("city", "service_type", "fare_sar", "pickup_ts")
            .persist(StorageLevel.MEMORY_AND_DISK))     # spill instead of recompute
hot.count()                                             # materialise once

# These three now read from cache, not the 180 GB Delta scan:
hot.groupBy("city").sum("fare_sar").show()
hot.groupBy("service_type").count().show()
hot.groupBy("city").agg({"fare_sar": "avg"}).show()

hot.unpersist()                                         # free it when done
```

### Salting a skewed aggregation

```python
# src/masar/tuning/salt.py
from pyspark.sql import DataFrame, functions as F

def salted_city_revenue(trips: DataFrame, salt_buckets: int = 16) -> DataFrame:
    """Riyadh holds ~35% of rows -> one giant partition. Salt to spread it."""
    salted = trips.filter("status = 'completed'") \
                  .withColumn("_salt", (F.rand() * salt_buckets).cast("int"))
    partial = salted.groupBy("city", "_salt").agg(F.sum("fare_sar").alias("rev"))
    return partial.groupBy("city").agg(F.sum("rev").alias("revenue_sar"))
```

## Hands-on Lab 3 — Diagnose and Fix a Shuffle-Heavy Job

| | |
|---|---|
| **Objective** | Take a deliberately slow Masar earnings job, locate its shuffles in the UI, and re-engineer it with filter-pushdown, a broadcast join, right-sized partitions, caching, and salting — measuring shuffle bytes and runtime at each step |
| **Duration** | 50 minutes |
| **Setup** | Labs 1–2 complete, `git checkout lab3_start` (contains `slow_earnings.py`) |

**Instructions & tasks**

1. *(6 min)* Run `slow_earnings.py` as-is. Record wall time, total shuffle read/write, and max-task duration from the UI. This is the baseline.
2. *(8 min)* In the plan, identify every `Exchange`. Which shuffle moves the most bytes? Note the join strategy.
3. *(8 min)* Push the `status='completed'` filter and column selection *before* the join. Re-measure shuffle bytes.
4. *(8 min)* Convert the driver join to a broadcast join. Confirm `BroadcastHashJoin` and the collapse in shuffle read.
5. *(6 min)* Set `shuffle.partitions` to a size-appropriate value for the sample; observe task count and per-task size.
6. *(8 min)* Cache the narrowed DataFrame; run the three downstream aggregations; compare to the uncached run.
7. *(4 min)* Detect Riyadh skew in the UI (max vs median task); apply `salted_city_revenue`; confirm task balance.
8. *(2 min)* Commit `perf(earnings): pushdown + broadcast + cache + salt` and paste the before/after table into `BENCHMARKS.md`.

**Expected output**
```
Baseline:  188 s | shuffle R/W 3.9 GB / 3.9 GB | max task 41 s (skew) | SortMergeJoin
+ pushdown/project:     121 s | shuffle 1.6 GB
+ broadcast join:        44 s | shuffle 190 MB | BroadcastHashJoin
+ shuffle.partitions=64:  38 s | 64 balanced tasks
+ cache (3 queries):     downstream 3.1 s total (was 96 s)
+ salt Riyadh:           max task 4.2 s (was 41 s); balanced
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Shuffle read unchanged after "broadcast" | Small side still over threshold | `F.broadcast(...)` explicitly; select fewer cols |
| Cache seems ignored (still scanning) | No action triggered / cached raw table | `.count()` after `.persist()`; cache the narrowed DF |
| One task still 40 s after salt | Salt applied after the skewing join, not before agg | Salt the key before the group-by; de-salt in a second stage |
| Job slower after `repartition(1)` | Funnelled all rows through one task | Use `coalesce`, or accept N output files |

**Instructor notes.** Have pairs keep the UI open on the Stages tab the whole lab — watching max-task-duration drop from 41 s to 4 s after salting is the most persuasive moment of Day 2. Fast finishers: try AQE skew handling (toggle the config) and compare against manual salting as a preview of Module 4.

## Mini Exercises

**Quiz (5 questions)**
1. Which operations force a shuffle? → `groupBy`, `join`, `distinct`, `orderBy`, windowed `partitionBy`.
2. `repartition` vs `coalesce` — which shuffles, which can only decrease partitions? → repartition shuffles; coalesce only decreases, no shuffle.
3. Default `spark.sql.shuffle.partitions`, and why is it often wrong? → 200; wrong because it ignores actual data size.
4. When is caching pure overhead? → when the DataFrame is used once or its recompute is a cheap scan.
5. Symptom of skew in the UI? → max task duration/shuffle-read far exceeds the median.

**Debugging exercise.** Give a job that caches the raw `trips` table then filters — ask why memory pressure is high and the cache barely helps (caching before narrowing).

**Measurement exercise.** Provide the same aggregation at `shuffle.partitions` = 8, 64, 512; have participants chart per-task size and runtime, and identify the sweet spot for the sample.

**Discussion questions.**
- Your teammate `repartition(1)`s every output "to get one clean file." What is the cost, and what would you do instead?
- Salting fixes skew but complicates the query. When do you prefer AQE's automatic handling, and when is manual salting worth it?

## Case Study — The Riyadh Skew That Blew the Nightly SLA

**Scenario.** Masar's nightly driver-earnings settlement job runs a `groupBy("city", "driver_id")` over the full year-to-date trips. It started missing its 20-minute SLA. The Spark UI showed 1,023 of 1,024 tasks finishing in under 15 seconds and one task running for 11 minutes — the Riyadh partition.

**Business context.** The job feeds driver payouts; a late run delays settlements and generates support tickets. The team's first instinct — "add more executors" — did nothing, because the bottleneck was a *single* task that more cores cannot subdivide.

**Technical challenge.** Break the one giant Riyadh partition into many so the work parallelises, without changing the settlement totals.

**Constraints.** Payout totals must be identical to the cent; the fix must survive the daily volume swings (Riyadh's share drifts 30–40%); the job runs on a shared cluster with a fixed executor budget.

**Solution approach (facilitate, don't lecture).** (1) Confirm the diagnosis: max vs median task duration in the UI. (2) Enable AQE skew-join handling and re-measure — often enough on its own. (3) Where the aggregation (not a join) is skewed, apply two-stage salting on `driver_id`/`city`. (4) Verify totals reconcile exactly against the un-salted result on a sample. (5) Add a monitoring check that flags when any task exceeds 5× the median next time.

**Discussion questions.**
1. Why did adding executors not help a single-task bottleneck?
2. How does salting turn one 11-minute task into many short ones — and why does the two-stage aggregation stay correct?
3. When would AQE skew handling suffice and salting be unnecessary complexity?
4. What proactive signal would have caught the drift before the SLA breach?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Shuffle bytes on earnings job | Performance | ≥ 90% reduction vs baseline | UI shuffle read/write |
| Max/median task ratio (post-fix) | Performance | < 2× | UI stage task summary |
| Post-shuffle partition size | Performance | 128–200 MB | shuffle bytes ÷ partitions |
| Cached-query speedup | Performance | ≥ 10× on repeated queries | timed before/after |
| Settlement total unchanged | Correctness | Exact match to baseline | sum reconciliation |

**Example benchmark table (filled during lab):**

| Version | Wall time | Shuffle R/W | Max task | Join |
|---|---|---|---|---|
| baseline | 188 s | 3.9 / 3.9 GB | 41 s | SortMerge |
| + pushdown | 121 s | 1.6 / 1.6 GB | 39 s | SortMerge |
| + broadcast | 44 s | 190 / 190 MB | 12 s | Broadcast |
| + right-sized + cache | 38 s | 190 MB | 9 s | Broadcast |
| + salt | 31 s | 210 MB | 4.2 s | Broadcast |

## Required Visuals and Training Assets

### Diagrams
1. **The shuffle, step by step** — *Purpose:* demystify the most expensive operation. *Elements:* map-side bucketed writes → network fetch → reduce-side merge, with disk and network icons and a byte counter. *Style:* three-stage flow.
2. **repartition vs coalesce** — *Purpose:* the decision. *Elements:* repartition full-shuffle balancing vs coalesce merging adjacent partitions with no network. *Style:* two-panel.
3. **Skew before/after salting** — *Purpose:* the headline fix. *Elements:* one giant Riyadh partition vs sixteen balanced salted partitions; a matching UI task-duration bar chart. *Style:* before/after with task bars.
4. **Cache decision tree** — *Purpose:* stop over-caching. *Elements:* "reused? expensive? fits?" gates ending in cache / don't cache / narrow-first. *Style:* flowchart.

### Images (screenshots)
1. **UI Stages tab with a skewed task** — one 41 s bar among sub-second bars.
2. **Exchange node in the physical plan** — labelled with shuffle bytes.
3. **Storage tab showing a cached, materialised DataFrame** with fraction cached.
4. **Before/after shuffle-bytes comparison** in the UI SQL tab.

### Simulations
1. **200-partitions-on-180 GB spill** — *Setup:* `sim_bad_shuffle_parts`. *Expected:* task spill-to-disk, near-OOM. *Objective:* size partitions to data.
2. **Cache-the-wrong-thing** — *Setup:* `sim_cache_raw` caches the full table. *Expected:* eviction thrash, no speedup. *Objective:* cache the narrowed, reused DataFrame.

### Interactive Activities
- **Shuffle-bytes bingo (10 min):** teams predict which of five queries moves the most shuffle bytes, then rank by the UI.
- **Skew hunt (10 min):** pairs race to find the skewed key in a mystery aggregation using only the Stages tab.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_sample` | Course tooling (Riyadh deliberately ~35% of rows) | Delta | 50 M rows | Skew + shuffle labs |
| `drivers` | Course tooling | Delta | 450 K rows | Broadcast vs sort-merge |
| `slow_earnings.py` | Course tooling (anti-tuned) | code | — | Lab 3 starting point |

### Demo Requirements
- **Instructor demo:** live-drop shuffle bytes on the earnings job from 3.9 GB to 190 MB via pushdown + broadcast, under 8 minutes.
- **Student demo:** one pair shows their skew fix and reconciles the settlement total.
- **Expected outputs:** ≥90% shuffle reduction, balanced tasks, identical totals.

---

# Module 4 — Performance Tuning and Query Plans

## Module Overview

**Purpose.** Module 3 taught the *levers* of performance — shuffle, partitioning, caching. This module teaches participants to *read the machine* so they know which lever to pull and can prove the pull worked. The core skill is reading a Spark **physical plan** from `explain()` and the Spark UI SQL graph: recognising the operators, spotting the expensive exchange, identifying the chosen join algorithm, and seeing where a filter did or did not get pushed into the scan. On top of plan literacy sits the modern tuning toolkit: **Adaptive Query Execution (AQE)**, join-strategy control, skew handling, partition pruning, and spill diagnosis. By the end, tuning stops being folklore ("try more executors") and becomes evidence-driven engineering ("the plan shows a sort-merge join and a 3.9 GB exchange; broadcast the dimension and the exchange disappears").

**Business relevance.** On a national-scale platform, an untuned job is not just slow — it is a recurring, compounding cost. A Masar analytics job that runs nightly, missing its window by two hours and burning an oversized cluster, costs real riyals every single night and blocks the 07:00 operations standup. The engineer who can open a query plan, name the bottleneck in thirty seconds, and defend a fix with before/after runtimes and shuffle bytes is the person Saudi data platform teams pay for. Plan-reading is also the language of production incident reviews: when a job that used to take 20 minutes suddenly takes three hours, the physical plan (and how it changed) is the primary evidence.

**Industry use cases.**
- A mobility analytics job regressed from 20 minutes to 3 hours after a data-volume shift flipped a broadcast join to a sort-merge join; reading the plan reveals the join strategy change in one line.
- A telecom's monthly aggregation spills 400 GB to disk because AQE was disabled and partitions were 900 MB; the Spark UI's spill metric plus the plan point straight at the fix.
- A bank's regulatory report scans an entire year of Delta files because a date predicate was written on a derived column and lost partition pruning; the plan's "PartitionFilters" line exposes the miss.

**Expected competencies.** After this module a participant can read `explain(mode="formatted")` and the UI SQL graph fluently, identify the join algorithm and the largest exchange, enable and interpret AQE (coalesced partitions, skew-join splits, broadcast promotion), force or prevent a broadcast join deliberately, confirm partition pruning and predicate pushdown in the plan, and diagnose spill from the UI.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Read `explain()` output and the UI SQL graph; name every major operator | LO5 |
| 4.2 | Explain Catalyst (rule/cost optimisation) and Tungsten (codegen, memory) roles | LO5 |
| 4.3 | Enable and interpret AQE: coalescing, skew-join splitting, broadcast promotion | LO3, LO5 |
| 4.4 | Choose and force join strategies (broadcast vs sort-merge vs shuffle-hash) | LO3, LO5 |
| 4.5 | Diagnose skew and spill from the plan and the UI and remediate them | LO3, LO5 |
| 4.6 | Confirm partition pruning and predicate/column pushdown in the physical plan | LO3, LO5, LO6 |

## Technical Content

### 1. Reading a physical plan

`df.explain(mode="formatted")` prints the **physical plan** — the tree of operators Spark will actually run, read bottom-up (leaves = scans, root = final action). The operators participants must recognise:

- **`FileScan parquet` / `Scan delta`** — the read. Carries `PushedFilters`, `PartitionFilters`, and `ReadSchema` — the three lines that tell you whether pushdown and pruning happened.
- **`Filter`** — a row filter *not* pushed into the scan (the residual after pushdown).
- **`Project`** — column selection.
- **`Exchange`** — a shuffle. `hashpartitioning(...)` = repartition by key; the single most important thing to count and size.
- **`HashAggregate`** — partial (pre-shuffle) and final (post-shuffle) aggregation; they bracket an `Exchange`.
- **`BroadcastHashJoin` / `SortMergeJoin` / `ShuffledHashJoin`** — the join algorithm. Naming it is the first move in any join-tuning task.
- **`BroadcastExchange`** — the small side being shipped to every executor.
- **`AQEShuffleRead`**, `coalesced` / `skewed=true` — AQE's runtime rewrites, visible after the query runs.

The reading drill: *find the scans, count the exchanges, name the join, check for pushed filters.* Four questions, thirty seconds, and 80% of tuning decisions are made.

### 2. Catalyst and Tungsten — the two engines under the plan

Two subsystems produce and execute the plan:

- **Catalyst** is the query optimiser (Module 2 introduced its four phases). It applies **rule-based** rewrites (predicate pushdown, projection pruning, constant folding, join reordering) and, for joins, **cost-based** optimisation (CBO) using table statistics to pick join order and strategy. Catalyst decides *what* to run.
- **Tungsten** is the execution engine. It gives Spark **whole-stage code generation** (fusing a chain of operators into one compiled Java function, eliminating virtual calls), **cache-friendly binary memory layout** (off-heap, columnar), and vectorised readers. Tungsten decides *how fast* it runs on each core.

Participants don't tune Tungsten directly, but they must recognise its fingerprint in the plan: operators wrapped in `WholeStageCodegen (n)` are fused and fast; an operator *outside* codegen (often a Python UDF or an unsupported expression) is a performance smell because it breaks the fused pipeline.

### 3. Adaptive Query Execution (AQE)

AQE (on by default in Spark 3.2+, and set in `build_session`) re-optimises the plan **at runtime** using actual shuffle statistics — fixing the three problems static planning cannot:

1. **Coalesce shuffle partitions** (`spark.sql.adaptive.coalescePartitions.enabled`): after a shuffle, AQE merges tiny partitions up toward a target size (`advisoryPartitionSizeInBytes`, ~64–128 MB). This makes the `shuffle.partitions=200` default mostly irrelevant — AQE right-sizes down automatically.
2. **Skew-join handling** (`spark.sql.adaptive.skewJoin.enabled`): AQE detects a partition far larger than the median and **splits** it into sub-partitions, parallelising the hot key (the automatic version of Module 3's salting).
3. **Dynamic broadcast promotion**: if a shuffle side turns out smaller than the broadcast threshold at runtime, AQE converts a planned sort-merge join into a broadcast join.

Teaching point: AQE rewrites are only visible in the plan **after execution** (the initial plan differs from the final). Show both: `explain()` before running, then the SQL-tab graph after, which is annotated with `AQEShuffleRead coalesced` / `skewed=true`.

### 4. Join strategies and how to control them

Spark picks among four join algorithms; knowing why lets you override wrongly:

| Strategy | When Spark picks it | Cost profile |
|---|---|---|
| **Broadcast hash join** | One side < `autoBroadcastJoinThreshold` (default 10 MB) | Cheapest — no big-side shuffle; ships small side to all executors |
| **Sort-merge join** | Both sides large, join key sortable | Shuffles + sorts both sides; the default for big-big joins |
| **Shuffle hash join** | One side smallish, no sort needed, hint given | Shuffles both, builds a hash table; niche |
| **Broadcast nested loop** | Non-equi joins / tiny inputs | Last resort; O(n·m) |

Control it explicitly: `F.broadcast(dim)` forces broadcast; `spark.sql.autoBroadcastJoinThreshold` raises/lowers the automatic cutoff (set `-1` to disable and force sort-merge for testing); SQL hints `/*+ BROADCAST(d) */`, `/*+ MERGE(...) */`, `/*+ SHUFFLE_HASH(...) */`. The Masar rule of thumb: every dimension (`drivers`, `riders`, `cities`, `weather`) is small enough to broadcast; the fact table is never broadcast. A regression to sort-merge on a dimension join is almost always a threshold or statistics problem.

### 5. Partition pruning, predicate/column pushdown, and spill

Three read-time optimisations save more than any shuffle tuning because *the cheapest data is the data you never read*:

- **Partition pruning:** the Masar lake is partitioned by `event_date`. A predicate `event_date = '2025-06-01'` lets Spark skip every other day's files — visible in the plan as `PartitionFilters: [event_date = ...]`. It is lost the moment you filter on a *derived* column (`to_date(pickup_ts)` instead of `event_date`), forcing a full-table scan.
- **Predicate pushdown:** row filters on non-partition columns (`fare_sar > 100`) are pushed into the Parquet reader using file statistics/row-group min-max — shown as `PushedFilters: [GreaterThan(fare_sar,100)]`.
- **Column pushdown (projection pruning):** `select("city","fare_sar")` means Delta never reads the other 12 columns — `ReadSchema` in the plan lists only what is read.

**Spill** is the other side of tuning: when a task's data exceeds executor memory, Spark writes to disk mid-operation. The UI shows "Spill (memory)" and "Spill (disk)" per task. Spill on a shuffle usually means partitions are too large (raise partition count / let AQE coalesce differently) or a join built too big a hash table (switch strategy). Spill is not fatal, but heavy spill is the difference between minutes and hours.

### 6. A tuning methodology and common mistakes

Teach tuning as a loop, not a bag of tricks:

1. **Measure the baseline** — wall time, shuffle R/W, max-task duration, spill, from the UI.
2. **Read the plan** — scans, exchanges, join strategy, pushed filters.
3. **Form one hypothesis** — the single most expensive operator.
4. **Change one thing** — broadcast, prune, repartition, config.
5. **Re-measure and compare** — keep the change only if the numbers move.
6. **Record it** in `BENCHMARKS.md`.

**Common mistakes (seeded in Lab 4):**
1. Tuning by config-roulette (twiddling ten settings at once) so no change is attributable.
2. Filtering on a derived date column and silently losing partition pruning.
3. Raising `autoBroadcastJoinThreshold` so high a "small" side OOMs the driver during broadcast collection.
4. Disabling AQE because "the plan looks different after running" — that is AQE working, not a bug.
5. Reading only wall-clock time and ignoring shuffle bytes/spill — the metrics that predict cost at full scale.
6. Optimising a query that runs once; tune the jobs that run nightly.

**Production considerations.** Keep statistics fresh (`ANALYZE TABLE ... COMPUTE STATISTICS`) so CBO and broadcast decisions are correct. Pin the tuning-relevant configs in the job, not in a notebook cell, so production matches what you tested. Treat a plan diff in code review as a first-class signal: a PR that flips a join strategy deserves a benchmark.

## Code Examples

### Reading and comparing plans

```python
# notebooks/04_read_the_plan.py
from pyspark.sql import functions as F
from masar.session import build_session, TRIPS_SAMPLE, DRIVERS_PATH

spark = build_session("plan-reading")
trips   = spark.read.format("delta").load(TRIPS_SAMPLE)
drivers = spark.read.format("delta").load(DRIVERS_PATH)

q = (trips.filter("status = 'completed' AND event_date = '2025-06-01'")
          .select("driver_id", "city", "fare_sar")
          .join(drivers.select("driver_id", "vehicle_type"), "driver_id")
          .groupBy("city", "vehicle_type")
          .agg(F.sum("fare_sar").alias("revenue_sar")))

# Read this bottom-up: Scan (with PartitionFilters + PushedFilters) -> Project
#  -> BroadcastExchange(drivers) -> BroadcastHashJoin -> HashAggregate
#  -> Exchange -> HashAggregate
q.explain(mode="formatted")

# After running, the Spark UI SQL tab shows AQE annotations the static plan cannot:
q.write.format("noop").mode("overwrite").save()   # cheap way to force execution
```

### Forcing, disabling, and observing join strategies

```python
# notebooks/04_join_strategies.py
# 1) Let Catalyst decide (drivers is small -> broadcast)
auto = trips.join(drivers, "driver_id")
auto.explain()                      # expect BroadcastHashJoin

# 2) Force sort-merge to SEE the cost of the naive strategy
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)   # disable broadcast
smj = trips.join(drivers, "driver_id")
smj.explain()                       # now SortMergeJoin + two big Exchanges
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 10 * 1024 * 1024)  # restore

# 3) Force broadcast explicitly (survives threshold/statistics drift)
forced = trips.join(F.broadcast(drivers), "driver_id")
forced.explain()                    # BroadcastHashJoin, guaranteed
```

### Proving partition pruning is (and isn't) happening

```python
# notebooks/04_pruning.py
# GOOD: filter on the PARTITION column -> only that day's files are read
good = trips.filter("event_date = '2025-06-01'").select("fare_sar")
good.explain(mode="formatted")
#   Look for:  PartitionFilters: [isnotnull(event_date), (event_date = 2025-06-01)]

# BAD: filter on a DERIVED column -> pruning lost, full-table scan
from pyspark.sql import functions as F
bad = trips.filter(F.to_date("pickup_ts") == F.lit("2025-06-01")).select("fare_sar")
bad.explain(mode="formatted")
#   PartitionFilters is EMPTY; the whole table is scanned then filtered.
```

### AQE in action — coalescing and skew handling

```python
# notebooks/04_aqe.py
# AQE is already on (build_session). Make its effect measurable.
spark.conf.set("spark.sql.adaptive.enabled", True)
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", True)
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", True)
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128m")
spark.conf.set("spark.sql.shuffle.partitions", 512)   # deliberately too many

city_rev = (trips.filter("status = 'completed'")
                 .groupBy("city").agg(F.sum("fare_sar").alias("rev")))
city_rev.collect()
# In the SQL tab: the 512 post-shuffle partitions are 'AQEShuffleRead coalesced'
# down to a handful of ~128 MB partitions; Riyadh's skewed partition shows
# 'skewed=true' and is split. Compare against AQE off:
spark.conf.set("spark.sql.adaptive.enabled", False)
city_rev.collect()   # now 512 tiny partitions + one giant Riyadh task
spark.conf.set("spark.sql.adaptive.enabled", True)
```

## Hands-on Lab 4 — Read the Plan, Kill the Bottleneck

| | |
|---|---|
| **Objective** | Take a regressed Masar analytics query, read its physical plan, identify the bottleneck (a lost broadcast + a lost prune), fix it, and prove the win with before/after plans, runtimes, and shuffle bytes |
| **Duration** | 50 minutes |
| **Setup** | Labs 1–3 complete, `git checkout lab4_start` (contains `regressed_report.py`); `trips_sample`, `drivers`, `weather` loaded; Spark UI open |

**Instructions & tasks**

1. *(6 min)* Run `regressed_report.py`. Record baseline wall time, shuffle R/W, spill, and max-task duration from the UI.
2. *(8 min)* Call `.explain(mode="formatted")`. Find the scans, count the exchanges, name the join strategy, and read the `PartitionFilters`/`PushedFilters` lines. Write a one-line diagnosis.
3. *(8 min)* Fix the lost partition prune: the query filters on `to_date(pickup_ts)`; rewrite it against `event_date`. Confirm `PartitionFilters` now populated and files-read drops in the UI.
4. *(8 min)* Fix the join: the dimension regressed to `SortMergeJoin`. Force `F.broadcast(...)`; confirm `BroadcastHashJoin` and the collapse of the two big exchanges.
5. *(8 min)* Toggle AQE off then on around the group-by; screenshot the `AQEShuffleRead coalesced` and `skewed=true` annotations. Explain in one sentence what AQE did.
6. *(6 min)* Diagnose any remaining spill; adjust `advisoryPartitionSizeInBytes` / partition count until spill is gone.
7. *(6 min)* Paste the before/after table into `BENCHMARKS.md` and commit `perf(report): restore prune+broadcast, tune AQE`.

**Expected output**
```
Baseline:      214 s | shuffle 3.9/3.9 GB | spill 620 MB | max task 44 s | SortMergeJoin | full scan (34 files)
+ event_date prune:     96 s | files read 2/34 | shuffle 3.9 GB
+ broadcast dimension:  31 s | shuffle 210 MB | BroadcastHashJoin
+ AQE coalesce+skew:    22 s | 6 coalesced partitions | Riyadh split | spill 0
Plan diff: SortMergeJoin -> BroadcastHashJoin; PartitionFilters empty -> [event_date=...]
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `PartitionFilters` still empty | Filtering a derived/UDF column, not `event_date` | Filter the literal partition column directly |
| Join stays `SortMergeJoin` after broadcast | Threshold set to `-1` from an earlier cell / dim too wide | Restore threshold; `F.broadcast(...)`; select fewer dim columns |
| Plan "changes after running" | AQE re-optimised at runtime | Expected — read the post-execution SQL graph, not the static plan |
| Heavy disk spill persists | Post-shuffle partitions too large | Lower `advisoryPartitionSizeInBytes` or raise partition count |
| Broadcast job OOMs the driver | "Small" side larger than driver memory | Don't broadcast it; prune columns or use sort-merge |

**Instructor notes.** The single most valuable moment is task 2: make every pair read the plan *out loud* to their partner before touching code. Fast finishers: raise `autoBroadcastJoinThreshold` and find the exact size at which Catalyst flips the dimension from broadcast to sort-merge, then explain why relying on that cutoff is fragile.

## Mini Exercises

**Quiz (5 questions)**
1. In a formatted plan, which node is a shuffle, and what does `hashpartitioning` mean? → `Exchange`; repartition rows by hash of the key.
2. How can you tell partition pruning happened? → non-empty `PartitionFilters` on the scan.
3. Name the three things AQE fixes at runtime. → coalesce small partitions, split skewed join partitions, promote to broadcast.
4. Which config disables automatic broadcast, and why would you set it temporarily? → `autoBroadcastJoinThreshold = -1`; to observe the sort-merge cost.
5. What does `WholeStageCodegen` around operators indicate? → Tungsten fused them into one compiled function (fast path).

**Plan-reading exercise.** Give participants three `explain()` outputs and ask them to name, for each, the join strategy, the number of exchanges, and whether the date filter was pushed to partitions.

**Regression hunt.** Provide two plans of the "same" query a week apart — one broadcast, one sort-merge — and have pairs identify the single line that changed and hypothesise why (statistics/threshold/volume).

**Discussion questions.**
- Your job's wall time is unchanged but shuffle bytes tripled after a code change. Why might wall time lie, and what breaks first at full scale?
- AQE automates coalescing and skew handling. What is left for the engineer to do, and where can AQE still make the wrong call?

## Case Study — The Report That Regressed From 20 Minutes to 3 Hours

**Scenario.** Masar's "weekly city-vehicle revenue" report ran in 20 minutes for months, then one Monday took over three hours. No code had changed. The on-call engineer's first instinct — add executors — made no difference. The Spark UI showed two enormous exchanges and a `SortMergeJoin` where there had always been a `BroadcastHashJoin`.

**Business context.** The report feeds a Monday leadership review. A three-hour run means the numbers arrive after the meeting. Because "nothing changed," the team initially suspected the cluster, wasting a morning on infrastructure before anyone opened the query plan.

**Technical challenge.** Explain why an unchanged query changed its physical plan, and restore the fast plan defensibly so the regression cannot silently recur.

**Constraints.** The report definition (SQL) must not change; the fix must survive weekly data-volume growth; the run must return to under 25 minutes on the shared cluster.

**Solution approach (facilitate, don't lecture).** (1) Diff the old and new plans — the join strategy flipped. (2) Diagnose the cause: the `drivers` dimension had grown just past `autoBroadcastJoinThreshold` (or its statistics went stale), so Catalyst stopped auto-broadcasting. (3) Make the broadcast explicit with `F.broadcast(drivers)` so it no longer depends on a size cutoff. (4) Refresh table statistics so CBO decisions are correct going forward. (5) Add a plan-assertion test to CI that fails if the report's join is not a `BroadcastHashJoin`.

**Discussion questions.**
1. How can a query with unchanged code change its physical plan?
2. Why did adding executors not help a plan-strategy regression?
3. When is an explicit `F.broadcast` hint better than trusting the automatic threshold — and what is the risk of hinting?
4. What lightweight CI check would have caught the flip before Monday?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Correct join strategy named from plan | Understanding | Learner names it in < 30 s | plan-reading drill |
| Partition pruning restored | Performance | Files read = matching partitions only | UI SQL "number of files read" |
| Shuffle bytes after tuning | Performance | ≥ 90% reduction vs regressed baseline | UI shuffle read/write |
| Spill after tuning | Performance | 0 disk spill on the report | UI task spill columns |
| AQE effect identified | Understanding | Learner explains coalesce + skew split | UI SQL AQE annotations |

**Example benchmark table (filled during lab):**

| Version | Wall time | Shuffle R/W | Spill | Join | Files read |
|---|---|---|---|---|---|
| regressed baseline | 214 s | 3.9 / 3.9 GB | 620 MB | SortMerge | 34 / 34 |
| + event_date prune | 96 s | 3.9 / 3.9 GB | 480 MB | SortMerge | 2 / 34 |
| + broadcast dim | 31 s | 210 / 210 MB | 90 MB | Broadcast | 2 / 34 |
| + AQE tuned | 22 s | 210 MB | 0 | Broadcast | 2 / 34 |

## Required Visuals and Training Assets

### Diagrams
1. **Anatomy of a physical plan** — *Purpose:* teach plan-reading vocabulary. *Elements:* an annotated `explain(formatted)` tree read bottom-up, with callouts on `Scan`(PartitionFilters/PushedFilters), `Exchange`, `BroadcastHashJoin`, partial/final `HashAggregate`. *Style:* annotated code with leader lines.
2. **Catalyst + Tungsten split** — *Purpose:* separate "what" from "how fast". *Elements:* Catalyst (rules + CBO → plan) feeding Tungsten (codegen + binary memory → execution). *Style:* two-box pipeline.
3. **AQE before/after** — *Purpose:* make runtime re-optimisation concrete. *Elements:* static plan (200 partitions, sort-merge) vs post-run plan (coalesced partitions, skew split, promoted broadcast). *Style:* left/right plan comparison.
4. **Join-strategy decision tree** — *Purpose:* choose deliberately. *Elements:* "is a side < threshold?" → broadcast; else sort-merge; hint overrides. *Style:* flowchart with the Masar rule (dims broadcast, fact never).

### Images (screenshots)
1. **UI SQL graph with a BroadcastExchange** — recognise broadcast visually.
2. **Scan node showing PartitionFilters populated** vs empty — the pruning tell.
3. **AQEShuffleRead "coalesced" / "skewed=true"** annotations after a run.
4. **Task table with disk-spill columns** highlighted before and after tuning.

### Simulations
1. **Lost-prune scan** — *Setup:* `sim_derived_date` filters on `to_date(pickup_ts)`. *Expected:* full-table scan, all files read. *Objective:* prune on the partition column.
2. **Threshold flip** — *Setup:* `sim_broadcast_flip` grows the dimension past the threshold. *Expected:* auto plan flips to sort-merge and slows 5×. *Objective:* pin broadcast with a hint.

### Interactive Activities
- **Plan bingo (10 min):** each pair gets a plan and races to mark `Exchange`, join type, `PushedFilters`, `PartitionFilters`, and `WholeStageCodegen`.
- **Tune-off (12 min):** two teams tune the same regressed query; lowest shuffle-bytes + zero spill wins the leaderboard slot.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_sample` | Course tooling (partitioned by `event_date`) | Delta | 50 M rows | Pruning + plan labs |
| `drivers` | Course tooling (sized near broadcast threshold) | Delta | 450 K rows | Broadcast/sort-merge flip |
| `weather` | Course tooling | Delta | small | Second dimension join |
| `regressed_report.py` | Course tooling (anti-tuned) | code | — | Lab 4 starting point |

### Demo Requirements
- **Instructor demo:** live plan-diff of the broadcast→sort-merge regression and the one-line fix, under 8 minutes.
- **Student demo:** one pair reads their tuned plan aloud and shows the AQE annotations.
- **Expected outputs:** correct plan diagnosis, restored prune + broadcast, zero spill, ≥90% shuffle reduction.

---

# Module 5 — Spark MLlib Pipelines at Scale

## Module Overview

**Purpose.** Everything so far has been analytics; this module is machine learning — but at a scale where scikit-learn's `fit()` on a pandas DataFrame is not an option. Participants learn Spark MLlib's `Pipeline` abstraction (the same `Transformer`/`Estimator`/`Pipeline` vocabulary sklearn users already know, but distributed), assemble a real feature-engineering pipeline over the Masar `trips` data, train a classifier that runs across executors on tens of millions of rows, tune it with distributed cross-validation, evaluate it with the right metrics for an imbalanced problem, and persist the fitted pipeline so it can be reloaded and applied in a batch job (Module 6). The concrete task: **predict, at request time, whether a Masar trip will be cancelled**, so the platform can intervene (better driver matching, surge adjustment).

**Business relevance.** Cancellations are pure lost value for a mobility platform — a rider who abandons, a driver who dispatched for nothing, and a support cost. A model that flags high-cancellation-risk requests lets operations act before the cancellation happens. But the training data is 2.1 billion trips: the model must be trained where the data lives, distributed, without ever collecting to a single machine. Across Saudi industry the pattern is identical — churn prediction on a telecom's subscriber base, default risk on a bank's full loan book, no-show prediction on a ministry's appointment system. The competency is building ML that *scales with the data* instead of forcing the data down to the model.

**Industry use cases.**
- A mobility platform trains a cancellation-risk classifier on a year of trips and scores live requests to trigger proactive driver re-matching.
- A bank builds a distributed feature pipeline over its full transaction history for default-risk scoring, re-fitted monthly.
- A telecom cross-validates a churn model across 40 million subscribers, where a single-machine fit would take days or simply not fit in memory.

**Expected competencies.** After this module a participant can build a Spark ML `Pipeline` (indexers, encoders, `VectorAssembler`, scaler, estimator), fit it on a distributed DataFrame, tune hyperparameters with `CrossValidator`/`TrainValidationSplit`, evaluate with `BinaryClassificationEvaluator`/`MulticlassClassificationEvaluator` using metrics appropriate to class imbalance, handle imbalance (class weights), and save/load the fitted pipeline for reuse.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain Transformer/Estimator/Pipeline and why it prevents train-serve skew | LO4 |
| 5.2 | Build distributed feature engineering (indexing, encoding, assembling, scaling) | LO4 |
| 5.3 | Train a distributed classifier (logistic regression / GBT) on the Masar lake | LO4 |
| 5.4 | Tune with distributed cross-validation and a parameter grid | LO4 |
| 5.5 | Evaluate an imbalanced classifier with the right metrics (AUC-PR, recall) | LO4, LO5 |
| 5.6 | Persist and reload a fitted pipeline for batch scoring | LO4, LO6 |

## Technical Content

### 1. The MLlib Pipeline abstraction

Spark ML mirrors scikit-learn's mental model, distributed over DataFrames:

- A **Transformer** has `.transform(df) -> df` — it adds/changes columns (e.g. `StringIndexer` model, `VectorAssembler`, a *fitted* model producing predictions).
- An **Estimator** has `.fit(df) -> Transformer` — it learns from data (e.g. `LogisticRegression`, `StringIndexer` before fitting, `StandardScaler`).
- A **Pipeline** is itself an Estimator: a sequence of stages; `pipeline.fit(train)` runs each stage's fit/transform in order and returns a `PipelineModel` (a Transformer) that applies the *whole* sequence with one `.transform()`.

Why this matters beyond tidiness: the `PipelineModel` bundles **every** feature transformation with the model. The exact same indexing, encoding, and scaling learned on training data is reapplied at scoring time — eliminating **train-serve skew**, the single most common cause of "great in the notebook, wrong in production." One artefact, one transformation path, reused in Module 6's batch job.

### 2. Distributed feature engineering

Features are computed as DataFrame columns and then vectorised. The standard Masar stack:

- **`StringIndexer`** — map a categorical string (`city`, `service_type`, `payment_method`) to a numeric index. `handleInvalid="keep"` buckets unseen categories at scoring time (critical for production).
- **`OneHotEncoder`** — expand indices into sparse one-hot vectors (for linear models; tree models can use indices directly).
- **`VectorAssembler`** — combine all feature columns into a single `features` vector column, the input every MLlib estimator expects.
- **`StandardScaler` / `MinMaxScaler`** — scale numeric features (needed for logistic regression, harmless-to-skip for trees).

Two big-data disciplines to teach: (1) build features from columns already in the lake plus cheap joins to dimensions — never a per-row Python UDF (Module 2's lesson applies doubly in ML). (2) Engineer only leakage-free features: use `request_ts`-time information (city, service_type, surge_multiplier, hour-of-day, is-weekend, driver rating) — **never** `dropoff_ts` or the fare of the very trip you are predicting, which are unknown at request time. Leakage is the deadliest and most seductive bug in ML at scale.

### 3. Training a distributed classifier

MLlib estimators run the training algorithm across executors — the data never leaves the cluster:

- **`LogisticRegression`** — fast, interpretable coefficients, a strong baseline; needs scaled, encoded features. Supports `weightCol` for class imbalance.
- **`GBTClassifier` / `RandomForestClassifier`** — tree ensembles, capture non-linear interactions, tolerate unscaled features and raw indices; usually the accuracy winner for tabular data like Masar.

The label: `label = 1` if `status = 'cancelled'` else `0`. The class balance is skewed (~12–15% cancellations), which drives every evaluation and imbalance decision below.

### 4. Hyperparameter tuning with distributed cross-validation

Never trust one train/test split at scale. MLlib provides:

- **`ParamGridBuilder`** — a grid of hyperparameters (e.g. `regParam`, `maxIter`, or GBT `maxDepth`, `maxIter`).
- **`CrossValidator`** — k-fold CV, each fold trained distributed; picks the best grid point by an evaluator's metric. Set `parallelism` to train several grid points concurrently (uses the cluster more fully).
- **`TrainValidationSplit`** — a single held-out split; far cheaper than k-fold, appropriate when data is huge and folds are expensive.

Teaching point: at 50 million rows, a 5-fold CV over a 12-point grid is 60 full trainings — real cluster time. Choose the grid deliberately, use `TrainValidationSplit` for large data, and always tune on a *sample* first to bound cost before scaling up.

### 5. Evaluating an imbalanced classifier

With ~13% positives, **accuracy is a trap**: a model predicting "never cancelled" scores 87% accuracy and is useless. Teach the right instruments:

- **`BinaryClassificationEvaluator`** with `areaUnderPR` (AUC-PR) — the honest headline metric for a rare positive class; `areaUnderROC` (AUC-ROC) as a secondary.
- **Precision / Recall / F1** at a chosen threshold — recall matters most here (catching cancellations); precision bounds the intervention cost.
- **The threshold is a business decision, not a default 0.5.** Sweep thresholds, show the precision-recall trade-off, and pick where the intervention economics work.

Handle imbalance with **class weights** (`weightCol`): weight positives up so the model does not ignore them — cheaper and often as effective as resampling, and it stays fully distributed. Always compare weighted vs unweighted on AUC-PR and recall.

### 6. Persistence and common mistakes

A fitted `PipelineModel` is saved and reloaded as a directory of Parquet/metadata — the artefact Module 6's batch job consumes:

```python
model.write().overwrite().save("s3a://masar-lakehouse/models/cancel_v1")
loaded = PipelineModel.load("s3a://masar-lakehouse/models/cancel_v1")
```

**Common mistakes (seeded in Lab 5):**
1. **Leakage** — including `dropoff_ts`, final fare, or `status` itself as a feature. Model looks perfect, fails live.
2. Judging the model by accuracy on a 13%-positive problem.
3. `.toPandas()` the training set to use sklearn — abandons distribution, OOMs at scale.
4. Fitting `StringIndexer` on train only, then hitting unseen categories at scoring time without `handleInvalid="keep"`.
5. Scaling *after* the split incorrectly, or forgetting scaling for logistic regression.
6. A 5-fold × huge-grid CV on the full dataset with no cost estimate — a surprise multi-hour cluster bill.

**Production considerations.** Version the model artefact and the training data snapshot (Delta version) together so a prediction is reproducible. Record the training metrics alongside the artefact. Keep the feature list in one module shared by training and scoring so they cannot drift. Re-fit on a schedule and compare AUC-PR against the incumbent before promoting.

## Code Examples

### Building the cancellation-prediction pipeline

```python
# src/masar/ml/features.py
"""Leakage-free feature spec, shared by training AND batch scoring (Module 6)."""
from pyspark.sql import DataFrame, functions as F

CATEGORICAL = ["city", "service_type", "payment_method"]
NUMERIC     = ["distance_km", "surge_multiplier", "hour_of_day", "driver_rating"]

def label_and_features(trips: DataFrame, drivers: DataFrame) -> DataFrame:
    """Only request-time information — nothing known solely after the trip."""
    dim = drivers.select("driver_id", F.col("rating").alias("driver_rating")) \
                 .dropDuplicates(["driver_id"])
    return (trips.join(F.broadcast(dim), "driver_id", "left")
            .withColumn("hour_of_day", F.hour("request_ts"))
            .withColumn("label",
                        F.when(F.col("status") == "cancelled", 1.0).otherwise(0.0))
            # NOTE: dropoff_ts, fare_sar of THIS trip, and status are NOT features.
            .select(*CATEGORICAL, *NUMERIC, "label")
            .na.fill({"driver_rating": 4.5, "distance_km": 0.0}))
```

```python
# src/masar/ml/pipeline.py
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import GBTClassifier
from masar.ml.features import CATEGORICAL, NUMERIC

def build_pipeline() -> Pipeline:
    indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_idx",
                              handleInvalid="keep") for c in CATEGORICAL]
    encoders = [OneHotEncoder(inputCol=f"{c}_idx", outputCol=f"{c}_oh")
                for c in CATEGORICAL]
    assembler = VectorAssembler(
        inputCols=[f"{c}_oh" for c in CATEGORICAL] + NUMERIC,
        outputCol="features_raw")
    scaler = StandardScaler(inputCol="features_raw", outputCol="features")
    gbt = GBTClassifier(featuresCol="features", labelCol="label",
                        maxDepth=5, maxIter=40)
    return Pipeline(stages=indexers + encoders + [assembler, scaler, gbt])
```

### Training, tuning, and evaluating at scale

```python
# notebooks/05_train_cancel_model.py
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from masar.session import build_session, TRIPS_SAMPLE, DRIVERS_PATH
from masar.ml.features import label_and_features
from masar.ml.pipeline import build_pipeline

spark   = build_session("cancel-model")
trips   = spark.read.format("delta").load(TRIPS_SAMPLE)
drivers = spark.read.format("delta").load(DRIVERS_PATH)

data = label_and_features(trips, drivers)
train, test = data.randomSplit([0.8, 0.2], seed=42)
train.cache(); train.count()          # materialise once for repeated CV passes

pipeline = build_pipeline()
grid = (ParamGridBuilder()
        .addGrid(pipeline.getStages()[-1].maxDepth, [4, 6])
        .addGrid(pipeline.getStages()[-1].maxIter, [30, 60])
        .build())

evaluator = BinaryClassificationEvaluator(labelCol="label",
                                          metricName="areaUnderPR")  # imbalance-honest

# TrainValidationSplit (not 5-fold CV) because data is large; parallelism uses the cluster
tvs = TrainValidationSplit(estimator=pipeline, estimatorParamMaps=grid,
                           evaluator=evaluator, trainRatio=0.8, parallelism=4)
model = tvs.fit(train)

preds = model.transform(test)
print("Test AUC-PR:", evaluator.evaluate(preds))
print("Test AUC-ROC:",
      BinaryClassificationEvaluator(labelCol="label",
                                    metricName="areaUnderROC").evaluate(preds))
```

### Class weights for imbalance + threshold sweep

```python
# notebooks/05_imbalance.py
from pyspark.sql import functions as F

# 1) Add a class-weight column (up-weight the ~13% positives)
pos = train.filter("label = 1").count(); neg = train.filter("label = 0").count()
w_pos = neg / (pos + neg); w_neg = pos / (pos + neg)
train_w = train.withColumn("w", F.when(F.col("label") == 1, w_pos).otherwise(w_neg))
# (rebuild the pipeline's final estimator with weightCol="w")

# 2) Sweep the decision threshold on probabilities — 0.5 is rarely right
from pyspark.ml.functions import vector_to_array
scored = preds.withColumn("p1", vector_to_array("probability")[1])
for t in [0.2, 0.3, 0.4, 0.5]:
    tp = scored.filter(f"p1 >= {t} AND label = 1").count()
    fp = scored.filter(f"p1 >= {t} AND label = 0").count()
    fn = scored.filter(f"p1 <  {t} AND label = 1").count()
    prec = tp / max(tp + fp, 1); rec = tp / max(tp + fn, 1)
    print(f"thr {t}: precision {prec:.3f}  recall {rec:.3f}")
```

### Persisting the fitted pipeline for batch reuse

```python
# notebooks/05_persist.py
MODEL_PATH = "s3a://masar-lakehouse/models/cancel_v1"    # local: ./lakehouse/models/cancel_v1
model.bestModel.write().overwrite().save(MODEL_PATH)

# Reload proves the artefact is self-contained (all transformers + the model)
from pyspark.ml import PipelineModel
reloaded = PipelineModel.load(MODEL_PATH)
reloaded.transform(test).select("city", "prediction", "probability").show(5)
```

## Hands-on Lab 5 — Distributed Cancellation-Prediction Pipeline

| | |
|---|---|
| **Objective** | Build, train, tune, evaluate, and persist a leakage-free Spark ML pipeline that predicts trip cancellation on the Masar lake — using imbalance-appropriate metrics and distributed cross-validation |
| **Duration** | 50 minutes |
| **Setup** | Labs 1–4 complete, `git checkout lab5_start`; `trips_sample`, `drivers` loaded; Spark UI open |

**Instructions & tasks**

1. *(6 min)* Build `label_and_features`; verify the label balance (~13% positive) and confirm **no leakage columns** are present.
2. *(8 min)* Assemble `build_pipeline()` (indexers → encoders → assembler → scaler → GBT). Fit on `train`; inspect the fitted `PipelineModel` stages.
3. *(8 min)* Evaluate on `test` with **AUC-PR** and AUC-ROC. Compute accuracy too and discuss why it flatters a 13%-positive model.
4. *(10 min)* Tune with `TrainValidationSplit` over a small grid (`maxDepth`, `maxIter`), `parallelism=4`. Record the best params and AUC-PR; note the wall time.
5. *(8 min)* Add class weights; re-evaluate. Sweep thresholds 0.2–0.5 and choose one by the precision/recall trade-off for "intervene on high-risk requests."
6. *(6 min)* Save the fitted pipeline to `models/cancel_v1`; reload it and score five rows to prove it is self-contained.
7. *(4 min)* Commit `feat(ml): cancellation pipeline v1 (AUC-PR + weights + persisted)` and paste metrics into `BENCHMARKS.md`.

**Expected output**
```
Label balance: 0.131 positive (cancelled)
Baseline GBT:      AUC-PR 0.412  AUC-ROC 0.781  accuracy 0.872 (misleading)
Tuned (d=6,it=60): AUC-PR 0.463  AUC-ROC 0.804   | TrainValidationSplit 6m 40s
+ class weights:   AUC-PR 0.465  recall@0.30 0.71 (was 0.48 @0.50)
Chosen threshold:  0.30  -> precision 0.34  recall 0.71
Persisted + reloaded: PipelineModel with 8 stages; 5 rows scored OK
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| AUC-PR near 0.99, "too good" | Leakage (`status`/`dropoff_ts`/this trip's fare in features) | Remove post-outcome columns; re-fit |
| Scoring errors on unseen category | `StringIndexer` without `handleInvalid` | Set `handleInvalid="keep"` on every indexer |
| CV runs for an hour | 5-fold × large grid on full data | Use `TrainValidationSplit`, shrink grid, tune on sample first |
| Logistic regression underperforms | Features unscaled | Keep `StandardScaler` in the pipeline before LR |
| `OneHotEncoder` error on trees | Encoding not needed; sparse vector edge cases | For GBT/RF feed indices directly; drop encoders |

**Instructor notes.** Task 1's leakage check is the whole module in miniature — have every pair state, out loud, why each excluded column is unknown at request time. Fast finishers: swap the GBT for `LogisticRegression`, compare AUC-PR and coefficients, and discuss the interpretability-vs-accuracy trade-off for an operations team.

## Mini Exercises

**Quiz (5 questions)**
1. Difference between a Transformer and an Estimator? → Transformer has `.transform`; Estimator has `.fit` returning a Transformer.
2. Why does a `PipelineModel` prevent train-serve skew? → it bundles the exact fitted feature transformations with the model, reused at scoring.
3. On a 13%-positive problem, why is accuracy misleading and what do you use instead? → a trivial "no" scores 87%; use AUC-PR / recall.
4. What does `handleInvalid="keep"` do and why is it needed? → buckets unseen categories at scoring so scoring doesn't error.
5. Name one feature that would be leakage in the cancellation model. → `dropoff_ts` / the completed fare / `status` itself.

**Leakage hunt.** Provide a feature list containing two leakage columns; have participants identify them and justify why each is unavailable at request time.

**Metric exercise.** Give confusion-matrix counts at three thresholds; have pairs compute precision/recall/F1 and recommend a threshold for a stated intervention cost.

**Discussion questions.**
- Trees vs logistic regression on Masar tabular data: what does each buy the operations team, and how would you decide?
- Your CV would take four hours at full scale. What do you change to bound the cost without abandoning tuning rigour?

## Case Study — The 99% Model That Failed on Day One

**Scenario.** A Masar data scientist built a cancellation model that scored **AUC-ROC 0.994** in the notebook — near-perfect. Deployed to score live requests, it was useless: it could not distinguish anything, because its best "feature" was `dropoff_ts` (null for cancelled trips) — information that does not exist at request time.

**Business context.** The near-perfect offline metric got the model fast-tracked past review. In production it degenerated to predicting "cancelled" whenever `dropoff_ts` was null — which is *definitionally* every cancelled trip — so it learned nothing generalisable and provided zero lead time for intervention.

**Technical challenge.** Diagnose the leakage, rebuild a strictly request-time feature set, and re-establish honest metrics that survive contact with production.

**Constraints.** Features must be computable at request time only; the model must beat the 13%-cancellation base rate on AUC-PR; the feature list must be shared with the scoring job so it cannot drift.

**Solution approach (facilitate, don't lecture).** (1) Rank feature importances / coefficients — the dominance of one post-outcome column is the tell. (2) Audit every feature against "is this known when the request is made?" (3) Rebuild features from `request_ts`-time fields only. (4) Re-evaluate on AUC-PR (expect a realistic ~0.45, not 0.99). (5) Move the feature spec into one shared module (`features.py`) imported by both training and the Module 6 batch job so the two can never diverge.

**Discussion questions.**
1. How does a single leakage feature produce a near-perfect offline metric and a worthless live model?
2. What one question, asked of every feature, would have caught this in review?
3. Why is a "realistic" AUC-PR of 0.45 more trustworthy than an offline 0.99?
4. How does sharing one feature module between training and scoring prevent a whole class of production bugs?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Leakage-free feature set | Correctness | Zero post-outcome features | feature audit checklist |
| Headline metric | Correctness | AUC-PR reported (not accuracy) | `BinaryClassificationEvaluator` |
| Model beats base rate | Performance | AUC-PR > 0.30 (base 0.13) | test-set evaluation |
| Distributed training | Scalability | No `toPandas`; runs across executors | UI executors during `fit` |
| Recall at chosen threshold | Business fit | Recall ≥ 0.65 for interventions | threshold sweep |
| Persisted + reloadable | Reproducibility | `PipelineModel.load` scores correctly | reload + score check |

**Example benchmark table (filled during lab):**

| Model / setting (50 M sample) | AUC-PR | AUC-ROC | Recall@thr | Train time |
|---|---|---|---|---|
| GBT baseline (thr 0.5) | 0.412 | 0.781 | 0.48 | 2m 10s |
| GBT tuned (TVS grid) | 0.463 | 0.804 | 0.52 | 6m 40s |
| GBT + class weights (thr 0.3) | 0.465 | 0.803 | 0.71 | 6m 55s |
| Logistic regression (scaled) | 0.401 | 0.769 | 0.44 | 1m 30s |

## Required Visuals and Training Assets

### Diagrams
1. **Pipeline stages flow** — *Purpose:* make the abstraction concrete. *Elements:* raw columns → StringIndexer → OneHotEncoder → VectorAssembler → StandardScaler → GBT, each labelled Transformer/Estimator, emitting one `PipelineModel`. *Style:* left-to-right stage chain.
2. **Train-serve skew, prevented** — *Purpose:* the core value of the pipeline. *Elements:* two paths (training, scoring) sharing the *same* fitted transformers vs a broken world with two divergent feature scripts. *Style:* good/bad comparison.
3. **Leakage timeline** — *Purpose:* teach request-time discipline. *Elements:* a trip timeline (request → pickup → dropoff) with a vertical "decision time" line; features left of it green, right of it red. *Style:* annotated timeline.
4. **Precision-recall trade-off** — *Purpose:* threshold is a business choice. *Elements:* a PR curve with the chosen operating point and the intervention-cost annotation. *Style:* labelled curve.

### Images (screenshots)
1. **Executors tab during distributed `fit`** — proof training uses the cluster, not the driver.
2. **PipelineModel stage list** after fitting — the eight bundled stages.
3. **AUC-PR vs AUC-ROC** side by side for the imbalanced model.
4. **Saved model directory** (Parquet + metadata) showing a self-contained artefact.

### Simulations
1. **Leakage demo** — *Setup:* `sim_leakage` adds `dropoff_ts` as a feature. *Expected:* AUC-ROC ~0.99 offline, garbage live. *Objective:* audit features against request time.
2. **Accuracy trap** — *Setup:* `sim_accuracy_trap` reports accuracy on the 13%-positive set. *Expected:* 87% "accuracy" from a constant predictor. *Objective:* use AUC-PR/recall.

### Interactive Activities
- **Feature-or-leakage sort (10 min):** teams sort 15 candidate columns into "request-time" vs "leakage" and defend each.
- **Threshold auction (10 min):** given intervention costs, teams pick a threshold to maximise net value and compare on the leaderboard.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips_sample` | Course tooling (~13% cancelled) | Delta | 50 M rows | Model training/eval |
| `drivers` | Course tooling (has `rating`) | Delta | 450 K rows | Feature join (driver_rating) |
| `models/cancel_v1` | Produced in Lab 5 | PipelineModel dir | small | Reused in Module 6 batch job |

### Demo Requirements
- **Instructor demo:** the leakage-vs-clean contrast — 0.99 offline collapsing to a realistic 0.46 AUC-PR once leakage is removed, under 8 minutes.
- **Student demo:** one pair explains their threshold choice against the intervention economics.
- **Expected outputs:** leakage-free pipeline, AUC-PR beating base rate, persisted + reloaded model.

---

# Module 6 — Big-Data Analytics Project

## Module Overview

**Purpose.** The previous five modules produced *pieces* — queries, tuned jobs, a fitted model. This module assembles them into a **productionised batch analytics workflow on the Lakehouse**: a job that reads yesterday's Masar trips incrementally, computes the analytics tables the business consumes, scores every trip with the cancellation model, and writes idempotent, partitioned Delta outputs that a re-run cannot corrupt. The subject matter is the discipline that separates a notebook from a job you can schedule and trust: incremental processing, idempotent writes, output partition layout, `MERGE`/upsert semantics, table maintenance (`OPTIMIZE`/`VACUUM`), and structuring code so it is testable and re-runnable. This is the direct on-ramp to the capstone and to streaming (SDA-DSC-313), which is this same job with a different clock.

**Business relevance.** Analytics that runs once in a notebook creates a slide; analytics that runs *every night, correctly, unattended* creates a data product. Saudi platforms live on nightly batch: settlement, KPI marts, risk scores, regulatory extracts. The engineer who can turn an exploratory analysis into an idempotent, incremental, partitioned Delta job — one that survives a re-run, a late-arriving file, and a mid-run failure without double-counting revenue — is building the backbone of the data platform. Idempotency in particular is not academic: a job that double-writes a day's revenue when someone re-runs it after a failure causes finance-grade incidents.

**Industry use cases.**
- A mobility platform runs a nightly job that incrementally processes the previous day's trips into a city-KPI mart and a scored-trips table, re-runnable without double counting.
- A bank's nightly risk batch upserts scores into a Delta table with `MERGE`, so a re-run corrects rather than duplicates.
- A telecom compacts thousands of small streaming-ingested files each night with `OPTIMIZE` so the next day's analytics reads fast.

**Expected competencies.** After this module a participant can structure a batch job as importable, testable functions; process incrementally by partition; write idempotently (partition overwrite / `MERGE` upsert); lay out output partitions for the downstream read; apply Delta table maintenance; and reuse the Module 5 model inside the batch scoring step without train-serve skew.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Structure a batch job as importable, testable functions (not a notebook) | LO6 |
| 6.2 | Process incrementally: read/compute one partition (day) at a time | LO6 |
| 6.3 | Write idempotently: partition overwrite and `MERGE` upsert semantics | LO6 |
| 6.4 | Lay out output partitions and maintain tables (`OPTIMIZE`, `VACUUM`, Z-order) | LO3, LO6 |
| 6.5 | Reuse the fitted pipeline for batch scoring without train-serve skew | LO4, LO6 |
| 6.6 | Add guardrails: row-count checks, idempotency proof, data-quality gates | LO6 |

## Technical Content

### 1. From notebook to job

A schedulable job is not a notebook with the cells re-ordered. Teach the structure:

- **Pure, importable functions** in `src/masar/jobs/` — each takes DataFrames/params and returns a DataFrame, no top-level side effects. This makes them unit-testable on tiny fixtures.
- **A thin `main(run_date)`** that wires reads → transforms → writes, driven by a single date argument.
- **One `config.py`** for all paths and the model location — the only thing that changes between environments.
- **Deterministic inputs** — a run is parameterised by `run_date` (and a Delta snapshot version), so re-running the same date produces the same output.

The litmus test: the whole job runs from the command line (`python -m masar.jobs.daily --date 2025-06-01`), and its transform functions are covered by fast tests on 100-row fixtures.

### 2. Incremental processing

Reprocessing 180 GB every night to add one day is waste. Incremental processing reads and writes **one partition at a time**:

- The input lake is partitioned by `event_date`; read only `run_date` with a partition-pruned filter (Module 4) — seconds, not minutes.
- Compute the day's analytics and the day's scored trips.
- Write only that day's output partition.

The bookkeeping question — "which days are already processed?" — is answered by the output table itself (a `MAX(event_date)` or a small watermark table), so the job knows where to resume. For late-arriving data, reprocess the affected day's partition; because writes are idempotent (next section), reprocessing is safe.

### 3. Idempotent writes — the heart of batch correctness

An idempotent write means **running the job for a date twice produces the same table as running it once** — no duplicates, no double-counted revenue. Two Delta mechanisms:

- **Dynamic/static partition overwrite:** overwrite *only* the run_date partition, leaving all others untouched.

```python
(daily_df.write.format("delta")
    .mode("overwrite")
    .option("replaceWhere", f"event_date = '{run_date}'")   # surgical, idempotent
    .partitionBy("event_date")
    .save(CITY_KPI_PATH))
```

`replaceWhere` is the key: a naive `mode("overwrite")` would wipe the *entire* table; `mode("append")` would duplicate on re-run. `replaceWhere` replaces exactly one day.

- **`MERGE` (upsert):** when output grain is keyed (e.g. one row per `trip_id` in a scored table), `MERGE` updates matching rows and inserts new ones — the canonical idempotent upsert.

```sql
MERGE INTO scored_trips t
USING updates u ON t.trip_id = u.trip_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
```

Teaching point: **choose the mechanism by output grain.** Aggregated per-day tables → `replaceWhere`. Keyed per-entity tables → `MERGE`. Never `append` a job that can be re-run.

### 4. Output layout and table maintenance

How you write dictates how fast the next job reads:

- **Partition by low-cardinality, high-selectivity columns** — `event_date` (and maybe `city`), so downstream reads prune. Do *not* partition by a high-cardinality key (`trip_id`) — that creates the small-files catastrophe.
- **`OPTIMIZE`** compacts many small files into few right-sized ones; **`ZORDER BY (city)`** co-locates rows by a common filter column so reads skip more files.
- **`VACUUM`** removes old, unreferenced files after the retention window (keep Delta time-travel long enough for audits, e.g. 7–30 days).

```sql
OPTIMIZE city_kpi ZORDER BY (city);
VACUUM city_kpi RETAIN 168 HOURS;   -- 7 days
```

These run as periodic maintenance, not every job, but the job must *write in a layout that maintenance can keep healthy*.

### 5. Batch scoring with the fitted pipeline

The Module 5 `PipelineModel` is reused verbatim — this is why the pipeline abstraction mattered:

```python
from pyspark.ml import PipelineModel
model = PipelineModel.load(MODEL_PATH)              # the exact fitted transformers + GBT
features = label_and_features(days_trips, drivers)  # SAME shared feature module
scored = model.transform(features).select("trip_id", "prediction", "probability")
```

No feature code is re-implemented in the job; it imports the same `features.py` the training used. That single shared module is the structural guarantee against train-serve skew (Module 5's lesson made operational). The scored output is upserted with `MERGE` on `trip_id`.

### 6. Guardrails and common mistakes

Production jobs assert their own correctness:

- **Row-count / null gates** before write (e.g. "revenue rows must equal distinct cities for the day"; "no null `trip_id`").
- **Idempotency test in CI** — run the job twice on a fixture date; assert the output table is byte-for-byte identical (this is the single most valuable test in the whole course).
- **Reconciliation** — the day's total revenue must match a direct query on the source.

**Common mistakes (seeded in Lab 6):**
1. `mode("append")` on a re-runnable job → double-counted revenue on the second run.
2. `mode("overwrite")` without `replaceWhere` → wipes the whole history to write one day.
3. Reprocessing the full lake nightly instead of one partition.
4. Partitioning output by `trip_id` → millions of tiny files.
5. Re-implementing feature logic in the job instead of importing the shared module → train-serve skew.
6. Never running `OPTIMIZE`/`VACUUM` → small-files rot and unbounded storage.

**Production considerations.** Make the job's date and Delta input-version explicit so a run is reproducible and auditable. Emit run metadata (rows in/out, duration, model version) to a log/table. Fail fast and loud on a guardrail breach rather than writing bad data. Schedule maintenance (`OPTIMIZE`/`VACUUM`) separately from the critical-path job.

## Code Examples

### The daily batch job — structured, incremental, idempotent

```python
# src/masar/jobs/daily.py
"""Nightly Masar analytics: city KPIs + scored trips for one run_date.
Runnable: python -m masar.jobs.daily --date 2025-06-01"""
import argparse
from pyspark.ml import PipelineModel
from pyspark.sql import functions as F
from masar.session import build_session
from masar.config import TRIPS_PATH, DRIVERS_PATH, CITY_KPI_PATH, SCORED_PATH, MODEL_PATH
from masar.analytics.city_report import city_performance
from masar.ml.features import label_and_features


def city_kpis_for(trips_day, run_date):
    return city_performance(trips_day).withColumn("event_date", F.lit(run_date))


def score_trips_for(trips_day, drivers, model):
    feats = label_and_features(trips_day, drivers)          # SHARED feature module
    keyed = trips_day.select("trip_id").join(
        model.transform(feats).select("prediction", "probability"))
    return keyed  # illustrative; real code carries trip_id through the pipeline


def run(run_date: str):
    spark = build_session(f"daily-{run_date}")
    # Incremental read: partition pruning means only run_date's files are scanned
    trips_day = (spark.read.format("delta").load(TRIPS_PATH)
                 .filter(F.col("event_date") == run_date))
    drivers = spark.read.format("delta").load(DRIVERS_PATH)
    model = PipelineModel.load(MODEL_PATH)

    kpis = city_kpis_for(trips_day, run_date)
    # Idempotent: replaceWhere overwrites ONLY this day's partition
    (kpis.write.format("delta").mode("overwrite")
         .option("replaceWhere", f"event_date = '{run_date}'")
         .partitionBy("event_date").save(CITY_KPI_PATH))

    scored = score_trips_for(trips_day, drivers, model)
    # Idempotent upsert by trip_id via MERGE (see 06_merge.py)
    upsert_scored(spark, scored, run_date)
    spark.stop()


if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--date", required=True)
    run(p.parse_args().date)
```

### Idempotent upsert with Delta MERGE

```python
# src/masar/jobs/merge.py
from delta.tables import DeltaTable

def upsert_scored(spark, scored_df, run_date):
    if DeltaTable.isDeltaTable(spark, SCORED_PATH):
        tgt = DeltaTable.forPath(spark, SCORED_PATH)
        (tgt.alias("t").merge(scored_df.alias("u"), "t.trip_id = u.trip_id")
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute())                        # re-running the date is safe
    else:
        (scored_df.write.format("delta").partitionBy("event_date").save(SCORED_PATH))
```

### The idempotency test — the most valuable test in the course

```python
# tests/test_idempotency.py
def test_daily_job_is_idempotent(spark, tmp_path, fixture_lake):
    from masar.jobs.daily import run
    run("2025-06-01")                          # first run
    first = spark.read.format("delta").load(CITY_KPI_PATH).collect()
    run("2025-06-01")                          # SAME date again (simulates a re-run)
    second = spark.read.format("delta").load(CITY_KPI_PATH).collect()
    assert first == second                     # no duplication, no double-count
```

### Table maintenance (scheduled separately)

```sql
-- notebooks/06_maintenance.sql  (run as periodic maintenance, not per job)
OPTIMIZE delta.`./lakehouse/city_kpi` ZORDER BY (city);
VACUUM  delta.`./lakehouse/city_kpi` RETAIN 168 HOURS;   -- keep 7 days of time-travel
```

## Hands-on Lab 6 — Productionise the Nightly Analytics Job

| | |
|---|---|
| **Objective** | Turn the course's analytics + model into a structured, incremental, idempotent batch job that writes partitioned Delta outputs, reuses the fitted pipeline, and proves idempotency with a re-run test |
| **Duration** | 50 minutes |
| **Setup** | Labs 1–5 complete, `git checkout lab6_start` (skeleton `jobs/daily.py`); `models/cancel_v1` from Lab 5 present |

**Instructions & tasks**

1. *(6 min)* Wire `run(run_date)`: incremental read of one `event_date`, confirm partition pruning in the UI (only that day's files scanned).
2. *(8 min)* Compute the city-KPI table; write it with `replaceWhere` on `event_date`. Confirm only the run_date partition changed.
3. *(8 min)* Load `models/cancel_v1` and score the day's trips using the **shared** `features.py`; do not re-implement features.
4. *(8 min)* Upsert scored trips with `MERGE` on `trip_id`. Run the job twice for the same date; confirm the scored table row count is unchanged.
5. *(8 min)* Add a guardrail: assert no null `trip_id` and that the day's revenue reconciles to a direct source query; make the job fail on breach.
6. *(6 min)* Run the idempotency test (`tests/test_idempotency.py`); make it green. Run `OPTIMIZE ZORDER BY (city)` and observe file compaction.
7. *(6 min)* Commit `feat(job): idempotent incremental daily analytics + scoring`; paste run metadata into `BENCHMARKS.md`.

**Expected output**
```
Incremental read (2025-06-01): 2/34 files scanned, 4.1 s
city_kpi written: 1 partition (event_date=2025-06-01), 14 rows, replaceWhere OK
scored_trips MERGE: 1,462,205 upserts
Re-run same date:  city_kpi identical (14 rows); scored_trips row count unchanged (idempotent)
Guardrail: 0 null trip_id; revenue reconciles to source (delta 0.00 SAR)
OPTIMIZE: 128 files -> 6 files; test_daily_job_is_idempotent PASSED
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Whole table wiped on write | `mode("overwrite")` without `replaceWhere` | Add `replaceWhere event_date = ...` |
| Revenue doubles on second run | `mode("append")` on re-runnable job | Use `replaceWhere` (aggregates) or `MERGE` (keyed) |
| Full-lake scan each night | No partition filter on read | Filter `event_date == run_date` for pruning |
| Millions of tiny output files | Partitioned by `trip_id` | Partition by `event_date`; `OPTIMIZE` to compact |
| Scoring drifts from training | Features re-implemented in the job | Import the shared `features.py` used in Lab 5 |

**Instructor notes.** Task 4's "run it twice, count unchanged" is the emotional payoff of the whole batch story — make everyone do it and watch the row count *not* move. Fast finishers: simulate a late-arriving file for a prior date and reprocess only that partition, proving the rest of the table is untouched.

## Mini Exercises

**Quiz (5 questions)**
1. What does idempotent mean for a batch job, and why does it matter? → running twice = running once; prevents double-counting on re-runs.
2. `replaceWhere` vs plain `overwrite` vs `append` — which is safe for a re-runnable daily aggregate? → `replaceWhere` (surgical one-partition overwrite).
3. When do you use `MERGE` instead of `replaceWhere`? → keyed per-entity output (upsert by key), e.g. scored trips by `trip_id`.
4. Why partition output by `event_date` and not `trip_id`? → low cardinality prunes reads; `trip_id` explodes into tiny files.
5. What does `OPTIMIZE ZORDER BY (city)` buy the next reader? → compacted files + data clustered by `city` so filtered reads skip more files.

**Refactor exercise.** Give a notebook that reprocesses the full lake and `append`s output; have participants convert it to incremental + `replaceWhere` and explain both fixes.

**Idempotency proof.** Have pairs run the job twice on the fixture date and demonstrate, with a row count and a checksum, that the output did not change.

**Discussion questions.**
- Where should the "which days are processed?" watermark live, and what are the trade-offs of deriving it from the output table vs a separate state table?
- A late file arrives for a date processed last week. Walk through the safe reprocessing path and why idempotency makes it low-risk.

## Case Study — The Double-Counted Revenue Incident

**Scenario.** A Masar nightly analytics job failed halfway one night. On-call re-ran it. The next morning, the city-revenue mart showed several cities with *doubled* revenue for that date — the job used `mode("append")`, so the re-run added a second copy of the day's rows instead of replacing them.

**Business context.** The doubled figures flowed into a finance dashboard and a driver-incentive calculation before anyone noticed. Unwinding it required identifying which partitions were affected, deleting duplicates, and reprocessing — a full morning of incident work and a shaken trust in the mart.

**Technical challenge.** Make the job idempotent so a re-run (or a late-file reprocess) is always safe, and add a test that would have caught the defect before release.

**Constraints.** Historical partitions must not be touched by a single-day re-run; the fix must reconcile the affected date to the source total; the guarantee must be enforced automatically, not by operator discipline.

**Solution approach (facilitate, don't lecture).** (1) Identify the `append` as the root cause. (2) Replace with `replaceWhere` for the aggregate table and `MERGE` for the keyed scored table. (3) Backfill/repair the corrupted date by reprocessing it (now safe). (4) Add the two-run idempotency test to CI so any regression to `append` fails the build. (5) Add a revenue-reconciliation guardrail that fails the job if the written total diverges from the source.

**Discussion questions.**
1. Why is `append` a latent double-counting bug on any re-runnable job?
2. How do `replaceWhere` and `MERGE` each guarantee idempotency, and when do you choose which?
3. What single automated test converts "please don't re-run twice" into a guarantee?
4. How does partition-scoped overwrite protect the rest of the table's history during a single-day repair?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Job is idempotent | Correctness | Two runs → identical table | idempotency test |
| Incremental read | Performance | Only run_date partition scanned | UI files-read |
| Revenue reconciliation | Correctness | Written total == source total | reconciliation check |
| Output file health | Performance | Post-`OPTIMIZE` files 128–256 MB | Delta file listing |
| Batch scoring reuse | Correctness | Same `features.py` as training | code/import check |
| Runnable from CLI + tested | Maintainability | `python -m` runs; fixtures green | CI |

**Example benchmark table (filled during lab):**

| Step (one run_date) | Wall time | Files read/written | Rows | Idempotent? |
|---|---|---|---|---|
| Incremental read | 4.1 s | 2 / — | 1.46 M | — |
| City-KPI `replaceWhere` | 6.8 s | — / 1 part | 14 | Yes |
| Score + `MERGE` | 22 s | — / merge | 1.46 M | Yes |
| Re-run same date | 30 s | — | unchanged | Proven |
| OPTIMIZE ZORDER | 18 s | 128 / 6 | — | — |

## Required Visuals and Training Assets

### Diagrams
1. **Notebook → job** — *Purpose:* the structural shift. *Elements:* scattered notebook cells vs `jobs/daily.py` + `config.py` + tested transform functions driven by `--date`. *Style:* messy/clean comparison.
2. **Incremental partition flow** — *Purpose:* process one day, not the lake. *Elements:* a partitioned input table with one `event_date` highlighted flowing to one output partition. *Style:* partition-highlight flow.
3. **Idempotent write mechanisms** — *Purpose:* choose by grain. *Elements:* `replaceWhere` (aggregate, one partition replaced) vs `MERGE` (keyed upsert) vs the broken `append` (duplicates). *Style:* three-panel with a red "append" panel.
4. **Lakehouse job architecture (target state)** — *Purpose:* the capstone blueprint. *Elements:* source Delta → incremental read → analytics + model scoring → idempotent partitioned Delta outputs → OPTIMIZE/VACUUM maintenance. *Style:* end-to-end pipeline.

### Images (screenshots)
1. **Delta history (`DESCRIBE HISTORY`)** showing one partition overwritten, not the whole table.
2. **Two identical run outputs** side by side proving idempotency.
3. **File count before/after `OPTIMIZE`** (128 → 6).
4. **CI run with the idempotency test green.**

### Simulations
1. **Append double-count** — *Setup:* `sim_append_rerun` runs an `append` job twice. *Expected:* doubled revenue. *Objective:* use `replaceWhere`/`MERGE`.
2. **Full-lake reprocess** — *Setup:* `sim_full_reprocess` re-reads 180 GB nightly. *Expected:* hours-long run. *Objective:* incremental partition read.

### Interactive Activities
- **Write-mode showdown (10 min):** teams match each output table to the correct write mode (`replaceWhere` / `MERGE` / plain overwrite) and justify.
- **Break-the-job (10 min):** pairs introduce a re-run and race to prove (or disprove) idempotency from the row count.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `trips` (partitioned) | Course tooling | Delta | 50 M sample / 2.1 B full | Incremental input |
| `city_kpi` | Produced by the job | Delta (part. `event_date`) | grows daily | Idempotent aggregate output |
| `scored_trips` | Produced by the job | Delta (keyed `trip_id`) | grows daily | MERGE upsert output |
| `models/cancel_v1` | Lab 5 | PipelineModel | small | Batch scoring |

### Demo Requirements
- **Instructor demo:** run the job, re-run the same date, and show the row count *not* move — under 6 minutes.
- **Student demo:** one pair shows their `MERGE` upsert and idempotency test green.
- **Expected outputs:** idempotent incremental job, reconciled revenue, compacted output, green CI.

---

# Final Capstone Project

## Title: The Masar Nightly Analytics Lakehouse Job

## Project Scenario

You are the newly assigned analytics engineer for **"Masar" (مسار)**, the national mobility and logistics platform. The exploratory analysis, tuning experiments, and cancellation model you built across Labs 1–6 have proven the value — leadership now wants a **production-grade nightly batch job** on the Lakehouse that operations can schedule and trust. Your mandate: deliver one job that, for any given `run_date`, reads the day's trips incrementally, produces the analytics tables the business consumes, scores every trip with the cancellation model, and writes idempotent, tuned, partitioned Delta outputs — a job whose *benchmarks and re-run behaviour prove its own quality*. Every lab is a component; the capstone is the integration plus your own extension.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Distributed correctness (LO1):** the job never collects raw data to the driver; all heavy work stays distributed; every action is justified. No `toPandas()` on the fact table anywhere.
2. **Analytics at scale (LO2):** produce a `city_kpi` table (revenue, completion rate, avg fare, cancellation rate per city per day) implemented in both a reusable DataFrame function and an equivalent registered SQL view; results reconcile to source.
3. **Performance, proven by plans (LO3/LO5):** every fact–dimension join is a `BroadcastHashJoin`; the incremental read is partition-pruned; AQE on; a `BENCHMARKS.md` shows before/after runtime, shuffle bytes, and spill with the query plans that justify each number.
4. **Distributed ML (LO4):** load the fitted `PipelineModel` (or re-fit) and score the day's trips using the **shared** `features.py`; report AUC-PR and the chosen threshold; no train-serve skew.
5. **Idempotent Lakehouse batch (LO6):** incremental per-`event_date` processing; `replaceWhere` for the aggregate and `MERGE` for the keyed scored table; partitioned outputs; `OPTIMIZE`/`VACUUM` maintenance documented; a passing idempotency test.
6. **Guardrails & reproducibility (LO6):** row-count/null gates and a revenue-reconciliation check that fail the job on breach; the run is parameterised by `run_date` (+ Delta input version) and emits run metadata (rows in/out, duration, model version).
7. **Engineering quality:** the job runs from the CLI (`python -m masar.jobs.daily --date ...`); transform functions are covered by fast fixture tests; a README runbook lets a stranger run it in 10 minutes; all paths in one `config.py`.

**One extension (choose at least one):**
- Skew-robust settlement: reproduce the Riyadh skew, fix it with AQE skew-join **and** manual salting, and reconcile totals to the cent.
- Data-quality report table: write a per-run DQ table (null rates, row deltas, late-arrival count) queryable over time.
- Model-refresh path: re-fit the cancellation model on the latest N days, compare AUC-PR to the incumbent, and promote only if better.
- Backfill mode: a `--from --to` range that reprocesses many days idempotently and in the right partition order.
- Z-order + prune benchmark: quantify the read-time win of `OPTIMIZE ZORDER BY (city)` on a downstream filtered query.

## Architecture (target state)

```
Delta source (trips partitioned by event_date, + drivers/riders/weather dims)
      │  incremental read (partition pruning on run_date)
      ▼
 analytics: city_performance()  ──broadcast joins──┐
      │                                            │
      ▼                                            ▼
 city_kpi (Delta, part. event_date)        scoring: PipelineModel.transform(features.py)
   write replaceWhere(event_date)                   │
                                                     ▼
                                        scored_trips (Delta, keyed) — MERGE upsert
      │
      ▼  guardrails: null gate + revenue reconciliation (fail-fast)
 run metadata table (rows in/out, duration, model_version, delta_version)
 maintenance (scheduled): OPTIMIZE ZORDER BY (city) · VACUUM RETAIN 168h
```

## Deliverables

1. Repository/notebook-project URL with full history and a `config.py` of all paths.
2. `python -m masar.jobs.daily --date <d>` runs green on the sample lake; the idempotency test passes.
3. `BENCHMARKS.md` with the six course benchmark tables filled from *your* runs (M1–M6), each with the plan/UI evidence.
4. 5-minute demo: run the job, re-run the same date showing row counts unchanged, one plan read aloud (broadcast + prune), one guardrail breach caught.
5. `DECISIONS.md`: five one-paragraph engineering decisions with rationale (e.g. `replaceWhere` vs `MERGE` per table, threshold choice, partition layout, salting vs AQE, TrainValidationSplit vs CV).

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: Day-1 analytics integrated (`city_kpi` in DF + SQL, reconciled) | End Day 1 | instructor spot-check |
| M-B: tuned job (broadcast + prune + AQE), BENCHMARKS started | End Day 2 | plan shows BroadcastHashJoin |
| M-C: model scoring wired via shared features | Day 3 H2 | AUC-PR reported, no leakage |
| M-D: idempotent incremental job + extension | Day 3 H4 | idempotency test green |
| M-E: demo + submission | Day 3 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Distributed correctness & analytics | 20 | Fully distributed; `city_kpi` in DF+SQL, reconciles exactly; no driver collection of raw data | Minor: one avoidable `collect`, small reconciliation gap | `toPandas`/`collect` of fact data; wrong or unreconciled numbers |
| Performance, proven by plans | 20 | All joins broadcast, reads pruned, AQE tuned; BENCHMARKS with plans justify every number | Mostly tuned; one join sort-merge or thin evidence | Naive joins, full scans, no plan evidence |
| Distributed ML | 15 | Model scored via shared features; AUC-PR + threshold reported; zero leakage | Works but accuracy-reported or thin threshold rationale | Leakage present, or features re-implemented (skew), or scored on driver |
| Idempotent Lakehouse batch | 20 | Incremental + `replaceWhere` + `MERGE`; idempotency test green; maintenance documented | Idempotent but one table uses wrong mode / no maintenance | `append` double-counts; full-lake reprocess; no idempotency |
| Guardrails & reproducibility | 15 | Fail-fast gates + reconciliation; parameterised run + metadata emitted | Gates present but not fail-fast; partial metadata | No guardrails; non-reproducible run |
| Demo & decisions doc | 10 | Crisp demo incl. re-run proof + plan read; DECISIONS shows trade-off literacy | Demo works, rationale thin | Cannot run own job cold |

**Pass ≥ 70. Distinction ≥ 90.** A chosen extension adds up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the evidence first*: run the idempotency test and re-run the job live before scoring the demo — the point of the course is that the job proves itself.
- Anti-pattern flags that cap a criterion at 70%: any `append` on a re-runnable table; a join silently regressed to sort-merge; accuracy reported instead of AUC-PR; features re-implemented in the job; a benchmark number with no plan/UI evidence.
- Verify one performance claim live: ask the participant to open the physical plan and point to the `BroadcastHashJoin` and the populated `PartitionFilters`.

## Bonus Tasks (for early finishers / distinction seekers)

1. Full-scale run: execute one day on the cluster against `masar_full` and report the numbers next to the sample.
2. `sim-skew` reproduction: introduce Riyadh skew, show which fix (AQE vs salt) wins, write a 10-line postmortem reconciling totals.
3. Cost estimate: translate shuffle-bytes and runtime deltas into an estimated monthly cluster-cost saving.
4. Plan-assertion CI: a test that fails if any capstone join is not a `BroadcastHashJoin` or the read loses partition pruning.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Which triggers execution: a transformation or an action? Give one example of each. → action (`count`); transformation (`filter`).
**Q2.** Why is `.collect()` on the full `trips` table dangerous? → pulls all rows to the driver → OOM.
**Q3.** A 180 GB Delta table of ~128 MB files reads as roughly how many partitions? → ~1,400.
**Q4.** Do `spark.sql(...)` and the DataFrame API produce different physical plans? → No — same Catalyst plan.
**Q5.** Which join avoids shuffling the big table, and when is it chosen? → broadcast hash join; when the other side is under the broadcast threshold.
**Q6.** Why prefer `F.when` over a Python UDF? → built-ins run in the JVM and are Catalyst-visible; UDFs serialise every row to Python.
**Q7.** Name three operations that force a shuffle. → `groupBy`, `join`, `distinct`/`orderBy`/windowed `partitionBy`.
**Q8.** `repartition` vs `coalesce` — which shuffles; which can only decrease partitions? → repartition shuffles; coalesce only decreases, no shuffle.
**Q9.** Default `spark.sql.shuffle.partitions`, and why is it often wrong? → 200; ignores actual data size.
**Q10.** How do you spot partition skew in the Spark UI? → max task duration/shuffle-read far exceeds the median.
**Q11.** In a formatted plan, which node is a shuffle and what does `PartitionFilters` being non-empty prove? → `Exchange`; partition pruning happened.
**Q12.** Name the three problems AQE fixes at runtime. → coalesce small partitions, split skewed join partitions, promote to broadcast.
**Q13.** Why is a filter on `to_date(pickup_ts)` slower than on `event_date`? → it loses partition pruning → full-table scan.
**Q14.** On a 13%-positive problem, why is accuracy misleading and what replaces it? → a constant "no" scores 87%; use AUC-PR / recall.
**Q15.** What is train-serve skew and how does a `PipelineModel` prevent it? → training/serving feature logic diverges; the fitted pipeline bundles and reuses the exact transforms.
**Q16.** Name one feature that would be leakage in the cancellation model. → `dropoff_ts` / this trip's fare / `status`.
**Q17.** What does idempotent mean for a batch job, and why does it matter? → run twice = run once; prevents double-counting on re-runs.
**Q18.** `replaceWhere` vs `MERGE` — when do you use each? → `replaceWhere` for per-partition aggregates; `MERGE` for keyed per-entity upserts.
**Q19.** Why partition an output table by `event_date` rather than `trip_id`? → low cardinality prunes reads; `trip_id` explodes into tiny files.
**Q20.** What does `OPTIMIZE ZORDER BY (city)` buy the next reader? → compacted files + city-clustered data so filtered reads skip more files.

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a slow Masar job (sort-merge join on a dimension, filter on a derived date, `shuffle.partitions=200`), produce a tuned version. Scored on: plan diagnosis notes (40%), correct fixes — broadcast + prune + AQE (40%), before/after benchmark evidence (20%).

**PA-2 (30 min, Day 3):** Given a batch job that uses `mode("append")` and re-implements features inline, triage: identify the double-count and skew risks, refactor to `replaceWhere`/`MERGE` and the shared feature module, and write the review. Scored against the model review (idempotency correctness 50%, skew/feature-reuse reasoning 30%, review actionability 20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (6 labs) | 30% | checkpoint commits + expected outputs + BENCHMARKS entries |
| PA-1 + PA-2 | 20% | tuned job + refactor artefacts + notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, evidence-first (idempotency test + plans) |

Badge issuance (Big-data badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** a passing idempotency test **and** zero academic-integrity flags (identical BENCHMARKS numbers across repos are checked).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Generate and stage both dataset scales: `trips_sample` (50 M / ~4.2 GB Delta) and, if a cluster is available, `masar_full` (2.1 B / ~180 GB); verify Riyadh is deliberately ~35% of rows for the skew lesson.
- [ ] Push all checkpoint tags (`lab1_start`/`lab1_solution` … `lab6_start`/`lab6_solution`) and the `sim_*` branches (`sim_collect_oom`, `sim_one_big_file`, `sim_join_blowup`, `sim_bad_shuffle_parts`, `sim_derived_date`, `sim_broadcast_flip`, `sim_leakage`, `sim_accuracy_trap`, `sim_append_rerun`, `sim_full_reprocess`).
- [ ] Fit and stage `models/cancel_v1` against the pinned PySpark/MLlib version; verify it reloads and scores.
- [ ] Dry-run all 6 labs end-to-end on a clean laptop **and** on the managed-Spark fallback (Databricks Community / Dataproc); confirm the Spark UI (port 4040) is reachable in whichever wins.
- [ ] Verify `replaceWhere`, `MERGE`, and `OPTIMIZE`/`VACUUM` all work in the chosen Delta version (behaviour varies across 2.x/3.x).
- [ ] Print A3 posters: cluster anatomy, lazy DAG, physical-plan anatomy, pipeline stages, idempotent-write mechanisms.
- [ ] Prepare the shared benchmark leaderboard (runtime, shuffle bytes, AUC-PR, image of the idempotency test).
- [ ] Confirm classroom network allows the Delta/Spark package downloads, or pre-stage the jars in a local mirror; big-data classes fail fastest on missing `delta-spark` jars.

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.11, `uv` or conda, `git`, and a JDK 17 (Spark 3.5 requirement).
- [ ] `pip install pyspark==3.5.* delta-spark==3.2.* pandas matplotlib pytest` (MLlib ships with PySpark).
- [ ] Launch flag ready: `--packages io.delta:delta-spark_2.12:3.2.0` (or the two Delta configs in `build_session`).
- [ ] ≥ 16 GB RAM recommended for the 50 M sample; 8 GB works with a smaller sample slice.
- [ ] Extract the sample lake to `./lakehouse/`; run `make doctor` (validates Java, PySpark, Delta jars, sample paths, Spark UI) and confirm it prints ✓ across the board.
- [ ] Fallback account ready on the managed-Spark platform in case a laptop cannot run the sample.

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| `Delta is not a valid data source` (missing jars) | High | `--packages io.delta:delta-spark_2.12:3.2.0` or the two configs; pre-mirror the jars for offline rooms |
| Notebook freezes on `.collect()` of a big DF | High | Kill in the UI; aggregate/`show` first — the M1 lesson, revisited |
| Spark UI 404 at :4040 | Medium | Port in use → UI moves to 4041+; read the "Bound SparkUI to" driver log |
| Full-lake scan instead of sample | Medium | Confirm `TRIPS_SAMPLE` path; ~4.2 GB not 180 GB |
| Plan "changes after running" confuses learners | Medium | That is AQE re-optimising at runtime; read the post-run SQL graph |
| Near-perfect AUC in Lab 5 | Medium | Leakage (`dropoff_ts`/fare/`status`); audit features against request time |
| Doubled revenue on job re-run | Medium | `append` → switch to `replaceWhere`/`MERGE`; run the idempotency test |
| JDK version mismatch / Spark won't start | Low | Install JDK 17; set `JAVA_HOME`; verify with `java -version` |
| Slow laptops on 50 M sample | Low | Use a smaller sample slice; pair on the stronger machine; managed-Spark fallback |

## Timing Recommendations

- Protect **Lab 3 (shuffle/skew)** and **Lab 4 (plan reading)** at full length — plan-reading is the newest skill and the most overrun-prone; publish checkpoint notebooks so stragglers fast-forward.
- If a cohort is strong: run one day on `masar_full` on the cluster and contrast the numbers; pull a capstone extension into main scope on Day 3.
- If a cohort is weak: shorten the Lab 4 spill-tuning task to a guided demo, but **never** drop the Lab 6 re-run/idempotency proof — it is the course's thesis made visible.
- Hard rule: capstone assembly (Day 3 H4) starts on time; kick off any full-dataset cluster run *before* the Dhuhr break so it completes while people are away.

## Discussion Prompts (use during transitions)

1. "What is the most expensive query you've seen reach production — and which module here would have caught it?"
2. "Your job finished in the same wall time but moved three times the shuffle bytes. What breaks first at full scale?"
3. "Who owns the cancellation-intervention threshold — data science, operations, or finance? What does your answer imply?"
4. "If a re-run can double your revenue numbers, is the job done? What does 'done' mean for a scheduled job?"
5. "Which of the six practices — distributed thinking, SQL/DataFrame fluency, shuffle tuning, plan reading, scalable ML, idempotent batch — would most change your team's next incident?"

## Wrap-up (Day 3 final 15 minutes)

- Map each mandatory capstone requirement back to the module that taught it (one slide): distributed correctness → M1; analytics → M2; tuning/plans → M3–M4; ML → M5; idempotent batch → M6.
- Forward pointer: **SDA-DSC-313 (Real-Time and Streaming Data Analytics)** is *this same job with a different clock* — the incremental batch you built becomes a Structured Streaming pipeline; the feature module, model, and idempotency discipline carry straight over.
- Collect: repo/notebook URLs, `BENCHMARKS.md`, `DECISIONS.md`, and the green idempotency test; issue Big-data badge recommendations within 5 working days.

---

*End of instructor package. All code samples target PySpark 3.5, Delta Lake 3.2, Python 3.11, JDK 17. Verify pinned versions and the `delta-spark` package coordinate in the course environment before each delivery. Always state whether a reported number refers to the 50 M-row sample or the 2.1 B-row full dataset.*
