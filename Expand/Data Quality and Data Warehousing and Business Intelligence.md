# Data Quality and Data Warehousing & Business Intelligence
## جودة البيانات ومستودعات البيانات وذكاء الاعمال

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Data Quality and Data Warehousing & Business Intelligence |
| **Arabic Title** | جودة البيانات ومستودعات البيانات وذكاء الاعمال |
| **Code** | SDA-DSC-212 |
| **Track** | Data Architecture & Engineering — معمارية البيانات وهندستها |
| **Level** | Practitioner |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Data analysts and BI developers, database designers, data-warehouse and ETL engineers, data stewards and data-quality officers, reporting leads in government entities |
| **Prerequisites** | None mandatory. SDA-FND-110 (Prompt Engineering and Responsible AI Use) recommended for the governance and documentation vocabulary; working SQL literacy (SELECT, JOIN, GROUP BY) assumed |
| **Assessment** | Eight graded labs; two practical assessments; the "Baseerah" warehouse + BI capstone |
| **Stackability** | Data-warehousing and BI badge; anchors the Data Architecture & Engineering specialisation. Derived from the SDAIA Data Warehousing & Business Intelligence programme and prepares for its certification exam. Next: SDA-DSC-214 (Modern Data Engineering for AI Systems) |
| **Tools & Platforms** | PostgreSQL · dbt · Apache Airflow · Power BI (or Metabase) · Great Expectations · dbdiagram/ERD tooling |

## Course Description

A practitioner course on turning messy operational data into a governed, trusted analytical asset. Participants learn metadata management, the three levels of data modelling (conceptual, logical, physical), normalisation through BCNF and the deliberate denormalisation trade-off, physical database design in PostgreSQL, data-quality engineering across the six quality dimensions, dimensional modelling with facts, dimensions and slowly-changing dimensions, ELT into a warehouse with dbt and Airflow, and the delivery of business-intelligence dashboards whose numbers survive executive scrutiny. The course maps directly onto the Data Warehousing and Business Intelligence certification syllabus and consolidates its eleven curriculum modules into eight teaching modules plus an applied capstone.

The course is built around a single evolving artefact: **"Baseerah" (بصيرة)**, the enterprise data warehouse and executive BI platform of a Saudi national water and utilities authority. Four source systems feed it — a **billing/CRM** system (customer accounts, meters, tariffs), a **SCADA/telemetry** feed (consumption readings and network pressure), a **work-order/maintenance** system (field jobs, technicians, assets), and a **finance ledger**. Three consumers depend on it: a regulator-facing **non-revenue-water (NRW) report**, an **executive KPI dashboard** reviewed by leadership every Sunday morning, and a **field-operations analytics** layer used by district supervisors. Across the five days participants profile and remediate Baseerah's data quality, capture business requirements and rules, model them conceptually → logically → physically, normalise then dimensionalise into a star schema, build ELT into the warehouse, add a semantic layer and dashboards, and govern every definition in a data dictionary and business glossary. Every lab produces a component of the capstone, so Day 5 is an integration exercise, not a from-scratch build — and the platform each participant owns is the same shape they will industrialise in SDA-DSC-214 (Modern Data Engineering for AI Systems).

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Explain the role of data modelling and metadata, and distinguish conceptual, logical, and physical models with the correct artefact at each stage
2. **LO2** — Elicit business requirements from stakeholders and document business rules as model-ready entities, attributes, and relationships
3. **LO3** — Design entity–relationship models with correct keys, cardinality, optionality, and referential integrity
4. **LO4** — Normalise a relational design through BCNF and justify deliberate denormalisation against reporting and performance needs
5. **LO5** — Implement a physical model in PostgreSQL with appropriate data types, constraints, indexes, and partitioning
6. **LO6** — Engineer data quality: profile sources, measure the six quality dimensions, remediate, match/merge duplicates, and operate stewardship
7. **LO7** — Design and build a dimensional data warehouse with declared fact grain, conformed dimensions, and slowly-changing dimension logic
8. **LO8** — Deliver ELT pipelines, BI dashboards, and governed KPI and data-dictionary definitions that make one number mean one thing

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | From business to model | M1: Data Modelling Fundamentals · M2: Business Requirements and Business Rules | 55% | 45% | Baseerah conceptual model (14 entities) + a signed-off business-rule register with 20 rules and their model implications |
| **Day 2** | Relational design done right | M3: Entity–Relationship Design, Keys, Cardinality · M4: Normalisation, Design Quality, Denormalisation | 40% | 60% | Logical ERD in 3NF/BCNF with keys and cardinality, plus a written denormalisation decision record |
| **Day 3** | Physical reality and data quality | M5: Physical Modelling, Types, Indexing, Constraints · M6: Data Quality Engineering | 35% | 65% | Deployed `core` schema in PostgreSQL (partitioned, indexed) + a Great Expectations suite lifting the composite DQ score from 72.4% to 94.8% |
| **Day 4** | The warehouse | M7: Data Warehouse and Dimensional Modelling | 35% | 65% | `mart` star schema: 5 fact tables, 9 dimensions, SCD2 on customer and meter, bridge + junk + degenerate dimensions in place |
| **Day 5** | Load, show, govern | M8: ELT, Business Intelligence, Dashboards, Definition Governance · Capstone | 25% | 75% | dbt+Airflow ELT run, executive KPI dashboard, NRW regulator report, data dictionary and glossary — plus the capstone demo |

## Hour-by-Hour Breakdown

### Day 1 — From Business to Model

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why warehouses fail** + course kickoff | See how undocumented definitions and unmodelled data destroy trust; meet the Baseerah golden thread and its four sources; PDPL framing for meter-level consumption | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Data modelling fundamentals** (M1) | Conceptual vs logical vs physical; metadata types; how modelling drives quality, integration, reporting and analytics | Lecture + model-walkthrough | 75/25 |
| 3 | **Lab 1 — Baseerah conceptual model** | Read four source-system briefs; produce a 14-entity conceptual model with definitions; classify each attribute for PDPL | Guided lab (pairs) | 20/80 |
| 4 | **Business requirements analysis** (M2) | Stakeholder elicitation; turning process narrative into entities/attributes/relationships; writing testable business rules | Lecture + live elicitation role-play | 60/40 |
| 5 | **Lab 2 — Business-rule register** | Interview the "NRW analyst" and "billing supervisor" personas; write 20 rules; map each to a model or a constraint | Guided lab (pairs) | 15/85 |

### Day 2 — Relational Design Done Right

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Entity–relationship design** (M3) | Strong/weak entities, attributes, identifying vs non-identifying relationships, cardinality and optionality, crow's-foot notation | Lecture + ERD dissection | 70/30 |
| 2 | **Keys: natural, surrogate, composite** | Primary/foreign/alternate keys; surrogate vs natural key trade-off; resolving many-to-many with associative entities | Lecture + demo | 60/40 |
| 3 | **Lab 3 — Logical ERD for Baseerah** | Build the full logical ERD in dbdiagram; resolve two many-to-many relationships; declare every key and cardinality | Guided lab | 15/85 |
| 4 | **Normalisation to BCNF** (M4) | Functional dependencies; 1NF → 2NF → 3NF → BCNF with a worked Baseerah example; update/insert/delete anomalies | Lecture + worked decomposition | 65/35 |
| 5 | **Lab 4 — Normalise then decide** | Decompose the denormalised `raw.billing_extract` to BCNF; then write the denormalisation decision record for the reporting layer | Guided lab | 15/85 |

### Day 3 — Physical Reality and Data Quality

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Physical modelling in PostgreSQL** (M5) | Logical → physical translation; data types and their cost; constraints as executable business rules; DDL conventions | Lecture + DDL demo | 65/35 |
| 2 | **Lab 5 — Deploy the `core` schema** | Generate DDL, add CHECK/FK/UNIQUE constraints, build B-tree vs BRIN indexes on 13.0M meter reads, partition by month | Guided lab | 10/90 |
| 3 | **Data quality engineering** (M6) | The six dimensions; profiling; rule authoring; remediation ladder; stewardship operating model | Lecture + profiling demo | 60/40 |
| 4 | **Lab 6a — Profile and score** | Profile all four sources; compute the composite DQ score (baseline 72.4%); write a Great Expectations suite | Guided lab | 10/90 |
| 5 | **Lab 6b — Match/merge and stewardship** | Deduplicate 3,320 duplicate customer records with deterministic + fuzzy matching and survivorship rules; raise steward tasks | Guided lab | 10/90 |

### Day 4 — The Warehouse

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Warehouse vs operational database** (M7) | OLTP vs OLAP; Inmon vs Kimball; warehouse components; the `raw → stg → core → mart` layering used all course | Lecture + architecture walkthrough | 70/30 |
| 2 | **Dimensional modelling: grain, facts, dimensions** | The four-step design process; declaring grain; additive / semi-additive / non-additive measures; star vs snowflake | Lecture + design clinic | 60/40 |
| 3 | **Lab 7a — Design and build the star** | Declare grain for five facts; build `dim_date`, `dim_customer`, `dim_meter`, `dim_district`; load `fct_meter_read_hourly` | Guided lab | 10/90 |
| 4 | **SCDs and the awkward dimensions** | SCD types 1/2/3 with SQL; conformed dimensions; degenerate, junk, and role-playing dimensions; bridges; late-arriving dimensions | Lecture + SQL demo | 55/45 |
| 5 | **Lab 7b — SCD2, bridge, junk, factless** | Implement SCD2 on `dim_customer` via a dbt snapshot; add `bridge_account_customer`, `dim_read_flag`, `fct_meter_inspection` | Guided lab | 10/90 |

### Day 5 — Load, Show, Govern

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **ELT into the warehouse** (M8) | ETL vs ELT; extraction patterns and CDC; dbt incremental models; orchestration and idempotency in Airflow | Lecture + pipeline demo | 55/45 |
| 2 | **BI, semantic layers and KPI governance** | KPI definition discipline; semantic layer; dashboard design for clarity; the NRW regulator report; data dictionary and glossary | Lecture + dashboard critique | 50/50 |
| 3 | **Lab 8 — ELT, dashboard, dictionary** | Run the Airflow DAG end-to-end; build the executive KPI dashboard and NRW report; publish the data dictionary from `meta` | Guided lab | 10/90 |
| 4 | **Capstone assembly** | Integrate Labs 1–8 into the Baseerah deliverable; complete the submission checklist; peer review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos; rubric-based peer + instructor scoring; path to SDA-DSC-214 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module works on the same Baseerah warehouse. Never introduce a throwaway example schema — always evolve Baseerah. Lab 1's conceptual model becomes Lab 3's ERD, becomes Lab 5's DDL, becomes Lab 7's star schema, becomes Lab 8's dashboard. That chain is exactly why the capstone is achievable in Day 5 Hour 4 as an integration.
- **Pace control:** Labs 5 (partitioning + index benchmarking) and 7b (SCD2 snapshots) are the most overrun-prone. Publish checkpoint tags (`lab1-start`, `lab1-solution`, `lab5-start`, `lab7b-start`, …) in the course repository so stragglers can fast-forward: `git checkout lab7b-start`. Every lab also ships a `--seed` restore script that rebuilds the expected end-state of the previous lab in under 90 seconds.
- **Pairing:** rotate pairs each day. Pair a strong-SQL participant with a strong-business-analysis participant. Days 1–2 reward the analyst; Days 3–5 reward the engineer; the deliberate discomfort in both directions is the point, because a warehouse fails at the seam between those two skills.
- **Environment strategy:** primary = local PostgreSQL 16 in Docker + Python 3.11 + `dbt-postgres` 1.7 + `great-expectations` 0.18 + Airflow 2.9 in the provided `docker compose` stack; BI = Power BI Desktop on Windows or **Metabase** in the same compose file for macOS/Linux participants. Fallback = a shared classroom PostgreSQL instance with one schema per participant (`baseerah_<initials>`). Verify both the week before delivery, and pre-pull the images: the Airflow image is the slowest download in the stack.
- **Data volume discipline:** the shipped Baseerah sample is the Riyadh North operating district — 61,420 raw customer-account rows, 64,800 meters, and **13,018,800** meter reads over 90 days. That is enough for BRIN vs B-tree and partition pruning to show real differences on a laptop, while the *national* figures (1,240,000 accounts, 1,318,500 meters) are used when teaching scale. Keep the two clearly separated on slides; participants conflate them otherwise.
- **Language:** deliver in English or Arabic; keep all code, schema names, table names, column names, dbt model names, and commit messages in English. This is production convention in Saudi enterprise environments — mixed-language identifiers break SQL tooling, `grep`-based operations, and every BI connector in the stack. The *business glossary* is deliberately the exception: every term carries an Arabic definition alongside the English one, because the glossary is read by business stakeholders, and Module 8 demonstrates the bilingual NRW report.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 4 is the heaviest cognitive day (dimensional modelling plus SCDs) — put the break between Hours 3 and 4, not later.
- **Assessment logistics:** rubric scoring happens live during Day 5 Hour 5 demos; collect repository URLs, the `baseerah/` project folder, and the exported data dictionary at the end of Hour 4 so table counts, dbt test results, and DQ scores can be verified before demos begin.
- **Governance framing:** treat Saudi PDPL (Personal Data Protection Law) as a first-class constraint from Day 1 Hour 1, not a Day-5 afterthought. Meter-level consumption is personal data: an hourly consumption curve reveals occupancy, household size, travel absence, and religious-practice patterns. Every model participants draw must classify each attribute, every lab must respect the classification, and the dashboards must aggregate before they expose. Say this in the first fifteen minutes.

---

# Module 1 — Data Modelling Fundamentals and the Conceptual → Logical → Physical Progression
## أساسيات نمذجة البيانات

## Module Overview

**Purpose.** Every failed warehouse this course examines failed the same way: somebody wrote SQL before anybody wrote a definition. This module gives participants the discipline that prevents that — the three-level modelling progression (conceptual → logical → physical), the metadata that makes each level durable, and the vocabulary to say precisely what a "customer", a "meter", and a "reading" *are* before a single `CREATE TABLE` is typed. It consolidates catalogue Module 1 (Data Modelling Fundamentals) and supplies the metadata-management framing that the course description leads with.

**Business relevance.** Saudi government entities modernising under Vision 2030 are consolidating decades of departmental systems into shared national data assets. The binding constraint is almost never the technology; it is that the billing department's "active customer" and the operations department's "active customer" have quietly meant different things for eleven years. A three-level model makes that disagreement visible on Day 1 of a programme instead of Month 9, and gives the entity's data-governance office an artefact it can approve, version, and audit against the National Data Management Office (NDMO) standards.

**Industry use cases.**
- A national utility merging four regional billing systems must agree one conceptual model of "customer account" before any migration script is written, or it will merge duplicates into a single mess at scale.
- A health insurer must show a regulator the logical model behind a submitted claims statistic, including which attributes are personal data under PDPL and where they are masked.
- A ministry publishing an open-data product needs a physical model whose column names, types, and units are documented well enough that external consumers do not misread cubic metres as litres.

**Expected competencies.** After this module a participant can distinguish conceptual, logical, and physical models and name the correct artefact and audience for each; explain how metadata (business, technical, operational) binds the three together; articulate how modelling decisions propagate into data quality, system integration, reporting, and analytics; and produce a defensible conceptual model with entity definitions and a PDPL classification for a real multi-source environment.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Define data modelling and state its role in translating business requirements into structured designs | LO1 |
| 1.2 | Distinguish conceptual, logical, and physical models by audience, content, and artefact | LO1 |
| 1.3 | Classify and use business, technical, and operational metadata | LO1, LO8 |
| 1.4 | Explain how modelling decisions propagate into data quality, integration, reporting, and analytics | LO1, LO6 |
| 1.5 | Produce a conceptual model with entity definitions and a PDPL attribute classification for four source systems | LO1, LO2 |

## Technical Content

### 1. What a data model actually is

A data model is a **specification of meaning that a machine can enforce**. It answers three questions in order: *what things exist* (entities), *what we know about each thing* (attributes), and *how the things relate* (relationships). Everything else — SQL dialects, index types, star schemas — is downstream implementation of those three answers.

The reason modelling is treated as a separate discipline, rather than as "the bit before you write DDL", is that the three answers are **business facts, not technical ones**. Whether a water meter can serve two customer accounts simultaneously is not a database question; it is a question about how the utility sells water. If a modeller guesses, the guess becomes a foreign key, the foreign key becomes a migration, and the migration becomes ten years of reconciliation meetings.

For Baseerah the stakes are concrete. The billing system knows a *customer account*. The SCADA feed knows a *meter*. The work-order system knows a *service point*. The finance ledger knows a *revenue contract*. Four systems, four identifiers, and — the participants will discover in Lab 1 — no agreement about whether these are four views of one thing or four genuinely different things. Answering that is the conceptual model.

### 2. The three levels

| Aspect | Conceptual model | Logical model | Physical model |
|---|---|---|---|
| Primary question | What does the business care about? | How is it structured, precisely? | How does it run in *this* engine? |
| Audience | Executives, domain experts, stewards | Data architects, analysts, developers | DBAs, engineers, performance owners |
| Contains | Entities, definitions, high-level relationships | All attributes, keys, cardinality, optionality, normalisation, domains | Tables, columns, data types, indexes, partitions, constraints, tablespaces |
| Excludes | Attributes, keys, technology | Indexes, storage, engine specifics | Nothing — it is the implementation |
| Typical artefact | One-page entity diagram + a definitions register | Crow's-foot ERD in 3NF/BCNF | `CREATE TABLE` DDL + index/partition scripts |
| Changes when | The business changes | The rules or structure change | The workload or the engine changes |
| Baseerah example | "A Customer Account is billed for water delivered through one or more Meters" | `customer_account(account_id PK, …)`, `meter(meter_id PK, account_id FK NOT NULL)` | `core.meter` with `meter_id BIGINT GENERATED ALWAYS AS IDENTITY`, BRIN on `installed_on` |

Three rules make the progression work:

1. **Each level is derivable from the one above it.** If your physical model contains a table that no logical entity explains, you have either an undocumented requirement or an accident. Both are defects.
2. **Each level is independently reviewable by a different audience.** The conceptual model is signed by the business; the logical model is reviewed by architecture; the physical model is reviewed by the DBA. Collapsing the levels means one review by one person who cannot possibly hold all three concerns.
3. **Levels are versioned separately but linked.** A physical change to add a partition does not require the business to re-approve the conceptual model. A conceptual change — "a meter may now be shared by two accounts" — must ripple through all three deliberately.

The commonest professional failure is jumping from a conversation straight to physical tables. It feels fast. It costs the project the conceptual model's clarity and the logical model's normalisation, and both losses surface later as data-quality defects that this course's Module 6 will spend a whole day repairing.

### 3. Metadata: the layer that keeps a model alive

A model that nobody can read six months later is a drawing, not a model. **Metadata** is what keeps it readable, and it comes in three kinds:

- **Business metadata** — what a thing means to a human. Definitions ("Non-Revenue Water is the difference between the volume of water put into the distribution network and the volume billed to customers, expressed as a percentage of input volume"), ownership, sensitivity classification, allowed values, and the Arabic term used with stakeholders. This lives in the **business glossary**.
- **Technical metadata** — what a thing is to a machine. Schema, column, data type, nullability, key structure, source system, transformation lineage. This lives in the **data dictionary** and is largely machine-generated.
- **Operational metadata** — what happened to the data. Load timestamps, row counts, run durations, test results, freshness, failure counts. This lives in your orchestration and quality tooling.

Module 8 builds all three for Baseerah in the `meta` schema. The reason they are introduced here, on Day 1, is that metadata is *cheap to capture while modelling and expensive to reconstruct afterwards*. Ask participants to write the one-sentence definition of every entity at the moment they draw it. This single habit is the highest-leverage thing in the module.

### 4. How modelling decisions propagate

Catalogue Module 1 asks participants to "explain the relationship between data modelling, data quality, system integration, reporting, and analytics". That relationship is causal and worth teaching explicitly with Baseerah examples:

| Modelling decision | Effect on data quality | Effect on integration | Effect on reporting/analytics |
|---|---|---|---|
| No unique constraint on `meter_serial` | Duplicate meters accumulate silently (uniqueness defect) | Two systems disagree on meter count | Meter-count KPI drifts upward with no physical cause |
| `consumption_m3` typed as `TEXT` | Invalid values ("N/A", "-") enter undetected (validity defect) | Every consumer must re-parse | Aggregations silently drop rows; NRW understated |
| No `valid_from`/`valid_to` on tariff | Historic invoices cannot be reproduced (accuracy defect) | Finance and billing diverge | Revenue restatement is impossible to explain |
| Address stored as one free-text field | No completeness measure possible per component | National Address service cannot be matched | District-level analysis needs manual cleansing |
| Meter reading grain undeclared | "Reading" sometimes hourly, sometimes cumulative index | SCADA and billing double-count | Consumption sums are wrong by a factor no one can find |

Walk the last row slowly. A cumulative meter *index* (odometer-style, always increasing) and a *delta* consumption value look identical in a `NUMERIC` column. Summing indexes produces a meaningless enormous number that looks plausible on a chart. Baseerah's regulator report was wrong for two quarters for exactly this reason, and no dashboard would ever have caught it. Only a declared grain and a modelled distinction would.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Definition before structure:* if you cannot write one unambiguous sentence defining an entity, you are not ready to draw it. Ambiguity you skip here becomes a JOIN condition nobody can justify later.
- *Model the business, not the screen:* source-system tables reflect a vendor's UI decisions from 2011. Model what the utility actually does.
- *One fact in one place (at the logical level):* this is the seed of normalisation, and it starts as a modelling instinct long before Module 4 formalises it.
- *Classify sensitivity at the moment of modelling:* PDPL classification is an attribute property, like data type. Adding it later means auditing thousands of columns.
- *The model is a contract, and contracts are versioned:* every change gets a version, a date, an author, and a reason.

**Common mistakes (each appears in the Lab 1 starter deliberately)**
1. Drawing the four source systems' tables and calling it a conceptual model — it is a *source inventory*, and it hides the fact that `billing.CUST_MST`, `wo.SERVICE_POINT`, and `fin.CONTRACT` may be the same entity.
2. Putting attributes on a conceptual model, which turns a one-page executive artefact into an unreadable wall and stalls sign-off.
3. Naming entities after systems (`SCADA_READING`) rather than after business concepts (`Meter Reading`), permanently coupling the model to a vendor.
4. Leaving "Customer" undefined so that it silently means *account holder* in billing and *occupant* in operations — the seed of the duplicate-customer problem Module 6 must solve.
5. Ignoring the difference between a *meter*, a *service point*, and a *connection*, so that meter replacement history is unrepresentable.
6. Recording no sensitivity classification, which makes the Day-5 dashboard a PDPL incident rather than a deliverable.

**Production considerations**
- Store models as text where possible (dbdiagram DBML, or dbt YAML) so they diff in Git. A model in a binary diagramming tool cannot be code-reviewed, and a model that cannot be code-reviewed rots.
- Maintain a **model-to-source mapping** from Day 1: every conceptual entity lists which source system(s) supply it. This becomes the extraction plan in Module 8 and prevents the classic "we modelled an entity no system actually produces" surprise.
- Agree the **naming standard** before the first entity: singular nouns for entities, `snake_case` for physical objects, no abbreviations except a published list, and English identifiers throughout (see the delivery-plan language note).

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides). A regional utility ran a two-year warehouse programme and delivered on time. Six weeks after go-live the executive dashboard reported 1,062,000 active customers; the billing system reported 1,240,000. The gap — 178,000 customers, about 14% — froze a SAR 220 million network-investment decision because nobody could say which number was the denominator for "coverage".

The investigation found no bug. The warehouse team had implemented "active = has a billed invoice in the last 90 days", which was a reasonable reading of a requirement written as "active customers". Billing meant "account status = ACTIVE", which includes seasonal properties, government facilities billed annually, and accounts under dispute. Both numbers were correct; the *definition* had never been modelled, so no code was wrong and no test could fail.

The fix took three days and no code: define both concepts as distinct entities in the conceptual model — `Customer Account` with a status, and a derived measure `Billing-Active Customer` with an explicit 90-day window — publish both in the glossary with Arabic terms, and label the dashboard tile with the definition it uses. The lesson participants must carry to Module 8: a KPI without exactly one governed definition is not a KPI, it is an opinion with a number attached.

## Code Examples

### The conceptual model as versionable text (DBML)

```
// models/conceptual/baseerah_conceptual.dbml
//
// WHY: a conceptual model must be reviewable by non-technical stewards AND
// diffable in Git. DBML gives us both: it renders to a diagram at dbdiagram.io
// and it code-reviews as text. No attributes here beyond identity — attributes
// belong to the logical model (Module 3). Every entity carries a one-sentence
// definition and a PDPL classification, captured at the moment of modelling.

Project baseerah {
  database_type: 'PostgreSQL'
  Note: 'Baseerah — national water & utilities authority warehouse. Conceptual model v1.0'
}

Table customer_account {
  account_id integer [pk]
  Note: '''
  A commercial agreement under which the authority bills a party for water
  delivered to one or more service points. Owned by: Billing Directorate.
  PDPL: contains personal data (holder name, national ID, contact).
  Source: billing/CRM (BILL.CUST_MST).
  '''
}

Table service_point {
  service_point_id integer [pk]
  Note: '''
  A physical location where water is delivered, identified by a National
  Address short code. Persists across meter replacements and account changes.
  PDPL: quasi-identifier (a precise address identifies a household).
  Source: billing/CRM + work-order system (both hold a partial view).
  '''
}

Table meter {
  meter_id integer [pk]
  Note: '''
  A physical measuring device installed at a service point for a period of
  time. A service point may have several meters over its life; only one is
  active at any instant. PDPL: non-personal alone, personal in combination.
  Source: billing/CRM (asset register) + SCADA (telemetry identity).
  '''
}

Table meter_reading {
  reading_id integer [pk]
  Note: '''
  A measurement taken from a meter at a point in time. GRAIN IS DECLARED HERE:
  one row = one meter, one timestamp, one read channel. Stores the cumulative
  index AND the derived delta volume as separate attributes -- conflating them
  is the defect described in Technical Content section 4.
  PDPL: PERSONAL DATA. Hourly consumption reveals occupancy and absence.
  Source: SCADA/telemetry (AMI meters) + billing (manual reads).
  '''
}

Table tariff {
  tariff_id integer [pk]
  Note: '''
  A time-bounded price schedule (block-rate) applied to consumption for a
  customer category. Historic tariffs MUST be retained to reproduce invoices.
  PDPL: non-personal. Source: billing/CRM (rate tables) + finance ledger.
  '''
}

Table work_order {
  work_order_id integer [pk]
  Note: '''
  A unit of field work raised against an asset or a service point, assigned to
  a technician, with a lifecycle from raised to closed. PDPL: contains
  technician identity (employee personal data) and the customer address.
  Source: work-order/maintenance system.
  '''
}

Table network_asset {
  asset_id integer [pk]
  Note: '''
  A maintained component of the distribution network (pump, valve, pressure-
  reducing valve, reservoir, main segment) belonging to a District Metered
  Area. PDPL: non-personal. Source: work-order/maintenance system + SCADA.
  '''
}

Table district_metered_area {
  dma_id integer [pk]
  Note: '''
  A hydraulically discrete zone of the network whose inflow is measured, so
  that input volume can be compared with billed volume. THE unit of
  non-revenue-water reporting. PDPL: non-personal. Source: SCADA.
  '''
}

Table ledger_entry {
  ledger_entry_id integer [pk]
  Note: '''
  A posted double-entry accounting line recognising billed revenue, collection,
  or write-off. The finance system, not billing, is the source of truth for
  recognised revenue. PDPL: non-personal at line level.
  Source: finance ledger.
  '''
}

Ref: customer_account.account_id < service_point.service_point_id      // one account, many service points
Ref: service_point.service_point_id < meter.meter_id                   // one point, many meters over time
Ref: meter.meter_id < meter_reading.reading_id                         // one meter, many readings
Ref: district_metered_area.dma_id < service_point.service_point_id     // a point sits in exactly one DMA
Ref: district_metered_area.dma_id < network_asset.asset_id             // an asset belongs to one DMA
Ref: network_asset.asset_id < work_order.work_order_id                 // a work order targets one asset
Ref: customer_account.account_id < ledger_entry.ledger_entry_id        // ledger lines reference an account
Ref: tariff.tariff_id < customer_account.account_id                    // an account is on one tariff at a time
```

### Capturing entity definitions and PDPL classification as data, not prose

```sql
-- sql/ddl/010_meta_model_registry.sql
--
-- WHY: definitions written in a document are read once and rot. Definitions
-- written into a table are queryable, joinable to the physical catalogue in
-- Module 8, and testable -- we can literally fail the build when a shipped
-- table has no definition. This registry is created on Day 1 and populated
-- from Lab 1 onward; Module 8 joins it to information_schema to publish the
-- data dictionary.

CREATE SCHEMA IF NOT EXISTS meta;

CREATE TABLE meta.entity_definition (
    entity_name        text PRIMARY KEY,
    entity_name_ar     text        NOT NULL,          -- glossary is bilingual by design
    definition_en      text        NOT NULL,
    definition_ar      text        NOT NULL,
    owning_directorate text        NOT NULL,
    steward_email      text        NOT NULL,
    -- PDPL classification drives masking, retention and dashboard aggregation.
    -- 'personal' = directly identifies; 'quasi' = identifies in combination;
    -- 'sensitive' = special category; 'none' = no personal data.
    pdpl_class         text        NOT NULL
        CHECK (pdpl_class IN ('personal', 'quasi', 'sensitive', 'none')),
    source_systems     text[]      NOT NULL,          -- model-to-source mapping
    model_version      text        NOT NULL DEFAULT 'v1.0',
    approved_on        date,
    CONSTRAINT definition_is_a_sentence
        CHECK (length(definition_en) >= 40)           -- blocks "the customer table"
);

COMMENT ON TABLE meta.entity_definition IS
  'Business metadata: one row per conceptual entity. Populated in Lab 1, '
  'published as the business glossary in Lab 8.';

INSERT INTO meta.entity_definition
    (entity_name, entity_name_ar, definition_en, definition_ar,
     owning_directorate, steward_email, pdpl_class, source_systems)
VALUES
    ('meter_reading', 'قراءة العداد',
     'A measurement taken from a meter at a point in time; one row is one '
     'meter, one timestamp, one read channel, carrying both the cumulative '
     'index and the derived delta volume.',
     'قياس مأخوذ من عداد في لحظة زمنية محددة؛ يمثل السجل الواحد عدادًا واحدًا '
     'وطابعًا زمنيًا واحدًا وقناة قراءة واحدة.',
     'Operations', 'steward.ops@baseerah.gov.sa', 'personal',
     ARRAY['scada_telemetry', 'billing_crm']),
    ('district_metered_area', 'منطقة القياس المحصورة',
     'A hydraulically discrete zone of the distribution network whose inflow '
     'is measured so that input volume can be compared with billed volume; '
     'the reporting unit for non-revenue water.',
     'منطقة منفصلة هيدروليكيًا من شبكة التوزيع يُقاس تدفقها الداخل لمقارنة '
     'الحجم المُدخل بالحجم المفوتر؛ وهي وحدة تقارير الفاقد المائي.',
     'Network Operations', 'steward.network@baseerah.gov.sa', 'none',
     ARRAY['scada_telemetry']);
```

### A build-time test that a model has definitions before it has tables

```python
# src/baseerah/model/check_definitions.py
"""Fail the build when a physical table ships without a business definition.

WHY: "we'll document it later" is how a data dictionary dies. Making the
absence of a definition a *build failure* moves documentation from goodwill to
gate. This script runs in CI from Day 1 and is reused unchanged in Module 8,
where it also checks the KPI register.

Exit code 0 = every non-exempt table in the target schemas has a definition
row in meta.entity_definition. Exit code 1 = list of offenders printed.
"""
from __future__ import annotations

import sys

import psycopg

# Schemas that hold modelled business objects. `raw` is exempt: it is a
# byte-faithful landing copy of source systems and is documented by the
# source-system contract, not by our own glossary.
GOVERNED_SCHEMAS = ("core", "mart")
EXEMPT_TABLES = {"core.schema_migration", "mart.dbt_audit_log"}

FIND_UNDOCUMENTED = """
SELECT t.table_schema || '.' || t.table_name AS qualified_name
FROM   information_schema.tables      AS t
LEFT   JOIN meta.entity_definition    AS d
       ON  d.entity_name = t.table_name
WHERE  t.table_schema = ANY(%(schemas)s)
  AND  t.table_type   = 'BASE TABLE'
  AND  d.entity_name IS NULL
ORDER  BY 1;
"""


def main(dsn: str) -> int:
    with psycopg.connect(dsn) as conn, conn.cursor() as cur:
        cur.execute(FIND_UNDOCUMENTED, {"schemas": list(GOVERNED_SCHEMAS)})
        offenders = [row[0] for row in cur.fetchall() if row[0] not in EXEMPT_TABLES]

    if not offenders:
        print(f"OK: every table in {GOVERNED_SCHEMAS} has a business definition.")
        return 0

    print(f"FAIL: {len(offenders)} table(s) shipped without a definition:")
    for name in offenders:
        print(f"  - {name}")
    print("\nAdd a row to meta.entity_definition before merging.")
    return 1


if __name__ == "__main__":
    # DSN comes from the environment so credentials never enter the repository.
    import os

    sys.exit(main(os.environ["BASEERAH_DSN"]))
```

## Hands-on Lab 1 — Build the Baseerah Conceptual Model

| | |
|---|---|
| **Objective** | Read the four source-system briefs, resolve the "is this the same thing?" questions, and produce a 14-entity conceptual model in DBML with a one-sentence definition and a PDPL classification for every entity |
| **Duration** | 50 minutes |
| **Setup** | PostgreSQL 16 (Docker), Python 3.11, `pip install psycopg[binary]==3.1.*`, a dbdiagram.io account (or the offline `dbml-renderer` in the repo), course repo cloned, `git checkout lab1-start` |

**Instructions & tasks**

1. *(8 min)* Read `docs/sources/*.md` — the four source-system briefs (billing/CRM, SCADA/telemetry, work-order, finance). Highlight every noun that could be an entity. Expect roughly 40 candidate nouns; you will keep about 14.
2. *(10 min)* Resolve the three identity questions the briefs deliberately leave open: (a) are `BILL.CUST_MST`, `WO.SERVICE_POINT`, and `FIN.CONTRACT` one entity or three? (b) is a *meter* the same as a *service point*? (c) does a *reading* mean an index or a volume? Write your answer and the evidence in `LAB1_DECISIONS.md`.
3. *(12 min)* Complete `models/conceptual/baseerah_conceptual.dbml` to 14 entities. Entities only — no attributes beyond the identifier. Render it and check it fits legibly on one page; if it does not, you have modelled the source systems, not the business.
4. *(10 min)* Write the one-sentence definition and the PDPL class for each entity directly in the DBML `Note`. Apply the 40-character rule from the `definition_is_a_sentence` constraint — if it is shorter than that, it is a label, not a definition.
5. *(6 min)* Load your definitions into `meta.entity_definition` with `python -m baseerah.model.load_definitions`, then run `python -m baseerah.model.check_definitions` and confirm it exits 0.
6. *(4 min)* Commit: `feat(model): baseerah conceptual model v1.0 with definitions and PDPL classes`.

**Expected output**
```
$ python -m baseerah.model.load_definitions models/conceptual/baseerah_conceptual.dbml
Parsed 14 entities from baseerah_conceptual.dbml
Inserted 14 rows into meta.entity_definition (model_version=v1.0)
  personal: 3   quasi: 2   sensitive: 0   none: 9

$ python -m baseerah.model.check_definitions
OK: every table in ('core', 'mart') has a business definition.

$ dbml-renderer -i models/conceptual/baseerah_conceptual.dbml -o docs/conceptual.svg
Rendered 14 entities, 13 relationships -> docs/conceptual.svg (1 page)
```

**Acceptance criteria**
- Exactly 14 entities, no attributes beyond the identifier, renders legibly on one page.
- Every entity has a definition of ≥ 40 characters and a PDPL class; `meter_reading` is classified `personal` and the reason is stated.
- `LAB1_DECISIONS.md` answers all three identity questions with evidence from the briefs, not preference.
- `check_definitions.py` exits 0.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `definition_is_a_sentence` CHECK violation on insert | Definition is a label ("customer table") | Write a full sentence stating what the thing *is* and what distinguishes it |
| Diagram is unreadable / spans pages | Attributes added to a conceptual model | Strip everything except the identifier; attributes belong to Lab 3 |
| Duplicate key on `entity_definition` insert | Same entity modelled twice under two source names | This *is* the lesson — merge them and record the decision in `LAB1_DECISIONS.md` |
| `dbml-renderer: unresolved Ref` | Relationship references an entity you renamed | Rename consistently; DBML is case-sensitive |

**Instructor notes.** The three identity questions are the whole lab. Walk the room during task 2 and listen for pairs who answer question (a) with "three, because there are three tables" — that is modelling the source systems, mistake #1 from the content section, and it is worth interrupting the room to name it out loud when you hear it. The correct answer is that `CUST_MST` and `FIN.CONTRACT` are the same conceptual entity (customer account) seen by two systems, while `WO.SERVICE_POINT` is a *different* entity — a location, which survives when the account changes. Question (c) is the grain trap from Technical Content section 4. Fast finishers: add a `meta.attribute_definition` sibling table and classify the twelve attributes of `customer_account` — this is a direct head start on Lab 3.

## Mini Exercises

**Quiz (5 questions)**
1. Which model level contains indexes and partitions? → **physical**.
2. Who is the primary audience for a conceptual model? → business stakeholders / domain experts and stewards (it is the artefact they sign).
3. Name the three kinds of metadata. → business, technical, operational.
4. Why must a meter reading distinguish cumulative index from delta volume? → summing an odometer-style index produces a meaningless total that still renders as a plausible chart.
5. True/False: a conceptual model should list every attribute. → **False** — attributes appear at the logical level.

**Debugging exercise.** Check out `git checkout lab1-broken-model`. It contains a "conceptual model" of 27 entities named `BILL_CUST_MST`, `SCADA_TAG_HIST`, `WO_SP_XREF`, and so on. Symptom: the executive review meeting cannot proceed because nobody in the room recognises a single entity name. Ask participants to diagnose (it is a source inventory, not a conceptual model) and to reduce it to 14 business-named entities. The discussion this opens: what have we lost by discarding the source names, and where must that mapping be preserved instead? (Answer: in the model-to-source mapping, which becomes the extraction plan in Module 8.)

