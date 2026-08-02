# Data Wrangling, SQL and Exploratory Analysis
## معالجة البيانات وSQL والتحليل الاستكشافي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Data Wrangling, SQL and Exploratory Analysis |
| **Arabic Title** | معالجة البيانات وSQL والتحليل الاستكشافي |
| **Module Code** | SDA-FND-104 |
| **Level** | Practitioner |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Analysts, engineers, and scientists preparing for track-level modules |
| **Prerequisites** | SDA-FND-103 (Python) |
| **Assessment** | SQL labs; EDA project with report |
| **Stackability** | Foundation badge · Required for Data Scientist track, recommended for AI Engineer track · Counts toward the AI & Data Foundations Certificate (SDA-FND-101→105) · Next: SDA-FND-105 and role-track entry (unlocks SDA-AIE-111, SDA-DSC-111, SDA-DSC-112, SDA-DSC-214) |
| **Tools & Platforms** | SQL (PostgreSQL) · pandas · Jupyter · Matplotlib/Seaborn |

## Course Description

A practical module covering the full journey from raw data to analysis-ready insight. Participants query relational databases with SQL, clean and reshape messy datasets, engineer features, and conduct rigorous exploratory data analysis. The module instils the data-quality discipline every AI and analytics role depends on.

The course is built around a single evolving artefact: **`city_services`**, a synthetic PostgreSQL database modelled on a Saudi municipal service-request platform (940/Balady-style): 487,000 citizen service requests across 17 municipalities over three years, plus two deliberately messy CSV extracts from field operations. Participants query it with SQL on Days 1–2, diagnose and clean its messy satellites on Day 3, reshape and feature-engineer it into an analysis-ready master table on Day 4, and explore it end-to-end on Day 5 — so the final capstone (an EDA report briefed to a "deputy-minister" panel) assembles work every lab already produced. Nothing in the course is a throwaway example; every hour deepens the same dataset.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design and execute SQL queries including joins, aggregations, and window functions
2. **LO2** — Diagnose data-quality issues and implement systematic cleaning strategies
3. **LO3** — Transform and reshape datasets for analysis using pandas
4. **LO4** — Engineer meaningful features from raw structured data
5. **LO5** — Conduct exploratory data analysis to surface patterns, anomalies, and relationships
6. **LO6** — Communicate EDA findings through clear visual and written summaries

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Speaking to databases | M1: Relational Databases & SQL Fundamentals | 45% | 55% | Query notebook answering 10 single-table business questions against `city_services` |
| **Day 2** | Joining, aggregating, windowing | M2: Advanced SQL — Joins, Aggregation, Window Functions | 40% | 60% | SLA-compliance and trend queries (multi-table + windows) · graded SQL practical (PA-1) |
| **Day 3** | Data-quality discipline | M3: Data-Quality Assessment & Cleaning Workflows | 40% | 60% | Profiling report + reproducible cleaning pipeline producing `inspections_clean.parquet` with a decision log |
| **Day 4** | Reshape, merge, engineer | M4: Reshaping, Merging & Transforming Datasets · M5: Feature Engineering for Analytics & ML | 35% | 65% | Validated master table + engineered feature set with feature dictionary · graded wrangling practical (PA-2) |
| **Day 5** | Explore, explain, deliver | M6: Exploratory Data Analysis & Visual Profiling · Capstone | 25% | 75% | Complete EDA report + 10-minute briefing to assessment panel |

## Hour-by-Hour Breakdown

### Day 1 — Speaking to Databases

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why analysis fails before it starts** + course kickoff | Recognise that 60–80% of analytical effort is data preparation; tour the raw-to-ready journey; meet `city_services` and the golden thread | Interactive lecture + dataset walkthrough | 80/20 |
| 2 | **The relational model and SQL fundamentals** (M1) | Tables, keys, constraints, types; SELECT / WHERE / ORDER BY / LIMIT; NULL three-valued logic | Lecture + live psql session | 70/30 |
| 3 | **Lab 1a — First queries** | Explore the schema; answer single-table questions; read constraint definitions as documentation | Guided lab (pairs) | 10/90 |
| 4 | **Expressions, CASE, dates and strings; SQL from Jupyter** (M1) | Casting, date arithmetic, string functions, CASE; logical query execution order; parameterised queries via SQLAlchemy | Lecture + notebook demo | 60/40 |
| 5 | **Lab 1b — The query notebook** | Answer 10 business questions in a reproducible Jupyter notebook; commit as capstone input | Guided lab (pairs) | 10/90 |

### Day 2 — Joining, Aggregating, Windowing

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Joins as row-matching** (M2) | Inner/left/full joins; semi- and anti-joins; grain and fan-out discipline | Lecture + whiteboard join walkthrough | 70/30 |
| 2 | **Lab 2a — Multi-table questions** | Join requests to categories, municipalities, SLA targets; detect fan-out with row-count assertions | Guided lab | 10/90 |
| 3 | **Aggregation, GROUP BY, HAVING, CTEs** (M2) | Aggregate semantics with NULLs; conditional aggregation with FILTER; readable multi-step CTEs | Lecture + live query building | 60/40 |
| 4 | **Window functions** (M2) | ROW_NUMBER/RANK, LAG/LEAD, moving averages; PARTITION BY / ORDER BY / frames; windows vs GROUP BY | Lecture + worked patterns | 70/30 |
| 5 | **Lab 2b + PA-1 SQL practical** | SLA compliance by municipality; month-over-month trends with LAG; graded 30-minute SQL assessment | Lab + assessment | 10/90 |

### Day 3 — Data-Quality Discipline

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **The six dimensions of data quality** (M3) | Completeness, validity, consistency, uniqueness, timeliness, accuracy; quality as measurable, not aesthetic | Lecture + horror-story discussion | 70/30 |
| 2 | **Profiling and missingness** (M3) | Systematic profiling before touching anything; missingness mechanisms (MCAR/MAR/MNAR) and defensible strategies | Lecture + profiling demo | 60/40 |
| 3 | **Lab 3a — Profile the field extracts** | Produce a written profiling report on `field_inspections.csv`; quantify every defect before fixing any | Guided lab | 10/90 |
| 4 | **Cleaning as reproducible code** (M3) | Type coercion, date parsing, text normalisation (Arabic-specific issues), duplicates, sentinels; pipeline functions + validation asserts | Lecture + refactoring demo | 60/40 |
| 5 | **Lab 3b — The cleaning pipeline** | Implement `clean_inspections.py`; emit cleaned parquet + machine-readable decision log | Guided lab | 10/90 |

### Day 4 — Reshape, Merge, Engineer

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Tidy data, reshaping, and disciplined merging** (M4) | Wide vs long; melt/pivot_table; merge with `validate=` and `indicator=`; grain checks | Lecture + reshaping demo | 60/40 |
| 2 | **Lab 4 — Build the master table** | Join SQL extracts + cleaned survey data into `requests_master.parquet`; assert row counts and key uniqueness | Guided lab | 10/90 |
| 3 | **Feature engineering for analytics and ML** (M5) | Datetime/calendar features (incl. Ramadan effects), encodings, ratios, entity-history aggregates; leakage | Lecture + feature walkthrough | 70/30 |
| 4 | **Lab 5 — The feature set** | Engineer 20+ features for SLA-breach analysis; write the feature dictionary | Guided lab | 10/90 |
| 5 | **PA-2 wrangling practical + capstone briefing** | Graded 30-minute cleaning/merging assessment; capstone scenario handed out; teams plan their EDA questions | Assessment + briefing | 20/80 |

### Day 5 — Explore, Explain, Deliver

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **EDA as a disciplined loop; visual profiling** (M6) | Question → evidence → interpretation → next question; univariate/bivariate/temporal profiling patterns | Lecture + live EDA | 60/40 |
| 2 | **Lab 6 — Guided EDA sprint** | Surface five defensible findings from the master table with appropriate plots | Guided lab | 10/90 |
| 3 | **Communicating findings** (M6) + capstone work | Chart integrity, insight statements vs chart dumps, report structure; teams draft their reports | Micro-lecture + project work | 30/70 |
| 4 | **Capstone assembly** | Finalise notebook, report, and briefing deck; peer review round against the rubric | Project work | 0/100 |
| 5 | **Capstone briefings + assessment + wrap-up** | 10-minute panel briefings; rubric scoring; path to SDA-FND-105 and role tracks | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module works the same `city_services` dataset. Never substitute toy datasets (iris, titanic) — the continuity is what makes Day 5's capstone assembly achievable and what teaches the compounding cost of early sloppiness.
- **Pace control:** Labs 2b and 4 are the most overrun-prone. Publish checkpoint notebooks and solution scripts (`lab1-solution.ipynb` … `lab6-solution.ipynb`) in the course repository so stragglers can fast-forward without losing the thread.
- **Pairing:** rotate pairs daily. Pair SQL-experienced participants with pandas-experienced ones on Days 1–2 and reverse the favour on Days 3–4; the skill transfer is the point.
- **Environment strategy:** primary = local Docker container running PostgreSQL 16 pre-loaded with `city_services` (one `docker compose up`, no DBA skills needed); fallback = hosted instance on the classroom network + JupyterHub. Verify both the week before delivery.
- **Language:** deliver in English or Arabic; keep all code, column names, and query text in English (production convention in Saudi enterprise environments), but keep the Arabic text columns (`name_ar`, districts) in the data — handling real Arabic text is a designed learning outcome, not an accident.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 5 afternoon is deliberately light on new theory.
- **Assessment logistics:** PA-1 (Day 2 H5) and PA-2 (Day 4 H5) are individually graded, closed-notes, open-documentation. Collect capstone repositories at the end of Day 5 H4 so notebooks can be spot-run before briefings begin.

---

# Module 1 — Relational Databases and SQL Fundamentals

## Module Overview

**Purpose.** Almost every dataset an analyst will ever touch begins life in a relational database, and the single highest-leverage skill in the data profession is asking that database precise questions. This module builds correct mental models — tables as sets of rows with declared types and constraints, NULL as "unknown" rather than "zero", queries as declarative descriptions of results — and makes participants fluent in single-table SQL before the joins of Module 2 raise the stakes.

**Business relevance.** Saudi organisations run their operational truth on relational systems: core banking, hospital information systems, ERP at industrial firms, and the government service platforms behind national portals. Analysts who cannot self-serve with SQL queue behind overloaded engineering teams for every question — a wait measured in days. Analysts who can, answer in minutes and become the person leadership calls first. SQL is also the lingua franca of every downstream tool this academy teaches, from warehouse modules (SDA-DSC-214) to ML pipelines.

**Industry use cases.**
- A municipal operations manager asks "how many high-priority streetlight requests are still open in the Eastern Region?" — a 6-line query, if someone in the room can write it.
- A hospital quality team pulls monthly admission counts by department directly from the HIS reporting replica instead of waiting for the vendor's quarterly extract.
- A bank analyst filters three years of transactions to a suspicious merchant-category slice in seconds, because the WHERE clause runs where the data lives instead of downloading 40 GB to a laptop.

**Expected competencies.** After this module a participant can read a schema and its constraints as documentation, write SELECT queries with filtering, sorting, expressions, CASE logic and date/string functions, reason correctly about NULL, and run parameterised SQL from a Jupyter notebook into a pandas DataFrame.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain the relational model: tables, rows, keys, constraints, and types as a data-quality contract | LO1, LO2 |
| 1.2 | Write single-table queries with SELECT, WHERE, ORDER BY, LIMIT, and DISTINCT | LO1 |
| 1.3 | Reason correctly about NULL and three-valued logic in filters and expressions | LO1, LO2 |
| 1.4 | Use casts, date arithmetic, string functions, and CASE to compute derived columns | LO1 |
| 1.5 | Run parameterised SQL from Jupyter into pandas safely (no string-formatted SQL) | LO1, LO3 |

## Technical Content

### 1. The relational model as a quality contract

A relational table is not "a spreadsheet in a server". It is a set of rows conforming to a declared schema — and every declaration is a promise the database *enforces*:

- **Types** (`integer`, `numeric(10,2)`, `text`, `timestamptz`, `boolean`) reject wrong-shaped data at write time. A `timestamptz` column cannot contain `"31/02/2024"`; a CSV column happily can. Half of Module 3's cleaning pain exists precisely because CSVs have no types.
- **Primary keys** guarantee row identity: `request_id` is unique and non-null, so counting requests is meaningful.
- **Foreign keys** guarantee referential integrity: every `requests.category_id` exists in `categories`. When participants meet orphaned codes in the messy CSVs later, they will understand what protection was lost at export.
- **NOT NULL and CHECK constraints** encode business rules (`priority BETWEEN 1 AND 4`, `satisfaction_score BETWEEN 1 AND 5`).

**Instructor note:** open the `city_services` schema with `\d requests` and read the constraints aloud as *documentation written by the engineering team to the analyst*. This framing — constraints as messages, not obstacles — pays off all week.

The course schema (memorise the grain of each table; grain errors are the root of most wrong answers this week):

| Table | Grain (one row =) | Rows | Key columns |
|---|---|---|---|
| `requests` | one citizen service request | 487,000 | request_id PK; citizen_id, category_id, municipality_id FKs; opened_at, closed_at, status, priority, channel, satisfaction_score, reopened_count |
| `citizens` | one registered (anonymised) citizen | 92,000 | citizen_id PK; district, city, registered_at |
| `categories` | one request category | 46 | category_id PK; name_en, name_ar, department |
| `municipalities` | one municipality | 17 | municipality_id PK; city, region, population |
| `sla_targets` | one category × priority SLA rule | 184 | (category_id, priority) PK; target_hours |
| `assignments` | one crew assignment to a request | 512,000 | assignment_id PK; request_id FK; crew_id, assigned_at, completed_at |

### 2. Anatomy of a query: written order vs logical order

SQL is declarative: you describe the result, the engine decides how. But the *logical* evaluation order differs from the written order, and knowing it dissolves the two most common beginner confusions:

```
Written:   SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT
Logical:   FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

Consequences worth stating explicitly:

- A column alias defined in SELECT (`AS resolution_hours`) is not visible in WHERE (WHERE runs first) but is visible in ORDER BY (which runs after SELECT) — in PostgreSQL.
- LIMIT is applied *last*: `LIMIT 100` does not make the WHERE cheaper; it truncates the answer. `LIMIT` is a display tool, never a sampling tool — a limited result with no ORDER BY is *arbitrary*, and arbitrary is not random (a lesson that returns in Module 6's sampling discussion).
- DISTINCT applies to the entire selected row, not the first column.

### 3. NULL: the honest unknown

NULL means *unknown or inapplicable*, and it propagates: `NULL + 1` is NULL, `NULL = NULL` is NULL (not true), and a WHERE clause keeps only rows evaluating to *true* — so `WHERE satisfaction_score != 5` silently drops every unrated request. The class must internalise:

- Test with `IS NULL` / `IS NOT NULL`, never `= NULL`.
- `COUNT(*)` counts rows; `COUNT(satisfaction_score)` counts non-null values — the difference *is* the completeness metric used in Module 3.
- `COALESCE(closed_at, now())` substitutes a value; use deliberately and comment why.
- Aggregates ignore NULLs (`AVG(satisfaction_score)` averages the rated subset only — is that the number leadership thinks it is getting? This exact ambiguity appears in the capstone dataset by design).

In `city_services`, `closed_at IS NULL` means the request is still open, and `satisfaction_score IS NULL` means the citizen never answered the survey — two different *kinds* of missing that Module 3 will name MAR and MNAR.

### 4. Expressions, dates, strings, and CASE

Derived columns move the computation to the data:

- **Casting:** `population::numeric`, `opened_at::date`. Integer division bites: `4/8` is `0`; write `4::numeric/8`.
- **Date arithmetic:** `closed_at - opened_at` yields an interval; `EXTRACT(EPOCH FROM closed_at - opened_at)/3600.0` yields resolution hours — the course's most reused expression. `date_trunc('month', opened_at)` is the idiom for monthly rollups (Module 2 uses it constantly).
- **Strings:** `lower()`, `trim()`, `split_part()`, `left()`, `||` concatenation, `LIKE`/`ILIKE` patterns. PostgreSQL handles Arabic text natively (UTF-8); `ILIKE` on `name_ar` works, and demonstrating a bilingual query early normalises Arabic data as first-class.
- **CASE** encodes business logic readably:

```sql
CASE
  WHEN priority = 1 THEN 'urgent'
  WHEN priority = 2 THEN 'high'
  ELSE 'routine'
END AS priority_band
```

CASE inside aggregates previews Module 2's conditional aggregation and gives participants an early "I can compute a KPI" win.

### 5. SQL from Jupyter: the analyst's production posture

The course's working posture from Hour 4 onward: heavy filtering and aggregation happen *in the database*; pandas receives the already-reduced result. The pattern:

```python
df = pd.read_sql(text(query), engine, params={...})
```

Three rules enforced all week:

1. **Parameterise, never format.** f-string SQL is an injection vulnerability and a quoting bug factory. `text("... WHERE region = :region")` with `params` is the only accepted form — even in "just a notebook", because notebooks become production with depressing regularity.
2. **Push filters down.** `SELECT *` on 487k rows then filtering in pandas wastes memory and network and hides intent; the lab benchmarks make the cost visible (8× wall-clock difference on the classroom setup).
3. **Queries live in named variables or `.sql` files,** not inline string soup — they are code, they get reviewed.

### 6. Common mistakes & production considerations

1. `WHERE score != 5` silently excluding NULLs — the classic three-valued-logic trap (planted in Lab 1b question 7).
2. `SELECT *` in saved analysis code — schema changes upstream silently change your analysis; name your columns.
3. Using LIMIT without ORDER BY and treating the result as "a sample".
4. Integer division producing zeros in rate calculations.
5. Filtering timestamps with `opened_at = '2025-03-01'` (matches midnight only) instead of half-open ranges `>= '2025-03-01' AND < '2025-04-01'` — half-open ranges are the course standard; they compose without gaps or double-counting.
6. String-formatted SQL with user-supplied values (injection; also breaks on the first Arabic apostrophe).

Production considerations: analysts read from **read replicas**, not the operational primary — a runaway analytical query on the primary is a service incident. Long-running queries should be tested with LIMIT during development but *finalised without it*. Every saved query should state its grain and its time window in a comment header — future-you is the first consumer.

## Code Examples

### Schema exploration (psql and information_schema)

```sql
-- labs/day1/explore_schema.sql
-- Orientation queries: run these before writing ANY analysis query.

-- What tables exist?
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

-- What does requests look like? (psql shortcut: \d requests)
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'requests'
ORDER BY ordinal_position;

-- How big, and over what period? Cheap sanity anchors for every later result.
SELECT
    count(*)                              AS n_requests,
    min(opened_at)                        AS first_request,
    max(opened_at)                        AS last_request,
    count(*) FILTER (WHERE closed_at IS NULL) AS still_open
FROM requests;
```

### Single-table business questions

```sql
-- labs/day1/q05_urgent_backlog.sql
-- Grain: one row per open urgent request. Window: all time.
-- Question: what does the urgent backlog look like, oldest first?
SELECT
    request_id,
    opened_at,
    round(EXTRACT(EPOCH FROM now() - opened_at) / 3600.0 / 24, 1) AS age_days,
    channel,
    municipality_id
FROM requests
WHERE status IN ('open', 'in_progress')
  AND priority = 1
ORDER BY opened_at ASC
LIMIT 50;
```

```sql
-- labs/day1/q08_channel_mix.sql
-- Grain: one row per channel. Window: 2025 only (half-open range).
SELECT
    channel,
    count(*)                                   AS n_requests,
    round(100.0 * count(*) / sum(count(*)) OVER (), 1) AS pct_of_total,
    round(avg(satisfaction_score), 2)          AS avg_satisfaction,   -- rated subset only!
    count(*) - count(satisfaction_score)       AS unrated
FROM requests
WHERE opened_at >= '2025-01-01' AND opened_at < '2026-01-01'
GROUP BY channel
ORDER BY n_requests DESC;
```

### CASE for business bands

```sql
-- labs/day1/q10_resolution_bands.sql
-- Resolution-time banding for closed requests in 2025.
SELECT
    CASE
        WHEN closed_at - opened_at <= interval '24 hours'  THEN '1. within 24h'
        WHEN closed_at - opened_at <= interval '72 hours'  THEN '2. 1-3 days'
        WHEN closed_at - opened_at <= interval '168 hours' THEN '3. 3-7 days'
        ELSE                                                    '4. over a week'
    END AS resolution_band,
    count(*) AS n_requests
FROM requests
WHERE closed_at IS NOT NULL
  AND opened_at >= '2025-01-01' AND opened_at < '2026-01-01'
GROUP BY resolution_band
ORDER BY resolution_band;
```

### Parameterised SQL from Jupyter into pandas

```python
# notebooks/day1_queries.ipynb (exported cell)
"""Course-standard database access pattern.

Rules:
1. Parameterise (:name) — NEVER f-strings into SQL.
2. Push filters/aggregation into the database.
3. State grain + window in the query comment.
"""
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg://analyst:***@localhost:5432/city_services")

MONTHLY_BY_REGION = text("""
    -- Grain: one row per (month, region). Window: parameterised.
    SELECT
        date_trunc('month', r.opened_at)::date AS month,
        m.region,
        count(*) AS n_requests
    FROM requests r
    JOIN municipalities m USING (municipality_id)
    WHERE r.opened_at >= :start AND r.opened_at < :end
    GROUP BY 1, 2
    ORDER BY 1, 2
""")

monthly = pd.read_sql(MONTHLY_BY_REGION, engine,
                      params={"start": "2024-01-01", "end": "2026-01-01"})
monthly.head()
#        month   region  n_requests
# 0 2024-01-01  Eastern        4211
# 1 2024-01-01   Makkah        6870
# ...
```

## Hands-on Lab 1 — Interrogate the Service Database

| | |
|---|---|
| **Objective** | Explore the `city_services` schema and answer 10 business questions with single-table SQL, delivered as a reproducible query notebook |
| **Duration** | 2 × 50 min (Day 1 H3 + H5) |
| **Setup** | `docker compose up -d db` (pre-loaded PostgreSQL 16); `pip install pandas sqlalchemy psycopg[binary] jupyter`; connection string on the board |
|

**Part A tasks (50 min — psql / SQL client)**
1. *(10 min)* Orientation: list tables, describe `requests`, run the sanity-anchor query (row count, date range, open count). Write the three numbers on paper — they are your lie detectors for the rest of the course.
2. *(10 min)* Read the constraints on `requests` and `sla_targets`; write one sentence per constraint stating the business rule it encodes.
3. *(25 min)* Answer questions 1–6 (provided sheet): request counts by status; urgent backlog aged oldest-first; busiest municipality by ID; 2025 channel mix; distinct departments; requests opened during Ramadan 1446 (date range provided).
4. *(5 min)* Peer-check: swap with your pair; verify each answer against the sanity anchors.

**Part B tasks (50 min — Jupyter)**
1. *(10 min)* Stand up the SQLAlchemy engine; re-run question 4 through `pd.read_sql` with parameters.
2. *(25 min)* Answer questions 7–10 in the notebook: unrated-request share (the NULL trap), resolution-time bands (CASE), month-of-year seasonality of `opened_at`, top-10 longest-open current requests.
3. *(10 min)* Add a markdown header per question: the question in plain language, grain, window, and one-sentence answer.
4. *(5 min)* Commit: `lab1: single-table query notebook`.

**Expected outputs**
```
Sanity anchors: 487,000 requests | 2023-01-02 → 2025-12-30 | 31,842 still open
Q7: 41.2% of closed 2025 requests have no satisfaction score
    (WHERE score != 5 gives 122,304 — WRONG; correct exclusion-aware count: 208,116)
Q9: clear Ramadan dip + summer peak visible in monthly counts
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `connection refused` | DB container not up / wrong port | `docker compose ps`; confirm 5432 mapping |
| Q7 count "too clean" | `!= 5` dropped NULLs silently | Add `OR satisfaction_score IS NULL`; discuss three-valued logic |
| `UndefinedColumn: resolution_hours` in WHERE | Alias used before SELECT runs | Repeat the expression or use a subquery/CTE |
| All-zero rates | Integer division | Cast one operand `::numeric` |
| Arabic text shows as `???` | Client encoding not UTF-8 | `SET client_encoding TO 'UTF8';` verify terminal font |

**Instructor notes.** Question 7 is the designed failure: roughly two-thirds of pairs will fall into the `!= 5` NULL trap. Let them; then reveal the discrepancy against the sanity anchor on the projector — the lesson lands ten times harder after a wrong answer they were confident in. Fast finishers: rewrite Q10 using a CTE, previewing Day 2.

## Mini Exercises

**Quiz (5 questions)**
1. `WHERE satisfaction_score != 5` — which rows are excluded? → score = 5 rows **and** all NULL-score rows.
2. `COUNT(*)` vs `COUNT(closed_at)` on `requests` — what is the difference, in business terms? → total requests vs closed requests; the gap is the open backlog.
3. Why is `LIMIT 1000` without ORDER BY not a sample? → row order is arbitrary (storage/plan dependent), so the subset is biased in unknowable ways.
4. Write the half-open range predicate for "March 2025". → `opened_at >= '2025-03-01' AND opened_at < '2025-04-01'`.
5. True/False: a PRIMARY KEY column can contain one NULL. → **False** (unique + not null).

**Debugging exercise.** A provided query claims to compute "average resolution days by priority" but returns identical values for all priorities — the `4/24` integer-division bug plus a missing `closed_at IS NOT NULL` filter. Participants must find both defects.

**Code-review exercise.** Review `review_me_module1.sql`: `SELECT *`, f-string parameterisation (shown in an accompanying notebook cell), `= NULL`, LIMIT-as-sample, and no grain comment. Five findings expected; compare against the model review.

**Discussion questions.**
- The engineering team offers you either (a) read access to the replica or (b) a weekly CSV export. Argue the data-quality case for (a) using constraint enforcement.
- When is computing in SQL better than pandas, and where is the line? (Volume reduction, single source of truth vs statistical tooling, visualisation.)

## Case Study — Self-Service Analytics at a National Open-Data Programme

**Scenario.** A government open-data office (modelled on national portal programmes) publishes municipal datasets as CSV extracts. Internally, its analysts answer ministerial questions from the same source systems. A new deputy-ministry request — "open urgent requests older than 30 days, by region, today" — takes the team four days: the CSV pipeline runs weekly, and the one analyst with database access is on leave.

**Business context.** The office's charter promises 48-hour turnaround on ministerial data requests. Missing it repeatedly triggered an internal review; the review found the bottleneck was not tooling budget but *SQL literacy concentrated in one person*.

**Technical challenge.** Design the team's self-service posture: who gets read access to what, with which guardrails, and what minimum SQL competency baseline.

**Constraints.** PDPL applies — citizen-identifying columns must not be broadly readable; the replica serves other teams (runaway queries are a shared-resource incident); analysts are Excel-strong, SQL-weak; the source schema changes quarterly.