**Design exercise.** The authority announces that from next quarter a single meter may be shared by two customer accounts in mixed-use buildings, with consumption split by a fixed percentage. State which of the three model levels must change, what changes at each, and which existing entity is no longer sufficient. (Expected: conceptual gains an associative entity `account_meter_share`; logical gains keys, cardinality, and a `share_pct` attribute with a sum-to-100 rule; physical gains a table, a composite key, and a constraint. This is the bridge table of Module 7.)

**Discussion questions.**
- Your programme is under schedule pressure and the sponsor proposes skipping the conceptual model because "we already have the source schemas". What do you concede, what do you refuse, and what is the cheapest artefact that still protects the programme?
- Should the *definition* of an entity be owned by the business or by the data team? Argue both sides, then decide what happens when the two disagree and a regulator has asked for the number tomorrow.

## Case Study — The Undefined Denominator at "Mizan" (ميزان)

**Scenario.** "Mizan" (ميزان), a Saudi health-insurance claims administrator processing claims for 3.4 million members across 11 insurers, built a claims data warehouse in eighteen months. At go-live the executive dashboard reported an average claim-settlement time of 6.2 days; the regulator's own submission, computed by the operations team from the source system, reported 11.8 days. Both teams had used the same warehouse.

**Business context.** Settlement time is a regulated service-level metric. A misstated figure is a compliance exposure, and the gap suspended a SAR 30 million provider-network expansion pending clarification. The CEO's question — "which number do I put in the board pack?" — had no defensible answer for five weeks.

**Technical challenge.** The warehouse had no conceptual model. The dashboard's clock started at `claim_adjudicated_ts` (when the claim entered the adjudication queue) and stopped at `payment_instruction_ts`. Operations started at `claim_received_ts` (when the member's provider submitted it) and stopped at `payment_settled_ts`. Neither team was wrong; there was no entity called "Claim" with a defined lifecycle, so there was no agreed answer to "when does a claim start?".

**Constraints.** The regulator's definition is fixed and non-negotiable, and it is the *received-to-settled* one. The insurers each submit claims in a different format with different timestamp semantics. Historic dashboards have been distributed to the board for four quarters and cannot be quietly changed without an explanation. PDPL applies throughout: claim records contain health data, a special category requiring explicit safeguards, so the remediation cannot involve exporting extracts to spreadsheets.