**Solution approach (facilitate, don't lecture).** Read-only role on the replica scoped to a curated schema of views (identifying columns excluded — PDPL by construction); statement timeout of 60 s on the analyst role; the ten most-asked ministerial questions codified as reviewed, commented `.sql` files in a shared repository; a two-day internal SQL bootcamp (this module, compressed) as the competency baseline; schema-change notes routed to the analyst channel.

**Discussion questions.**
1. Which specific guardrail addresses each constraint? Map them one-to-one.
2. Why are *views* the right PDPL boundary rather than "please don't select those columns"?
3. The weekly CSV pipeline still exists for external publication. What quality checks should run on the export, given what constraints the CSV loses? (Foreshadows Module 3.)
4. What belongs in the query repository's review checklist? Draft five items.

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Lab 1 questions answered correctly | Correctness | ≥ 8 / 10 | answer key |
| Sanity-anchor discipline | Method | anchors recorded + cited on ≥ 2 answers | notebook review |
| NULL-trap question (Q7) | Correctness | correct *after* class debrief, 100% | re-submission |
| Filter pushdown | Performance | DB-side filter ≥ 5× faster than fetch-all-then-filter | timed cells in lab notebook |
| Parameterised queries | Code quality | 0 f-string SQL in committed notebook | grep + review |
| Query documentation | Communication | grain + window comment on 10/10 queries | review checklist |

**Example benchmark table (filled during lab):**

| Approach | Rows transferred | Wall clock | Peak notebook memory |
|---|---|---|---|
| `SELECT *` then pandas filter | 487,000 | 14.2 s | 610 MB |
| WHERE + aggregation in DB | 36 | 1.7 s | 22 MB |

## Required Visuals and Training Assets

### Diagrams
1. **`city_services` entity-relationship diagram** — *Purpose:* the course's anchor image; posted on the wall all week. *Elements:* six tables as boxes with column lists, PK/FK notation, crow's-foot relationships; grain stated under each table name ("one row = one request"); row counts as badges. *Style:* clean ERD, one accent colour per table reused in all later diagrams. *Designer note:* label both English and Arabic names on `categories` to signal bilingual data is first-class.
2. **Written order vs logical order of a query** — *Elements:* two parallel columns of clause keywords connected by crossing arrows; callouts at the two confusion points (alias visibility, LIMIT-last). *Style:* simple two-column flow, printable A5 for desks.
3. **Three-valued logic truth table poster** — *Elements:* TRUE/FALSE/NULL truth tables for AND, OR, NOT; a red banner "WHERE keeps only TRUE". *Style:* reference card.
4. **Half-open date-range motif** — *Elements:* timeline with `[ )` brackets showing March fully covered, April excluded, no midnight gap; a crossed-out `BETWEEN` variant double-counting a boundary. *Style:* number-line diagram.

### Images (screenshots)
1. **psql `\d requests` output** — *why:* constraint-reading exercise reference; *content:* full table description with FKs and CHECKs visible.
2. **Jupyter cell with `pd.read_sql` + params and its DataFrame result** — *why:* the course-standard access pattern, verbatim; *content:* exact code from the example, result head.
3. **The Q7 trap, before and after** — *why:* the module's money shot; *content:* two cells side by side, wrong count vs corrected count with `IS NULL` handling, difference highlighted.
4. **pgAdmin/DBeaver ERD auto-view** — *why:* participants verify their mental model; *content:* the six tables with relationship lines.

### Simulations
1. **The silent NULL drop** — *Setup:* Lab 1b Q7 as designed. *Expected behaviour:* confident wrong answers, detected via sanity anchors. *Learning objective:* three-valued logic; anchor-checking as a habit.
2. **Runaway query** — *Setup:* instructor runs an unfiltered cross-join style query against the classroom DB with the analyst role's 60 s statement timeout active. *Expected:* query cancelled by timeout with a clear error. *Learning objective:* shared-resource citizenship; why replicas and timeouts exist.

### Interactive Activities
- **Constraint archaeology (15 min):** pairs receive the DDL of `sla_targets` and `requests` and write the business rulebook it implies; compare against the "official" rulebook — every mismatch is a discussion point.
- **Query telephone (10 min):** one participant states a business question in words; their pair writes the SQL; a third pair back-translates the SQL to words. Divergences reveal ambiguity (usually the time window or grain).

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `city_services` DB | Synthetic, generated by course tooling (request patterns calibrated to realistic municipal seasonality: Ramadan dip, summer peak, salary-day bumps) | PostgreSQL dump | 487k requests + satellites | Golden thread, all modules |
| Question sheet Q1–Q10 | Course repo | MD | 1 page | Lab 1 |
| `docker-compose.yml` (db service) | Course repo | YAML | — | One-command environment |

### Demo Requirements
- **Instructor demo:** live psql session from `\dt` to the channel-mix query, narrating each clause; then the same query from Jupyter with parameters — the point is the *identical* SQL in both worlds.
- **Student demo:** two pairs present one question each at end of Hour 5, stating grain and window before showing SQL.
- **Expected outputs:** committed query notebook with 10 documented answers; sanity anchors recorded.

---

# Module 2 — Advanced SQL: Joins, Aggregation, Window Functions

## Module Overview

**Purpose.** Real questions rarely live in one table: "SLA compliance by municipality" needs `requests`, `sla_targets`, and `municipalities`; "month-over-month change" needs a row to see its neighbour. This module makes participants dangerous in the best way: fluent joins with grain discipline, honest aggregation, readable CTE pipelines, and window functions — the single highest-leverage SQL skill for analytics — all while learning to *distrust and verify* their own row counts.

**Business relevance.** The difference between a junior and a senior analyst is rarely syntax; it is whether their numbers can be trusted. Fan-out from a careless join silently double-counts revenue; a NULL-blind average flatters a KPI; a mis-partitioned window mixes municipalities. In Saudi enterprises reporting to boards and regulators (SAMA-supervised banks, sector regulators, ministry dashboards), a wrong aggregate in a briefing is a credibility event. This module teaches the verification habits that prevent it.

**Industry use cases.**
- A ministry dashboard team computes SLA-breach rates per municipality per month — a three-table join with conditional aggregation, refreshed nightly.
- A bank's fraud analysts use `LAG` over card transactions partitioned by customer to compute time-since-last-transaction, the classic velocity signal.
- A telecom capacity planner ranks cell sites by 7-day moving-average load with window frames to schedule upgrades before congestion, not after.

**Expected competencies.** Participants can choose and verify the correct join type, detect and fix fan-out, aggregate with GROUP BY/HAVING/FILTER correctly under NULLs, structure multi-step logic with CTEs, apply ROW_NUMBER/RANK/LAG/LEAD and moving aggregates with correct PARTITION/ORDER/frame clauses, and read an EXPLAIN plan well enough to know when to ask for an index.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Select and implement the correct join type (inner, left, semi, anti) for a business question | LO1 |
| 2.2 | Detect and prevent join fan-out using grain reasoning and row-count assertions | LO1, LO2 |
| 2.3 | Aggregate correctly with GROUP BY, HAVING, and FILTER, accounting for NULL semantics | LO1 |
| 2.4 | Compose multi-step analyses as readable CTE pipelines | LO1, LO6 |
| 2.5 | Apply window functions (ranking, offset, moving aggregates) with correct partitions and frames | LO1 |
| 2.6 | Use EXPLAIN to distinguish a slow query from a wrong one | LO1 |

## Technical Content

### 1. Joins as row-matching, not table-gluing

A join is a rule for matching rows. Teach each type as the business question it answers on `city_services`:

| Join | Business question | Example |
|---|---|---|
| **INNER** | "requests *and* their category details" — only matches survive | requests × categories for department rollups |
| **LEFT** | "all requests, with satisfaction callbacks *where they exist*" — left side is sacred | requests × callbacks; NULLs mark no-callback |
| **FULL** | "everything from both sides, matched where possible" — reconciliation | comparing two extract versions |
| **Semi (EXISTS)** | "requests that *have* at least one assignment" — no columns needed from the other side, no fan-out possible | `WHERE EXISTS (SELECT 1 FROM assignments a WHERE a.request_id = r.request_id)` |
| **Anti (NOT EXISTS)** | "requests with *no* assignment" — the orphan hunter | quality checks; Module 3 reuses this pattern in pandas as `indicator=True` |

Two rules the class repeats aloud: **know the grain of both sides before joining**, and **a LEFT JOIN filtered in WHERE on the right side silently becomes an INNER JOIN** (`WHERE c.department = 'Roads'` drops the NULL rows LEFT was preserving — move the condition into `ON`, or accept that you meant INNER).

### 2. Fan-out: the silent multiplier

`requests` is 1:many with `assignments` (avg 1.05, max 4 assignments per request). Join them and count "requests": you get 512,000, not 487,000 — a 5% inflation that survives into every downstream percentage. Fan-out is the most expensive SQL mistake in industry because it *runs successfully*.

Defences, in course-mandated order:
1. **State the output grain before writing the query.** "One row per request" → any join to `assignments` needs pre-aggregation (`GROUP BY request_id` in a CTE) or `EXISTS`.
2. **Assert row counts.** `count(*)` before and after the join; equal counts or explained growth. In notebooks: `assert len(df) == n_requests`.
3. **Check key cardinality when unsure:** `SELECT request_id, count(*) FROM assignments GROUP BY 1 HAVING count(*) > 1 LIMIT 5`.

This discipline transfers verbatim to pandas `merge(validate="one_to_many")` in Module 4 — say so now; the repetition is designed.

### 3. Honest aggregation

- `GROUP BY` defines the output grain; every selected non-aggregate column must be in it (PostgreSQL enforces this — appreciate the error).
- **HAVING filters groups; WHERE filters rows.** WHERE runs before grouping, so it is cheaper — filter early, group late.
- **Aggregates ignore NULL:** `avg(satisfaction_score)` is the mean of the *rated*. If rating propensity correlates with experience (it does — angry citizens rate more), the average is biased. The honest report shows the metric *and its coverage*: `count(score)::numeric / count(*) AS response_rate`.
- **Conditional aggregation** builds entire KPI tables in one pass:

```sql
count(*) FILTER (WHERE breach)             AS n_breached,
round(100.0 * count(*) FILTER (WHERE breach) / count(*), 1) AS breach_pct
```

`FILTER` is PostgreSQL's readable form of `SUM(CASE WHEN … THEN 1 ELSE 0 END)`; teach both, prefer FILTER.

### 4. CTEs: SQL you can review

`WITH` names intermediate results and turns a page of nested subqueries into a readable pipeline: *resolve → compare to SLA → aggregate*. Course style rules: one logical step per CTE; CTE names are nouns describing their grain (`closed_requests`, `request_sla`, `monthly_breach`); the final SELECT is boring. A CTE pipeline is also a *debugging* structure — `SELECT * FROM request_sla LIMIT 20` inspects any stage. Note for honesty: CTEs in modern PostgreSQL (12+) are inlined by the planner unless `MATERIALIZED` is specified, so readability costs nothing.

### 5. Window functions: aggregates that keep the rows

`GROUP BY` collapses rows; a window function computes over a group *while every row survives*. Anatomy: `func() OVER (PARTITION BY … ORDER BY … ROWS BETWEEN …)`.

The four patterns that cover 90% of analytical use:

1. **Ranking / top-N-per-group:** `ROW_NUMBER() OVER (PARTITION BY municipality_id ORDER BY n DESC)` then `WHERE rn <= 3` in the outer query — "top 3 categories per municipality", unanswerable with GROUP BY alone. Teach ROW_NUMBER vs RANK vs DENSE_RANK with a tie example.
2. **Offset:** `LAG(n_requests) OVER (PARTITION BY region ORDER BY month)` — month-over-month change, time-since-previous-event. LAG at the wrong grain (forgotten PARTITION) is the window equivalent of fan-out: the first row of each region sees the *previous region's* last value.
3. **Moving aggregates:** `avg(n) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` — the 7-day smoothing used in every operations dashboard. Distinguish `ROWS` (physical rows) from `RANGE` (value-based); with gaps in dates, ROWS over a date-complete series (or RANGE) is the correct choice — a planted lab bug makes this concrete.
4. **Share-of-total:** `count(*) / sum(count(*)) OVER ()` — window over an aggregate, the idiom from Lab 1's channel mix, now formally explained.

Logical placement: windows evaluate *after* WHERE/GROUP BY/HAVING, *before* ORDER BY/LIMIT — hence you cannot filter on a window function directly; wrap in a CTE and filter outside (the "top-N idiom").

### 6. Performance literacy & common mistakes

Not a tuning course — but analysts must distinguish *slow* from *wrong* and file useful requests:

- `EXPLAIN (ANALYZE, BUFFERS)` reads: Seq Scan vs Index Scan, estimated vs actual rows (a 100× estimate error means stale statistics or a misunderstood predicate).
- Indexes serve WHERE and JOIN keys; `city_services` ships with indexes on FKs and `opened_at` — the lab measures one query with and without.
- Functions on the *filtered column* defeat indexes: `WHERE date_trunc('month', opened_at) = …` scans; the half-open range on the raw column uses the index. (The Module 1 habit, now with a performance justification.)

**Common mistakes:** (1) LEFT JOIN + right-side WHERE = accidental INNER; (2) fan-out double counting; (3) forgetting PARTITION BY in LAG; (4) filtering a window function in WHERE instead of the CTE idiom; (5) `count(DISTINCT …)` as a fan-out band-aid — it fixes the count and leaves every `sum()` in the query still wrong; (6) HAVING conditions that belong in WHERE, scanning far more than needed. Production: nightly KPI queries live in version control with tests (golden rows); dashboards read from summary tables, not 487k-row scans per page load.

## Code Examples

### The SLA-compliance pipeline (CTEs + conditional aggregation)

```sql
-- labs/day2/sla_compliance.sql
-- Grain: one row per (municipality, month). Window: 2025.
-- Business definition of breach: resolution time exceeds target_hours
-- for the request's category & priority. Open requests excluded (see D1).
WITH closed_requests AS (
    SELECT
        request_id, municipality_id, category_id, priority,
        date_trunc('month', opened_at)::date AS month,
        EXTRACT(EPOCH FROM closed_at - opened_at) / 3600.0 AS resolution_hours
    FROM requests
    WHERE closed_at IS NOT NULL
      AND opened_at >= '2025-01-01' AND opened_at < '2026-01-01'
),
request_sla AS (
    SELECT
        cr.*,
        s.target_hours,
        cr.resolution_hours > s.target_hours AS breach
    FROM closed_requests cr
    JOIN sla_targets s USING (category_id, priority)   -- 1:1 by design: verify!
),
monthly AS (
    SELECT
        m.city, m.region, r.month,
        count(*)                                        AS n_closed,
        count(*) FILTER (WHERE breach)                  AS n_breached,
        round(100.0 * count(*) FILTER (WHERE breach) / count(*), 1) AS breach_pct
    FROM request_sla r
    JOIN municipalities m USING (municipality_id)
    GROUP BY m.city, m.region, r.month
)
SELECT * FROM monthly ORDER BY breach_pct DESC;
```

### Fan-out detection and the pre-aggregation fix

```sql
-- labs/day2/fanout_demo.sql
-- WRONG: grain says "one row per request" but the join says otherwise.
SELECT count(*) FROM requests r JOIN assignments a USING (request_id);
-- 512,347  ← inflated: 25,347 requests have >1 assignment

-- RIGHT: collapse assignments to request grain FIRST.
WITH assignment_stats AS (
    SELECT request_id,
           count(*)          AS n_assignments,
           min(assigned_at)  AS first_assigned_at
    FROM assignments
    GROUP BY request_id
)
SELECT count(*)
FROM requests r
LEFT JOIN assignment_stats a USING (request_id);
-- 487,000  ← grain preserved; unassigned requests kept by LEFT
```

### Top-N per group and month-over-month (window patterns)

```sql
-- labs/day2/top3_categories.sql
-- Top 3 request categories per municipality, 2025.
WITH counts AS (
    SELECT municipality_id, category_id, count(*) AS n
    FROM requests
    WHERE opened_at >= '2025-01-01' AND opened_at < '2026-01-01'
    GROUP BY 1, 2
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY municipality_id
                              ORDER BY n DESC, category_id) AS rn
    FROM counts
)
SELECT m.city, c.name_en, r.n
FROM ranked r
JOIN municipalities m USING (municipality_id)
JOIN categories     c USING (category_id)
WHERE r.rn <= 3                     -- window filtered OUTSIDE the window CTE
ORDER BY m.city, r.rn;
```

```sql
-- labs/day2/mom_change.sql
-- Month-over-month change per region; note the PARTITION BY — without it,
-- January of one region "inherits" December of the previous region.
WITH monthly AS (
    SELECT m.region,
           date_trunc('month', r.opened_at)::date AS month,
           count(*) AS n
    FROM requests r
    JOIN municipalities m USING (municipality_id)
    GROUP BY 1, 2
)
SELECT region, month, n,
       n - LAG(n) OVER (PARTITION BY region ORDER BY month)           AS delta,
       round(100.0 * (n - LAG(n) OVER (PARTITION BY region ORDER BY month))
             / NULLIF(LAG(n) OVER (PARTITION BY region ORDER BY month), 0), 1)
                                                                      AS pct_change,
       round(avg(n) OVER (PARTITION BY region ORDER BY month
                          ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 0)
                                                                      AS ma_3mo
FROM monthly
ORDER BY region, month;
```

### Windowed extract into pandas (bridge to Day 3)

```python
# notebooks/day2_trends.ipynb (exported cell)
"""Pull the windowed trend table and plot it — the first Matplotlib
moment of the course, deliberately trivial: SQL did the hard part."""
import matplotlib.pyplot as plt

trend = pd.read_sql(MOM_CHANGE_QUERY, engine)          # query from mom_change.sql
fig, ax = plt.subplots(figsize=(10, 4))
for region, grp in trend.groupby("region"):
    ax.plot(grp["month"], grp["ma_3mo"], label=region)
ax.set_title("Service requests — 3-month moving average by region")
ax.set_ylabel("requests / month")
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
```

## Hands-on Lab 2 — SLA Analytics with Joins and Windows

| | |
|---|---|
| **Objective** | Produce the SLA-compliance table, fan-out proof, top-3 categories per municipality, and MoM trend queries — each with a stated grain and a row-count assertion |
| **Duration** | 2 × 50 min (Day 2 H2 + H5 first half) |
| **Setup** | Day 1 environment; `labs/day2/` question sheet; solutions tagged `lab2-solution` |

**Part A tasks (50 min)**
1. *(10 min)* Fan-out proof: run the naive `requests × assignments` count, explain the inflation in one written sentence, then fix with pre-aggregation. Keep both queries — the pair is your evidence artefact.
2. *(15 min)* Build `sla_compliance.sql` stepwise, `SELECT`-ing from each CTE as you go; assert the `request_sla` CTE has exactly as many rows as `closed_requests` (the 1:1 join verified, not assumed).
3. *(15 min)* Anti-join hunt: find requests with no assignment (`NOT EXISTS`) and closed requests missing an SLA target row; report counts. (There are 1,214 of the latter — planted; they matter in Module 3.)
4. *(10 min)* Semi vs inner: rewrite one query both ways; compare row counts and EXPLAIN output.

**Part B tasks (25 min, before PA-1)**
1. *(10 min)* Top-3 categories per municipality with ROW_NUMBER; verify exactly 51 rows (17 × 3).
2. *(10 min)* MoM + 3-month moving average per region; sanity-check January rows have NULL delta (LAG boundary) — if not, your PARTITION is wrong.
3. *(5 min)* Commit: `lab2: sla compliance + window trend queries`.

**Checkpoints & expected outputs**
```
Fan-out: 512,347 vs 487,000 — explained in writing
request_sla row assert: 315,806 = 315,806  ✓ (closed 2025 requests with SLA rows)
Orphans: 3,406 unassigned requests; 1,214 closed requests without SLA target
Top-3 result: 51 rows exactly
MoM: first month per region delta IS NULL  ✓
Worst breach cell: Ta'if roads category, Aug 2025 — 41.3% breach_pct
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Top-3 returns 40-something rows | Ties + RANK, or partitions with <3 categories | Use ROW_NUMBER with a tiebreaker column; check small municipalities |
| Delta non-NULL in first month | Missing PARTITION BY region in LAG | Add it; re-check every window in the query |
| `window functions are not allowed in WHERE` | Filtering the window directly | Wrap in CTE; filter outside |
| breach_pct > 100 or NULL | Fan-out re-introduced via assignments join, or /0 | Re-check grain; NULLIF the denominator |
| Query runs > 60 s and cancels | Function on filtered column defeating index | Half-open range on raw `opened_at` |

**Instructor notes.** The fan-out proof is the lab's centrepiece — collect each pair's one-sentence explanation and read two aloud; imprecise language ("it duplicates stuff") gets refined publicly. The missing-SLA-target orphans are deliberately left unresolved today: write the number on the whiteboard corner where it stays until Module 3 diagnoses upstream quality issues.

## Mini Exercises

**Quiz.** (1) LEFT JOIN then `WHERE right.col = 'x'` — what did you actually write? → an INNER JOIN. (2) Your join output has more rows than the left table and you expected 1:1 — first diagnostic query? → group right side by key, `HAVING count(*) > 1`. (3) RANK vs ROW_NUMBER on ties? → RANK repeats with gaps; ROW_NUMBER arbitrary unless tiebroken. (4) Why can't WHERE filter a window function? → windows evaluate after WHERE; use the CTE idiom. (5) `avg(satisfaction_score)` covers which rows, and what must accompany it in a report? → rated rows only; the response rate.

**Debugging exercise.** `debug_me_module2.sql` computes "average assignments per request" as 1.00 exactly — an inner join dropped the multi-assignment requests before a mistaken `DISTINCT`. Two defects; find both and state the correct value (1.05).

**Code-review exercise.** Review a colleague's "monthly dashboard query": LEFT JOIN converted by WHERE, `count(DISTINCT request_id)` masking fan-out while `sum(resolution_hours)` stays inflated, and no NULL guard on a pct denominator. Three findings, each with the business impact stated in riyals or percentage points.

**Discussion.** The dashboard team wants this SLA query run per page load; the DBA objects. Where should the boundary between "query at read time" and "precomputed summary table" sit, and who owns refresh correctness?

## Case Study — Ridership Analytics for a Riyadh Bus Network

**Scenario.** A public-transport operator's analytics team receives tap-in events (12M rows/month: card_id, route, stop, tapped_at) and must deliver: top 5 routes per time-band, week-over-week ridership change per route, and "time since previous tap" per card to flag pass-sharing (two taps 40 km apart within 10 minutes).

**Business context.** Network redesign decisions — where to add frequency before a major season — hinge on these numbers; a fan-out error in the route × stop join previously double-counted interchange stations and nearly triggered a wrong fleet reallocation costing ~SAR 9M.

**Technical challenge.** Express all three deliverables as window-function pipelines over event data, with verification steps that would have caught the interchange double-count.

**Constraints.** The events table is append-only and late-arriving (up to 48 h); card_ids are pseudonymised under PDPL and must never leave the analytics schema; queries must complete within the nightly batch window.

**Solution approach.** Top-N: aggregate to (route, time-band) then ROW_NUMBER partition per band. WoW: LAG over week partitioned by route, with a calendar spine CTE so missing weeks appear as NULL rather than silently comparing across gaps. Pass-sharing: `LAG(tapped_at) OVER (PARTITION BY card_id ORDER BY tapped_at)` + stop-distance lookup; flag deltas < 10 min with distance > threshold. Verification: interchange stations enumerated; assertion that event count equals sum of route-level counts; late-arrival window handled by recomputing a trailing 3-day slice nightly.

**Discussion questions.** (1) Why does the calendar-spine CTE matter for LAG-based WoW — what lie does its absence tell? (2) Which deliverable is most sensitive to fan-out and why? (3) The pass-sharing flag will have false positives (families sharing legitimately where permitted) — what is the analyst's responsibility in how the flag is worded and used? (4) Sketch the summary-table layer you would precompute for a public dashboard.

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Fan-out proof + written explanation | Method | 100% of pairs | artefact review |
| Row-count assertions present | Method | ≥ 3 per lab notebook | review checklist |
| SLA table correctness | Correctness | matches golden result exactly | golden-row comparison |
| Top-N and MoM queries | Correctness | 51 rows / NULL first-month deltas | answer key |
| PA-1 SQL practical | Assessment | ≥ 70/100 individually | rubric |
| Indexed vs non-indexed timing | Performance literacy | measured + one-sentence EXPLAIN reading | lab notebook |

**Example benchmark table:**

| Query | Rows out | Cold run | With index on opened_at | Plan node |
|---|---|---|---|---|
| SLA compliance (2025) | 204 | 3.9 s | 1.1 s | Index Scan + HashAgg |
| MoM by region (3 yrs) | 612 | 2.4 s | 2.2 s | Seq Scan (full-table by design) + WindowAgg |
| Naive fan-out count | 1 | 1.8 s | — | Hash Join (rows=512,347: read the estimate!) |

## Required Visuals and Training Assets

### Diagrams
1. **Join-type gallery on real tables** — *Purpose:* replace abstract Venn diagrams with row-level truth. *Elements:* 6-row miniature `requests` and 4-row `sla_targets` shown as actual grids; inner/left/anti results drawn row by row with kept/dropped rows colour-coded; fan-out panel showing one request matching two assignments becoming two rows. *Style:* table-grid illustration, not Venn. *Designer note:* this is the module's wall poster; Venn diagrams actively mislead about fan-out — do not use them.
2. **Grain ladder** — *Elements:* the same data at four grains (event → request → municipality-month → region-year) with arrows labelled by the operation (GROUP BY) and a red arrow labelled "join below your grain = fan-out". *Style:* vertical ladder.
3. **Window-function anatomy** — *Elements:* one OVER clause exploded: PARTITION walls, ORDER arrow, frame brackets sliding over rows; the four patterns (rank/offset/moving/share) as mini-panels. *Style:* annotated code + row-strip hybrid.
4. **Logical query-processing order, extended** — *Elements:* Module 1's diagram + GROUP BY/HAVING/window placement; "why WHERE can't see windows" callout. *Style:* extension of the M1 printable.

### Images (screenshots)
1. **Side-by-side fan-out counts in psql** — *why:* the money shot; *content:* 512,347 vs 487,000 with the fixing CTE visible.
2. **EXPLAIN ANALYZE output, annotated** — *why:* plan-reading literacy; *content:* Index Scan vs Seq Scan variants of the same query with timings circled.
3. **CTE pipeline in an IDE with one stage SELECTed** — *why:* debuggability of CTE style; *content:* cursor on `SELECT * FROM request_sla LIMIT 20` and its result.
4. **The 3-month moving-average plot** — *why:* expected Lab output; *content:* regional lines with Ramadan dips visible.

### Simulations
1. **The interchange double-count** — *Setup:* branch dataset `sim-fanout` adds a stops mapping table where interchange stations appear twice. *Expected:* naive route totals inflate 8%; assertions catch it. *Learning objective:* fan-out arrives via reference tables too, not just event tables.
2. **The gap-blind moving average** — *Setup:* delete one municipality's February data (planted upstream outage). *Expected:* ROWS-frame 3-month average silently spans Jan→Mar; calendar-spine version shows the hole. *Learning objective:* ROWS vs RANGE vs spine; absence of data is data.
3. **PARTITION amnesia** — *Setup:* provided LAG query without PARTITION BY. *Expected:* first-month deltas non-NULL and absurd (region boundary bleed). *Learning objective:* every window clause is load-bearing.

### Interactive Activities
- **Human window function (10 min):** 12 participants stand in two rows (two partitions) holding month cards; the instructor "runs" LAG and a 3-frame moving average by walking the rows; the partition boundary error is performed physically.
- **Query autopsy (15 min):** groups receive three anonymised real-world queries (one correct, one fan-out, one LEFT-join-broken) and must rank trustworthiness with written justification.

### Datasets
No new datasets — Module 2 deepens `city_services` deliberately (golden thread). The `sim-fanout` and gap variants ship as SQL patches applied to a scratch schema, leaving the canonical data untouched.

### Demo Requirements
- **Instructor demo:** build `sla_compliance.sql` live, CTE by CTE, running each stage; make one deliberate fan-out mistake and catch it with the row-count assert — rehearse the recovery; the *catching* is the lesson.
- **Student demo:** one pair walks the class through their fan-out explanation; one pair presents the MoM plot and reads the Ramadan dip aloud.
- **Expected outputs:** all queries committed with grain comments; PA-1 completed individually in the last 30 minutes of Hour 5.

---

# Module 3 — Data-Quality Assessment and Cleaning Workflows

## Module Overview

**Purpose.** The database's constraints protected participants for two days; today the protection is removed. Two CSV extracts from field operations — no types, no keys, no referential integrity — carry every defect the real world produces: mixed date formats, Arabic/English value variants, sentinel codes masquerading as measurements, duplicates from double-submission, and missingness that *means something*. This module turns cleaning from improvised cell-by-cell fixes into an engineering discipline: profile first, decide with evidence, implement as reproducible code, log every decision.

**Business relevance.** Data quality is where analytics credibility is won or lost — and it is a national priority: NDMO data-management standards make quality measurement and remediation an explicit obligation for government entities, and PDPL makes carelessness with personal data a legal exposure, not just a technical one. In industry, the pattern is universal: the model is blamed, the pipeline is audited, and the root cause is a silent `-999` averaged into a KPI eight months earlier. Organisations pay for this module's discipline exactly once — either here, or in production.

**Industry use cases.**
- A hospital network deduplicates patient records across three legacy systems before an EMR migration — false merges are a clinical-safety issue, missed merges a billing one.
- A ministry consolidating municipal field reports finds four spellings of the same city across submitting offices ("Taif", "Ta'if", "At-Ta'if", "الطائف") and needs a defensible mapping, not a guess.
- A utility's smart-meter feed uses `9999` for "read failed"; one quarter of unfiltered readings inflates consumption forecasts and triggers a procurement error.

**Expected competencies.** Participants can quantify quality along six dimensions, profile a dataset systematically before changing anything, classify missingness (MCAR/MAR/MNAR) and choose defensible treatments, normalise types/dates/text including Arabic-specific variants, deduplicate with explicit identity rules, and package the whole workflow as a re-runnable pipeline with validation asserts and a decision log.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Assess a dataset along the six quality dimensions and produce a quantified profiling report | LO2 |
| 3.2 | Classify missingness mechanisms and select treatments with stated justification | LO2 |
| 3.3 | Normalise types, dates, categorical values, and Arabic/English text variants | LO2, LO3 |
| 3.4 | Identify and resolve duplicates using explicit identity rules | LO2 |
| 3.5 | Implement cleaning as a reproducible, validated pipeline with a decision log | LO2, LO6 |

## Technical Content

### 1. The six dimensions, made measurable

Quality talk stays vague until each dimension becomes a number you can track:

| Dimension | Question | Metric on `field_inspections.csv` |
|---|---|---|
| **Completeness** | Is the value present? | % non-null per column (`df.notna().mean()`) |
| **Validity** | Does it conform to type/range/format? | % parseable dates; % scores in [1,5] |
| **Consistency** | Does it agree with itself and other sources? | % city values matching the canonical list; closed_at ≥ opened_at |
| **Uniqueness** | Is each real-world thing represented once? | duplicate rate under the identity rule |
| **Timeliness** | Is it fresh enough for the decision? | lag between event and record arrival |
| **Accuracy** | Does it match reality? | sampled comparison vs `city_services` DB (the luxury of having ground truth — rare in practice, say so) |

The deliverable pattern taught here — a *quality scorecard* per dataset, before/after cleaning — reappears in the capstone rubric. NDMO framing: these dimensions map directly onto national data-management standards; participants heading into government roles will meet this scorecard again with official letterhead.

### 2. Profile before you touch

The cardinal rule: **no mutation before measurement.** The profiling sequence, in order, as code:

1. **Shape and dtypes:** `df.shape`, `df.dtypes` — every `object` column is a question to answer, not a fact to accept.
2. **Per-column completeness:** `df.isna().mean().sort_values()` — but beware *disguised* missingness: `""`, `"N/A"`, `"غير متوفر"`, `-999`, `9999` are all "missing wearing a costume". Load first with `keep_default_na=False` to *see* the costumes, then declare them explicitly via `na_values`.
3. **Cardinality and top values:** `df[col].value_counts(dropna=False).head(20)` per categorical — this is where "Taif" meets "Ta'if".
4. **Numeric distributions:** `df.describe()` — a minimum of `-999` on a 1–5 score column is a sentinel announcement.
5. **Cross-field rules:** vectorised boolean checks (`(df.closed_at < df.opened_at).sum()`) — impossible combinations are consistency defects.
6. **Duplicates at the *claimed* key:** `df.duplicated(subset=["inspection_id"]).sum()`.

Everything is written into `profiling_report.md` with counts and percentages. The report is the *contract for the cleaning pipeline*: every fix implemented must trace to a documented defect, and every documented defect must be fixed, deferred with reason, or accepted with reason.

### 3. Missingness has mechanisms, and mechanisms decide treatments

- **MCAR** (completely at random): a flaky export dropped 2% of rows regardless of content. Deletion is safe; imputation is easy.
- **MAR** (at random, conditional on observables): tablet-based field forms capture GPS; paper forms (older inspectors, rural offices) don't. Missingness correlates with *observed* columns — analyse by group or impute within group.
- **MNAR** (not at random): satisfaction score missing *because* the citizen was angry, or completion time missing *because* the job wasn't done. The absence is signal. Deleting or mean-imputing MNAR data doesn't just lose information — it manufactures bias.

Treatments, with course rules: **drop rows** only with stated criteria and counted casualties; **drop columns** when completeness is hopeless (< 40%) *and* the column is not decision-critical; **impute** only with documented method and a companion `_imputed` flag column; **keep as NaN** and handle downstream — often the most honest choice for analytics (as opposed to ML pipelines, where Module 5 revisits imputation). Mean-imputing a bimodal column is manufacturing a value no citizen ever gave; medians resist outliers; group-wise medians respect MAR structure.

### 4. Types, dates, and text — the normalisation gauntlet

- **Types:** `pd.to_numeric(errors="coerce")` converts and *quarantines* failures as NaN — always count them before and after (`.isna().sum()` delta = rows coerced; investigate a sample). Never `errors="ignore"` (silently returns object) — deprecated for good reason.
- **Dates:** the extract mixes `2025-03-14`, `14/03/2025`, and Excel serials (`45730`). Strategy: parse each format *explicitly* on its matching subset (regex mask → `pd.to_datetime(format=...)`), never one permissive pass that guesses day-vs-month per row. A permissive parse that flips 14/03 and 03/14 for ambiguous days corrupts *silently* — the worst class of defect. Excel serials: `pd.to_datetime(n, unit="D", origin="1899-12-30")`.
- **Arabic text specifics** (the course treats these as first-class, not exotica): alef variants (أ/إ/آ vs ا), teh marbuta vs heh (ة/ه), tatweel elongation (ـــ), Eastern Arabic digits (٠١٢٣٤٥٦٧٨٩) needing translation to ASCII digits before numeric parsing, and invisible RTL/LTR marks (U+200E/U+200F) that make visually identical strings compare unequal. Normalisation function: strip marks, unify alef/teh-marbuta, translate digits, `str.strip()`, then map to canonical values.
- **Categorical harmonisation:** build an explicit mapping table (`city_mapping.csv`: variant → canonical) rather than inline `.replace({...})` chains — the mapping is reviewable, versionable, and reusable; unmapped values fail loudly to a quarantine list instead of passing through.

### 5. Duplicates and identity

"Duplicate" is a *decision*, not a fact: two rows with the same `inspection_id` but different scores are a conflict to resolve, not a dedup call. Course procedure: (1) define the identity rule (which columns constitute "the same event"); (2) split exact duplicates (`df.duplicated(keep="first")` — safe to drop, count them) from key-duplicates with conflicting values; (3) resolve conflicts with a stated rule (latest `submitted_at` wins; or aggregate; or escalate to source) — implemented as `sort_values().drop_duplicates(subset=key, keep="last")`; (4) record counts at each step. Fuzzy duplicates (same site, same day, 1-character-different city spelling) get flagged for the mapping table, not auto-merged — auto-merge without review is how hospital systems merge two different patients.

### 6. Cleaning as a pipeline: common mistakes & production considerations

The deliverable is not a clean DataFrame; it is a **function that produces one**: `raw → clean_inspections(raw) → (clean_df, decision_log)`. Structure: small named steps (`normalize_text`, `parse_dates`, `resolve_duplicates`, `apply_sentinels`), chained with `.pipe()`, each appending counts to the log; terminal `validate()` with hard asserts (key unique, dates in plausible range, scores in [1,5] or NaN, no unmapped cities). Re-running on the raw file must reproduce the output byte-for-byte.

**Common mistakes:** (1) cleaning in 40 unordered notebook cells — irreproducible by construction (the "restart and run all" test fails); (2) overwriting the raw file — raw data is immutable, always; (3) `inplace=True` chains obscuring order of operations (also: `inplace` is disappearing from pandas — don't teach it); (4) imputing without flag columns, destroying the ability to analyse missingness later; (5) dropping "bad" rows without counting them — 4% loss is a footnote, 34% is a finding; (6) fixing values by row index (`df.loc[8123, "city"] = ...`) — index positions are not stable identities; fix by rule. **Production:** cleaning rules drift as upstream systems change — pipelines carry versioned rule files and alert on quarantine-rate spikes; PDPL note: even "messy" extracts containing citizen data are personal-data processing — copies on laptops are governed artefacts; the course works on synthetic data precisely so this can be said without irony.

## Code Examples

### Profiling pass (run before touching anything)

```python
# src/wrangling/profile.py
"""Profiling utilities: measurement before mutation.
Output feeds profiling_report.md — the contract for the cleaning pipeline."""
import pandas as pd

SENTINEL_CANDIDATES = ["", "N/A", "NA", "-", "--", "غير متوفر", "لا يوجد",
                       "-999", "9999", "0000"]

def load_raw(path: str) -> pd.DataFrame:
    # keep_default_na=False → see missingness costumes before declaring them
    return pd.read_csv(path, dtype=str, keep_default_na=False)

def profile(df: pd.DataFrame) -> pd.DataFrame:
    """One row per column: the quality scorecard skeleton."""
    rows = []
    for col in df.columns:
        s = df[col]
        rows.append({
            "column": col,
            "n": len(s),
            "empty_or_sentinel": s.isin(SENTINEL_CANDIDATES).sum(),
            "pct_missing_disguised": round(100 * s.isin(SENTINEL_CANDIDATES).mean(), 1),
            "n_unique": s.nunique(),
            "top_value": s.mode().iat[0] if not s.mode().empty else None,
            "sample_values": list(s.drop_duplicates().head(5)),
        })
    return pd.DataFrame(rows).sort_values("pct_missing_disguised", ascending=False)
```

### Arabic-aware text normalisation and the mapping table

```python
# src/wrangling/textnorm.py
"""Text normalisation for mixed Arabic/English administrative data."""
import re
import pandas as pd

ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
INVISIBLE_MARKS = re.compile(r"[‎‏‪-‮]")   # LRM/RLM/embedding
TATWEEL = "ـ"

def normalize_text(s: pd.Series) -> pd.Series:
    return (s.astype("string")
             .str.translate(ARABIC_DIGITS)
             .str.replace(INVISIBLE_MARKS, "", regex=True)
             .str.replace(TATWEEL, "", regex=False)
             .str.replace("[أإآ]", "ا", regex=True)     # unify alef variants
             .str.replace("ة", "ه", regex=False)        # teh marbuta → heh (matching only!)
             .str.strip()
             .str.lower())

def map_to_canonical(s: pd.Series, mapping: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Apply the reviewed variant→canonical mapping. Unmapped values are
    QUARANTINED (returned separately), never passed through silently."""
    lookup = dict(zip(mapping["variant"], mapping["canonical"]))
    mapped = s.map(lookup)
    quarantine = s[mapped.isna() & s.notna()]
    return mapped, quarantine
```

### Explicit multi-format date parsing (no permissive guessing)

```python
# src/wrangling/dates.py
"""Parse each date format on its own explicitly-matched subset.
One permissive pd.to_datetime pass would guess day/month per row — silent corruption."""
import pandas as pd

ISO   = r"^\d{4}-\d{2}-\d{2}"
DMY   = r"^\d{2}/\d{2}/\d{4}"
SERIAL = r"^\d{5}$"                       # Excel serial, e.g. 45730

def parse_mixed_dates(s: pd.Series) -> tuple[pd.Series, pd.Series]:
    s = s.astype("string").str.strip()
    out = pd.Series(pd.NaT, index=s.index, dtype="datetime64[ns]")

    m = s.str.match(ISO, na=False)
    out[m] = pd.to_datetime(s[m], format="%Y-%m-%d")

    m = s.str.match(DMY, na=False)
    out[m] = pd.to_datetime(s[m], format="%d/%m/%Y")   # confirmed with source office

    m = s.str.match(SERIAL, na=False)
    out[m] = pd.to_datetime(s[m].astype(int), unit="D", origin="1899-12-30")

    unparsed = s[out.isna() & s.notna() & (s != "")]
    return out, unparsed                   # unparsed goes to the decision log
```

### The pipeline with decision log and terminal validation

```python
# src/wrangling/clean_inspections.py
"""Reproducible cleaning pipeline: raw CSV in, clean parquet + decision log out.
Re-running on the same raw file reproduces the output exactly."""
import json
import pandas as pd
from wrangling.textnorm import normalize_text, map_to_canonical
from wrangling.dates import parse_mixed_dates

LOG: list[dict] = []

def log_step(name: str, **counts):
    LOG.append({"step": name, **counts})

def resolve_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    exact = df.duplicated().sum()
    df = df.drop_duplicates()
    conflicts = df.duplicated(subset="inspection_id").sum()
    # Rule (documented): latest submission wins for conflicting resubmissions
    df = (df.sort_values("submitted_at")
            .drop_duplicates(subset="inspection_id", keep="last"))
    log_step("resolve_duplicates", exact_dupes_dropped=int(exact),
             conflicting_resubmissions_resolved=int(conflicts))
    return df

def apply_sentinels(df: pd.DataFrame) -> pd.DataFrame:
    n_before = df["quality_score"].isin(["-999", "9999"]).sum()
    df["quality_score"] = pd.to_numeric(
        df["quality_score"].replace({"-999": None, "9999": None}), errors="coerce")
    df["quality_score_missing"] = df["quality_score"].isna()   # flag, not erase
    log_step("apply_sentinels", sentinel_scores_nulled=int(n_before))
    return df

def validate(df: pd.DataFrame) -> pd.DataFrame:
    assert df["inspection_id"].is_unique, "identity rule violated"
    assert df["inspected_at"].between("2023-01-01", "2026-01-01").all()
    ok = df["quality_score"].between(1, 5) | df["quality_score"].isna()
    assert ok.all(), "scores outside [1,5] survived cleaning"
    assert df["city"].notna().all(), "unmapped cities passed quarantine"
    return df

def clean(raw: pd.DataFrame, city_mapping: pd.DataFrame) -> pd.DataFrame:
    df = (raw
          .pipe(resolve_duplicates)
          .pipe(apply_sentinels))
    df["inspected_at"], unparsed = parse_mixed_dates(df["inspected_at_raw"])
    log_step("parse_dates", unparsed=len(unparsed))
    df["city"], quarantine = map_to_canonical(normalize_text(df["city_raw"]),
                                              city_mapping)
    log_step("map_cities", quarantined=len(quarantine))
    df = df[df["city"].notna()]            # quarantine excluded, counted above
    return validate(df)

if __name__ == "__main__":
    raw = pd.read_csv("data/raw/field_inspections.csv", dtype=str,
                      keep_default_na=False)
    mapping = pd.read_csv("data/reference/city_mapping.csv")
    clean(raw, mapping).to_parquet("data/clean/inspections_clean.parquet")
    json.dump(LOG, open("data/clean/cleaning_log.json", "w"),
              indent=2, ensure_ascii=False)
```

## Hands-on Lab 3 — Profile and Clean the Field Extracts

| | |
|---|---|
| **Objective** | Produce a quantified profiling report on `field_inspections.csv` (12,400 rows, 14 defect types planted), then a reproducible pipeline emitting `inspections_clean.parquet` + `cleaning_log.json` |
| **Duration** | 2 × 50 min (Day 3 H3 + H5) |
| **Setup** | `data/raw/field_inspections.csv` + `satisfaction_callbacks.csv`; starter module skeletons in `src/wrangling/`; `pip install pandas pyarrow` |

**Part A — Profile (50 min)**
1. *(10 min)* Load with `dtype=str, keep_default_na=False`; run the profiling scorecard; list every column whose missingness wears a costume.
2. *(10 min)* Value-counts pass on `city_raw` and `inspection_type`: how many variants map to how many real cities? Draft `city_mapping.csv` (the Arabic/English variants are in there — 41 variants, 17 cities).
3. *(10 min)* Date triage: regex-count the three formats in `inspected_at_raw`; find the 212 Excel serials.
4. *(10 min)* Duplicates: exact vs conflicting-resubmission counts under the `inspection_id` identity rule; cross-field check `completed_at < inspected_at`.
5. *(10 min)* Write `profiling_report.md`: every defect, its count, its proposed treatment, and — crucially — the ones you propose *not* to fix, with reasons.

**Part B — Clean (50 min)**
1. *(25 min)* Implement the pipeline steps against the skeleton; every step logs counts.
2. *(10 min)* Terminal `validate()` — make it fail first (comment out the quarantine filter), read the assert, restore.
3. *(5 min)* Reproducibility test: delete outputs, re-run, `diff` the logs — identical or you have hidden state.
4. *(10 min)* Before/after quality scorecard table into the report; commit `lab3: profiling report + cleaning pipeline`.

**Checkpoints & expected outputs**
```
Profiling: 6 columns with disguised missingness; quality_score min -999 (317 rows)
city_raw: 41 variants → 17 canonical cities; 23 rows quarantined (unmappable)
Dates: 9,644 ISO / 2,544 DMY / 212 Excel serials; 12 unparseable → log
Duplicates: 186 exact dropped; 94 conflicting resubmissions resolved latest-wins
Final: 12,097 rows clean; validate() passes; re-run reproduces byte-identical log
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| All dates parse but spot-checks look wrong | Permissive single-pass parse guessed month/day | Use the explicit per-format masks; count each mask |
| Two visually identical city strings won't match | Invisible RTL/LRM marks | Apply `normalize_text` before mapping; hexdump one value to prove it |
| `SettingWithCopyWarning` storms | Chained indexing on a slice | Use `.loc` or restructure into `.pipe()` steps |
| Re-run gives different row counts | Mutating `raw` in place / notebook cell order | Raw immutable; pipeline is a script; "restart & run all" test |
| Scores column still object dtype | Sentinels replaced but not converted | `pd.to_numeric(errors="coerce")` after replacement; count coercions |

**Instructor notes.** The unparseable-dates dozen and the 23 quarantined cities are deliberate residue — teams that claim 100% cleanliness have silently passed garbage through, and the debrief makes that the discussion. Connect back to Day 2's whiteboard corner: the 1,214 missing SLA targets were this same disease seen from the database side. Fast finishers: clean `satisfaction_callbacks.csv` (fewer defects, needed for Module 4 anyway).

## Mini Exercises

**Quiz.** (1) Name the three missingness mechanisms and give a `city_services` example of each. (2) Why load with `keep_default_na=False` first? → to observe disguised missingness before declaring `na_values`. (3) What must accompany every imputation? → a documented method and an `_imputed`/`_missing` flag column. (4) Why is a permissive date parse worse than a failing one? → it corrupts silently (day/month swaps) instead of failing loudly. (5) Exact duplicate vs key conflict — different how? → identical rows are safe drops; same key + different values need a resolution *rule*.

**Debugging exercise.** A provided notebook "cleans" the callbacks file but its average satisfaction drops from 3.8 to 2.1 after cleaning — it coerced the Eastern-Arabic-digit scores (٤ etc.) to NaN and then filled NaN with 0. Two defects, both silent; find them via the before/after distribution comparison.

**Code-review exercise.** Review a cleaning PR: `inplace=True` chains, raw file overwritten, a `df.loc[8123] = ...` row-index fix, no counts logged, mean imputation on an MNAR column without a flag. Five findings; state the downstream harm of each.

**Discussion.** The field-office manager asks you to "just fix" the city spellings permanently in their source system. What is the correct escalation path, and why is fixing at source better *and* riskier than fixing in the pipeline?

## Case Study — Patient-Record Deduplication Across a Hospital Network

**Scenario.** A three-hospital private network in the Western Region migrates to a unified EMR. Legacy systems hold 1.9M patient records; a naive national-ID match links only 61% — the rest have missing IDs (old records), transposed digits, or Arabic/Latin name-only records with four transliteration variants ("Mohammed/Mohamed/Muhammad/محمد").

**Business context.** False merges (two patients become one chart) are a clinical-safety incident with mandatory reporting; missed merges cause duplicate tests, billing disputes, and a fragmented history at the bedside. The migration go-live date is fixed; the steering committee wants a defensible plan, not a perfect one.

**Technical challenge.** Design the deduplication workflow: blocking, matching tiers, thresholds, human-review queue sizing, and the audit trail — the same profile → rule → resolve → log discipline as the lab, at higher stakes.

**Constraints.** PDPL: matching uses identifiers lawfully held, minimum necessary staff see full records; review capacity is 3 clerks ≈ 900 pairs/day; clinical-safety office must sign the auto-merge rule; no record may be deleted — merges are reversible links.

**Solution approach.** Tiered matching: T1 exact national ID (auto-link); T2 normalised name + DOB + phone (auto-link only if all three agree post text-normalisation — the lab's `normalize_text` generalised to transliteration mapping); T3 partial agreement → scored candidate pairs into the human queue, blocked by DOB-year+first-initial to keep pair volume feasible; everything below threshold stays unlinked. Every auto-link carries the rule ID and inputs that fired it (the decision log, promoted to audit evidence); a random 2% of auto-links is human-verified weekly to estimate the false-merge rate; the safety office signs the T2 rule against that measured rate.

**Discussion questions.** (1) Which error is worse here, false merge or missed merge — and how does that asymmetry set the auto-merge threshold? (2) Compute the review-queue duration if T3 yields 41,000 pairs; what do you cut if it exceeds the runway? (3) Why "reversible links, never deletes" — connect to the raw-data-immutability rule from the lab. (4) What changes in this design under PDPL data-minimisation if a research team later requests the linked dataset?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Defect detection (14 planted types) | Completeness of profiling | ≥ 12/14 found before cleaning | profiling report vs answer key |
| Quantification discipline | Method | every reported defect has a count | report review |
| Pipeline reproducibility | Engineering | byte-identical log on re-run | diff test |
| Terminal validation | Engineering | ≥ 4 hard asserts, all meaningful | code review |
| Decision-log coverage | Auditability | 100% of mutations logged with counts | log inspection |
| Residue honesty | Judgement | unparseable/quarantined items reported, not hidden | report review |
| Cleaning wall-clock | Performance | full pipeline ≤ 30 s on 12,400 rows | timed run |

**Example benchmark table:**

| Stage | Rows in | Rows out | Values changed | Time |
|---|---|---|---|---|
| resolve_duplicates | 12,400 | 12,120 | — | 0.4 s |
| apply_sentinels | 12,120 | 12,120 | 317 nulled + flagged | 0.1 s |
| parse_dates | 12,120 | 12,120 | 12 unparsed → log | 1.2 s |
| map_cities | 12,120 | 12,097 | 41 variants → 17 canon; 23 quarantined | 0.8 s |
| validate | 12,097 | 12,097 | 0 (asserts only) | 0.1 s |

## Required Visuals and Training Assets

### Diagrams
1. **The six quality dimensions wheel** — *Purpose:* module anchor; scorecard vocabulary. *Elements:* six segments, each with its one-line question and its `field_inspections` metric; NDMO-alignment note in the footer. *Style:* wheel/hex layout, course palette, printable A4.
2. **Profile → decide → clean → validate loop** — *Elements:* four-stage cycle with artefacts on each edge (profiling report, decision log, clean parquet, assert results); a red shortcut arrow labelled "notebook cell soup" crossing the middle, struck out. *Style:* cycle diagram with artefact icons.
3. **Missingness mechanisms triptych** — *Elements:* three panels (MCAR/MAR/MNAR) each with a `city_services` example and its safe treatments; MNAR panel carries a warning banner "the absence is the signal". *Style:* three-panel comparison card.
4. **Anatomy of a disguised missing value** — *Elements:* one column's value-counts bar chart with sentinels highlighted (`-999`, `""`, `غير متوفر`) and their reclassification arrows to NaN + flag. *Style:* annotated bar chart.

### Images (screenshots)
1. **Profiling scorecard DataFrame output** — *why:* expected Lab 3a artefact; *content:* the per-column table with `pct_missing_disguised` sorted descending.
2. **Hexdump of two "identical" city strings** — *why:* makes invisible marks visceral; *content:* U+200F visible in one, absent in the other.
3. **Failing `validate()` traceback** — *why:* asserts as guardrails, not decoration; *content:* the quarantine assert firing with its message.
4. **Before/after distribution plot of quality_score** — *why:* the sentinel effect visualised; *content:* histogram with the -999 spike vs cleaned distribution.

### Simulations
1. **The silent day/month swap** — *Setup:* branch notebook using one permissive `pd.to_datetime` pass. *Expected:* all rows "parse"; the monthly plot shows an impossible March spike (ambiguous-day DMY rows mis-read). *Learning objective:* loud failure beats silent success; explicit-format parsing.
2. **The sentinel average** — *Setup:* skip `apply_sentinels`; compute mean quality score. *Expected:* 2.9 vs true 3.7 — a KPI moved by ghosts. *Learning objective:* profiling before aggregation, always.
3. **Hidden-state notebook** — *Setup:* provided notebook passes top-to-bottom *only* in its saved execution order. *Expected:* "restart & run all" fails; participants convert it to a pipeline script. *Learning objective:* reproducibility is a property you test, not assume.

### Interactive Activities
- **Defect bingo (15 min):** pairs get bingo cards of defect types; first to *evidence* (with a count) five-in-a-row from the raw file wins. Forces broad profiling instead of fixating on the first defect found.
- **Treatment tribunal (15 min):** three proposed treatments for the missing satisfaction scores (drop / median-impute / keep-NaN + flag) are each defended by a team for two minutes; the class votes with justification. There is a best answer (keep + flag) but the arguing is the point.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `field_inspections.csv` | Synthetic, 14 defect types planted by course tooling | CSV | 12,400 rows | Lab 3 primary |
| `satisfaction_callbacks.csv` | Synthetic, 6 defect types | CSV | 38,000 rows | Fast-finisher + Module 4 input |
| `city_mapping.csv` (participants author it) | Lab output | CSV | 41 rows | Reviewed reference artefact |
| Defect answer key | Instructor pack | MD | 1 page | Debrief |

### Demo Requirements
- **Instructor demo:** the sentinel-average simulation live (2.9 → 3.7 reveal), then the day/month-swap plot — two silent corruptions made loud in ten minutes; rehearse the reveals.
- **Student demo:** one pair presents their decision log end-to-end; the class challenges one treatment choice.
- **Expected outputs:** every participant enters Day 4 with `inspections_clean.parquet`, `cleaning_log.json`, and a defensible profiling report — Module 4 consumes them directly.

---

# Module 4 — Reshaping, Merging, and Transforming Datasets

## Module Overview

**Purpose.** Analysis-ready data has a shape, and raw data almost never arrives in it. This module teaches the pandas transformation vocabulary — tidy-data reasoning, wide↔long reshaping, disciplined merging with the same grain paranoia as Module 2's joins, split-apply-combine with `groupby`, and time-aware operations — culminating in the course's central engineering artefact: a validated **master table** at one-row-per-request grain that joins the SQL world of Days 1–2 to the cleaned extracts of Day 3.

**Business relevance.** Every analytics and ML team maintains some version of the master table this module builds — the "analytical base table" in banking, the "flat file" in consulting, the "feature source" in ML platforms. Its correctness is inherited by every dashboard, report, and model downstream, which is why merge discipline (`validate=`, row-count asserts, `indicator=`) is not pedantry: a fan-out in the base table is an error *multiplied by everything built on it*. Teams that treat table assembly as engineering ship trustworthy numbers; teams that treat it as improvisation ship apologies.

**Industry use cases.**
- A Hajj-season operations centre merges pilgrim-transport feeds from multiple carriers into a single arrival-flow table — mismatched keys and duplicate manifests are the daily reality.
- A retail chain pivots transaction lines (long) into store-week sales matrices (wide) for planners, and melts them back for modelling — fluency in both directions, on demand.
- A national statistics team combines survey waves with registry extracts using validated many-to-one joins, publishing the merge-rate table alongside the statistics as a quality disclosure.

**Expected competencies.** Participants can state and check a table's grain, reshape between wide and long with `melt`/`pivot_table`, merge with explicit cardinality validation and match-rate reporting, use `groupby` with `agg`/`transform` correctly (knowing which preserves shape), apply `merge_asof` for time-adjacent joins, and manage dtypes/memory well enough to keep half-million-row work interactive.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Diagnose whether a dataset is tidy for a given analysis and reshape it with melt/pivot_table | LO3 |
| 4.2 | Merge datasets with explicit cardinality validation, match-rate reporting, and grain preservation | LO3, LO2 |
| 4.3 | Apply split-apply-combine: agg vs transform vs apply, chosen correctly | LO3 |
| 4.4 | Join time-stamped data with merge_asof and resample time series to analysis grain | LO3 |
| 4.5 | Assemble and validate the analysis-ready master table consumed by Modules 5–6 | LO3, LO4 |

## Technical Content

### 1. Tidy data: shape follows question

Tidy structure — each variable a column, each observation a row, each observational unit a table — is the shape pandas, Seaborn, and every ML library assume. But "observation" depends on the question: for "satisfaction by channel", one row per *request* is tidy; for "compare monthly trends across regions", one row per *(month, region)* is tidy; the planner's spreadsheet with months as columns is tidy *for a human eye* and hostile to computation. So the operational skill is not memorising a definition — it is stating the target grain out loud and reshaping toward it. Wide data is a *presentation* format; long data is a *computation* format; professionals convert between them without ceremony.

### 2. Wide ↔ long mechanics

- **`melt`** (wide → long): month columns become `(month, value)` pairs. Name things properly at the moment of melting (`var_name="month"`, `value_name="n_requests"`) — downstream code reads these names forever.
- **`pivot_table`** (long → wide): specify `index`, `columns`, `values`, and — always explicitly — `aggfunc`. The default (`mean`) silently *aggregates* when the index×columns pair is not unique; `aggfunc="sum"` vs `"mean"` is an analytical decision, not a formality. `pivot` (no aggfunc) raises on duplicates — use it when duplicates would mean a bug, precisely *because* it raises.
- **`stack`/`unstack`** move levels between index and columns — most useful straight after a two-key `groupby` to lay results out for humans.
- Round-trip identity: `melt` then `pivot_table` must reproduce the original (a lab checkpoint) — if it doesn't, something aggregated along the way and you now know your keys weren't unique.

### 3. Merging with discipline (Module 2's joins, translated)

`pd.merge` is SQL joining without the safety rails of a schema — so the rails are re-installed by hand, every time:

1. **Declare cardinality:** `validate="one_to_one"` / `"many_to_one"` — pandas raises if reality disagrees. This single argument would prevent most production merge bugs and costs nothing. Course rule: *every* merge carries `validate=`.
2. **Measure the match:** `indicator=True` adds `_merge` (`both` / `left_only` / `right_only`); `value_counts()` on it is the **match-rate report**. An 88% match rate is not an error — it is a *finding* that goes in the report (which 12% of requests had no inspection, and are they random? Usually not — MAR strikes again).
3. **Preserve the grain:** row count before == row count after for a `many_to_one` left merge; assert it.
4. **Mind the keys:** dtype mismatches (`int64` vs `str` request IDs — exactly what a CSV round-trip produces) match *nothing* silently on merge; whitespace and case differences ditto (Module 3's normalisation is the prerequisite); NaN never equals NaN — rows with null keys match nothing.
5. **`how=` follows the question,** not habit: analytical base tables are usually built with `left` from the spine (the table whose grain defines the output).

`concat` is the other axis: stacking same-shaped extracts (`axis=0` — check column alignment, pandas aligns by *name* not position) or side-by-side by index (`axis=1` — verify index alignment first or enjoy silent NaN interleaving).

### 4. Split-apply-combine, and the transform/agg distinction

`groupby` is Module 2's GROUP BY with a twist that trips everyone: what comes back.

- **`agg`** collapses: one row per group (`gb["resolution_hours"].agg(["mean", "median", "count"])`). Named aggregation (`n_requests=("request_id", "count")`) keeps output columns readable.
- **`transform`** preserves shape: one value per *original row*, broadcast from its group — exactly the window-function idea from Module 2 (`SELECT avg(x) OVER (PARTITION BY g)`). This is how group-relative columns are built: `df["dev_from_city_median"] = df["res_hours"] - gb["res_hours"].transform("median")`. Say the SQL parallel out loud; participants who mastered windows get transform for free.
- **`apply`** is the escape hatch: arbitrary per-group functions, at 10–100× the cost and none of the vectorisation. Course rule: reach for `apply` only after `agg`/`transform` have been shown insufficient — and expect to justify it in review.

### 5. Time-aware operations

- **`resample`** is groupby over time bins: `df.set_index("opened_at").resample("W")["request_id"].count()` — weekly volumes with *explicit* empty bins (a silent advantage over `groupby(week)`: missing weeks appear as 0/NaN instead of vanishing — Module 2's calendar-spine lesson, solved natively).
- **`merge_asof`** joins each row to the *most recent* row of another table — the correct tool for "which fee schedule / policy version / staffing roster was in force when this request opened". Requirements: both sides sorted by the key; `by=` for per-group matching; `tolerance=` to refuse stale matches. The lab joins requests to a `crew_rosters` table effective-dated monthly — an exact-key merge here is simply *wrong* (rosters don't change per-request), which is why this pattern earns its place.
- Timezones: `city_services` timestamps are `timestamptz` (UTC in storage); convert to `Asia/Riyadh` *once*, at load, and document it — mixed-awareness comparisons raise, which is pandas doing you a favour.

### 6. Dtypes, memory, and common mistakes

At 487k rows the master table fits anywhere; the *habits* must survive to 50M. `category` dtype for low-cardinality strings (city, channel, status) cuts memory ~10×; `Int64` (nullable) keeps integer keys integer despite NaNs (the float64 key corruption — `1024.0` — is a planted lab bug); `df.info(memory_usage="deep")` before and after is the receipt. Parquet, not CSV, for intermediate artefacts: types survive, reads are 10× faster, and the Module 3 lesson (CSV loses the schema) stops repeating.

**Common mistakes:** (1) merging without `validate=` — the unprotected join; (2) ignoring `_merge` and never learning that 12% didn't match; (3) `pivot_table` silently averaging duplicates the analyst didn't know existed; (4) `apply` with a Python loop inside where `transform("mean")` existed; (5) float-contaminated key columns after a NaN-introducing merge, breaking the *next* merge; (6) building the master table in one 400-character chained expression — chain in reviewable steps with intermediate asserts. **Production:** master tables are *rebuilt from raw* on schedule, never patched in place (the Module 3 immutability rule at table scale); the assembly script publishes its match-rate table as metadata alongside the parquet — downstream consumers read the quality disclosure with the data.

## Code Examples

### Reshaping: melt, pivot_table, and the round-trip check

```python
# notebooks/day4_reshape.ipynb (exported cells)
"""Wide↔long fluency drills on the monthly extract."""
import pandas as pd

wide = pd.read_sql(MONTHLY_WIDE_QUERY, engine)   # one row per region, 36 month cols

# Wide → long: computation shape
long = wide.melt(id_vars="region", var_name="month", value_name="n_requests")
long["month"] = pd.to_datetime(long["month"])

# Long → wide: presentation shape. aggfunc EXPLICIT even when keys are unique.
back = long.pivot_table(index="region", columns="month",
                        values="n_requests", aggfunc="sum")

# Round-trip identity: if this fails, keys weren't unique and something aggregated
pd.testing.assert_frame_equal(
    back.sort_index(axis=1), wide.set_index("region").sort_index(axis=1),
    check_names=False)
```

### The disciplined merge (validate, indicator, assert)

```python
# src/wrangling/build_master.py (excerpt 1)
"""Every merge: declared cardinality, measured match rate, preserved grain."""

requests = pd.read_parquet("data/extracts/requests_2023_2025.parquet")   # the SPINE
inspections = pd.read_parquet("data/clean/inspections_clean.parquet")

n_before = len(requests)

master = requests.merge(
    inspections[["request_id", "quality_score", "quality_score_missing",
                 "inspected_at"]],
    on="request_id",
    how="left",                 # spine grain is sacred
    validate="one_to_one",      # one inspection per request, or raise
    indicator=True,
)

# Match-rate report: a FINDING, not a debug print — it ships with the table
match_report = master["_merge"].value_counts()
print(match_report)
# both          11,872
# left_only    475,128     ← only 2.4% of requests get field inspections: expected
master = master.drop(columns="_merge")

assert len(master) == n_before, "grain violated: spine row count changed"
```

### Group-relative columns: transform as the window function of pandas

```python
# src/wrangling/build_master.py (excerpt 2)
"""Group-relative context columns — SQL window functions, pandas dialect."""

master["resolution_hours"] = (
    (master["closed_at"] - master["opened_at"]).dt.total_seconds() / 3600
)

gb_city = master.groupby("city", observed=True)

# transform → one value per ROW (shape preserved), like AVG(...) OVER (PARTITION BY city)
master["city_median_res_hours"] = gb_city["resolution_hours"].transform("median")
master["res_vs_city_median"] = (
    master["resolution_hours"] / master["city_median_res_hours"]
)

# agg → one value per GROUP (collapsed), like GROUP BY city
city_summary = gb_city.agg(
    n_requests=("request_id", "count"),
    median_res_hours=("resolution_hours", "median"),
    satisfaction=("satisfaction_score", "mean"),
    satisfaction_coverage=("satisfaction_score", lambda s: s.notna().mean()),
)
```

### merge_asof: joining to what was in force at the time

```python
# src/wrangling/build_master.py (excerpt 3)
"""Attach the crew roster that was effective WHEN the request opened.
Exact-key merge is wrong here: rosters are effective-dated, not per-request."""

rosters = (pd.read_parquet("data/reference/crew_rosters.parquet")
             .sort_values("effective_from"))
master = master.sort_values("opened_at")

master = pd.merge_asof(
    master, rosters,
    left_on="opened_at", right_on="effective_from",
    by="municipality_id",                 # match within the municipality
    direction="backward",                 # most recent roster BEFORE opening
    tolerance=pd.Timedelta("180D"),       # refuse absurdly stale matches
)

# Dtype hygiene for the artefact
for col in ["city", "region", "channel", "status", "department"]:
    master[col] = master[col].astype("category")
master["crew_size"] = master["crew_size"].astype("Int64")   # nullable int, not float

master.to_parquet("data/clean/requests_master.parquet")
```

## Hands-on Lab 4 — Assemble the Master Table

| | |
|---|---|
| **Objective** | Build `requests_master.parquet` — one row per request, 34 columns — from the SQL extract, the cleaned inspections, the callbacks file, and the effective-dated rosters; every merge validated, every match rate reported |
| **Duration** | 50 minutes (Day 4 H2) |
| **Setup** | Day 3 outputs present (or `data/clean_reference/` fallback); `requests_2023_2025.parquet` extract provided; skeleton `build_master.py` |

**Tasks**
1. *(5 min)* Load the spine; record its row count and key uniqueness (`is_unique`) — the two invariants every later step must preserve.
2. *(10 min)* Merge cleaned inspections (`one_to_one`, left, indicator); write the match-rate report; explain the 2.4% in one sentence (field inspections are sampled, not universal).
3. *(10 min)* Merge callbacks — but it arrives at *callback* grain (a request can be called twice): pre-aggregate to request grain first (Module 2's pre-aggregation fix, pandas dialect), then `many_to_one`… which is now `one_to_one`. The planted trap: merging raw first "works" and adds 3,912 rows.
4. *(10 min)* `merge_asof` the rosters with `by=municipality_id`; count rows outside tolerance; investigate five.
5. *(10 min)* Group-relative columns (`city_median_res_hours`, `res_vs_city_median`); dtype pass (`category`, `Int64`); `info(memory_usage="deep")` before/after into the notebook.
6. *(5 min)* Terminal validation cell: spine count preserved, key unique, no float keys, memory ≤ 120 MB. Commit `lab4: validated master table`.

**Checkpoints & expected outputs**
```
Spine: 487,000 rows, request_id unique ✓
Inspections merge: both=11,872 (2.4%) — sampled programme, expected
Callbacks trap: naive merge → 490,912 rows (caught by assert); pre-agg fix → 487,000 ✓
merge_asof: 1,166 requests with no roster within 180 days (early-2023 boundary)
Memory: 118 MB → 41 MB after category/Int64 pass
requests_master.parquet: 487,000 × 34, written with schema intact
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `MergeError: not a one-to-one merge` | Callbacks at wrong grain (the trap working as designed) | Pre-aggregate to request grain; thank the validate= |
| Match rate 0% on a merge | Key dtype mismatch (str vs int after CSV round-trip) | Align dtypes explicitly before merging; check `df.dtypes` |
| `merge_asof` raises "keys must be sorted" | Unsorted inputs | Sort both sides by the time key (and check `by=` groups) |
| Key column becomes float64 with `.0` | NaN introduced into int column by a left merge | `Int64` nullable dtype |
| Round-trip assert fails in reshaping drill | Duplicate (index, column) pairs silently averaged | Find the duplicates; decide sum vs mean *consciously* |

**Instructor notes.** The callbacks trap is the module's designed failure: roughly half the room merges raw and gets saved by `validate=` — which is precisely the argument for always writing it. Pairs that used Day 3's fast-finisher cleaned callbacks connect the modules viscerally. Keep every pair's match-rate report; Module 6 reuses the "who gets inspected?" question as an EDA finding (inspection is not random — it is triggered by reopened requests).

## Mini Exercises

**Quiz.** (1) `agg` vs `transform` — shape of each output? → one row per group vs one value per original row. (2) Which single merge argument would have caught the callbacks trap? → `validate="one_to_one"`. (3) When is `pivot` preferable to `pivot_table`? → when duplicate keys would indicate a bug — it raises instead of averaging. (4) Why did `crew_size` become 3.0 after the merge, and what fixes it? → NaN forced float64; nullable `Int64`. (5) What does `resample("W")` give you that `groupby(week_col)` doesn't? → explicit empty bins — absent weeks appear instead of vanishing.

**Debugging exercise.** A provided script builds a "monthly satisfaction by department" pivot whose national average moved from 3.7 to 4.1 — a `pivot_table` default-mean over an unnoticed duplicate grain plus an inner (default) merge that dropped unrated months. Two defects; find both and state which direction each biased the number.

**Code-review exercise.** Review a master-table PR: no `validate=` anywhere, `_merge` never inspected, `apply` with a row loop computing what `transform("mean")` does, CSV intermediates, and a 300-character single chain with no asserts. Five findings with downstream blast radius stated.

**Discussion.** The master table now exists. Who owns it — the analyst who built it, or a data-engineering team? What changes when three other teams start reading the parquet?

## Case Study — Unifying Pilgrim-Transport Feeds for Hajj Operations

**Scenario.** A seasonal operations centre receives four carrier feeds for pilgrim ground transport (bus manifests, gate scans, dispatch logs, and a carrier-submitted daily summary). Grains differ (passenger, vehicle-trip, gate-event, carrier-day), keys differ (permit number vs trip ID vs plate), clocks differ (one feed logs in UTC, others in Asia/Riyadh), and one carrier resubmits corrected manifests up to 12 hours later.

**Business context.** The centre's arrival-flow table drives staffing at reception points; over-count and staff stand idle, under-count and queues form in heat — both outcomes are measured in headlines. Last season's table double-counted resubmitted manifests on peak day by 7%.

**Technical challenge.** Design the assembly: choose the spine grain, sequence the merges/pre-aggregations, handle resubmissions and clock skew, and define the validation battery that would have caught the 7%.

**Constraints.** Feeds arrive on different cadences (real-time to daily); passenger-level data is personal data — the analytical table must carry counts, not identities, beyond the ingestion layer (data minimisation); the table rebuilds every 30 minutes during peak; carrier D's summary is the *only* source for one remote route.

**Solution approach.** Spine = vehicle-trip grain (the operational decision unit); passenger manifests pre-aggregated to trip counts at ingestion (minimisation applied at the earliest layer); resubmissions resolved latest-wins on (carrier, manifest_id) *before* merging — Module 3's duplicate rule at feed scale; all timestamps normalised to Asia/Riyadh at load with the UTC feed converted, not assumed; gate scans joined `merge_asof` (nearest scan within 45 min of scheduled arrival, `by=` route); carrier-day summary joined `many_to_one` as a *reconciliation column*, not a source — a per-carrier daily delta report flags divergence > 3%; validation battery: spine count vs distinct trip IDs, per-carrier match rates, resubmission counts, and a peak-day golden comparison against the previous rebuild.

**Discussion questions.** (1) Why is the carrier-day summary demoted to reconciliation rather than merged as data? (2) Where exactly does the 7% double-count enter, and which validation step catches it — dedup order matters; trace it. (3) The remote route has *only* the summary feed — how do you represent lower-confidence rows honestly in the table? (4) Which parts of this design are the lab's `build_master.py` at bigger scale? Map them step to step.

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Spine preservation | Correctness | 487,000 rows at every step | asserts in script |
| Merge discipline | Method | 100% of merges carry `validate=` + match-rate report | code review |
| Callbacks trap | Correctness | caught by validate or pre-empted | lab observation |
| Round-trip reshape check | Correctness | assert passes | notebook |
| Memory after dtype pass | Performance | ≤ 45 MB (from ~118 MB) | `info(memory_usage="deep")` |
| Full rebuild wall-clock | Performance | ≤ 60 s raw-to-parquet | timed run |
| transform vs apply usage | Code quality | 0 unjustified `apply` | review |

**Example benchmark table:**

| Operation | Naive approach | Disciplined approach | Delta |
|---|---|---|---|
| Callbacks merge | 490,912 rows (silent fan-out) | 487,000 (pre-agg + validate) | correctness |
| Group medians | `apply` loop: 41 s | `transform("median")`: 0.9 s | 45× |
| Master table load | CSV: 9.8 s, dtypes lost | parquet: 0.9 s, schema intact | 11× + fidelity |
| Memory | 118 MB object-heavy | 41 MB category/Int64 | 2.9× |

## Required Visuals and Training Assets

### Diagrams
1. **Master-table assembly map** — *Purpose:* the module's anchor; the capstone's data lineage in one image. *Elements:* the spine (requests extract) flowing left-to-right; each satellite (inspections, callbacks→pre-agg, rosters via asof) joining with its cardinality and match rate labelled on the edge; validation gates as checkpoints; `requests_master.parquet` as the terminal artefact feeding M5/M6 boxes. *Style:* lineage/flow diagram reusing the Module 1 ERD colours per table.
2. **agg vs transform vs apply** — *Elements:* one 9-row grouped table processed three ways, output shapes drawn to scale (3 rows / 9 rows / "anything, slowly"); SQL-parallel captions (GROUP BY / window / —). *Style:* three-panel row-strip.
3. **Wide↔long round trip** — *Elements:* the same numbers as a region×month grid and as a long triple-column table, melt and pivot arrows both directions, the round-trip identity as a loop; a hazard icon where duplicate keys would break it. *Style:* before/after with loop arrow.
4. **merge_asof timeline** — *Elements:* roster effective-dates as flags on a timeline, request open-times as dots, backward-matching arrows, one dot outside tolerance left unmatched with a NULL tag. *Style:* horizontal timeline.

### Images (screenshots)
1. **`MergeError` from validate= on the callbacks trap** — *why:* the argument for the argument; *content:* full traceback with the message readable.
2. **Match-rate report cell** — *why:* the finding-not-debug framing; *content:* `_merge` value_counts with the 2.4% row and its one-sentence interpretation.
3. **`info(memory_usage="deep")` before/after** — *why:* dtype pass receipt; *content:* 118 MB vs 41 MB side by side.
4. **The master table's head in Jupyter** — *why:* target artefact reference; *content:* 34 columns with dtypes row visible (categories and Int64 evident).

### Simulations
1. **The silent fan-out (unprotected)** — *Setup:* same callbacks merge with `validate=` removed. *Expected:* 490,912 rows, no error; downstream satisfaction average shifts +0.07. *Learning objective:* the bug is quiet and the KPI moves — validate= is the alarm you install in advance.
2. **The dtype-mismatch ghost merge** — *Setup:* inspections file with request_id as int, spine as str. *Expected:* 0% match rate, all-NaN columns, no exception. *Learning objective:* a merge that matches nothing still "succeeds"; match-rate reporting catches what exceptions don't.
3. **Clock-skew asof** — *Setup:* rosters in UTC, requests in Asia/Riyadh, both naive. *Expected:* boundary requests match the *previous* roster; only the tolerance count hints at it. *Learning objective:* timezone normalisation at load, once, documented.

### Interactive Activities
- **Grain court (15 min):** six dataset cards (gate events, manifests, monthly summary…) — teams must state each one's grain in one sentence and design the pre-aggregation needed to join it to a given spine; judged by peers.
- **Merge-plan sketching (10 min):** before touching the keyboard in Lab 4, every pair sketches the assembly map on paper (spine, order, cardinalities). The sketch is checked against the final script in the debrief — divergences are the lesson.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `requests_2023_2025.parquet` | SQL extract, provided (or self-produced from Day 2 queries) | Parquet | 487k rows | Spine |
| `crew_rosters.parquet` | Synthetic, effective-dated monthly | Parquet | 612 rows | merge_asof exercise |
| Day 3 cleaned outputs | Participants' own (reference fallback provided) | Parquet | 12k + 38k | Satellites |
| `requests_master.parquet` | **Lab output** | Parquet | 487k × 34 | Input to M5, M6, capstone |

### Demo Requirements
- **Instructor demo:** the callbacks trap live — merge raw, hit the `MergeError`, read it aloud, fix with pre-aggregation; then the dtype ghost-merge (0% match, no error) as the counterpoint: one failure is loud, one silent, and the discipline covers both.
- **Student demo:** one pair walks their assembly map sketch vs final script; one pair presents the memory before/after.
- **Expected outputs:** every participant holds a validated `requests_master.parquet` by end of Hour 2 — Modules 5 and 6 consume it directly; a reference copy ships in `data/clean_reference/` so nobody is blocked.

---

# Module 5 — Feature Engineering for Analytics and ML

## Module Overview

**Purpose.** Raw columns record what happened; features encode what it *means*. This module teaches the craft of turning the master table's timestamps, categories, and histories into analytically meaningful variables — calendar effects (including Ramadan and salary-cycle patterns specific to the regional context), encodings that ML libraries can consume, ratios and rates that normalise away size, and entity-history aggregates that give each row memory — while drilling the discipline that separates features from statistical fraud: **leakage awareness** and **point-in-time correctness**.

**Business relevance.** In tabular problems — which is most of enterprise ML in banking, telecom, government services — feature quality beats model choice, consistently and by a wide margin. A gradient-boosted model on thoughtful features outperforms a deep model on raw columns in nearly every industry benchmark that resembles this data. Equally important commercially: leaked features are the most expensive ML failure mode, because they produce *brilliant offline metrics* and worthless production models — the error is discovered only after deployment budgets are spent. Analysts who can engineer honest features are the bridge between this Foundation module and both role tracks.

**Industry use cases.**
- A digital bank's credit-risk team builds salary-cycle and transaction-velocity features from account histories — every feature documented, point-in-time correct, and reviewed for leakage before model training.
- A telecom churn model's strongest features are engineered ratios (data-usage trend vs plan allowance, support-contact rate per month of tenure), not raw usage columns.
- A municipal operations team engineers "repeat-request density per district" to direct preventive maintenance — a pure analytics use of feature engineering, no model required.

**Expected competencies.** Participants can derive calendar/datetime features (Gregorian and Hijri-aware), choose and implement categorical encodings appropriate to cardinality and downstream use, construct ratios/rates/bins with edge-case care, build entity-history aggregates that respect time ordering, detect target and temporal leakage, and document every feature in a feature dictionary.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Derive datetime and calendar features including region-relevant effects (Ramadan, weekends, salary cycle) | LO4 |
| 5.2 | Encode categorical variables appropriately for cardinality and downstream use | LO4 |
| 5.3 | Construct ratio, rate, binned, and flag features with explicit edge-case handling | LO4 |
| 5.4 | Build point-in-time-correct entity-history aggregates (expanding/rolling, time-shifted) | LO4, LO3 |
| 5.5 | Detect and prevent target and temporal leakage in a feature set | LO4, LO2 |
| 5.6 | Document features in a feature dictionary a stranger could rebuild from | LO4, LO6 |

## Technical Content

### 1. What makes a feature good

Four tests, applied to every candidate: **predictive plausibility** (a mechanism you can say out loud — "requests opened Thursday afternoon wait over the weekend, so day-of-week should matter for resolution time"); **availability at decision time** (would the value exist at the moment the prediction/decision is made? — the leakage question in disguise); **stability** (does its meaning survive upstream changes? a feature built on a free-text field is a maintenance liability); **interpretability in the room** (can you explain it to the operations manager whose process it describes?). The module's framing target is *SLA breach*: which features, computable at request-opening time, relate to eventual breach? That "at opening time" clause does an enormous amount of work — half the master table's columns (closed_at, resolution_hours, satisfaction_score) are *outcomes*, not features, for this target.

### 2. Datetime and calendar features

From `opened_at`, the standard extraction: hour, day-of-week, month, is-weekend — with the regional correction that the weekend is Friday–Saturday, so `dayofweek.isin([4, 5])`, not the imported 5–6. Beyond the standard set, the features that actually move metrics in Saudi operational data:

- **Ramadan and Eid effects:** service demand reshapes (evening peaks, category mix shifts) and workforce capacity changes. Hijri calendar dates shift ~11 days earlier each Gregorian year, so *no fixed Gregorian rule works* — use a maintained mapping table (`hijri_calendar.csv`: gregorian_date → hijri month, is_ramadan, is_eid) joined onto the data. This is also the honest engineering lesson: some domain knowledge arrives as reference data, not as code.
- **Salary-cycle features:** day-of-month distance from the 27th (public-sector payday) captures spending/activity cycles visible in the request data.
- **Cyclical encoding** for hour and month where models need continuity across the wrap (23:00 ≈ 00:00): `sin(2π·h/24)`, `cos(2π·h/24)`. For tree models this matters little (say so — honesty about when a technique earns its complexity); for linear/distance-based methods it matters a lot.
- **Elapsed-time features:** citizen tenure at request time (`opened_at - registered_at`) — note it is point-in-time correct by construction because registration precedes the request.

### 3. Encoding categoricals

Choice follows cardinality and consumer:

| Encoding | When | Watch out |
|---|---|---|
| **One-hot** (`pd.get_dummies`) | Low cardinality (channel: 4, region: 5) | Column explosion at high cardinality; fix categories so train/serve columns align (`pd.Categorical(values, categories=known)`) |
| **Ordinal** (explicit map) | True order exists (priority 1–4) | Never let alphabetical order masquerade as meaning |
| **Frequency / count** | Mid–high cardinality (46 categories, 17 municipalities) | Compute on training window only; document the window |
| **Target (mean) encoding** | High cardinality + supervised target | The leakage machine: encode with out-of-fold or time-prior means *only*; naive full-data target encoding is memorisation — demonstrated in the lab, not just asserted |
| **Leave as `category` dtype** | Downstream is gradient boosting with native categorical support | Interop documented |

The conceptual anchor: an encoding computed *from the same rows it will describe, using the target*, has smuggled the answer into the question. That sentence, internalised, prevents an entire failure class.

### 4. Numeric transforms, bins, ratios, and flags

- **Skew handling:** `np.log1p(resolution_hours)` tames the long tail (median 26h, max 2,100h); show the before/after histograms — this pre-answers Module 6's "why does the mean mislead".
- **Binning:** `pd.cut` (fixed, business-meaningful edges: the SLA bands) vs `pd.qcut` (data-driven quantiles). Business edges are stable and explainable; quantile edges shift with every rebuild — record them if you use them.
- **Ratios and rates** normalise away size: requests *per 10k population* (join `municipalities.population`) makes Riyadh comparable with Al-Baha; `reopened_count / (1 + prior_requests)` expresses reopen propensity. Edge-case discipline: `NULLIF`-equivalent guards (`np.where(denom > 0, num/denom, np.nan)`), and *decide* what 0/0 means in the domain rather than letting NaN decide for you.
- **Flags** encode domain knowledge cheaply: `is_resubmission` (same citizen, same category, within 7 days — a rolling self-join), `quality_score_missing` (Module 3's honesty flag, now revealed as a *feature*: MNAR missingness carries signal, and here is where it pays off).

### 5. Entity-history aggregates: features with memory, honestly

The strongest features in operational data summarise the past: "how many requests has this citizen opened before this one?", "what was this municipality's breach rate over the trailing 90 days?". They are also where leakage breeds. The rules:

- **Expanding history with exclusion of the present:** `gb.cumcount()` gives prior request count (strictly before, by construction). For prior *outcomes*: `gb["breach"].transform(lambda s: s.shift(1).expanding().mean())` — the `shift(1)` is load-bearing; without it, each row's own outcome contaminates its own feature.
- **Trailing windows over time, not rows:** municipality breach rate over trailing 90 *days* uses a time-based rolling window on a date-sorted frame — trailing-N-rows windows mean different durations in busy vs quiet municipalities.
- **The as-of principle generalised:** every history feature must be computable from data timestamped *strictly before* `opened_at`. Module 4's `merge_asof` is the same principle as a join; this module states it as the universal law: **a feature row may only see the past.**

### 6. Leakage, the feature dictionary, and common mistakes

**Target leakage:** the feature encodes the outcome (using `closed_at`-derived anything to predict breach; using `satisfaction_score` — collected after resolution — as an input). **Temporal leakage:** the feature uses information from after the decision moment (full-dataset means, this month's totals attached to mid-month rows). Detection heuristics taught: a feature "too good to be true" in a quick correlation check usually is; audit any feature whose computation touches columns timestamped after the decision point; when in doubt, re-derive the feature as-of and compare.

**The feature dictionary** is the module's governance artefact — one row per feature: name, plain-language definition, formula/source columns, availability time (what must have happened for it to exist), leakage review note, owner. It is the module's answer to "six months later, what is `res_vs_city_median_90d` and can we trust it?" — and it is a graded capstone deliverable.

**Common mistakes:** (1) target encoding on the full dataset (demonstrated failing in the lab); (2) trailing windows including the current row; (3) dividing by zero-able denominators without a decided policy; (4) one-hot at train time with categories that differ at serve time; (5) imported weekend definition (Sat–Sun) silently wrong for the region; (6) features nobody can define six months later — the dictionary exists because this *will* otherwise happen. **Production:** feature logic drifts from training to serving when reimplemented — the shared-feature-module principle (compute once, import everywhere) is the cure, and it is exactly what participants will meet as *feature stores* in the MLOps module (SDA-AIE-216) and the DS track.

## Code Examples

### Calendar features with Hijri reference data

```python
# src/features/calendar.py
"""Calendar features: Gregorian mechanics + Hijri reference data.
The Hijri mapping is DATA (maintained table), not code — it shifts yearly."""
import numpy as np
import pandas as pd

def add_calendar_features(df: pd.DataFrame, hijri: pd.DataFrame) -> pd.DataFrame:
    ts = df["opened_at"].dt.tz_convert("Asia/Riyadh")
    out = df.assign(
        opened_hour=ts.dt.hour,
        opened_dow=ts.dt.dayofweek,
        is_weekend=ts.dt.dayofweek.isin([4, 5]),          # Fri–Sat, NOT Sat–Sun
        opened_month=ts.dt.month,
        days_from_payday=(ts.dt.day - 27).abs().clip(upper=15),
        hour_sin=np.sin(2 * np.pi * ts.dt.hour / 24),
        hour_cos=np.cos(2 * np.pi * ts.dt.hour / 24),
        opened_date=ts.dt.date.astype("datetime64[ns]"),
    )
    out = out.merge(hijri[["gregorian_date", "is_ramadan", "is_eid"]],
                    left_on="opened_date", right_on="gregorian_date",
                    how="left", validate="many_to_one")
    assert out["is_ramadan"].notna().all(), "hijri table doesn't cover data range"
    return out.drop(columns=["gregorian_date", "opened_date"])
```

### Entity-history features (point-in-time correct)

```python
# src/features/history.py
"""History features: each row may only see the PAST.
Every function here must survive the as-of audit."""
import pandas as pd

def add_citizen_history(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("opened_at")                      # time order is the contract
    g = df.groupby("citizen_id", observed=True)

    df["citizen_prior_requests"] = g.cumcount()           # strictly before: 0 for first
    # Prior reopen rate: shift(1) excludes the CURRENT request's own outcome
    df["citizen_prior_reopen_rate"] = (
        g["was_reopened"]
        .transform(lambda s: s.shift(1).expanding().mean())
    )
    df["days_since_citizen_last_request"] = (
        df["opened_at"] - g["opened_at"].shift(1)
    ).dt.total_seconds() / 86400
    return df

def add_municipality_trailing(df: pd.DataFrame) -> pd.DataFrame:
    """Trailing 90-DAY breach rate per municipality, as of each request's opening.
    Time-based window: trailing-N-rows would mean different durations per city."""
    df = df.sort_values("opened_at")
    def trailing(s: pd.Series) -> pd.Series:
        return (s.shift(1)                                # exclude current row
                 .rolling("90D").mean())
    df["muni_breach_rate_90d"] = (
        df.set_index("opened_at")
          .groupby("municipality_id", observed=True)["breach"]
          .transform(trailing)
          .to_numpy()
    )
    return df
```

### The target-encoding leak, demonstrated then fixed

```python
# notebooks/day4_leakage_demo.ipynb (exported cells)
"""Demonstration: naive target encoding memorises; out-of-fold encoding generalises.
Run on the SLA-breach target with an 80/20 time split (train = 2023–2024, test = 2025)."""
import pandas as pd

train, test = df[df.opened_at < "2025-01-01"], df[df.opened_at >= "2025-01-01"]

# LEAKY: category encoded with the mean of the SAME rows it will describe
leaky_map = df.groupby("category_id", observed=True)["breach"].mean()

# HONEST: encoding computed on train only, applied to both;
# unseen categories fall back to the global train prior
prior = train["breach"].mean()
honest_map = train.groupby("category_id", observed=True)["breach"].mean()

for frame in (train, test):
    frame["cat_enc_leaky"] = frame["category_id"].map(leaky_map)
    frame["cat_enc_honest"] = frame["category_id"].map(honest_map).fillna(prior)

# Correlation with the target, train vs test — the leak's signature:
# leaky looks stronger on train and COLLAPSES less than you'd hope on test
# because 2025 rows contributed to their own encoding.
# leaky  : train r=0.31 | test r=0.29   ← inflated both sides (test leaked in)
# honest : train r=0.27 | test r=0.24   ← smaller, real, trustworthy
```

### The feature dictionary (governance artefact)

```python
# src/features/dictionary.py
"""Every feature ships with its documentation row. The build fails if a
feature column exists without a dictionary entry — governance as a test."""
FEATURE_DICTIONARY = [
    {
        "name": "muni_breach_rate_90d",
        "definition": "Municipality's SLA-breach rate over the 90 days "
                      "strictly before this request opened",
        "source": "requests_master: breach, opened_at, municipality_id",
        "available": "at request opening (uses only prior closed requests)",
        "leakage_review": "shift(1) + trailing window verified 2026-07; "
                          "as-of audit notebook 05_audit.ipynb",
        "owner": "analytics-foundation-cohort",
    },
    # ... one entry per feature, no exceptions
]

def check_dictionary(df, feature_cols):
    documented = {f["name"] for f in FEATURE_DICTIONARY}
    undocumented = set(feature_cols) - documented
    assert not undocumented, f"undocumented features: {sorted(undocumented)}"
```

## Hands-on Lab 5 — Engineer the SLA-Breach Feature Set

| | |
|---|---|
| **Objective** | Produce `features_v1.parquet`: 22+ documented, leakage-reviewed features at request grain for the SLA-breach question, plus the leakage demonstration run on your own data |
| **Duration** | 50 minutes (Day 4 H4) |
| **Setup** | `requests_master.parquet` from Lab 4; `hijri_calendar.csv` provided; skeleton `src/features/` |

**Tasks**
1. *(5 min)* Outcome quarantine: list every master-table column that is an *outcome* relative to request-opening time; these are banned as features for this target. (Expected list: closed_at, resolution_hours, status, satisfaction_score, reopened_count-as-final — 7 columns.)
2. *(10 min)* Calendar block: implement `add_calendar_features`; verify the Ramadan flag against known dates; plot request volume by `is_ramadan` × hour as a smoke test (evening shift visible).
3. *(10 min)* Encodings: one-hot channel, ordinal priority, frequency-encode category *computed on 2023–2024 only*; document the window in the dictionary.
4. *(15 min)* History block: citizen prior counts, prior reopen rate (with `shift(1)`), days-since-last, municipality trailing-90d breach rate. Run the as-of audit cell: recompute one feature for 20 sampled rows using only data before each row's `opened_at`; assert equality.
5. *(5 min)* Run the target-encoding leak demo on your own frame; record the four correlations.
6. *(5 min)* `check_dictionary()` passes; write `features_v1.parquet`; commit `lab5: leakage-reviewed feature set + dictionary`.

**Checkpoints & expected outputs**
```
Outcome quarantine: 7 columns banned, listed with reasons
Ramadan smoke test: evening (20:00–01:00) request share doubles in Ramadan ✓
As-of audit: 20/20 sampled rows match recomputation ✓
Leak demo: leaky r_train=0.31/r_test=0.29 vs honest 0.27/0.24 (±0.02)
features_v1.parquet: 487,000 × (spine keys + 22 features); dictionary complete
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `citizen_prior_reopen_rate` NaN everywhere | `shift(1)` on unsorted frame / groups of size 1 | Sort by opened_at first; NaN for first requests is *correct* — document it |
| Trailing 90d rate identical across cities | Forgot `groupby` before rolling | Group, then transform; check a two-city sample by hand |
| Ramadan flag all-False in 2024 | Hijri table year gap / date dtype mismatch on merge key | Assert coverage (the planted gap is March 2024); normalise both to datetime64 |
| Audit cell mismatches on 2 rows | Trailing window included current row | The `shift(1)` is missing in one function |
| Dictionary check fails | Feature added without entry | That is the feature working — write the entry |

**Instructor notes.** The as-of audit is the habit this module exists to install — 20 sampled rows, brute-force recomputation, equality assert; slow, unglamorous, and the difference between a feature set and a liability. The hijri-table coverage gap (March 2024 missing) is planted so the coverage assert earns its keep. Fast finishers: engineer one feature of their own invention, defend its mechanism in one sentence, and add it to the dictionary — the best ones get named in the debrief.

## Mini Exercises

**Quiz.** (1) Why is `satisfaction_score` banned as an SLA-breach feature? → collected after resolution; pure target-side leakage. (2) What does `shift(1)` accomplish in expanding history features? → excludes the current row's own outcome from its own feature. (3) Frequency encoding computed on the full dataset — what leaks? → test-period category volumes inform train rows (temporal leakage), and the encoding drifts irreproducibly. (4) When does cyclical encoding of hour matter, and when is it ceremony? → matters for linear/distance models; near-irrelevant for trees. (5) The regional weekend is which days, and where did the wrong default come from? → Fri–Sat; imported Sat–Sun assumptions in western-default code.

**Debugging exercise.** A provided feature set achieves suspicious 0.94 correlation between `avg_category_resolution` and breach — the feature was computed including each request's own resolution time *and* the full 2025 test period. Participants must identify both leaks and re-derive the honest version (r drops to 0.31).

**Code-review exercise.** Review a features PR: full-data target encoding, a rolling window without `shift`, `is_weekend` as Sat–Sun, a `pop_density` feature dividing by a zero-able denominator with no policy, and three undocumented features. Five findings; for each, state whether it corrupts offline metrics, production behaviour, or both.

**Discussion.** The operations manager proposes a feature: "crew supervisor name — some supervisors are just better." Discuss the stability, fairness, and governance dimensions before the technical ones. What would you build instead? (Trailing crew-level performance rates — behaviour, not identity.)

## Case Study — Churn Features at a Saudi Telecom Operator

**Scenario.** A national operator's churn model for prepaid mobile shows 0.91 AUC offline and performs barely better than random in production. The post-mortem finds the training table was built from a *current* snapshot: `days_since_last_topup` computed as of extraction date (not as of the prediction date), plan type reflecting post-churn downgrades, and a target-encoded `district` feature computed on the full labelled set.

**Business context.** The retention campaign budget (SAR 30M/year) was allocated on the model's offline lift projections; the campaign called the wrong customers for two quarters. Trust in the data-science team is now the scarcest resource in the building.

**Technical challenge.** Rebuild the feature pipeline point-in-time correct: define the prediction moment, reconstruct every feature as-of that moment, and design the audit that proves it.

**Constraints.** Source systems overwrite state (current plan, current balance) — history must come from event logs, which are complete for only 14 of 22 features; the model must score weekly on 8M subscribers within a 4-hour window; PDPL: location-derived features require minimisation review; the business insists on keeping "their" 22 features.

**Solution approach.** Prediction moment defined as Sunday 00:00 weekly; every feature re-derived from event logs as-of that moment (topup events → true `days_since_last_topup`; plan-change events → plan *at prediction time*); the 8 features without event history are either rebuilt from newly-logged state snapshots going forward (accepting a cold-start period) or retired with the business shown the leakage evidence per feature — the as-of audit (sample, recompute, compare) is run per feature and its results table *is* the retirement argument; district target-encoding replaced with trailing out-of-time churn rates; the weekly batch computes features with the same shared module used at training time (train/serve consistency — the SDA-FND-104 lesson that SDA-AIE-216 industrialises).

**Discussion questions.** (1) Why did the offline AUC *rise* from the leaks while production lift fell? Walk the mechanism. (2) Which of the lab's disciplines would have caught each of the three named defects, and at what cost versus the SAR 30M misallocation? (3) The business wants the retired features back "because they worked" — construct the two-minute explanation using the audit table. (4) What governance changes make this failure structurally harder to repeat? (Feature dictionary with availability column as a merge-gate requirement.)

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Outcome quarantine | Leakage discipline | 7/7 outcome columns identified | checklist vs key |
| As-of audit | Leakage discipline | 20/20 sampled rows reproduce | audit cell |
| Leak demo correlations | Understanding | four values within ±0.02 of reference | notebook |
| Feature count & coverage | Completeness | ≥ 22 features, ≥ 4 per family (calendar/encoding/ratio/history) | dictionary |
| Dictionary completeness | Governance | 100% features documented; check passes | `check_dictionary` |
| Build determinism | Engineering | identical parquet hash on re-run | hash comparison |
| Feature build wall-clock | Performance | ≤ 90 s on 487k rows | timed run |

**Example benchmark table:**

| Feature family | Count | Example | As-of audited | Notes |
|---|---|---|---|---|
| Calendar | 8 | is_ramadan, days_from_payday | by construction | Hijri via reference table |
| Encodings | 5 | cat_freq_2324 | window documented | train-window only |
| Ratios/flags | 5 | requests_per_10k_pop, quality_score_missing | n/a | denominator policy stated |
| History | 6 | muni_breach_rate_90d | 20/20 ✓ | shift(1) verified |

## Required Visuals and Training Assets

### Diagrams
1. **The decision-time line** — *Purpose:* the module's anchor: everything left of the line may be a feature, everything right is outcome. *Elements:* a request's lifecycle on a horizontal timeline (opened → assigned → closed → rated), a bold vertical line at `opened_at`, master-table columns placed on their true side, banned columns in red on the right. *Style:* timeline with column tokens; poster-sized — the capstone rubric references it.
2. **Leakage mechanism panel** — *Elements:* two flows: honest (train-window stats → applied forward) vs leaky (full-data stats looping back into their own rows), the loop drawn as a literal circular arrow labelled "the answer inside the question". *Style:* two-panel flow, red loop.
3. **Encoding decision tree** — *Elements:* cardinality and consumer branching to one-hot / ordinal / frequency / target-OOF / native category; leakage warnings on the target-encoding leaf. *Style:* compact flowchart, printable.
4. **Rolling window with shift(1)** — *Elements:* a row strip with the 90-day window drawn behind each row, the current row visibly excluded (hatched), one wrong panel including it with the contamination highlighted. *Style:* row-strip pair.

### Images (screenshots)
1. **Ramadan × hour heatmap** — *why:* the calendar feature earning its keep; *content:* request volume by hour, Ramadan vs non-Ramadan rows, evening shift obvious.
2. **Leak demo output cell** — *why:* the four correlations, participants verify their own; *content:* leaky vs honest, train vs test, annotated.
3. **As-of audit cell passing** — *why:* the habit artefact; *content:* 20-row comparison frame, all-equal assert.
4. **Feature dictionary rendered as a table** — *why:* the governance deliverable's look-and-feel; *content:* 6 columns × 8 example rows including a leakage_review entry.

### Simulations
1. **The 0.94 correlation trap** — *Setup:* provided leaky feature set (debugging exercise). *Expected:* participants find both leaks via the audit method, not by inspection luck. *Learning objective:* too-good-to-be-true has a procedure, not a feeling.
2. **Hijri coverage gap** — *Setup:* March 2024 missing from the reference table. *Expected:* the coverage assert fires; without it, silent all-False Ramadan flags. *Learning objective:* reference data is data — validate it like data.
3. **Train/serve category drift** — *Setup:* one-hot on 2023–24 train categories; 2025 introduces a new category. *Expected:* column mismatch at "serve" time; fixed with declared categories. *Learning objective:* encodings are contracts, not conveniences.

### Interactive Activities
- **Feature pitch round (15 min):** each pair invents one feature for the breach question and pitches it against the four tests (mechanism, availability, stability, interpretability); the class assigns it to "build / build-with-caution / reject" — rejected pitches with leakage are the most instructive.
- **Leakage line-up (10 min):** ten feature definitions on cards; teams sort into leaky/honest/depends and must state the decision-time argument for each. Two cards are genuinely "depends" (on the prediction moment) — that discussion is the point.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `hijri_calendar.csv` | Course reference (with planted March 2024 gap) | CSV | 1,096 rows | Calendar features + coverage lesson |
| `requests_master.parquet` | Lab 4 output | Parquet | 487k × 34 | Feature source |
| `features_v1.parquet` | **Lab output** | Parquet | 487k × ~28 | Capstone + M6 input |
| Leaky feature set | Instructor pack | Parquet | 487k × 6 | Debugging exercise |

### Demo Requirements
- **Instructor demo:** the target-encoding leak run live end-to-end — build leaky, show the flattering number, build honest, show the smaller true number, and *say out loud that smaller-but-real wins*; then one as-of audit performed by hand on a single row.
- **Student demo:** two pairs pitch their invented features (from the fast-finisher task) to the room.
- **Expected outputs:** `features_v1.parquet` + complete dictionary committed; every participant can state the decision-time rule unprompted — the wrap-up cold-calls three people for it.

---

# Module 6 — Exploratory Data Analysis and Visual Profiling

## Module Overview

**Purpose.** EDA is not "making some plots" — it is a disciplined interrogation: pose a question, choose the statistic or picture that answers it, interpret honestly, and let the answer generate the next question. This module teaches that loop on the master table participants now know intimately: univariate profiling and outlier reasoning, bivariate and categorical relationships, temporal structure, anomaly surfacing — and the craft of Matplotlib/Seaborn visuals that inform rather than decorate. It closes with the skill the whole week has been building toward: converting findings into written insight statements a decision-maker can act on.

**Business relevance.** EDA is where analysis earns or squanders its influence. A chart-dump deck gets a polite nod and no decision; three defensible findings with stated evidence and caveats redirect budgets. EDA is also the cheapest risk-management tool in AI: most modelling disasters (leakage, skew, population drift, label problems) are *visible in honest EDA* before a single model is trained — which is why both role tracks assume this competency on entry. And in government contexts, a misleading axis in a published chart is a public-trust incident, not a styling choice.

**Industry use cases.**
- A tourism authority explores visitor-flow data before commissioning a forecasting model and discovers the "growth trend" is one airport's scanner replacement — an EDA finding worth more than the model it corrected.
- A hospital operations team profiles ER arrivals and finds the Friday-evening staffing gap in ninety minutes of structured EDA on data they already had.
- A ministry's analysts EDA a new supplier dataset as due diligence: population coverage, missingness structure, and internal consistency — before any conclusions are allowed downstream.

**Expected competencies.** Participants can run the EDA loop systematically, profile distributions and justify outlier decisions, quantify and visualise relationships without confusing correlation for causation, decompose temporal patterns, choose chart types that match the question, apply visual-integrity rules, and write insight statements with evidence, magnitude, and caveat.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Conduct the EDA loop: question → evidence → interpretation → next question, documented as it runs | LO5 |
| 6.2 | Profile univariate distributions; detect and *reason about* outliers (error vs signal) | LO5, LO2 |
| 6.3 | Analyse relationships across numeric and categorical variables with appropriate statistics and plots | LO5 |
| 6.4 | Surface temporal patterns: trend, seasonality, and anomalies against expectation | LO5 |
| 6.5 | Apply chart-choice and visual-integrity principles in Matplotlib/Seaborn | LO6 |
| 6.6 | Write insight statements that carry evidence, magnitude, and caveat | LO6 |

## Technical Content

### 1. EDA as a disciplined loop

The failure mode to name on the projector: the aimless notebook — forty cells, thirty plots, zero sentences, ending in "…so yeah". The course's loop, enforced by notebook structure:

1. **Question** (markdown, before any code): "Do request volumes differ by channel across regions?"
2. **Evidence** (one cell): the table or plot that answers *that question* — not five plots hoping one speaks.
3. **Interpretation** (markdown, after): what the evidence says, what it doesn't, and the *next* question it raises.

Three loop-starters that structure any tabular EDA: **know your grain and population** (who is in this data, who isn't — the inspections match-rate finding from Module 4 returns here: inspected requests are *not* a random sample, and any conclusion about "quality" must carry that caveat); **profile before relating** (univariate before bivariate — you cannot interpret a correlation between two variables you haven't seen alone); **expected before observed** (write down what you expect first; surprise is only detectable against expectation — this is what separates exploration from confirmation-shopping).

### 2. Univariate profiling and the outlier decision

- **Central tendency honestly:** `resolution_hours` — mean 68h, median 26h. The gap *is* the finding: a long right tail. Reporting the mean alone would flatter no one and mislead everyone; the course rule is median + IQR for skewed operational metrics, mean only with its distribution shown.
- **Distribution pictures:** histogram (bin-width sensitivity demonstrated: 20 vs 200 bins tell different stories on the same data), ECDF (`sns.ecdfplot` — no binning choice at all, ideal for "what share resolves within 72h?" questions), boxplot (compact, but hides bimodality — show the two-humped counterexample once and the lesson sticks).
- **Outliers get a *decision*, not a deletion.** Detection is mechanical (IQR fences, |z| > 3 on log scale for skewed data); the decision is analytical. Course taxonomy: **error** (a 2,100-hour resolution that is a data defect → route back to Module 3's pipeline), **signal** (a genuine catastrophic case → *the most important row in the dataset* for an operations review), **different population** (bulk-registered municipal internal requests mixed in with citizen requests → segment, don't trim). Trimming outliers to "clean up the plot" is silently choosing answer (1) without investigation — say this bluntly.

### 3. Relationships: bivariate and categorical

- **Numeric × numeric:** scatter (with `alpha` at this row count, or `hexbin` beyond ~50k points); Pearson r for linear association, Spearman ρ when monotone-but-curved (resolution vs backlog is exactly this shape). Anscombe's quartet gets ninety seconds on the projector — same r, four wildly different realities — as permanent inoculation against unplotted correlations.
- **Numeric × categorical:** grouped medians with counts (`groupby.agg`), `sns.boxplot`/`violinplot` by group ordered by median (alphabetical ordering wastes the reader's effort). Every group comparison carries its n — a "worst municipality" with 40 requests is noise wearing a ranking.
- **Categorical × categorical:** crosstabs with `normalize=` chosen to match the question (row-share vs column-share answer *different questions* — demonstrate with channel × region both ways), heatmap for the eye.
- **Correlation ≠ causation, operationally:** municipalities with more crews have *worse* SLA rates — because crews are allocated to struggling municipalities (confounding by allocation policy). The class must produce this explanation themselves in Lab 6; EDA states associations and *candidate* mechanisms; causal claims need designs beyond this course (the honest pointer to DSC-213).
- **Simpson's reversal, live:** aggregate satisfaction favours the call-centre channel; within every priority stratum, the app wins — because urgent (low-satisfaction) requests disproportionately arrive by phone. Planted in the data; found in the lab; remembered forever.

### 4. Temporal structure and anomalies

- **Resample to the question's grain** (daily for operations, monthly for strategy); overlay a 7-day rolling mean rather than replacing the raw series — smoothing *hides* exactly the single-day anomalies operations cares about.
- **Seasonality by decomposition-lite:** month-of-year and day-of-week profiles (`groupby(month).median()` with year-over-year lines) before reaching for statistical decomposition — at Foundation level, the profile plots answer the business question and are explainable in the briefing.
- **Anomaly = deviation from expectation:** the day the app channel flatlines (planted: a 3-day outage in June 2024) is invisible in monthly data, obvious in daily with a day-of-week expectation. Anomalies in *counts* are often pipeline events, not world events — the analyst's first question is "did reality change or did the recording change?" (the tourism-scanner story, generalised).
- Missing-data structure over time is itself a finding: plot missingness rate by month — the satisfaction-score coverage drop after the 2025 survey redesign (planted) changes how any satisfaction trend must be read.

### 5. Visualisation craft with Matplotlib/Seaborn

Chart choice follows the question: distribution → histogram/ECDF; comparison across categories → ordered bars with n; relationship → scatter/hexbin; composition over time → stacked area (with the caveat that middle layers are hard to read); trend → line. Course integrity rules (graded in the capstone): bar charts of counts/amounts start at zero (line charts of rates need not — but say so on the axis); one message per chart, stated *in the title as a sentence* ("Roads requests breach SLA 3× more often in summer" not "SLA by month"); axes labelled with units; colour used for meaning, not decoration (and colourblind-safe palettes: `colorblind` in Seaborn); annotate the takeaway on the chart itself — the reader should not have to re-derive it; sorted categoricals; no dual y-axes (they manufacture correlation visually — show the two-panel alternative).

Mechanics taught through use: figure/axes API (not pyplot state machine — composability for small multiples), `sns.FacetGrid`/`catplot` for small multiples (the honest way to show 17 municipalities without spaghetti), `fig.savefig(dpi=150, bbox_inches="tight")` for report-grade exports, and a course style sheet (`sdaia_eda.mplstyle`) so every deliverable looks intentional.

### 6. Communicating findings: common mistakes & production considerations

**The insight statement** — the module's writing discipline. Formula: **finding (with magnitude) + evidence + caveat + implied action.** Weak: "Satisfaction varies by channel." Strong: "App-channel requests resolve 31% faster than call-centre requests at the same priority (median 19h vs 27.5h, 2025, n=214k), though app users skew toward urban municipalities — channel-shift investment should be evaluated per region." Every capstone finding must parse into these four parts; the rubric checks each.

Report structure taught (and used in the capstone): one-page executive summary (findings ranked by decision-relevance, not discovery order) → method and data-quality notes (the Module 3 scorecard and Module 4 match rates *belong here*, visible) → findings with charts → appendix (reproducibility pointer to the notebook). The notebook is the lab record; the report is the communication — confusing the two produces forty-page chart dumps.

**Common mistakes:** (1) plots without questions (decoration); (2) mean-reporting on skewed distributions; (3) trimming outliers without the error/signal/population decision; (4) unordered categorical axes; (5) correlation language sliding into causal language ("drives", "leads to") without a design that supports it; (6) findings without n or time window; (7) the missing denominator — "312 complaints in Al-Kharj" means nothing without per-10k-population context (Module 5's ratio features exist for this). **Production:** EDA notebooks are working documents — dated, re-runnable top-to-bottom, data version pinned; published charts carry source and date; under PDPL, small-n group breakdowns can re-identify individuals — the course rule is no published cell below n=20, which is also good statistics.

## Code Examples

### The loop, as notebook structure

```python
# notebooks/eda_master.ipynb — cell sequence for one loop iteration
# ── markdown ─────────────────────────────────────────────
# ## Q7: Does resolution time differ by channel, controlling for priority?
# Expectation (written BEFORE looking): app faster — digital intake skips
# call-centre transcription. Risk: channel correlates with municipality.

# ── code ─────────────────────────────────────────────────
import seaborn as sns
import matplotlib.pyplot as plt

closed = master[master["closed_at"].notna()]
tbl = (closed.groupby(["priority", "channel"], observed=True)
             .agg(median_hours=("resolution_hours", "median"),
                  n=("request_id", "count"))
             .reset_index())

g = sns.catplot(data=closed, x="channel", y="resolution_hours",
                col="priority", kind="box", showfliers=False,
                order=["app", "web", "call_center", "walk_in"],
                height=3, aspect=0.9)
g.set(yscale="log")          # long tail: log scale or the boxes are pancakes
g.figure.suptitle("App requests resolve fastest at every priority level", y=1.03)

# ── markdown ─────────────────────────────────────────────
# Finding: app median 19h vs call-centre 27.5h (P2, n=214k) — holds at all
# priorities, so it is not a priority-mix artefact. Caveat: app share is 71%
# urban; next loop → Q8: does the gap survive within-municipality comparison?
```

### Honest distribution profiling

```python
# notebooks/eda_master.ipynb (univariate cell)
"""Mean vs median as a finding, and the ECDF for threshold questions."""
res = closed["resolution_hours"]
print(f"mean {res.mean():.0f}h | median {res.median():.0f}h | "
      f"p90 {res.quantile(.9):.0f}h | max {res.max():.0f}h")
# mean 68h | median 26h | p90 142h | max 2,102h  ← the tail IS the story

fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
axes[0].hist(res.clip(upper=400), bins=80)
axes[0].set(title="Resolution hours (clipped at 400 for display — noted!)",
            xlabel="hours", ylabel="requests")
sns.ecdfplot(res, ax=axes[1])
axes[1].axvline(72, ls="--", c="grey")
axes[1].annotate("81% resolve within 72h", xy=(72, 0.81),
                 xytext=(200, 0.6), arrowprops={"arrowstyle": "->"})
axes[1].set(title="ECDF: share resolved by X hours", xlabel="hours")
fig.tight_layout()
```

### Simpson's reversal check (course-standard pattern)

```python
# notebooks/eda_master.ipynb (stratification cell)
"""Any aggregate group comparison gets a stratified counterpart before it
is allowed to become a finding."""
overall = closed.groupby("channel", observed=True)["satisfaction_score"].mean()
by_stratum = (closed.groupby(["priority", "channel"], observed=True)
                    ["satisfaction_score"].mean().unstack())

# overall: call_center 3.61 > app 3.48        ← aggregate story
# by_stratum: app wins in EVERY priority row   ← stratified truth
# Mechanism: urgent requests (low satisfaction) arrive disproportionately
# by phone. The aggregate compares different mixes, not different channels.
```

### Daily anomaly surfacing against expectation

```python
# notebooks/eda_master.ipynb (temporal cell)
"""Anomaly = deviation from day-of-week expectation, not from the mean."""
daily = (master.set_index("opened_at")
               .groupby([pd.Grouper(freq="D"), "channel"], observed=True)
               .size().rename("n").reset_index())

app = daily[daily["channel"] == "app"].set_index("opened_at")
app["dow_expected"] = (app.groupby(app.index.dayofweek)["n"]
                          .transform("median"))
app["ratio"] = app["n"] / app["dow_expected"]

anomalies = app[app["ratio"] < 0.35]
# 2024-06-11 … 2024-06-13: ratio ≈ 0.04 — the app outage, invisible monthly.
# First question is NOT "what happened in the city?" but
# "did the recording change?" — check other channels the same days:
# call_center ratio ≈ 1.6 the same days → demand displaced, not absent. Outage.
```

## Hands-on Lab 6 — The EDA Sprint

| | |
|---|---|
| **Objective** | Produce five defensible findings on the master table using the loop discipline — each with question, evidence, interpretation, and a report-grade chart; at least one temporal, one stratified, one involving data-quality structure |
| **Duration** | 50 minutes (Day 5 H2), flowing into capstone work H3–H4 |
| **Setup** | `requests_master.parquet` + `features_v1.parquet`; `sdaia_eda.mplstyle`; starter notebook with the loop skeleton |

**Tasks**
1. *(5 min)* Population statement: write the five-line "who is in this data" preamble (grain, window, exclusions, known coverage gaps from Modules 3–4).
2. *(10 min)* Univariate sweep: resolution hours, satisfaction (with coverage), volumes — mean/median gaps flagged; one outlier investigated to an error/signal/population verdict.
3. *(15 min)* Two relationship loops minimum: the channel question (with the Simpson's check — it is planted; find it) and one of your own.
4. *(10 min)* Temporal loop: daily volumes by channel against day-of-week expectation; identify and *diagnose* the June 2024 anomaly (recording vs reality — the displaced-demand check).
5. *(10 min)* Write the five insight statements in the four-part formula; export the five charts via `savefig`; peer-swap: your pair must reconstruct each finding from statement + chart alone — anything they can't reconstruct gets rewritten.

**Checkpoints & expected outputs**
```
Population preamble: 487k requests, 2023–2025, inspections non-random (2.4%,
  triggered by reopens), satisfaction coverage drops 2025-03 (survey redesign)
Simpson's: aggregate call_center > app; stratified app wins all priorities ✓
Anomaly: 2024-06-11/13 app ratio 0.04 with call_center 1.6 → outage, displaced demand
Outlier verdict: 2,102h case = signal (genuine escalation), documented not trimmed
5 insight statements passing the four-part parse; charts pass integrity checklist
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Boxplots are unreadable pancakes | Long tail on linear scale | Log scale or showfliers=False — and *note the choice on the chart* |
| "Worst municipality" finding | n=40 group ranked against n=40,000 | Show n with every group statistic; minimum-n rule |
| Anomaly hunt finds Eid, not the outage | Deviation measured from overall mean | Day-of-week expectation baseline; holidays are *expected* deviations |
| Correlation heatmap of everything | Plot-first, question-never | Delete it; loops start with questions — heatmaps are indexes, not findings |
| Satisfaction "trend" discovered | Coverage change (2025 redesign) read as level change | Plot coverage alongside; the M3 scorecard warned you |

**Instructor notes.** The peer-reconstruction test in task 5 is the module's assessment in miniature — enforce it strictly; it converts "I have plots" into "I have findings" in twenty minutes. Both planted discoveries (Simpson's, the outage) should be *found*, not revealed: circulate and nudge with questions ("is your channel comparison comparing the same requests?"), never answers. The satisfaction-coverage trap catches teams who skipped their own Module 3 scorecard — poetic, and worth saying aloud.

## Mini Exercises

**Quiz.** (1) Mean 68h, median 26h — what does the gap tell you and which do you report? → strong right skew; median (+ distribution) for operational claims. (2) Your "insight" compares group means across categories with n from 40 to 40,000 — what is missing? → per-group n and a minimum-n rule. (3) A count anomaly appears in one channel only — first hypothesis? → recording/pipeline change; check displacement in other channels. (4) Why are dual y-axes banned? → the scale choice manufactures visual correlation; two panels are honest. (5) Rewrite as an insight statement: "requests are seasonal." → e.g. "Summer months carry 34% more requests than the annual median (2023–25, all regions), concentrated in Roads and Water — seasonal crew allocation should front-load Q3."

**Debugging exercise.** A provided notebook concludes "satisfaction improved 0.4 points in 2025". Three defects stack: coverage dropped (redesign), the mean is computed over the rated subset (Module 1's lesson), and the channel mix shifted toward app. Participants must decompose how much each contributes and write the honest replacement statement.

**Code-review exercise.** Review a findings deck: truncated bar axis exaggerating a 3% difference, a dual-axis chart implying correlation, causal verbs on associations, an unordered 17-bar municipality chart, and a small-n district breakdown (n=11, PDPL flag). Five findings; propose the fix for each.

**Discussion.** Your EDA surfaces that one municipality's numbers are almost certainly a recording artefact — publishing the ranking as-is embarrasses them unfairly; withholding it looks like suppression. What does honest publication look like? (Annotation, footnote discipline, and the quality scorecard shipped with the ranking.)

## Case Study — Visitor-Flow EDA for a Tourism Authority

**Scenario.** A tourism authority receives monthly visitor estimates for 28 destinations from three sources (border systems, mobile-operator movement data, hotel registrations) and wants a forecasting model. The analytics team is given two weeks of EDA first — over the objections of a vendor who proposed skipping straight to modelling.

**Business context.** Destination-marketing budgets (nine figures annually) follow the visitor numbers. Last year's flagship "42% growth" figure at one destination — celebrated publicly — later proved to be a border-system scanner upgrade that changed counting methodology mid-year.

**Technical challenge.** Structure the two-week EDA to establish: which sources agree where and when; what each source's population actually is; which apparent trends are methodology artefacts; and whether the data supports destination-level forecasting at all.

**Constraints.** Mobile-operator data arrives pre-aggregated (PDPL minimisation — no unit records, minimum cell size already applied); sources use different destination boundaries; the scanner-upgrade dates are documented for only one of six border posts; the vendor's model deadline pressure is political, not technical.

**Solution approach.** Week 1: population statements per source (border = entries, mobile = presence, hotels = commercial overnight — three *different* quantities, none wrong); pairwise source-agreement analysis by destination-month (scatter + ratio time series — a level shift in a ratio series is a methodology fingerprint, the scanner story generalised into a detection method); boundary reconciliation table. Week 2: temporal structure per destination (Hajj/Umrah seasonality vs school-holiday seasonality vs weekend micro-cycles — different destinations breathe on different calendars); anomaly census with recording-vs-reality verdicts; a data-readiness scorecard per destination. Deliverable: an EDA report whose first finding is that 9 of 28 destinations lack forecastable series — redirecting the modelling scope *before* the spend, which is the entire argument for EDA-first.

**Discussion questions.** (1) Why is the ratio-of-sources time series a better methodology-change detector than any single source's level? (2) The three sources measure three populations — construct the sentence that lets a non-technical director hold all three at once. (3) The vendor argues the model will "learn around" the artefacts. Rebut with this week's concepts (an uncontrolled level shift is temporal leakage's cousin: the model learns the scanner, not the tourists). (4) Which parts of the two-week plan are Lab 6's tasks at institutional scale?

## Benchmarks and Evaluation

| Metric | Category | Target | Measured with |
|---|---|---|---|
| Loop discipline | Method | 100% of findings carry question-before + interpretation-after | notebook review |
| Population preamble | Method | present, ≥ 4 coverage facts from M3/M4 artefacts | review |
| Planted discoveries | Correctness | Simpson's + outage found and correctly diagnosed | debrief |
| Insight-statement quality | Communication | 5/5 parse into finding/evidence/caveat/action | rubric |
| Chart integrity checklist | Communication | 10/10 items on all exported charts | checklist |
| Peer reconstruction | Communication | ≥ 4/5 findings reconstructable by the pair | lab observation |
| Notebook reproducibility | Engineering | restart-and-run-all clean | spot run |

**Example benchmark table:**

| Finding | Evidence type | n | Caveat carried | Reconstruction |
|---|---|---|---|---|
| App resolves 31% faster (median, per priority) | stratified boxplots + table | 214k | urban skew | ✓ |
| June 2024 app outage displaced ~9k requests to phone | dow-expectation ratios | 3 days | single incident | ✓ |
| Satisfaction "trend" is coverage artefact | coverage-alongside plot | — | redesign date | ✓ |

## Required Visuals and Training Assets

### Diagrams
1. **The EDA loop** — *Purpose:* module anchor. *Elements:* question → evidence → interpretation → next-question cycle; artefact icons (markdown, one chart, markdown); a struck-out side path labelled "40 plots, 0 sentences". *Style:* cycle diagram matching Module 3's loop visually (deliberate rhyme: profile-clean loop, question-evidence loop).
2. **Chart-choice matrix** — *Elements:* question types (distribution/comparison/relationship/trend/composition) × recommended charts with mini-thumbnails; hazard icons on pie-for-many-categories and dual-axis cells. *Style:* poster grid, printable A3 — participants keep it.
3. **Simpson's reversal, drawn** — *Elements:* the actual course numbers: aggregate bars (call-centre ahead) exploding into per-priority panels (app ahead in each), with the mix table that reconciles them. *Style:* one-to-many exploded panel.
4. **Anatomy of an insight statement** — *Elements:* the strong example sentence colour-coded into finding/evidence/caveat/action segments; the weak version beside it, mostly grey. *Style:* annotated typography card; reused in the capstone rubric.

### Images (screenshots)
1. **The loop in a real notebook** — *why:* structure participants replicate; *content:* markdown-code-markdown triplet from the example, rendered.
2. **Bin-width sensitivity pair** — *why:* histogram literacy; *content:* same data at 20 and 200 bins with different apparent stories.
3. **The outage in daily vs monthly views** — *why:* resolution-grain lesson; *content:* flat monthly line vs daily crater with dow-expectation band.
4. **A rubric-passing capstone chart** — *why:* target quality reference; *content:* sentence-title, annotated takeaway, ordered categories, n shown, source+date footer.

### Simulations
1. **Simpson's planted reversal** — *Setup:* in the data as shipped. *Expected:* found via the stratification-check rule. *Learning objective:* aggregate comparisons compare mixes.
2. **The coverage-artefact trend** — *Setup:* satisfaction survey redesign 2025-03 (coverage 58% → 31%). *Expected:* naive trend claim; caught by coverage-alongside plotting. *Learning objective:* metric changes vs measurement changes.
3. **The app outage** — *Setup:* 3-day June 2024 flatline with call-centre displacement. *Expected:* found only at daily grain with dow expectation; correctly attributed to recording/channel shift, not demand change. *Learning objective:* anomaly diagnosis procedure.

### Interactive Activities
- **Chart makeover clinic (15 min):** four deliberately bad charts (dual-axis, truncated bars, rainbow 17-line spaghetti, unordered categories) projected; the room redesigns each verbally before pairs implement one.
- **Insight-statement slam (10 min):** pairs read their strongest statement aloud; the room scores the four parts on fingers; missing parts get supplied live. Fast, public, and it calibrates the whole cohort before the capstone.

### Datasets
No new datasets — Module 6 is the payoff of the golden thread: the master table and features, carrying every planted structure (Simpson's, outage, coverage break, non-random inspections) that Modules 1–5 built the tools to handle.

### Demo Requirements
- **Instructor demo:** one full loop live on the projector — question written first, expectation stated, one chart, interpretation typed in real time including a caveat; then the Simpson's reveal done *as a failure*: present the aggregate finding confidently, invite objections, stratify, recant. Rehearse the recant — modelling intellectual honesty is the demo.
- **Student demo:** two pairs present one finding each under the slam format.
- **Expected outputs:** five findings per pair, charts exported, statements written — one hour later this *is* the capstone's core, by design.

---

# Final Capstone Project

## Title: From Raw Records to Ministerial Brief — EDA on a Government Service Dataset

## Project Scenario

You are the analytics unit supporting a deputy ministry responsible for municipal services (the government-style context the whole course has inhabited). The deputy minister's office has asked one question, three weeks before the annual budget cycle: **"Where is municipal service delivery failing citizens, why, and what should we look at first?"** You hold the `city_services` database, the field extracts, and everything you built this week. Your mandate: deliver an analysis-ready dataset, a rigorous exploratory analysis, and a written brief with visuals that a non-technical decision-maker can act on — with every number defensible under challenge, because the office *will* challenge them. This capstone folds in the course's seventh topic (the EDA case study on a real government-style dataset) as its living core: the case study is not read about, it is performed.

## Requirements

**Mandatory (maps to grading rubric):**

1. **SQL extraction (LO1):** the analytical extract is produced by SQL you wrote — at minimum one multi-table join, one aggregation, and one window function, each with a stated grain and a row-count sanity check. Fan-out anywhere in the lineage is a capped criterion (see instructor notes).
2. **Data-quality assessment (LO2):** a quantified quality scorecard (six dimensions) covering every source used; the messy extracts cleaned through your reproducible pipeline; a decision log covering 100% of mutations; residue (quarantine/unparseable) reported, not hidden.
3. **Analysis-ready master table (LO3):** one-row-per-request table assembled with validated merges (`validate=` on every merge), match-rate reports included as quality disclosures, spine grain preserved and asserted, dtype-disciplined parquet artefact.
4. **Engineered features (LO4):** ≥ 10 features spanning at least three families (calendar, encoding, ratio/flag, history), each documented in the feature dictionary with an availability/leakage note; at least one history feature passing a demonstrated as-of audit.
5. **Exploratory analysis (LO5):** ≥ 6 findings produced through the loop discipline (question before, interpretation after), including at least one temporal pattern, one stratified comparison (with the Simpson's check shown), one anomaly with a recording-vs-reality verdict, and one finding *about the data itself* (coverage/quality structure).
6. **Communication (LO6):** a written report — one-page executive summary, method & data-quality notes, findings with report-grade charts (integrity checklist compliant), reproducibility appendix — plus a 10-minute briefing. Every finding parses as finding/evidence/caveat/action.
7. **Reproducibility:** one command (or one documented sequence) rebuilds every artefact from raw; notebooks pass restart-and-run-all; raw data untouched.

**One extension (choose at least one):**
- **Regional deep-dive:** a two-page annex on one region with district-level analysis (minimum-n rule enforced — PDPL-aware small-cell suppression demonstrated)
- **The equity lens:** requests-per-10k-population and resolution-time comparison across municipality population sizes, with the confounding discussion done properly
- **Quality early-warning:** a re-runnable script that recomputes the quality scorecard on a fresh extract and diffs against baseline, flagging degradations
- **Interactive appendix:** the five key charts rebuilt as a linked small-multiple dashboard page (Matplotlib/Seaborn static grid is acceptable; the design is what's graded)
- **SQL-only replication:** one pandas finding replicated entirely in SQL (CTEs + windows) with a short note on where each tool earned its place

## Architecture (target state)

```
PostgreSQL (city_services)                 messy extracts (CSV)
        │  SQL: joins/agg/windows                  │  profiling report
        │  grain + row-count checks                │  cleaning pipeline + decision log
        ▼                                          ▼
  requests extract (parquet) ──── validated merges (validate= / match rates)
                                   merge_asof (rosters) ──► requests_master.parquet
                                                                  │
                                             feature build (dictionary + as-of audit)
                                                                  ▼
                                                        features_v1.parquet
                                                                  │
                                              EDA loop notebook (6+ findings)
                                                                  ▼
                              REPORT.pdf (exec summary · quality notes · findings)
                                          + 10-minute panel briefing
```

## Deliverables

1. Repository (or structured folder) with: SQL files, `src/wrangling/` + `src/features/` pipelines, notebooks, and a README stating the rebuild sequence
2. Artefacts: cleaned parquets, `requests_master.parquet`, `features_v1.parquet`, `cleaning_log.json`, quality scorecard, feature dictionary
3. `REPORT.pdf` (6–10 pages: 1-page executive summary, method & quality notes, findings, appendix)
4. 10-minute briefing (max 8 slides or the report's charts) delivered to the assessment panel, with 5 minutes of challenge questions
5. `DECISIONS.md`: five one-paragraph analytical decisions with rationale (e.g., outlier verdicts, imputation choices, why a finding was demoted after a caveat surfaced)

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: SQL extract + sanity checks (Labs 1–2 consolidated) | End Day 2 | PA-1 + spot-check of grain comments |
| M-B: cleaned extracts + scorecard (Lab 3) | End Day 3 | pipeline re-run reproduces log |
| M-C: master table + feature set (Labs 4–5) | End Day 4 | validation cell green; dictionary complete |
| M-D: six findings drafted (Lab 6 + capstone H3) | Day 5 H3 | peer reconstruction test passed |
| M-E: report + briefing | Day 5 H5 | rubric scoring by panel |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| SQL extraction & correctness | 15 | Joins/agg/windows correct with grain discipline and checks; SQL readable as CTE pipelines | Correct results; thin verification or grain comments | Fan-out in lineage, unverified counts, monolithic queries |
| Data-quality work | 15 | Scorecard quantified; pipeline reproducible; decision log complete; residue honestly reported | Cleaning sound; log or residue reporting partial | Cell-soup cleaning, raw overwritten, defects silently passed |
| Master-table engineering | 15 | All merges validated with match-rate disclosures; grain asserted; dtype-disciplined artefact | Table correct; discipline partially evidenced | Unvalidated merges, silent fan-out, CSV-degraded types |
| Feature engineering | 10 | ≥10 documented features, 3+ families; as-of audit shown; no leakage | Features sound; documentation or audit thin | Leaky or undocumented features |
| EDA depth & honesty | 25 | 6+ loop-disciplined findings incl. temporal, stratified (Simpson's shown), anomaly verdict, data-about-data; expected-vs-observed reasoning visible | Findings correct but loop discipline uneven; 1 required type missing | Chart dump, unstratified comparisons, anomalies unexplained |
| Communication | 15 | Exec summary decision-ranked; all statements parse 4-part; charts pass integrity checklist; briefing survives challenge | Report solid; some statements or charts below standard | Chart-dump report, causal overreach, unlabeled/misleading visuals |
| Reproducibility & decisions doc | 5 | One-command rebuild; restart-and-run-all clean; DECISIONS.md shows judgement | Rebuild works with friction | Cannot rebuild own artefacts |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the artefacts first* (re-run the pipeline, read the decision log and match rates, spot-run the notebook), the briefing second — the course's thesis is that the work should testify for itself.
- Anti-pattern flags that cap a criterion at 70%: any merge without `validate=`; outliers trimmed without a verdict; a finding whose stratified check was skipped; satisfaction claims without coverage disclosure; group rankings without n.
- Verify one claim live in the challenge round: pick a number from the executive summary and ask the team to trace it to the cell that produced it, within two minutes.
- Panel composition: instructor + one guest playing the non-technical director; the director asks only plain-language questions — teams must answer without jargon (a graded communication behaviour).
- The planted structures (Simpson's reversal, June 2024 outage, coverage break, non-random inspections) form the reference finding set; strong teams find 3–4 of them *plus* something the course team didn't plant — reward the latter explicitly.

## Bonus Tasks (for early finishers / distinction seekers)

1. Replicate the trailing-90-day municipality breach rate in pure SQL (window frame `RANGE BETWEEN INTERVAL '90 days' PRECEDING AND CURRENT ROW` minus current row) and reconcile against the pandas version
2. Quantify the June 2024 outage's displaced demand with a counterfactual dow-expectation estimate and a stated uncertainty range
3. Build the quality scorecard diff tool (extension 3) and run it against a provided "next quarter" extract with two new planted defects
4. Draft the one-page NDMO-style data-quality disclosure that would accompany public release of the municipal rankings

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** `WHERE satisfaction_score != 5` excludes which rows? → score = 5 **and** all NULL scores (three-valued logic).
**Q2.** `COUNT(*)` vs `COUNT(closed_at)` — the difference means what? → total vs closed; the gap is the open backlog (and a completeness metric).
**Q3.** Correct predicate for "all of March 2025"? → half-open range: `>= '2025-03-01' AND < '2025-04-01'`.
**Q4.** LEFT JOIN then WHERE on a right-side column does what? → silently becomes INNER; move the condition to ON or accept INNER.
**Q5.** Your 1:1 join returned more rows than the left table — first diagnostic? → group the right side by key, `HAVING count(*) > 1`.
**Q6.** Why can't WHERE filter a window function? → windows evaluate after WHERE; wrap in a CTE and filter outside.
**Q7.** LAG without PARTITION BY across regions causes what? → boundary bleed: each region's first row sees the previous region's last value.
**Q8.** Name the three missingness mechanisms with one example each. → MCAR (flaky export), MAR (paper forms lack GPS), MNAR (angry citizens skip the survey).
**Q9.** Why load a messy CSV with `keep_default_na=False` first? → to observe disguised missingness (sentinels, empty strings) before declaring it.
**Q10.** Why is one permissive `pd.to_datetime` pass on mixed formats dangerous? → per-row day/month guessing corrupts silently; parse each format explicitly on its matched subset.
**Q11.** Exact duplicate vs key conflict — the operational difference? → exact rows drop safely; same key + different values needs a stated resolution rule.
**Q12.** Which merge argument catches unexpected cardinality, and what does it cost? → `validate=`; nothing.
**Q13.** `agg` vs `transform` output shapes, and transform's SQL cousin? → per-group vs per-row; window functions.
**Q14.** When is `merge_asof` correct where an exact-key merge is wrong? → effective-dated reference data ("what was in force at that time").
**Q15.** An int key column shows `1024.0` after a merge — cause and fix? → NaN forced float64; nullable `Int64`.
**Q16.** Why is `satisfaction_score` banned as an SLA-breach feature? → collected after resolution — target-side leakage; violates decision-time availability.
**Q17.** What does `shift(1)` do in a trailing history feature and what breaks without it? → excludes the current row's own outcome; without it each row leaks into itself.
**Q18.** Naive full-data target encoding fails how? → the answer is smuggled into the question: inflated offline metrics, no production value.
**Q19.** Mean 68h vs median 26h — what do you report for an operational SLA claim and why? → median (+ distribution/ECDF); the tail makes the mean unrepresentative.
**Q20.** A group comparison flips direction after stratification — name the effect and the course rule that catches it. → Simpson's reversal; every aggregate group comparison gets a stratified counterpart before becoming a finding.

## Practical Assessments

**PA-1 — SQL practical (30 min, Day 2 H5, individual):** against a fresh scratch schema (same shape, different values), produce: one three-table aggregation with a grain comment, one top-N-per-group, one LAG-based change query, and one fan-out proof-and-fix. Scored: correctness of results (50%), grain/verification discipline (30%), readability (20%). Auto-checked against golden results; discipline scored by rubric.

**PA-2 — Wrangling practical (30 min, Day 4 H5, individual):** given a small messy CSV (6 planted defects) and a spine table, deliver a cleaning function with counts logged and a validated merge with match-rate report. Scored: defects found and treated (40%), pipeline reproducibility (30%), merge discipline (30%).

**PA-3 — Capstone (rubric above):** the EDA project with report — 40% of course grade. SQL labs + PA-1/PA-2 and lab completion — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (6 labs) | 25% | committed artefacts + checkpoint outputs |
| PA-1 (SQL practical) | 15% | golden-result check + rubric |
| PA-2 (wrangling practical) | 10% | rubric |
| Quiz | 10% | 10-question selection |
| Capstone: EDA project with report | 40% | rubric, artefact-first |

Badge issuance (Foundation badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical decision logs or identical "original" findings across teams are checked). The badge counts toward the AI & Data Foundations Certificate (SDA-FND-101→105) and satisfies the SDA-FND-104 prerequisite for SDA-AIE-111, SDA-DSC-111, SDA-DSC-112, and SDA-DSC-214.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Rebuild the `city_services` Docker image from the course generator; verify all planted structures land (NULL-trap counts, fan-out totals, Simpson's reversal, June 2024 outage, 2025 coverage break, missing SLA targets, hijri gap) against `PLANTED_ANSWERS.md`
- [ ] Run all six labs plus PA-1/PA-2 end-to-end on a clean machine **and** the hosted fallback (JupyterHub + shared PostgreSQL)
- [ ] Load `field_inspections.csv`, `satisfaction_callbacks.csv`, `crew_rosters.parquet`, `hijri_calendar.csv`, and the reference cleaned/master parquets (`data/clean_reference/`) onto the shared drive
- [ ] Create the PA-1 scratch schema with regenerated values; verify golden results
- [ ] Print A2/A3 posters: the ERD, join-type gallery (no Venn!), decision-time line, chart-choice matrix; print desk cards: logical query order, three-valued logic, insight-statement anatomy
- [ ] Set the analyst-role statement timeout (60 s) on the classroom database; test the runaway-query demo
- [ ] Prepare the shared leaderboard (sanity anchors, fan-out numbers, benchmark timings) and the whiteboard corner for the "1,214 missing SLA targets" running gag
- [ ] Invite and brief the Day 5 panel guest (the "non-technical director" role — plain-language questions only)
- [ ] Confirm classroom network allows PyPI (or mirror configured) and that Docker Desktop installs are pre-approved by participants' IT

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git
- [ ] Docker Desktop (WSL2 on Windows) — used only to run the course database; verify `docker run hello-world`
- [ ] `pip install pandas pyarrow sqlalchemy "psycopg[binary]" jupyterlab matplotlib seaborn`
- [ ] A SQL client (psql included with the container; DBeaver or pgAdmin optional)
- [ ] Clone the course repository; run `python scripts/doctor.py` (validates versions, pulls the DB image, runs one test query, prints ✓/✗ per item)
- [ ] Reply to the email with the doctor script's output

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Docker/WSL2 not enabled on Windows laptops | High | Pre-session email + first-hour floater; hosted DB fallback needs zero local install |
| SQL-comfortable participants racing ahead on Days 1–2, pandas-comfortable on Days 3–4 | High | The designed pairing rotation; fast-finisher tracks exist in every lab |
| `!= NULL` and `= NULL` habits from other tools | High | The Q7 trap handles it; reinforce with the desk card |
| Excel instincts: editing values by hand / in place | Medium | Raw-immutability rule stated Day 3 Hour 1 and enforced in review; the reproducibility diff test catches violations |
| Arabic text rendering issues in terminals/plots | Medium | UTF-8 client encoding; provide the tested matplotlib font config (`Noto Naskh Arabic`) in the style sheet |
| `SettingWithCopyWarning` panic | Medium | Teach the `.loc`/pipeline pattern once, Day 3; it recurs less with `.pipe()` style |
| Participants "improving" the master table schema mid-Day-5 | Medium | Freeze the schema at M-C; changes require re-running the validation cell — usually self-deterring |
| Slow laptops on the 487k-row feature build | Low | The dtype pass halves memory; reference parquets unblock anyone; pair on the stronger machine |
| Timezone confusion (UTC storage vs Riyadh display) | Low | The convert-once-at-load rule; one desk-card line |

## Timing Recommendations

- Protect Lab 3 and Lab 6 at full length — quality discipline and the EDA loop are the module's soul; compress Module 4's reshaping drills (Section 2) if behind, never its merge discipline (Section 3).
- If a cohort is strong: pull the SQL-only replication bonus into Day 2, and let Day 5 H3 start capstone drafting early.
- If a cohort is weak: convert Lab 5's history-feature block to guided live-coding; never drop the leakage demo or the as-of audit — they are the course's thesis for the ML-bound.
- Hard rule: capstone assembly (Day 5 H4) starts on time; cut discussion, not drafting time. Reports beat rehearsals — a rough briefing of solid findings outscores a polished briefing of thin ones, and the rubric reflects that.
- The planted discoveries must be *found*, not announced. If by mid-Lab-6 no pair has the Simpson's reversal, nudge with the stratification-check rule, not the answer.

## Discussion Prompts (use during transitions)

1. "What is the most expensive wrong number you have seen survive into a leadership deck — and at which of this week's stages would it have died?"
2. "Your database enforces types and keys; your CSV enforces nothing. What else in your organisation is a CSV pretending to be a database?"
3. "The mean says 68 hours, the median says 26. Which number does the citizen feel — and which one goes in the press release?"
4. "Who should own the master table once three teams depend on it — and what does your answer imply about whether analysts are engineers?"
5. "A feature that predicts brilliantly offline and fails in production — whose failure is it: the model's, the feature's, or the process that let it through?"
6. "If your EDA can only be trusted because *you* did it, what have you actually built?"

## Wrap-up (final day, last 15 minutes)

- Map each capstone requirement to the module that taught it (one slide: SQL → M1/M2, scorecard → M3, master table → M4, features → M5, findings & report → M6).
- Forward pointers: SDA-FND-105 completes the Foundations Certificate; the Data Scientist track (SDA-DSC-111/112) assumes this module's EDA and wrangling discipline as its floor; the AI Engineer track (SDA-AIE-111) consumes the leakage and train/serve-consistency lessons directly; SDA-DSC-214 industrialises the pipeline thinking into Lakehouse-scale data engineering.
- Collect: repository links, `REPORT.pdf`, `DECISIONS.md`; issue badge recommendations within 5 working days.
- Close on the golden thread: the same 487,000 rows were, across five days, a database, a mess, a table, a feature source, and finally a brief on a decision-maker's desk — the journey *is* the job.

---

*End of instructor package. All code samples target Python 3.12, pandas ≥ 2.2, PostgreSQL 16, SQLAlchemy ≥ 2.0, Matplotlib ≥ 3.8, Seaborn ≥ 0.13. Verify pinned versions in the course lock file before each delivery.*