**Solution approach (facilitate, don't lecture).** Steer the room towards: (1) model the `Claim` entity conceptually with an explicit lifecycle — received → adjudicated → instructed → settled — and name all four timestamps as distinct attributes; (2) define *two* measures, `regulatory_settlement_days` and `adjudication_cycle_days`, register both in the glossary with owners, and forbid the unqualified term "settlement time"; (3) label every dashboard tile with the measure name it renders; (4) restate the four historic quarters once, with a published note, rather than silently. Resist the room's instinct to "just pick one" — the operational metric is genuinely useful to operations and deleting it destroys real management information. The failure was never having two metrics; it was having two metrics with one name.

**Discussion questions.**
1. Why could no automated test have caught this defect? What kind of artefact is the only possible control?
2. The dashboard's number was *better* than the regulator's. What organisational incentive does that create, and how does a conceptual model with named owners counteract it?
3. Mizan's data team argues the fix belongs in the semantic layer, not the conceptual model. Where do you stand, and what does each choice cost when a twelfth insurer is onboarded?
4. How would you restate four quarters of board reporting in a way that increases trust rather than destroying it?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Conceptual entities modelled | Coverage | 14 entities, 13 relationships | DBML render + entity count |
| Definition completeness | Governance | 100% of entities have a ≥ 40-char definition | `check_definitions.py` exit code |
| PDPL classification coverage | Compliance | 100% of entities classified; `meter_reading` = personal | `meta.entity_definition` query |
| Source-mapping coverage | Traceability | Every entity maps to ≥ 1 of the 4 source systems | `source_systems` array non-empty |
| Identity decisions resolved | Analysis | 3/3 answered with evidence in `LAB1_DECISIONS.md` | instructor review |

**Example benchmark table (filled during lab):**

| Source system | Candidate nouns found | Entities retained | PDPL: personal/quasi | Notes |
|---|---|---|---|---|
| billing/CRM | 17 | 5 | 2 / 1 | `CUST_MST` and `FIN.CONTRACT` merged to one entity |
| SCADA/telemetry | 9 | 3 | 1 / 0 | `meter_reading` is personal — the key classification call |
| work-order/maintenance | 11 | 4 | 0 / 1 | technician identity is employee personal data |
| finance ledger | 6 | 2 | 0 / 0 | ledger lines non-personal at line grain |
| **Total** | **43** | **14** | **3 / 2** | 9 entities classified `none` |

## Required Visuals and Training Assets

### Diagrams
1. **The three-level pyramid for Baseerah** — *Purpose:* the anchor image for the whole course, reused in every module header slide. *Elements:* three stacked bands (conceptual / logical / physical) with the same entity, `meter_reading`, shown at each level: a named box, then a keyed attribute list, then a partitioned DDL fragment with a BRIN index. Audience icons on the right of each band. *Style:* flat vector, three-colour palette, English labels with Arabic subtitles. *Designer description:* "A pyramid narrowing upward in abstraction but widening downward in detail; the same object traced by a vertical thread through all three bands."
2. **Baseerah source-to-entity map** — *Purpose:* make the four-source integration problem visible before any modelling starts. *Elements:* four source-system boxes on the left (billing/CRM, SCADA, work-order, finance) with arrows converging on the 14 conceptual entities; the three contested entities highlighted in amber. *Style:* left-to-right convergence diagram; amber = "identity question unresolved". *Designer description:* "Four coloured pipes feeding a set of neutral-grey entity boxes; three boxes glow amber to show contested identity."
3. **Metadata triangle** — *Purpose:* fix the three metadata kinds in memory. *Elements:* business / technical / operational metadata as three corners, each with its home artefact (glossary / data dictionary / run log) and a Baseerah example. *Style:* triangle with example callouts.
4. **How a modelling decision propagates** — *Purpose:* render Technical Content section 4 visually. *Elements:* a single decision node ("`consumption_m3` typed as TEXT") with four downstream consequence lanes (quality, integration, reporting, analytics) each ending in a concrete Baseerah symptom. *Style:* fan-out causal diagram, red consequence chips.

### Images (screenshots)
1. **A rendered 14-entity conceptual model on one page** — *why:* participants need the visual target for "fits on a page"; *content:* the completed Lab 1 output at readable zoom.
2. **`meta.entity_definition` query result** — *why:* proves definitions are *data*, not documents; *content:* a `SELECT entity_name, pdpl_class, owning_directorate` result grid with the Arabic names rendering correctly.
3. **The failing `check_definitions.py` CI run** — *why:* documentation-as-a-gate must be seen to fail; *content:* a red pipeline step listing two undocumented tables.

### Simulations
1. **The undefined denominator** — *Setup:* branch `sim-active-customer` ships two SQL scripts computing "active customers" with different but defensible rules against the same Baseerah sample. *Expected behaviour:* one returns 58,100, the other 49,780 — a 14.3% gap, matching the utility story in section 6. *Learning objective:* a definition gap produces two correct answers and zero failing tests.
2. **Index versus volume** — *Setup:* branch `sim-index-vs-delta` provides 5,000 readings where 60% are cumulative index values and 40% are deltas, undistinguished. *Expected behaviour:* `SUM(reading_value)` returns 41.2 billion m³ for a district that consumes 2.1 million m³ — absurd, but the chart renders smoothly. *Learning objective:* grain and semantics must be modelled, not inferred.

### Interactive Activities
- **Entity or attribute? (12 min):** 24 cards (Meter, Meter Serial Number, District, Tariff Band, Technician, Pressure Reading, Invoice Line, National Address …) sorted into entity / attribute / neither, then defended. The arguable cases (Tariff Band, National Address) are the point.
- **Definition duel (10 min):** two teams independently write the one-sentence definition of "active customer" for Baseerah, then read them aloud simultaneously. Discuss which the dashboard should use and who has authority to decide.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `docs/sources/*.md` | Four synthetic source-system briefs written for this course (billing/CRM, SCADA, work-order, finance) | Markdown | 4 files, ~1,400 words | Requirement material for Labs 1 and 2 |
| `raw/customer_account_extract.csv` | Synthetic billing extract, Riyadh North district | CSV | 61,420 rows | Profiled in M1, deduplicated in M6 |
| `raw/meter_register.csv` | Synthetic meter/asset register | CSV | 64,800 rows | Meter dimension from M3 onward |
| `models/conceptual/baseerah_conceptual.dbml` | Lab 1 starter (7 entities pre-filled, 7 to add) | DBML | 14 entities at completion | The conceptual model artefact |

### Demo Requirements
- **Instructor demo (7 min):** run `sim-index-vs-delta` live. Show the 41.2 billion m³ total, then show the chart of it — smooth, professional, entirely wrong. Then add the modelled distinction between index and delta, re-run to 2.1 million m³, and close with: "no test failed, no error was raised, and the only control that would have caught this is a model." This lands the module's thesis harder than any slide.

---

# Module 2 — Business Requirements Analysis and Business-Rule Capture
## تحليل متطلبات الأعمال وقواعد الأعمال

## Module Overview

**Purpose.** A data model is only as good as the requirements it encodes, and requirements arrive as prose, arguments, spreadsheets, and the phrase "everyone knows that". This module teaches the elicitation and documentation discipline that converts stakeholder language into entities, attributes, relationships, and — most importantly — **testable business rules**. It covers catalogue Module 2 in full and supplies the rule register that Modules 3, 4, and 5 turn into keys, normal forms, and CHECK constraints.

**Business relevance.** In Saudi government entities the requirements for a shared data asset come from several directorates at once, each with statutory obligations and none with authority over the others. A billing directorate, a network-operations directorate, and a finance directorate will each describe "the same" process differently and all be correct within their own mandate. Without a rule register with named owners, the model quietly encodes whichever directorate spoke to the modeller last. With one, disagreement surfaces as a numbered, dated, owned decision — which is exactly the evidence an NDMO data-governance assessment asks for.

**Industry use cases.**
- A utility must decide whether a disconnected-for-non-payment account is still an "active customer" for coverage reporting; the answer changes a nationally published percentage.
- A procurement authority must encode a rule that a supplier cannot bid on a tender their affiliate is evaluating — a relationship constraint no source system enforces.
- A regulator requires that any submitted figure be reproducible from stated rules; "the analyst applied judgement" is a finding, not an explanation.

**Expected competencies.** After this module a participant can plan and run a requirements elicitation session; convert process narrative into a first-cut entity/attribute/relationship set; write business rules in a structured, testable form with type, owner, and enforcement point; distinguish rules that belong in the model from rules that belong in a constraint, a transformation, or a report; and maintain a rule register that survives contact with disagreement.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Plan and conduct requirements elicitation with data stakeholders | LO2 |
| 2.2 | Convert process narrative into candidate entities, attributes, and relationships | LO2, LO1 |
| 2.3 | Write business rules in a structured, testable form with owner and enforcement point | LO2, LO5 |
| 2.4 | Classify rules by type (structural, derivation, action-enabling, constraint) | LO2 |
| 2.5 | Maintain a rule register and trace each rule to a model element or a control | LO2, LO8 |

## Technical Content

### 1. Elicitation: getting requirements that are actually requirements

Stakeholders rarely state requirements. They state **solutions** ("we need a column for the old meter number"), **complaints** ("the report is always wrong on the 3rd"), and **habits** ("we've always excluded government accounts"). The analyst's job is to work backwards from each of these to the underlying fact about the business.

Four techniques carry most of the load:

- **Process walkthrough.** Ask the stakeholder to narrate one complete instance end to end — one customer, one meter, one billing cycle — using real values. Concrete instances expose exceptions that abstract descriptions hide. "Walk me through the last meter you replaced" produces more model than an hour of "how does meter replacement work?".
- **Artefact archaeology.** Ask for the actual outputs: the last regulator submission, the spreadsheet the supervisor maintains privately, the printed invoice. The private spreadsheet is the single richest source of unmodelled requirements in any organisation, because it is where people patch what the system cannot do.
- **Exception hunting.** For every rule stated, ask "when is that not true?" three times. The third answer is usually the real requirement. ("Every meter belongs to a service point." — "Unless it's in the warehouse before installation." — "Or it's a bulk meter on a DMA inlet, which has no customer at all.")
- **Definition forcing.** When a term appears twice from two mouths, stop and ask both people to define it separately. This is the technique that surfaced the Mizan defect in Module 1 and it takes ninety seconds.

Record everything in the stakeholder's words *first*, then translate. Translating in the room loses the original phrasing, which is the evidence you need when the requirement is later disputed.

### 2. From narrative to a first-cut model

The classical technique — still the fastest — is **noun/verb analysis**. Take the narrative, mark the nouns as entity or attribute candidates and the verbs as relationship candidates, then prune.

Consider this fragment from the Baseerah billing supervisor:

> "When a customer opens an account we register the property and issue a meter. Every month the meter is read — automatically for smart meters, by a field reader otherwise — and we calculate consumption against the tariff band for that property type. If the reading is missing we estimate from the last three months. Government accounts are billed annually, not monthly."

| Extracted | Candidate | Decision |
|---|---|---|
| customer | Entity | Yes — but *account holder*; distinct from `customer_account` |
| account | Entity | Yes — `customer_account` |
| property | Entity | Yes — `service_point` (property is the business word, service point the modelled one) |
| meter | Entity | Yes |
| reading | Entity | Yes — `meter_reading` |
| consumption | Attribute / derived | Derived measure, not an entity |
| tariff band | Entity | Yes — `tariff` with bands |
| property type | Attribute of `service_point` | Attribute, and it *drives* tariff — a rule |
| smart meter / field reader | Attribute (`read_channel`) | Attribute of the reading, not two entities |
| estimate | Rule + attribute | Rule R-07 plus an `is_estimated` flag on the reading |
| government account | Attribute (`customer_category`) + rule | Attribute plus billing-frequency rule R-11 |

Three heuristics decide entity versus attribute:
1. **Does it have its own attributes?** A tariff has a band structure, effective dates, and a rate — entity. A read channel has only a name — attribute.
2. **Does it have an independent lifecycle?** A meter is installed, replaced, retired independently of the account — entity. A property type does not change on its own — attribute.
3. **Would you ever want a list of them for its own sake?** "Show me all tariffs" is a real request; "show me all read channels" is a lookup at best.

### 3. Business rules: the four types

A **business rule** is a statement that defines or constrains some aspect of the business, expressed so it can be checked. Classify each rule, because the type determines where it is enforced.

| Type | Definition | Baseerah example | Enforced by |
|---|---|---|---|
| **Structural** | Asserts the shape of the data | "A meter reading must belong to exactly one meter" | Model: FK + `NOT NULL` (M3) |
| **Constraint** | Restricts allowed values or states | "Consumption volume may not be negative" | Physical: `CHECK` (M5) |
| **Derivation** | Defines how a value is computed | "NRW % = (input volume − billed volume) ÷ input volume × 100" | Transformation: dbt model (M8) |
| **Action-enabling** | Triggers a process when a condition holds | "If a meter reports zero for 60 consecutive days, raise an inspection work order" | Application/orchestration, *not* the model |

The most common professional error is enforcing an action-enabling rule as a constraint, which makes the warehouse reject real data. If Baseerah refuses to load a reading because it should have triggered an inspection, the warehouse is now lying about what happened in the field. Load the truth; raise the alert separately.

The second most common error is leaving a derivation rule unwritten because "the formula is obvious". NRW has at least three defensible formulations depending on whether authorised unbilled consumption (firefighting, mosque supply, network flushing) is subtracted. Baseerah's regulator mandates one. Write it down.

### 4. Writing a rule so it can be tested

A rule is testable when a reader can convert it to a query without asking a question. Use a fixed structure:

```
R-<nnn> | <type> | <owner> | <status>
GIVEN   <the scope: which rows, which period>
WHEN    <the condition>
THEN    <the assertion or the action>
BECAUSE <the business reason, one sentence>
TEST    <the query or expectation that verifies it>
```

Worked example:

```
R-014 | constraint | Billing Directorate (steward.billing@baseerah.gov.sa) | approved
GIVEN   every row in core.meter_reading where read_channel = 'AMI'
WHEN    reading_type = 'delta'
THEN    volume_m3 must be >= 0 AND <= 200
BECAUSE a residential AMI meter physically cannot register more than 200 m3
        in one hour; higher values indicate a meter fault or a unit error,
        both of which must be quarantined rather than billed.
TEST    expect_column_values_to_be_between(volume_m3, 0, 200)
        filtered on read_channel='AMI' AND reading_type='delta'
```

Note what the BECAUSE clause buys you. In eighteen months somebody will find a legitimate 260 m³ hourly reading at an industrial connection and will want to widen the bound. The BECAUSE tells them the rule was scoped to residential meters, so the correct fix is to scope it by `customer_category`, not to loosen it globally. Rules without reasons get loosened; rules with reasons get refined.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Every rule has exactly one named owner:* not a directorate, a person with an email. Ownerless rules cannot be changed and therefore cannot be maintained.
- *Rules are numbered and never renumbered:* R-014 stays R-014 forever, even when superseded, because it is referenced from code, tests, and the data dictionary.
- *Capture the exception with the rule:* a rule with no stated exceptions has not been interrogated hard enough.
- *Separate what is true from what should be true:* the warehouse records reality; controls flag deviation. Conflating them destroys the audit trail.
- *Trace every rule to an enforcement point:* a rule with no enforcement point is a wish.

**Common mistakes (each appears in the Lab 2 starter deliberately)**
1. Recording the stakeholder's *solution* ("add a column `old_meter_no`") instead of the requirement ("meter replacement history must be reconstructable"), which produces a column instead of an entity.
2. Writing an untestable rule ("data must be accurate") that no query can verify and no steward can act on.
3. Encoding an action-enabling rule as a constraint, causing the loader to reject valid field reality.
4. Omitting the rule's scope, so a residential bound is applied to industrial meters and 3% of legitimate data is quarantined.
5. Leaving two contradictory rules from two directorates in the register without escalation, so the implementer silently picks one.
6. Assigning ownership to "IT", which guarantees the business will disown the rule the moment it produces an inconvenient number.

**Production considerations**
- Keep the rule register in the repository as YAML, not in a wiki. It must diff, review, and version with the code that implements it, and Module 6 generates Great Expectations suites directly from it.
- Every rule carries a `status` (`draft` / `approved` / `superseded`) and a `supersedes` link. Regulators ask what the rule was on a given date; a register without history cannot answer.
- Budget for the escalation path *before* you find a contradiction. "Contradictions go to the Data Governance Committee, which meets fortnightly" is a plan; discovering you need one mid-build is a delay.

### 6. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's requirements phase collected 63 rules from three directorates. Two of them read, in the original words:

- Billing: "A customer is active if their account status is ACTIVE." (Owner: Billing Directorate.)
- Network Operations: "A customer is active if we delivered water to them this quarter." (Owner: Network Operations.)

Nobody noticed for six weeks, because both were true statements about the business and neither team read the other's rules. The contradiction surfaced only when the coverage KPI on the draft dashboard could be computed two ways, giving 58,100 and 49,780 customers for the same district — the 14.3% gap the Module 1 simulation reproduces.

The resolution is the teaching point. The Data Governance Committee did not choose a winner. It ruled that both concepts exist and gave them separate names and separate owners — `registered_customer` (billing) and `supplied_customer` (network operations) — banned the unqualified term "active customer" from all Baseerah artefacts, and required every dashboard tile to name the measure it renders. Two rules, two owners, zero ambiguity. That decision, recorded as R-021 and R-022 with a `supersedes` link to the ambiguous R-009, is what participants replicate in Lab 2 and consume in Lab 8's KPI register.

## Code Examples

### The rule register as versionable YAML

```yaml
# rules/baseerah_rules.yml
#
# WHY: business rules must diff, review, and version alongside the code that
# implements them. A wiki page cannot be code-reviewed, cannot be tested, and
# cannot answer "what was the rule on 2026-03-01?". This file is the single
# source of truth for Baseerah's rules; Module 6 generates Great Expectations
# suites from it and Module 8 publishes it into the data dictionary.
#
# Numbering is permanent. A superseded rule is never deleted and never reused.

version: 1.4
register_owner: data.governance@baseerah.gov.sa
escalation: "Contradictions go to the Data Governance Committee (fortnightly, Sundays)."

rules:
  - id: R-003
    type: structural
    owner: steward.ops@baseerah.gov.sa
    status: approved
    approved_on: 2026-02-11
    given: "every row in core.meter_reading"
    when: "always"
    then: "meter_id must be NOT NULL and must reference an existing core.meter"
    because: >
      A reading that cannot be attributed to a physical device cannot be billed,
      cannot be attributed to a DMA, and silently corrupts the non-revenue-water
      denominator.
    enforcement: "FOREIGN KEY core.meter_reading.meter_id -> core.meter(meter_id)"
    test: "expect_column_values_to_not_be_null(meter_id)"

  - id: R-009
    type: derivation
    owner: data.governance@baseerah.gov.sa
    status: superseded
    superseded_by: [R-021, R-022]
    given: "customer accounts in the reporting district"
    when: "computing the coverage KPI"
    then: "count customers where the customer is active"
    because: "Original ambiguous rule retained for audit; see R-021 and R-022."
    enforcement: none
    test: none

  - id: R-021
    type: derivation
    owner: steward.billing@baseerah.gov.sa
    status: approved
    approved_on: 2026-03-04
    supersedes: [R-009]
    given: "core.customer_account as at the reporting date"
    when: "computing registered_customer_count"
    then: "count accounts where account_status = 'ACTIVE'"
    because: >
      Billing's registered base is the legal customer count used for tariff
      and licensing returns. It deliberately includes seasonal and disputed
      accounts because the authority still holds a contractual obligation.
    enforcement: "mart model fct_customer_snapshot + KPI register entry"
    test: "dbt test: not_null(account_status); accepted_values(account_status)"

  - id: R-022
    type: derivation
    owner: steward.network@baseerah.gov.sa
    status: approved
    approved_on: 2026-03-04
    supersedes: [R-009]
    given: "core.meter_reading for the reporting quarter"
    when: "computing supplied_customer_count"
    then: >
      count distinct account_id having SUM(volume_m3) > 0 across the quarter
    because: >
      Network Operations reports service coverage, which requires evidence of
      actual delivery. An ACTIVE account with zero consumption is registered
      but not supplied, and counting it overstates network reach.
    enforcement: "mart model fct_meter_read_hourly aggregated in the KPI layer"
    test: "reconciliation: supplied_customer_count <= registered_customer_count"

  - id: R-014
    type: constraint
    owner: steward.billing@baseerah.gov.sa
    status: approved
    approved_on: 2026-02-19
    given: "core.meter_reading where read_channel = 'AMI' and reading_type = 'delta'"
    when: "the service point customer_category = 'RESIDENTIAL'"
    then: "volume_m3 must be between 0 and 200 inclusive"
    because: >
      A residential AMI meter cannot physically register more than 200 m3 in one
      hour. Higher values indicate a meter fault or a litre/cubic-metre unit
      error; both must be quarantined for steward review, never billed.
    enforcement: "CHECK constraint on core.meter_reading + GX quarantine rule"
    test: "expect_column_values_to_be_between(volume_m3, 0, 200)"

  - id: R-031
    type: action_enabling
    owner: steward.network@baseerah.gov.sa
    status: approved
    approved_on: 2026-02-25
    given: "core.meter_reading aggregated to a daily grain"
    when: "a meter reports zero volume for 60 consecutive days"
    then: "raise an inspection work order in the maintenance system"
    because: >
      Sustained zero consumption is the strongest single indicator of a stopped
      meter, which is the largest component of apparent (non-physical) losses
      in the NRW figure.
    # CRITICAL: enforcement is a downstream process, NOT a database constraint.
    # Rejecting the load would make the warehouse lie about what the field
    # actually reported.
    enforcement: "Airflow task baseerah_dq.raise_zero_read_inspections"
    test: "unit test on the detection query against a fixture with 3 known meters"
```

### Turning the register into executable tests

```python
# src/baseerah/rules/compile_rules.py
"""Compile the YAML rule register into Great Expectations expectations.

WHY: a rule written in a document and a test written in code drift apart within
one release. Generating the tests FROM the register makes drift impossible: if
the rule changes, the test changes in the same commit, and a rule with no
enforcement is visible as a gap rather than hidden as an omission.

Only `constraint` and `structural` rules compile to expectations.
`derivation` rules become dbt models (Module 8) and `action_enabling` rules
become Airflow tasks -- this function refuses to compile them, loudly.
"""
from __future__ import annotations

import pathlib
from typing import Any

import yaml

COMPILABLE = {"constraint", "structural"}


def load_register(path: pathlib.Path) -> dict[str, Any]:
    """Read the register and reject duplicate or renumbered rule IDs."""
    register = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = [r["id"] for r in register["rules"]]
    duplicates = {i for i in ids if ids.count(i) > 1}
    if duplicates:
        raise ValueError(f"Rule IDs are permanent and unique; duplicated: {duplicates}")
    return register


def compile_expectations(register: dict[str, Any]) -> list[dict[str, Any]]:
    """Emit a Great Expectations expectation config per compilable rule.

    The rule ID is carried into `meta` so that a failing expectation in the
    Day-3 quality gate points a steward straight back at the owning rule and
    its BECAUSE clause -- the single biggest reduction in triage time we get
    from this whole approach.
    """
    expectations: list[dict[str, Any]] = []
    for rule in register["rules"]:
        if rule["status"] != "approved":
            continue  # draft and superseded rules never gate a pipeline
        if rule["type"] not in COMPILABLE:
            continue
        if rule.get("test") in (None, "none"):
            raise ValueError(
                f"{rule['id']} is an approved {rule['type']} rule with no test. "
                "Approved structural/constraint rules must be enforceable."
            )
        expectations.append(
            {
                "expectation_type": _expectation_type(rule["test"]),
                "kwargs": _expectation_kwargs(rule["test"]),
                "meta": {
                    "rule_id": rule["id"],
                    "owner": rule["owner"],
                    "because": rule["because"].strip(),
                    "scope": rule["given"],
                },
            }
        )
    return expectations


def _expectation_type(test: str) -> str:
    """`expect_column_values_to_be_between(volume_m3, 0, 200)` -> the type."""
    return test.split("(", 1)[0].strip()


def _expectation_kwargs(test: str) -> dict[str, Any]:
    """Parse the positional args of the shorthand test syntax.

    Deliberately strict: an unparseable test string is a register defect and
    must fail the build rather than silently produce a weaker expectation.
    """
    inner = test.split("(", 1)[1].rsplit(")", 1)[0]
    parts = [p.strip() for p in inner.split(",") if p.strip()]
    kwargs: dict[str, Any] = {"column": parts[0]}
    if len(parts) == 3:
        kwargs["min_value"] = float(parts[1])
        kwargs["max_value"] = float(parts[2])
    elif len(parts) != 1:
        raise ValueError(f"Cannot parse test shorthand: {test!r}")
    return kwargs


if __name__ == "__main__":
    reg = load_register(pathlib.Path("rules/baseerah_rules.yml"))
    exps = compile_expectations(reg)
    print(f"Compiled {len(exps)} expectations from {len(reg['rules'])} rules")
    for e in exps:
        print(f"  {e['meta']['rule_id']}: {e['expectation_type']}({e['kwargs']['column']})")
```

## Hands-on Lab 2 — Elicit and Register the Baseerah Business Rules

| | |
|---|---|
| **Objective** | Run two scripted stakeholder interviews, extract a first-cut entity/attribute set, and produce a register of 20 structured, testable, owned rules — including at least one contradiction escalated rather than silently resolved |
| **Duration** | 50 minutes |
| **Setup** | Course repo, `git checkout lab2-start`, `pip install pyyaml==6.0.* great-expectations==0.18.*`; two participants per pair take the persona cards from `docs/personas/` (NRW Analyst, Billing Supervisor) |

**Instructions & tasks**

1. *(10 min)* Run interview A. One participant plays the **Billing Supervisor** persona from the card; the other elicits using process walkthrough and exception hunting. Record verbatim notes in `LAB2_INTERVIEW_A.md` — the stakeholder's words, not your translation.
2. *(10 min)* Swap and run interview B with the **NRW Analyst** persona. The card deliberately contains a statement that contradicts the Billing Supervisor's definition of an active customer. Do not resolve it in the room.
3. *(10 min)* Perform noun/verb analysis on both transcripts. Produce `LAB2_CANDIDATES.md` with a three-column table: candidate | entity/attribute/derived/rule | which of the three heuristics decided it. Expect 30–36 candidates.
4. *(12 min)* Write 20 rules into `rules/baseerah_rules.yml` using the GIVEN/WHEN/THEN/BECAUSE/TEST structure. Cover all four types: at least 6 structural, 6 constraint, 5 derivation, 3 action-enabling. Every rule needs an owner email and a status.
5. *(5 min)* Run `python -m baseerah.rules.compile_rules`. It must compile your structural and constraint rules and must *refuse* any approved rule with no test. Fix what it rejects, then record the contradiction from step 2 as two separately named rules with an escalation note.
6. *(3 min)* Commit: `feat(rules): baseerah business-rule register v1.0 with 20 owned rules`.

**Expected output**
```
$ python -m baseerah.rules.compile_rules
Compiled 12 expectations from 20 rules
  R-003: expect_column_values_to_not_be_null(meter_id)
  R-004: expect_column_values_to_not_be_null(service_point_id)
  R-006: expect_column_values_to_be_unique(meter_serial)
  R-014: expect_column_values_to_be_between(volume_m3)
  R-015: expect_column_values_to_be_between(pressure_bar)
  ...
Skipped 5 derivation rules  -> implemented as dbt models (Module 8)
Skipped 3 action_enabling rules -> implemented as Airflow tasks (Module 8)

$ python -m baseerah.rules.lint_register
WARN  R-018 and R-019 both define 'active customer' with different logic.
      Owners differ (billing vs network). ESCALATION REQUIRED.
      -> recorded in LAB2_ESCALATIONS.md as governance item GOV-001
1 contradiction found, 1 escalated. OK.
```

**Acceptance criteria**
- 20 rules, all with owner email, status, and a BECAUSE clause of at least one full sentence.
- Type coverage: ≥ 6 structural, ≥ 6 constraint, ≥ 5 derivation, ≥ 3 action-enabling.
- `compile_rules.py` produces 12 expectations and rejects nothing.
- The active-customer contradiction is escalated as GOV-001, not silently resolved, and the superseded rule retains its number.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `ValueError: approved rule with no test` | An approved structural/constraint rule left `test: none` | Either write the test or drop status back to `draft` — an unenforceable approved rule is a lie |
| `Cannot parse test shorthand` | Free-text test description instead of the shorthand syntax | Use `expectation_name(column[, min, max])` |
| Only 4 rules compile | Most rules written as derivations | Derivations are valuable but do not gate loads; rebalance towards structural/constraint |
| Register lint reports 0 contradictions | The two personas were merged into one interview | Re-run interview B separately; the contradiction is the lesson |

**Instructor notes.** The single behaviour to watch for in task 1 is the elicitor writing down solutions instead of requirements. When you hear a participant note "add a column for the old meter number", stop the pair and ask what the supervisor is actually trying to do — reconstruct replacement history. That is mistake #1 and it is the difference between a column and an entity. In task 5, some pairs will "helpfully" resolve the contradiction by picking billing's definition. Push back hard: an analyst who resolves a governance question by preference has just made a decision they have no authority to make, and it will reappear as a wrong number on an executive dashboard in Module 8. Fast finishers: write the three exception cases for R-014 (industrial meters, bulk DMA inlet meters, and meters under test) and re-scope the rule properly.

## Mini Exercises

**Quiz (5 questions)**
1. Which rule type must never be enforced as a database constraint? → **action-enabling** — rejecting the load makes the warehouse misreport reality.
2. What does the BECAUSE clause protect against? → rules being loosened instead of refined when a legitimate exception appears.
3. Give the three heuristics for entity versus attribute. → own attributes; independent lifecycle; worth listing for its own sake.
4. Where does NRW % belong in the four-type classification? → **derivation** — implemented as a dbt model, not a constraint.
5. True/False: a superseded rule should be deleted from the register. → **False** — it is retained with a `superseded_by` link for audit.

**Debugging exercise.** Check out `git checkout lab2-overzealous-constraint`. R-031 (the 60-day zero-consumption rule) has been implemented as a `CHECK` constraint that rejects any reading of zero. Symptom: the nightly load fails at 02:14 with 11,480 rejected rows, and the on-call engineer disables the constraint to get the load through — permanently. Discuss: what did the organisation lose (the ability to detect stopped meters, *and* the constraint entirely), and what is the correct enforcement point? This opens the broader discussion of why a control that blocks the pipeline gets deleted while a control that raises a task gets worked.

**Design exercise.** The finance directorate states: "Revenue is recognised when the invoice is issued, not when it is collected." Write this as a structured rule with all five clauses, classify its type, name a plausible owner, and state its enforcement point. Then state what would have to change in the model if the authority later moved to cash-basis recognition for one customer category.

**Discussion questions.**
- A directorate refuses to name an individual owner for a rule, offering only the directorate name. What are you actually being told, and what do you do?
- Is it ever correct to ship a warehouse with a known, unresolved rule contradiction? Argue for it, then say what must be true about the dashboard for it to be defensible.

## Case Study — The Two Harvests at "Hasad" (حصاد)

**Scenario.** "Hasad" (حصاد), a Saudi agricultural procurement cooperative operating grain-receiving centres in Al-Qassim, Hail, and Al-Jouf, built a settlement warehouse to compute payments to 24,000 registered farmers. In its first season the warehouse computed a total procurement liability of SAR 812 million; the finance directorate's own ledger showed SAR 847 million. The 4.3% gap — SAR 35 million — arrived one week before the seasonal payment run.

**Business context.** Farmers are paid per tonne delivered, at a grade-adjusted price, within 30 days of delivery. A late or wrong payment run is a national news story and a ministerial escalation. The cooperative cannot delay the run.

**Technical challenge.** No rule register existed. Three rules had been implemented from three separate conversations: the receiving centres' rule ("a delivery is counted when the truck is weighed out"), the quality lab's rule ("a delivery is counted when the grade certificate is issued", typically 1–3 days later), and finance's rule ("a delivery is counted when the receipt note is posted", which happens in batches). Deliveries near the season boundary fell into different periods under each rule, and roughly 39,000 tonnes sat in the gap.

**Constraints.** The season boundary is fixed by ministerial regulation and cannot be moved. Grade certificates are legally required before payment, so the quality-lab timestamp cannot simply be ignored. Farmer-level delivery data includes national ID and bank details — PDPL personal data — so the reconciliation cannot be done by emailing extracts between three directorates, which is exactly what was proposed in the first crisis meeting.

**Solution approach (facilitate, don't lecture).** Guide the room to separate the three timestamps as three distinct modelled attributes of one `Delivery` entity (`weighed_out_ts`, `graded_ts`, `posted_ts`) rather than choosing one; then define three separately named derivation rules — `delivered_tonnes` (operations), `certified_tonnes` (quality), `payable_tonnes` (finance) — each with an owner, and declare that the seasonal liability figure uses `payable_tonnes` because that is the one the regulation defines. The reconciliation between the three becomes a permanent report rather than a crisis. Push the room past the tempting shortcut of "just use the weigh-out timestamp for everything": it would make this year's number match and would silently misstate the liability of every delivery graded after the boundary in every future season.

**Discussion questions.**
1. Which of the four rule types were all three of Hasad's rules, and why did that make the divergence invisible to every database constraint in the system?
2. What is the cheapest artefact that would have caught this in week one of the programme, and who would have had to read it?
3. Finance proposes making its rule the only one and deleting the other two. What is lost operationally, and how do you argue it?
4. The reconciliation report must show farmer-level differences to be useful, but farmer identity is PDPL personal data. How do you design the report so stewards can act without a bulk personal-data export?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Rules registered | Coverage | 20 rules across all 4 types | `baseerah_rules.yml` count by type |
| Rule testability | Quality | 100% of approved structural/constraint rules compile | `compile_rules.py` exit code |
| Ownership completeness | Governance | 100% of rules have an individual owner email | register lint |
| Contradictions escalated | Governance | 1/1 escalated as GOV-001, none silently resolved | `LAB2_ESCALATIONS.md` review |
| Candidate extraction rate | Analysis | 30–36 candidates from two transcripts | `LAB2_CANDIDATES.md` count |

**Example benchmark table (filled during lab):**

| Rule type | Count | Compiles to expectations | Enforcement point | Module implemented |
|---|---|---|---|---|
| structural | 6 | 6 | FK / NOT NULL | M3 → M5 |
| constraint | 6 | 6 | CHECK / GX quarantine | M5 → M6 |
| derivation | 5 | 0 | dbt model + KPI register | M8 |
| action_enabling | 3 | 0 | Airflow task | M8 |
| **Total** | **20** | **12** | — | — |

## Required Visuals and Training Assets

### Diagrams
1. **Narrative → model funnel** — *Purpose:* make noun/verb analysis concrete. *Elements:* the billing-supervisor paragraph on the left with nouns and verbs highlighted in two colours, funnelling into three output bins (entity, attribute, rule) with the three heuristics as gates. *Style:* left-to-right funnel with gate icons. *Designer description:* "A block of quoted text whose highlighted words flow down through three labelled sieves into three trays."
2. **The four rule types and their enforcement points** — *Purpose:* the module's central discrimination. *Elements:* four rule cards, each with an arrow to its enforcement layer (model / physical constraint / transformation / orchestration), with a red cross showing the action-enabling → constraint mis-wiring. *Style:* four-lane mapping with one deliberate anti-pattern marked.
3. **Rule lifecycle** — *Purpose:* explain permanence and supersession. *Elements:* R-009 draft → approved → superseded, with R-021 and R-022 branching from it; audit trail ribbon underneath. *Style:* timeline with branch.
4. **Escalation path** — *Purpose:* show that contradiction has a process, not a preference. *Elements:* two contradicting rules → lint detection → GOV item → Data Governance Committee → two renamed rules + glossary ban on the ambiguous term. *Style:* swimlane with the committee as a distinct lane.

### Images (screenshots)
1. **The persona card for the NRW Analyst** — *why:* participants must see the level of detail a good persona carries; *content:* the card with its planted contradiction highlighted for the instructor's copy only.
2. **`compile_rules.py` refusing an untestable approved rule** — *why:* the gate must be seen to bite; *content:* the traceback with the rule ID and the message.
3. **Register lint output showing GOV-001** — *why:* contradiction detection is the module's payoff; *content:* the WARN block with both rule IDs and owners.

### Simulations
1. **The disappearing constraint** — *Setup:* branch `lab2-overzealous-constraint` with R-031 mis-implemented as a CHECK. *Expected behaviour:* the nightly load rejects 11,480 rows and the provided "on-call fix" script disables the constraint entirely. *Learning objective:* a control at the wrong enforcement point is deleted, not fixed — you lose both the rule and the control.
2. **Scope drift** — *Setup:* branch `sim-rule-scope` applies R-014's 0–200 m³ bound to all meters instead of residential AMI meters. *Expected behaviour:* 2,940 legitimate industrial readings (3.1% of industrial volume) are quarantined and the district's billed volume drops by 4.2%, worsening the NRW figure. *Learning objective:* an unscoped rule manufactures data-quality defects.

### Interactive Activities
- **Requirement or solution? (12 min):** 16 quoted stakeholder statements sorted into "requirement", "solution in disguise", or "complaint"; for each solution, the group states the underlying requirement.
- **Three whys (10 min):** in pairs, one participant states a Baseerah rule and the other asks "when is that not true?" three times. Collect the best-discovered exception from each pair on the whiteboard.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `docs/personas/*.md` | Two scripted stakeholder persona cards written for this course | Markdown | 2 cards, ~900 words | Interview material with a planted contradiction |
| `rules/baseerah_rules.yml` | Lab 2 starter (5 rules pre-filled, 15 to add) | YAML | 20 rules at completion | The rule register; consumed by M5, M6, M8 |
| `docs/artefacts/nrw_submission_q4.xlsx` | Synthetic prior regulator submission | XLSX | 1 sheet, 42 rows | Artefact archaeology exercise |
| `docs/artefacts/supervisor_private_tracker.xlsx` | Synthetic private spreadsheet with 3 unmodelled rules | XLSX | 2 sheets, 310 rows | The richest requirements source in the lab |

### Demo Requirements
- **Instructor demo (6 min):** open `supervisor_private_tracker.xlsx` live and find the three rules the official system does not implement (a manual estimate override, a hand-maintained list of "meters we know are broken", and a colour-coded disconnection exclusion). Say out loud: "every one of these is a requirement someone decided not to tell us, and every one of them will otherwise arrive as a data-quality defect on Day 3."

---

# Module 3 — Entity–Relationship Design, Keys, and Cardinality
## تصميم الكيانات والعلاقات

## Module Overview

**Purpose.** This module turns the conceptual model and the rule register into a precise logical model: every entity given its attributes, every relationship given a cardinality and an optionality, every table given a key that will still be correct in ten years. It covers catalogue Module 3 completely, and it is where the surrogate-versus-natural-key decision — the decision that most often ages badly — is made deliberately rather than by habit.

**Business relevance.** Key design is the most expensive reversible decision in a data platform, and the least visible. A utility that used the meter serial number as the primary key discovers, at meter-replacement time, that its entire reading history is now attached to a device rather than to a location. Correcting that after five years of history means a migration of hundreds of millions of rows and a restatement of every historic consumption report. Getting it right on Day 2 costs nothing.

**Industry use cases.**
- A national registry must model one-to-one relationships that are optional on one side (every licence has at most one appeal) without creating nullable sprawl.
- A logistics operator must resolve a genuine many-to-many (a shipment may be carried on several legs; a leg carries several shipments) into an associative entity that carries its own attributes.
- A utility must model a self-referencing hierarchy (a network main feeds sub-mains feeds service connections) without a fixed depth.

**Expected competencies.** After this module a participant can identify strong and weak entities and their attributes; classify relationships by cardinality and optionality and read crow's-foot notation fluently; resolve many-to-many relationships with associative entities that carry attributes; choose between natural, surrogate, and composite keys with a stated rationale; and specify referential-integrity actions that match the business rule rather than the default.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Identify main and supporting entities and assign attributes with domains | LO3, LO1 |
| 3.2 | Classify relationships by cardinality (1:1, 1:M, M:N) and optionality | LO3 |
| 3.3 | Resolve many-to-many relationships with associative entities | LO3, LO4 |
| 3.4 | Choose primary, foreign, and alternate keys with a defensible rationale | LO3 |
| 3.5 | Specify referential-integrity actions that implement the owning business rule | LO3, LO5 |

## Technical Content

### 1. Entities, attributes, domains

A **strong entity** exists independently and is identified by its own attributes: `customer_account`, `meter`, `network_asset`. A **weak entity** cannot be identified without its parent: `invoice_line` is meaningless without `invoice`, and its identity is `(invoice_id, line_no)`. Weak entities participate in **identifying relationships**, drawn with a solid line, and their parent key is part of their own key.

Every attribute needs a **domain** — the set of values it may take — recorded at the logical level, not discovered at load time. Baseerah's `read_channel` has domain `{AMI, MANUAL, ESTIMATED, BULK}`; `pressure_bar` has domain `NUMERIC(5,2)` in `[0.00, 25.00]`. Domains recorded here become CHECK constraints in Module 5 and Great Expectations rules in Module 6 without further analysis.

Distinguish three attribute kinds: **identifying** (part of a key), **descriptive** (the business content), and **derived** (computable from others). Derived attributes are recorded in the logical model *and marked as derived*, so the physical model can decide independently whether to store or compute them. `volume_m3` on a reading is derived from consecutive index values; storing it is a performance decision, marking it derived is a modelling decision.

### 2. Cardinality and optionality — read them as sentences

Cardinality answers "how many"; optionality answers "must there be any". Together they produce four readings per relationship, and the discipline is to say all four aloud:

| Relationship | Reading | Baseerah truth |
|---|---|---|
| `customer_account` — `service_point` | One account serves **one or more** service points; one service point is served by **exactly one** account *at a time* | 1:M, mandatory both sides |
| `service_point` — `meter` | One service point has **zero or more** meters over its life; one meter is installed at **zero or one** service point | 1:M, optional both sides (a meter in the warehouse has no service point) |
| `meter` — `meter_reading` | One meter has **zero or more** readings; one reading belongs to **exactly one** meter | 1:M, mandatory on the reading side |
| `network_asset` — `network_asset` | One asset **may feed** zero or more assets; one asset **is fed by** zero or one asset | 1:M self-referencing, optional |
| `customer_account` — `meter` (mixed-use) | One account may share **zero or more** meters; one meter may be shared by **one or more** accounts | **M:N — must be resolved** |

The optional-meter case is the one participants get wrong. If `meter.service_point_id` is `NOT NULL`, the authority cannot record a meter that has been procured but not yet installed — and the asset register, which must account for every device, becomes unable to represent reality. That is a modelling error masquerading as data-integrity rigour.

### 3. Resolving many-to-many

A relational database cannot store M:N directly. The resolution is an **associative entity** (also called a junction, link, or bridge table). The mechanical part is easy; the professional part is recognising that the associative entity almost always has **attributes of its own**, and those attributes are the actual requirement.

Baseerah's mixed-use buildings need `account_meter_share(account_id, meter_id, valid_from, valid_to, share_pct)`. The share percentage does not belong to the account or to the meter — it belongs to the *relationship*, and it is time-bounded because the split changes when tenancies change. Any design that stores `share_pct` on either parent is wrong, and the wrongness will show up as an unallocated remainder in the revenue reconciliation.

The same pattern resolves `work_order` ↔ `technician` (a job may need two technicians; a technician works many jobs) with `work_order_assignment(work_order_id, technician_id, role, hours_logged)`. Again: `role` and `hours_logged` are relationship attributes. This associative entity becomes the bridge table of Module 7.

### 4. Keys: natural, surrogate, composite

| Key type | Definition | Baseerah example | When to use | Failure mode |
|---|---|---|---|---|
| **Natural** | A real-world identifier that already exists | `meter_serial`, `national_id` | Only when guaranteed unique, stable, non-null, and non-sensitive | Reissued serials; PDPL exposure of national ID in every FK |
| **Surrogate** | A meaningless system-generated value | `meter_id BIGINT IDENTITY` | Default choice for warehouse and most operational entities | Duplicates hide behind different surrogates unless a natural key is also enforced |
| **Composite** | Two or more attributes together | `(invoice_id, line_no)` | Weak entities and associative entities where the combination *is* the identity | Wide FKs propagate into every child; painful joins |
| **Alternate (business) key** | A unique natural key kept alongside a surrogate | `UNIQUE(meter_serial)` | Always, when a natural key exists | Omitting it is how 3,320 duplicate customers appear in Module 6 |

The rule to teach: **use a surrogate primary key and enforce the natural key as a UNIQUE constraint.** This is not fence-sitting; each key does a different job. The surrogate gives stable, narrow, non-sensitive joins and lets the natural key change without cascading. The unique constraint preserves the business truth that two rows with the same meter serial are the same meter — which is precisely the truth that, when omitted, produces the duplicate-customer crisis Module 6 spends an hour repairing.

Two PDPL consequences make this non-negotiable at Baseerah. First, a national ID used as a foreign key propagates personal data into every child table, including tables that have no business need for it — a data-minimisation breach by design. Second, an erasure or correction request against a natural key means updating every child row; against a surrogate it means updating one.

### 5. Referential integrity: match the action to the rule

Foreign keys default to `NO ACTION`, and defaults are how business rules get lost. For each relationship, decide the delete and update behaviour from the rule register:

- `meter_reading.meter_id → meter` : **RESTRICT** on delete. A meter with readings may never be deleted; retiring it is a status change. (R-003.)
- `account_meter_share.account_id → customer_account` : **CASCADE** on delete. The share only exists as part of the relationship; if the account is genuinely removed, the share is meaningless.
- `service_point.dma_id → district_metered_area` : **RESTRICT**. DMA boundaries are redrawn by re-pointing service points, never by deleting a DMA.
- `meter.service_point_id → service_point` : **SET NULL** on delete is *wrong* here even though the column is nullable — it would silently orphan an installed meter. Use RESTRICT and require an explicit uninstall.

Note the last one. Nullable does not mean "safe to null". Optionality describes what states are legal; the referential action describes how the system may move between them.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Read every relationship aloud in both directions* before drawing it. Half of all cardinality errors are caught by the sentence sounding wrong.
- *Surrogate PK + UNIQUE natural key,* always, when a natural key exists.
- *Relationship attributes belong to the associative entity,* never to a parent.
- *Optionality is a business fact,* not a convenience; `NOT NULL` that contradicts reality forces workarounds that corrupt data.
- *Name foreign keys after the role,* not the target table, when an entity plays two roles (`raised_by_technician_id`, `closed_by_technician_id`).

**Common mistakes (each appears in the Lab 3 starter deliberately)**
1. `meter_serial` as the primary key of `meter` — breaks when a serial is reissued by a manufacturer and exposes reading history to renumbering.
2. `meter.service_point_id NOT NULL` — makes uninstalled stock unrepresentable.
3. `share_pct` stored on `customer_account` instead of on the associative entity — produces shares that do not sum to 100 and a permanent revenue remainder.
4. An M:N left unresolved between `work_order` and `technician`, "solved" with `technician_1_id` and `technician_2_id` columns — the repeating-group anti-pattern Module 4 formally kills.
5. A composite FK `(account_id, meter_id)` propagated into three child tables, making every downstream join four-column and every index enormous.
6. All foreign keys left at the default `NO ACTION`, so the delete rules from the register are simply absent.

**Production considerations**
- Index every foreign key column. PostgreSQL indexes the referenced primary key automatically but *not* the referencing column, and an unindexed FK turns every parent delete into a sequential scan of the child.
- Keep keys narrow: an eight-byte `BIGINT` surrogate versus a 40-character composite text key is a difference of gigabytes across a 13-million-row fact table and every index on it.
- Decide the identity generation strategy explicitly: `GENERATED ALWAYS AS IDENTITY` prevents application code from inserting its own values, which is what you want for a warehouse-owned surrogate.

### 7. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's predecessor system keyed `meter` on `meter_serial`. In 2023 a manufacturer reissued a serial block, and 1,180 new meters arrived carrying serials already present in the register. The load failed on a unique violation — which was, ironically, the system working correctly. The operational fix, applied under pressure, was to append `-B` to the new serials. Eighteen months later a field technician scanned a physical meter, searched the serial as printed, found nothing, and raised a fault on the wrong device; the correct device kept leaking for another five weeks. The cost was not the migration; it was that the primary key had become a value humans had to remember to distort. A surrogate `meter_id` with `UNIQUE(meter_serial, manufacturer_code)` would have absorbed the reissue with no human ever knowing.

## Code Examples

### The logical model as DBML, with keys, cardinality, and domains

```
// models/logical/baseerah_logical.dbml
//
// WHY: the logical model is where cardinality, optionality, keys and domains
// become precise. It is still engine-neutral -- no index types, no partitions,
// no tablespaces (those arrive in Module 5). Every relationship below was read
// aloud in both directions before it was drawn, and every note cites the rule
// from rules/baseerah_rules.yml that justifies it.

Table customer_account {
  account_id        bigint      [pk, note: 'surrogate; GENERATED ALWAYS AS IDENTITY']
  account_no        varchar(16) [unique, not null, note: 'natural/business key from billing CRM']
  holder_national_id varchar(10) [null, note: 'PDPL personal. NOT a key. Masked outside core.']
  customer_category varchar(20) [not null, note: 'domain: RESIDENTIAL|COMMERCIAL|GOVERNMENT|INDUSTRIAL']
  account_status    varchar(16) [not null, note: 'domain: ACTIVE|SUSPENDED|CLOSED|DISPUTED (R-021)']
  tariff_id         bigint      [not null]
  opened_on         date        [not null]
  closed_on         date        [null, note: 'null = open; CHECK closed_on >= opened_on in M5']
}

Table service_point {
  service_point_id  bigint      [pk]
  national_address  varchar(12) [unique, not null, note: 'PDPL quasi-identifier']
  account_id        bigint      [not null, note: 'exactly one account at a time (1:M mandatory)']
  dma_id            bigint      [not null, note: 'a point sits in exactly one DMA (RESTRICT on delete)']
  property_type     varchar(20) [not null, note: 'drives tariff band -- see R-011']
  city              varchar(40) [not null, note: 'domain: Riyadh|Jeddah|Dammam|Al-Ahsa|Abha|Madinah|Jubail']
}

Table meter {
  meter_id          bigint      [pk, note: 'surrogate: absorbs manufacturer serial reissue']
  meter_serial      varchar(24) [not null]
  manufacturer_code varchar(8)  [not null]
  service_point_id  bigint      [null, note: 'NULLABLE: procured-but-not-installed stock is real']
  meter_type        varchar(12) [not null, note: 'domain: AMI|MECHANICAL|BULK']
  installed_on      date        [null]
  removed_on        date        [null]

  indexes {
    (meter_serial, manufacturer_code) [unique, name: 'uq_meter_serial_mfr']
  }
}

Table meter_reading {
  reading_id        bigint      [pk]
  meter_id          bigint      [not null, note: 'RESTRICT on delete (R-003)']
  read_ts           timestamptz [not null]
  read_channel      varchar(10) [not null, note: 'domain: AMI|MANUAL|ESTIMATED|BULK']
  reading_type      varchar(8)  [not null, note: 'domain: index|delta -- the M1 grain lesson']
  index_m3          numeric(12,3) [null, note: 'cumulative odometer value; null for delta rows']
  volume_m3         numeric(10,3) [null, note: 'DERIVED from consecutive indexes; 0..200 for res. AMI (R-014)']
  is_estimated      boolean     [not null, default: false]

  indexes {
    (meter_id, read_ts) [unique, name: 'uq_reading_meter_ts']
  }
}

// Associative entity resolving the M:N between accounts and shared meters.
// share_pct belongs HERE -- it is a property of the relationship, not of
// either parent. Time-bounded because tenancy splits change.
Table account_meter_share {
  account_id  bigint       [not null]
  meter_id    bigint       [not null]
  valid_from  date         [not null]
  valid_to    date         [not null, default: '9999-12-31']
  share_pct   numeric(5,2) [not null, note: 'shares for a meter+period must sum to 100.00']

  indexes {
    (account_id, meter_id, valid_from) [pk]
  }
}

Table work_order {
  work_order_id     bigint      [pk]
  work_order_no     varchar(20) [unique, not null, note: 'becomes a DEGENERATE dimension in M7']
  asset_id          bigint      [null, note: 'null when the job targets a service point, not an asset']
  service_point_id  bigint      [null]
  raised_ts         timestamptz [not null]
  closed_ts         timestamptz [null]
  wo_type           varchar(24) [not null, note: 'domain: LEAK_REPAIR|METER_EXCHANGE|INSPECTION|DISCONNECT']
}

// Second M:N resolution: a job may need several technicians; a technician
// works many jobs. role and hours_logged are relationship attributes.
Table work_order_assignment {
  work_order_id bigint       [not null]
  technician_id bigint       [not null]
  role          varchar(16)  [not null, note: 'domain: LEAD|SUPPORT|INSPECTOR']
  hours_logged  numeric(5,2) [not null]

  indexes {
    (work_order_id, technician_id) [pk]
  }
}

Ref: customer_account.tariff_id > tariff.tariff_id                       // M:1 mandatory
Ref: service_point.account_id > customer_account.account_id              // M:1 mandatory
Ref: service_point.dma_id > district_metered_area.dma_id                 // M:1 mandatory
Ref: meter.service_point_id > service_point.service_point_id             // M:1 OPTIONAL
Ref: meter_reading.meter_id > meter.meter_id                             // M:1 mandatory
Ref: account_meter_share.account_id > customer_account.account_id
Ref: account_meter_share.meter_id > meter.meter_id
Ref: work_order.asset_id > network_asset.asset_id
Ref: work_order_assignment.work_order_id > work_order.work_order_id
Ref: work_order_assignment.technician_id > technician.technician_id
```

### Verifying cardinality claims against the actual data

```sql
-- sql/validation/030_verify_cardinality.sql
--
-- WHY: a cardinality drawn on a diagram is a hypothesis about the business.
-- Before we cast it into NOT NULL and UNIQUE constraints in Module 5, we test
-- it against the landed source data. Every row this returns is either a data
-- defect (Module 6 fixes it) or a modelling error (we fix the diagram now).
-- Running this BEFORE writing DDL is the single cheapest hour in the course.

-- Claim 1: one service point is served by exactly one account AT A TIME.
-- A violation means either overlapping account periods or a genuine M:N we
-- have not modelled (mixed-use buildings -- see account_meter_share).
SELECT 'C1: service_point served by >1 account' AS claim,
       sp.service_point_id,
       count(DISTINCT sp.account_id) AS distinct_accounts
FROM   raw.service_point_extract AS sp
GROUP  BY sp.service_point_id
HAVING count(DISTINCT sp.account_id) > 1
ORDER  BY distinct_accounts DESC
LIMIT  20;

-- Claim 2: meter_serial + manufacturer_code is unique.
-- Expected result on the shipped sample: 14 groups -- the manufacturer serial
-- reissue described in Technical Content section 7. These are NOT duplicates
-- of the same physical meter; they are distinct devices needing the composite
-- alternate key rather than serial alone.
SELECT 'C2: duplicate serial+manufacturer' AS claim,
       meter_serial,
       manufacturer_code,
       count(*) AS device_count
FROM   raw.meter_register
GROUP  BY meter_serial, manufacturer_code
HAVING count(*) > 1
ORDER  BY device_count DESC;

-- Claim 3: a meter may exist without a service point (procured stock).
-- We EXPECT rows here. If this returns zero, our nullable FK is unjustified
-- and a reviewer will rightly ask why the column is nullable.
SELECT 'C3: uninstalled meters (expected non-zero)' AS claim,
       count(*) AS uninstalled_meters
FROM   raw.meter_register
WHERE  service_point_id IS NULL;

-- Claim 4: shares for a meter in a period sum to exactly 100.00.
-- This is the relationship-attribute rule. Any row returned is unallocated
-- revenue, which is why share_pct cannot live on a parent table.
SELECT 'C4: meter shares not summing to 100' AS claim,
       meter_id,
       valid_from,
       sum(share_pct) AS total_pct
FROM   raw.account_meter_share_extract
GROUP  BY meter_id, valid_from
HAVING sum(share_pct) <> 100.00
ORDER  BY abs(sum(share_pct) - 100.00) DESC
LIMIT  20;
```

## Hands-on Lab 3 — Build the Baseerah Logical ERD

| | |
|---|---|
| **Objective** | Convert the 14-entity conceptual model into a complete logical ERD with attributes, domains, keys, cardinality and optionality; resolve two many-to-many relationships; and verify every cardinality claim against the landed data before it becomes a constraint |
| **Duration** | 50 minutes |
| **Setup** | PostgreSQL 16 with `raw` schema loaded (`make load-raw`, ~90 s), dbdiagram.io or `dbml-renderer`, course repo, `git checkout lab3-start` |

**Instructions & tasks**

1. *(8 min)* Extend `models/logical/baseerah_logical.dbml` from 6 pre-filled entities to all 14. Give every attribute a domain note. Mark derived attributes explicitly.
2. *(10 min)* Read each of the 19 relationships aloud in both directions with your pair and record cardinality + optionality. Where the sentence sounds wrong, fix the model, not the sentence. Log any change in `LAB3_DECISIONS.md`.
3. *(10 min)* Resolve the two many-to-many relationships (`customer_account` ↔ `meter`, `work_order` ↔ `technician`) with associative entities. Each must carry at least one relationship attribute and a composite primary key.
4. *(10 min)* Apply the key rule to all 14 entities: surrogate PK plus a UNIQUE alternate key wherever a natural key exists. Fix the three planted key defects in the starter (serial-as-PK, `NOT NULL` on `meter.service_point_id`, `share_pct` on the parent).
5. *(8 min)* Run `psql -f sql/validation/030_verify_cardinality.sql`. Reconcile every result: C2 must return 14 groups, C3 must return a non-zero count, C1 and C4 must return only rows you can explain. Record the reconciliation in `LAB3_DECISIONS.md`.
6. *(4 min)* Commit: `feat(model): baseerah logical ERD v1.0 with keys, cardinality and M:N resolution`.

**Expected output**
```
$ dbml-renderer -i models/logical/baseerah_logical.dbml -o docs/logical.svg
Rendered 16 entities (14 conceptual + 2 associative), 19 relationships

$ psql -f sql/validation/030_verify_cardinality.sql
 claim                                      | ...
--------------------------------------------+-----
 C1: service_point served by >1 account     | 62 rows   -- mixed-use buildings
 C2: duplicate serial+manufacturer          | 14 rows   -- manufacturer reissue
 C3: uninstalled meters (expected non-zero) | 1,842
 C4: meter shares not summing to 100        | 9 rows    -- data defect -> M6
(4 claims verified)
```

**Acceptance criteria**
- 16 entities rendered (14 + 2 associative); every relationship carries an explicit cardinality and optionality.
- Both associative entities carry ≥ 1 relationship attribute and a composite PK.
- All 14 entities use a surrogate PK; every entity with a natural key has a UNIQUE alternate key; the three planted defects are fixed.
- `LAB3_DECISIONS.md` explains all four cardinality-verification results, including why C3 returning 1,842 *validates* the nullable FK.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| C1 returns 0 rows | Mixed-use extract not loaded | Re-run `make load-raw`; the 62 shared service points are the M:N evidence |
| C2 returns 0 rows | Grouped on `meter_serial` alone, not the composite | Group on `(meter_serial, manufacturer_code)` — the composite is the point |
| Renderer rejects composite PK | DBML needs an `indexes { ... [pk] }` block, not `[pk]` per column | Use the `indexes` block as shown in the example |
| C4 returns 400+ rows | Joined shares to all meters rather than shared meters | Restrict to meters present in the share extract |

**Instructor notes.** Task 2 is the module. Stand at the back and listen for pairs reading relationships aloud; the ones who skip it will produce a diagram that looks right and encodes at least two wrong cardinalities. When a pair says "one meter belongs to one service point" without the "zero or", interrupt and ask where the 1,842 uninstalled meters go. In task 4, expect resistance to surrogate keys from participants with strong operational backgrounds — "but the serial *is* the meter". Use the reissue story; it converts people faster than theory. Fast finishers: model the self-referencing `network_asset` hierarchy (a main feeds sub-mains) and write the recursive CTE that returns all downstream assets of a given pump.

## Mini Exercises

**Quiz (5 questions)**
1. What makes an entity weak? → it cannot be identified without its parent; the parent key is part of its own key.
2. Why is `share_pct` a relationship attribute? → it describes the association between an account and a meter, not either parent alone.
3. State the key rule taught in this module. → surrogate primary key **plus** a UNIQUE constraint on the natural/business key.
4. Why must `meter.service_point_id` be nullable? → procured-but-not-yet-installed meters are real and must be representable in the asset register.
5. Which referential action fits `meter_reading.meter_id`? → **RESTRICT** — a meter with readings is retired by status, never deleted.

**Debugging exercise.** Check out `git checkout lab3-repeating-group`. `work_order` carries `technician_1_id`, `technician_2_id`, `technician_3_id`. Symptom: a four-technician emergency repair in Al-Ahsa cannot be recorded, and the "hours per technician" report requires a three-way UNION. Ask participants to diagnose (unresolved M:N as a repeating group), fix it with the associative entity, and then note that Module 4 will name this formally as a 1NF violation.

**Design exercise.** The authority introduces bulk meters at DMA inlets, which measure network input and belong to no customer. State what changes in the logical model: which relationship becomes optional, whether a new entity is needed, and how the NRW calculation reaches both bulk and customer meters through the model. (Expected: `meter.service_point_id` already nullable handles it; add `meter.dma_id` nullable for bulk meters; NRW joins input via `dma_id` and billed via `service_point → dma_id`.)

**Discussion questions.**
- Your DBA argues that surrogate keys "hide the business meaning" and make debugging harder. Where are they right, and what do you put in place to get their benefit without giving up the surrogate?
- A national ID is unique, stable, and non-null. Under PDPL, is that enough to make it a good primary key? Argue the data-minimisation case both ways.

## Case Study — The Unresolvable Join at "Jisr" (جسر)

**Scenario.** "Jisr" (جسر), a Saudi trade-finance integrator connecting 14 banks to a customs and logistics network, built a settlement warehouse to report on letter-of-credit lifecycles. Six months in, a routine reconciliation showed 4,180 shipments — 2.9% of the quarter — appearing in the shipment fact table but reachable from no letter of credit, and SAR 61 million of financed value therefore unattributed.

**Business context.** Every financed shipment must be traceable to its instrument for both regulatory reporting to SAMA and the banks' own exposure calculations. Unattributed value is not a reporting inconvenience; it is a control failure that must be declared.

**Technical challenge.** The relationship between a letter of credit and a shipment is genuinely many-to-many: one instrument may finance several partial shipments, and one consolidated shipment may draw on several instruments. The original model represented it as 1:M with `shipment.lc_id`, and the loader wrote whichever instrument arrived first. When a consolidated shipment referenced a second instrument, there was nowhere to put it, so the loader dropped the link — silently, because the FK was nullable.

**Constraints.** The 14 banks submit in three different message formats and cannot be asked to change. Historic data must be re-attributed, not discarded, because the regulatory submissions for two quarters were built on it. Instrument and shipment records contain commercially sensitive counterparty data, so the re-attribution cannot be outsourced. The fix must be delivered before the next quarterly submission, six weeks away.

**Solution approach (facilitate, don't lecture).** Steer towards: (1) resolve the M:N with an associative entity `lc_shipment_allocation(lc_id, shipment_id, allocated_value_sar, allocated_on)` — and note immediately that `allocated_value_sar` is the relationship attribute that makes partial draws representable at all; (2) add a constraint that allocations for a shipment sum to its financed value, turning silent loss into a loud failure; (3) backfill from the raw message archive, which retained all links even though the model could not; (4) restate the two quarters with a published reconciliation. Resist the room's first instinct to add `lc_id_2` and `lc_id_3` — ask how many columns are enough, and let them discover that the answer is "unknowable", which is exactly why repeating groups are forbidden.

**Discussion questions.**
1. The foreign key was nullable and the loader wrote nulls. What control would have made this loud on day one rather than silent for six months?
2. Why is `allocated_value_sar` impossible to store on either parent table?
3. Jisr's team proposes keeping the 1:M model and adding a separate "exceptions" table for multi-instrument shipments. What does that cost over three years?
4. How do you re-attribute two quarters of regulatory submissions in a way that a supervisor treats as a correction rather than a restatement of trust?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Entities in logical model | Coverage | 16 (14 conceptual + 2 associative) | DBML render count |
| Relationships specified | Completeness | 19/19 with cardinality *and* optionality | ERD review |
| M:N resolved | Correctness | 2/2 with ≥ 1 relationship attribute each | schema inspection |
| Alternate keys declared | Correctness | 100% of entities with a natural key | UNIQUE constraint count |
| Cardinality claims verified | Validation | 4/4 reconciled against `raw` | `030_verify_cardinality.sql` |

**Example benchmark table (filled during lab):**

| Claim | Query result | Interpretation | Action |
|---|---|---|---|
| C1: service points with > 1 account | 62 | Mixed-use buildings — genuine M:N | Model `account_meter_share` |
| C2: duplicate serial + manufacturer | 14 | Manufacturer serial reissue | Composite alternate key, surrogate PK |
| C3: uninstalled meters | 1,842 | Procured stock is real | Keep FK nullable — justified |
| C4: shares not summing to 100 | 9 | Data defect, not a model defect | Raise to Module 6 remediation backlog |

## Required Visuals and Training Assets

### Diagrams
1. **Crow's-foot cheat card for Baseerah** — *Purpose:* fluency in reading notation. *Elements:* the four cardinality/optionality symbol pairs, each illustrated with a real Baseerah relationship and its spoken sentence in English and Arabic. *Style:* reference card, printed A5, one per participant. *Designer description:* "A two-column card: symbol on the left, the sentence it means on the right, four rows."
2. **M:N resolution, before and after** — *Purpose:* the module's core mechanic. *Elements:* left panel shows `work_order` with three technician columns crossed out in red; right panel shows the associative entity with `role` and `hours_logged` highlighted as the requirement that only this shape can hold. *Style:* before/after split.
3. **Key decision tree** — *Purpose:* make key choice a procedure, not a preference. *Elements:* decision nodes (Is there a natural key? Is it stable? Is it non-sensitive? Is it narrow?) terminating in surrogate/natural/composite recommendations, with the PDPL branch called out. *Style:* flowchart with the PDPL node in a distinct colour.
4. **Baseerah logical ERD (reference poster)** — *Purpose:* the artefact every subsequent module points at. *Elements:* all 16 entities, 19 relationships, keys shown, associative entities shaded. *Style:* A1 wall poster, crow's-foot, English identifiers with Arabic entity subtitles.

### Images (screenshots)
1. **The rendered logical ERD** — *why:* the completion target for Lab 3; *content:* full diagram at readable zoom with the two associative entities shaded.
2. **`030_verify_cardinality.sql` output** — *why:* proves cardinality is testable, not decorative; *content:* the four claim results with the 62/14/1,842/9 figures.
3. **A repeating-group table in the wild** — *why:* participants must recognise the anti-pattern instantly; *content:* the `technician_1_id … technician_3_id` schema from the debugging branch.

### Simulations
1. **The reissued serial** — *Setup:* branch `sim-serial-reissue` loads 1,180 meters whose serials collide with existing rows under a serial-as-PK model. *Expected behaviour:* the load aborts on a unique violation; the provided "hotfix" appends `-B` and the subsequent technician-lookup query returns nothing for the printed serial. *Learning objective:* a natural PK makes humans distort business data to satisfy the database.
2. **The vanishing link** — *Setup:* branch `sim-nullable-fk` reproduces the Jisr defect on Baseerah's shared meters: a nullable `account_id` on the share table with a loader that writes the first match only. *Expected behaviour:* 9.4% of shared-meter volume becomes unattributed and the district revenue reconciliation is short by SAR 1.34M. *Learning objective:* nullable foreign keys turn model gaps into silent data loss.

### Interactive Activities
- **Read it aloud (12 min):** each pair receives three Baseerah relationships written only as symbols and must produce the four spoken sentences; the room votes on whether each is true of a water utility.
- **Key court (10 min):** one participant argues for `national_id` as the primary key of `customer_account`, another argues against on PDPL and stability grounds; the room rules and records the ratio.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `raw.service_point_extract` | Synthetic billing extract, Riyadh North | Postgres table | 64,800 rows (62 shared) | Cardinality claim C1 |
| `raw.meter_register` | Synthetic asset register with a planted serial reissue | Postgres table | 64,800 rows (1,842 uninstalled, 14 reissue pairs) | Claims C2 and C3 |
| `raw.account_meter_share_extract` | Synthetic mixed-use share extract | Postgres table | 138 rows (9 defective) | Claim C4; becomes the M7 bridge |
| `models/logical/baseerah_logical.dbml` | Lab 3 starter (6 entities pre-filled, 3 defects planted) | DBML | 16 entities at completion | The logical model artefact |

### Demo Requirements
- **Instructor demo (6 min):** run `sim-serial-reissue` live. Show the unique violation, apply the `-B` hotfix, then run the technician's lookup query for the serial as printed on the physical meter and get zero rows. Close with: "the database is now correct and the field is now wrong. That is what a natural primary key costs."

---

# Module 4 — Normalisation, Design Quality, and the Denormalisation Trade-off
## التطبيع وتحسين جودة التصميم

## Module Overview

**Purpose.** Normalisation is the only formal quality theory relational modelling has. This module teaches it as a decision procedure — functional dependencies in, anomaly-free tables out — through 1NF, 2NF, 3NF and BCNF on a real Baseerah table, and then teaches its deliberate reversal, because the warehouse participants build on Day 4 is *intentionally* denormalised. It covers catalogue Module 4 in full, including the explicit requirement to balance normalisation against reporting and analytics needs.

**Business relevance.** Update anomalies are not academic. When a tariff rate is stored redundantly on every invoice line, a rate correction touches millions of rows and will be applied incompletely — and the resulting revenue restatement is the kind of finding that ends careers in a regulated utility. Conversely, an operational team that normalises a reporting mart into eleven joins produces a dashboard nobody uses. Knowing which side of the line a table sits on is the practitioner skill.

**Industry use cases.**
- A billing system must guarantee that a tariff rate change is applied exactly once, everywhere — a 3NF requirement.
- A retail chain must eliminate the partial dependency that lets the same product carry two different category names in two branches.
- A reporting mart must serve a 40-column executive grid in under two seconds, which no fully normalised design will do — a controlled denormalisation.

**Expected competencies.** After this module a participant can derive functional dependencies from business rules; decompose a relation losslessly through 1NF → 2NF → 3NF → BCNF; name the specific anomaly each normal form removes; recognise the BCNF-but-3NF case; and write a denormalisation decision record that states what redundancy is introduced, what protects it, and what it buys.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Derive functional dependencies from business rules and data | LO4, LO2 |
| 4.2 | Identify insert, update, and delete anomalies in an unnormalised relation | LO4 |
| 4.3 | Decompose losslessly through 1NF, 2NF, 3NF and BCNF | LO4 |
| 4.4 | Distinguish 3NF from BCNF and handle the overlapping-candidate-key case | LO4 |
| 4.5 | Justify a deliberate denormalisation with a written decision record | LO4, LO7 |

## Technical Content

### 1. Functional dependencies, the raw material

`X → Y` means: for any two rows agreeing on `X`, they must agree on `Y`. Dependencies come from **business rules, not from sample data** — a dependency that happens to hold in today's extract but is not required by the business is a coincidence, and normalising on a coincidence produces a model that breaks next quarter.

From Baseerah's rule register:
- `meter_id, read_ts → volume_m3, read_channel, is_estimated` (a reading is identified by device and instant)
- `account_no → customer_category, tariff_id, account_status` (account attributes depend on the account)
- `tariff_id, block_no → rate_sar_per_m3, block_upper_m3` (a rate depends on the tariff and the block)
- `service_point_id → dma_id, city, property_type`
- `technician_id → depot_code` (a technician is based at exactly one depot)

A **candidate key** is a minimal attribute set that functionally determines every other attribute. **Prime attributes** belong to some candidate key; everything else is non-prime. Those two definitions carry all four normal forms.

### 2. The four forms and the anomaly each removes

Work `raw.billing_extract` — the flat file the billing system actually delivers, one row per invoice line:

```
account_no, holder_name, customer_category, tariff_code, tariff_name,
block_no, block_upper_m3, rate_sar_per_m3, invoice_no, invoice_date,
meter_serials, consumed_m3, line_amount_sar, district_code, district_officer
```

| Form | Rule | Violation here | Anomaly removed |
|---|---|---|---|
| **1NF** | Atomic values; no repeating groups | `meter_serials` holds `"M-4471;M-4472"` for shared meters | Cannot query, join, or constrain a multi-valued cell; counts are unreliable |
| **2NF** | 1NF + no partial dependency on part of a composite key | Key is `(invoice_no, block_no)`; `holder_name` depends on `account_no` alone | **Update anomaly:** a holder name change must be applied to every line of every invoice, and will not be |
| **3NF** | 2NF + no transitive dependency of non-prime on non-prime | `tariff_code → tariff_name` and `tariff_code` is non-prime | **Insert anomaly:** a new tariff cannot exist until someone is invoiced on it. **Delete anomaly:** removing the last invoice erases the tariff definition |
| **BCNF** | Every determinant is a superkey | See section 3 | Residual redundancy in relations with overlapping candidate keys |

Decomposition must be **lossless** (the natural join of the parts reconstructs the whole exactly) and should be **dependency-preserving** (every FD is enforceable within one resulting table without a join). 3NF always allows both. BCNF guarantees losslessness but may sacrifice dependency preservation — which is exactly why BCNF is a judgement call and 3NF is the default.

### 3. The BCNF case that is already in 3NF

This is the part participants have usually met only as an abstraction, so ground it in Baseerah. Consider the district tariff-officer assignment:

```
district_tariff_officer(district_code, tariff_code, officer_id)
```

Business rules: within a district, each tariff category has exactly one responsible officer; and every officer serves exactly one district.

FDs: `{district_code, tariff_code} → officer_id` and `officer_id → district_code`.

Candidate keys: `{district_code, tariff_code}` and `{officer_id, tariff_code}`. They **overlap** on `tariff_code`. Every attribute is prime, so there is no transitive dependency of a non-prime attribute — the relation **is in 3NF**. But `officer_id` is a determinant and is not a superkey, so it **violates BCNF**, and the residual redundancy is real: the fact "officer 4471 works in district RYD-N" is repeated once per tariff category, and an officer transferring districts requires a multi-row update that can be applied inconsistently.

BCNF decomposition: `officer_district(officer_id PK, district_code)` and `district_tariff_officer(officer_id, tariff_code, PK(officer_id, tariff_code))`. Lossless, but the FD `{district_code, tariff_code} → officer_id` now spans both tables and can only be enforced with a join — dependency preservation is lost. Baseerah's decision, recorded in the model, is to take the BCNF decomposition and enforce the lost dependency with a deferred constraint trigger, because officer transfers happen monthly and inconsistent transfers had already caused two mis-routed escalations.

### 4. Denormalisation, deliberately

Normalisation optimises for **write correctness**. Analytical workloads optimise for **read simplicity and speed**. A star schema is a denormalised design — a dimension table is typically in 2NF at best — and that is not a compromise, it is the correct answer for its workload.

| | Normalised (`core`) | Denormalised (`mart`) |
|---|---|---|
| Optimises | Write correctness, storage, integrity | Read speed, query simplicity |
| Redundancy | Eliminated | Deliberate and controlled |
| Update cost | One row | Many rows — hence rebuilt, not updated |
| Joins for a typical report | 7–11 | 1–2 |
| Who writes it | Applications and ELT | ELT only, never a user |
| Protection against drift | Constraints | Rebuild-from-source + reconciliation tests |

The discriminator is **who writes**. Redundancy is dangerous when many writers can update copies independently. In a mart, only the ELT pipeline writes, it rebuilds from the normalised core, and a reconciliation test proves the copies agree. That is a controlled redundancy, and it is why Baseerah's `dim_customer` cheerfully repeats `city`, `district_name`, and `tariff_name` that `core` stores once.

A denormalisation without those three protections — single writer, rebuild from a normalised source, reconciliation test — is not denormalisation. It is just redundancy.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Normalise to 3NF by default; go to BCNF when the residual redundancy causes real inconsistency.* Do not chase 5NF in a utility warehouse.
- *Derive FDs from rules, never from a data sample.*
- *Denormalise only downstream of a normalised source of truth.* Never as the source itself.
- *Every denormalisation gets a written decision record* naming the redundancy, the protection, and the measured benefit.
- *A repeating group is a modelling failure, not a formatting choice* — `"M-4471;M-4472"` is the same defect as `technician_1_id, technician_2_id`.

**Common mistakes (each appears in the Lab 4 starter deliberately)**
1. Splitting on a coincidence: the sample shows `city → tariff_code` because Riyadh North happens to be all-residential; the rule says otherwise.
2. A lossy decomposition that cannot be rejoined, discovered only when a reconciliation count differs by 1.7%.
3. Stopping at 2NF and declaring victory, leaving `tariff_code → tariff_name` transitively dependent.
4. Normalising the *mart* to 3NF, producing an eleven-join dashboard query at 14 seconds that the business abandons.
5. Denormalising the operational `core` "for performance" and then letting two applications write it.
6. Treating `meter_serials` as a display formatting problem and calling `string_to_array` in every downstream query.

**Production considerations**
- Test losslessness explicitly. After decomposition, `SELECT count(*) FROM (rejoined)` must equal the original count, and a full `EXCEPT` in both directions must return zero rows. Make it a CI test.
- Enforce FDs lost to BCNF decomposition with a constraint trigger or a scheduled reconciliation, and record which mechanism you chose and why.
- Measure the denormalisation benefit before and after. "It felt faster" is not a decision record; "1,240 ms → 210 ms on the executive grid, 5.9× " is.

### 6. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's predecessor stored `rate_sar_per_m3` directly on each invoice line — a textbook transitive dependency, defended for years as "denormalised for reporting speed". In 2025 the residential block-2 rate changed from SAR 4.00 to SAR 4.30. The correction script updated invoice lines by `tariff_code` and `block_no`, but 118,000 lines carried a legacy `tariff_code` spelling (`RES-B2` rather than `RES_B2`) inherited from a 2019 migration. Those lines kept the old rate. Nobody noticed for five months, because every individual invoice was internally consistent — `consumed_m3 × rate = line_amount` held on every row.

The discovery came from finance: recognised revenue was SAR 4.1 million below the tariff model's prediction for the period, a 0.9% gap that survived three explanations before someone queried distinct rates per block. Under a 3NF design there is exactly one row holding the block-2 rate; the update is one row and cannot be partially applied. The redundancy did not cause a bug — it removed the possibility of the database preventing one.

## Code Examples

### The full decomposition, executed and verified

```sql
-- sql/normalisation/040_decompose_billing_extract.sql
--
-- WHY: normalisation taught on a whiteboard is forgotten by Friday.
-- Executing the decomposition and then PROVING it lossless is what makes the
-- theory operational. Each step below names the anomaly it removes and the
-- rule from rules/baseerah_rules.yml that supplies the dependency.
--
-- Source: raw.billing_extract -- 486,300 invoice lines, Riyadh North, 12 months.

-- ---------------------------------------------------------------------------
-- 1NF: eliminate the repeating group in meter_serials ("M-4471;M-4472").
-- Anomaly removed: a multi-valued cell cannot be joined, counted, or
-- constrained. 2,140 of 486,300 lines carry more than one serial.
-- ---------------------------------------------------------------------------
CREATE TABLE stg.invoice_line_meter AS
SELECT b.invoice_no,
       b.block_no,
       trim(s.meter_serial) AS meter_serial
FROM   raw.billing_extract AS b
CROSS  JOIN LATERAL unnest(string_to_array(b.meter_serials, ';')) AS s(meter_serial)
WHERE  b.meter_serials IS NOT NULL;

-- ---------------------------------------------------------------------------
-- 2NF: key of the line is (invoice_no, block_no). Attributes depending on
-- account_no alone are PARTIALLY dependent and move out.
-- Anomaly removed: UPDATE -- a holder-name change touched every line of every
-- invoice for that account (avg 26.4 lines/account/year here).
-- ---------------------------------------------------------------------------
CREATE TABLE stg.account AS
SELECT DISTINCT
       b.account_no,
       b.holder_name,
       b.customer_category,
       b.tariff_code,
       b.district_code
FROM   raw.billing_extract AS b;

ALTER TABLE stg.account ADD PRIMARY KEY (account_no);

-- ---------------------------------------------------------------------------
-- 3NF: tariff_code -> tariff_name and (tariff_code, block_no) -> rate are
-- transitive dependencies through the non-prime attribute tariff_code.
-- Anomaly removed: INSERT (a new tariff needs an invoice to exist) and
-- DELETE (removing the last invoice erases the tariff definition).
-- This is the exact defect described in Technical Content section 6.
-- ---------------------------------------------------------------------------
CREATE TABLE stg.tariff AS
SELECT DISTINCT b.tariff_code, b.tariff_name
FROM   raw.billing_extract AS b;

ALTER TABLE stg.tariff ADD PRIMARY KEY (tariff_code);

CREATE TABLE stg.tariff_block AS
SELECT DISTINCT
       b.tariff_code,
       b.block_no,
       b.block_upper_m3,
       b.rate_sar_per_m3
FROM   raw.billing_extract AS b;

ALTER TABLE stg.tariff_block ADD PRIMARY KEY (tariff_code, block_no);
ALTER TABLE stg.tariff_block
      ADD FOREIGN KEY (tariff_code) REFERENCES stg.tariff (tariff_code);

-- The residue: the invoice line itself, now holding only what depends on
-- its own full key.
CREATE TABLE stg.invoice_line AS
SELECT b.invoice_no,
       b.block_no,
       b.account_no,
       b.invoice_date,
       b.consumed_m3,
       b.line_amount_sar
FROM   raw.billing_extract AS b;

ALTER TABLE stg.invoice_line ADD PRIMARY KEY (invoice_no, block_no);
ALTER TABLE stg.invoice_line
      ADD FOREIGN KEY (account_no) REFERENCES stg.account (account_no);

-- ---------------------------------------------------------------------------
-- LOSSLESSNESS PROOF. A decomposition that cannot be rejoined has destroyed
-- data, and the loss is usually invisible until a reconciliation months later.
-- Both queries below must return 0. This runs in CI.
-- ---------------------------------------------------------------------------
WITH rejoined AS (
    SELECT il.invoice_no, il.block_no, a.holder_name, a.customer_category,
           a.tariff_code, t.tariff_name, tb.block_upper_m3, tb.rate_sar_per_m3,
           il.invoice_date, il.consumed_m3, il.line_amount_sar, a.district_code
    FROM   stg.invoice_line AS il
    JOIN   stg.account      AS a  ON a.account_no  = il.account_no
    JOIN   stg.tariff       AS t  ON t.tariff_code = a.tariff_code
    JOIN   stg.tariff_block AS tb ON tb.tariff_code = a.tariff_code
                                 AND tb.block_no    = il.block_no
)
SELECT 'lost rows (original minus rejoined)' AS check_name, count(*) AS violations
FROM (
    SELECT invoice_no, block_no, holder_name, customer_category, tariff_code,
           tariff_name, block_upper_m3, rate_sar_per_m3, invoice_date,
           consumed_m3, line_amount_sar, district_code
    FROM   raw.billing_extract
    EXCEPT
    SELECT * FROM rejoined
) AS lost
UNION ALL
SELECT 'spurious rows (rejoined minus original)', count(*)
FROM (
    SELECT * FROM rejoined
    EXCEPT
    SELECT invoice_no, block_no, holder_name, customer_category, tariff_code,
           tariff_name, block_upper_m3, rate_sar_per_m3, invoice_date,
           consumed_m3, line_amount_sar, district_code
    FROM   raw.billing_extract
) AS spurious;

-- ---------------------------------------------------------------------------
-- Proof that 3NF makes the section-6 defect impossible: exactly one rate row
-- per (tariff, block). Under the flat design this returned 2 for RES block 2.
-- ---------------------------------------------------------------------------
SELECT tariff_code, block_no, count(DISTINCT rate_sar_per_m3) AS distinct_rates
FROM   stg.tariff_block
GROUP  BY tariff_code, block_no
HAVING count(DISTINCT rate_sar_per_m3) > 1;
```

### The denormalisation decision record, as a testable artefact

```yaml
# docs/decisions/DD-002-denormalise-dim-customer.yml
#
# WHY: "we denormalised for performance" is not a decision, it is an excuse.
# This record forces the three protections that separate a controlled
# denormalisation from plain redundancy: a single writer, a rebuild from a
# normalised source, and a reconciliation test. CI reads this file and fails
# if the named reconciliation test is absent or failing.

id: DD-002
title: Denormalise district, city and tariff attributes into mart.dim_customer
status: approved
decided_on: 2026-03-18
decided_by: data.architecture@baseerah.gov.sa
supersedes: none

context: >
  The executive KPI dashboard renders a 40-column customer grid filtered by
  district, city, customer category and tariff name. Against the normalised
  core schema this requires a 7-table join. Measured on the Riyadh North
  sample (58,100 customers): 1,240 ms p95, which misses the 2-second
  interactive budget once four dashboard tiles run concurrently.

decision: >
  mart.dim_customer carries district_code, district_name_en, district_name_ar,
  city, tariff_code and tariff_name as denormalised attributes, duplicated
  from core.district and core.tariff.

redundancy_introduced:
  - core.district.district_name_en duplicated across 58,100 dimension rows
  - core.tariff.tariff_name duplicated across 58,100 dimension rows

protections:
  single_writer: "dbt model mart/dim_customer.sql; no application or human writes"
  rebuild_from_normalised: "full rebuild from core on every daily run; the
                            dimension is never updated in place except by the
                            SCD2 snapshot logic in Module 7"
  reconciliation_test: "tests/reconcile_dim_customer_vs_core.sql -- asserts
                        zero rows where dim attributes disagree with core"

measured_benefit:
  before_p95_ms: 1240
  after_p95_ms: 210
  speedup: "5.9x"
  joins_before: 7
  joins_after: 1

rejected_alternatives:
  - option: "Materialised view over the normalised join"
    why_rejected: >
      Refresh locks the view for 40 s during the daily load, and the SCD2
      history requirement in Module 7 cannot be expressed as a view.
  - option: "Leave normalised and add indexes"
    why_rejected: >
      Tested: 1,240 ms -> 890 ms. Still misses the interactive budget, because
      the cost is join count, not scan cost.

reverts_if: >
  The reconciliation test fails twice in a rolling 30 days, indicating the
  rebuild guarantee is not holding.
```

## Hands-on Lab 4 — Normalise to BCNF, Then Decide What to Give Back

| | |
|---|---|
| **Objective** | Decompose `raw.billing_extract` (486,300 lines) through 1NF → 2NF → 3NF, handle one genuine BCNF case, prove losslessness, then write and defend a denormalisation decision record for the reporting layer |
| **Duration** | 50 minutes |
| **Setup** | PostgreSQL 16 with `raw` loaded, `psql`, course repo, `git checkout lab4-start` |

**Instructions & tasks**

1. *(8 min)* Derive the functional dependencies of `raw.billing_extract` **from `rules/baseerah_rules.yml`**, not from the data. Write them in `LAB4_FDS.md`. The starter contains one planted coincidental dependency (`city → tariff_code`) — reject it and say why.
2. *(10 min)* Execute the 1NF and 2NF steps. Record the row counts: 486,300 lines expand to 488,440 line-meter rows at 1NF, and `stg.account` lands at 58,100 rows.
3. *(10 min)* Execute the 3NF step for `tariff` and `tariff_block`. Then run the distinct-rate check and confirm it returns zero rows — the anomaly from the walkthrough is now structurally impossible.
4. *(8 min)* Handle the BCNF case in `raw.district_tariff_officer`: identify both candidate keys, show it is in 3NF, show it violates BCNF, decompose it, and state in `LAB4_BCNF.md` which functional dependency you have lost and how you will enforce it.
5. *(9 min)* Run the losslessness proof. Both counts must be 0. Then write `docs/decisions/DD-002-denormalise-dim-customer.yml` with your own measured before/after timings from `EXPLAIN ANALYZE`.
6. *(5 min)* Commit: `feat(model): decompose billing extract to BCNF + DD-002 denormalisation record`.

**Expected output**
```
$ psql -f sql/normalisation/040_decompose_billing_extract.sql
CREATE TABLE stg.invoice_line_meter   488,440 rows   (1NF: 2,140 lines expanded)
CREATE TABLE stg.account               58,100 rows   (2NF)
CREATE TABLE stg.tariff                     6 rows   (3NF)
CREATE TABLE stg.tariff_block              19 rows   (3NF)
CREATE TABLE stg.invoice_line         486,300 rows

           check_name                | violations
-------------------------------------+------------
 lost rows (original minus rejoined) |          0
 spurious rows (rejoined minus orig) |          0

 tariff_code | block_no | distinct_rates
-------------+----------+----------------
(0 rows)     -- the SAR 4.1M anomaly is now structurally impossible

$ psql -f sql/normalisation/041_bcnf_officer.sql
district_tariff_officer: candidate keys {district_code,tariff_code}, {officer_id,tariff_code}
  in 3NF: yes (all attributes prime)
  in BCNF: NO (officer_id -> district_code; officer_id is not a superkey)
  decomposed -> officer_district (74 rows), officer_tariff (183 rows)
  FD lost: {district_code,tariff_code} -> officer_id  [enforced by trigger]
```

**Acceptance criteria**
- `LAB4_FDS.md` lists ≥ 6 rule-derived FDs and explicitly rejects the planted coincidental one.
- All five decomposed tables exist with the row counts above; the distinct-rate check returns 0 rows.
- Both losslessness checks return 0; `LAB4_BCNF.md` names the lost FD and its enforcement mechanism.
- `DD-002` contains all three protections and real measured timings, not the example's.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Losslessness check returns non-zero "lost rows" | Joined `tariff_block` on `block_no` only | Join on `(tariff_code, block_no)` — the composite is the key |
| `stg.account` has 61,420 rows, not 58,100 | Selected `DISTINCT` over columns including a varying one | 2NF split must project only account-dependent attributes |
| 1NF table has 486,300 rows | `unnest` applied without `CROSS JOIN LATERAL` | Use the lateral form; 2,140 multi-serial lines must expand |
| BCNF step declares the relation "not in 3NF" | Non-prime attribute assumed without checking both candidate keys | Enumerate both candidate keys first; all attributes here are prime |

**Instructor notes.** Task 1 is where the module is won or lost. Participants who derive FDs by running `GROUP BY` over the sample will find `city → tariff_code` and normalise on it, producing a schema that breaks the moment a commercial connection appears in Riyadh North. Interrupt the room when you see the first `GROUP BY` and say it out loud. Task 4 will produce genuine confusion — that confusion is the lesson, because "in 3NF but not BCNF" is the case most people have only met abstractly. Have the two candidate keys written on the board before they start. Fast finishers: implement the deferred constraint trigger that enforces the lost FD and demonstrate it rejecting an inconsistent officer transfer.

## Mini Exercises

**Quiz (5 questions)**
1. Which anomaly does 3NF remove that 2NF does not? → insert/delete anomalies from transitive dependencies (a tariff that cannot exist without an invoice).
2. Where do functional dependencies come from? → business rules, not sample data.
3. What is lost in a BCNF decomposition that 3NF would have kept? → dependency preservation — an FD may span two tables.
4. Name the three protections that make a denormalisation controlled. → single writer; rebuild from a normalised source; reconciliation test.
5. True/False: a star-schema dimension should be normalised to 3NF. → **False** — that is a snowflake, and it costs read simplicity for no write benefit.

**Debugging exercise.** Check out `git checkout lab4-lossy-split`. `stg.tariff_block` has been keyed on `block_no` alone. Symptom: the rejoin produces 1,462,900 rows instead of 486,300 — a fan-out — and the invoice total for the district rises from SAR 41.2M to SAR 124.6M. Ask participants to diagnose the missing key attribute, then discuss why a lossy decomposition that *inflates* is easier to catch than one that *loses*, and what test catches both.

**Design exercise.** Baseerah adds seasonal tariffs: the same tariff code has different block rates in summer (Apr–Sep) and winter (Oct–Mar), and historic invoices must remain reproducible. State the new functional dependency, the change to `tariff_block`'s key, and whether the result is still in 3NF. Then state what happens to `DD-002` when the dashboard must show the *invoice-time* tariff name rather than today's.

**Discussion questions.**
- A senior developer argues that "3NF is a 1970s idea; we have cheap storage now". What is the actual counter-argument, and which of their claims is genuinely correct?
- Your mart's reconciliation test has failed twice this month and the team wants to relax it to a 0.1% tolerance. What does that concession actually buy, and what does it cost you the next time finance asks a question?

## Case Study — The Two Names for One Product at "Wafra" (وفرة)

**Scenario.** "Wafra" (وفرة), a Saudi grocery retail chain running 214 stores across Riyadh, Jeddah and Dammam, discovered that its category-performance report showed 3,180 SKUs contributing to two different categories simultaneously. Total category revenue exceeded total revenue by SAR 18.4 million for the quarter — a figure that is arithmetically impossible and had been published to the board twice.

**Business context.** Category performance drives shelf-space allocation, supplier negotiations, and the buying team's bonus. A category that appears larger than it is receives shelf space it did not earn, at the direct expense of one that did.

**Technical challenge.** The product master was a single flat table keyed on `(sku, store_id)` — a design chosen so each store could hold its own price. `category_name` and `category_manager` depend on `sku` alone, a partial dependency on part of a composite key: a textbook 2NF violation. When the category taxonomy was reorganised, the update script processed stores in batches and failed partway on 41 stores. Those stores kept the old category names. Every individual row remained internally consistent, so no constraint fired and no report errored.

**Constraints.** The chain cannot take the product master offline during trading hours. Two years of historic category reporting exists and the board has seen it. Supplier contracts reference category revenue thresholds, so a restatement has commercial consequences with third parties. Store-level pricing must be preserved — it is the reason the composite key was chosen in the first place, and it is a genuine requirement.

**Solution approach (facilitate, don't lecture).** Guide the room to the 2NF decomposition: `product(sku PK, category_code, category_manager, …)` and `product_store_price(sku, store_id, price_sar, PK(sku, store_id))`, with `category(category_code PK, category_name_en, category_name_ar)` completing 3NF. Then push on the two harder questions the case is really about. First: the historic restatement — the correct category *at the time* must be recoverable, which means the category assignment is time-varying and needs `valid_from`/`valid_to`, foreshadowing SCD2 in Module 7. Second: the supplier contracts — the room will want to restate silently; ask what a supplier's auditor would think of a silently changed threshold. Resist the shortcut of "just fix the 41 stores": it repairs today's number and leaves the design that will produce the same defect at the next reorganisation.

**Discussion questions.**
1. Why did no database constraint fire, and what constraint *would* have made the partial update impossible?
2. The composite key was chosen for a real requirement. Where exactly did the design go wrong, given that the requirement was valid?
3. What does "reproduce last year's category report" require of the model, and which module of this course supplies that mechanism?
4. Wafra's analytics team wants the reporting mart to keep `category_name` denormalised on every sales fact row. Under what three conditions is that correct, and are they met here?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Decomposition completeness | Correctness | 5 tables in 3NF + 2 in BCNF | schema inspection |
| Losslessness | Correctness | 0 lost rows, 0 spurious rows | `EXCEPT` proof in CI |
| Anomaly elimination | Quality | 0 tariff blocks with > 1 distinct rate | distinct-rate query |
| FD derivation discipline | Analysis | ≥ 6 rule-derived FDs; planted coincidence rejected | `LAB4_FDS.md` review |
| Denormalisation justification | Governance | DD-002 with 3 protections + measured timings | decision-record review |

**Example benchmark table (filled during lab):**

| Step | Table | Rows | Normal form | Anomaly removed | Rejoin check |
|---|---|---|---|---|---|
| source | `raw.billing_extract` | 486,300 | 0NF | — | — |
| 1NF | `stg.invoice_line_meter` | 488,440 | 1NF | multi-valued cell | pass |
| 2NF | `stg.account` | 58,100 | 2NF | update (holder name) | pass |
| 3NF | `stg.tariff` | 6 | 3NF | insert/delete (tariff) | pass |
| 3NF | `stg.tariff_block` | 19 | 3NF | update (rate change) | pass |
| BCNF | `officer_district` | 74 | BCNF | officer transfer inconsistency | pass (FD lost, trigger added) |

## Required Visuals and Training Assets

### Diagrams
1. **The four normal forms as an anomaly ladder** — *Purpose:* make each form memorable by its anomaly rather than its definition. *Elements:* four rungs, each labelled with the form, the violation in `raw.billing_extract`, and a red icon for the anomaly it removes. *Style:* vertical ladder, red anomaly chips falling away at each rung. *Designer description:* "A ladder climbed left to right; at each step a red defect card drops off and lands in a discard pile."
2. **The BCNF-but-3NF case** — *Purpose:* the module's hardest concept, made visual. *Elements:* `district_tariff_officer` with both candidate keys highlighted in two colours showing their overlap on `tariff_code`, the `officer_id → district_code` arrow marked as a non-superkey determinant, and the decomposition with the lost FD drawn as a dotted line spanning both tables. *Style:* annotated relation diagram with an explicit "lost dependency" callout.
3. **Normalised core → denormalised mart** — *Purpose:* show that both are correct for different jobs. *Elements:* left = 7-table join with a 1,240 ms badge; right = star schema with a 210 ms badge; between them the three protection gates (single writer, rebuild, reconcile). *Style:* two-panel with gate icons in the channel.
4. **Anatomy of an update anomaly** — *Purpose:* the SAR 4.1M story rendered. *Elements:* a rate-change script hitting rows, 118,000 rows with a legacy code spelling shown in amber and skipped, and the revenue gap chart underneath. *Style:* data-flow with a highlighted miss.

### Images (screenshots)
1. **Losslessness proof output** — *why:* the check must be seen returning zero; *content:* the two-row result grid with both counts at 0.
2. **`EXPLAIN ANALYZE` before and after DD-002** — *why:* denormalisation must be measured, not asserted; *content:* the two plans side by side with the 1,240 ms and 210 ms totals visible.
3. **The distinct-rate query returning zero rows** — *why:* proves an anomaly is now structurally impossible; *content:* the empty result set with the query text above it.

### Simulations
1. **The partial rate update** — *Setup:* branch `sim-rate-update` runs the 2025 block-2 rate change against a flat, unnormalised invoice table containing 118,000 legacy-spelling rows. *Expected behaviour:* every invoice remains internally consistent, no error is raised, and recognised revenue for the period is SAR 4.1M (0.9%) below the tariff model. *Learning objective:* redundancy removes the database's ability to prevent an error.
2. **The fan-out rejoin** — *Setup:* branch `lab4-lossy-split` keys `tariff_block` on `block_no` alone. *Expected behaviour:* the rejoin returns 1,462,900 rows and the district invoice total inflates from SAR 41.2M to SAR 124.6M. *Learning objective:* losslessness is a property to be tested, not assumed.

### Interactive Activities
- **Normalise on paper (15 min):** teams receive a printed 12-column extract of Baseerah work orders and normalise it to 3NF with scissors and cards, then defend their decomposition to another team.
- **Coincidence or rule? (10 min):** eight candidate functional dependencies observed in the sample data; teams classify each as a genuine business rule or a sampling coincidence, then check against the rule register.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `raw.billing_extract` | Synthetic flat billing export, Riyadh North, 12 months | Postgres table | 486,300 rows (2,140 multi-serial) | The decomposition subject |
| `raw.district_tariff_officer` | Synthetic officer assignment with overlapping candidate keys | Postgres table | 183 rows, 74 officers | The BCNF case |
| `sim-rate-update` fixture | Synthetic 2025 tariff change with 118,000 legacy-code rows | SQL script | 486,300 rows affected | The update-anomaly simulation |
| `docs/decisions/DD-002-*.yml` | Lab 4 starter (context filled, decision blank) | YAML | 1 record | The denormalisation artefact |

### Demo Requirements
- **Instructor demo (7 min):** run `sim-rate-update` live against the flat table. Show three invoices picked at random — all internally consistent. Show the revenue gap. Then run the same change against the 3NF `stg.tariff_block`: one row, one update, no possible partial application. Close with: "normalisation did not fix a bug here. It removed the shape of design in which that bug can exist."

---

# Module 5 — Physical Modelling, Data Types, Indexing, and Constraints
## النمذجة الفيزيائية وقواعد البيانات

## Module Overview

**Purpose.** This module lands the logical model on a real engine. Participants translate entities to tables, domains to data types, business rules to constraints, and access patterns to indexes and partitions — then measure the result on 13,018,800 meter readings. It covers catalogue Module 5 in full, including performance, scalability, and maintainability considerations, and it is where the abstract work of Days 1–2 becomes something that either runs in 46 milliseconds or does not.

**Business relevance.** Baseerah's field-operations layer must return a district supervisor's daily consumption view while they are standing at a service point on a tablet. Two seconds is usable; fourteen is not, and the supervisor reverts to phoning the control room. Physical design is where a data model either earns its adoption or loses it, and the difference is usually one index choice and one partitioning decision — both of which cost nothing at design time and are painful to retrofit at 13 million rows and impossible at 1.4 billion.

**Industry use cases.**
- A utility stores years of interval meter data whose queries are always time-ranged, making BRIN indexes 2,200× smaller than B-tree for the same pruning job.
- A ministry must guarantee that a status column can never hold an undocumented value, enforced by the database rather than by every application that writes to it.
- A national registry partitions by month so that a retention policy is a partition drop rather than a nine-hour `DELETE`.

**Expected competencies.** After this module a participant can generate physical DDL from a logical model with justified type choices; implement business rules as CHECK, UNIQUE, FK and exclusion constraints; choose between B-tree, BRIN, GIN and partial indexes from an access pattern; design a partitioning strategy that supports both pruning and retention; and read `EXPLAIN (ANALYZE, BUFFERS)` well enough to defend a design in review.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Translate a logical model into engine-specific DDL with justified data types | LO5, LO3 |
| 5.2 | Implement business rules as database constraints and state their enforcement cost | LO5, LO2 |
| 5.3 | Select index types from access patterns and measure the result | LO5 |
| 5.4 | Design a partitioning strategy supporting pruning, maintenance, and retention | LO5 |
| 5.5 | Read query plans and defend a physical design in review | LO5 |

## Technical Content

### 1. Types are a correctness decision before they are a performance one

| Logical domain | Wrong choice | Right choice | Why it matters at Baseerah |
|---|---|---|---|
| Money | `FLOAT` | `NUMERIC(12,2)` | Binary floating point cannot represent SAR 0.10 exactly; invoice totals drift by fractions of a halala across millions of lines and never reconcile with the ledger |
| Volume | `TEXT` | `NUMERIC(10,3)` | `TEXT` admits `'N/A'`, `'-'`, `'12,5'`; every aggregation then silently drops or errors |
| Timestamp | `TIMESTAMP` | `TIMESTAMPTZ` | SCADA emits UTC, billing emits `Asia/Riyadh`; without a zone the two are silently three hours apart and daily boundaries are wrong |
| Status | `VARCHAR(50)` free | `VARCHAR(16)` + `CHECK IN (...)` | The domain is the business rule; without the CHECK you get `ACTIVE`, `Active`, `ACTIVE ` and a `GROUP BY` that reports three statuses |
| Identifier | `UUID` | `BIGINT IDENTITY` | 16 bytes vs 8, random insert order destroys B-tree locality on a 13M-row fact table |
| Address | `TEXT` | `VARCHAR(12)` (National Address short code) + components | Free text cannot be validated, matched, or completeness-measured |

Two Baseerah-specific calls. `NUMERIC(10,3)` for `volume_m3` gives millilitre resolution up to 9,999,999.999 m³ — far beyond any meter — and is exact under summation, which matters because NRW is a difference of two large sums. And `read_ts TIMESTAMPTZ NOT NULL` is non-negotiable: the single most common defect in utility warehouses is a naive timestamp that puts three hours of consumption in the wrong day, which shifts the daily NRW figure by roughly 12%.

### 2. Constraints are executable business rules

Each rule type from Module 2 has a physical home. Write the rule ID into the constraint name so a violation in production names its owner:

- `NOT NULL` — mandatory participation (structural rules).
- `UNIQUE` — the alternate/natural key from Module 3. This is the constraint whose absence produces Module 6's 3,320 duplicates.
- `CHECK` — domains and value bounds (constraint rules). Cheap: evaluated per row on write, no lookup.
- `FOREIGN KEY` — referential integrity with the action chosen in Module 3. Costs an index lookup per write; requires an index on the referencing column.
- `EXCLUDE USING gist` — the constraint most modellers do not know they need. It enforces non-overlap: no service point may have two active accounts over overlapping periods. Expressing that with CHECK is impossible; with application code it is a race condition.

The cost of a constraint is paid on write and refunded on every read forever, because downstream code no longer needs defensive handling. The exception is bulk load: dropping and recreating indexes and validating constraints with `NOT VALID` then `VALIDATE CONSTRAINT` turns a 22-minute load into a 3 minute 48 second one, which is exactly the pattern Lab 5 measures.

### 3. Index selection from access patterns

Start from the queries, never from the columns.

| Baseerah access pattern | Index | Rationale |
|---|---|---|
| One meter, a date range ("show me meter M-4471 last week") | B-tree `(meter_id, read_ts)` | Equality then range — the classic composite leading-column rule |
| A whole district for one day (NRW daily balance) | BRIN `(read_ts)` | Data arrives in time order, so physical and logical order correlate; BRIN stores min/max per block range |
| Open work orders only (2.1% of rows) | Partial B-tree `(asset_id) WHERE closed_ts IS NULL` | Index only the rows anyone queries; 47× smaller |
| Search a holder name | GIN on `to_tsvector` / `pg_trgm` | Substring and fuzzy match, used by the Module 6 match/merge |
| Every FK column | B-tree on the referencing column | PostgreSQL does *not* create these automatically |

The BRIN-versus-B-tree result on Baseerah's readings is the number participants remember:

| Index | Size | Build time | 1-day district range scan |
|---|---|---|---|
| none (seq scan) | — | — | 2,140 ms |
| BRIN `(read_ts)` | 184 kB | 9 s | 118 ms |
| B-tree `(read_ts)` | 412 MB | 71 s | 96 ms |
| B-tree `(meter_id, read_ts)` | 486 MB | 84 s | 46 ms (single meter) |

BRIN gives 94.5% of the B-tree's range-scan benefit for 0.04% of the space, *provided* physical order correlates with time. That proviso is the whole lesson: BRIN on a randomly ordered table is worthless, which is why it pairs naturally with time-partitioned append-only data and never with a mutable dimension.

### 4. Partitioning: pruning, maintenance, retention

Declarative range partitioning by month on `read_ts` buys Baseerah three distinct things, and participants should be able to name all three:

1. **Pruning** — a one-day query touches 1 of 3 partitions in the sample (1 of 84 at national scale over seven years), before any index is consulted.
2. **Maintenance** — `VACUUM`, `ANALYZE`, and index rebuilds run per partition, so no single operation locks the whole 1.4-billion-row table.
3. **Retention** — PDPL data minimisation requires meter-level personal data to be aged out. `DROP TABLE meter_read_y2026m01` is instantaneous and reclaims space; `DELETE ... WHERE read_ts < ...` on the same volume takes hours, bloats the table, and requires a `VACUUM FULL` that takes an exclusive lock.

The costs are real and must be taught alongside: the partition key must appear in the `WHERE` clause or you scan everything; unique constraints must include the partition key; and over-partitioning (daily partitions over seven years = 2,555 tables) makes planning slower than the scan it saves. Monthly is the right grain here because retention policy and reporting cycles are both monthly.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Types encode domains; constraints encode rules; indexes encode access patterns.* Three different inputs, three different decisions.
- *Name every constraint after its rule ID* (`ck_meter_reading_volume_r014`) so a production violation is self-documenting.
- *Never index speculatively.* Every index is paid for on every write and in every backup.
- *Measure before and after with `EXPLAIN (ANALYZE, BUFFERS)`* — buffer counts, not wall-clock, are the comparable number on a shared laptop.
- *Partition for retention as much as for speed;* PDPL makes this a compliance control, not an optimisation.

**Common mistakes (each appears in the Lab 5 starter deliberately)**
1. `volume_m3` declared `DOUBLE PRECISION`, so the district total disagrees with the ledger by SAR 0.34 and no one can explain it.
2. `read_ts TIMESTAMP` without a zone, moving 8.4% of readings into the wrong day.
3. No index on the foreign key `meter_reading.meter_id`, so a meter retirement takes 41 seconds.
4. A B-tree on `read_ts` where BRIN would do, costing 412 MB for a 22 ms improvement.
5. Partition key absent from the query predicate, so every "optimised" query scans all partitions.
6. All constraints created before the bulk load, turning a 3 minute 48 second load into 22 minutes.

**Production considerations**
- Keep DDL in numbered, forward-only migration files in the repository. A physical model that lives only in the running database cannot be reviewed, rolled forward, or rebuilt.
- Set `fillfactor` below 100 only on tables with in-place updates; the append-only reading table should stay at 100.
- Schedule `ANALYZE` after every bulk load. A partitioned table with stale statistics will choose a sequential scan over your new index and you will blame the index.

### 6. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's first field-operations release put the district daily-consumption view behind a query that scanned the full reading table: 2,140 ms in the lab, 31 seconds against production volumes. Supervisors tried it for two weeks and went back to phoning the control room; adoption was 4%. The engineering response was to buy more memory. The actual fix was a BRIN index costing 184 kB and nine seconds to build, plus monthly partitioning — 31 seconds to 380 ms, and adoption reached 71% within a month. The lesson is not that indexes are good. It is that the physical model is a *product* decision: the same logical model, deployed two ways, is either used or abandoned, and no amount of correct modelling upstream survives a fourteen-second dashboard.

## Code Examples

### Physical DDL: types, constraints named after rules, partitioning

```sql
-- sql/ddl/050_core_meter_reading.sql
--
-- WHY: this is the logical model from Module 3 landed on PostgreSQL 16.
-- Three things are deliberate and worth reading closely:
--   1. every constraint is named after the rule it enforces (rules/baseerah_rules.yml),
--      so a production violation message names its owner;
--   2. the table is RANGE partitioned by month on read_ts, which serves pruning,
--      per-partition maintenance, AND the PDPL retention drop;
--   3. no indexes are created here -- they are created AFTER the bulk load in
--      052_indexes.sql, because building them first costs 18 extra minutes.

CREATE SCHEMA IF NOT EXISTS core;

CREATE TABLE core.meter_reading (
    reading_id    bigint        GENERATED ALWAYS AS IDENTITY,
    meter_id      bigint        NOT NULL,
    -- TIMESTAMPTZ, not TIMESTAMP: SCADA emits UTC and billing emits
    -- Asia/Riyadh. A naive type silently shifts 8.4% of readings by 3 hours
    -- and moves them into the wrong reporting day.
    read_ts       timestamptz   NOT NULL,
    read_channel  varchar(10)   NOT NULL,
    reading_type  varchar(8)    NOT NULL,
    -- NUMERIC, not DOUBLE PRECISION: NRW is a difference of two large sums,
    -- and binary float error accumulates into an unexplainable SAR variance.
    index_m3      numeric(12,3),
    volume_m3     numeric(10,3),
    is_estimated  boolean       NOT NULL DEFAULT false,
    ingested_at   timestamptz   NOT NULL DEFAULT now(),

    -- The partition key must be part of every unique constraint on a
    -- partitioned table. This is a PostgreSQL requirement, and it is also
    -- correct here: uniqueness is (device, instant).
    CONSTRAINT pk_meter_reading PRIMARY KEY (reading_id, read_ts),
    CONSTRAINT uq_meter_reading_meter_ts_r003 UNIQUE (meter_id, read_ts),

    CONSTRAINT ck_meter_reading_channel_r005 CHECK (
        read_channel IN ('AMI', 'MANUAL', 'ESTIMATED', 'BULK')),
    CONSTRAINT ck_meter_reading_type_r002 CHECK (
        reading_type IN ('index', 'delta')),
    -- R-014 scoped correctly: the 0..200 residential bound is applied in the
    -- quality layer where customer_category is available. Here we enforce only
    -- the physically universal rule: a delta volume is never negative, and an
    -- index reading is never negative.
    CONSTRAINT ck_meter_reading_nonneg_r013 CHECK (
        (reading_type = 'delta' AND volume_m3 >= 0)
     OR (reading_type = 'index' AND index_m3 >= 0)),
    -- A row must carry the value its type promises.
    CONSTRAINT ck_meter_reading_value_present_r002 CHECK (
        (reading_type = 'index' AND index_m3 IS NOT NULL)
     OR (reading_type = 'delta' AND volume_m3 IS NOT NULL))
) PARTITION BY RANGE (read_ts);

-- Monthly partitions. Monthly (not daily) because the retention policy and
-- the reporting cycle are both monthly; daily would give 2,555 partitions
-- over a 7-year retention window and make planning slower than the scan.
CREATE TABLE core.meter_reading_y2026m04 PARTITION OF core.meter_reading
    FOR VALUES FROM ('2026-04-01 00:00:00+03') TO ('2026-05-01 00:00:00+03');
CREATE TABLE core.meter_reading_y2026m05 PARTITION OF core.meter_reading
    FOR VALUES FROM ('2026-05-01 00:00:00+03') TO ('2026-06-01 00:00:00+03');
CREATE TABLE core.meter_reading_y2026m06 PARTITION OF core.meter_reading
    FOR VALUES FROM ('2026-06-01 00:00:00+03') TO ('2026-07-01 00:00:00+03');

-- Foreign key added NOT VALID so the bulk load is not slowed by per-row
-- checking, then validated once. VALIDATE takes only a SHARE UPDATE EXCLUSIVE
-- lock, so it does not block reads or writes.
ALTER TABLE core.meter_reading
    ADD CONSTRAINT fk_meter_reading_meter_r003
    FOREIGN KEY (meter_id) REFERENCES core.meter (meter_id)
    ON DELETE RESTRICT NOT VALID;

COMMENT ON TABLE core.meter_reading IS
  'Grain: one meter, one instant, one channel. PDPL: PERSONAL DATA -- hourly '
  'consumption reveals occupancy. Retention 25 months at meter grain (partition '
  'drop); aggregated beyond. Rules R-002, R-003, R-005, R-013, R-014.';

-- The non-overlap constraint that CHECK cannot express: no service point may
-- have two accounts with overlapping validity periods. Without this the
-- billing system can double-bill a property and only a report will notice.
CREATE EXTENSION IF NOT EXISTS btree_gist;

ALTER TABLE core.service_point_account
    ADD CONSTRAINT ex_service_point_no_overlap_r008
    EXCLUDE USING gist (
        service_point_id WITH =,
        daterange(valid_from, valid_to, '[)') WITH &&
    );
```

### Index strategy, built after load, and benchmarked

```sql
-- sql/ddl/052_indexes.sql
--
-- WHY: indexes are created AFTER the COPY, not before. Building them first
-- makes the 13,018,800-row load take 22 minutes instead of 3 min 48 s, because
-- every insert maintains every index. Created afterwards, the three indexes
-- below cost 164 seconds in total and the load stays fast.
--
-- Each index below exists because of a NAMED access pattern. There are no
-- speculative indexes: every one is paid for on every write and in every backup.

-- Pattern A: "show me meter M-4471 last week" (field-ops tablet, p95 < 500 ms).
-- Equality on meter_id then range on read_ts -> equality column leads.
-- 486 MB, 84 s build, 46 ms for a single meter over 7 days.
CREATE INDEX ix_meter_reading_meter_ts
    ON core.meter_reading USING btree (meter_id, read_ts);

-- Pattern B: "the whole district for one day" (NRW daily balance).
-- Readings are appended in time order, so physical and logical order
-- correlate: BRIN stores min/max per 128-page range and prunes almost as well
-- as a B-tree for 0.04% of the size. 184 kB, 9 s build, 118 ms vs 2,140 ms seq.
-- pages_per_range lowered from the 128 default to 32 because our monthly
-- partitions are small enough that finer granularity is nearly free.
CREATE INDEX ix_meter_reading_ts_brin
    ON core.meter_reading USING brin (read_ts) WITH (pages_per_range = 32);

-- Pattern C: open work orders only -- 3,880 of 184,600 rows (2.1%).
-- A partial index is 47x smaller than the full index and is the only one the
-- dispatcher's screen ever needs.
CREATE INDEX ix_work_order_open_asset
    ON core.work_order USING btree (asset_id, raised_ts)
    WHERE closed_ts IS NULL;

-- Pattern D: fuzzy holder-name search, used by the Module 6 match/merge and by
-- the call centre. Trigram GIN handles substring and misspelling alike.
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX ix_customer_account_holder_trgm
    ON core.customer_account USING gin (holder_name gin_trgm_ops);

-- Every foreign key referencing column needs its own index: PostgreSQL indexes
-- the referenced PK automatically but NOT the referencing column, so a parent
-- delete degrades to a sequential scan of the child (41 s on this table).
CREATE INDEX ix_meter_service_point ON core.meter (service_point_id);
CREATE INDEX ix_service_point_dma   ON core.service_point (dma_id);
CREATE INDEX ix_work_order_asset    ON core.work_order (asset_id);

-- Statistics must be refreshed after a bulk load or the planner will ignore
-- the indexes we just built and you will blame the indexes.
ANALYZE core.meter_reading;
ANALYZE core.work_order;

-- Benchmark harness: run each pattern with BUFFERS so results are comparable
-- across laptops of different speeds. Buffer counts, not milliseconds, are
-- the number to record in BENCHMARKS.md.
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT sum(volume_m3) AS district_m3
FROM   core.meter_reading AS mr
JOIN   core.meter         AS m  ON m.meter_id = mr.meter_id
JOIN   core.service_point AS sp ON sp.service_point_id = m.service_point_id
WHERE  mr.read_ts >= '2026-06-14 00:00:00+03'
  AND  mr.read_ts <  '2026-06-15 00:00:00+03'   -- partition key IN the predicate
  AND  mr.reading_type = 'delta'
  AND  sp.dma_id = 41;
```

## Hands-on Lab 5 — Deploy and Benchmark the `core` Schema

| | |
|---|---|
| **Objective** | Generate physical DDL for all 16 entities, fix six planted physical defects, bulk-load 13,018,800 readings, then build and benchmark the index and partitioning strategy against four named access patterns |
| **Duration** | 50 minutes |
| **Setup** | PostgreSQL 16 (Docker, 4 GB RAM allocated), `raw` schema loaded, course repo, `git checkout lab5-start`. The `COPY` files are pre-generated: `data/core_meter_reading.csv` is 1.06 GB |

**Instructions & tasks**

1. *(8 min)* Review `sql/ddl/050_core_meter_reading.sql` in the starter and find the six planted defects (float money, naive timestamp, missing FK index, over-wide B-tree, missing partition predicate in the benchmark query, constraints created before load). Record each in `LAB5_DEFECTS.md` with the symptom you predict.
2. *(8 min)* Fix the type and constraint defects and deploy the schema: `make deploy-core`. Confirm 16 tables and 3 monthly partitions exist and that every constraint name carries its rule ID.
3. *(10 min)* Bulk-load with `make load-core`. Time it. You should see 3 min 48 s ± 25 s with no indexes present; if you see 22 minutes you created indexes first — that *is* defect #6.
4. *(10 min)* Build the four indexes from `052_indexes.sql` and record size and build time for each with `\di+` and `pg_relation_size`. BRIN must land at 184 kB and the composite B-tree at 486 MB.
5. *(10 min)* Run the four benchmark queries with `EXPLAIN (ANALYZE, BUFFERS)`. Record buffers and milliseconds in `BENCHMARKS.md`. Then re-run the district query with the `read_ts` predicate removed and record how many partitions are scanned — this is defect #5 made visible.
6. *(4 min)* Commit: `feat(core): physical schema with partitioning, constraints and measured index strategy`.

**Expected output**
```
$ make load-core
COPY core.meter_reading FROM 'data/core_meter_reading.csv'
13018800 rows copied in 228.4 s  (3 min 48 s, 57,000 rows/s)
ALTER TABLE ... VALIDATE CONSTRAINT fk_meter_reading_meter_r003   14.2 s

$ psql -c '\di+ core.*'
 ix_meter_reading_meter_ts       | btree | 486 MB  | build  84 s
 ix_meter_reading_ts_brin        | brin  | 184 kB  | build   9 s
 ix_work_order_open_asset        | btree | 216 kB  | build   0.3 s
 ix_customer_account_holder_trgm | gin   |  11 MB  | build   6 s

$ psql -f sql/bench/run_patterns.sql
 pattern                                  | plan                        | buffers | ms
------------------------------------------+-----------------------------+---------+------
 A single meter, 7 days                   | Index Scan (meter_id,ts)    |     142 |   46
 B district, 1 day  (BRIN)                | Bitmap Heap Scan on BRIN    |  18,430 |  118
 B district, 1 day  (no index, seq)       | Parallel Seq Scan           | 421,600 | 2140
 C open work orders                       | Index Scan (partial)        |      61 |    3
 D holder name ILIKE '%Al-Hars%'          | Bitmap Heap Scan on GIN     |     380 |   22

$ psql -f sql/bench/no_partition_predicate.sql
 Partitions scanned: 3 of 3   (with predicate: 1 of 3)   ms: 341 -> 118
```

**Acceptance criteria**
- All 16 `core` tables deployed; `meter_reading` partitioned monthly with 3 partitions; every constraint name contains its rule ID.
- Load completes in under 5 minutes with 13,018,800 rows and zero constraint violations.
- BRIN index ≤ 200 kB and the district query improves from ~2,140 ms to ~118 ms.
- `BENCHMARKS.md` records buffers and milliseconds for all four patterns plus the partition-pruning comparison.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Load takes 22 minutes | Indexes or a validated FK created before `COPY` | Drop indexes, load, rebuild; add FK as `NOT VALID` then `VALIDATE` |
| `no partition of relation found for row` | A reading falls outside the three monthly partitions | Add the missing partition; never use a DEFAULT partition for time-series |
| BRIN index used but scan is still 2,000 ms | Table not in time order (rows loaded shuffled) | Reload in `read_ts` order, or `CLUSTER`; BRIN needs physical correlation |
| `unique constraint must include partition key` | `UNIQUE (meter_id, read_ts)` declared without `read_ts` in the PK | Include the partition key in every unique constraint on a partitioned table |

**Instructor notes.** The BRIN-versus-B-tree comparison in task 4 is the moment of the module — 184 kB against 486 MB for nearly the same range performance genuinely surprises people. Have the numbers on the board before they run it so they can check their own. Watch for participants who reload the data shuffled and then conclude BRIN "doesn't work"; that is the correlation proviso and it is worth stopping the room for. In task 5, the partition-pruning comparison must be run by everyone — participants who only read about pruning do not internalise that an index cannot save a query whose predicate omits the partition key. Fast finishers: add a fourth partition for July, write the retention job that drops the oldest partition, and time it against the equivalent `DELETE` (instant versus 6 min 20 s).

## Mini Exercises

**Quiz (5 questions)**
1. Why is `NUMERIC` mandatory for SAR amounts? → binary floating point cannot represent decimal fractions exactly; error accumulates and never reconciles with the ledger.
2. When is BRIN a bad choice? → when physical row order does not correlate with the indexed column, e.g. a mutable dimension.
3. What must a unique constraint on a partitioned table include? → the partition key.
4. Which constraint type enforces non-overlapping validity periods? → `EXCLUDE USING gist` with a range and `&&`.
5. Name the three benefits of partitioning. → pruning, per-partition maintenance, retention by partition drop.

**Debugging exercise.** Check out `git checkout lab5-naive-timestamp`. `read_ts` is `TIMESTAMP` and SCADA data was loaded as UTC while manual reads were loaded as local time. Symptom: the daily NRW figure for the district swings between 27.8% and 35.1% with no operational cause, and the discrepancy is exactly the volume read between 21:00 and 24:00. Ask participants to find the three-hour shift, then discuss why this class of defect survives every row-level quality check ever written.

**Design exercise.** National rollout multiplies the reading table from 13,018,800 rows to approximately 1.4 billion over seven years. State what changes in the partitioning strategy, whether the BRIN index still fits, whether `bigint` remains sufficient for `reading_id`, and what the PDPL retention job looks like at that scale.

**Discussion questions.**
- Your DBA wants to drop all foreign keys "for load performance". What do you actually lose, and what is the compromise that keeps 90% of the speed and 100% of the integrity?
- Constraints move error detection from the application to the database. Who now owns the resulting production incident at 02:00, and how should that change the on-call runbook?

## Case Study — The Fourteen-Second Dashboard at "Tayyar" (تيار)

**Scenario.** "Tayyar" (تيار), a Saudi electricity distribution operator serving 2.8 million connections in the Eastern Province, deployed a smart-meter analytics platform holding 9.4 billion interval readings. The load-profile screen used by 340 network planners took 14 seconds to render a single feeder for a single day. After four months, usage telemetry showed 61 of 340 licensed users had opened it in the previous 30 days.

**Business context.** The platform cost SAR 42 million and was justified on the basis that planners would shift from annual peak estimates to daily observed load profiles, deferring roughly SAR 300 million of network reinforcement. None of that benefit was being realised, and the programme faced a cancellation review.

**Technical challenge.** The reading table was a single unpartitioned heap with a B-tree on `(reading_ts)` and another on `(meter_id)`. Every feeder query joined readings to a meter-to-feeder mapping and scanned a large fraction of the table because the planner's filter was on *feeder*, not on meter or time-first. The B-tree on `reading_ts` alone was 61 GB and mostly unused. The vendor's recommendation was to move to a larger instance class.

**Constraints.** The platform cannot be taken offline for more than a four-hour window, and only on a Friday. Interval readings at meter grain are personal data under PDPL and the entity's own retention policy caps them at 24 months, but the existing `DELETE`-based retention job had never completed inside its window and had silently been disabled 14 months earlier. The 9.4 billion rows include 3.1 billion beyond the retention limit.

**Solution approach (facilitate, don't lecture).** Steer towards: (1) partition by month on `reading_ts` and add `feeder_id` to the meter dimension so the join prunes; (2) replace the 61 GB `reading_ts` B-tree with BRIN, which on correlated append-only data gives comparable pruning for a few megabytes; (3) build a composite `(meter_id, reading_ts)` B-tree for the single-meter pattern; (4) make retention a partition drop, which both fixes the performance problem and closes a 14-month PDPL breach in one change. The most important facilitation move is to stop the room from treating the retention failure as a separate issue: it is the *same* design defect, and presenting it as one change with two benefits is how the fix gets funded.

**Discussion questions.**
1. Why did adding hardware not fix this, and what does that tell you about which layer the defect lived in?
2. The retention job was disabled by an engineer under delivery pressure and nobody noticed for 14 months. What control would have surfaced it?
3. Rank the four proposed changes by benefit-per-risk given the four-hour Friday window. Which do you ship first?
4. How would you present the combined performance-and-PDPL case to a cancellation review board without appearing to have hidden the compliance breach?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Schema deployed | Coverage | 16 tables, 3 monthly partitions | `\dt core.*` |
| Constraint traceability | Governance | 100% of constraints named with a rule ID | catalogue query on `pg_constraint` |
| Bulk load throughput | Performance | 13,018,800 rows in < 5 min (≈ 57,000 rows/s) | `make load-core` timing |
| Range-scan improvement | Performance | 2,140 ms → ≤ 130 ms with BRIN | `EXPLAIN (ANALYZE, BUFFERS)` |
| Partition pruning | Performance | 1 of 3 partitions scanned with predicate | plan inspection |

**Example benchmark table (filled during lab):**

| Access pattern | Index used | Size | Build | Buffers | Latency |
|---|---|---|---|---|---|
| A — one meter, 7 days | btree `(meter_id, read_ts)` | 486 MB | 84 s | 142 | 46 ms |
| B — district, 1 day | brin `(read_ts)` | 184 kB | 9 s | 18,430 | 118 ms |
| B — district, 1 day (no index) | seq scan | — | — | 421,600 | 2,140 ms |
| C — open work orders | partial btree | 216 kB | 0.3 s | 61 | 3 ms |
| D — holder-name fuzzy search | gin `pg_trgm` | 11 MB | 6 s | 380 | 22 ms |

## Required Visuals and Training Assets

### Diagrams
1. **Logical → physical translation map** — *Purpose:* show that physical design is a set of decisions, not a transcription. *Elements:* three parallel columns (logical element / decision to make / physical artefact) with Baseerah rows: entity→table, domain→type+CHECK, alternate key→UNIQUE, relationship→FK+action, access pattern→index, retention→partition. *Style:* three-column mapping table rendered as a diagram. *Designer description:* "Left column of logical shapes, arrows through a decision diamond, right column of DDL fragments."
2. **B-tree versus BRIN on time-series** — *Purpose:* the module's headline result. *Elements:* two index structures drawn to relative scale — a tall B-tree labelled 486 MB against a tiny BRIN block-range summary labelled 184 kB — over the same physically time-ordered heap, with the correlation requirement called out in red. *Style:* to-scale comparison with a warning chip.
3. **Partitioning serves three masters** — *Purpose:* participants must name all three. *Elements:* one partitioned table with three arrows out: pruning (query), maintenance (VACUUM/ANALYZE per partition), retention (DROP with a PDPL badge). *Style:* hub-and-spoke.
4. **Constraint-to-rule traceability** — *Purpose:* make governance visible in the engine. *Elements:* a production error message `ck_meter_reading_nonneg_r013` traced back through the rule register to a named owner and a BECAUSE clause. *Style:* trace ribbon from error text to steward's photo card.

### Images (screenshots)
1. **`\di+` output showing all four indexes with sizes** — *why:* the 486 MB against 184 kB contrast must be seen in a real terminal; *content:* the index list with the size column highlighted.
2. **Two `EXPLAIN` plans side by side** — *why:* plan-reading is the assessable skill; *content:* Parallel Seq Scan at 2,140 ms next to Bitmap Heap Scan on BRIN at 118 ms.
3. **Partition pruning in the plan** — *why:* pruning is invisible unless you look; *content:* the plan showing `Subplans Removed: 2` with the predicate present, and its absence without.

### Simulations
1. **The load that took 22 minutes** — *Setup:* branch `sim-index-first` creates all indexes and validated constraints before the `COPY`. *Expected behaviour:* the same 13,018,800 rows take 22 min instead of 3 min 48 s, a 5.8× penalty. *Learning objective:* index maintenance is paid on every insert; order of operations is a design decision.
2. **The shuffled BRIN** — *Setup:* branch `sim-brin-shuffled` loads the readings in random order. *Expected behaviour:* BRIN is built, is chosen by the planner, and delivers 1,980 ms — barely better than the sequential scan. *Learning objective:* BRIN's benefit is entirely contingent on physical/logical correlation.

### Interactive Activities
- **Pick the index (12 min):** eight Baseerah access patterns on cards; teams choose an index type for each and defend it, then check against the measured table.
- **Constraint or code? (10 min):** ten business rules; teams place each in the database (CHECK/FK/EXCLUDE/UNIQUE) or the application, and state what breaks if it is placed in the other.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `data/core_meter_reading.csv` | Synthetic AMI + manual reads, Riyadh North, 90 days | CSV | 13,018,800 rows / 1.06 GB | Bulk load, indexing, partitioning |
| `data/core_work_order.csv` | Synthetic maintenance jobs, 24 months | CSV | 184,600 rows (3,880 open) | Partial-index pattern |
| `data/core_customer_account.csv` | Deduplicated account master (post-M6 target state) | CSV | 58,100 rows | Trigram index pattern |
| `sql/bench/run_patterns.sql` | Course benchmark harness | SQL | 4 patterns | `BENCHMARKS.md` evidence |

### Demo Requirements
- **Instructor demo (7 min):** build the BRIN index live in nine seconds, show `\di+` reporting 184 kB, run the district query at 118 ms, then drop the predicate and show all three partitions scanned. Close with: "184 kilobytes bought 18× on a query that decided whether 340 planners used a SAR 42 million platform."

---

# Module 6 — Data Quality Engineering: Profiling, Rules, Remediation, and Stewardship
## هندسة جودة البيانات

## Module Overview

**Purpose.** This module carries the "Data Quality" half of the course title. Participants learn to measure quality across six named dimensions rather than argue about it, to profile sources systematically, to encode quality rules as executable expectations, to apply a remediation ladder that never silently invents data, to match and merge duplicate customer records with explicit survivorship rules, and to run a stewardship loop that assigns defects to humans who can actually fix them. It delivers the data-quality controls of catalogue Module 8 (validation, cleansing, matching, error tracking) as a first-class module rather than a bullet inside integration.

**Business relevance.** Baseerah's regulator-facing NRW figure is a difference of two large numbers. A 3% understatement of billed volume — entirely achievable through duplicate accounts, stopped meters recorded as zero, and readings that arrive in the wrong day — moves the reported NRW figure by roughly 2 percentage points and can turn a compliant utility into a non-compliant one on paper. Quality here is not hygiene; it is the difference between a defensible submission and a regulatory finding.

**Industry use cases.**
- A hospital group must resolve duplicate patient records before a national health record can be joined, with survivorship rules that never lose a clinically relevant field.
- A utility must distinguish a genuine zero-consumption property from a stopped meter, because one is revenue and the other is loss.
- A ministry publishing open data must measure completeness per attribute before publication, because an 80%-populated column is worse than an absent one.

**Expected competencies.** After this module a participant can profile a source and produce a defensible quality baseline; define and measure the six quality dimensions; author a Great Expectations suite from the rule register; choose the correct rung of the remediation ladder for a defect class; implement deterministic and fuzzy match/merge with survivorship rules; and operate a stewardship queue with measurable throughput.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Profile a source system and produce a quantitative quality baseline | LO6 |
| 6.2 | Define and measure the six data-quality dimensions | LO6 |
| 6.3 | Author executable expectation suites generated from the rule register | LO6, LO2 |
| 6.4 | Apply the remediation ladder without fabricating data | LO6 |
| 6.5 | Implement match/merge with deterministic, fuzzy and survivorship logic | LO6, LO3 |
| 6.6 | Operate a stewardship queue with owners and service levels | LO6, LO8 |

## Technical Content

### 1. The six dimensions, measured

"Data quality" is unmanageable until it is decomposed. Six dimensions cover the field, and each has a distinct measurement, a distinct cause, and a distinct fix.

| Dimension | Question | Baseerah measurement | Baseline | Target |
|---|---|---|---|---|
| **Completeness** | Is the value present where it is required? | % of required attributes populated across 9 profiled columns | 71.0% | 96.0% |
| **Validity** | Does the value conform to its domain, format, or range? | % of rows passing 11 domain/format expectations | 88.2% | 99.1% |
| **Accuracy** | Does the value correspond to the real world? | % of readings not physically impossible (negative, > 3× rolling median, index going backwards) | 81.4% | 97.4% |
| **Consistency** | Do related values agree with each other and across systems? | % of accounts whose tariff class agrees with service-point property type, and whose billed volume reconciles to metered volume | 64.1% | 92.8% |
| **Uniqueness** | Does one real-world thing appear exactly once? | mean of 4 uniqueness checks: `account_no` 94.6%, `holder_national_id` 92.7%, `national_address` 40.2%, `meter_serial+manufacturer` 99.98% | 81.9% | 99.5% |
| **Timeliness** | Did the value arrive when the business needed it? | % of AMI readings landing within the 4-hour SLA | 47.8% | 84.0% |

Each dimension score is the row-weighted pass rate of the expectations assigned to it; the **composite score is the unweighted mean of the six**, giving Baseerah a baseline of **72.4%** and a post-remediation target of **94.8%**. Publish the composite *and* the six components: a single number hides which directorate owns the problem, and a scorecard that cannot be assigned is a scorecard nobody works.

Two Baseerah subtleties worth teaching. Uniqueness at 81.9% is dragged down almost entirely by `national_address` at 40.2% — because in the sample 62 service points genuinely share an address (mixed-use buildings, resolved by the Module 3 associative entity), and thousands more share it because the address was typed rather than selected. Only the second group is a defect. And timeliness at 47.8% is a *pipeline* problem, not a data problem: no amount of cleansing improves it, which is why it is the dimension most often quietly dropped from scorecards.

### 2. Profiling: what to compute before you have any opinions

Profiling produces facts; the quality baseline is an interpretation of those facts. For every column compute: row count, null count and rate, distinct count and cardinality ratio, min/max/mean/percentiles for numerics, min/max length and top-20 patterns for strings, and top-20 frequency values. Then look for the five smells:

1. **A cardinality ratio of exactly 1.0** on a column you did not expect to be a key — you have found an undeclared natural key (or a source export bug).
2. **A top value that is a sentinel** — `'N/A'`, `'0000-00-00'`, `'-1'`, `'UNKNOWN'`. These are nulls wearing a costume, and they pass every `NOT NULL` check.
3. **More than three string patterns** in a supposedly formatted column: `RYD-0041`, `ryd 41`, `41` are one district in three dialects.
4. **A minimum of zero or a maximum at a round number** — `9999.999` is a clamp, not a measurement.
5. **A distribution that changes at a date boundary** — a system migration nobody documented.

### 3. The remediation ladder

Given a defect, choose the highest rung you can justify. Never skip upward without evidence.

| Rung | Action | When | Baseerah example |
|---|---|---|---|
| 1 | **Fix at source** | The source system can and should hold the correct value | Missing `national_address` — push back to billing; 4,180 addresses corrected in the CRM |
| 2 | **Reject and quarantine** | The row cannot be trusted and must not enter the warehouse silently | Negative delta volume: 24,760 readings quarantined for steward review |
| 3 | **Derive deterministically** | The correct value is computable from other trusted data with no judgement | `volume_m3` recomputed from consecutive `index_m3` values |
| 4 | **Impute, flagged** | No better option, and consumers can be told | Estimated reads for a failed AMI meter, `is_estimated = true`, excluded from the NRW denominator |
| 5 | **Accept and document** | The defect is immaterial or unfixable | 62 genuinely shared addresses — documented as a known exception, not a defect |

The rule that must be stated aloud: **imputation is always flagged and never silent**. An estimated reading that looks identical to a measured one is not a repaired record; it is a fabricated one, and in a regulator-facing NRW submission it is a misrepresentation. Baseerah's `is_estimated` boolean exists for exactly this reason and every downstream measure respects it.

### 4. Match/merge and survivorship

Baseerah's billing extract holds 61,420 account rows describing 58,100 real customers: **3,320 duplicate records**, created by call-centre re-registration, migration from two legacy regional systems, and the absence of the alternate key Module 3 insisted on.

A three-pass strategy:

- **Pass 1 — deterministic.** Exact match on `holder_national_id` where present. Highest confidence, resolves 2,140 duplicates. National ID is PDPL personal data, so the match runs inside `core` and only surrogate `customer_id` values leave it.
- **Pass 2 — normalised deterministic.** Match on normalised `(national_address, normalised_holder_name)`. Normalisation strips honorifics, unifies Arabic orthographic variants (أ/إ/ا, ة/ه, ى/ي), collapses whitespace, and transliterates consistently. Resolves a further 890.
- **Pass 3 — probabilistic.** Trigram similarity on name plus address proximity, scored, with a review band. Above 0.92 auto-merge (290 pairs); 0.80–0.92 goes to a steward (188 pairs, of which 106 were confirmed merges); below 0.80 no match.

**Survivorship** decides which value wins in the surviving golden record, and it is field-level, not record-level:

| Field | Survivorship rule | Why |
|---|---|---|
| `holder_national_id` | Non-null, then most frequent | An ID appearing on three records is more likely correct than a typo appearing once |
| `holder_name` | Longest non-abbreviated form | "Abdulrahman" beats "A." — recoverable detail wins |
| `mobile_no` | Most recently updated | Contact data decays; recency is the best proxy for correctness |
| `opened_on` | Earliest | The customer relationship began at the first registration |
| `account_status` | Most severe (`DISPUTED` > `SUSPENDED` > `ACTIVE` > `CLOSED`) | Never merge a dispute out of existence |
| `national_address` | From the record with a validated address | Validation beats recency |

Record-level "the newest record wins" survivorship is the commonest and worst choice: it discards the earliest `opened_on`, which is a legal fact, and it can silently resolve a dispute. Every merge must be reversible — Baseerah keeps `core.customer_merge_log` with the surviving `customer_id`, every merged source ID, the pass and score that matched them, and the steward who approved it.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Measure before you remediate;* a baseline you did not record cannot demonstrate improvement to a sponsor.
- *Every expectation traces to a rule ID,* so a failure names an owner and a reason.
- *Quarantine, don't drop.* A dropped row is invisible; a quarantined row is a work item.
- *Imputation is flagged, always.*
- *Merges are logged and reversible;* a match at 0.93 confidence is still 7% wrong at scale.
- *A steward is a person with time allocated,* not a job title on a slide.

**Common mistakes (each appears in the Lab 6 starter deliberately)**
1. Treating sentinel values (`'N/A'`, `'0000-00-00'`) as populated, inflating completeness from 71.0% to a fictitious 94%.
2. Auto-merging everything above 0.80 similarity, which merges 82 genuinely distinct customers who share a family name and a district.
3. Silent imputation of missing reads with the previous value, which makes a stopped meter look like a paying customer and *reduces* apparent NRW while increasing real loss.
4. Dropping rows that fail expectations instead of quarantining, so billed volume falls 2.1% with no audit trail.
5. Applying record-level survivorship, discarding the earliest `opened_on` and resolving 14 disputes into `ACTIVE`.
6. Publishing a single composite score with no dimension breakdown, so no directorate accepts ownership.

**Production considerations**
- Run expectations at the `raw → stg` boundary, not after transformation: you want to know the source was wrong, not that your model was.
- Keep quarantine in a table with the same schema plus `failed_expectation`, `rule_id`, `quarantined_at`, and a steward-assignment column. Quarantine that is not routed is a bin.
- Track steward throughput as an operational metric — items raised, items closed, median age. A queue growing faster than it is worked is a governance failure, and it shows up as quality decay six months later.

### 6. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's NRW figure improved from 31.4% to 28.9% in one quarter with no field work whatsoever, and the network directorate was congratulated. The cause was a data-quality "improvement": missing AMI reads had begun being backfilled with the previous non-null reading, un-flagged, by a well-intentioned engineer. Meters that had stopped entirely — the single largest component of apparent loss — now reported plausible consumption, which was billed, which raised billed volume, which lowered NRW. The utility was reporting a 2.5-point improvement while losing more water than before, and it took a field audit of 40 properties in Al-Ahsa to find it. When the imputation was flagged and excluded from the NRW denominator, the figure returned to 31.7%. The lesson is stark and worth stating as the module's thesis: **a quality process that cannot distinguish a repaired value from a measured one will eventually improve your metrics by damaging your business.**

## Code Examples

### Profiling that produces a defensible baseline

```python
# src/baseerah/dq/profile.py
"""Profile a source table and emit a quality baseline into dq.profile_result.

WHY: remediation without a recorded baseline cannot be defended to a sponsor
and cannot be regression-tested. This profiler deliberately treats SENTINELS
as missing -- 'N/A', '0000-00-00', '-1', 'UNKNOWN' pass NOT NULL checks while
carrying no information, and counting them as populated is how a real 71.0%
completeness gets reported as a fictitious 94%.
"""
from __future__ import annotations

import psycopg

# Values that are structurally present but semantically absent. Extend this
# list per source system; every one below was found in the Baseerah extracts.
SENTINELS = ("N/A", "n/a", "-", "--", "UNKNOWN", "NULL", "0000-00-00", "-1", "")

PROFILE_COLUMN = """
WITH src AS (SELECT {col}::text AS v FROM {table})
SELECT
    count(*)                                              AS row_count,
    count(v)                                              AS non_null,
    count(*) FILTER (WHERE v = ANY(%(sentinels)s))        AS sentinel_count,
    count(DISTINCT v)                                     AS distinct_count,
    min(length(v))                                        AS min_len,
    max(length(v))                                        AS max_len
FROM src;
"""

TOP_PATTERNS = """
-- Collapse each value to its shape: digits -> 9, letters -> A. Three or more
-- distinct shapes in a formatted column means three dialects of one concept.
SELECT regexp_replace(regexp_replace({col}::text, '[0-9]', '9', 'g'),
                      '[A-Za-z]', 'A', 'g') AS shape,
       count(*) AS n
FROM   {table}
WHERE  {col} IS NOT NULL
GROUP  BY 1 ORDER BY n DESC LIMIT 20;
"""


def profile_column(conn: psycopg.Connection, table: str, col: str) -> dict:
    """Return the profile facts for one column, sentinel-aware."""
    with conn.cursor() as cur:
        cur.execute(PROFILE_COLUMN.format(table=table, col=col),
                    {"sentinels": list(SENTINELS)})
        rows, non_null, sentinels, distinct, min_len, max_len = cur.fetchone()

        cur.execute(TOP_PATTERNS.format(table=table, col=col))
        shapes = cur.fetchall()

    # Completeness counts a sentinel as MISSING. This single decision is the
    # difference between an honest baseline and a flattering one.
    populated = non_null - sentinels
    return {
        "table": table,
        "column": col,
        "row_count": rows,
        "completeness_pct": round(100.0 * populated / rows, 2) if rows else 0.0,
        "sentinel_count": sentinels,
        "distinct_count": distinct,
        "cardinality_ratio": round(distinct / rows, 6) if rows else 0.0,
        "min_len": min_len,
        "max_len": max_len,
        "distinct_shapes": len(shapes),
        "top_shape": shapes[0][0] if shapes else None,
        # Smell flags from Technical Content section 2.
        "smell_undeclared_key": rows > 0 and distinct == rows,
        "smell_multi_format": len(shapes) > 3,
        "smell_sentinel_heavy": rows > 0 and sentinels / rows > 0.01,
    }


def profile_table(conn: psycopg.Connection, table: str, columns: list[str]) -> None:
    """Profile every named column and persist the results for the baseline."""
    with conn.cursor() as cur:
        for col in columns:
            p = profile_column(conn, table, col)
            cur.execute(
                """
                INSERT INTO dq.profile_result
                    (table_name, column_name, row_count, completeness_pct,
                     sentinel_count, distinct_count, cardinality_ratio,
                     distinct_shapes, smell_flags, profiled_at)
                VALUES (%(table)s, %(column)s, %(row_count)s, %(completeness_pct)s,
                        %(sentinel_count)s, %(distinct_count)s,
                        %(cardinality_ratio)s, %(distinct_shapes)s,
                        %(smells)s, now())
                """,
                {**p, "smells": [k for k, v in p.items()
                                 if k.startswith("smell_") and v]},
            )
            flags = " ".join(k for k, v in p.items() if k.startswith("smell_") and v)
            print(f"{table}.{col:<24} complete={p['completeness_pct']:>6.2f}%  "
                  f"shapes={p['distinct_shapes']:<3} {flags}")
    conn.commit()
```

### Match/merge with field-level survivorship and a reversible log

```sql
-- sql/dq/062_customer_match_merge.sql
--
-- WHY: 61,420 raw account rows describe 58,100 real customers. Merging them
-- is not a deduplication script -- it is a decision about which value of each
-- field survives, and it must be REVERSIBLE. Every merge below is written to
-- core.customer_merge_log with the pass, the score, and the approver, because
-- a probabilistic match at 0.93 confidence is still 7% wrong at scale.
--
-- PDPL: holder_national_id never leaves the core schema. Downstream consumers
-- receive only the surrogate customer_id.

-- Pass 1 -- deterministic on national ID. Highest confidence: 2,140 duplicates.
CREATE TEMP TABLE match_pass1 AS
SELECT min(account_id) AS surviving_id,
       array_agg(account_id ORDER BY account_id) AS merged_ids,
       'P1_NATIONAL_ID' AS pass,
       1.00 AS score
FROM   stg.customer_account_raw
WHERE  holder_national_id IS NOT NULL
  AND  holder_national_id <> ALL (ARRAY['N/A', '0000000000', '-1'])
GROUP  BY holder_national_id
HAVING count(*) > 1;

-- Pass 2 -- normalised deterministic on (address, name). A further 890.
-- normalise_ar() unifies Arabic orthographic variants (أ إ آ -> ا, ة -> ه,
-- ى -> ي), strips honorifics and tatweel, and collapses whitespace. Without
-- it, "عبد الرحمن" and "عبدالرحمن" are different customers forever.
CREATE TEMP TABLE match_pass2 AS
SELECT min(a.account_id) AS surviving_id,
       array_agg(a.account_id ORDER BY a.account_id) AS merged_ids,
       'P2_NORM_ADDR_NAME' AS pass,
       0.98 AS score
FROM   stg.customer_account_raw AS a
WHERE  NOT EXISTS (SELECT 1 FROM match_pass1 p
                   WHERE a.account_id = ANY(p.merged_ids))
  AND  a.national_address IS NOT NULL
GROUP  BY a.national_address, core.normalise_ar(a.holder_name)
HAVING count(*) > 1;

-- Pass 3 -- probabilistic. Trigram name similarity within the same DMA.
-- Three bands, and the middle band goes to a HUMAN. Auto-merging the 0.80-0.92
-- band would merge 82 genuinely distinct customers who share a family name
-- and a district -- planted defect #2 in the lab starter.
CREATE TEMP TABLE match_pass3 AS
SELECT LEAST(a.account_id, b.account_id)    AS surviving_id,
       ARRAY[LEAST(a.account_id, b.account_id),
             GREATEST(a.account_id, b.account_id)] AS merged_ids,
       CASE WHEN similarity(core.normalise_ar(a.holder_name),
                            core.normalise_ar(b.holder_name)) >= 0.92
            THEN 'P3_AUTO' ELSE 'P3_REVIEW' END AS pass,
       round(similarity(core.normalise_ar(a.holder_name),
                        core.normalise_ar(b.holder_name))::numeric, 3) AS score
FROM   stg.customer_account_raw AS a
JOIN   stg.customer_account_raw AS b
       ON  b.account_id > a.account_id
       AND b.dma_id     = a.dma_id
       AND core.normalise_ar(b.holder_name) % core.normalise_ar(a.holder_name)
WHERE  similarity(core.normalise_ar(a.holder_name),
                  core.normalise_ar(b.holder_name)) >= 0.80;

-- Field-level survivorship. NOT "newest record wins": that discards the
-- earliest opened_on (a legal fact) and can resolve a dispute out of existence.
CREATE TABLE core.customer_golden AS
WITH clusters AS (
    SELECT surviving_id, unnest(merged_ids) AS member_id, pass, score
    FROM   (SELECT * FROM match_pass1
            UNION ALL SELECT * FROM match_pass2
            UNION ALL SELECT * FROM match_pass3 WHERE pass = 'P3_AUTO') AS m
)
SELECT c.surviving_id AS customer_id,
       -- non-null, then most frequent
       mode() WITHIN GROUP (ORDER BY r.holder_national_id)
              FILTER (WHERE r.holder_national_id IS NOT NULL) AS holder_national_id,
       -- longest non-abbreviated form: "Abdulrahman" beats "A."
       (array_agg(r.holder_name ORDER BY length(r.holder_name) DESC))[1] AS holder_name,
       -- contact data decays: recency is the best proxy for correctness
       (array_agg(r.mobile_no ORDER BY r.updated_at DESC NULLS LAST))[1] AS mobile_no,
       -- the relationship began at the FIRST registration
       min(r.opened_on) AS opened_on,
       -- most severe status wins: never merge a dispute out of existence
       (array_agg(r.account_status ORDER BY
            CASE r.account_status WHEN 'DISPUTED'  THEN 1
                                  WHEN 'SUSPENDED' THEN 2
                                  WHEN 'ACTIVE'    THEN 3
                                  ELSE 4 END))[1] AS account_status,
       -- validation beats recency for addresses
       (array_agg(r.national_address ORDER BY r.address_validated DESC NULLS LAST,
                                              r.updated_at DESC))[1] AS national_address
FROM   clusters AS c
JOIN   stg.customer_account_raw AS r ON r.account_id = c.member_id
GROUP  BY c.surviving_id;

-- Reversibility: every merge is logged with its pass, score and approver.
INSERT INTO core.customer_merge_log
    (surviving_customer_id, merged_account_id, match_pass, match_score,
     approved_by, merged_at)
SELECT surviving_id, unnest(merged_ids), pass, score,
       CASE WHEN pass LIKE 'P3%' THEN 'steward.billing@baseerah.gov.sa'
            ELSE 'automated' END,
       now()
FROM   (SELECT * FROM match_pass1
        UNION ALL SELECT * FROM match_pass2
        UNION ALL SELECT * FROM match_pass3 WHERE pass = 'P3_AUTO') AS m;

-- The review band NEVER auto-merges. It becomes steward work items.
INSERT INTO dq.steward_task (task_type, subject_ids, detail, assigned_to, sla_days)
SELECT 'CUSTOMER_MERGE_REVIEW', merged_ids,
       format('Trigram score %s - confirm or reject merge', score),
       'steward.billing@baseerah.gov.sa', 5
FROM   match_pass3 WHERE pass = 'P3_REVIEW';
```

## Hands-on Lab 6 — Profile, Score, Remediate, and Deduplicate

| | |
|---|---|
| **Objective** | Produce the Baseerah quality baseline (72.4%), author a Great Expectations suite generated from the rule register, apply the remediation ladder to five defect classes, and deduplicate 3,320 customer records with field-level survivorship — reaching a composite score of 94.8% |
| **Duration** | 100 minutes (Lab 6a: 50 min, Lab 6b: 50 min) |
| **Setup** | PostgreSQL 16 with `core` deployed from Lab 5, `pip install great-expectations==0.18.* psycopg[binary]==3.1.*`, `pg_trgm` enabled, course repo, `git checkout lab6-start` |

**Instructions & tasks**

1. *(12 min)* **6a.** Profile all four sources with `python -m baseerah.dq.profile --all`. Record the composite baseline in `DQ_BASELINE.md`. It must come out at 72.4%; if you get 94% you counted sentinels as populated — planted defect #1.
2. *(12 min)* **6a.** Generate the expectation suite from the rule register (`python -m baseerah.rules.compile_rules --to-gx`) and run it. Triage the failures into the six dimensions and confirm your dimension scores match the table (completeness 71.0, validity 88.2, accuracy 81.4, consistency 64.1, uniqueness 81.9, timeliness 47.8).
3. *(14 min)* **6a.** Apply the remediation ladder to five defect classes, choosing and recording a rung for each: missing `national_address` (rung 1), negative delta volume (rung 2), `volume_m3` recomputable from `index_m3` (rung 3), failed AMI meters (rung 4, flagged), 62 shared addresses (rung 5). Quarantine — never drop — and confirm 24,760 readings land in `dq.quarantine`.
4. *(12 min)* **6a.** Re-score. Confirm five of six dimensions improve and record which one does not (timeliness — it is a pipeline problem and cleansing cannot touch it). Commit: `feat(dq): baseline 72.4% + expectation suite + remediation ladder`.
5. *(30 min)* **6b.** Run the three match passes. Pass 1 must resolve 2,140, pass 2 a further 890, pass 3 auto-merge 290 and route 188 pairs to review. Implement field-level survivorship and confirm `core.customer_golden` holds 58,100 rows and that no `DISPUTED` account has been merged into `ACTIVE`.
6. *(20 min)* **6b.** Verify reversibility by un-merging one cluster from `core.customer_merge_log`. Re-score the composite to 94.8%. Commit: `feat(dq): customer match/merge with survivorship and reversible merge log`.

**Expected output**
```
$ python -m baseerah.dq.profile --all
raw.customer_account.national_address   complete= 91.20%  shapes=7   smell_multi_format
raw.customer_account.holder_national_id complete= 82.40%  shapes=3   smell_sentinel_heavy
raw.meter_reading.volume_m3             complete= 96.10%  shapes=2
...
COMPOSITE DQ SCORE (baseline): 72.4%
  completeness 71.0 | validity 88.2 | accuracy 81.4
  consistency  64.1 | uniqueness 81.9 | timeliness 47.8

$ great_expectations checkpoint run baseerah_core
Validation FAILED. 14 of 31 expectations failed.
  R-014 expect_column_values_to_be_between(volume_m3)  ->  24,760 unexpected
  R-006 expect_column_values_to_be_unique(account_no)  ->   3,320 unexpected
  R-011 expect_column_values_to_not_be_null(national_address) -> 5,405 unexpected

$ psql -f sql/dq/062_customer_match_merge.sql
Pass 1 (national ID, deterministic) : 2,140 duplicates resolved
Pass 2 (normalised addr+name)       :   890 duplicates resolved
Pass 3 (trigram >= 0.92, auto)      :   290 duplicates resolved
Pass 3 (trigram 0.80-0.92, review)  :   188 pairs -> dq.steward_task
core.customer_golden                : 58,100 rows  (from 61,420 raw)
core.customer_merge_log             :  3,320 rows  (all reversible)
DISPUTED accounts merged into ACTIVE:      0   <-- survivorship rule held

$ python -m baseerah.dq.score --after
COMPOSITE DQ SCORE (post-remediation): 94.8%
  completeness 96.0 | validity 99.1 | accuracy 97.4
  consistency  92.8 | uniqueness 99.5 | timeliness 84.0
```

**Acceptance criteria**
- Baseline composite is 72.4% with all six dimension scores recorded and sentinel-aware.
- 24,760 readings quarantined (not dropped); `dq.quarantine` carries `rule_id` and an assigned steward.
- `core.customer_golden` holds exactly 58,100 rows; zero `DISPUTED` accounts merged into `ACTIVE`; every merge is in the log and one un-merge is demonstrated.
- Post-remediation composite is 94.8%; `DQ_BASELINE.md` explains why timeliness lags the others.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Baseline reads ~94% | Sentinels counted as populated | Pass the `SENTINELS` list to the profiler; `'N/A'` is missing data |
| `customer_golden` has 57,180 rows | Auto-merged the 0.80–0.92 review band | Restrict auto-merge to ≥ 0.92; the review band is human work |
| Arabic names not matching | `normalise_ar()` not applied | Normalise orthographic variants before similarity; أ/ا and ة/ه are the same name |
| Billed volume falls 2.1% after remediation | Failing rows dropped rather than quarantined | Route to `dq.quarantine`; a dropped row is invisible loss |

**Instructor notes.** The single most valuable moment is task 1 for the pairs who get 94%. Do not correct them immediately — let them present the flattering number, then ask them to `SELECT DISTINCT national_address ORDER BY 1 LIMIT 20` and watch them find `'N/A'` at the top. That discovery is worth twenty minutes of lecture on sentinels. In 6b, expect strong pressure to auto-merge the review band because 188 manual reviews feels like failure; ask what the utility's position is when it has merged two brothers at the same address into one account and billed one of them for both. Fast finishers: compute the NRW impact of the remediation — billed volume rises 1.8% and the district NRW figure moves from 31.4% to 30.2%, entirely through data quality, with zero field work.

## Mini Exercises

**Quiz (5 questions)**
1. Which dimension cannot be improved by cleansing? → **timeliness** — it is a pipeline/SLA problem.
2. Why must imputed values be flagged? → an unflagged estimate is indistinguishable from a measurement and misrepresents a regulator-facing figure.
3. What is wrong with "newest record wins" survivorship? → it discards the earliest `opened_on` and can resolve a dispute into `ACTIVE`.
4. Give two sentinel values that defeat a `NOT NULL` check. → `'N/A'`, `'0000-00-00'` (also `'-1'`, `'UNKNOWN'`).
5. Why quarantine instead of drop? → a dropped row is invisible loss with no audit trail; a quarantined row is an assignable work item.

**Debugging exercise.** Check out `git checkout lab6-silent-imputation`. Missing AMI reads are backfilled with the previous non-null value and no flag. Symptom: district NRW improves from 31.4% to 28.9% in one quarter with no field work, and stopped meters continue to be billed. Ask participants to find the imputation, add the flag, exclude flagged reads from the NRW denominator, and watch the figure return to 31.7%. Then discuss the organisational hazard: the person who introduced this was rewarded for it.

**Design exercise.** The authority acquires a regional water company with 214,000 accounts in its own format, 11% of which are believed to overlap with existing Baseerah customers. Design the match/merge: which passes apply, what changes in survivorship when the acquired system's `opened_on` predates Baseerah's, how you size the review band so a two-person steward team can clear it in six weeks, and what you tell the regulator about the customer count during the transition.

**Discussion questions.**
- Your composite score is 94.8% and the sponsor wants 99%. What is the honest answer about what the last four points cost, and which dimension would you refuse to chase?
- Should a data-quality gate block a regulator submission, or flag it? Argue both, then decide what the submission cover note must say in each case.

## Case Study — The Duplicate Patient Master at "Nubras" (نبراس)

**Scenario.** "Nubras" (نبراس), a Saudi private hospital group operating six facilities in Riyadh, Jeddah and Abha, was preparing to connect to a national health record exchange. A pre-integration audit found that its 1.34 million patient records described an estimated 1.19 million distinct people — roughly 150,000 duplicates, 11.2% of the master.

**Business context.** A duplicate patient record is not a reporting inconvenience. It splits a clinical history, so an allergy recorded at the Jeddah facility is invisible at Abha. The integration cannot proceed until the master is resolved, and the exchange's onboarding window closes in ten weeks.

**Technical challenge.** Duplicates arose from three mechanisms: emergency-department registration under a partial name when an ID was not to hand; Arabic name variants entered inconsistently across six facilities with different keyboard layouts; and a 2019 acquisition whose records were loaded without any matching at all. National ID was present on only 78% of records, and among the acquired records on 41%.

**Constraints.** A false merge in a clinical system is a patient-safety event, so the tolerance for over-matching is far lower than in a utility. Health data is a special category under PDPL requiring explicit safeguards, so the matching cannot be done by an external vendor without a formal processing agreement. Merges must be clinically reversible with a full audit trail. The hospital cannot pause registration during the exercise.

**Solution approach (facilitate, don't lecture).** Guide the room towards: (1) a much narrower auto-merge band than Baseerah's — deterministic passes only, plus probabilistic matches above 0.97 that *also* agree on date of birth and gender; (2) a large, deliberately accepted review queue, sized against clinician availability rather than against the deadline; (3) survivorship that is *additive* for clinical fields — allergies, diagnoses and medications from all merged records are unioned, never selected between, because losing an allergy is unacceptable while carrying a duplicate one is merely untidy; (4) a "possible duplicate" banner in the clinical UI for the unresolved review band, which delivers most of the safety benefit before any merge happens. The facilitation move that matters: push back when the room proposes tuning the threshold to clear the queue by the deadline. The deadline is negotiable; a false merge is not.

**Discussion questions.**
1. Why is survivorship for clinical fields additive rather than selective, and where does that logic also apply in a utility?
2. The review band cannot be cleared in ten weeks. What can be delivered in ten weeks that captures most of the safety benefit?
3. How would you measure the *harm* of the current duplicates so the board can compare it against the cost of the programme?
4. National ID is missing on 59% of acquired records. What is the highest rung of the remediation ladder available, and what does it cost?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Composite DQ score | Quality | 72.4% → 94.8% | `baseerah.dq.score` before/after |
| Expectation coverage | Governance | ≥ 31 expectations, 100% traced to a rule ID | GX suite `meta.rule_id` |
| Quarantine discipline | Correctness | 24,760 rows quarantined, 0 dropped | `dq.quarantine` count vs source delta |
| Duplicate resolution | Quality | 3,320 resolved; 58,100 golden records | `core.customer_golden` count |
| Merge reversibility | Governance | 100% logged; 1 un-merge demonstrated | `core.customer_merge_log` |

**Example benchmark table (filled during lab):**

| Dimension | Baseline | After | Driver of the change | Ladder rung used |
|---|---|---|---|---|
| Completeness | 71.0% | 96.0% | 4,180 addresses corrected at source | 1 |
| Validity | 88.2% | 99.1% | domain CHECKs + sentinel mapping | 1, 2 |
| Accuracy | 81.4% | 97.4% | 24,760 impossible reads quarantined | 2 |
| Consistency | 64.1% | 92.8% | tariff/property-type reconciliation | 1, 3 |
| Uniqueness | 81.9% | 99.5% | 3,320 duplicates merged | 3 |
| Timeliness | 47.8% | 84.0% | SCADA polling interval change — *not* cleansing | pipeline fix |
| **Composite** | **72.4%** | **94.8%** | — | — |

## Required Visuals and Training Assets

### Diagrams
1. **The six dimensions with Baseerah measurements** — *Purpose:* the module's scorecard, reused on every subsequent day. *Elements:* six panels, each with the dimension name (English + Arabic), its question, its Baseerah measurement, and a baseline→target bar. *Style:* dashboard-style card grid. *Designer description:* "Six equal cards in two rows; each has a horizontal progress bar from the baseline value to the target, the shortfall in amber."
2. **The remediation ladder** — *Purpose:* make rung choice a procedure. *Elements:* five rungs from "fix at source" down to "accept and document", each with its Baseerah example and row count, with a red arrow marking the forbidden move (skipping to rung 4 without evidence). *Style:* vertical ladder with a crossed-out shortcut.
3. **Three-pass match/merge with survivorship** — *Purpose:* the module's most intricate mechanic. *Elements:* 61,420 records funnelling through deterministic → normalised → probabilistic passes with counts on each arrow (2,140 / 890 / 290 / 188 to review), then a field-level survivorship panel showing six fields and their winning rules. *Style:* funnel plus an exploded record view. *Designer description:* "A funnel narrowing 61,420 to 58,100, with a side branch of 188 routed to a person icon."
4. **Silent imputation, visualised** — *Purpose:* the module's thesis. *Elements:* two NRW trend lines — reported (falling to 28.9%) and actual (rising) — diverging at the point imputation began, with a stopped-meter icon underneath. *Style:* dual-line chart with a divergence shading.

### Images (screenshots)
1. **Great Expectations Data Docs for `baseerah_core`** — *why:* participants must see the rendered validation report as the evidence artefact; *content:* the failed-expectation list with rule IDs visible.
2. **`dq.quarantine` with steward assignment** — *why:* proves quarantine is routed work, not a bin; *content:* rows with `rule_id`, `failed_expectation`, `assigned_to`, `age_days`.
3. **The steward review queue for the 0.80–0.92 band** — *why:* the human decision must look like a real interface; *content:* two candidate records side by side with the trigram score and merge/reject buttons.

### Simulations
1. **The flattering baseline** — *Setup:* branch `sim-sentinel-blind` profiles without the sentinel list. *Expected behaviour:* completeness reports 94% against a true 71.0%, and the composite reports 88.1% against 72.4%. *Learning objective:* a quality measurement is only as honest as its definition of "missing".
2. **The over-eager merge** — *Setup:* branch `sim-automerge-080` auto-merges everything above 0.80 similarity. *Expected behaviour:* `customer_golden` lands at 57,180 rows; 82 genuinely distinct customers are merged, 14 disputes are resolved into `ACTIVE`, and one merged pair is two brothers at the same address. *Learning objective:* precision matters more than recall when the merge is destructive.

### Interactive Activities
- **Rung it (12 min):** twelve Baseerah defect cards; teams assign a remediation rung to each and defend the two that provoke argument (failed AMI meters, shared addresses).
- **Survivorship court (12 min):** two duplicate customer records printed side by side with conflicting values in eight fields; each team decides the surviving value per field and the room compares — the disagreements are exactly where a written survivorship rule is needed.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `raw.customer_account_extract` | Synthetic billing extract with 3,320 planted duplicates and 4 sentinel styles | Postgres table | 61,420 rows | Profiling, match/merge |
| `raw.meter_reading_dirty` | Synthetic reads with 24,760 impossible values and 6.1% late arrivals | Postgres table | 13,018,800 rows | Accuracy and timeliness scoring |
| `dq/expectations/baseerah_core.json` | Generated from `rules/baseerah_rules.yml` | GX suite JSON | 31 expectations | The quality gate |
| `dq/steward_task_seed.csv` | Pre-seeded steward queue with 3 aged items | CSV | 3 rows | Stewardship throughput exercise |

### Demo Requirements
- **Instructor demo (8 min):** run `sim-silent-imputation` live. Show NRW falling from 31.4% to 28.9%. Ask the room whether to celebrate. Then show the 40 Al-Ahsa properties whose meters have been stopped for eleven weeks and are still being billed. Add the flag, exclude flagged reads, and show 31.7%. Close with the module thesis verbatim: "a quality process that cannot distinguish a repaired value from a measured one will eventually improve your metrics by damaging your business."

---

# Module 7 — Data Warehouse and Dimensional Modelling: Facts, Dimensions, Star vs Snowflake, SCDs
## تصميم مستودعات البيانات والنمذجة البعدية

## Module Overview

**Purpose.** This is the module the course is named for. Participants learn what a data warehouse is and how it differs from the operational database they built on Day 3; then they design and build a dimensional model — declaring grain, separating facts from dimensions, classifying measures, choosing star over snowflake, and implementing the slowly-changing-dimension logic without which no historical report can ever be reproduced. It consolidates catalogue Modules 6 (Data Warehouse Design) and 7 (Dimensional Modelling), and it delivers the awkward dimension patterns — degenerate, junk, role-playing, bridge, late-arriving — that separate a working warehouse from a diagram.

**Business relevance.** Baseerah's regulator asks, in March, what the non-revenue-water figure was for the Al-Ahsa district in the previous October, computed with the tariff bands and DMA boundaries that were in force *then*. A warehouse without slowly-changing dimensions can only answer with today's structure applied to last October's volumes, which is a different number and a wrong one. SCD2 is not a modelling refinement; it is the difference between a warehouse that can be audited and one that cannot.

**Industry use cases.**
- A utility must reproduce a historic regulatory submission exactly, including tariff bands and district boundaries as they stood.
- A hospitality group must analyse revenue by the rate plan in force at booking time, not the rate plan in force today.
- A ministry must report headcount by the organisational structure at each reporting date across four reorganisations.

**Expected competencies.** After this module a participant can contrast OLTP and OLAP designs; apply the four-step dimensional design process; declare and defend a fact grain; classify measures as additive, semi-additive or non-additive; choose star or snowflake with justification; implement SCD types 1, 2 and 3 in SQL and as dbt snapshots; and model degenerate, junk, role-playing, conformed and bridge dimensions plus late-arriving dimension rows.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Contrast operational databases and data warehouses by purpose, structure and usage | LO7 |
| 7.2 | Apply the four-step dimensional design process and declare fact grain | LO7 |
| 7.3 | Classify measures as additive, semi-additive or non-additive and aggregate each correctly | LO7 |
| 7.4 | Choose between star and snowflake with a stated justification | LO7, LO4 |
| 7.5 | Implement SCD types 1, 2 and 3 and handle late-arriving dimensions | LO7 |
| 7.6 | Model degenerate, junk, role-playing, conformed and bridge dimensions | LO7, LO3 |

## Technical Content

### 1. Operational database versus data warehouse

| Aspect | Operational (`core`, OLTP) | Warehouse (`mart`, OLAP) |
|---|---|---|
| Purpose | Run the business | Understand the business |
| Unit of work | One transaction, one row | One question, millions of rows |
| Design goal | Write correctness, minimum redundancy | Read simplicity and speed |
| Normal form | 3NF/BCNF | Dimensional (deliberately denormalised) |
| Time | Current state | Full history, versioned |
| Update pattern | In place | Append and version; never edited by a user |
| Typical query | "Meter M-4471's last reading" | "Consumption by district by month by tariff band for 3 years" |
| Users | Applications | Analysts, dashboards, regulators |
| Volatility | Constant writes | Batch loads on a schedule |

Two design philosophies dominate. **Inmon** builds a normalised enterprise warehouse first, then dependent dimensional marts — slower to first value, stronger for enterprise integration. **Kimball** builds conformed dimensional marts directly on a bus matrix — faster to value, and the approach this course teaches. Baseerah takes a pragmatic hybrid, which is what most utilities actually run: a 3NF `core` (Inmon-flavoured, built in Module 5) as the integrated source of truth, and Kimball star schemas in `mart` built from it. The Module 4 denormalisation decision record is precisely the bridge between the two.

The warehouse components map to the layers participants already have: **sources** (four systems) → **extraction and staging** (`raw`, `stg`) → **integration** (`core`) → **presentation** (`mart`) → **analytical layer** (semantic model and dashboards, Module 8).

### 2. The four-step design process, and grain above all

1. **Select the business process.** Not a report, a *process*: metering, billing, field maintenance, network balancing. A process has events, and events become facts.
2. **Declare the grain.** One sentence, in business language, stating what one row of the fact table represents. Do this before choosing dimensions or measures. Everything downstream is determined by it.
3. **Identify the dimensions.** Everything you would put after "by": by district, by month, by tariff band, by meter type.
4. **Identify the facts.** The numeric measurements that are true at that grain.

Baseerah's five facts, with grain declared verbatim:

| Fact table | Grain (one row =) | Rows | Type |
|---|---|---|---|
| `fct_meter_read_hourly` | one meter, one hour, one read channel | 13,018,800 | transaction |
| `fct_billing_line` | one invoice line (one invoice, one tariff block) | 486,300 | transaction |
| `fct_work_order` | one completed work order | 184,600 | accumulating snapshot |
| `fct_network_balance_daily` | one DMA, one calendar day | 3,690 | periodic snapshot |
| `fct_meter_inspection` | one meter, one inspection campaign | 42,800 | **factless** |

Grain errors are the most expensive dimensional modelling defect and the hardest to unwind, because every downstream query encodes the assumption. Two Baseerah rules: a fact table has **exactly one** grain — mixing hourly AMI reads and monthly manual reads in one table without a grain-distinguishing dimension makes `SUM(volume_m3)` meaningless — and **the grain is stated in the table comment**, so nobody has to reverse-engineer it from a `GROUP BY`.

### 3. Measures: additive, semi-additive, non-additive

| Class | Definition | Baseerah examples | Aggregation rule |
|---|---|---|---|
| **Additive** | Summable across every dimension | `volume_m3`, `line_amount_sar`, `leak_repair_count` | `SUM` freely |
| **Semi-additive** | Summable across some dimensions but not time | `index_m3` (cumulative meter odometer), `reservoir_level_m`, `account_balance_sar` | `SUM` across meters at a point in time; `LAST_VALUE` or `AVG` across time |
| **Non-additive** | Not summable at all; a ratio | `nrw_pct`, `collection_rate_pct`, `avg_pressure_bar` | Store the numerator and denominator as additive facts; compute the ratio at query time |

The non-additive rule is the one that gets violated. Storing `nrw_pct` per DMA per day and then averaging it across 41 DMAs gives the *unweighted* mean of percentages, which is not the district NRW — it over-weights small DMAs. Baseerah's `fct_network_balance_daily` therefore stores `input_volume_m3` and `billed_volume_m3` as additive facts and defines NRW in the semantic layer as `SUM(input) - SUM(billed)) / SUM(input)`. That single decision is why the district figure reconciles with the sum of its parts.

The semi-additive case is equally concrete: summing `index_m3` across hours for one meter produces a number in the billions with no physical meaning — the Module 1 walkthrough defect, now formally classified.

### 4. Star versus snowflake

A **star** keeps each dimension in one flat table. A **snowflake** normalises dimension hierarchies into sub-tables (`dim_service_point → dim_district → dim_region`).

| | Star | Snowflake |
|---|---|---|
| Dimension tables | One per dimension, denormalised | Normalised into hierarchy tables |
| Joins for a typical query | 1 per dimension | 2–4 per dimension |
| Query simplicity | High; BI tools model it natively | Lower; users must know the hierarchy |
| Storage | Slightly larger | Slightly smaller |
| Hierarchy change handling | Rebuild the dimension | Update one row |
| When to prefer | Almost always | Very large, volatile, or genuinely shared hierarchies |

Baseerah is a star. The saving from snowflaking `dim_service_point` is 64,800 rows × ~60 bytes of repeated district text ≈ 3.9 MB — irrelevant against a 13-million-row fact table — while the cost is an extra join on every field-operations query and a semantic model most Power BI users will build incorrectly. The one deliberate exception is `dim_tariff_block`, kept separate from `dim_tariff` because the block structure is a genuine one-to-many that would otherwise force `fct_billing_line` to a different grain.

### 5. Slowly changing dimensions

A customer moves from tariff RES-A to RES-B. What should last quarter's report show?

| Type | Behaviour | History | Baseerah use | Cost |
|---|---|---|---|---|
| **Type 0** | Retain original, never change | Original only | `opened_on` | None |
| **Type 1** | Overwrite | None | Corrections: a misspelled name | Restates history silently |
| **Type 2** | New row, versioned with `valid_from`/`valid_to`/`is_current` | Full | `dim_customer`, `dim_meter`, `dim_service_point` | Dimension grows; every fact must carry the *surrogate* key |
| **Type 3** | Add a prior-value column | One step back | `dim_tariff.prior_rate_sar_per_m3` | Only one change remembered |
| **Type 6** | 1 + 2 + 3 combined | Full + current-value column | Not used at Baseerah | Complexity |

**Type 2 is the default for anything a regulator may ask about historically.** Its non-negotiable companion rule: the fact table must store the dimension's **surrogate key at the time of the event**, not the natural key. If `fct_billing_line` stores `account_no`, joining to `dim_customer` returns every version and fans out the invoice total; if it stores `customer_sk` resolved at load time, the invoice joins to exactly the customer version that was in force. This is the single most common SCD2 implementation error and it inflates revenue figures rather than deflating them, which means nobody complains until an auditor does.

**Late-arriving dimensions** are the operational reality that breaks naive SCD2. A meter reading for meter `M-88214` arrives at 02:00 but the meter's registration record does not reach `core` until 06:00. Three options, and Baseerah uses the third: reject the fact (loses data); hold it in a suspense table (adds a state machine); or **insert an inferred dimension member** — a `dim_meter` row with the natural key, `is_inferred = true`, and unknown attributes — then let the real record update it via the normal SCD2 path. The fact keeps its correct surrogate key and nothing is lost.

### 6. The awkward dimensions

- **Degenerate dimension.** `work_order_no` and `invoice_no` are dimension-like attributes with no other attributes of their own. They live *in the fact table* as plain columns. Creating `dim_invoice(invoice_sk, invoice_no)` adds a join and stores nothing.
- **Junk dimension.** `fct_meter_read_hourly` has four low-cardinality flags: `read_channel` (4), `reading_type` (2), `is_estimated` (2), `quality_flag` (3). Rather than four columns on 13 million rows, build `dim_read_flag` with all 48 combinations and store one `read_flag_sk`. Saves storage, and gives the BI tool a single tidy attribute group.
- **Role-playing dimension.** `dim_date` is joined three times to `fct_work_order` — as raised date, scheduled date, and closed date. One physical table, three views (`vw_dim_date_raised`, …) so the BI model shows three clearly named date dimensions.
- **Conformed dimension.** `dim_date`, `dim_dma` and `dim_customer` are shared identically by several facts. This is what makes "billed volume by DMA by month" and "leak repairs by DMA by month" comparable on one chart. A dimension that is *nearly* conformed — same name, different keys — is worse than no conformity at all, because it produces charts that look joinable and are not.
- **Bridge table.** `bridge_account_meter` resolves the mixed-use many-to-many from Module 3, carrying `share_pct` as a weighting factor. Any query joining through a bridge must multiply by the weight or it double-counts: 62 shared meters in the sample inflate billed volume by 4.1% if the weighting is forgotten.
- **Factless fact.** `fct_meter_inspection` records that an inspection happened, with no measure. It answers coverage questions ("which meters were *not* inspected in campaign 2026-Q2?") that no measure-bearing fact can, because it is the absence that matters.

### 7. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Declare grain in one sentence before anything else,* and put it in the table comment.
- *Never store a ratio as a fact;* store its numerator and denominator.
- *Facts carry surrogate keys resolved at event time,* never natural keys.
- *Conform or do not share.* Two dimensions with the same name and different keys are a trap.
- *Every bridge join carries its weight,* enforced by a test that the weights sum to 1.

**Common mistakes (each appears in the Lab 7 starter deliberately)**
1. Mixing hourly AMI reads and monthly manual reads in one fact table with no grain-distinguishing dimension, making `SUM(volume_m3)` a nonsense figure.
2. Storing `nrw_pct` as a fact and averaging it across DMAs, over-weighting small DMAs by 3.8 points.
3. Joining `fct_billing_line` to `dim_customer` on `account_no` under SCD2, fanning out invoice totals by the number of versions (district revenue inflates from SAR 41.2M to SAR 44.9M).
4. Snowflaking `dim_service_point` into four hierarchy tables for a 3.9 MB saving and a four-join query.
5. Forgetting the bridge weight, inflating billed volume by 4.1% and understating NRW by 1.3 points.
6. Rejecting facts whose dimension row has not yet arrived, silently dropping 1,140 readings a day for new meters.

**Production considerations**
- Build `dim_date` once, out to 2030, with fiscal periods, Hijri date, Ramadan and Eid flags, and weekend flags set for the Saudi Friday–Saturday weekend. Consumption behaviour changes materially in Ramadan and any seasonality analysis that ignores it is wrong.
- Never let a user or an application write to `mart`. One writer — the ELT pipeline — is the protection that makes the denormalisation safe (Module 4, DD-002).
- Reconcile every fact table to its `core` source on every run: row count, and the sum of each additive measure. A mart that silently diverges from core is worse than no mart.

### 8. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's regulator requested a restatement of the Al-Ahsa NRW figure for the previous October. The warehouse returned 26.8%; the original submission had said 29.3%. Neither the volumes nor the code had changed. The cause was that three DMA boundaries had been redrawn in December, and `dim_dma` was Type 1 — overwritten. Every historical query now assigned October's meters to December's DMAs. The warehouse was not wrong about today; it had silently rewritten the past. Converting `dim_dma` to Type 2 and reloading from the `core` history restored 29.3%, and the fix took two days. The regulator's follow-up question was the more expensive one: "which other figures have you restated without knowing?"

## Code Examples

### SCD Type 2 as a dbt snapshot, and the fact that resolves the correct version

```sql
-- snapshots/scd2_customer.sql
--
-- WHY: dim_customer must answer "who was this customer, and on which tariff,
-- in October?" -- not "who are they now". dbt's snapshot materialisation
-- implements SCD2 with valid_from/valid_to/is_current maintained for us, and
-- (critically) it is idempotent: re-running it on unchanged data creates no
-- new versions. Strategy is `check` rather than `timestamp` because the
-- billing CRM's updated_at is unreliable -- 12% of rows carry the migration
-- date rather than a real change date.

{% snapshot scd2_customer %}
{{
    config(
      target_schema='mart',
      unique_key='customer_id',
      strategy='check',
      check_cols=['customer_category', 'tariff_code', 'account_status',
                  'national_address', 'dma_id'],
      invalidate_hard_deletes=True
    )
}}

select
    customer_id,                 -- natural/business key from core.customer_golden
    account_no,
    customer_category,
    tariff_code,
    account_status,
    national_address,
    dma_id,
    opened_on,
    -- PDPL: holder_national_id is deliberately ABSENT. The dimension is read
    -- by the BI layer; the national ID never leaves core. Name is masked to
    -- initial + family name for the same reason.
    core.mask_holder_name(holder_name) as holder_name_masked
from {{ source('core', 'customer_golden') }}

{% endsnapshot %}
```

```sql
-- models/marts/dim_customer.sql
--
-- WHY: the snapshot gives us versions; this model gives us a conformed
-- dimension with a stable surrogate key, an "unknown member" for late-arriving
-- facts, and the is_current flag the BI layer filters on. Row count: 61,940
-- versions for 58,100 customers (3,840 changes captured over 12 months).

{{ config(materialized='table', unique_key='customer_sk') }}

with versions as (

    select
        -- Surrogate key: stable hash of the natural key plus the version start.
        -- A hash (not a sequence) so a full rebuild reproduces identical keys
        -- and the fact tables do not have to be reloaded.
        {{ dbt_utils.generate_surrogate_key(['customer_id', 'dbt_valid_from']) }}
            as customer_sk,
        customer_id,
        account_no,
        customer_category,
        tariff_code,
        account_status,
        national_address,
        dma_id,
        opened_on,
        holder_name_masked,
        dbt_valid_from                                as valid_from,
        coalesce(dbt_valid_to, timestamp '9999-12-31') as valid_to,
        (dbt_valid_to is null)                        as is_current,
        false                                         as is_inferred
    from {{ ref('scd2_customer') }}

),

-- The "unknown member". Every conformed dimension needs one so that a fact
-- whose dimension row has not yet arrived can still load with a valid FK.
-- Without it the loader must either reject the fact or write a NULL key, and
-- both lose data. Key -1 by convention across every Baseerah dimension.
unknown_member as (

    select
        '-1'                    as customer_sk,
        -1                      as customer_id,
        'UNKNOWN'               as account_no,
        'UNKNOWN'               as customer_category,
        'UNKNOWN'               as tariff_code,
        'UNKNOWN'               as account_status,
        null                    as national_address,
        -1                      as dma_id,
        null::date              as opened_on,
        'UNKNOWN'               as holder_name_masked,
        timestamp '1900-01-01'  as valid_from,
        timestamp '9999-12-31'  as valid_to,
        true                    as is_current,
        true                    as is_inferred

)

select * from versions
union all
select * from unknown_member
```

```sql
-- models/marts/fct_billing_line.sql
--
-- WHY: this model contains the single most important join in the whole
-- warehouse and the most commonly botched one. Under SCD2, joining on the
-- NATURAL key (account_no) returns every version of the customer and fans out
-- the invoice: district revenue inflates from SAR 41.2M to SAR 44.9M and no
-- error is raised. We resolve the surrogate key that was IN FORCE at the
-- invoice date, using a range join on the dimension's validity window.
--
-- Grain: one invoice line = one invoice, one tariff block. 486,300 rows.

{{ config(
     materialized='incremental',
     unique_key=['invoice_no', 'block_no'],
     incremental_strategy='delete+insert',
     partition_by={'field': 'invoice_date', 'granularity': 'month'}
) }}

with lines as (

    select
        il.invoice_no,          -- DEGENERATE dimension: lives in the fact,
        il.block_no,            -- no dim_invoice table, nothing to store there
        il.account_no,
        il.invoice_date,
        il.consumed_m3,
        il.line_amount_sar
    from {{ source('core', 'invoice_line') }} as il
    {% if is_incremental() %}
      -- 5-day lookback: billing corrections routinely restate the prior week.
      where il.invoice_date >= (select max(invoice_date) - interval '5 days'
                                from {{ this }})
    {% endif %}

),

resolved as (

    select
        l.invoice_no,
        l.block_no,
        -- THE SCD2 RANGE JOIN. coalesce to the unknown member (-1) so a
        -- late-arriving customer never causes the fact to be dropped.
        coalesce(dc.customer_sk, '-1')          as customer_sk,
        coalesce(dt.tariff_sk,   '-1')          as tariff_sk,
        dd.date_sk                              as invoice_date_sk,
        l.invoice_date,
        -- ADDITIVE measures only. nrw_pct and collection_rate are ratios and
        -- are computed in the semantic layer from these numerators/denominators.
        l.consumed_m3                           as billed_volume_m3,
        l.line_amount_sar                       as billed_amount_sar
    from lines as l
    left join {{ ref('dim_customer') }} as dc
           on  dc.account_no  = l.account_no
           -- the version in force AT THE INVOICE DATE, not the current one
           and l.invoice_date >= dc.valid_from::date
           and l.invoice_date <  dc.valid_to::date
    left join {{ ref('dim_tariff') }} as dt
           on  dt.tariff_code = dc.tariff_code
           and l.invoice_date >= dt.valid_from::date
           and l.invoice_date <  dt.valid_to::date
    left join {{ ref('dim_date') }} as dd
           on  dd.date_day = l.invoice_date

)

select * from resolved
```

### The bridge, the junk dimension, and the weighting test

```sql
-- models/marts/bridge_account_meter.sql
--
-- WHY: 62 mixed-use meters are shared between two or more accounts (the M:N
-- resolved in Module 3). Any query joining billed volume through a shared
-- meter MUST multiply by share_weight or it double-counts: forgetting the
-- weight inflates district billed volume by 4.1% and understates the NRW
-- figure by 1.3 percentage points. The accompanying dbt test asserts that
-- weights sum to exactly 1.0 per meter per period, which makes the error
-- impossible to ship rather than merely discouraged.

{{ config(materialized='table') }}

select
    {{ dbt_utils.generate_surrogate_key(['ams.meter_id', 'ams.valid_from']) }}
        as bridge_sk,
    dm.meter_sk,
    dc.customer_sk,
    ams.valid_from,
    ams.valid_to,
    -- share_pct is a RELATIONSHIP attribute (Module 3). Stored as a weight in
    -- [0,1] so consuming queries can multiply directly.
    (ams.share_pct / 100.0)::numeric(6,5) as share_weight
from {{ source('core', 'account_meter_share') }} as ams
join {{ ref('dim_meter') }} as dm
      on  dm.meter_id  = ams.meter_id
      and ams.valid_from >= dm.valid_from and ams.valid_from < dm.valid_to
join {{ ref('dim_customer') }} as dc
      on  dc.customer_id = ams.account_id
      and ams.valid_from >= dc.valid_from and ams.valid_from < dc.valid_to
```

```yaml
# models/marts/marts.yml
#
# WHY: dimensional correctness is not self-evident from the SQL. These tests
# encode the three invariants that, when broken, produce plausible-looking
# wrong numbers rather than errors: bridge weights summing to 1, grain
# uniqueness, and referential completeness against the unknown member.

version: 2

models:
  - name: fct_meter_read_hourly
    description: >
      GRAIN: one meter, one hour, one read channel. 13,018,800 rows.
      Additive: volume_m3. Semi-additive: index_m3 (never SUM across time).
    tests:
      # Grain is an assertion, not a comment. This test is the grain.
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns: [meter_sk, read_hour_sk, read_flag_sk]
    columns:
      - name: read_flag_sk
        description: "JUNK dimension: read_channel x reading_type x is_estimated x quality_flag = 48 members"
        tests:
          - relationships:
              to: ref('dim_read_flag')
              field: read_flag_sk
      - name: index_m3
        description: "SEMI-ADDITIVE cumulative odometer. Aggregate with LAST_VALUE across time, SUM across meters at an instant."

  - name: bridge_account_meter
    tests:
      # The invariant that prevents the 4.1% double-count.
      - dbt_utils.expression_is_true:
          expression: "share_weight > 0 and share_weight <= 1"
      - assert_bridge_weights_sum_to_one:
          group_by: [meter_sk, valid_from]

  - name: fct_network_balance_daily
    description: >
      GRAIN: one DMA, one calendar day. 3,690 rows (41 DMAs x 90 days).
      Stores input_volume_m3 and billed_volume_m3 as ADDITIVE facts.
      nrw_pct is NON-ADDITIVE and is therefore NOT stored here -- it is
      defined once in the semantic layer as
      (SUM(input) - SUM(billed)) / SUM(input).
    columns:
      - name: input_volume_m3
        tests: [not_null, dbt_utils.expression_is_true: {expression: ">= 0"}]
      - name: nrw_pct
        # Deliberately absent. If a reviewer adds it, this test fails the build.
        tests:
          - column_does_not_exist
```

## Hands-on Lab 7 — Build the Baseerah Star Schema

| | |
|---|---|
| **Objective** | Declare grain for five facts, build nine dimensions including SCD2 on customer and meter, implement the junk, degenerate, bridge and factless patterns, and prove that a historic restatement returns the same figure it did at the time |
| **Duration** | 100 minutes (Lab 7a: 50 min, Lab 7b: 50 min) |
| **Setup** | PostgreSQL 16 with `core` populated and deduplicated from Lab 6, `pip install dbt-postgres==1.7.* dbt-utils`, course repo, `git checkout lab7-start` |

**Instructions & tasks**

1. *(10 min)* **7a.** Write the grain sentence for all five fact tables into `models/marts/marts.yml` table descriptions. Have your pair read each aloud; if it needs two sentences, the grain is wrong. Fix the planted defect in `fct_meter_read_hourly`, which currently mixes hourly and monthly reads.
2. *(15 min)* **7a.** Build the four base dimensions: `dim_date` (2,557 rows, 2024–2030, with Hijri date, Ramadan and Eid flags, Friday–Saturday weekend), `dim_dma` (41), `dim_service_point` (64,800), `dim_read_flag` (48 junk members). Run `dbt build --select dim_*`.
3. *(15 min)* **7a.** Load `fct_meter_read_hourly` (13,018,800 rows) resolving `read_flag_sk` from the junk dimension. Confirm the grain test passes and that `index_m3` is documented as semi-additive.
4. *(10 min)* **7a.** Load `fct_network_balance_daily` (3,690 rows) with `input_volume_m3` and `billed_volume_m3` as additive facts. Confirm `nrw_pct` is *not* a column and that the `column_does_not_exist` test passes. Commit: `feat(mart): base dimensions + hourly reads + network balance facts`.
5. *(20 min)* **7b.** Implement the SCD2 snapshot for `dim_customer` and `dim_meter`. Run it twice against unchanged data and confirm no new versions are created (idempotency). Then apply `fixtures/tariff_change_2026-05.sql` and confirm `dim_customer` grows from 58,101 to 61,940 rows.
6. *(15 min)* **7b.** Build `fct_billing_line` with the SCD2 range join, `bridge_account_meter` with weights, and the factless `fct_meter_inspection`. Fix the planted natural-key join defect and confirm district revenue is SAR 41.2M, not SAR 44.9M.
7. *(15 min)* **7b.** Run the historic restatement test: compute Al-Ahsa NRW for the prior period with today's dimensions (Type 1 behaviour) and with SCD2, and record both figures in `LAB7_RESTATEMENT.md`. Commit: `feat(mart): SCD2 customer/meter, bridge, factless, restatement proof`.

**Expected output**
```
$ dbt build --select mart
06:14:02  1 of 16 OK created sql table model mart.dim_date .............. 2,557 rows  [0.9s]
06:14:03  2 of 16 OK created sql table model mart.dim_dma ................... 41 rows  [0.1s]
06:14:03  3 of 16 OK created sql table model mart.dim_read_flag ............. 48 rows  [0.1s]
06:14:04  4 of 16 OK snapshotted mart.scd2_customer ..................... 61,940 rows  [4.2s]
06:14:09  5 of 16 OK created sql table model mart.dim_customer ......... 61,941 rows  [1.8s]
06:14:11  6 of 16 OK created sql table model mart.dim_meter ............. 68,410 rows  [2.1s]
06:14:14  7 of 16 OK created sql table model mart.bridge_account_meter ..... 138 rows  [0.2s]
06:14:16  8 of 16 OK created incremental model mart.fct_meter_read_hourly
                                                              13,018,800 rows  [2m12s]
06:16:28  9 of 16 OK created incremental model mart.fct_billing_line ... 486,300 rows  [11.4s]
06:16:40 10 of 16 OK created sql table model mart.fct_work_order ...... 184,600 rows  [4.8s]
06:16:45 11 of 16 OK created sql table model mart.fct_network_balance_daily 3,690 rows [0.6s]
06:16:46 12 of 16 OK created sql table model mart.fct_meter_inspection . 42,800 rows  [1.2s]
06:16:47 13 of 16 PASS unique_combination fct_meter_read_hourly grain ........... [1.9s]
06:16:49 14 of 16 PASS assert_bridge_weights_sum_to_one ......................... [0.1s]
06:16:49 15 of 16 PASS column_does_not_exist fct_network_balance_daily.nrw_pct .. [0.1s]
06:16:49 16 of 16 PASS relationships fct_billing_line.customer_sk -> dim_customer [0.7s]
Done. PASS=16 WARN=0 ERROR=0 SKIP=0 TOTAL=16

$ psql -f sql/bench/restatement_check.sql
 method                          | al_ahsa_nrw_pct | district_revenue_sar
---------------------------------+-----------------+----------------------
 SCD2 (dimensions as at period)  |           29.30 |         41,204,880
 Type 1 (today's dimensions)     |           26.80 |         41,204,880
 natural-key join (defect)       |           29.30 |         44,912,190   <-- fan-out
```

**Acceptance criteria**
- Five fact tables with a one-sentence grain in the table comment; the grain uniqueness test passes on `fct_meter_read_hourly`.
- Nine dimensions built; `dim_customer` at 61,941 rows (61,940 versions + unknown member); SCD2 snapshot is idempotent on re-run.
- `bridge_account_meter` weights sum to 1.0 per meter per period; district revenue is SAR 41.2M with the surrogate-key join.
- `LAB7_RESTATEMENT.md` records 29.30% (SCD2) versus 26.80% (Type 1) and explains which is correct and why.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| District revenue is SAR 44.9M | Joined `fct_billing_line` to `dim_customer` on `account_no` | Use the surrogate key resolved by the validity range join |
| Snapshot creates new versions on every run | `strategy='timestamp'` on an unreliable `updated_at` | Use `strategy='check'` with explicit `check_cols` |
| 1,140 readings/day dropped | Facts rejected when the dimension row is absent | `coalesce(dim.sk, '-1')` to the unknown member, or insert an inferred member |
| Billed volume 4.1% high | Bridge joined without multiplying by `share_weight` | Multiply the measure by `share_weight` in every bridge-traversing query |

**Instructor notes.** Task 1 sets up the whole day: make every pair say the grain sentence out loud. The pairs who cannot do it in one sentence have a mixed-grain fact table and will fail the uniqueness test in task 3 — let that happen rather than pre-empting it. Task 6's fan-out defect is the highest-value teaching moment in the course, because the wrong number is *higher* and therefore nobody complains: put both revenue figures on the board and ask which one a finance director would query. The restatement test in task 7 is the module's thesis and directly rehearses a capstone requirement; do not let it be skipped for time. Fast finishers: implement `dim_date` role-playing views for `fct_work_order` (raised / scheduled / closed) and demonstrate all three in one query.

## Mini Exercises

**Quiz (5 questions)**
1. What must be declared before dimensions or measures are chosen? → the **grain**, in one business sentence.
2. Why must `nrw_pct` not be stored as a fact? → it is non-additive; averaging ratios across DMAs over-weights small DMAs (by 3.8 points here).
3. Which key must a fact store under SCD2, and why? → the dimension **surrogate key in force at event time**; the natural key fans the fact out across versions.
4. What is a factless fact table for? → recording that an event happened with no measure — coverage and absence questions.
5. When is a junk dimension worth building? → when several low-cardinality flags would otherwise sit on a very large fact table (48 members replacing 4 columns on 13M rows).

**Debugging exercise.** Check out `git checkout lab7-type1-dma`. `dim_dma` is Type 1 and three DMA boundaries were redrawn in December. Symptom: the October NRW figure for Al-Ahsa is 26.8% today and was 29.3% when submitted; no code or volume changed. Ask participants to diagnose the overwritten dimension, convert it to Type 2, reload from `core` history, and confirm 29.3% returns. Then discuss the regulator's follow-up question — "what else have you restated without knowing?" — and what control answers it.

**Design exercise.** The authority begins offering prepaid meters, where consumption is deducted from a purchased balance. State the grain of the new fact, classify `balance_remaining_m3` as additive, semi-additive or non-additive, decide whether it belongs in `fct_meter_read_hourly` or a new fact table, and say which existing dimensions conform to it unchanged.

**Discussion questions.**
- Your BI developer wants `dim_customer` flattened to current values only "because SCD2 confuses users". What do you concede, what do you refuse, and what is the design that satisfies both?
- Kimball or Inmon for a national utility with four source systems and a seven-year regulatory retention obligation? Argue it, then say where the hybrid Baseerah uses is actually a fudge.

## Case Study — The Rate Plan That Never Was at "Qimam" (قمم)

**Scenario.** "Qimam" (قمم), a Saudi hospitality group operating 31 hotels in Makkah, Madinah, Riyadh and AlUla, rebuilt its revenue warehouse. Three months after go-live, the finance team found that revenue attributed to the "Umrah Flexible" rate plan for the previous Hajj season had fallen from SAR 128 million in the original reports to SAR 41 million, while a plan that had not existed during that season showed SAR 94 million.

**Business context.** Rate-plan performance drives commercial strategy, distribution-channel contracts, and the pricing team's targets. Three quarters of commercial decisions had been made on the original figures, and two distribution contracts contained revenue-share clauses referencing plan-level performance.

**Technical challenge.** `dim_rate_plan` was Type 1. In the annual pricing review, twelve rate plans had been renamed, four merged, and two split. Every historical booking now pointed at the *current* plan definition, because the fact table stored `rate_plan_code` — the natural key — and the dimension had been overwritten in place. The warehouse had no memory that "Umrah Flexible" had ever existed under that definition.

**Constraints.** Bookings are made up to 400 days in advance, so a booking's rate plan may be renamed twice between booking and stay — meaning the model needs the plan as at booking date *and* as at stay date. Two distribution contracts have revenue-share clauses with a third party, so a restatement has external legal consequences. The source PMS retains only current rate-plan definitions; the history exists solely in nightly extract files kept for 18 months. PDPL applies to guest records, so any reconstruction must work from booking-level aggregates rather than guest-level exports where possible.

**Solution approach (facilitate, don't lecture).** Steer towards: (1) convert `dim_rate_plan` to Type 2 and reconstruct history from the 18 months of extract files, accepting that anything older is unrecoverable and must be documented as such; (2) store the resolved surrogate key on the booking fact at *both* booking date and stay date — this is a role-playing use of the same SCD2 dimension and is the part the room will not see unaided; (3) handle the four merges and two splits explicitly, since a split cannot be reconstructed by any automatic rule and needs a documented allocation decision; (4) notify the two distribution partners proactively with a reconciliation, because a revenue-share figure discovered to be wrong by the counterparty is a different conversation from one disclosed by you. Resist the room's instinct to "restate everything and move on": the splits require a business decision that no engineer should make alone.

**Discussion questions.**
1. Why did storing the natural key on the fact make the Type 1 dimension's damage total rather than partial?
2. A booking's rate plan may be renamed twice between booking and stay. Which SCD pattern handles that, and how many joins to the same dimension does the fact need?
3. Merges can be reconstructed automatically; splits cannot. Why, and who must decide the allocation?
4. What do you tell the two distribution partners, and when — before or after you have the corrected figures?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Star schema built | Coverage | 5 facts, 9 dimensions, 1 bridge | `dbt build --select mart` |
| Grain integrity | Correctness | 100% of facts pass grain uniqueness | `unique_combination_of_columns` |
| SCD2 correctness | Correctness | `dim_customer` 61,941 rows; snapshot idempotent on re-run | double-run diff |
| Bridge weighting | Correctness | weights sum to 1.0 for all 62 shared meters | `assert_bridge_weights_sum_to_one` |
| Historic restatement | Auditability | SCD2 reproduces 29.30%; Type 1 gives 26.80% | `restatement_check.sql` |

**Example benchmark table (filled during lab):**

| Table | Grain | Rows | Build time | Pattern demonstrated |
|---|---|---|---|---|
| `dim_date` | one calendar day | 2,557 | 0.9 s | conformed, role-playing |
| `dim_customer` | one customer version | 61,941 | 1.8 s | SCD2 + unknown member |
| `dim_meter` | one meter version | 68,410 | 2.1 s | SCD2 + inferred members |
| `dim_tariff` | one tariff | 6 | 0.1 s | SCD3 (`prior_rate_sar_per_m3`) |
| `dim_read_flag` | one flag combination | 48 | 0.1 s | junk dimension |
| `bridge_account_meter` | one account-meter-period | 138 | 0.2 s | bridge with weights |
| `fct_meter_read_hourly` | one meter, one hour, one channel | 13,018,800 | 2 m 12 s | transaction fact, semi-additive `index_m3` |
| `fct_billing_line` | one invoice line | 486,300 | 11.4 s | degenerate `invoice_no`, SCD2 range join |
| `fct_work_order` | one completed work order | 184,600 | 4.8 s | accumulating snapshot, degenerate `work_order_no` |
| `fct_network_balance_daily` | one DMA, one day | 3,690 | 0.6 s | additive numerator/denominator only |
| `fct_meter_inspection` | one meter, one campaign | 42,800 | 1.2 s | factless fact |

## Required Visuals and Training Assets

### Diagrams
1. **The Baseerah bus matrix** — *Purpose:* the module's organising artefact and the capstone's map. *Elements:* five business processes as rows, nine dimensions as columns, ticks where a dimension conforms; `dim_date`, `dim_dma` and `dim_customer` shown as conformed across three or more processes. *Style:* matrix grid, conformed dimensions highlighted. *Designer description:* "A 5×9 grid of ticks; three columns shaded to show conformity across processes."
2. **Star schema for `fct_meter_read_hourly`** — *Purpose:* the canonical star. *Elements:* central fact with grain sentence in the box, five dimensions radiating out, the junk dimension expanded to show its 48 members, `index_m3` labelled semi-additive in amber. *Style:* classic star with measure-class colour coding.
3. **SCD types 1, 2 and 3 on one customer** — *Purpose:* make the abstraction concrete. *Elements:* the same customer's tariff change shown three ways — overwritten (Type 1), two versioned rows with validity windows (Type 2), one row with a prior-value column (Type 3) — and the October report figure each produces. *Style:* three-panel with the resulting figure under each.
4. **The fan-out** — *Purpose:* the most valuable diagram in the module. *Elements:* one invoice line joining to three customer versions on the natural key, producing three rows and SAR 44.9M; beside it, the surrogate-key join producing one row and SAR 41.2M. *Style:* before/after join diagram with row multiplication drawn explicitly.

### Images (screenshots)
1. **`dbt build --select mart` full output** — *why:* the target state for Lab 7; *content:* all 16 nodes green with row counts and timings visible.
2. **`dim_customer` rows for one customer across two versions** — *why:* SCD2 must be seen as data; *content:* two rows with `valid_from`, `valid_to`, `is_current` and the differing `tariff_code`.
3. **The restatement comparison** — *why:* the audit story in one image; *content:* the three-row result grid showing 29.30 / 26.80 / the SAR 44.9M fan-out.

### Simulations
1. **The overwritten boundary** — *Setup:* branch `lab7-type1-dma` redraws three DMA boundaries against a Type 1 dimension. *Expected behaviour:* the October Al-Ahsa NRW figure silently changes from 29.3% to 26.8% with no code or data change. *Learning objective:* a Type 1 dimension rewrites the past without telling anyone.
2. **The bridge that was forgotten** — *Setup:* branch `sim-bridge-unweighted` joins billed volume through `bridge_account_meter` without multiplying by `share_weight`. *Expected behaviour:* district billed volume rises 4.1% and NRW falls 1.3 points, both in the flattering direction. *Learning objective:* bridge traversal without weighting is a silent double-count.

### Interactive Activities
- **Declare the grain (12 min):** eight described business processes; each team writes the one-sentence grain and the room votes on which are truly single-grain. Two of the eight are deliberately mixed.
- **Additive, semi-additive, or ratio? (10 min):** fourteen Baseerah measures on cards, sorted into the three classes; the arguable ones (`index_m3`, `avg_pressure_bar`, `open_work_order_count`) are the discussion.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `core.customer_golden` | Output of Lab 6 match/merge | Postgres table | 58,100 rows | SCD2 snapshot source |
| `fixtures/tariff_change_2026-05.sql` | Synthetic tariff migration affecting 3,840 customers | SQL | 3,840 updates | Triggers SCD2 versioning |
| `core.account_meter_share` | Mixed-use share extract, remediated in Lab 6 | Postgres table | 138 rows / 62 meters | Bridge table source |
| `fixtures/inspection_campaign_2026q2.csv` | Synthetic inspection coverage | CSV | 42,800 rows | Factless fact |

### Demo Requirements
- **Instructor demo (8 min):** run the natural-key join and the surrogate-key join side by side on `fct_billing_line`. Show SAR 44.9M and SAR 41.2M. Ask which one gets escalated. Then run `lab7-type1-dma` and show October's NRW figure changing by itself. Close with the regulator's question: "what else have you restated without knowing?"

---

# Module 8 — ELT into the Warehouse, Business Intelligence, Dashboards, and Definition Governance
## تكامل البيانات وذكاء الأعمال وحوكمة التعاريف

## Module Overview

**Purpose.** The final module makes the warehouse move and makes it mean something. Participants build the ELT that loads `raw → stg → core → mart` on a schedule, orchestrate it idempotently in Airflow, add a semantic layer where every KPI has exactly one definition, design an executive dashboard and a bilingual regulator report, and publish a data dictionary and business glossary generated from the database rather than typed into a document. It consolidates catalogue Modules 8 (ETL/ELT), 9 (BI and dashboards) and 10 (documentation and definition governance), leaving catalogue Module 11 to become the capstone.

**Business relevance.** A dashboard tile with two possible definitions is not a management tool; it is a meeting. Baseerah's leadership reviews six KPIs every Sunday, and the regulator receives a quarterly NRW submission that must be reproducible three years later. Both depend on the same discipline: one definition, one owner, one implementation, published where a business reader can find it. This is the module where the modelling, quality and warehousing work of the previous four days becomes a decision somebody trusts.

**Industry use cases.**
- A ports authority must publish berth-utilisation figures whose definition is identical in the board pack, the regulator return, and the operations screen.
- A utility must reproduce a three-year-old regulatory submission byte-for-byte, including the code version and the dimension state.
- A ministry must publish a data dictionary for an open-data product so external consumers do not misread units or nulls.

**Expected competencies.** After this module a participant can design extraction patterns including CDC; build dbt incremental models with correct lookback and idempotency; orchestrate a dependency-ordered DAG that is safe to re-run; define a semantic layer and a governed KPI register; design dashboards for clarity rather than density; produce a bilingual regulator report; and generate a data dictionary and business glossary automatically from database and model metadata.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 8.1 | Contrast ETL and ELT and choose extraction patterns including CDC | LO8 |
| 8.2 | Build idempotent incremental dbt models with correct lookback windows | LO8, LO7 |
| 8.3 | Orchestrate a dependency-ordered, re-runnable pipeline in Airflow | LO8 |
| 8.4 | Define KPIs in a governed register with one owner and one implementation | LO8, LO2 |
| 8.5 | Design dashboards and a bilingual regulator report for clarity and auditability | LO8 |
| 8.6 | Generate a data dictionary and business glossary from live metadata | LO8, LO1 |

## Technical Content

### 1. ETL, ELT, and how data actually leaves a source system

**ETL** transforms in a separate engine before loading; **ELT** loads raw first and transforms inside the warehouse. ELT wins where the warehouse has elastic compute and where reprocessing matters — and reprocessing matters enormously at Baseerah, because a rule change in Module 2 must be reapplied to history, which is only possible if the raw landing is retained.

| | ETL | ELT |
|---|---|---|
| Transform location | Separate engine | Inside the warehouse |
| Raw retained? | Usually not | Always (`raw` schema) |
| Reprocessing a rule change | Re-extract from source | Re-run SQL over retained raw |
| Skills required | Tool-specific | SQL |
| Fits Baseerah because | — | rule changes are frequent; regulator asks about history |

Extraction patterns, in increasing order of sophistication:

- **Full extract** — simple, safe, and correct for small slow-changing sources. Baseerah uses it for `tariff` (6 rows) and `dma` (41 rows).
- **Incremental by watermark** — `WHERE updated_at > last_run`. Fast, but misses hard deletes and depends on a trustworthy `updated_at`. Baseerah's billing CRM sets `updated_at` to the migration date on 12% of rows, which is exactly why the SCD2 snapshot in Module 7 uses `check` rather than `timestamp` strategy.
- **CDC (change data capture)** — read the source's transaction log. Captures deletes and true change order, at the cost of source-side configuration. Baseerah uses log-based CDC only for the billing CRM, whose deletes matter (an account closure is a real event).
- **Append-only streams** — SCADA telemetry, which never updates, only appends. The simplest and most reliable pattern, and the reason the reading table can be BRIN-indexed and time-partitioned.

### 2. Incremental models, lookback, and idempotency

An incremental model that filters `WHERE read_ts >= (SELECT max(read_ts) FROM this)` is wrong in a way that takes months to surface: late-arriving data is never picked up. Baseerah's AMI feed delivers 6.1% of readings more than 24 hours late (the Module 6 timeliness figure), so a strict high-watermark filter silently loses them.

The fix is a **lookback window** wider than the observed lateness, combined with a `merge` or `delete+insert` strategy so re-processing the window is idempotent. Baseerah uses 72 hours for readings (covering 99.4% of observed lateness) and 5 days for billing lines (covering routine billing corrections). Full-refresh for `fct_meter_read_hourly` takes 2 m 12 s; an incremental run with the 72-hour lookback takes 8.4 s.

**Idempotency is the property that makes an orchestrated pipeline operable.** Re-running yesterday's load must produce the same result, not double it. Test it deliberately: run the DAG twice and assert identical row counts and identical measure sums. If that test does not exist, the on-call engineer at 02:00 cannot safely retry anything.

### 3. Orchestration

The Baseerah DAG is one dependency-ordered graph, runnable with one command:

```
extract_billing ─┐
extract_scada   ─┼─► load_raw ─► dq_gate ─► build_core ─► snapshot_scd2 ─► build_mart ─► reconcile ─► publish_dictionary
extract_workorder┤                  │
extract_finance ─┘                  └─► quarantine + steward tasks
```

Three operational rules: the quality gate sits at the `raw → core` promotion (fail fast on structural defects, quarantine value defects); the reconciliation step runs *after* the mart and compares every additive measure against `core`; and the dictionary publication runs last, so documentation can never describe a state the warehouse is not in.

### 4. The semantic layer and KPI governance

A **semantic layer** is where a business concept is defined once, in one place, in terms of the star schema — and every consumer reads it from there. Without it, the same KPI is re-implemented in each dashboard, each report, and each analyst's spreadsheet, and they diverge. This is the failure Module 1 opened with and Module 2 escalated as GOV-001.

Baseerah's KPI register carries, for every KPI: an ID, an English and Arabic name, a one-sentence definition, the owner, the exact SQL, the fact and dimensions it reads, the aggregation class of each measure, the refresh cadence, and the rule IDs it implements. Twelve KPIs are governed; the six on the executive dashboard are:

| KPI | Definition (governed) | Class | Owner |
|---|---|---|---|
| `nrw_pct` | `(SUM(input_volume_m3) − SUM(billed_volume_m3)) / SUM(input_volume_m3) × 100`, DMA-day grain aggregated | non-additive ratio | Network Operations |
| `registered_customer_count` | accounts where `account_status = 'ACTIVE'` at the reporting date (R-021) | additive count | Billing |
| `supplied_customer_count` | distinct accounts with `SUM(volume_m3) > 0` in the quarter (R-022) | additive count | Network Operations |
| `billed_volume_m3` | `SUM(billed_volume_m3)` from `fct_billing_line`, bridge-weighted | additive | Billing |
| `collection_rate_pct` | `SUM(collected_sar) / SUM(billed_amount_sar) × 100` | non-additive ratio | Finance |
| `mean_repair_hours` | `SUM(repair_hours) / COUNT(work_order)` on closed leak repairs | non-additive ratio | Field Operations |

The two customer counts are the whole governance lesson made permanent. **The term "active customer" is banned from every Baseerah artefact**, because it has two legitimate meanings owned by two directorates. A tile that renders `registered_customer_count` says so on its face. This is not pedantry; it is the control that prevents the SAR 220 million decision from freezing again.

### 5. Dashboard design for a decision, not a display

Six principles, each with a Baseerah application:

1. **One question per tile.** If a tile answers two, it answers neither well.
2. **Name the measure on the tile,** not a friendly abbreviation. "Registered customers (R-021)" beats "Customers".
3. **Show the comparison the decision needs** — target, prior period, or peer DMA. A bare number is unreadable.
4. **Aggregate before you expose.** Meter-level consumption is PDPL personal data; the executive dashboard never renders below DMA grain, and the field-operations layer applies row-level security by district.
5. **Make staleness visible.** A "data as at" stamp driven by the pipeline's actual completion time, not the dashboard's render time.
6. **Order by decision, not by data source.** The Sunday review runs NRW → billed volume → collection rate → repairs; the layout follows that sequence.

The **regulator NRW report** adds two requirements the dashboard does not have: it is **bilingual** (Arabic and English column headers and labels, since it is read by both the authority's board and the regulator's technical staff), and it is **reproducible** — every submission stores the dbt invocation ID, the git commit SHA, the dimension snapshot timestamp, and the DQ composite score at the time of generation. Three years later, "what was the figure and how was it computed?" has a complete answer.

### 6. Documentation generated, not written

A data dictionary maintained by hand is out of date the week it is published. Baseerah generates it by joining `information_schema` (technical metadata) to `meta.entity_definition` and `meta.attribute_definition` (business metadata from Module 1) to the dbt manifest (lineage), and publishes it as part of the DAG. The build fails if a `core` or `mart` table has no definition — the Module 1 `check_definitions.py` gate, now enforcing at the end of the pipeline as well as in CI.

The **business glossary** is the bilingual sibling: business terms with English and Arabic definitions, the owner, the KPI or attribute that implements the term, and the banned-term list (`active customer`, `consumption` used without specifying index or delta, `revenue` used without specifying billed or collected).

### 7. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *One definition, one owner, one implementation.* Everything else is negotiable.
- *Lookback wider than observed lateness,* measured, not guessed.
- *Idempotency is tested, not assumed* — run the DAG twice in CI.
- *Aggregate before exposing personal data,* by design rather than by dashboard filter.
- *Documentation is generated at the end of the pipeline,* so it cannot describe a state that does not exist.

**Common mistakes (each appears in the Lab 8 starter deliberately)**
1. A strict `max(read_ts)` incremental filter, losing 6.1% of readings to lateness with no error.
2. A dashboard tile labelled "Customers" that silently renders `supplied_customer_count` while the board believes it is the registered base — the GOV-001 defect resurfacing at the presentation layer.
3. `nrw_pct` averaged across DMAs in the BI tool rather than computed from summed numerator and denominator, over-stating district NRW by 3.8 points.
4. A meter-level drill-through on the executive dashboard, exposing household consumption curves to users with no need for them — a PDPL breach in a Power BI click.
5. A hand-maintained data dictionary that diverges from the schema within two sprints.
6. A pipeline that is not idempotent, so the on-call retry double-loads 486,300 billing lines.

**Production considerations**
- Pin the dbt and Airflow versions and record the invocation ID with every published figure. Reproducibility is a version problem before it is a data problem.
- Set row-level security in the BI tool from a governed mapping table, not from hand-maintained groups; the field-operations layer must show a supervisor only their districts.
- Alert on the *reconciliation* step, not just on task failure. A DAG that succeeds while the mart diverges from core is the dangerous case.

### 8. Real-world example walkthrough

Narrate this (5 minutes). Baseerah's first executive dashboard shipped with a tile labelled "Customers: 49,780". The board read it as the registered base and asked why 8,000 customers had disappeared since the last quarter. Nobody had disappeared: the tile rendered `supplied_customer_count`, the network-operations definition, because that was the query the BI developer had been handed. Two weeks of investigation, one escalation, and a directorate-level argument later, the fix was to rename the tile "Supplied customers (R-022)" and add a second tile "Registered customers (R-021): 58,100". Both numbers had always been correct. The entire cost — roughly 40 person-days and a great deal of credibility — was incurred because a label was shorter than a definition.

## Code Examples

### The incremental fact model with a measured lookback

```sql
-- models/marts/fct_meter_read_hourly.sql
--
-- WHY: 6.1% of AMI readings arrive more than 24 hours late (the Module 6
-- timeliness measurement). A strict `where read_ts > max(read_ts)` filter
-- would silently drop every one of them -- no error, no failed test, just a
-- district consumption figure that is quietly 6% light and an NRW figure that
-- is quietly 4 points high.
--
-- The 72-hour lookback covers 99.4% of observed lateness. Combined with
-- delete+insert on the natural grain, re-processing the window is IDEMPOTENT:
-- running the DAG twice produces identical row counts and identical sums,
-- which is what makes an 02:00 retry safe.
--
-- Grain: one meter, one hour, one read channel. 13,018,800 rows.
-- Full refresh: 2 m 12 s. Incremental with lookback: 8.4 s.

{{ config(
     materialized='incremental',
     unique_key=['meter_sk', 'read_hour_sk', 'read_flag_sk'],
     incremental_strategy='delete+insert',
     on_schema_change='fail'
) }}

with source_reads as (

    select
        r.meter_id,
        date_trunc('hour', r.read_ts) as read_hour,
        r.read_channel,
        r.reading_type,
        r.is_estimated,
        r.quality_flag,
        r.volume_m3,
        r.index_m3
    from {{ source('core', 'meter_reading') }} as r
    where r.reading_type = 'delta'   -- index rows feed a separate semi-additive model

    {% if is_incremental() %}
      -- 72-hour lookback, NOT a strict high watermark. The partition key is in
      -- the predicate so PostgreSQL prunes to the affected monthly partitions.
      and r.read_ts >= (select max(read_hour) - interval '72 hours' from {{ this }})
    {% endif %}

),

keyed as (

    select
        -- Surrogate keys resolved against the SCD2 version in force AT READ TIME.
        -- coalesce to the unknown member so a late-arriving meter registration
        -- never causes a reading to be dropped (Module 7, late-arriving dims).
        coalesce(dm.meter_sk, '-1')                       as meter_sk,
        dh.date_hour_sk                                   as read_hour_sk,
        drf.read_flag_sk                                  as read_flag_sk,
        coalesce(dsp.service_point_sk, '-1')              as service_point_sk,
        coalesce(dd.dma_sk, '-1')                         as dma_sk,
        sr.read_hour,
        -- ADDITIVE
        sum(sr.volume_m3)                                 as volume_m3,
        -- SEMI-ADDITIVE: last value in the hour, never summed across time
        max(sr.index_m3)                                  as index_m3,
        count(*)                                          as read_count
    from source_reads as sr
    join {{ ref('dim_meter') }} as dm
          on  dm.meter_id = sr.meter_id
          and sr.read_hour >= dm.valid_from and sr.read_hour < dm.valid_to
    join {{ ref('dim_date_hour') }} as dh
          on  dh.date_hour = sr.read_hour
    -- JUNK dimension: 4 flags collapsed into one 48-member key rather than
    -- four columns on 13 million rows.
    join {{ ref('dim_read_flag') }} as drf
          on  drf.read_channel  = sr.read_channel
          and drf.reading_type  = sr.reading_type
          and drf.is_estimated  = sr.is_estimated
          and drf.quality_flag  = sr.quality_flag
    left join {{ ref('dim_service_point') }} as dsp
          on  dsp.service_point_id = dm.service_point_id
          and sr.read_hour >= dsp.valid_from and sr.read_hour < dsp.valid_to
    left join {{ ref('dim_dma') }} as dd
          on  dd.dma_id = dsp.dma_id
          and sr.read_hour >= dd.valid_from and sr.read_hour < dd.valid_to
    group by 1, 2, 3, 4, 5, 6

)

select * from keyed
```

### The governed KPI register and the semantic layer built from it

```yaml
# semantic/kpi_register.yml
#
# WHY: this file is the reason two directorates can read the same dashboard.
# Every KPI has ONE definition, ONE owner and ONE implementation; the semantic
# layer and the dashboard both read from here, so a definition cannot be
# re-implemented differently in a BI tool. The banned_terms list is enforced by
# a lint that fails the build if a dashboard label or a model description uses
# an ambiguous term.

version: 2.1
register_owner: data.governance@baseerah.gov.sa

banned_terms:
  - term: "active customer"
    reason: "Two legitimate meanings owned by two directorates (GOV-001)."
    use_instead: ["registered_customer_count (R-021)", "supplied_customer_count (R-022)"]
  - term: "consumption"
    reason: "Ambiguous between cumulative index and delta volume (Module 1)."
    use_instead: ["billed_volume_m3", "metered_volume_m3", "meter_index_m3"]
  - term: "revenue"
    reason: "Ambiguous between billed and collected."
    use_instead: ["billed_amount_sar", "collected_amount_sar"]

kpis:
  - id: KPI-001
    name_en: "Non-Revenue Water"
    name_ar: "الفاقد المائي"
    definition_en: >
      The difference between the volume of water put into the distribution
      network and the volume billed to customers, expressed as a percentage of
      input volume, aggregated from DMA-day grain.
    definition_ar: >
      الفرق بين حجم المياه المُدخل إلى شبكة التوزيع والحجم المفوتر للعملاء،
      معبرًا عنه كنسبة مئوية من الحجم المُدخل، مجمّعًا من مستوى المنطقة واليوم.
    owner: steward.network@baseerah.gov.sa
    implements_rules: [R-025]
    measure_class: non_additive_ratio
    # CRITICAL: the ratio is computed from SUMMED numerator and denominator.
    # Averaging per-DMA percentages over-weights small DMAs by 3.8 points.
    sql: |
      (sum(f.input_volume_m3) - sum(f.billed_volume_m3))
        / nullif(sum(f.input_volume_m3), 0) * 100
    fact: fct_network_balance_daily
    dimensions: [dim_date, dim_dma]
    refresh: daily
    target_2030: 24.0
    current_value: 30.2
    excludes: >
      Readings flagged is_estimated are excluded from the billed volume
      denominator (Module 6 remediation ladder rung 4).

  - id: KPI-002
    name_en: "Registered customers"
    name_ar: "العملاء المسجلون"
    definition_en: >
      The count of customer accounts whose account_status is ACTIVE at the
      reporting date, including seasonal, government and disputed accounts,
      because the authority holds a contractual obligation to each.
    definition_ar: >
      عدد حسابات العملاء التي تكون حالتها نشطة في تاريخ التقرير، شاملةً الحسابات
      الموسمية والحكومية والمتنازع عليها.
    owner: steward.billing@baseerah.gov.sa
    implements_rules: [R-021]
    measure_class: additive_count
    sql: |
      count(distinct case when dc.account_status = 'ACTIVE'
                          then dc.customer_id end)
    fact: fct_customer_snapshot
    dimensions: [dim_date, dim_customer, dim_dma]
    refresh: daily
    current_value: 58100

  - id: KPI-003
    name_en: "Supplied customers"
    name_ar: "العملاء المزوّدون"
    definition_en: >
      The count of distinct customer accounts with metered volume greater than
      zero in the reporting quarter; measures network reach, not the registered
      base, and is always less than or equal to KPI-002.
    definition_ar: >
      عدد حسابات العملاء المتمايزة التي سُجّل لها استهلاك أكبر من صفر خلال ربع
      التقرير؛ ويقيس التغطية الفعلية للشبكة وليس القاعدة المسجلة.
    owner: steward.network@baseerah.gov.sa
    implements_rules: [R-022]
    measure_class: additive_count
    sql: |
      count(distinct case when agg.volume_m3 > 0 then agg.customer_id end)
    fact: fct_meter_read_hourly
    dimensions: [dim_date, dim_customer, dim_dma]
    refresh: daily
    current_value: 49780
    reconciliation: "KPI-003 <= KPI-002 must always hold; asserted in CI."
```

### Orchestration with an idempotency proof and generated documentation

```python
# dags/baseerah_daily.py
"""The Baseerah daily warehouse DAG: extract -> load -> gate -> core -> mart.

WHY: an orchestrated pipeline is only operable if it is safe to re-run. Every
task below is idempotent, and the `assert_idempotent` task proves it by
capturing measure sums before and after a repeat build of the mart. Without
that proof the on-call engineer at 02:00 has no safe action and will either
do nothing or double-load 486,300 billing lines.

Documentation publication runs LAST so the dictionary can never describe a
state the warehouse is not in.
"""
from __future__ import annotations

import pendulum
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

RIYADH = pendulum.timezone("Asia/Riyadh")


@dag(
    dag_id="baseerah_daily",
    schedule="0 3 * * *",                    # 03:00 Riyadh, after SCADA close-out
    start_date=pendulum.datetime(2026, 4, 1, tz=RIYADH),
    catchup=False,
    max_active_runs=1,                       # never two writers into mart
    default_args={"retries": 2, "retry_delay": pendulum.duration(minutes=5)},
    tags=["baseerah", "warehouse"],
)
def baseerah_daily():

    # --- Extract: four sources, four patterns (Technical Content section 1) ---
    extract_billing = BashOperator(
        task_id="extract_billing_cdc",
        # Log-based CDC: the billing CRM's deletes are real events (account
        # closures) and a watermark extract would miss every one of them.
        bash_command="python -m baseerah.extract.billing_cdc --since-lsn {{ var.value.billing_lsn }}",
    )
    extract_scada = BashOperator(
        task_id="extract_scada_append",
        # Append-only telemetry: simplest and most reliable pattern.
        bash_command="python -m baseerah.extract.scada --date {{ ds }} --lookback-hours 72",
    )
    extract_workorder = BashOperator(
        task_id="extract_workorder_watermark",
        bash_command="python -m baseerah.extract.workorder --since '{{ prev_ds }}'",
    )
    extract_finance = BashOperator(
        task_id="extract_finance_full",
        # 2.9M ledger lines but only 6 tariffs and 41 DMAs change; full extract
        # of the small reference tables is simpler than tracking their changes.
        bash_command="python -m baseerah.extract.finance --mode full",
    )

    @task
    def dq_gate(**context) -> dict[str, int]:
        """Fail fast on structural defects; quarantine value defects.

        Structural failures (null meter_id, duplicate grain key) mean the
        source contract is broken and downstream models would produce silently
        wrong numbers -- stop. Value failures (out-of-range volume) are
        quarantined and routed to a steward, because the load must still
        deliver the 99% of rows that are good.
        """
        from baseerah.dq.gate import run_checkpoint

        result = run_checkpoint("baseerah_core", run_id=context["run_id"])
        if result.structural_failures:
            raise ValueError(
                f"Structural DQ failure, aborting: {result.structural_failures}. "
                f"Owners notified: {result.owners}"
            )
        return {"quarantined": result.quarantined_rows,
                "composite_score": result.composite_score}

    build_core = BashOperator(
        task_id="build_core",
        bash_command="dbt build --select core --target prod --project-dir /opt/baseerah",
    )
    snapshot_scd2 = BashOperator(
        task_id="snapshot_scd2",
        # Snapshots must run BEFORE the mart so facts resolve against the
        # dimension version in force at event time (Module 7).
        bash_command="dbt snapshot --target prod --project-dir /opt/baseerah",
    )
    build_mart = BashOperator(
        task_id="build_mart",
        bash_command="dbt build --select mart --target prod --project-dir /opt/baseerah",
    )

    @task
    def assert_idempotent() -> None:
        """Prove the mart build is safe to retry.

        Capture the additive measure sums, rebuild the mart, and compare. Any
        difference means a re-run would corrupt the warehouse, and that is a
        blocking defect rather than a warning.
        """
        import subprocess

        from baseerah.warehouse.checks import measure_fingerprint

        before = measure_fingerprint(
            ["fct_meter_read_hourly", "fct_billing_line", "fct_work_order"]
        )
        subprocess.run(
            ["dbt", "build", "--select", "mart", "--target", "prod",
             "--project-dir", "/opt/baseerah"],
            check=True,
        )
        after = measure_fingerprint(
            ["fct_meter_read_hourly", "fct_billing_line", "fct_work_order"]
        )
        if before != after:
            raise ValueError(
                f"Mart build is NOT idempotent. before={before} after={after}. "
                "A retry would corrupt the warehouse."
            )

    @task
    def reconcile_mart_to_core() -> None:
        """Assert every additive measure in mart equals its core source.

        Alerting only on task failure misses the dangerous case: a DAG that
        succeeds while the mart silently diverges from core.
        """
        from baseerah.warehouse.checks import reconcile

        diffs = reconcile(
            pairs=[("mart.fct_billing_line.billed_volume_m3",
                    "core.invoice_line.consumed_m3"),
                   ("mart.fct_billing_line.billed_amount_sar",
                    "core.invoice_line.line_amount_sar"),
                   ("mart.fct_meter_read_hourly.volume_m3",
                    "core.meter_reading.volume_m3")],
            tolerance=0.0,       # exact: these are NUMERIC, not floating point
        )
        if diffs:
            raise ValueError(f"Mart/core reconciliation failed: {diffs}")

    publish_docs = BashOperator(
        task_id="publish_data_dictionary",
        # Generated from information_schema + meta.entity_definition + the dbt
        # manifest. Fails if any core/mart table lacks a business definition.
        bash_command=(
            "dbt docs generate --target prod --project-dir /opt/baseerah && "
            "python -m baseerah.meta.publish_dictionary --out /srv/baseerah/dictionary"
        ),
    )

    gate = dq_gate()
    [extract_billing, extract_scada, extract_workorder, extract_finance] >> gate
    gate >> build_core >> snapshot_scd2 >> build_mart
    build_mart >> assert_idempotent() >> reconcile_mart_to_core() >> publish_docs


baseerah_daily()
```

## Hands-on Lab 8 — Run the Pipeline, Build the Dashboard, Publish the Dictionary

| | |
|---|---|
| **Objective** | Fix the incremental lookback defect, orchestrate the full DAG idempotently, build the six-tile executive dashboard and the bilingual NRW regulator report from the governed KPI register, and publish a generated data dictionary and business glossary |
| **Duration** | 50 minutes |
| **Setup** | PostgreSQL 16 with `mart` built from Lab 7, `docker compose up airflow`, Power BI Desktop or Metabase from the compose stack, course repo, `git checkout lab8-start` |

**Instructions & tasks**

1. *(8 min)* Run `dbt build --select fct_meter_read_hourly` incrementally with the starter's strict watermark filter, then compare row counts against a full refresh. You will find 39,700 readings missing (6.1% of the 72-hour window). Replace the filter with the 72-hour lookback and confirm the counts match.
2. *(8 min)* Trigger `baseerah_daily` in Airflow. Confirm all nine tasks succeed, that `assert_idempotent` passes, and that `reconcile_mart_to_core` reports zero differences. Record the total run time in `BENCHMARKS.md` (expect 4 m 10 s full, 52 s incremental).
3. *(10 min)* Complete `semantic/kpi_register.yml` to twelve KPIs. Every KPI needs an owner, both language definitions, the measure class, and the rule IDs it implements. Run `python -m baseerah.semantic.lint_kpis` — it must reject any KPI whose label uses a banned term.
4. *(12 min)* Build the six-tile executive dashboard. Each tile names its KPI ID, shows a comparison (target or prior period), and carries the pipeline's "data as at" timestamp. Fix the planted defect: the "Customers" tile currently renders `supplied_customer_count` under an ambiguous label.
5. *(8 min)* Build the bilingual NRW regulator report. It must show 30.2% for the district, carry Arabic and English headers, and stamp the dbt invocation ID, git SHA and DQ composite score. Verify no tile or report row exposes data below DMA grain.
6. *(4 min)* Run `python -m baseerah.meta.publish_dictionary` and confirm it generates entries for all 16 `core` and 15 `mart` objects, and fails if you remove one definition. Commit: `feat(bi): governed KPI register, executive dashboard, bilingual NRW report, generated dictionary`.

**Expected output**
```
$ dbt build --select fct_meter_read_hourly   # starter, strict watermark
13,018,800 -> 12,979,100 rows   (39,700 late readings LOST, 6.1% of window)

$ dbt build --select fct_meter_read_hourly   # with 72h lookback
13,018,800 rows  incremental run 8.4s   (full refresh: 2m12s)

$ airflow dags trigger baseerah_daily
extract_billing_cdc ....... success  18.2s
extract_scada_append ...... success  41.6s
extract_workorder_watermark success   6.1s
extract_finance_full ...... success  12.4s
dq_gate ................... success  33.8s   quarantined=24,760  composite=94.8
build_core ................ success  46.9s
snapshot_scd2 ............. success  12.7s
build_mart ................ success  2m18s
assert_idempotent ......... success  2m21s   fingerprint MATCH
reconcile_mart_to_core .... success   4.2s   0 differences
publish_data_dictionary ... success   9.1s   31 objects documented
DAG run: success in 4m10s

$ python -m baseerah.semantic.lint_kpis
REJECT tile 'Customers' -> banned term resolution failed: label does not name a KPI ID
  suggestion: 'Registered customers (KPI-002)' or 'Supplied customers (KPI-003)'
1 violation. Fix before publishing.

$ python -m baseerah.meta.publish_dictionary --out /srv/baseerah/dictionary
core: 16 tables, 148 columns documented
mart: 15 objects (5 facts, 9 dimensions, 1 bridge), 121 columns documented
glossary: 34 business terms (EN+AR), 3 banned terms with replacements
FAIL check: 0 undocumented objects
```

**Acceptance criteria**
- Incremental run recovers all 13,018,800 rows with the 72-hour lookback; `assert_idempotent` passes on a repeat build.
- Twelve KPIs registered with owners, bilingual definitions, measure class and rule IDs; the KPI lint passes.
- Six-tile dashboard where every tile names its KPI ID and shows a comparison; no view exposes data below DMA grain.
- Bilingual NRW report shows 30.2% and stamps invocation ID, git SHA and DQ composite score; dictionary documents 31 objects and fails when one definition is removed.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Incremental run loses ~39,700 rows | Strict `max(read_ts)` watermark | 72-hour lookback + `delete+insert` on the grain |
| `assert_idempotent` fails | `incremental_strategy='append'` | Use `delete+insert` or `merge` on the declared unique key |
| District NRW reads 34.0% not 30.2% | BI tool averaging per-DMA percentages | Compute from summed numerator and denominator per KPI-001 |
| Arabic labels render reversed or as boxes | Font without Arabic coverage / no RTL setting | Use an Arabic-capable font and set the report's text direction to RTL |

**Instructor notes.** Task 1 is the highest-value five minutes of Day 5: the strict-watermark defect produces no error and a plausible number, and participants who have not seen it will ship it. Make everyone run both counts. In task 4, expect at least one pair to argue that "Customers" is fine because "everyone knows what it means" — that is the exact sentence that cost the SAR 220 million decision in Module 1, and it is worth quoting back to them. In task 5, walk the room checking that nobody has added a meter-level drill-through "for convenience"; it is a PDPL breach delivered in two clicks and it is the most common capstone anti-pattern. Fast finishers: add row-level security to the field-operations layer driven by a governed district-mapping table, and demonstrate two supervisor logins seeing different districts.

## Mini Exercises

**Quiz (5 questions)**
1. Why does a strict high-watermark incremental filter lose data? → late-arriving rows fall below the watermark and are never re-read; here 6.1% of AMI readings.
2. What makes a pipeline safe to retry at 02:00? → idempotency, proven by a repeat-build fingerprint test.
3. Why must a ratio KPI be defined in the semantic layer? → averaging per-group ratios over-weights small groups; the numerator and denominator must be summed first.
4. What three stamps make a regulator submission reproducible? → dbt invocation ID, git commit SHA, dimension snapshot timestamp (plus the DQ composite score).
5. Why is the dictionary published as the last DAG task? → so documentation can never describe a warehouse state that does not exist.

**Debugging exercise.** Check out `git checkout lab8-append-incremental`. `fct_billing_line` uses `incremental_strategy='append'`. Symptom: an Airflow retry after a transient network failure double-loads the 5-day lookback window; district revenue jumps from SAR 41.2M to SAR 47.6M and the reconciliation step catches it. Ask participants to fix the strategy, then discuss why the reconciliation task — not the DAG's success status — was the control that mattered.

**Design exercise.** The regulator adds a requirement to report NRW split into *real* losses (leaks, overflows) and *apparent* losses (metering error, unauthorised consumption). State what new fact or dimension is needed, which existing KPI must be superseded rather than edited, how the change is recorded in the KPI register, and what you publish about the prior periods.

**Discussion questions.**
- A directorate wants its own dashboard with its own definition of billed volume "because our board reads it differently". What do you offer them, and what do you refuse?
- Should the executive dashboard show the DQ composite score alongside the KPIs? Argue both sides, then decide what happens on the Sunday the score drops to 81%.

## Case Study — Three Definitions of a Berth at "Marasi" (مراسي)

**Scenario.** "Marasi" (مراسي), a Red Sea ports and logistics operator running container and bulk terminals at Jeddah and Yanbu, publishes berth utilisation to its board, to the transport regulator, and to an operations control screen. In the same week the three sources reported 84%, 71%, and 92% for the same quarter at the same terminal.

**Business context.** Berth utilisation drives a SAR 1.8 billion capacity-expansion business case. The regulator's figure determines a concession compliance test. The operations figure drives shift rostering. All three had been used for over a year without anyone comparing them side by side.

**Technical challenge.** Three teams had implemented "utilisation" independently against the same warehouse: the board figure counted occupied berth-hours over calendar hours; the regulator figure excluded declared maintenance windows from the denominator; the operations figure counted a berth as occupied from pilot boarding to line release rather than from first line to last line. Each was correct for its purpose, none was documented, and the warehouse's star schema supported all three equally well — which was precisely the problem.

**Constraints.** The regulator's definition is fixed by the concession agreement and cannot change. The board's figure has been used in two published annual reports. The operations definition is the only one that matches what a terminal manager can observe from the quay. All three must survive; the expansion business case must be rebuilt on one of them within eight weeks.

**Solution approach (facilitate, don't lecture).** Guide the room to: (1) register three separately named KPIs — `berth_occupancy_calendar_pct`, `berth_utilisation_regulatory_pct`, `berth_working_time_pct` — each with an owner, a definition, and its exact SQL, and ban the unqualified term "utilisation"; (2) implement all three in one semantic layer over the existing star, so the numbers can never diverge from their definitions again; (3) label every tile, report and screen with the KPI it renders; (4) rebuild the business case on the regulatory definition, because that is the one with an external commitment attached, and show the other two alongside as context. The facilitation trap to watch for: the room will want to declare one "the truth". Push back — three real business questions require three measures, and the failure was never plurality, it was anonymity.

**Discussion questions.**
1. The star schema supported all three definitions equally well. Is that a strength or a weakness of dimensional modelling, and what layer must compensate?
2. Two annual reports used the board figure. What is the correct disclosure, and does it differ from the Qimam and Mizan cases?
3. How would you make it structurally impossible for a fourth definition to appear next year?
4. The operations definition is the only one a terminal manager can verify by looking out of the window. What does that suggest about which definition should drive day-to-day behaviour?

## Benchmarks and Evaluation

| Metric | Category | Target after M8 | How measured |
|---|---|---|---|
| Pipeline completeness | Coverage | 9-task DAG succeeds end to end | Airflow run status |
| Incremental correctness | Correctness | 13,018,800 rows with 72-hour lookback; 0 lost | row-count diff vs full refresh |
| Idempotency | Reliability | measure fingerprint identical on repeat build | `assert_idempotent` task |
| KPI governance | Governance | 12 KPIs, 100% with owner + bilingual definition; lint clean | `lint_kpis` exit code |
| Documentation coverage | Governance | 31 objects, 269 columns, 0 undocumented | `publish_dictionary` output |

**Example benchmark table (filled during lab):**

| Stage | Task | Duration | Rows processed | Note |
|---|---|---|---|---|
| Extract | billing CDC | 18.2 s | 4,180 changes | deletes captured |
| Extract | SCADA append | 41.6 s | 173,584 | 72-hour lookback window |
| Gate | `dq_gate` | 33.8 s | 13,018,800 checked | 24,760 quarantined, composite 94.8 |
| Core | `dbt build --select core` | 46.9 s | — | 16 models |
| Snapshot | `dbt snapshot` | 12.7 s | 3,840 new versions | SCD2 |
| Mart | `dbt build --select mart` | 2 m 18 s | — | 16 nodes incl. tests |
| Verify | `assert_idempotent` | 2 m 21 s | — | fingerprint match |
| Verify | `reconcile_mart_to_core` | 4.2 s | 3 measure pairs | 0 differences |
| Publish | dictionary + glossary | 9.1 s | 31 objects | 0 undocumented |
| **Total** | **full run** | **4 m 10 s** | — | incremental run: 52 s |

## Required Visuals and Training Assets

### Diagrams
1. **The Baseerah DAG** — *Purpose:* the capstone's architecture in one image. *Elements:* four extract tasks with their pattern labels (CDC / append / watermark / full), converging through the DQ gate with its quarantine branch, then core → snapshot → mart → idempotency → reconcile → publish. *Style:* left-to-right DAG with the gate and reconcile nodes emphasised. *Designer description:* "A pipeline graph where two diamond-shaped control nodes (gate, reconcile) are visually heavier than the rectangular build nodes."
2. **The lookback window** — *Purpose:* make late arrival visible. *Elements:* a timeline of readings by event time with 6.1% arriving after the watermark line, shaded as lost; the 72-hour lookback drawn as a wider recapture band. *Style:* timeline with two bands. *Designer description:* "Dots along a time axis; those left of a red watermark line are grey (lost); a blue band 72 hours wide recaptures them."
3. **One KPI, one owner, one implementation** — *Purpose:* the governance thesis. *Elements:* the KPI register at the centre feeding the semantic layer, which feeds dashboard, regulator report, and ad-hoc analysis; a crossed-out arrow showing a BI tool implementing its own version. *Style:* hub-and-spoke with one forbidden path.
4. **The executive dashboard wireframe** — *Purpose:* a design target for Lab 8. *Elements:* six tiles in decision order, each annotated with its KPI ID, comparison type, and PDPL aggregation floor; a "data as at" stamp in the header. *Style:* annotated wireframe, Arabic and English labels.

### Images (screenshots)
1. **The Airflow graph view of a successful run** — *why:* the pipeline must be seen as one operable object; *content:* all nine tasks green with durations.
2. **The bilingual NRW regulator report** — *why:* the deliverable that faces outward; *content:* Arabic and English headers, 30.2%, and the reproducibility stamps in the footer.
3. **The generated data dictionary page for `fct_meter_read_hourly`** — *why:* documentation as an artefact, not a promise; *content:* the grain sentence, column list with measure classes, lineage, and the owning steward.

### Simulations
1. **The silent watermark** — *Setup:* branch `lab8-strict-watermark` uses `max(read_ts)` with no lookback. *Expected behaviour:* 39,700 readings (6.1%) are lost per run with no error; district billed volume drifts 6% light and NRW reads roughly 4 points high. *Learning objective:* correctness defects that raise no error are the ones that reach production.
2. **The ambiguous tile** — *Setup:* branch `sim-ambiguous-tile` labels a tile "Customers" rendering `supplied_customer_count`. *Expected behaviour:* the board reads 49,780 as the registered base and asks where 8,320 customers went. *Learning objective:* a label shorter than a definition is a governance failure at the presentation layer.

### Interactive Activities
- **Tile critique (12 min):** four printed dashboard tiles, each with a different defect (unnamed measure, no comparison, ratio averaged, meter-level drill-through). Teams identify the defect and rewrite the tile.
- **Write the definition (12 min):** each participant writes the governed definition of one Baseerah KPI in English and Arabic; the room reviews two at random against the register's required fields.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `semantic/kpi_register.yml` | Lab 8 starter (3 KPIs pre-filled, 9 to add) | YAML | 12 KPIs at completion | Semantic layer + dashboard labels |
| `mart.*` | Output of Lab 7 | Postgres schema | 5 facts, 9 dims, 1 bridge | Dashboard and report source |
| `fixtures/late_arrivals_72h.sql` | Synthetic late AMI batch | SQL | 39,700 readings | Lookback-window exercise |
| `reports/nrw_regulator_template.pbix` | Bilingual report template | PBIX / Metabase JSON | 1 report, 4 pages | Regulator submission |

### Demo Requirements
- **Instructor demo (8 min):** run the incremental build with the strict watermark and with the lookback, side by side, and show the 39,700-row gap. Then open the ambiguous tile and ask the room what number the board is reading. Close the course's technical arc with: "the pipeline was green, every test passed, and the number was wrong. That is what the last five days have been about."

---

# Final Capstone Project

## Title: Baseerah — From Four Source Systems to One Number Leadership Can Defend

## Project Scenario

You are the data architect for **Baseerah (بصيرة)**, the enterprise data warehouse and BI platform of a Saudi national water and utilities authority. Four source systems feed you: a billing/CRM system, a SCADA/telemetry feed, a work-order/maintenance system, and a finance ledger. Three consumers depend on you: the regulator, who receives a quarterly non-revenue-water submission and can ask you to reproduce any historic figure; the executive committee, which reviews six KPIs every Sunday morning; and 41 district supervisors, who need field-operations analytics on a tablet while standing at a service point.

Your mandate is not to build a warehouse. It is to build a warehouse whose numbers survive being questioned — by a regulator asking what October looked like in October, by a finance director whose ledger disagrees with your revenue, and by two directorates who each have a legitimate and different definition of "active customer". Everything you built in Labs 1–8 is a component. The capstone is the integration, the evidence, and your own extensions.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Three-level model with metadata (LO1):** conceptual model (14 entities, one-page), logical ERD (16 entities including 2 associative), and deployed physical schema — each versioned, each with a definition and PDPL classification for every entity, and a build gate that fails when a `core` or `mart` table has no definition.
2. **Requirements and business rules (LO2):** a rule register of ≥ 20 rules covering all four rule types, each with an individual owner, a BECAUSE clause and an enforcement point; the active-customer contradiction escalated as a governance item, never silently resolved.
3. **ER design and keys (LO3):** surrogate primary keys with UNIQUE alternate keys throughout; both many-to-many relationships resolved with associative entities carrying relationship attributes; referential actions chosen per rule, not by default; all four cardinality claims verified against the landed data.
4. **Normalisation and a justified denormalisation (LO4):** `raw.billing_extract` decomposed to 3NF with a lossless-rejoin proof, one BCNF case handled with its lost dependency named and enforced, and a decision record for the mart denormalisation stating the redundancy, the three protections, and measured before/after timings.
5. **Physical implementation (LO5):** `core` deployed in PostgreSQL with rule-named constraints, monthly range partitioning on `meter_reading`, an index strategy justified by four named access patterns, and a benchmark table showing the BRIN/B-tree/sequential comparison from your own runs.
6. **Data quality engineering (LO6):** a sentinel-aware baseline of 72.4% across all six dimensions, ≥ 31 expectations traced to rule IDs, the remediation ladder applied to five defect classes with quarantine (never drop), 3,320 duplicates resolved with field-level survivorship and a reversible merge log, and a post-remediation composite of 94.8%.
7. **Dimensional warehouse (LO7):** 5 facts with a one-sentence grain in the table comment, 9 dimensions, SCD2 on customer and meter with an idempotent snapshot, plus working junk, degenerate, role-playing, conformed, bridge and factless patterns — and a historic-restatement proof that SCD2 reproduces the figure originally submitted.
8. **ELT, BI and definition governance (LO8):** a nine-task idempotent Airflow DAG with a DQ gate and a mart/core reconciliation, incremental models with a measured lookback, a 12-KPI governed register with bilingual definitions and owners, a six-tile executive dashboard where every tile names its KPI, a bilingual NRW regulator report with reproducibility stamps, and a generated data dictionary and business glossary.

**One extension (choose at least one):**
- Add prepaid meters: a new fact with its own grain, a semi-additive balance measure, and conformity to the existing dimensions with no change to `dim_date`, `dim_dma` or `dim_customer`.
- Add real/apparent loss decomposition to the NRW report, superseding rather than editing KPI-001, with a published note on prior periods.
- Implement row-level security on the field-operations layer from a governed district-mapping table, demonstrated with two supervisor logins.
- Extend match/merge to a simulated 214,000-account regional acquisition, sizing the steward review band against a two-person team.
- Build a data-quality trend dashboard that plots the six dimension scores over the DAG's run history and alerts when the composite drops below 90%.

## Architecture (target state)

```
SOURCES                 raw            stg          core (3NF)        mart (star)         CONSUMERS
 billing/CRM ──CDC──┐                                                ┌ dim_date ────────┐
 SCADA ────append───┤                          ┌ customer_golden ┐   │ dim_customer(SCD2)│  executive
 work-order ─w/mark─┼─► landed ──► conformed ──┤ meter           ├──►│ dim_meter (SCD2)  ├─► KPI dashboard
 finance ────full───┘   (as        (typed,     │ meter_reading   │   │ dim_dma (conformed)│   (6 tiles)
                        received)   deduped)   │ invoice_line    │   │ dim_read_flag(junk)│
                             │                 │ work_order      │   │ bridge_account_    │  regulator
                        DQ GATE ──quarantine──►│ account_meter_  │   │   meter (weighted) ├─► NRW report
                        (31 expectations,      │   share         │   ├ fct_meter_read_hourly  (bilingual)
                         6 dimensions,         └─────────────────┘   │ fct_billing_line   │
                         72.4% -> 94.8%)                             │ fct_work_order     │  field ops
                             │                                       │ fct_network_balance├─► analytics
                        steward queue                                └ fct_meter_inspection   (RLS by
                        (SLA 5 days)                                        (factless)          district)

  orchestrated by ONE idempotent DAG: extract >> gate >> core >> snapshot >> mart >> assert >> reconcile >> publish
  governance: 20 rules · 12 KPIs (1 definition, 1 owner) · data dictionary + bilingual glossary · PDPL aggregation floor
```

## Deliverables

1. Git repository URL with full history and a one-command run (`make pipeline` or an Airflow DAG trigger) that rebuilds everything from `raw`.
2. The three model artefacts — conceptual DBML, logical DBML, physical DDL migrations — plus the rendered diagrams.
3. `BENCHMARKS.md` with every course benchmark table filled from *your* runs: load throughput, index sizes and timings, DQ dimension scores before and after, dbt build times, DAG stage durations.
4. `GOVERNANCE.md`: the rule register summary, the KPI register, the escalated governance items, the PDPL classification and aggregation floor, and the retention policy with its partition-drop mechanism.
5. `DECISIONS.md`: six one-paragraph engineering decisions with rationale (surrogate vs natural key, BCNF vs 3NF for the officer relation, denormalisation of `dim_customer`, index strategy, SCD type per dimension, lookback window length).
6. A 6-minute demo: one-command pipeline run, a quality-gate quarantine, the historic-restatement proof, the dashboard with a tile that names its KPI, and the bilingual regulator report with its reproducibility stamps.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: conceptual model + rule register with escalation | End Day 1 | 14 entities defined + GOV-001 raised |
| M-B: logical ERD in BCNF + denormalisation decision record | End Day 2 | cardinality claims verified + lossless rejoin proof |
| M-C: `core` deployed, benchmarked, DQ baseline and remediation | End Day 3 | composite 72.4% → 94.8% + 58,100 golden records |
| M-D: star schema with SCD2 and restatement proof | End Day 4 | `dbt build --select mart` green + 29.30% reproduced |
| M-E: DAG, dashboard, dictionary, demo | Day 5 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Modelling progression & metadata | 15 | All three levels versioned and consistent; every entity defined and PDPL-classified; build gate enforces it | Minor gaps in definitions or one level drifting from another | Levels collapsed; source tables presented as a conceptual model; no definitions |
| Requirements & rule governance | 12 | ≥ 20 rules, all four types, individual owners, BECAUSE clauses; contradiction escalated | Rules present but thin BECAUSE clauses or directorate-level ownership | Untestable rules; contradiction silently resolved; action-enabling rule as a constraint |
| ER design, keys & integrity | 13 | Surrogate + alternate keys throughout; both M:N resolved with relationship attributes; referential actions justified; claims verified | One key or cardinality defect; claims partly verified | Natural PK on `meter`; repeating groups; default `NO ACTION` everywhere |
| Normalisation & denormalisation | 12 | 3NF + one BCNF case with the lost FD named and enforced; lossless proof; decision record with measured timings | Decomposition correct, BCNF or proof thin | Lossy split undetected; denormalised with no protections |
| Physical design & performance | 13 | Partitioned, rule-named constraints, four justified indexes, own benchmark table, pruning demonstrated | Works; index choice partly unjustified or benchmarks incomplete | Naive timestamps, float money, no partitioning, speculative indexes |
| Data quality engineering | 15 | Sentinel-aware 72.4% baseline, ≥ 31 traced expectations, quarantine not drop, reversible match/merge with field-level survivorship, 94.8% | Most present; survivorship record-level or quarantine partial | Flattering baseline; rows dropped; silent imputation; over-eager auto-merge |
| Dimensional warehouse, ELT & BI | 20 | Grain declared and tested; SCD2 with restatement proof; all six dimension patterns; idempotent DAG; 12 governed KPIs; bilingual report; generated dictionary | Star built and loading; one pattern missing or KPI governance thin | Fan-out on natural-key join; ratio stored as fact; ambiguous tile labels; non-idempotent DAG |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope scores ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the running warehouse and repository evidence first* — one-command run, `dbt build` output, the restatement proof, the DQ score history, the generated dictionary — and the demo second. The point of the course is that the platform testifies for itself.
- Anti-pattern flags that cap a criterion at 70%: a natural key as a fact-table foreign key under SCD2 (the fan-out); a ratio stored as a fact; silent un-flagged imputation; rows dropped rather than quarantined; a dashboard tile whose label does not name its KPI; meter-level personal data exposed below the DMA aggregation floor; a non-idempotent pipeline.
- Verify one claim live per participant: ask them to run the historic-restatement query and explain which figure is correct and why, or to re-run the DAG and show the idempotency fingerprint matching. A participant who cannot explain their own restatement result has integrated components without understanding them.

## Bonus Tasks (for early finishers / distinction seekers)

1. Implement a `column_does_not_exist` style guard for every non-additive measure so a reviewer cannot add a stored ratio to a fact table without failing the build.
2. Add a seasonal tariff (summer/winter block rates), state the new functional dependency, and prove that historic invoices still reproduce exactly.
3. Build a lineage view that answers, for any dashboard tile, which rules, columns, and source systems it depends on — and demonstrate it for `nrw_pct`.
4. Implement the PDPL retention job as a partition drop, time it against the equivalent `DELETE`, and document the aggregate that survives the drop.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Which model level contains indexes and partitions? → physical.
**Q2.** Name the three kinds of metadata. → business, technical, operational.
**Q3.** Which rule type must never be enforced as a database constraint? → action-enabling.
**Q4.** State the key rule taught in Module 3. → surrogate primary key plus a UNIQUE constraint on the natural/business key.
**Q5.** Why must `meter.service_point_id` be nullable? → procured-but-not-installed meters are real and must be representable.
**Q6.** Which anomaly does 3NF remove that 2NF does not? → insert/delete anomalies from transitive dependencies.
**Q7.** What is lost in a BCNF decomposition that 3NF preserves? → dependency preservation (an FD may span two tables).
**Q8.** Name the three protections that make a denormalisation controlled. → single writer; rebuild from a normalised source; reconciliation test.
**Q9.** Why is `NUMERIC` mandatory for SAR amounts? → binary float cannot represent decimal fractions exactly; error accumulates and never reconciles.
**Q10.** When is BRIN a bad index choice? → when physical row order does not correlate with the indexed column.
**Q11.** Name the three benefits of partitioning. → pruning, per-partition maintenance, retention by partition drop.
**Q12.** Which data-quality dimension cannot be improved by cleansing? → timeliness.
**Q13.** Why must imputed values be flagged? → an unflagged estimate is indistinguishable from a measurement and misrepresents a regulator-facing figure.
**Q14.** What is wrong with "newest record wins" survivorship? → it discards the earliest `opened_on` and can resolve a dispute into ACTIVE.
**Q15.** What must be declared before dimensions or measures are chosen? → the grain, in one business sentence.
**Q16.** Which key must a fact table store under SCD2, and why? → the dimension surrogate key in force at event time; a natural key fans the fact out across versions.
**Q17.** Why must a ratio never be stored as a fact? → it is non-additive; averaging per-group ratios over-weights small groups.
**Q18.** What is a factless fact table for? → recording that an event happened with no measure — coverage and absence questions.
**Q19.** Why does a strict high-watermark incremental filter lose data? → late-arriving rows fall below the watermark and are never re-read.
**Q20.** What three stamps make a regulator submission reproducible? → dbt invocation ID, git commit SHA, dimension snapshot timestamp.

## Practical Assessments

**PA-1 (30 min, Day 3):** Given a `core` schema with float money, naive timestamps, an unindexed foreign key and no partitioning, restore correctness and performance: fix the types, add the partition strategy, justify one index change with `EXPLAIN (ANALYZE, BUFFERS)`, and produce a sentinel-aware quality baseline for one table. Scored on diagnosis notes (40%), fixes (40%), measured evidence (20%).

**PA-2 (30 min, Day 4):** Given a mart where `fct_billing_line` joins `dim_customer` on the natural key and `dim_dma` is Type 1, diagnose the inflated revenue and the drifting historic NRW figure, convert the dimension to SCD2, correct the join, and prove that the original submitted figure is reproduced. Scored on diagnosis (40%), correctness of fix (40%), restatement evidence (20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (8 labs) | 30% | checkpoint commits, expected outputs, `BENCHMARKS.md` entries |
| PA-1 + PA-2 | 20% | fixed schemas, query plans, restatement proof, diagnosis notes |
| Quiz | 10% | 10-question selection, closed book |
| Capstone (Baseerah warehouse + BI) | 40% | rubric, warehouse-first |

Badge issuance (Data-warehousing and BI badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical benchmark timings, DQ scores, or merge logs across repositories are checked) **and** no PDPL red flags — meter-level personal data exposed below the DMA aggregation floor, national IDs propagated outside `core`, or retention policy absent — any one of which blocks issuance regardless of score.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course repositories; push all checkpoint tags (`lab1-start` … `lab8-start`, every `*-solution`, and all `sim-*` and `lab*-broken` branches)
- [ ] Regenerate the Baseerah synthetic dataset with the pinned generator seed; verify the headline counts exactly: 61,420 raw accounts, 58,100 golden, 64,800 meters, 13,018,800 readings, 486,300 invoice lines, 184,600 work orders
- [ ] Dry-run all eight labs end to end on a clean machine, timing Lab 5's bulk load (must land at 3 m 48 s ± 25 s on the reference laptop) and Lab 7's mart build (4 m 10 s full DAG)
- [ ] Bring up the `docker compose` stack (PostgreSQL 16, Airflow 2.9, Metabase) and pre-pull the images; the Airflow image is the slowest download and the usual Day-5 delay
- [ ] Verify `dbt-postgres` 1.7, `dbt-utils`, `great-expectations` 0.18 and `psycopg` 3.1 install cleanly from the pinned lock file, and that `pg_trgm` and `btree_gist` extensions are available
- [ ] Print A1 posters: the three-level pyramid, the Baseerah logical ERD, the six quality dimensions, the bus matrix, the star schema, and the DAG
- [ ] Print A5 reference cards: the crow's-foot cheat card and the remediation ladder, one per participant
- [ ] Load the fixtures into the shared drive: the two persona cards, the private supervisor spreadsheet, the tariff-change SQL, the late-arrival batch, and the inspection campaign CSV
- [ ] Confirm the classroom network allows the package index and the container registry; in restricted government environments, pre-pull to a local registry and test one participant machine end to end

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.11 + git + a GitHub account
- [ ] Docker Desktop (WSL2 on Windows) or Colima; verify `docker run hello-world` and allocate ≥ 4 GB RAM to the engine
- [ ] `pip install dbt-postgres==1.7.* dbt-utils great-expectations==0.18.* psycopg[binary]==3.1.* pyyaml==6.0.*`
- [ ] Power BI Desktop (Windows) **or** confirm you will use the Metabase container in the course compose stack
- [ ] A dbdiagram.io account, or `npm i -g @softwaretechnik/dbml-renderer` for offline rendering
- [ ] Clone the course repo and run `make doctor` (validates Docker, PostgreSQL connectivity, dbt, Great Expectations, the extensions, and prints ✓/✗ per check)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Docker memory too low for the 13M-row load | High | Require ≥ 4 GB in the Docker engine settings; provide a 2M-row reduced dataset as the documented fallback |
| Sentinels counted as populated, giving a flattering DQ baseline | High | The planted defect — let it happen, then have them `SELECT DISTINCT ... LIMIT 20` and find `'N/A'` |
| Natural-key join to an SCD2 dimension (revenue fan-out) | High | Put both revenue figures on the board; require the surrogate range join in the acceptance criteria |
| Indexes created before the bulk load (22 min instead of 3 m 48 s) | High | Order of operations in `make load-core`; teach `NOT VALID` + `VALIDATE` |
| dbt profile/connection errors on first run | Medium | Ship a working `profiles.yml` in the repo; run `dbt debug` as the first command of Lab 7 |
| Arabic text rendering as boxes or reversed in the BI tool | Medium | Install an Arabic-capable font; set report text direction to RTL; verify on one machine before Day 5 |
| Snapshot creating new versions on every run | Medium | `strategy='check'` with explicit `check_cols`; the CRM's `updated_at` is unreliable on 12% of rows |
| Auto-merging the 0.80–0.92 similarity band | Medium | Acceptance criterion is 58,100 golden records; 57,180 means over-merging |
| Airflow container slow to become healthy on Day 5 | Medium | Start the stack at the beginning of Day 4's last hour, not on Day 5 morning |
| Confusion between the sample district and national figures | Low | Keep the two on separate slides; the sample is Riyadh North, the national figures are for scale only |

## Timing Recommendations

- Protect Lab 6b (match/merge) and Lab 7b (SCD2) at full length; compress Module 4's theory if behind, because the decomposition lands through the lab anyway.
- If a cohort is strong: pull the row-level-security extension and the prepaid-meter fact into main scope on Day 5, and run the BCNF trigger implementation as a whole-room exercise.
- If a cohort is weak: run Lab 7b's snapshot as a guided demo rather than a solo lab, but never skip the restatement *observation* — it is the module's thesis made visible and it is directly assessed in PA-2.
- Hard rule: the capstone assembly (Day 5 Hour 4) must start on time. Cut discussion, cut the fast-finisher tasks, cut the dashboard polish — never cut build time.
- Reserve the Day-1 Hour-1 PDPL framing even when running late. Introducing personal-data constraints on Day 5 produces a cohort that has already built a warehouse that breaches them.

## Discussion Prompts (use during transitions)

1. "Two directorates give you two definitions of the same word and both are right. What do you build, and who decides?"
2. "Your data-quality score improved and your business got worse. How is that possible, and what does it say about what you were measuring?"
3. "A regulator asks what October looked like — in October. What must be true of your dimensions for you to answer, and what must be true of your evidence for them to believe you?"
4. "Every test passed, the pipeline was green, and the number was wrong. Which control was missing?"
5. "If the warehouse is the evidence and Sunday morning is the decision, what does your current schema testify about the definitions your organisation has never written down?"

## Wrap-up (Day 5 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it, on one slide: three-level model (M1), rules and requirements (M2), keys and cardinality (M3), normalisation and the denormalisation record (M4), physical design and benchmarks (M5), data quality and match/merge (M6), dimensional model and SCDs (M7), ELT, BI and definition governance (M8).
- Forward pointer: SDA-DSC-214 (Modern Data Engineering for AI Systems) takes exactly this warehouse and industrialises it — the same `raw → core → mart` layering becomes a medallion Lakehouse with Delta Lake, streaming ingestion, and an AI feature store alongside the BI mart. Participants who have built Baseerah arrive with the modelling discipline that course assumes and rarely finds.
- Collect: repository URLs, `BENCHMARKS.md`, `GOVERNANCE.md`, `DECISIONS.md`, the exported data dictionary and business glossary, and the dashboard/report files. Issue badge recommendations within 5 working days, and return per-criterion rubric feedback with at least one named strength and one named gap per participant.

---

*End of instructor package. All code samples target PostgreSQL 16, Python 3.11, dbt-core 1.7 with dbt-postgres and dbt-utils, Great Expectations 0.18+, Apache Airflow 2.9, and Power BI Desktop or Metabase; verify the pinned versions in the course lock file before each delivery. City names, entity names and business glossary terms carry Arabic alongside English — the glossary and the regulator report are bilingual by design — while all code, schema names, table names, column names, dbt model names and commit messages remain in English per Saudi enterprise production convention. Saudi PDPL obligations are treated as first-class constraints from Day 1 Hour 1: meter-level consumption is personal data, national identifiers never leave the `core` schema, the DMA aggregation floor is enforced in every published view, and retention is implemented as a partition drop rather than a promise.*
