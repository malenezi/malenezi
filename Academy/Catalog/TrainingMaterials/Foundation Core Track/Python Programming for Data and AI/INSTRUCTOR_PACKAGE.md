# Python Programming for Data and AI
## برمجة بايثون للبيانات والذكاء الاصطناعي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Python Programming for Data and AI |
| **Arabic Title** | برمجة بايثون للبيانات والذكاء الاصطناعي |
| **Module Code** | SDA-FND-103 |
| **Level** | Practitioner |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Aspiring AI engineers and data scientists, developers, technical graduates |
| **Prerequisites** | Basic computer literacy; programming logic recommended |
| **Assessment** | Daily labs; coding assignments; mini-project |
| **Stackability** | Core technical badge · Counts toward the AI & Data Foundations Certificate (SDA-FND-101→105) · Prerequisite for all track-level technical modules · Next: SDA-FND-104, SDA-AIE-111, SDA-AIE-113, SDA-DSC-111, SDA-DSC-214 |
| **Tools & Platforms** | Python · NumPy · pandas · Git/GitHub · VS Code · pytest · Jupyter |

## Course Description

An intensive hands-on module that builds job-ready Python skills for data and AI work. Participants progress from core language constructs to scientific computing with NumPy and pandas, version control, and clean, testable code. It is the technical gateway to both the AI Engineer and Data Scientist tracks.

The course is built around a single evolving artefact: the **Wafr Markets daily sales pipeline** — a data-processing package that participants grow from a handful of cleaning functions on Day 1 into a version-controlled, tested, reproducible pipeline that ingests messy point-of-sale files and a live weather API, transforms them with NumPy and pandas, and emits a daily KPI report. Every lab produces a component of the final mini-project, so by Day 5 each participant owns a working end-to-end data processing pipeline — the same shape of codebase they will extend in SDA-FND-104 and in every track-level module that follows.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Develop structured Python programs using functions, data structures, and object-oriented design
2. **LO2** — Implement data manipulation and numerical computation workflows with pandas and NumPy
3. **LO3** — Apply version control with Git and collaborative repository workflows
4. **LO4** — Debug, test, and refactor Python code using systematic practices
5. **LO5** — Build reusable scripts and notebooks for data acquisition and processing
6. **LO6** — Organise projects with virtual environments and dependency management

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Thinking in Python | M1: Python Core — Types, Control Flow, Functions, OOP | 45% | 55% | Cleaning functions + typed record classes for the sales pipeline, runnable as script and notebook |
| **Day 2** | Data in, data out | M2: Data Structures & File/API Data Handling · M5 (part A): Local Git | 40% | 60% | Ingestion layer reading POS CSVs and a weather API, under Git with a clean commit history |
| **Day 3** | Compute at array speed | M3: NumPy Arrays & Vectorised Computation · M5 (part B): GitHub Collaboration | 40% | 60% | Vectorised KPI engine (≥ 50× loop speedup) merged via a reviewed pull request |
| **Day 4** | Tables and trust | M4: pandas for Tabular Data · M6: Testing, Debugging & Code Quality | 35% | 65% | pandas transform layer + pytest suite (≥ 80% coverage on cleaning/KPI code) |
| **Day 5** | Reproducible and shippable | M7: Environments & Dependency Management · Mini-Project Capstone | 25% | 75% | Clone-to-run reproducible pipeline + 5-minute capstone demo, rubric-assessed |

## Hour-by-Hour Breakdown

### Day 1 — Thinking in Python

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Course kickoff + why Python owns data & AI** | Recognise where Python sits in the data/AI stack; meet the golden-thread pipeline; verify environments (python, VS Code, Jupyter) | Interactive lecture + guided setup check | 60/40 |
| 2 | **Types, collections, and control flow** (M1) | Use scalars, strings, lists, tuples, dicts, sets; iteration patterns; comprehensions; truthiness pitfalls | Lecture + live REPL demo | 70/30 |
| 3 | **Lab 1a — Clean the messy sales export** | Write parsing and cleaning functions over raw POS records using core types and comprehensions | Guided lab (pairs) | 10/90 |
| 4 | **Functions and OOP for data work** (M1) | Design function signatures; avoid the mutable-default trap; type hints; dataclasses; dunder methods; when OOP earns its keep | Lecture + live coding | 70/30 |
| 5 | **Lab 1b — Model the domain** | Build `SaleRecord` and `DailyBatch` classes; refactor Lab 1a functions into a module importable from script and notebook | Guided lab (pairs) | 10/90 |

### Day 2 — Data In, Data Out

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Data structures in anger** (M2) | Choose dict/set/Counter/defaultdict for lookup, dedup, grouping; navigate nested JSON-shaped data | Lecture + worked example | 60/40 |
| 2 | **Files and APIs done right** (M2) | Read CSV/JSON safely (pathlib, context managers, encodings); call REST APIs with requests; handle pagination and failures | Lecture + live demo | 60/40 |
| 3 | **Lab 2 — Build the ingestion layer** | Load POS CSVs and the weather API into validated record lists; quarantine malformed rows | Guided lab | 10/90 |
| 4 | **Version control begins** (M5 part A) | Explain snapshots vs diffs; init/status/add/commit/log/diff; .gitignore for data work; undo safely | Lecture + live demo | 60/40 |
| 5 | **Lab 5a — Put the pipeline under Git** | Initialise the repo, write .gitignore, commit Day 1–2 work as logical commits, read history | Guided lab | 10/90 |

### Day 3 — Compute at Array Speed

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **NumPy arrays and vectorisation** (M3) | ndarray memory model; dtypes; shape; vectorised operations vs Python loops; ufuncs | Lecture + benchmark demo | 70/30 |
| 2 | **Indexing, masks, axis logic, broadcasting** (M3) | Boolean masks; fancy indexing; axis semantics; broadcasting rules; views vs copies; NaN handling | Lecture + live coding | 60/40 |
| 3 | **Lab 3 — Vectorise the KPI engine** | Replace loop-based revenue/discount statistics with NumPy; measure the speedup | Guided lab | 10/90 |
| 4 | **GitHub and collaboration** (M5 part B) | Remotes; push/pull; branches; pull requests; code review; resolving merge conflicts | Lecture + live conflict demo | 60/40 |
| 5 | **Lab 5b — Collaborate on the repo** | Push to GitHub; run a branch → PR → review → merge cycle in pairs; create and resolve a real conflict | Guided lab (pairs) | 10/90 |

### Day 4 — Tables and Trust

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **pandas fundamentals** (M4) | Series/DataFrame/Index anatomy; read_csv parameters that matter; dtypes incl. category and datetime; loc/iloc | Lecture + live demo | 70/30 |
| 2 | **Cleaning and transforming tables** (M4) | Missing data strategy; duplicates; string/date fixes; groupby-agg; merge/join; avoiding chained-assignment bugs | Lecture + worked example | 60/40 |
| 3 | **Lab 4 — The pandas transform layer** | Clean a full month of sales, join the weather feed, produce the daily-KPI DataFrame | Guided lab | 10/90 |
| 4 | **Testing and debugging** (M6) | pytest anatomy; fixtures and parametrize; testing data transformations; reading tracebacks; pdb and the VS Code debugger | Lecture + demo | 60/40 |
| 5 | **Lab 6 — Test the pipeline** | Write unit tests for cleaning/KPI functions; hunt three planted bugs; produce a coverage report | Guided lab | 10/90 |

### Day 5 — Reproducible and Shippable

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Environments and dependencies** (M7) | venv mechanics; pip; pinning with requirements.txt; pyproject.toml; Jupyter kernels bound to environments | Lecture + demo | 60/40 |
| 2 | **Lab 7 — Make it reproducible + capstone kickoff** | Rebuild the project in a clean venv; pin dependencies; verify clone-to-run on a partner's machine; capstone briefing | Guided lab | 20/80 |
| 3 | **Capstone build I** | Assemble ingest → clean → transform → KPI → report end to end | Project work | 0/100 |
| 4 | **Capstone build II + peer review** | Finish the pipeline; run the test suite; open the submission PR; peer code-review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric scoring; quiz; path to SDA-FND-104 and the tracks | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same Wafr Markets sales pipeline. Never introduce a throwaway example codebase — always evolve `wafr-pipeline`. This is what makes the mini-project achievable inside Day 5.
- **Pace control:** Labs 1a and 4 are the most overrun-prone (first contact with Python, and pandas selection semantics respectively). Publish checkpoint tags (`lab1-start`, `lab1-solution`, `lab2-start`, …) in the course repository so stragglers can fast-forward: `git checkout lab3-start` (from Day 2 onward, once Git exists — for Day 1, distribute checkpoint zips).
- **Pairing:** rotate pairs each day. Pair a participant with prior programming exposure with a true beginner; the catalog admits both, and the skill transfer is the point.
- **Environment strategy:** primary = local Python 3.12 + VS Code + Jupyter; fallback = GitHub Codespaces (devcontainer provided) or JupyterHub if the venue's machines are locked down. Verify both the week before delivery.
- **Language:** deliver in English or Arabic; keep all code, identifiers, and commit messages in English (production convention in Saudi enterprise environments — mixed-language identifiers and logs break grep-based operations and code review).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 5 afternoon is deliberately theory-free.
- **Assessment logistics:** daily labs are checked off via checkpoint commits at end of day; the two coding assignments (CA-1 after Day 2, CA-2 after Day 4) are take-home with next-morning review; rubric scoring of the mini-project happens live during Day 5 Hour 5 demos. Collect repository URLs at the end of Day 5 Hour 4 so histories can be inspected before demos begin.

---

# Module 1 — Python Core: Types, Control Flow, Functions, and OOP

## Module Overview

**Purpose.** Everything downstream — NumPy, pandas, testing, the tracks themselves — is written in the language this module teaches. The goal is not syntax tourism; it is the working mental model of Python that data professionals actually use: everything is an object, names bind to objects, mutability has consequences, functions are the unit of design, and classes exist to give data a shape and a vocabulary. Participants leave writing small, correct, readable programs — the raw material of every later lab.

**Business relevance.** Python is the lingua franca of data and AI work in the Saudi market and globally: it is the language of pandas, scikit-learn, PyTorch, and every major LLM SDK. Organisations building national data capabilities need staff who write Python that a colleague can read, review, and extend — not one-off notebook incantations. The difference between a scripted analysis and a structured program is the difference between a person and a capability.

**Industry use cases.**
- A bank's analytics team turns a 400-line ad-hoc script that reconciles card settlements into a module of named, testable functions — the precondition for the audit team signing off on it.
- A logistics operator models shipments as dataclasses with validation, so malformed depot exports fail loudly at parse time instead of corrupting downstream ETAs.
- A government statistics unit standardises on comprehension-based transformation patterns so seasonal staff can read each other's data-preparation code.

**Expected competencies.** After this module a participant can choose appropriate built-in types, write comprehensions and generator expressions, design functions with clear signatures and type hints, avoid the classic mutability traps, define dataclasses and regular classes with dunder methods, and explain when object-oriented design earns its keep in data code.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain Python's object/name model and predict the behaviour of mutable vs immutable values | LO1 |
| 1.2 | Select and use core collections (list, tuple, dict, set) for data-processing tasks | LO1 |
| 1.3 | Write clear control flow and comprehension-based transformations over record collections | LO1, LO5 |
| 1.4 | Design functions with typed signatures, sensible defaults, and no hidden state | LO1, LO4 |
| 1.5 | Model domain records with dataclasses and classes, including validation and dunder methods | LO1 |

## Technical Content

### 1. The Python mental model: objects, names, mutability

Python has no variables in the C sense — it has **names bound to objects**. Every value is an object with an identity, a type, and (sometimes) mutable state. Three consequences drive most beginner bugs and deserve explicit class time:

- **Assignment never copies.** `b = a` binds a second name to the *same* list; `b.append(x)` "changes `a`" because there is only one list. Demonstrate with `id()` and settle it permanently.
- **Mutable vs immutable is a behavioural contract.** `int`, `float`, `str`, `tuple` are immutable — operations return new objects. `list`, `dict`, `set` mutate in place. Data code passes collections between functions constantly; knowing which functions mutate their arguments and which return new values is the difference between a pipeline and a haunted house.
- **Equality vs identity.** `==` asks "same value?", `is` asks "same object?". The only routine legitimate use of `is` in this course is `is None`.

**Instructor note:** run the `a = [1,2]; b = a; b.append(3)` demo *before* naming the rule, and let the room predict the output of `print(a)`. The wrong guesses are the teachable moment.

### 2. Core types and collections for data work

The four workhorse collections, taught through the lens of the sales data they will carry all week:

| Collection | Use in the pipeline | Key properties |
|---|---|---|
| `list` | Ordered rows read from a CSV | Ordered, mutable, allows duplicates; O(n) membership test |
| `tuple` | A fixed record before it earns a class: `(branch, sku, qty, price)` | Immutable, hashable → usable as dict key |
| `dict` | branch_id → branch metadata; SKU → unit price | O(1) lookup by key; insertion-ordered; the shape of JSON |
| `set` | The set of valid SKUs; deduplicating customer IDs | O(1) membership; no duplicates; set algebra (`&`, `-`, `|`) |

Strings get their own ten minutes because raw data arrives as text: slicing, `split`/`join`, `strip`, f-strings (including format specs like `f"{revenue:,.2f}"`), and the discipline of **decoding once at the boundary** — bytes → `str` with an explicit encoding (`utf-8`, and `cp1256` for legacy Arabic Windows exports, which the lab data deliberately includes).

Numbers: `int` is arbitrary-precision; `float` is IEEE-754 doubles — so `0.1 + 0.2 != 0.3`, and money in SAR is handled either as integer halalas or with explicit rounding at report boundaries. This single slide prevents a week of "why is my total 10419.999999998?" questions.

### 3. Control flow and iteration patterns

Beyond `if`/`elif`/`else` and `while`, the patterns that mark idiomatic data code:

- **Iterate over collections directly**, never over `range(len(x))`. `enumerate()` when the index is genuinely needed; `zip()` to walk parallel sequences (column names + row values).
- **Comprehensions** as the default transformation syntax: `[clean(r) for r in rows if r.qty > 0]` reads as a sentence. Dict and set comprehensions for reshaping (`{b["id"]: b for b in branches}`). Rule of thumb: one `for`, at most one `if` — beyond that, write a loop or a function.
- **Generator expressions** for aggregation without materialising: `sum(r.total for r in rows)` — this becomes the "before" picture that NumPy vectorisation replaces in Module 3.
- **Structured error handling**: `try/except` around *the specific line that can fail*, catching *the specific exception* (`ValueError` from `float(...)`, `KeyError` from missing columns), with `else`/`finally` shown once. The anti-pattern `except Exception: pass` is named, shamed, and banned on Day 1 — Module 6 shows the bug it hides.
- **Truthiness pitfalls in data**: `if qty:` skips legitimate zero quantities; `if response:` on an empty-but-successful API payload lies. The rule taught: be explicit — `if qty is not None`, `if len(rows) == 0`.

### 4. Functions as the unit of design

Functions are where structure begins; everything Module 6 tests and Module 5 reviews is a function.

- **Signature design:** few parameters, typed, with keyword-only arguments (`def load_sales(path: Path, *, encoding: str = "utf-8")`) for anything a call site might misorder.
- **The mutable-default trap:** `def add_row(row, batch=[])` shares one list across all calls. The idiom: default to `None`, create inside. This is planted in Lab 1's starter code — every cohort finds it the hard way, which is the point.
- **Return values over prints; pure functions over side effects.** A function that takes rows and returns cleaned rows can be tested, reused in a notebook, and composed into a pipeline. A function that prints and mutates globals can only be watched.
- **Type hints from day one** (`list[dict[str, str]]`, `float | None`): not because the interpreter enforces them, but because VS Code and ruff turn them into live documentation and instant feedback — and because every SDAIA module after this one uses them.
- **Docstrings** in the one-line-summary + args/returns style; participants write them from Lab 1b onward because the capstone rubric scores them.
- **Scope in 5 minutes:** LEGB, why `global` is a design smell, and why the fix is "pass it in, return it out".

### 5. Object-oriented design for data records

OOP is taught as *modelling*, not ceremony:

- **`@dataclass` first.** A `SaleRecord` dataclass with typed fields gives construction, `repr`, and `==` for free, and states the schema of the pipeline in one readable block. `frozen=True` where immutability protects invariants; `__post_init__` for validation (quantities positive, branch code in the known set).
- **Regular classes when behaviour joins data.** `DailyBatch` wraps a list of records and answers questions about them (`total_revenue()`, `by_branch()`); it earns class-hood because it maintains an invariant (all records share one business date) and offers a vocabulary.
- **Dunder methods** as protocol hooks: `__len__` and `__iter__` make `DailyBatch` behave like the collection it is; `__repr__` makes debugging humane. Magic methods are how objects plug into the language, not magic.
- **Inheritance appears in one slide** — a `Discount` base with `PercentDiscount`/`FixedDiscount` — and is immediately balanced with the guidance that data code prefers **composition**: pipelines are built by combining small objects and functions, not by deep hierarchies. `NotImplementedError`-style abstract methods are mentioned; ABCs and protocols are deferred to later modules.
- **When NOT to write a class:** if it has two methods and one is `__init__`, it wanted to be a function. Data code is mostly functions operating on well-named data structures; classes appear where invariants and vocabulary do.

### 6. Common mistakes & production considerations

1. Mutating a list while iterating over it (skipped rows, silent) — iterate over a copy or build a new list.
2. The mutable default argument (planted in Lab 1 starter).
3. `except Exception: pass` around parsing — the malformed rows vanish and so does the audit trail; count and quarantine instead.
4. Floating-point money compared with `==` — compare with rounding at boundaries or use integer halalas.
5. Shadowing built-ins (`list = [...]`, `sum = 0`) — later code breaks mysteriously; ruff flags it.
6. Giant do-everything functions — if it parses, cleans, aggregates, and prints, it cannot be tested; one verb per function.

Production considerations: scripts that will run unattended need `if __name__ == "__main__":` guards so imports are side-effect-free (Module 7 packages them); every parse failure should be *counted and reported*, never silently dropped — regulated Saudi sectors (SAMA-supervised banks, health providers) treat dropped records as an audit finding; and the same cleaning function must serve both the notebook exploration and the production script — one source of truth for logic, established here and enforced through the capstone.

## Code Examples

### Domain records with a dataclass

```python
# src/wafr_pipeline/records.py
"""Domain records for the Wafr Markets sales pipeline.

Rules for this file: stdlib only — no pandas, no requests.
The schema of the whole pipeline lives here, in one readable place.
"""
from dataclasses import dataclass, field
from datetime import date, datetime

VALID_CHANNELS = {"store", "app", "web"}


@dataclass(frozen=True)
class SaleRecord:
    """One POS line item, already validated."""
    branch_code: str          # e.g. "RUH-014"
    sku: str
    quantity: int
    unit_price_sar: float
    channel: str
    sold_at: datetime

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError(f"quantity must be positive, got {self.quantity}")
        if self.unit_price_sar < 0:
            raise ValueError(f"negative price for {self.sku}")
        if self.channel not in VALID_CHANNELS:
            raise ValueError(f"unknown channel: {self.channel!r}")

    @property
    def total_sar(self) -> float:
        return self.quantity * self.unit_price_sar


@dataclass
class DailyBatch:
    """All validated records for one branch-day, plus what we rejected."""
    business_date: date
    records: list[SaleRecord] = field(default_factory=list)   # NEVER =[]
    rejected: int = 0

    def __len__(self) -> int:
        return len(self.records)

    def __iter__(self):
        return iter(self.records)

    def total_revenue(self) -> float:
        return round(sum(r.total_sar for r in self.records), 2)

    def by_branch(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for r in self.records:
            totals[r.branch_code] = totals.get(r.branch_code, 0.0) + r.total_sar
        return {k: round(v, 2) for k, v in totals.items()}
```

### Parsing at the boundary: explicit, counted failures

```python
# src/wafr_pipeline/cleaning.py
"""Raw dict rows -> validated SaleRecord objects.

Every rejection is COUNTED, never silently dropped.
"""
from datetime import datetime
from wafr_pipeline.records import SaleRecord, DailyBatch

DATE_FORMATS = ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M")   # legacy POS mixes both


def parse_sold_at(raw: str) -> datetime:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(raw.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"unparseable timestamp: {raw!r}")


def clean_row(raw: dict[str, str]) -> SaleRecord:
    """One row in, one validated record out — or a loud ValueError."""
    return SaleRecord(
        branch_code=raw["branch_code"].strip().upper(),
        sku=raw["sku"].strip(),
        quantity=int(raw["quantity"]),
        unit_price_sar=float(raw["unit_price_sar"]),
        channel=raw["channel"].strip().lower(),
        sold_at=parse_sold_at(raw["sold_at"]),
    )


def build_batch(rows: list[dict[str, str]], business_date) -> DailyBatch:
    batch = DailyBatch(business_date=business_date)
    for raw in rows:
        try:
            batch.records.append(clean_row(raw))
        except (ValueError, KeyError):
            batch.rejected += 1          # counted, reported, auditable
    return batch
```

### Script entrypoint (import-safe from day one)

```python
# src/wafr_pipeline/report_day1.py
"""Day-1 CLI: python -m wafr_pipeline.report_day1 data/pos_sample.csv"""
import csv
import sys
from datetime import date
from pathlib import Path

from wafr_pipeline.cleaning import build_batch


def main(path: Path) -> None:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    batch = build_batch(rows, business_date=date.today())
    print(f"Accepted {len(batch):,} records, rejected {batch.rejected}")
    print(f"Revenue: SAR {batch.total_revenue():,.2f}")
    for branch, total in sorted(batch.by_branch().items()):
        print(f"  {branch}: SAR {total:,.2f}")


if __name__ == "__main__":            # imports stay side-effect-free
    main(Path(sys.argv[1]))
```

## Hands-on Lab 1 — Clean the Sales Export, Then Give It a Shape

| | |
|---|---|
| **Objective** | Part (a): write cleaning functions over the raw Wafr POS export using core types and comprehensions. Part (b): refactor into `SaleRecord`/`DailyBatch` and a runnable script |
| **Duration** | 2 × 50 minutes (Day 1 Hours 3 and 5) |
| **Setup** | Python 3.12, VS Code, course materials folder with `pos_sample.csv` (5,000 rows, ~3% deliberately malformed) and `lab1_starter.py` |

**Instructions & tasks**

*Part (a) — functions first*
1. *(5 min)* Open `pos_sample.csv` in VS Code; identify by eye the four kinds of dirt (blank quantities, negative prices, two timestamp formats, lowercase branch codes).
2. *(15 min)* Write `parse_sold_at`, `clean_row` in `lab1.py`; run against the first 20 rows in the REPL/Jupyter.
3. *(15 min)* Write `build_batch`-style loop with counted rejections; print accepted/rejected totals.
4. *(10 min)* Replace the reporting loop with comprehensions/generator expressions: total revenue, revenue per branch, set of distinct SKUs sold.
5. *(5 min)* Find the planted mutable-default bug in `lab1_starter.py`'s `add_to_batch(row, batch=[])` and fix it; explain to your partner why every call shared one list.

*Part (b) — object-oriented refactor*
1. *(15 min)* Convert the row tuple/dict into the `SaleRecord` frozen dataclass with `__post_init__` validation; move rejection counting into `DailyBatch`.
2. *(15 min)* Implement `__len__`, `__iter__`, `total_revenue`, `by_branch`; confirm `sum(r.total_sar for r in batch)` works because of `__iter__`.
3. *(10 min)* Create the module layout `src/wafr_pipeline/{records,cleaning,report_day1}.py`; run `python -m wafr_pipeline.report_day1 data/pos_sample.csv`.
4. *(10 min)* Run the same functions from a Jupyter notebook (`from wafr_pipeline.cleaning import build_batch`) — one logic, two front-ends.

**Expected output**
```
$ python -m wafr_pipeline.report_day1 data/pos_sample.csv
Accepted 4,851 records, rejected 149
Revenue: SAR 1,204,417.50
  DMM-003: SAR 188,204.25
  JED-021: SAR 402,881.00
  RUH-014: SAR 613,332.25
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: wafr_pipeline` | Running from wrong directory / src not on path | Run with `python -m` from repo root; Module 7 makes this permanent with an editable install |
| `UnicodeDecodeError` on the CSV | File contains cp1256 Arabic branch notes column | Pass `encoding="utf-8"`, then demonstrate the failing legacy file with `encoding="cp1256"` — boundary decoding lesson |
| All rows rejected | `KeyError` from a misspelled column name caught by the broad handler | Narrow the `except`, print one exception, fix the key — a preview of Module 6's "debug before you guess" |
| Totals differ from expected by ~0.01 | Rounding at the wrong layer | Round once at report boundary, not per record |
| `dataclasses.FrozenInstanceError` | Mutating a frozen record during cleaning | Fix the value *before* constructing the record — validation at the boundary |

**Instructor notes.** Part (a) step 5 (mutable default) and part (b) step 4 (same function from script and notebook) are the two moments that define the course's philosophy — do both on the projector even if pairs finish early. Fast finishers: add a `channel_mix()` method returning percentage of revenue per channel, or make `SaleRecord` orderable by `sold_at` with `order=True`.

## Mini Exercises

**Quiz (5 questions)**
1. `a = [1, 2]; b = a; b += [3]` — what is `a`? → `[1, 2, 3]`; names bind to the same object and `+=` mutates lists in place.
2. Why is `def f(x, acc=[])` a bug? → the default list is created once at definition time and shared across calls.
3. Which collection answers "have we seen this customer ID before?" fastest, and why? → `set`; O(1) hashed membership.
4. When does a group of functions deserve to become a class? → when they share data whose invariants must be maintained (and named).
5. `0.1 + 0.2 == 0.3` → `False`; IEEE-754 floats; compare with rounding or use integer halalas for money.

**Debugging exercise.** `debug_me_m1.py`: a loop removes "bad" rows with `rows.remove(r)` while iterating, so adjacent bad rows survive. Participants must reproduce, explain, and fix (build a new list). The bug is invisible on clean data — connect this to why Module 6 tests use crafted edge-case data.

**Code-review exercise.** Review `review_me_m1.py` (90 lines): shadowed built-in (`sum = 0`), bare `except`, single 60-line function, no type hints, prints instead of returns. Each pair writes ≥4 review comments; compare against the instructor's model review.

**Discussion questions.**
- Your team inherits an analysis where all logic lives in one notebook. What is the *first* function you would extract, and why? (the parse/clean boundary — it is the most reused and most testable)
- Should `SaleRecord` reject a 0-halala price or accept it? Who in the business decides? (data rules are business rules — foreshadows the validation conversations in the tracks)

## Case Study — Script Sprawl at a Riyadh Last-Mile Logistics Startup

**Scenario.** "Naql Express", a Riyadh-based last-mile delivery startup, runs nightly operations on 23 Python scripts written by four different early employees. Each script re-implements its own parsing of the depot CSV export: three different timestamp parsers, two different definitions of "delivered", and one script that silently skips rows with missing coordinates.

**Business context.** The COO's morning dashboard disagreed with the finance reconciliation by 4% for a month. The discrepancy traced to the silent row-skipping script feeding one report but not the other. Investor due diligence is in eight weeks, and the numbers must reconcile.

**Technical challenge.** Consolidate the parsing/cleaning logic into a single shared module with explicit, counted rejection handling — without rewriting all 23 scripts at once.

**Constraints.** One junior engineer available; nightly runs cannot break; the depot export format cannot be changed (third-party WMS); two scripts are cron jobs nobody has edited in a year.

**Solution approach (facilitate, don't lecture).** (1) Write `shipments.py` with a `ShipmentRecord` dataclass and one `clean_row` — the single source of truth; (2) port the two dashboard-feeding scripts first (highest business value), leaving others untouched; (3) every rejection counted and written to a daily `rejects.csv` — the 4% gap becomes visible, explainable, and fixable; (4) port remaining scripts opportunistically as they next need edits. Participants should recognise this as exactly the Lab 1 structure applied under real constraints.

**Discussion questions.**
1. Why port the dashboard scripts first rather than the oldest ones?
2. The silent-skip script's author says "those rows were garbage anyway." What is the professional response? (quarantine and count — garbage is a *finding*, not a deletion)
3. What single artefact would have prevented the 4% incident? (one shared cleaning module — or a rejection report anyone reads)
4. How do you verify the ported scripts produce identical output to the originals? (run both, diff outputs on a week of real files — a golden-file test, formalised in Module 6)

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Lab 1 script processes 5k rows | Performance | < 2 s end to end | `time python -m wafr_pipeline.report_day1 …` |
| Rejected-row accounting | Correctness | 149/149 malformed rows counted, 0 silently dropped | compare against corpus manifest |
| Function length (max) | Code quality | ≤ 25 lines per function | review checklist |
| Type-hint coverage on public functions | Code quality | 100% | ruff / review |
| Mutable-default and bare-except count | Code quality | 0 | ruff rules B006, E722 |
| Same logic callable from script and notebook | Reusability | Yes (demonstrated) | lab step (b)4 |

**Example benchmark table (filled during lab):**

| Version | 5k rows | Rejections counted | Max function length | ruff findings |
|---|---|---|---|---|
| lab1_starter.py | 1.9 s | 0 (silent drops) | 61 lines | 9 |
| lab1-solution | 0.7 s | 149 | 18 lines | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **Names-and-objects box diagram** — *Purpose:* the module's anchor mental model. *Elements:* two name tags (`a`, `b`) with arrows to one list object; a second panel where reassignment moves one arrow; a third where `.append` mutates the shared object. *Style:* flat vector, three-panel strip, English labels with Arabic subtitles. *Designer note:* the arrows are the content — make them thick.
2. **Collection chooser flowchart** — *Elements:* questions ("ordered? need lookup by key? duplicates meaningful?") leading to list/tuple/dict/set with a pipeline example at each leaf. *Style:* compact decision tree, printable A4 poster.
3. **Function anatomy poster** — *Elements:* one annotated signature (`def load_sales(path: Path, *, encoding: str = "utf-8") -> list[SaleRecord]:`) with callouts: typed params, keyword-only marker, return type, docstring position. *Style:* monospace code with labelled arrows.
4. **"When does it deserve a class?" decision strip** — *Elements:* data + behaviour + invariant → class; otherwise function + dict/dataclass; `DailyBatch` vs `clean_row` as the worked contrast. *Style:* two-lane comparison.

### Images (screenshots)
1. **VS Code with type-hint hover and ruff squiggle** — *why:* participants configure the same setup in Hour 1; *content:* `clean_row` with a hover tooltip showing the signature and one deliberate ruff warning.
2. **REPL session of the `id()` demo** — *why:* expected-output reference for the names/objects demo; *content:* `id(a) == id(b)` returning True after aliasing.
3. **Terminal — expected Lab 1 output** — *why:* self-check reference; *content:* exactly the accepted/rejected/revenue block from the lab spec.
4. **Jupyter notebook importing `wafr_pipeline`** — *why:* proves the one-logic-two-front-ends message; *content:* `from wafr_pipeline.cleaning import build_batch` and a chart cell.

### Simulations
1. **Mutable-default incident** — *Setup:* `lab1_starter.py` ships with `add_to_batch(row, batch=[])`. *Expected behaviour:* second file's batch contains the first file's rows; totals inflate. *Learning objective:* definition-time evaluation of defaults; the fix idiom.
2. **Silent-skip audit gap** — *Setup:* branch of the starter with `except Exception: continue` and no counter. *Expected behaviour:* output looks clean, totals are wrong by exactly the rejected rows; participants must add counting and reconcile against the manifest. *Learning objective:* rejection accounting as an audit requirement.

### Interactive Activities
- **"Predict the output" card round (15 min):** eight aliasing/mutability snippets on cards; pairs commit to a prediction before the instructor runs each live. Score kept on the board.
- **Collection sort race (10 min):** 12 task cards ("dedupe customer IDs", "keep rows in file order", "price lookup by SKU"…) physically sorted onto four collection posters; class challenges two placements.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `pos_sample.csv` | Synthetic, course tooling (Faker + KSA branch codes RUH/JED/DMM, SAR amounts, injected dirt) | CSV | 5,000 rows × 7 cols | Lab 1; reused as the small fixture all week |
| `pos_sample_manifest.json` | Course tooling | JSON | 1 file | Ground truth: which rows are malformed and why (for rejection reconciliation) |
| `legacy_export_cp1256.csv` | Course tooling | CSV (cp1256) | 200 rows | Encoding demonstration |

### Demo Requirements
- **Instructor demo:** the aliasing/`id()` demo; then live-refactor one messy starter function into a typed, docstringed function in under 5 minutes — rehearse it, the speed is the message.
- **Student demo:** two volunteer pairs walk through their `DailyBatch` design at end of Hour 5; class challenges one design decision each.
- **Expected outputs:** working `python -m wafr_pipeline.report_day1`, zero ruff findings on the two starter rules (B006, E722), rejection count matching the manifest.

---

# Module 2 — Data Structures and File/API Data Handling

## Module Overview

**Purpose.** Real data does not arrive as clean Python objects; it arrives as files with wrong encodings, JSON with surprise nulls, and APIs that paginate, throttle, and fail. This module teaches the acquisition layer: choosing the right in-memory structure for the job, reading files safely and portably, consuming REST APIs defensively, and validating everything at the boundary so the rest of the pipeline can trust its inputs.

**Business relevance.** Data acquisition is where most analyst time is actually spent and where most data-quality incidents are born. Organisations consuming the Saudi Open Data portal, internal ERP exports, and third-party APIs need staff who can build ingestion that fails loudly, retries politely, and documents what it rejected. A team whose pipelines start with a hardened ingestion layer spends its time on analysis; a team whose pipelines start with `pd.read_csv` and hope spends its time on archaeology.

**Industry use cases.**
- A ministry analytics unit ingests monthly Excel/CSV drops from 13 regional offices, each with slightly different headers — normalised by one shared ingestion module with per-office rejection reports.
- A retail chain enriches sales data with weather via a public API, with caching and retry logic so a flaky third party cannot stall the nightly run.
- A fintech pulls exchange rates from a provider API, validating schema and value ranges before a single rate touches pricing code.

**Expected competencies.** After this module a participant can select dict/set/Counter/defaultdict structures deliberately, traverse and reshape nested JSON, read CSV/JSON files with pathlib and explicit encodings, call REST APIs with requests (timeouts, retries, pagination, status handling), keep credentials out of code, and validate external data at the boundary.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Choose appropriate data structures (dict, set, Counter, defaultdict, nested combinations) for acquisition tasks | LO1 |
| 2.2 | Read and write CSV/JSON files robustly with pathlib, context managers, and explicit encodings | LO5 |
| 2.3 | Consume a paginated REST API with timeouts, retries, and status-code handling | LO5 |
| 2.4 | Validate and reshape external data at the boundary into typed records | LO1, LO5 |
| 2.5 | Keep secrets and environment-specific paths out of source code | LO5, LO6 |

## Technical Content

### 1. Choosing structures deliberately

Module 1 introduced the collections; this module makes selection automatic:

- **dict as index:** `{sku: product}` built once, O(1) lookups forever. The pattern `by_key = {p["sku"]: p for p in products}` appears in every ingestion job ever written.
- **`collections.Counter`** for frequency questions (`Counter(r.branch_code for r in records).most_common(5)`) and **`defaultdict(list)`** for grouping (`groups[r.branch_code].append(r)`) — the two imports that eliminate 80% of clumsy grouping loops. pandas' `groupby` (Module 4) is this pattern industrialised.
- **set algebra as reconciliation:** `expected_branches - reporting_branches` answers "who hasn't sent today's file?" in one line — a real operational report.
- **Nested structures mirror JSON:** `dict[str, list[dict[str, Any]]]` is what an API response actually is. Teach reading a shape aloud ("a dict of branch code to list of row dicts") and flattening early — deep nesting is where bugs hide. Convert to flat records (Module 1's dataclasses) as soon as validation passes.
- **Tuples as composite keys:** `(branch_code, business_date) -> total` — hashable, self-documenting with a comment, and the mental model for pandas MultiIndex later.

### 2. Files done right

- **pathlib everywhere:** `Path` objects compose with `/`, know their parents and suffixes, and are portable across the Windows laptops in the room and the Linux servers in production. String-concatenated paths are banned from lab code.
- **Context managers always:** `with path.open(...) as f:` guarantees closure on success or exception. Name the failure it prevents: file handles exhausted mid-run on a directory of 400 files.
- **Encodings are explicit.** `open()` without `encoding=` uses a platform-dependent default (still cp1252/cp1256 on many Windows machines) — the single most common "works on my machine" in mixed-OS Saudi offices. Course rule: every `open()` names its encoding; UTF-8 unless the source dictates otherwise; the lab includes a genuine cp1256 legacy file.
- **The csv module before pandas:** `csv.DictReader` teaches what a delimited file *is* — including quoting, embedded commas in Arabic product names, and the `newline=""` requirement on Windows. Participants who meet pandas first treat files as magic; participants who meet csv first can debug pandas.
- **Writing outputs:** atomic-ish pattern — write to `report.tmp`, then `Path.replace()` to the final name — so a crash never leaves a half-written report that a downstream consumer ingests.

### 3. JSON: the shape of modern data

- `json.load`/`json.dump` and the type mapping (object→dict, array→list, null→None, numbers→int/float). Round-trip caveats: JSON has no dates, no tuples, no NaN — dates travel as ISO-8601 strings and are parsed at the boundary (`datetime.fromisoformat`).
- **Defensive access:** `payload["data"]["stations"][0]["temp_c"]` is five KeyErrors waiting to happen. Idioms: `.get()` with sentinel checks for optional fields, explicit `KeyError` for *required* fields (a missing required field should crash loudly, not default silently), and one `validate_payload()` function per source that turns "whatever arrived" into "records we trust".
- **JSON Lines (`.jsonl`)** for record streams: one object per line, appendable, streamable — the format of most modern data logs and LLM training corpora; participants read one with a plain file iterator.
- `json.dumps(..., ensure_ascii=False, indent=2)` so Arabic text stays readable in output files rather than becoming `رياض` escape soup.

### 4. Consuming REST APIs defensively

Built on `requests` against the course's local weather API (offline-friendly stub of a public weather service):

- **Anatomy of the call:** method + URL + `params=` (never hand-built query strings) + headers; `response.status_code`, `response.json()`.
- **The non-negotiable trio:** (1) **timeout on every call** — `requests` waits forever by default, and a hung nightly job is an incident; (2) **`raise_for_status()`** or explicit status handling — a 500's body is an error page, and `response.json()` on it produces a confusing secondary exception far from the cause; (3) **retry with backoff for 429/5xx** — a `for attempt in range(3)` loop with `time.sleep(2 ** attempt)` teaches the concept before anyone reaches for a library.
- **Pagination:** loop on `page` param or follow a `next` link until exhausted, accumulating records — with a hard max-pages guard against an API that never says stop.
- **Secrets out of code:** API keys come from environment variables (`os.environ["WAFR_WEATHER_KEY"]`) or a git-ignored `.env` loaded at startup — never literals, never committed. Module 5 shows *why* with git history; here the habit is installed.
- **Cache during development:** save each response to `data/cache/{date}.json` and read the cache when present — faster labs, polite to providers, and reproducible runs. This is a baby version of the caching every production ingestion layer has.

### 5. Validation at the boundary

The module's architectural idea: **outside data is untrusted until validated, and validation happens once, at the edge.**

- Every source (CSV, API) gets a `to_records()` function that returns `list[SaleRecord]` / `list[WeatherReading]` plus a rejection count — downstream code never sees raw dicts.
- Range and sanity checks belong here: temperatures in −10…60 °C for KSA, quantities positive, timestamps within the requested window. A reading of 999 °C is a sensor sentinel, not a heatwave — and it will silently destroy the mean if allowed through (NumPy makes this concrete in Module 3).
- Schema drift is detected loudly: if the API adds/renames fields, the required-key check fails on day one, not in a quarterly report.

### 6. Common mistakes & production considerations

1. `requests.get(url)` with no timeout — the hung-job classic.
2. Calling `.json()` before checking status — masking the real HTTP error with a JSON decode error.
3. Platform-default encodings — works on the author's laptop, garbles Arabic on the server.
4. Building paths with `+ "/" +` — breaks the moment code changes OS.
5. Trusting `payload.get("value", 0)` for required fields — a missing field becomes a plausible zero and poisons every aggregate downstream.
6. Committing an API key "temporarily" — Module 5 demonstrates that git history remembers forever.

Production considerations: ingestion jobs are *re-run* — design them idempotent (same inputs → same outputs, cache keyed by date); log source, row counts, and rejection counts on every run (the one-line run summary is what on-call reads); respect provider terms and rate limits — and under PDPL, data pulled from APIs containing personal data inherits handling obligations the moment it lands on disk, so know what your ingestion stores and for how long.

## Code Examples

### File ingestion with explicit boundaries

```python
# src/wafr_pipeline/ingest_files.py
"""POS CSV files -> validated records. All rejection counted."""
import csv
from datetime import date
from pathlib import Path

from wafr_pipeline.cleaning import build_batch
from wafr_pipeline.records import DailyBatch

RAW_DIR = Path("data/raw")            # overridden by config in Module 7


def read_pos_file(path: Path, *, encoding: str = "utf-8") -> list[dict[str, str]]:
    """One file -> raw dict rows. newline='' matters on Windows."""
    with path.open(newline="", encoding=encoding) as f:
        return list(csv.DictReader(f))


def ingest_day(business_date: date, raw_dir: Path = RAW_DIR) -> DailyBatch:
    """All branch files for one date -> one validated batch."""
    pattern = f"pos_{business_date:%Y%m%d}_*.csv"
    files = sorted(raw_dir.glob(pattern))
    if not files:
        raise FileNotFoundError(f"no POS files matching {pattern} in {raw_dir}")

    rows: list[dict[str, str]] = []
    for path in files:
        rows.extend(read_pos_file(path))
    batch = build_batch(rows, business_date)
    print(f"[ingest] {business_date}: {len(files)} files, "
          f"{len(batch):,} accepted, {batch.rejected} rejected")
    return batch
```

### Defensive API client with cache, timeout, retry, pagination

```python
# src/wafr_pipeline/weather_api.py
"""Weather enrichment client for the course API (stub of a public service).

Non-negotiables demonstrated: timeout, status check, retry, cache, no keys in code.
"""
import json
import os
import time
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import requests

BASE_URL = os.environ.get("WAFR_WEATHER_URL", "http://localhost:8001")
CACHE_DIR = Path("data/cache")


@dataclass(frozen=True)
class WeatherReading:
    city: str
    observed_at: datetime
    temp_c: float

    def __post_init__(self) -> None:
        if not (-10.0 <= self.temp_c <= 60.0):        # KSA sanity range
            raise ValueError(f"implausible temperature {self.temp_c} for {self.city}")


def _fetch_page(day: date, page: int) -> dict:
    for attempt in range(3):
        resp = requests.get(
            f"{BASE_URL}/v1/readings",
            params={"date": day.isoformat(), "page": page},
            headers={"X-Api-Key": os.environ["WAFR_WEATHER_KEY"]},
            timeout=10,                               # NEVER omit
        )
        if resp.status_code in (429, 500, 502, 503):
            time.sleep(2 ** attempt)                  # backoff: 1s, 2s, 4s
            continue
        resp.raise_for_status()                       # 4xx: our bug — fail loudly
        return resp.json()
    raise RuntimeError(f"weather API unavailable after 3 attempts (page {page})")


def fetch_readings(day: date) -> list[WeatherReading]:
    """All pages for one day, cached to disk for reproducible re-runs."""
    cache = CACHE_DIR / f"weather_{day:%Y%m%d}.json"
    if cache.exists():
        payload_pages = json.loads(cache.read_text(encoding="utf-8"))
    else:
        payload_pages, page = [], 1
        while page <= 50:                             # hard guard: never loop forever
            payload = _fetch_page(day, page)
            payload_pages.append(payload)
            if not payload["has_next"]:
                break
            page += 1
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(payload_pages, ensure_ascii=False), encoding="utf-8")

    readings, rejected = [], 0
    for payload in payload_pages:
        for item in payload["readings"]:              # required keys: KeyError = loud
            try:
                readings.append(WeatherReading(
                    city=item["city"],
                    observed_at=datetime.fromisoformat(item["observed_at"]),
                    temp_c=float(item["temp_c"]),
                ))
            except (ValueError, KeyError):
                rejected += 1
    print(f"[weather] {day}: {len(readings)} readings, {rejected} rejected")
    return readings
```

### Structure selection in ten lines

```python
# snippets/structures_demo.py — the grouping/reconciliation idioms
from collections import Counter, defaultdict

by_branch: defaultdict[str, list] = defaultdict(list)
for r in batch:
    by_branch[r.branch_code].append(r)                 # grouping

top_skus = Counter(r.sku for r in batch).most_common(5)  # frequency

expected = {"RUH-014", "JED-021", "DMM-003", "RUH-101"}
missing_today = expected - set(by_branch)              # reconciliation
```

## Hands-on Lab 2 — Build the Ingestion Layer

| | |
|---|---|
| **Objective** | Ingest a week of POS CSV files and the weather API into validated record lists with counted rejections and a run summary |
| **Duration** | 50 minutes (Day 2 Hour 3) |
| **Setup** | Lab 1 solution; course weather stub running (`python -m course_tools.weather_stub`); `data/raw/` with 7×4 branch files (one file cp1256-encoded, one branch missing on day 3); `WAFR_WEATHER_KEY` in a provided `.env` |

**Instructions & tasks**

1. *(10 min)* Implement `read_pos_file` + `ingest_day` with pathlib globbing; run for day 1 and reconcile counts against the manifest.
2. *(5 min)* Hit the cp1256 file: diagnose the `UnicodeDecodeError`, add per-file encoding handling via the provided `encodings.json` sidecar.
3. *(15 min)* Implement `_fetch_page`/`fetch_readings`: timeout, status handling, 3-attempt backoff, pagination with the max-page guard, disk cache. Verify a second run says `[cache]` and makes zero HTTP calls (stub logs requests).
4. *(10 min)* Reconciliation report: using set algebra, print branches expected-but-missing per day; using `Counter`, print top-5 SKUs for the week.
5. *(5 min)* Simulate failure: instructor flips the stub to return 503 for 20 seconds — confirm your retry loop rides it out and the run completes.
6. *(5 min)* Write the run summary line (files, accepted, rejected per source) and save the week's validated output to `data/staged/week1.jsonl` (`ensure_ascii=False`).

**Expected output**
```
$ python -m wafr_pipeline.run_ingest --week 2026-W23
[ingest] 2026-06-01: 4 files, 19,384 accepted, 616 rejected
...
[weather] 2026-06-03: 72 readings, 3 rejected
[reconcile] 2026-06-03: missing branches: {'JED-021'}
[top-skus] WTR-1.5L (14,210), KHB-BRD (11,873), LBN-1L (9,442), ...
Staged 135,512 records -> data/staged/week1.jsonl
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `KeyError: 'WAFR_WEATHER_KEY'` | `.env` not loaded into the shell/session | Export the var or use the provided loader; discuss why the key is not in code |
| Second run still hits the API | Cache path built with string concat / wrong date format | Use `Path` and `f"{day:%Y%m%d}"`; print the cache path once |
| `requests.exceptions.ConnectionError` | Weather stub not running | `python -m course_tools.weather_stub` in a second terminal |
| Retry loop spins forever on 404 | 404 treated as retryable | Only 429/5xx retry; 4xx is *our* bug — `raise_for_status()` |
| Arabic product names as `ر…` in the JSONL | `ensure_ascii` default | `json.dumps(..., ensure_ascii=False)` |

**Instructor notes.** Task 5 (live 503 storm) is the moment the retry code stops being ceremony — announce it dramatically. Watch for pairs calling `.json()` before the status check in task 3; let one hit the confusing `JSONDecodeError`, then debug it publicly. Fast finishers: add `--force-refresh` to bypass the cache, or dedupe rows replayed across files with a `set` of `(branch, sku, sold_at)` keys.

## Mini Exercises

**Quiz (5 questions)**
1. Why must every `requests` call have a `timeout`? → default is wait-forever; a hung call becomes a hung job.
2. A required field is missing from an API payload. `.get(field, 0)` or `payload[field]`? → `[field]`: required means a loud KeyError, not a silent plausible zero.
3. What does `newline=""` do in `open()` for csv on Windows? → prevents blank-row/CRLF mangling; csv module handles line endings itself.
4. Which structure answers "which expected branches sent no file today?" in one expression? → set difference.
5. Why cache API responses to disk during development? → reproducible runs, speed, provider politeness — and idempotent re-runs.

**Debugging exercise.** `debug_me_m2.py` calls `.json()` on a 500 response and crashes with `JSONDecodeError` two functions away from the real failure. Participants must find the true cause from the traceback and add `raise_for_status()` — the lesson is that the *first* error in causal order matters, not the loudest.

**Code-review exercise.** Review a PR that hard-codes `C:\Users\fahad\data\`, embeds an API key literal, retries on 404, and swallows `UnicodeDecodeError` with `errors="ignore"`. Four findings minimum; the `errors="ignore"` one matters most — it silently deletes Arabic characters instead of failing.

**Discussion questions.**
- The weather provider offers a bulk daily file *and* a REST API. Which do you ingest, and what decides it? (volume, freshness needs, failure modes, cost)
- Your ingestion rejected 616 rows this week. Who should see that number, and in what form? (rejection reporting as a product, not a log line)

## Case Study — Consolidating Regional Reporting at a National Statistics Unit

**Scenario.** A statistics unit in a large Saudi ministry receives monthly indicator files from 13 regional offices: nominally the same CSV template, in practice three header spellings, two encodings, one office that exports from an ancient system with `dd/mm/yyyy` dates, and occasional Excel files renamed to `.csv`. Two analysts spend the first week of every month hand-fixing files before analysis can start.

**Business context.** The unit publishes a national dashboard with a statutory monthly deadline. Last quarter, a silently mis-parsed date column shifted one region's figures a month forward; the correction required a public erratum.

**Technical challenge.** Build one ingestion module that normalises all 13 variants into validated records, quarantines what it cannot parse, and produces a per-office data-quality report — turning the week of hand-fixing into a 20-minute review of the rejection report.

**Constraints.** Offices cannot be forced onto a new template this fiscal year; the unit's machines are Windows with no admin rights (pure-Python solutions only); the erratum made leadership allergic to silent fixes — every transformation must be logged.

**Solution approach (facilitate, don't lecture).** (1) A per-office `sources.json` sidecar: encoding, header mapping, date format — configuration, not code forks; (2) one `to_records()` boundary with counted, categorised rejections written to `quarantine/{office}/{month}.csv`; (3) the data-quality report ranks offices by rejection rate — which, in three months of real use, is what finally motivates offices to fix their exports; (4) the renamed-Excel case is detected by sniffing magic bytes, not extension, and rejected with a human-readable reason.

**Discussion questions.**
1. Why is the per-office sidecar better than 13 `if office == …` branches? (data-driven config scales, is reviewable, and non-programmers can edit it)
2. The erratum came from a *successful* parse of wrong data. Which validation would have caught the month-shift? (range check: indicator dates must fall inside the reporting month)
3. Where is the line between "normalise silently" and "reject loudly"? (normalisations are logged and reversible; semantic guesses are rejections)
4. Sketch the one-page data-quality report a department head would actually read.

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Week ingest wall-clock (28 files + API, warm cache) | Performance | < 10 s | `time` on lab run |
| API calls on second (cached) run | Efficiency | 0 | stub request log |
| Rejection reconciliation vs manifest | Correctness | 100% accounted, categorised | manifest diff |
| Hard-coded paths / keys in source | Code quality | 0 | grep + review |
| Retry behaviour under 503 storm | Reliability | run completes; ≤ 3 attempts/page; backoff observed | stub log timestamps |
| Staged JSONL readability | Correctness | Arabic intact (no `\u` escapes) | spot check |

**Example benchmark table (filled during lab):**

| Run | Files | API calls | Accepted | Rejected | Wall-clock |
|---|---|---|---|---|---|
| Cold (first) | 28 | 21 | 135,512 | 4,289 | 24 s |
| Warm (cached) | 28 | 0 | 135,512 | 4,289 | 7 s |
| During 503 storm | 28 | 29 (8 retries) | 135,512 | 4,289 | 41 s |

## Required Visuals and Training Assets

### Diagrams
1. **Ingestion boundary diagram** — *Purpose:* the module's anchor. *Elements:* untrusted zone (files, API, red tint) → boundary wall with `to_records()` gates → trusted zone (typed records, green tint); a quarantine bin with a counter beneath each gate. *Style:* two-zone flow, English labels with Arabic subtitles.
2. **API call lifecycle flowchart** — *Elements:* request → timeout? → status 2xx/4xx/429/5xx branches → retry loop with backoff timer → parse → validate. *Style:* flowchart; the happy path is the thin one — that's the joke and the lesson.
3. **JSON→Python type map poster** — *Elements:* the six JSON types with arrows to Python types; callout boxes for the missing ones (dates, NaN, tuples). *Style:* two-column poster, printable A4.
4. **Pagination loop strip** — *Elements:* pages 1..n accumulating into one list; the `has_next` flag; the max-page guard as an emergency brake. *Style:* comic-strip sequence.

### Images (screenshots)
1. **VS Code with `data/raw/` tree and one open POS file** — *why:* participants recognise the dirt visually; *content:* mixed timestamp formats highlighted.
2. **Terminal — the 503-storm run** — *why:* expected-behaviour reference; *content:* retry/backoff log lines with visible 1s/2s/4s gaps.
3. **Stub request log showing zero calls on cached run** — *why:* proves the cache; *content:* two run blocks, second one empty.
4. **`.env` file next to `.gitignore`** — *why:* the secret-hygiene habit; *content:* key in `.env`, `.env` line in `.gitignore`, both visible.

### Simulations
1. **503 storm** — *Setup:* stub flag `--fail-window 20`. *Expected:* naive code crashes; retry code completes with logged backoff. *Learning objective:* transient vs permanent failure handling.
2. **Schema drift** — *Setup:* stub `--v2` renames `temp_c` to `temperature_c`. *Expected:* required-key validation fails on the first page with a clear error naming the missing key. *Learning objective:* loud schema-drift detection beats silent defaults.
3. **Encoding trap** — *Setup:* one branch file in cp1256. *Expected:* explicit decode failure → sidecar-driven per-file encoding. *Learning objective:* encodings are metadata, not guesswork.

### Interactive Activities
- **"Trust or reject?" card round (10 min):** 12 payload cards (temp 999, missing key, extra key, empty list, `"N/A"` string in numeric field…) — teams sort into accept / normalise-and-log / reject, defend choices.
- **Structure charades (10 min):** task on screen, pairs hold up the collection card (dict/set/Counter/defaultdict) they'd reach for; disagreements argued out.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `data/raw/pos_YYYYMMDD_*.csv` (28 files) | Course tooling: 4 branches × 7 days, injected dirt, one cp1256 file, one missing branch-day | CSV | ~140k rows total | Lab 2 ingestion; feeds Modules 3–4 |
| Weather stub API | `course_tools.weather_stub` (Flask, offline) | REST/JSON | 3 cities × 24 h × 7 d | API consumption practice; enrichment in Module 4 |
| `sources/encodings.json` | Course handout | JSON | 1 file | Per-file encoding sidecar pattern |
| `data/staged/week1.jsonl` | Produced by Lab 2 | JSONL | ~135k records | Input to Module 3 |

### Demo Requirements
- **Instructor demo:** live `curl`/browser hit of the stub, then the same via requests with the timeout deliberately set to 0.001 to show the exception; the 503-storm flip.
- **Student demo:** one pair walks through their retry loop line by line; class identifies which status codes retry and which fail fast.
- **Expected outputs:** staged JSONL, reconciliation report, zero API calls on warm run — the artefacts Module 3 consumes.

---

# Module 3 — NumPy Arrays and Vectorised Computation

## Module Overview

**Purpose.** Python loops over 135,000 records work; over 135 million they do not. NumPy is the reason Python owns numerical computing: a typed, contiguous array object and a library of vectorised operations that run at C speed. This module rewires how participants think about computation — from "for each row" to "for the whole array at once" — and teaches the memory model, indexing, broadcasting, and numerical hygiene that pandas, scikit-learn, and PyTorch all assume.

**Business relevance.** Vectorised thinking is the single largest performance lever a data professional controls. The difference between a 40-minute loop and a 2-second array operation decides whether an analysis is interactive or overnight, whether a national-scale dataset fits the nightly window, and whether the compute bill is reasonable. Every ML framework participants will meet in the tracks (scikit-learn in SDA-AIE-111, tensors everywhere after) is NumPy semantics with different clothes.

**Industry use cases.**
- A utilities analytics team computes per-meter consumption statistics across 8 million smart meters — a pandas/NumPy aggregation measured in seconds, not the legacy VBA hours.
- A crowd-management team processes gate-sensor counts during Hajj at minute resolution, using boolean masks to isolate surge windows across thousands of sensors simultaneously.
- A retail pricing team simulates discount scenarios as array operations over the full SKU catalogue, testing 200 scenarios interactively in a notebook.

**Expected competencies.** After this module a participant can create and inspect ndarrays (dtype, shape), replace row loops with vectorised expressions and ufuncs, select with boolean masks and fancy indexing, reason about axis semantics in reductions, apply broadcasting deliberately, distinguish views from copies, handle NaN correctly, and benchmark loop-vs-vector honestly.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Create and inspect ndarrays; choose dtypes deliberately | LO2 |
| 3.2 | Replace Python loops with vectorised expressions and ufuncs, and measure the speedup | LO2 |
| 3.3 | Select and update data with boolean masks and fancy indexing | LO2 |
| 3.4 | Apply reductions along the correct axis and explain the result's shape | LO2 |
| 3.5 | Use broadcasting to combine arrays of different shapes, and predict when it fails | LO2 |
| 3.6 | Avoid view/copy and NaN pitfalls in numerical code | LO2, LO4 |

## Technical Content

### 1. Why arrays: the memory model

A Python list of 1M floats is 1M pointers to 1M boxed objects scattered across the heap; every `+` dispatches dynamically. An ndarray is **one contiguous block of typed memory** plus metadata (dtype, shape, strides). Consequences:

- **Speed:** operations compile to tight C loops over contiguous memory (and use SIMD). The lab measures ~50–200× on realistic operations — participants generate this number themselves, which is why they believe it.
- **Memory:** `np.float64` costs 8 bytes/element vs ~56 for a boxed Python float. `arr.nbytes` makes it visible.
- **Discipline:** one dtype per array. `np.array([1, 2, "3"])` silently becomes strings — the classic ingestion accident; check `arr.dtype` before trusting any computation.
- **dtype choices that matter in practice:** `float64` default for money/measures; `int64` for counts; the NaN trap — integer arrays cannot hold NaN, so a "count" column with missing values arrives as float (this explains a thousand confused pandas moments in Module 4); `datetime64` exists and powers time arithmetic.

### 2. Vectorisation and ufuncs

The core move: `revenue = qty * price` where both are arrays — no loop, elementwise at C speed.

- **Ufuncs** (`np.log1p`, `np.round`, `np.maximum`, comparison operators) apply elementwise and return new arrays. Whole-array arithmetic composes: `discounted = np.round(revenue * (1 - disc_rate), 2)`.
- **Reductions:** `arr.sum()`, `.mean()`, `.std()`, `.min()`, `.max()`, `np.percentile(arr, [50, 95])`. Teach `.sum()` on a 135k-element array vs `sum()` builtin on a list — both correct, one 100× faster; then note `np.sum` on a *list* pays conversion cost every call: convert once, compute many.
- **`np.where(cond, a, b)`** as vectorised if/else: `np.where(temp_c > 38, revenue_cold_drinks * 1.0, 0.0)` — the conditional logic of the KPI engine without a single `if`.
- **Honest benchmarking:** `time.perf_counter()` around both versions, warm runs, same data. The lab's expected table anchors intuition: milliseconds vs seconds.

### 3. Indexing: slices, masks, fancy indexing

- **Slicing** works like lists but per-axis: `matrix[:5, 2]` — and 2-D thinking starts here (rows × columns, exactly a table).
- **Boolean masks are queries:** `revenue[branch == "RUH-014"]`, `qty[(qty > 0) & (price < 100)]` — note `&`/`|` with parentheses, not `and`/`or` (which raise the famously cryptic "truth value of an array is ambiguous" — show the error on purpose, once, on the projector).
- **Masked assignment repairs data:** `temp[temp > 60] = np.nan` — the sentinel-999 repair from Module 2, now in one line.
- **Fancy indexing** with an integer array (`arr[order]` where `order = np.argsort(revenue)[::-1]`) — top-N reports in two lines.
- **`np.argsort` / `np.argmax`** return *positions*, which then index other arrays — the idiom behind "which branch had the peak hour?"

### 4. Axis logic and 2-D data

A branches × hours revenue matrix makes axis semantics concrete:

- `matrix.sum(axis=0)` collapses rows → per-hour totals (shape `(24,)`); `axis=1` collapses columns → per-branch totals (shape `(4,)`). Rule that sticks: **the axis you name is the axis that disappears.**
- `keepdims=True` preserves shape for subsequent broadcasting — introduced exactly where it is needed (share-of-day normalisation).
- Reductions with axes are the mental model for pandas `groupby` and for tensor operations in the tracks — say this out loud; it is why the module exists.

### 5. Broadcasting: combining shapes deliberately

Broadcasting rules in one slide: align shapes from the right; dimensions match if equal or one of them is 1; missing dimensions are treated as 1.

- Scalar × array is broadcasting's trivial case (everyone already used it).
- `(4, 24) matrix / (4, 1) row_totals` → per-branch share of day. `(4, 24) - (24,) hourly_mean` → per-hour deviation. Both drawn as shape diagrams, not just code.
- **Predict-the-shape drills** before running anything — broadcasting errors caught at design time are free; at runtime they are either a loud `ValueError` (fine) or a silently *wrong-shaped but valid* result (expensive). Example of the dangerous case: `(4,) + (4, 1)` yields `(4, 4)` — plausible-looking garbage.

### 6. Common mistakes & production considerations

1. **Views vs copies:** slices are views — mutating `window = arr[:100]` mutates `arr`. `.copy()` when independence is intended. (Planted in the lab.)
2. `np.nan` poisons plain reductions: `arr.mean()` → nan; use `np.nanmean` *after deciding* whether missing-ignored is the right business answer — `nanmean` is a decision, not a fix.
3. `==` with NaN is always False; `np.isnan(arr)` is the test.
4. Mixed-type ingestion producing `dtype=object` arrays — all the syntax, none of the speed; check dtype first when "NumPy is slow".
5. Growing arrays with `np.append` in a loop — quadratic; accumulate in a list, convert once.
6. Float equality: `np.isclose`/`np.allclose` for comparisons, never `==` on computed floats — this becomes the backbone of numerical tests in Module 6.

Production considerations: memory is the real constraint at scale — a `float64` array of 500M elements is 4 GB before any temporary, and chained expressions create temporaries (mention `out=` and chunking as the escape hatches, deferred to SDA-DSC-215 for the distributed answer); random data needs `np.random.default_rng(seed)` for reproducible simulations (rubric requirement in the capstone's scenario task); and vectorised code is *review-friendly* — a masked expression states intent where a 15-line loop hides it.

## Code Examples

### From records to arrays

```python
# src/wafr_pipeline/kpi_arrays.py
"""Columnar arrays from validated records: convert once, compute many."""
import numpy as np

from wafr_pipeline.records import DailyBatch


def to_columns(batch: DailyBatch) -> dict[str, np.ndarray]:
    """Records -> column arrays. The one loop we keep."""
    return {
        "qty":    np.array([r.quantity for r in batch], dtype=np.int64),
        "price":  np.array([r.unit_price_sar for r in batch], dtype=np.float64),
        "branch": np.array([r.branch_code for r in batch]),          # dtype '<U7'
        "hour":   np.array([r.sold_at.hour for r in batch], dtype=np.int64),
    }
```

### The KPI engine, loop vs vector

```python
# benchmarks/loop_vs_vector.py
"""The module's centrepiece: same answers, different centuries."""
import time
import numpy as np


def kpis_loop(records) -> dict:
    total = 0.0
    high_value = 0
    for r in records:                       # 135k iterations of interpreter
        line = r.quantity * r.unit_price_sar
        total += line
        if line > 500:
            high_value += 1
    return {"revenue": round(total, 2), "high_value_lines": high_value}


def kpis_vector(cols) -> dict:
    line = cols["qty"] * cols["price"]      # one C loop
    return {
        "revenue": float(np.round(line.sum(), 2)),
        "high_value_lines": int((line > 500).sum()),   # mask -> count idiom
    }


def bench(fn, arg, n=5) -> float:
    """Best-of-n wall clock. Convert data OUTSIDE the timed region —
    including the list->array conversion in the timing is the classic
    way to 'prove' NumPy is slow."""
    times = []
    for _ in range(n):
        t0 = time.perf_counter()
        fn(arg)
        times.append(time.perf_counter() - t0)
    return min(times)
```

### Masks, axes, broadcasting on the branch×hour matrix

```python
# snippets/matrix_demo.py
import numpy as np

rng = np.random.default_rng(42)             # reproducible demo data
branches = np.array(["RUH-014", "RUH-101", "JED-021", "DMM-003"])
revenue = rng.gamma(shape=2.0, scale=900.0, size=(4, 24)).round(2)  # (branches, hours)

hourly_total = revenue.sum(axis=0)          # (24,)  — axis 0 disappears
branch_total = revenue.sum(axis=1)          # (4,)

# broadcasting: share of each branch's day per hour
share = revenue / revenue.sum(axis=1, keepdims=True)      # (4,24)/(4,1) -> (4,24)
assert np.allclose(share.sum(axis=1), 1.0)                # never == on floats

# masks: which branch-hours beat the network-wide hourly mean?
hot = revenue > hourly_total.mean()
peak_hour_per_branch = revenue.argmax(axis=1)             # positions, not values

# repair: sentinel temperatures -> NaN, then a *decided* nanmean
temp = np.array([31.0, 34.5, 999.0, 38.2, 36.0])
temp[temp > 60] = np.nan
mean_temp = np.nanmean(temp)                # decision: ignore missing readings
```

## Hands-on Lab 3 — Vectorise the KPI Engine

| | |
|---|---|
| **Objective** | Replace the loop-based KPI computation with NumPy, produce the branch×hour revenue matrix, and measure the speedup honestly |
| **Duration** | 50 minutes (Day 3 Hour 3) |
| **Setup** | Lab 2 staged data (`week1.jsonl`, ~135k records); `pip install numpy`; `git checkout lab3-start` |

**Instructions & tasks**

1. *(5 min)* Load staged records; build column arrays with `to_columns`; verify dtypes (`int64`, `float64` — anyone with `object` has dirty data escaping Module 2's boundary; find it).
2. *(10 min)* Implement `kpis_vector` (revenue, high-value-line count, p50/p95 line value via `np.percentile`); run both versions; assert equality with `np.isclose`.
3. *(10 min)* Benchmark loop vs vector with `perf_counter` (best of 5); fill the benchmark table; compute your speedup factor.
4. *(10 min)* Build the `(branches, hours)` revenue matrix (hint: accumulate with `np.add.at` or a masked loop over 4 branches — discuss why 4 iterations is fine); compute per-hour network totals, per-branch peak hour (`argmax`), and share-of-day via broadcasting with `keepdims`.
5. *(10 min)* Weather repair: load the week's temperatures, mask sentinel values to NaN, compute `nanmean` per city; then the planted trap — `window = temps[:24]; window += 100` — explain what happened to `temps` and fix with `.copy()`.
6. *(5 min)* Commit with a message stating the measured speedup; push (Git exists as of Day 2).

**Expected output**
```
$ python -m wafr_pipeline.kpi_report --week 2026-W23
dtypes OK: qty=int64 price=float64
loop:   2.84 s    vector: 0.011 s    speedup: 258×
revenue SAR 6,204,881.75 | high-value lines 8,412 | p50 63.25 | p95 412.80
peak hour per branch: RUH-014→20h  RUH-101→21h  JED-021→22h  DMM-003→19h
share-of-day rows sum to 1.0: True (allclose)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `dtype=object` on price array | A `"N/A"` string survived ingestion | Fix at the Module 2 boundary, not with `astype` duct tape — this is the architecture lesson |
| "truth value of an array is ambiguous" | `and`/`or` on masks | `&`/`|` with parentheses |
| `mean()` returns nan | NaN in array after sentinel repair | Decide: `np.nanmean` (and say why ignoring is correct here) |
| Speedup only ~5× | Benchmarking includes the list→array conversion each run | Convert once outside the timed region; discuss amortisation |
| Share-of-day shapes clash `(4,24)` vs `(4,)` | Missing `keepdims=True` | Add it; draw the shapes |
| Original temps array corrupted | View mutation from the planted trap | `.copy()` — views vs copies |

**Instructor notes.** The benchmark (task 3) is the module's emotional core: have three pairs read their speedups aloud and write the range on the board. Task 5's view trap should be allowed to *happen* before it is explained. Fast finishers: vectorise the discount-scenario grid (5 discount rates × full price array via broadcasting) or implement p95 per branch without a loop (`np.percentile` on the matrix with `axis=`).

## Mini Exercises

**Quiz (5 questions)**
1. `revenue.sum(axis=0)` on a `(4, 24)` matrix returns what shape, meaning what? → `(24,)`; per-hour totals — the named axis disappears.
2. Why can't an `int64` array hold a missing value? → no NaN in integers; missingness forces float (or masked/nullable types).
3. `a = arr[10:20]; a[:] = 0` — what happened to `arr`? → elements 10–19 zeroed; slices are views.
4. When is `np.nanmean` the *wrong* fix? → when missingness is informative or systematic — ignoring it biases the answer; the decision precedes the function.
5. Predict: `(3,) + (3,1)` → broadcasts to `(3,3)` — legal, and usually a bug; name the guard (assert shapes / keepdims discipline).

**Debugging exercise.** `debug_me_m3.py` computes weekly revenue that is exactly 100× too large for one branch: a unit-mismatch bug where halalas were treated as SAR for files from one POS version. The fix is a masked scale correction (`price[pos_version == 2] /= 100`) — and a boundary validation so it never recurs.

**Code-review exercise.** Review a PR that replaces a clear 8-line loop with a nested `np.where(np.where(...))` one-liner, uses `np.append` in a loop elsewhere, and compares floats with `==` in a test. Discuss: vectorisation serves *clarity and speed*, not golf.

**Discussion questions.**
- Your colleague says "NumPy is premature optimisation for our 10k-row files." Defend and attack. (correctness idioms and pandas fluency are the real reasons at small scale; speed is free)
- The share-of-day matrix could be computed in SQL, pandas, or NumPy. What decides where computation lives? (where the data already is, who maintains it, testability)

## Case Study — Gate-Sensor Analytics for Crowd Management at Mass Events

**Scenario.** An operations-analytics team supporting a mass-gathering venue (stadium-scale events in Riyadh) receives per-minute entry counts from 220 gate sensors: a `(220, 1440)` matrix per event day. The legacy analysis is a Python loop over sensors that takes 40 minutes per day and cannot answer surge questions interactively during the event itself.

**Business context.** Crowd-safety decisions (opening relief gates, redirecting flows) need "which sectors exceed threshold flow *right now*" in seconds. The team also runs post-event reviews comparing all gates against historical percentiles — currently an overnight batch.

**Technical challenge.** Rebuild the analysis as array computation: rolling 5-minute flows via sliced sums, threshold masks per sector, per-gate p95 against a `(220,)` historical baseline via broadcasting, and sector aggregation with axis reductions — interactive on a laptop.

**Constraints.** Data arrives as CSVs from a vendor system (no schema control — Module 2 boundary applies); sensors drop out mid-event producing NaN runs (the nan-decision applies: a dead sensor is *not* zero flow); the safety officer needs outputs as simple ranked tables, not code.

**Solution approach (facilitate, don't lecture).** (1) Validate and load into `(gates, minutes)` float64 with NaN for dropouts; (2) 5-minute rolling flow via `cumsum` differences (show the trick); (3) `flow > threshold[gate_sector][:, None]` broadcasting for per-sector thresholds; (4) `np.nanpercentile(history, 95, axis=1)` baseline, exceedance mask, `argsort` for the ranked table; (5) the 40-minute loop becomes ~0.5 s — which is what makes *during-event* use possible at all. The point to land: vectorisation changed what the team can *do*, not just how fast they do it.

**Discussion questions.**
1. Why must a dead sensor be NaN rather than 0? What answer does each choice corrupt?
2. Which parts of this belong in NumPy vs pandas? (pure numeric matrix ops vs labelled joins/reporting — a preview of Module 4's division of labour)
3. The vendor proposes streaming the data instead of CSVs. What changes in the analysis code? (ideally nothing — the boundary absorbs it; the arrays don't care)
4. What is the safety-relevant difference between a 40-minute answer and a 5-second answer to the same question?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| KPI computation, 135k records | Performance | ≥ 50× speedup vector vs loop; vector < 50 ms | lab benchmark |
| Loop/vector result agreement | Correctness | `np.isclose` on all KPIs | lab assertion |
| Column dtypes | Correctness | zero `object` arrays | dtype check |
| Share-of-day row sums | Correctness | `allclose(…, 1.0)` | lab assertion |
| NaN handling | Correctness | sentinel repairs masked; nan-decisions documented in comments | review |
| `np.append`-in-loop occurrences | Code quality | 0 | grep + review |

**Example benchmark table (filled during lab):**

| Operation | Loop | Vector | Speedup |
|---|---|---|---|
| Revenue + high-value count (135k) | 2.84 s | 11 ms | 258× |
| p50/p95 line value | 1.9 s (sort-based) | 6 ms | ~300× |
| Branch×hour matrix build | — | 38 ms | — |
| Full KPI report | 5.1 s | 68 ms | 75× |

## Required Visuals and Training Assets

### Diagrams
1. **List-of-boxes vs contiguous array** — *Purpose:* the module's anchor memory model. *Elements:* left panel — list of pointers to scattered boxed floats; right panel — one contiguous typed block with dtype/shape/strides labels; a speed dial beneath each. *Style:* memory-layout schematic, English labels with Arabic subtitles.
2. **Axis semantics cube** — *Elements:* a `(4, 24)` grid with axis-0 and axis-1 arrows; two collapse animations/frames showing which dimension disappears under `sum(axis=…)`. *Style:* before/after frames; the caption is the rule ("the axis you name disappears").
3. **Broadcasting shape alignment ladder** — *Elements:* worked alignments `(4,24)/(4,1)`, `(4,24)-(24,)`, and the dangerous `(3,)+(3,1)`→`(3,3)` marked red. *Style:* right-aligned shape stacks, tick/cross verdicts.
4. **View vs copy** — *Elements:* one buffer, two metadata headers pointing into it (view); versus duplicated buffer (copy); a mutation lightning bolt showing propagation. *Style:* schematic pair.

### Images (screenshots)
1. **Terminal — benchmark output** — *why:* expected-output reference; *content:* loop/vector/speedup line exactly as in lab spec.
2. **The "truth value is ambiguous" error** — *why:* pre-exposure defuses panic; *content:* the full traceback with the `&` fix beneath.
3. **Jupyter cell with shape-annotated pipeline** — *why:* models the shape-comment habit; *content:* each line commented with its result shape.
4. **`arr.nbytes` comparison cell** — *why:* memory visibility; *content:* list vs array size for 1M floats.

### Simulations
1. **View-mutation corruption** — *Setup:* planted `window = temps[:24]; window += 100` in lab step 5. *Expected:* source array corrupted; participants diagnose with `np.shares_memory`. *Learning objective:* views are performance, copies are safety; choose knowingly.
2. **object-dtype slowdown** — *Setup:* branch `sim-object-dtype` where one `"N/A"` survives ingestion. *Expected:* array ops "work" but 50× slower and `.sum()` raises on strings; participants trace to the boundary. *Learning objective:* dtype is the first thing you check.
3. **Sentinel-poisoned mean** — *Setup:* weather feed with 999.0 sentinels left in. *Expected:* city mean of ~180 °C in the report; participants mask and justify `nanmean`. *Learning objective:* validation and NaN decisions are business logic.

### Interactive Activities
- **Shape-prediction lightning round (10 min):** ten expressions on screen; pairs write predicted shapes on mini-whiteboards before execution; running score.
- **Vectorisation golf, reversed (10 min):** given an unreadable nested one-liner, teams rewrite it as *clear* vectorised code with intermediate names — clarity is the winning condition.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `week1.jsonl` (staged) | Lab 2 output | JSONL | ~135k records | The lab's working data — golden thread |
| `gate_counts_sample.npz` | Course tooling (synthetic, surge patterns injected) | NPZ | (220, 1440) ×3 days | Case-study exploration; fast finishers |
| `temps_week1.json` | Weather stub (with sentinels) | JSON | 3 cities × 7 days hourly | NaN-decision exercise |

### Demo Requirements
- **Instructor demo:** the live benchmark on the projector with the room predicting the speedup first; the ambiguous-truth-value error triggered and fixed deliberately.
- **Student demo:** two pairs present their branch×hour matrix insights (peak hours, share-of-day) as if to the Wafr operations manager — numbers, not code.
- **Expected outputs:** committed `kpi_arrays.py` + benchmark table; the matrix and KPI results Module 4 will reproduce in pandas and compare against.

---

# Module 4 — pandas for Tabular Data Manipulation

## Module Overview

**Purpose.** pandas is where the week converges: labelled, heterogeneous tables with the array speed of Module 3 underneath, the file/API sources of Module 2 flowing in, and the boundary discipline of Modules 1–2 still applying. This module teaches the DataFrame as a *thinking tool* — selection, cleaning, grouping, joining, and time-based analysis — and the habits that separate reliable pandas code from the fragile notebook incantations that give the library its bad reputation.

**Business relevance.** pandas is the default instrument of analytical work in every data team participants will join; it is also the substrate of feature engineering in both tracks. Organisations lose real money to pandas misuse: silent dtype coercions that corrupt IDs, chained-assignment bugs that "clean" nothing, and merges that silently duplicate rows and double revenue. A practitioner who can produce a *defensibly correct* groupby-merge pipeline is immediately useful; one who can only produce a plausible one is a liability with a notebook.

**Industry use cases.**
- A hospital network merges lab results with admissions across three systems, using validated keys and merge cardinality checks so no patient row silently duplicates.
- A retail chain (our golden thread) computes daily branch KPIs joined with weather to quantify the temperature–beverage-sales relationship that drives stocking decisions.
- A telecom regulator aggregates operator-submitted quality metrics quarterly, with groupby pipelines whose every intermediate step is inspectable and testable.

**Expected competencies.** After this module a participant can load real files with deliberate dtypes, select with `loc`/`iloc` confidently, clean missing/duplicate/mistyped data with documented decisions, build groupby-aggregate pipelines, perform merges with cardinality validation, handle datetimes and resampling, and write pandas code as named, testable steps.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Load tabular data with explicit dtypes, datetime parsing, and NA handling | LO2, LO5 |
| 4.2 | Select and transform data with loc/iloc and vectorised column operations, avoiding chained assignment | LO2 |
| 4.3 | Apply a documented missing-data and deduplication strategy | LO2, LO4 |
| 4.4 | Build groupby-aggregate pipelines answering business questions | LO2 |
| 4.5 | Join datasets with merge, validating key uniqueness and cardinality | LO2 |
| 4.6 | Analyse time-based data with datetime indexing and resampling | LO2 |

## Technical Content

### 1. Anatomy: Series, DataFrame, Index

A DataFrame is a dict of column Series sharing one row Index; each Series wraps a NumPy (or pandas nullable) array plus labels. Three orientation facts prevent early confusion:

- **Operations are column-wise by default** and vectorised — `df["total"] = df["qty"] * df["price"]` is Module 3's array multiply with labels on.
- **The Index is not a column.** It aligns operations, powers `.loc`, and travels through groupby/merge. Alignment is a superpower (two Series add by label, not position) and a trap (misaligned indexes produce NaN, not errors — demonstrate once).
- **dtypes per column,** visible via `df.dtypes` and `df.info()`. The first act on any new DataFrame is `df.info()` + `df.head()` — installed as a reflex from the first demo. The Module 3 payoff: participants already know why a count column with NaN shows as float64, and what `object` dtype implies about performance and dirt.

### 2. Getting data in, deliberately

`pd.read_csv` has ~50 parameters because files are wild; the six that matter: `dtype=` (IDs are *strings* — leading zeros die otherwise; branch codes as `category` for memory and speed), `parse_dates=`, `na_values=` (the vendor's `"N/A"`, `"-"`, `""`), `encoding=`, `usecols=` (read only what you need), and `nrows=` for a fast first look at a huge file.

- `pd.read_json`/`json_normalize` for the weather feed; `to_parquet`/`read_parquet` shown once — dtypes survive round-trips, files shrink ~5×, and the tracks use Parquet everywhere (SDA-DSC-214 makes it a way of life).
- **The load contract:** immediately after reading, assert what must be true — expected columns present, key columns non-null, dates within window. Five lines of `assert` after `read_csv` catch upstream drift on day one; this pattern becomes pytest tests in Module 6.

### 3. Selection and assignment without regret

- **`.loc[rows, cols]` (labels/masks) and `.iloc[rows, cols]` (positions)** as the only two selection tools in lab code; `df[...]` shorthand only for single-column access.
- Boolean-mask queries read like the Module 3 idiom with labels: `df.loc[(df.branch == "RUH-014") & (df.total > 500), ["sku", "total"]]`.
- **Chained assignment is the classic pandas bug:** `df[df.qty > 0]["total"] = ...` writes to a temporary and silently discards it. The rule: **one `.loc` per assignment** — `df.loc[df.qty > 0, "total"] = ...`. With pandas 3's copy-on-write this *always* does nothing rather than sometimes — cleaner semantics, same lesson; the course teaches the `.loc` form as permanent style.
- Derived columns via vectorised expressions or `.assign()` for chainable pipelines; `np.where`/`pd.cut` for conditional and banded columns (price bands for the KPI report).
- `.apply()` demoted honestly: it is a Python loop in costume — last resort after vectorised ops and string/dt accessors (`df.sku.str.upper()`, `df.sold_at.dt.hour`).

### 4. Cleaning as documented decisions

The module's stance: cleaning steps are *decisions with owners*, not keystrokes.

- **Missing data:** quantify first (`df.isna().sum()`), then decide per column — drop rows (when the row is meaningless without the value), fill with a constant/derived value (when a default is *true*, e.g., discount NaN means 0 — confirmed with the business), or leave NaN and use NaN-aware aggregation. `fillna(0)` on temperatures is a lie; on discounts it is a documented fact. Same function, opposite integrity.
- **Duplicates:** `df.duplicated(subset=key_cols)` — *define the key* (branch, sku, sold_at), count before dropping, and keep the drop count in the run report (Module 1's rejection-accounting principle, now in pandas).
- **Type repair:** `pd.to_numeric(..., errors="coerce")` turns dirty strings into NaN *and hands you the mask of what failed* — coerce-then-inspect, never coerce-and-forget.
- **Strings and categories:** `.str.strip().str.upper()` normalisation at load; `astype("category")` for low-cardinality columns (branch, channel) — memory drops visibly (`memory_usage(deep=True)`).

### 5. Groupby, merge, and time

- **Groupby is split-apply-combine:** `df.groupby("branch")["total"].sum()`, multi-key groups, named aggregations (`.agg(revenue=("total","sum"), lines=("sku","count"), p95=("total", lambda s: s.quantile(.95)))`). The Module 3 bridge: groupby is masked reduction industrialised — participants have already built it by hand.
- **Merge with paranoia:** `pd.merge(sales_daily, weather_daily, on=["city","date"], how="left", validate="m:1")`. The `validate=` and `indicator=True` parameters are taught as *mandatory* in lab code: the classic incident is a duplicated key on the right side silently multiplying revenue rows. Left/inner/outer chosen by asking "what do I want to happen to non-matches?" — and the anti-join (`indicator` + filter) answers "which sales days have no weather?"
- **Time:** `pd.to_datetime` at the boundary, `.dt` accessor for parts, `set_index` on the timestamp for `resample("D")`/`("W")` aggregation, and `sort_index` before any range slicing. Timezone note: store UTC or naive-local consistently and *say which* — mixed tz-aware/naive columns are a favourite silent bug.
- **Reshaping in one worked example:** `pivot_table(index="date", columns="branch", values="total", aggfunc="sum")` produces exactly Module 3's branch×hour matrix with labels; `melt` goes back. Wide for humans, long for computation.

### 6. Common mistakes & production considerations

1. Chained assignment (silently lost writes) — one `.loc` per assignment, always.
2. Merging without `validate=` — the revenue-doubling m:m accident; cardinality is an assertion, not a hope.
3. IDs read as int64 — leading zeros gone, and 16-digit IDs overflow to negative on some sources; `dtype={"national_id": "string"}`.
4. `fillna(0)` as reflex — encode *meaning*, not convenience; document every fill.
5. `.apply(axis=1)` row loops for arithmetic that vectorises — 100× slower and unreviewable.
6. Mutating the raw frame in place across 30 notebook cells — keep `raw` immutable, derive `clean` via named steps; notebook order-dependence is Module 1's hidden-state smell reborn.

Production considerations: pandas is single-machine, in-memory — know the ceiling (`memory_usage(deep=True)`; rule of thumb: need ~3–5× the data size in RAM for real work) and the escalation path (chunked reads, Parquet + column pruning, then the distributed tools of SDA-DSC-215); pipelines-as-functions (each step takes and returns a DataFrame) are what make Module 6's tests possible; and under PDPL, a DataFrame with customer identifiers is personal-data processing — drop or hash identifier columns you do not need at the *load* step, not at the report step.

## Code Examples

### The load contract

```python
# src/wafr_pipeline/tables.py
"""Staged records -> trusted DataFrame. Assert the contract at the boundary."""
import pandas as pd

EXPECTED_COLS = {"branch_code", "sku", "quantity", "unit_price_sar",
                 "channel", "sold_at"}


def load_sales(path) -> pd.DataFrame:
    df = pd.read_json(path, lines=True,
                      dtype={"branch_code": "category", "sku": "string",
                             "channel": "category"},
                      convert_dates=["sold_at"])
    missing = EXPECTED_COLS - set(df.columns)
    assert not missing, f"schema drift — missing columns: {missing}"
    assert df["sold_at"].notna().all(), "null timestamps escaped ingestion"
    assert (df["quantity"] > 0).all(), "non-positive quantities escaped ingestion"
    df["total_sar"] = (df["quantity"] * df["unit_price_sar"]).round(2)
    df["date"] = df["sold_at"].dt.date
    df["hour"] = df["sold_at"].dt.hour
    return df
```

### Cleaning with documented decisions

```python
# src/wafr_pipeline/clean_tables.py
"""Every cleaning step: quantified, decided, counted. No reflex fills."""
import pandas as pd


def clean_sales(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = raw.copy()                                   # raw stays immutable
    report: dict[str, int] = {}

    # DECISION (business-confirmed): discount NaN means "no discount" -> 0
    report["discount_filled"] = int(df["discount_rate"].isna().sum())
    df["discount_rate"] = df["discount_rate"].fillna(0.0)

    # DECISION: exact duplicates on the business key are POS replays -> drop, count
    key = ["branch_code", "sku", "sold_at"]
    dupes = df.duplicated(subset=key, keep="first")
    report["duplicates_dropped"] = int(dupes.sum())
    df = df.loc[~dupes]

    # Coerce-then-inspect: dirty numeric strings become NaN and get COUNTED
    df["unit_price_sar"] = pd.to_numeric(df["unit_price_sar"], errors="coerce")
    bad_price = df["unit_price_sar"].isna()
    report["bad_price_dropped"] = int(bad_price.sum())
    df = df.loc[~bad_price]

    df["total_sar"] = (df["quantity"] * df["unit_price_sar"]
                       * (1 - df["discount_rate"])).round(2)
    return df, report
```

### Groupby, validated merge, resample

```python
# src/wafr_pipeline/kpi_tables.py
"""The daily KPI frame: groupby -> validated merge -> time features."""
import pandas as pd

BRANCH_CITY = {"RUH-014": "Riyadh", "RUH-101": "Riyadh",
               "JED-021": "Jeddah", "DMM-003": "Dammam"}


def daily_kpis(sales: pd.DataFrame, weather_daily: pd.DataFrame) -> pd.DataFrame:
    daily = (sales
             .assign(city=sales["branch_code"].map(BRANCH_CITY))
             .groupby(["date", "branch_code", "city"], observed=True)
             .agg(revenue_sar=("total_sar", "sum"),
                  lines=("sku", "count"),
                  avg_line_sar=("total_sar", "mean"),
                  cold_drink_rev=("total_sar",
                                  lambda s: s[sales.loc[s.index, "sku"]
                                              .str.startswith("BEV")].sum()))
             .round(2)
             .reset_index())

    # validate='m:1' — many branch-days per one city-day of weather.
    # A duplicated weather row would raise HERE, not double revenue silently.
    kpis = pd.merge(daily, weather_daily, on=["city", "date"],
                    how="left", validate="m:1", indicator=True)
    unmatched = (kpis["_merge"] != "both").sum()
    if unmatched:
        print(f"[kpi] WARNING: {unmatched} branch-days without weather")
    return kpis.drop(columns="_merge")


def weekly_trend(sales: pd.DataFrame) -> pd.DataFrame:
    ts = sales.set_index("sold_at").sort_index()
    return ts["total_sar"].resample("D").sum().to_frame("revenue_sar")
```

## Hands-on Lab 4 — The pandas Transform Layer

| | |
|---|---|
| **Objective** | Clean the full month of sales in pandas, join the weather feed with a validated merge, and produce the daily-KPI DataFrame that the capstone will ship |
| **Duration** | 50 minutes (Day 4 Hour 3) |
| **Setup** | `pip install pandas pyarrow`; month dataset `pos_month.parquet` (~560k rows, dirt included) + `weather_month.json`; `git checkout lab4-start` |

**Instructions & tasks**

1. *(5 min)* Load with the load-contract function; run `df.info()` and `df.isna().sum()`; write down (in the notebook, in words) what is dirty and what you will do about each column.
2. *(10 min)* Implement `clean_sales` with the counted decisions (discount fill, key dedup, price coercion); reconcile `report` against the manifest.
3. *(5 min)* The planted chained-assignment cell "fixes" negative quantities but changes nothing — diagnose, then rewrite as one `.loc` assignment.
4. *(10 min)* Build `daily_kpis`: groupby with named aggregations, then the weather merge with `validate="m:1"` and `indicator=True`. The provided weather file contains a duplicated Jeddah day — let `validate` catch it, then dedupe the *weather* side and justify why that side.
5. *(10 min)* Time analysis: resample daily revenue; compute revenue by hour-of-day across the month; produce `pivot_table(date × branch)`; confirm the branch×hour pivot matches Module 3's matrix totals (`np.allclose`).
6. *(5 min)* Answer the business question in one markdown cell: *does temperature move beverage revenue?* (`kpis[["max_temp_c","cold_drink_rev"]].corr()` per city + one scatter).
7. *(5 min)* Save the KPI frame to `data/marts/daily_kpis.parquet`; commit with the cleaning report in the message; push.

**Expected output**
```
$ python -m wafr_pipeline.build_kpis --month 2026-06
[clean] discount_filled=31,204  duplicates_dropped=1,872  bad_price_dropped=409
[kpi]   120 branch-days, 0 without weather (after weather dedup)
[check] pandas pivot == numpy matrix: True
[trend] best day 2026-06-26 SAR 322,410.50 | Riyadh temp↔cold-drinks corr 0.71
Wrote data/marts/daily_kpis.parquet (120 rows × 11 cols)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `MergeError: Merge keys are not unique in right dataset` | The planted duplicate weather day | That's `validate=` working — dedupe weather, not sales; discuss why |
| Assignment "didn't take" | Chained indexing writing to a temporary | One `.loc[mask, col] = value`; show the copy-on-write explanation |
| Branch codes as object, groupby slow | Forgot `category` dtype at load | Set dtype in the load contract, not downstream |
| `TypeError` comparing tz-aware and naive datetimes | Weather timestamps tz-aware, sales naive | Normalise at the boundary (`dt.tz_localize(None)` or store both UTC); state the decision |
| Revenue double the manifest | Merge ran m:m before dedup / dedup key wrong | `validate=` + recount; the incident the lab is designed around |
| Pivot ≠ NumPy matrix | Dedup ran after the M3 export, or NaN fill differences | Reconcile step by step — teaches lineage thinking |

**Instructor notes.** Task 4 is the heart: let `validate="m:1"` throw on the projector and treat the exception as the hero of the story — that error is a production incident refused. Task 6 gives the module a business payoff; ask two pairs to state the correlation *in a sentence a merchandiser would act on*. Fast finishers: add `pd.cut` price bands to the KPI frame, or compute each branch's revenue share per day with `groupby.transform("sum")`.

## Mini Exercises

**Quiz (5 questions)**
1. Why must national IDs be read with `dtype="string"`? → leading zeros vanish and long IDs can overflow as int64; IDs are labels, not numbers.
2. `df[df.qty > 0]["total"] = 0` — what happens? → writes to a temporary copy; the original is untouched (pandas 3 CoW makes this reliably a no-op). One `.loc` per assignment.
3. What does `validate="m:1"` promise, and when does it raise? → right keys unique; raises when the right side would fan out rows — the silent duplication guard.
4. When is `fillna(0)` correct and when is it corruption? → correct when 0 is the *true* meaning (confirmed default, e.g., no discount); corruption when it invents a measurement (temperature).
5. `groupby("branch")["total"].sum()` in Module 3 terms? → masked reductions per group label — split-apply-combine over the same arrays.

**Debugging exercise.** `debug_me_m4.ipynb`: month revenue is exactly double for Jeddah. Cause: an m:m merge with a duplicated weather day performed *without* validate, upstream of the KPI groupby. Participants must localise it by checking row counts before/after each step — the "count rows at every step" habit is the lesson.

**Code-review exercise.** Review a notebook PR: 34 cells mutating `df` in place, an `apply(axis=1)` computing `qty*price`, `fillna(0)` on temperature, and a merge with no `validate`. Write the four review comments *and* the refactor plan (named-step functions) — connect to Module 6's testability.

**Discussion questions.**
- "The notebook gives the right numbers today." What breaks first when it runs on next month's data, and which habit from this module catches it? (load contract asserts)
- Your KPI frame feeds a Power BI dashboard and a scikit-learn model. Where should derived columns live so both agree? (the shared transform layer — the skew lesson from SDA-AIE-113's world, planted early)

## Case Study — Unifying Lab Results Across a Hospital Network

**Scenario.** A three-hospital network in the Eastern Province consolidates COVID-era lab systems: each hospital exports test results (CSV/Excel) with different column names, patient-ID formats (one zero-pads to 10 digits, one doesn't), local-time timestamps, and result units (mg/dL vs mmol/L for glucose). The analytics team must produce one clean results table joined to an admissions feed for readmission analysis.

**Business context.** A previous attempt double-counted 3% of results after a merge fanned out on duplicated admission rows; the resulting utilisation report briefly informed a staffing decision before being retracted. Clinical-analytics credibility is on the line, and PDPL applies to every identifier column in every intermediate file.

**Technical challenge.** Build a pandas pipeline: per-hospital load contracts → ID normalisation (zero-pad as *string*) → unit harmonisation with a conversion table merge → deduplication on a defined clinical key → `validate=`-guarded join to admissions → readmission flags via time-window logic.

**Constraints.** Excel exports cannot be turned off this year; identifiers must be hashed at load (PDPL minimisation) with the salt held outside the repo; the clinical lead must be able to read the cleaning report and see every dropped/converted count; the pipeline reruns monthly and must be idempotent.

**Solution approach (facilitate, don't lecture).** (1) Three thin `load_hospital_X()` functions sharing one contract-checker — differences are config (column maps), logic is shared (Module 2's sidecar pattern in pandas form); (2) glucose unit fix as a *merge with a conversion table*, not an if-chain — reviewable by clinicians; (3) `validate="m:1"` on the admissions join, `indicator=True` anti-join report for orphan results; (4) time-window readmission via sorted `merge_asof` (shown as the "there's a tool for that" moment); (5) the cleaning report is the deliverable that rebuilds trust — every count reconciles.

**Discussion questions.**
1. Why hash patient IDs at load rather than at report time? (every intermediate file is PDPL-scoped; minimise early)
2. The 3% double-count survived visual inspection of samples. What *systematic* check catches it? (row-count invariants + `validate=`; samples lie about joins)
3. Who signs off that mmol/L→mg/dL ×18.0 is correct — the engineer or the lab director? What does that imply about where the factor lives? (a reviewed data table, not code)
4. Sketch the four assertions you would put in this pipeline's load contract.

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Month build wall-clock (560k rows) | Performance | < 20 s end to end | `time` on lab run |
| Cleaning report reconciliation | Correctness | 100% of fills/drops counted and matching manifest | manifest diff |
| Merge fan-out incidents | Correctness | 0 (all merges `validate=`-guarded) | grep + row-count checks |
| pandas pivot vs NumPy matrix | Correctness | `allclose` agreement | lab assertion |
| Chained-assignment warnings | Code quality | 0 | run log / linting |
| Memory footprint after category dtypes | Efficiency | ≥ 40% reduction vs all-object load | `memory_usage(deep=True)` |

**Example benchmark table (filled during lab):**

| Step | Rows in | Rows out | Wall-clock | Notes |
|---|---|---|---|---|
| load (parquet) | 560,214 | 560,214 | 1.8 s | dtypes per contract |
| clean_sales | 560,214 | 557,933 | 2.1 s | 1,872 dupes, 409 bad prices |
| daily_kpis (groupby+merge) | 557,933 | 120 | 1.3 s | validate=m:1 |
| full pipeline | — | — | 12.4 s | incl. parquet write |

## Required Visuals and Training Assets

### Diagrams
1. **DataFrame anatomy** — *Purpose:* the module's anchor. *Elements:* column Series as labelled NumPy arrays, shared row Index as a spine, dtype tags per column; a magnifier showing one Series = array + labels. *Style:* exploded-view schematic, English labels with Arabic subtitles.
2. **Split-apply-combine** — *Elements:* one table splitting into per-branch groups, an aggregation squeezing each, results recombining with the group key as index. *Style:* three-stage flow matching the groupby code beneath it.
3. **Merge cardinality poster** — *Elements:* 1:1, m:1, m:m key diagrams; the m:m case with a red "rows multiply" explosion; `validate=` as a checkpoint gate. *Style:* key-matching diagram, printable A4 — this poster prevents real incidents.
4. **Missing-data decision tree** — *Elements:* "is a default TRUE? is the row meaningful without it? is missingness informative?" → fill / drop / keep-NaN leaves, each with a golden-thread example. *Style:* compact flowchart.

### Images (screenshots)
1. **`df.info()` + `isna().sum()` on the raw month** — *why:* the first-look reflex; *content:* dtypes and NA counts with the dirty columns visible.
2. **`MergeError` from `validate="m:1"`** — *why:* the hero error; *content:* full traceback plus the duplicated weather rows shown with `weather[weather.duplicated(["city","date"], keep=False)]`.
3. **Chained-assignment no-op cell** — *why:* the classic bug, seen once under supervision; *content:* before/after with the `.loc` fix.
4. **Temperature vs cold-drink scatter** — *why:* the business payoff; *content:* per-city scatter with correlation annotated.

### Simulations
1. **Revenue-doubling merge** — *Setup:* duplicated weather day, `validate` removed in branch `sim-fanout`. *Expected:* Jeddah revenue doubles silently; found via step-wise row counts. *Learning objective:* joins are where money silently duplicates; validate and count.
2. **ID corruption on load** — *Setup:* branch `sim-idload` reads loyalty IDs without dtype. *Expected:* leading zeros gone; join to loyalty file loses 8% of matches. *Learning objective:* dtype at load is a correctness decision.
3. **Timezone mismatch** — *Setup:* weather feed tz-aware UTC, sales naive local. *Expected:* TypeError on comparison (loud) after a silent one-hour join skew is narrowly avoided; participants normalise at boundary. *Learning objective:* declare the timezone convention once.

### Interactive Activities
- **"Fill, drop, or keep?" committee (15 min):** six missing-data scenarios from the golden thread; teams play analyst/business-owner/auditor roles and must reach a *documented* decision per column.
- **Merge-forensics race (10 min):** given before/after row counts of five merges, teams diagnose which fanned out, which lost rows, and which anti-join to run.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `pos_month.parquet` | Course tooling: June 2026, 4 branches, injected dirt incl. POS replays | Parquet | ~560k rows | Lab 4 main dataset |
| `weather_month.json` | Weather stub export, one duplicated Jeddah day planted | JSON | 90 city-days | Validated-merge exercise |
| `loyalty_ids.csv` | Course tooling, zero-padded IDs | CSV | 20k rows | ID-dtype simulation |
| `daily_kpis.parquet` | Produced by Lab 4 | Parquet | 120 rows | Input to Module 6 tests and the capstone |

### Demo Requirements
- **Instructor demo:** the chained-assignment no-op and the `validate=` MergeError, both triggered live and narrated as incident post-mortems; the pivot-vs-NumPy reconciliation.
- **Student demo:** one pair presents the temperature–beverage finding as a 90-second stakeholder brief; class challenges the causal leap (correlation ≠ stocking decision — a hook for DSC-213).
- **Expected outputs:** `daily_kpis.parquet` + cleaning report committed — the exact frame the capstone report ships and Module 6 tests.

---

# Module 5 — Git, GitHub, and Collaboration Workflows

## Module Overview

**Purpose.** Code that matters is written by teams over time, and Git is how teams share code without overwriting each other and how anyone answers "what changed, when, and why?" This module (delivered as part A on Day 2 — local Git — and part B on Day 3 — GitHub collaboration) makes version control a daily reflex rather than a ceremony: commit at every meaningful step, branch for every change, review before merge, and never lose work again.

**Business relevance.** Version control is the baseline of professional software practice that every Saudi enterprise engineering review expects; it is also an *audit* mechanism — the commit history is evidence of what logic produced which published number, which matters in regulated reporting. Teams without Git discipline ship `final_v2_REAL_fixed.py` folders; teams with it ship reviewable, revertible, attributable change. Every subsequent SDAIA module assumes fluent Git; SDA-AIE-113 builds its whole CI/CD story on the workflows installed here.

**Industry use cases.**
- A two-analyst team at a fintech works on the same pipeline simultaneously — branches and PRs replace the shared-folder file-locking chaos they arrived with.
- A ministry data team reconstructs exactly which cleaning rule produced last quarter's published indicator, from the tag on the release commit.
- A junior's well-meant "small fix" to a revenue calculation is caught in code review before it reaches the nightly run — the review *is* the control.

**Expected competencies.** After this module a participant can initialise and maintain a repository with a purposeful .gitignore, stage and commit in logical units with meaningful messages, read and search history, branch/merge and resolve conflicts calmly, collaborate through GitHub with push/pull/PR/review, and apply the data-work-specific hygiene (no data files, no secrets, no bulky notebook outputs in history).

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain the snapshot model: working tree, staging area, commits, branches as pointers | LO3 |
| 5.2 | Run the daily loop — status, diff, add, commit, log — with logical commits and meaningful messages | LO3 |
| 5.3 | Branch, merge, and resolve conflicts including notebook-specific cases | LO3 |
| 5.4 | Collaborate via GitHub: remotes, push/pull, pull requests, and code review | LO3, LO4 |
| 5.5 | Apply data-work Git hygiene: .gitignore for data/secrets/outputs, and recover from common mistakes | LO3, LO6 |

## Technical Content

### 1. The mental model: snapshots and pointers

Git stores **snapshots of the whole project**, not diffs; diffs are computed for display. Three places, one arrow diagram used all module: **working tree** (your files) → `git add` → **staging area** (the next snapshot, composed deliberately) → `git commit` → **history** (immutable chain of snapshots). A **branch is a movable pointer** to a commit; `HEAD` is "where you are". Ten minutes on this model saves hours of cargo-cult confusion later — every command in the module is then narrated as "which of the three places does this touch?"

- The staging area is a *feature*, not friction: it is how one messy working session becomes three clean, reviewable commits (`git add -p` shown once as the power tool).
- Commits are cheap and local; committing every 20–30 minutes of coherent work is the taught cadence. "I'll commit when it's finished" is how work gets lost.

### 2. The daily loop

`git status` (constantly — the situational-awareness command), `git diff` (what would I be committing?), `git add`, `git commit -m`, `git log --oneline --graph`. Message discipline: imperative summary ≤ 50 chars, body explains *why* when non-obvious — `clean: count and quarantine bad-price rows` not `changes`/`asdf`. The history of the golden-thread repo is itself a course artefact: by Day 5 it reads as the story of the week, and the capstone rubric grades it.

- **Reading history:** `git log -- path`, `git log -S "block_threshold"` (who touched this logic and when), `git show`, `git blame` framed as archaeology, not blame.
- **Undo, by scenario** (taught as a decision table, not trivia): unstaged mess → `git restore file`; staged too much → `git restore --staged`; bad last message → `commit --amend` (only if unpushed); committed a mistake that's pushed → `git revert` (new inverse commit — history is shared, never rewritten once public).

### 3. Branching, merging, conflicts

- Branch per change: `git switch -c fix/price-coercion`. Merges: fast-forward vs merge commit shown on the pointer diagram — once the model is pointers, both are obvious.
- **Conflicts demystified:** a conflict is Git *refusing to guess* between two edits to the same lines — it is a question, not an error. Read the markers, choose/compose, `add`, `commit`. The lab manufactures one on purpose in a calm setting so the first real one isn't at 16:55 on a deadline day.
- **Notebook conflicts** get their own treatment: `.ipynb` is JSON with embedded outputs, and merging it is misery. Course policy: strip outputs before committing (`nbstripout` or "Clear All Outputs" + save), keep logic in `.py` modules that notebooks import (Module 1's structure paying off again), and treat notebooks as thin, disposable front-ends.

### 4. GitHub and the collaboration workflow

- Remotes: `clone`, `push`, `pull` (= fetch + merge), `origin` as convention. Auth via SSH keys or fine-grained PAT — set up in the lab, the eternal first-push time sink.
- **The PR workflow as the unit of team change:** branch → commits → push → open PR with a description that says *why* → review comments → respond/fix → merge → delete branch. The PR is simultaneously a quality gate, a teaching channel, and the audit record.
- **Reviewing code is a skill:** the course review checklist (does it run? are the counts reported? naming? one purpose per function? tests updated?) and review etiquette — comment on the code, not the person; prefer questions ("what happens when qty is 0 here?"); approve explicitly. Participants both give and receive a review in Lab 5b — receiving one calmly is also the skill.
- `pull` before you push; when rejected (non-fast-forward), `pull` then resolve — the two-person simulation makes this muscle memory. (`--rebase` for a linear local history is mentioned for the curious, not required.)

### 5. Git hygiene for data work

- **.gitignore from birth:** `data/`, `.env`, `__pycache__/`, `.venv/`, `outputs/`, `.ipynb_checkpoints/`. Repos version *logic*, not data: data is large, often sensitive (PDPL — a committed customer extract is an incident, not a mistake), and changes for non-logic reasons. Small *fixture* samples for tests (Module 6) are the deliberate exception.
- **Secrets and history:** the demo that lands — commit a fake API key, delete it in the next commit, then `git log -p` shows it perfectly preserved. Removal ≠ un-leaking: a leaked-and-pushed secret is *rotated first*, history-cleaned second. This connects Module 2's env-var habit to its real justification.
- Large files: Git chokes on churning binaries; course rule is data stays out (pointer to Git LFS and data-versioning tools as the professional escape hatch, covered in the tracks).
- Tags for milestones: `git tag v0.4-day4` — the capstone submission is a tag, and the ministry case's "which logic produced the published number" is answered by one.

### 6. Common mistakes & team considerations

1. `git add .` swallowing data files, `.env`, and 40 MB of notebook outputs — status-before-add, ignore-file-first.
2. One giant end-of-day commit ("day 3 work") — unreviewable, unrevertible; commit per logical step.
3. Working on `main` directly, then wanting to undo half of it — branch per change makes undo trivial (delete the branch).
4. Merge-conflict panic: accepting "theirs" wholesale to make the markers go away — resolve by *reading*, and run the code/tests after resolving.
5. `git push --force` to "fix" a rejected push — on shared branches this deletes teammates' work; the course bans force-push on shared branches outright.
6. Treating review comments as attacks — the team consideration: review is how teams stay collectively responsible for code no single person fully owns.

Team considerations: agree conventions early (branch naming, message style, who merges); small PRs get reviewed, 2,000-line PRs get rubber-stamped — keep them small; and the history quality of a repo is a *shared asset* — it is the team's institutional memory and, in regulated contexts, its evidence.

## Worked Examples

### The repository birth ritual (Lab 5a's spine)

```bash
# Day 2, Hour 5 — wafr-pipeline goes under version control
cd wafr-pipeline
git init
cat > .gitignore <<'EOF'
data/
outputs/
.env
.venv/
__pycache__/
.ipynb_checkpoints/
EOF
git add .gitignore && git commit -m "chore: ignore data, env, and caches from birth"

git add src/wafr_pipeline/records.py src/wafr_pipeline/cleaning.py
git commit -m "feat: domain records and counted cleaning from Day 1"

git add src/wafr_pipeline/ingest_files.py src/wafr_pipeline/weather_api.py
git commit -m "feat: file ingestion and defensive weather client"

git log --oneline --graph          # the story so far, readable
```

### Branch → conflict → resolution (Lab 5b, manufactured on purpose)

```bash
# Partner A                                # Partner B (same file, same lines)
git switch -c feat/p95-kpi                 git switch -c feat/median-kpi
# edits kpi_arrays.py line 30              # edits kpi_arrays.py line 30
git commit -am "feat: add p95 line KPI"    git commit -am "feat: add median KPI"
git push -u origin feat/p95-kpi            git push -u origin feat/median-kpi
# A's PR merges first. B updates:
git switch main && git pull
git switch feat/median-kpi && git merge main
# CONFLICT (content): kpi_arrays.py
#   <<<<<<< HEAD          (B's median)
#   =======               (A's p95, now in main)
#   >>>>>>> main
# B composes BOTH KPIs, then:
python -m pytest -q                # resolve, THEN verify
git add src/wafr_pipeline/kpi_arrays.py
git commit -m "merge: combine p95 and median KPIs"
git push
```

### The undo decision table (handout)

| Situation | Command | Rewrites history? |
|---|---|---|
| Messed up a file, not staged | `git restore <file>` | No |
| Staged the wrong thing | `git restore --staged <file>` | No |
| Bad message / forgot a file, NOT pushed | `git commit --amend` | Local only — fine |
| Bad commit, already pushed | `git revert <sha>` | No — adds inverse commit |
| Committed a secret, already pushed | Rotate the secret FIRST, then clean history | Yes — with team coordination |

### The PR description template (course convention)

```markdown
## What
Add p95 line-value KPI to the daily report.

## Why
Merchandising asked for tail behaviour, not just averages —
p95 catches the bulk-purchase pattern the mean hides.

## How verified
- pytest suite green locally (14 passed)
- KPI reconciles with Module 3 NumPy value on week1 (allclose)

## Reviewer notes
Percentile method is NumPy default ('linear') — flag if we need 'nearest'.
```

## Hands-on Lab 5 — Version the Pipeline, Then Collaborate on It

| | |
|---|---|
| **Objective** | Part (a, Day 2): put `wafr-pipeline` under Git with hygiene from birth. Part (b, Day 3): full GitHub pair workflow — push, branch, PR, review, merge, and one deliberate conflict |
| **Duration** | 2 × 50 minutes (Day 2 Hour 5, Day 3 Hour 5) |
| **Setup** | Git installed and configured (`user.name`, `user.email`); GitHub accounts with SSH/PAT auth ready (pre-course checklist); pairs assigned |

**Instructions & tasks**

*Part (a) — local Git*
1. *(10 min)* The birth ritual: `init`, write `.gitignore` *first*, verify with `git status` that `data/` and `.env` are invisible.
2. *(15 min)* Commit Days 1–2 work as ≥ 4 logical commits (records / cleaning / ingestion / weather client) with imperative messages.
3. *(10 min)* History reading: `log --oneline --graph`; find with `git log -S "timeout"` which commit introduced the API timeout; `git blame` one function.
4. *(10 min)* Undo drills, scripted: mangle a file and `restore` it; stage a data file "by accident" and unstage it; amend a typo'd message.
5. *(5 min)* The secret demo: commit `WAFR_WEATHER_KEY = "sk_live_fake123"` in a scratch file, delete it, commit again, then recover it from `git log -p`. State the rotation rule aloud.

*Part (b) — GitHub collaboration*
1. *(10 min)* Create the GitHub repo, `push -u origin main`; partner clones. First-push auth issues resolved here, with the floater's help.
2. *(15 min)* Each partner: branch (`feat/p95-kpi` / `feat/median-kpi`), implement, push, open a PR using the course template.
3. *(10 min)* Review each other's PR: ≥ 2 substantive comments using the checklist; author responds with a fix commit; merge PR #1.
4. *(10 min)* Partner B now has a genuine conflict on the same lines: merge `main` into the branch, resolve by *composing both features*, run the code, push, merge PR #2.
5. *(5 min)* `git tag v0.3-day3 && git push --tags`; verify the repo graph on GitHub shows the full story.

**Expected output**
```
$ git log --oneline --graph -8
*   9f3c2ba (HEAD -> main, tag: v0.3-day3, origin/main) merge: combine p95 and median KPIs
|\
| * 4e81d07 feat: add median line KPI
* | b7a90fe feat: add p95 line KPI
|/
* 2c664a1 feat: defensive weather client with cache and retry
* 8d12f45 feat: file ingestion with counted rejections
* 51b0e9a feat: domain records and counted cleaning from Day 1
* e4a7c3d chore: ignore data, env, and caches from birth
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `Permission denied (publickey)` on first push | SSH key not added to agent/GitHub | The pre-course checklist's test command `ssh -T git@github.com`; PAT fallback |
| `data/pos_month.parquet` shows in `git status` | .gitignore written after files were tracked, or pattern typo | `git rm --cached`, fix pattern — teaches ignore-only-affects-untracked |
| Push rejected (non-fast-forward) | Partner merged first | `git pull`, resolve, push — the intended lesson, not an accident |
| Conflict markers committed into the file | Resolved by saving without editing markers | Fix, run the code, amend — "resolve means the code runs" |
| PR shows 3,000 changed lines of notebook JSON | Outputs not stripped | Clear outputs / nbstripout; recommit — the notebook-hygiene lesson |
| Wrong author on commits | `user.email` unset or personal | `git config`, amend the last commit; note history keeps old ones |

**Instructor notes.** Part (a) task 5 (the secret that never dies) is the demo participants retell — do it on the projector with theatrical `git log -p`. In part (b), resist rescuing pairs from the conflict too early; the composure is the curriculum. Fast finishers: add a PR template file to the repo (`.github/pull_request_template.md`), or protect `main` on GitHub and observe what changes.

## Mini Exercises

**Quiz (5 questions)**
1. Working tree, staging area, history — which does `git add` move content between? → working tree → staging area.
2. A pushed commit contains a wrong formula. `--amend`, `revert`, or `reset`? → `revert`; shared history is never rewritten.
3. What is a branch, physically? → a movable pointer (a 41-byte file) to a commit.
4. Why strip notebook outputs before committing? → outputs are bulky, churn on every run, leak data into history, and make diffs/merges unreadable.
5. You committed and pushed an API key, then deleted it in the next commit. Status? → still leaked (history preserves it); rotate first, then clean history.

**Debugging exercise.** A provided repo has a KPI regression somewhere in 12 commits. Participants use `git log -S "round("` and `git diff <sha>~ <sha>` to find the commit that changed rounding from report-boundary to per-record (Module 1's lesson, archaeologically rediscovered). Optional stretch: the same hunt with `git bisect run pytest -q`.

**Code-review exercise.** Each pair reviews a prepared PR containing one real logic bug (dedup key missing `sold_at`), one style issue, and one missing-count report. The exercise is scored on *finding the logic bug* — review is a correctness activity, not a formatting one.

**Discussion questions.**
- Your team's history is 40 commits titled "update". What has the team actually lost? (revert granularity, archaeology, review context, audit evidence)
- Who should merge a PR — the author or the reviewer? Argue both; note what your answer implies about accountability.

## Case Study — The Overwritten Quarter at a Jeddah Fintech

**Scenario.** A six-person data team at a Jeddah payments fintech collaborates via a shared network drive: `pipeline_final.py`, `pipeline_final_v2.py`, `pipeline_final_v2_SARA.py`. During quarter-end close, two analysts edit `pipeline_final_v2.py` in the same hour via desktop sync; the second save wins, silently discarding a fee-calculation fix. The wrong fee logic runs quarter-end; the discrepancy (SAR 1.9M in mis-attributed fees) surfaces three weeks later during reconciliation.

**Business context.** The post-incident review cannot even establish *which* logic ran on close night — the file has no history, the sync service keeps 30 days of versions, and the deadline was 47 days ago. The regulator's follow-up question — "show us the change control for this calculation" — has no good answer.

**Technical challenge.** Migrate the team to a Git/GitHub workflow that makes the incident class impossible: every change attributable, reviewed before merge, and the production run traceable to an exact commit.

**Constraints.** Quarter-close scripts cannot pause for a tooling migration; two analysts have never used Git; some scripts embed credentials (a second incident waiting); the compliance officer needs evidence *she* can read, not commands.

**Solution approach (facilitate, don't lecture).** (1) Repo per pipeline with history imported from the best-known copy; tags at every production run (`close-2026Q2`) — the regulator's question becomes `git show close-2026Q2`; (2) branch-and-PR mandatory with review by a second analyst for anything touching money math — the fee fix would have been a visible, reviewed PR, not a lost save; (3) credentials moved to env/secret store *before* the repo is shared (Module 2 + the secret-demo lesson); (4) the two Git-new analysts pair for two weeks — the Lab 5b workflow is literally their onboarding; (5) compliance gets the GitHub PR view — approvals, timestamps, diffs — as the change-control record. Institutional memory now lives in history, not in Sara's filename suffixes.

**Discussion questions.**
1. Which single practice from this module would have prevented the SAR 1.9M incident outright? (any of: no shared-file editing, PR review on money math, tagged runs — argue which is *load-bearing*)
2. Why are tags the answer to the regulator, rather than "we're pretty sure it was v2"?
3. The team lead proposes everyone pushes straight to `main` "to keep velocity". Predict the failure and propose the lightweight alternative (small PRs, fast review SLA).
4. What does the compliance officer actually need to see, and how does the PR view provide it without teaching her Git?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Repo hygiene | Code quality | 0 data files, secrets, or outputs in history | `git log --stat` audit + checklist |
| Commit granularity | Code quality | ≥ 8 logical commits by end of Day 3; no "update"-style messages | history review |
| PR cycle completed | Collaboration | 2 PRs each: opened, reviewed (≥ 2 substantive comments), merged | GitHub audit |
| Conflict resolution | Collaboration | 1 conflict resolved with both features intact and code running | lab checkpoint |
| Undo drills | Fluency | All 4 scenarios executed without instructor help | lab checklist |
| Time to first successful push | Logistics | ≤ 15 min including auth | lab timing |

**Example benchmark table (filled during lab):**

| Checkpoint | Pair median | Slowest pair | Notes |
|---|---|---|---|
| init → first commit | 6 min | 11 min | .gitignore-first enforced |
| First push (incl. auth) | 9 min | 22 min | PAT fallback used twice |
| PR opened → merged | 14 min | 25 min | review depth varies |
| Conflict → resolved & green | 8 min | 18 min | one pair committed markers |

## Required Visuals and Training Assets

### Diagrams
1. **Three-places flow** — *Purpose:* the module's anchor. *Elements:* working tree → staging → history columns; every core command as a labelled arrow between them (add, commit, restore, restore --staged); HEAD and branch pointers on the history chain. *Style:* horizontal flow, command arrows in monospace, English labels with Arabic subtitles — this is the poster on the wall all week.
2. **Branch-as-pointer sequence** — *Elements:* five frames: linear history → new branch pointer → divergence → fast-forward merge vs merge commit. *Style:* commit-graph dots and arrows, two-panel ending.
3. **PR workflow loop** — *Elements:* branch → push → PR → review comments → fix commits → merge → delete branch; the audit-trail sidebar showing who/when/what. *Style:* cycle diagram with a GitHub-style UI inset.
4. **"What .gitignore protects you from"** — *Elements:* data files (PDPL icon), .env (key icon), caches, notebook outputs — each with the incident it prevents. *Style:* four-quadrant poster.

### Images (screenshots)
1. **`git log --oneline --graph` of the golden-thread repo** — *why:* the target history, readable as a story; *content:* exactly the expected-output block.
2. **A real PR with review comments and a fix commit** — *why:* models review tone and the comment-fix-resolve loop; *content:* two substantive comments, author response, approval.
3. **Conflict markers in VS Code with the merge editor** — *why:* defuses conflict panic; *content:* both versions visible, "Accept Both" being *edited* afterward.
4. **`git log -p` showing the "deleted" secret** — *why:* the demo participants retell; *content:* the key visible in a past commit's diff.

### Simulations
1. **The lost-save re-enactment** — *Setup:* two participants edit the same file via a shared folder (no Git), save 30 s apart. *Expected:* second save wins silently; then the same edits via branches merge cleanly. *Learning objective:* the fintech case, felt personally in 5 minutes.
2. **Secret-in-history drill** — *Setup:* scripted commit/delete of a fake key. *Expected:* recovery from `log -p`; rotation-first response stated. *Learning objective:* history is forever; rotate first.
3. **Notebook-diff horror** — *Setup:* commit a notebook with outputs, change one line, view the PR diff. *Expected:* 3,000-line JSON diff; then stripped-output version diffs in 3 lines. *Learning objective:* notebook hygiene policy.

### Interactive Activities
- **Command charades on the three-places poster (10 min):** instructor names a situation ("staged the data file"), pairs point to the arrow that fixes it before typing anything.
- **Commit-message speed review (10 min):** 12 real-world messages on screen; thumbs up/down with one-sentence justification; class writes the repo's message convention together.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `wafr-pipeline` repo (participants' own) | Built Days 1–3 | Git repo | ~30 files | The collaboration substrate — golden thread |
| `archaeology-repo.bundle` | Course tooling: 12 commits, one planted regression | Git bundle | small | log -S / bisect exercise |
| Prepared review PR | Course org on GitHub | PR | 1 | Code-review exercise with planted logic bug |

### Demo Requirements
- **Instructor demo:** the three-places poster walked with live commands; the secret-that-never-dies; a live conflict resolved calmly with tests run afterward.
- **Student demo:** one pair walks the class through their merged PR — what the reviewer caught, what changed in response.
- **Expected outputs:** every participant leaves Day 3 with a GitHub repo whose history tells the week's story — the capstone will be graded partly *from* it.

---

# Module 6 — Testing, Debugging, and Code Quality

## Module Overview

**Purpose.** Data code fails differently from ordinary code: it usually fails *silently*, producing plausible wrong numbers instead of stack traces. This module installs the systematic defences — pytest unit tests around every cleaning and KPI function, edge-case and golden-file thinking, disciplined debugging from the traceback down to `pdb`, and the quality tooling (ruff, type hints, review) that keeps a codebase honest as it grows. It converts the golden-thread pipeline from "code that ran" into "code we can change without fear".

**Business relevance.** The expensive data bugs are the quiet ones: the fee calculation that was wrong for a quarter, the dedup key that dropped real sales, the mean computed over sentinel values. Tests are the cheapest instrument an organisation has for catching these before publication — and in regulated Saudi contexts, a test suite around report logic is *evidence of control*, the kind auditors and data-governance reviews (NDMO) increasingly expect. Teams with tests refactor weekly; teams without tests fear their own code.

**Industry use cases.**
- A bank's regulatory-reporting team guards every published aggregate with tests on crafted edge cases (zero-value days, single-transaction branches, Ramadan-shifted calendars) after an erratum incident.
- A retail analytics team refactors a slow KPI job with confidence because a golden-file test pins the outputs byte-for-byte.
- A ministry's data unit makes ruff + pytest a pre-merge requirement, catching the bare-except and mutable-default classics in review automatically.

**Expected competencies.** After this module a participant can write pytest tests with fixtures and parametrisation, design edge-case and golden-file tests for data transformations, read a traceback from the bottom up, debug with `pdb`/VS Code breakpoints instead of print-scatter, run coverage honestly, and apply ruff and the course review checklist as routine quality gates.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Write pytest unit tests with clear arrange-act-assert structure for pipeline functions | LO4 |
| 6.2 | Use fixtures, `parametrize`, and `tmp_path` to test data code cleanly | LO4 |
| 6.3 | Design edge-case, property, and golden-file tests for data transformations | LO4, LO2 |
| 6.4 | Debug failures systematically: traceback reading, breakpoints, hypothesis-driven isolation | LO4 |
| 6.5 | Apply ruff, type hints, and coverage as routine quality gates | LO4, LO1 |

## Technical Content

### 1. Why data code needs tests more, not less

The common objection — "my code is exploratory, tests would slow me down" — inverts the truth. Exploratory code becomes load-bearing the moment its number reaches a slide. The taxonomy taught:

- **Loud failures** (exceptions) are the good ones — Module 1's validation philosophy already converts many silent failures into loud ones.
- **Silent failures** are the data-native kind: wrong dedup key, `fillna` on the wrong column, a merge fan-out, an off-by-one in a date window. No traceback will ever come. Only a *test with a known answer* catches them.
- The testing pyramid for pipelines: many fast **unit tests** on pure functions (cleaning rules, KPI math — Module 1's function discipline is why these are easy), some **component tests** on whole steps with small fixture files, and one or two **end-to-end** runs on the mini fixture asserting the final numbers. The pyramid stays cheap because the architecture allowed it — say this explicitly; it closes the loop opened on Day 1.

### 2. pytest mechanics

- **Anatomy:** files `tests/test_*.py`, functions `test_*`, plain `assert` (pytest's rewritten asserts show values on failure — demonstrate the diff output on a failing frame comparison).
- **Arrange–Act–Assert** as the readable shape; one behaviour per test; the test name is a sentence (`test_replayed_pos_rows_are_dropped_once`).
- **Fixtures** for shared setup: a `small_batch` fixture returning six crafted records (every edge case represented); `tmp_path` for anything touching disk — tests never write into the repo.
- **`@pytest.mark.parametrize`** turns the timestamp-format zoo into one table-driven test — twelve cases, four lines.
- **Testing exceptions:** `pytest.raises(ValueError, match="negative price")` — the validation contract from Module 1 is itself under test.
- **pandas/NumPy assertions:** `pandas.testing.assert_frame_equal` (with `check_like`, `atol` where justified) and `np.isclose`/`allclose` — never `==` on computed floats (Module 3's rule, now enforced by tooling).

### 3. Testing data transformations

The module's craft section — what to test when the subject is a table:

- **Crafted micro-fixtures beat production samples:** six rows where you *know* the answer (one duplicate, one bad price, one zero-discount NaN, one boundary timestamp) prove more than 500k rows where you don't. The manifest-reconciliation habit from Modules 2–4 was this idea all along.
- **Property-style invariants:** cleaning never *increases* row count; revenue is non-negative; every rejected row is counted (`len(in) == len(out) + rejected`); share-of-day sums to 1. Cheap to write, catch whole bug classes.
- **Golden-file tests:** run the reference pipeline on the fixture once, save `expected_kpis.parquet`, and assert future runs match. The governance rule taught with it: a golden file is *regenerated deliberately, in a reviewed commit that explains why* — never edited to make red turn green. (This rule becomes CI policy in SDA-AIE-113.)
- **Boundary catalogue for data code:** empty input, single row, all-rejected input, Unicode/Arabic text fields, month boundaries and DST-free but Hijri-adjacent calendar quirks, the largest file the pipeline claims to support.
- What *not* to test: pandas itself, the weather provider's uptime, or exact float digits beyond a justified tolerance — tests assert *our* logic.

### 4. Systematic debugging

Debugging is taught as method, not heroics:

- **Read the traceback bottom-up:** last frame = where it died; the *cause* is usually a few frames up in your own code; exception *type* narrows hypotheses instantly (`KeyError` = missing key ≠ `ValueError` = bad value). The Module 2 exercise (JSONDecodeError masking an HTTP 500) is re-referenced as "first error in causal order".
- **Reproduce small, then fix:** shrink the failing case to the smallest input that still fails (often one row) — that row *becomes a new test fixture*, so the bug can never return unnoticed. Bug → failing test → fix → green is the course's canonical loop.
- **Breakpoints over print-scatter:** `breakpoint()` and the pdb survival set (`n`, `s`, `c`, `p expr`, `q`); the VS Code debugger with a data-inspection view for DataFrames; conditional breakpoints for "only when branch == JED-021".
- **Hypothesis-driven isolation:** state what you believe, test the belief with the cheapest observation (`df.shape` between steps, `assert` probes), halve the search space — debugging as binary search, with `git bisect` (Module 5) as its history-dimension twin.
- **When stuck:** rubber-duck the code aloud to your pair; diff against the last green commit (`git diff`); check dtypes and shapes *first* — in this course's experience, half of all "logic bugs" are dtype or shape bugs.

### 5. Code quality as a system: ruff, hints, coverage, review

- **ruff** as linter+formatter: one tool, one config in `pyproject.toml`; the course rule set catches the classics live in the editor (B006 mutable defaults, E722 bare except, F841 unused variable — each maps to a bug seen this week). Format on save ends style debates permanently.
- **Type hints + editor checking** as the zero-cost test layer: hints on public functions caught three lab bugs this week before any test ran (mistyped Optional handling, str vs Path). Full mypy discipline is deferred to SDA-AIE-113; here hints are documentation that argues back.
- **Coverage honestly:** `pytest --cov=wafr_pipeline --cov-report=term-missing`; target ≥ 80% on `cleaning.py`/`kpi_*.py` — and the anti-metric warning: coverage measures *execution*, not *verification*; a test with no meaningful assert inflates the number and protects nothing. Review the asserts, not the percentage.
- **The review checklist as quality gate** (Module 5's PR workflow now has teeth): does it run, are edge cases tested, are counts reported, naming, function size, no banned patterns. Tests turn review from "looks right to me" into "the evidence is green".

### 6. Common mistakes & production considerations

1. Tests that mirror the implementation (`assert clean(df).equals(clean(df))`) — test *known answers*, not the code against itself.
2. One giant `test_everything` — when it fails, it says nothing; one behaviour per test.
3. Tests depending on execution order or shared mutable fixtures — pytest runs them independently; so must you.
4. Golden files regenerated casually to silence a red suite — the discipline is the point; a red golden test is a *question* ("did we mean to change the numbers?").
5. Debugging by shotgun edit — change one thing per hypothesis, keep the failing test as the scoreboard.
6. Chasing 100% coverage through trivial tests while `clean_sales`'s edge cases sit untested — cover the code where wrong answers cost money.

Production considerations: fast suites get run, slow suites get skipped — keep unit tests under seconds by testing pure functions on micro-fixtures (the architecture dividend again); flaky tests (time-dependent, network-dependent) erode trust — freeze time via injected clocks and stub the API (the course weather stub exists partly for this); and the suite is the *enabler of change* — the capstone's final refactor hour is deliberately scheduled after the suite exists, so participants feel the difference between changing tested and untested code.

## Code Examples

### Fixtures and edge-case unit tests

```python
# tests/unit/test_cleaning.py
"""Unit tests for the cleaning boundary. Micro-fixture: every row a known story."""
from datetime import date, datetime

import pytest

from wafr_pipeline.cleaning import build_batch, clean_row, parse_sold_at


@pytest.fixture
def raw_rows() -> list[dict[str, str]]:
    good = {"branch_code": "ruh-014", "sku": "WTR-1.5L", "quantity": "2",
            "unit_price_sar": "4.50", "channel": "Store",
            "sold_at": "2026-06-01 14:22:10"}
    return [
        good,
        {**good, "sold_at": "01/06/2026 14:22"},        # legacy format — must parse
        {**good, "quantity": "0"},                       # boundary — must reject
        {**good, "unit_price_sar": "-4.50"},             # negative — must reject
        {**good, "channel": "kiosk"},                    # unknown — must reject
        {**good, "sku": "تمر-سكري-1KG"},                 # Arabic SKU — must pass
    ]


def test_branch_code_is_normalised(raw_rows):
    assert clean_row(raw_rows[0]).branch_code == "RUH-014"


def test_arabic_sku_survives_cleaning(raw_rows):
    assert clean_row(raw_rows[5]).sku == "تمر-سكري-1KG"


def test_every_rejection_is_counted(raw_rows):
    batch = build_batch(raw_rows, business_date=date(2026, 6, 1))
    assert len(batch) == 3
    assert batch.rejected == 3
    assert len(raw_rows) == len(batch) + batch.rejected   # conservation invariant


@pytest.mark.parametrize("raw, expected_hour", [
    ("2026-06-01 09:05:00", 9),
    ("01/06/2026 21:40", 21),
])
def test_both_timestamp_formats_parse(raw, expected_hour):
    assert parse_sold_at(raw).hour == expected_hour


def test_unparseable_timestamp_is_loud():
    with pytest.raises(ValueError, match="unparseable"):
        parse_sold_at("June 1st, 2026")
```

### Golden-file and property tests on the pandas layer

```python
# tests/component/test_kpi_tables.py
"""Component tests: whole steps on the mini fixture, known answers pinned."""
from pathlib import Path

import pandas as pd
import pandas.testing as pdt
import pytest

from wafr_pipeline.clean_tables import clean_sales
from wafr_pipeline.kpi_tables import daily_kpis

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def mini_sales() -> pd.DataFrame:
    return pd.read_parquet(FIXTURES / "mini_sales.parquet")     # 200 crafted rows


def test_cleaning_never_invents_rows(mini_sales):
    clean, report = clean_sales(mini_sales)
    assert len(clean) <= len(mini_sales)
    assert len(clean) + report["duplicates_dropped"] \
                      + report["bad_price_dropped"] == len(mini_sales)


def test_daily_kpis_match_golden(mini_sales):
    """Golden file: regenerated ONLY deliberately, in a reviewed commit.
    A red here means 'the numbers changed' — that is a question, not a nuisance."""
    clean, _ = clean_sales(mini_sales)
    weather = pd.read_parquet(FIXTURES / "mini_weather.parquet")
    result = daily_kpis(clean, weather)
    expected = pd.read_parquet(FIXTURES / "expected_kpis.parquet")
    pdt.assert_frame_equal(result, expected, check_like=True, atol=0.01)


def test_merge_never_fans_out(mini_sales):
    clean, _ = clean_sales(mini_sales)
    weather = pd.read_parquet(FIXTURES / "mini_weather.parquet")
    daily_rows_before = clean.groupby(["date", "branch_code"], observed=True).ngroups
    assert len(daily_kpis(clean, weather)) == daily_rows_before
```

### The canonical debugging loop, captured

```python
# tests/unit/test_regression_dedup_key.py
"""Regression test born from a real lab bug (Day 4): dedup key omitted sold_at,
so two legitimate same-SKU sales in one branch-day were 'deduplicated'.
The shrunken reproduction became this permanent fixture."""
import pandas as pd

from wafr_pipeline.clean_tables import clean_sales


def test_same_sku_different_times_are_both_kept():
    rows = pd.DataFrame([
        {"branch_code": "RUH-014", "sku": "WTR-1.5L", "quantity": 1,
         "unit_price_sar": 4.5, "discount_rate": 0.0,
         "sold_at": pd.Timestamp("2026-06-01 09:00:00")},
        {"branch_code": "RUH-014", "sku": "WTR-1.5L", "quantity": 1,
         "unit_price_sar": 4.5, "discount_rate": 0.0,
         "sold_at": pd.Timestamp("2026-06-01 17:30:00")},   # later, real, distinct
    ])
    clean, report = clean_sales(rows)
    assert len(clean) == 2
    assert report["duplicates_dropped"] == 0
```

### Quality gates in pyproject.toml

```toml
# pyproject.toml (excerpt) — one file, all gates
[tool.ruff]
line-length = 99
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "F", "B", "I", "UP"]   # incl. B006 mutable defaults, E722 bare except

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q --cov=wafr_pipeline --cov-report=term-missing"
```

## Hands-on Lab 6 — Test the Pipeline, Hunt the Bugs

| | |
|---|---|
| **Objective** | Build a pytest suite over cleaning and KPI code (≥ 80% coverage on those modules), pin a golden file, and find three planted bugs using systematic debugging |
| **Duration** | 50 minutes (Day 4 Hour 5) |
| **Setup** | `pip install pytest pytest-cov`; `git checkout lab6-start` (contains `tests/fixtures/` minis and three planted bugs); VS Code debugger configured |

**Instructions & tasks**

1. *(10 min)* Write the cleaning unit tests: normalisation, Arabic SKU survival, the conservation invariant (`in == out + rejected`), and the parametrised timestamp table. Run; **two tests fail** — that's the hunt starting.
2. *(10 min)* Bug 1 (loud): read the traceback bottom-up, identify the mistyped exception in `parse_sold_at` (`except ValueError` vs the raised `TypeError` on None input); shrink to a one-row reproduction; fix; keep the reproduction as a regression test.
3. *(10 min)* Bug 2 (silent): the conservation invariant fails — `clean_tables.py` drops bad-price rows *without counting one category*. Use `breakpoint()` inside `clean_sales`, inspect the masks, fix the report dict. Discuss: no traceback would ever have come.
4. *(10 min)* Golden file: run the reference pipeline on the mini fixture, save `expected_kpis.parquet`, write `test_daily_kpis_match_golden` plus the fan-out property test. Bug 3 reveals itself: the golden comparison fails on one column — the planted rounding change (per-record vs boundary). Decide which behaviour is *correct*, fix, regenerate the golden **in its own commit with a message explaining why**.
5. *(5 min)* Coverage: `--cov-report=term-missing`; add one test to cover the highest-value uncovered branch (the empty-input path); confirm ≥ 80% on `cleaning.py` + `clean_tables.py`.
6. *(5 min)* ruff over the whole repo; fix findings; commit `test: pipeline suite with golden file (14 tests, 84% cov)`; push and open the PR — your partner reviews the *asserts*, not just the diff.

**Expected output**
```
$ pytest
.............. 14 passed in 2.31s
---------- coverage ----------
cleaning.py        94%   clean_tables.py    86%
kpi_tables.py      81%   TOTAL (gated)      84%
$ ruff check src tests
All checks passed!
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` in pytest but not in scripts | Package not installed editable; tests import differently | `pip install -e .` — Module 7 formalises this the next morning |
| Golden test fails with a wall of DataFrame diff | Column order / dtype drift, not values | `check_like=True`, compare dtypes first — read the assertion output, it says which |
| `assert_frame_equal` fails on the 12th decimal | Float round-trip through parquet | `atol=0.01` with a comment justifying the tolerance |
| Debugger never hits the breakpoint | Breakpoint in the un-imported copy (src vs stale install) | `pip install -e .`; check `module.__file__` |
| Coverage stuck below 80% | Error-path branches untested | `term-missing` lists the lines; test the *reject* paths — they're the point |
| Tests pass alone, fail together | Shared mutated fixture (module-scope frame edited in place) | Copy in the fixture or narrow the scope — test independence |

**Instructor notes.** Bug 3's decision moment (which rounding is correct?) matters more than the fix — make the pair *say the business rule out loud* before touching code, and enforce the golden-regeneration-in-own-commit ritual on the projector. If time is tight, cut task 5's extra coverage test, never the golden-file governance discussion. Fast finishers: freeze the clock — inject a `now()` function into anything date-dependent and test the month-boundary case; or add a `pytest.ini` marker separating `slow` component tests.

## Mini Exercises

**Quiz (5 questions)**
1. Why do silent failures dominate data code, and what is the only reliable catch? → wrong-but-plausible numbers raise nothing; a test with a known answer.
2. What does the conservation invariant `len(in) == len(out) + rejected` protect against? → uncounted drops — the audit-gap bug class.
3. When is regenerating a golden file legitimate? → deliberate, explained, reviewed change to intended behaviour — its own commit, never to silence red.
4. A traceback shows `KeyError: 'temp_c'` inside pandas internals. Where do you look? → up-stack at *your* frame that passed the key; the exception type says "missing key", the frame says whose.
5. Your suite has 96% coverage and missed the fan-out bug. How? → coverage measures execution, not verification — no assert examined row counts.

**Debugging exercise.** `debug_me_m6.py`: the weekly report crashes only when run for weeks containing a branch with zero sales (empty group → `.agg` on empty frame → dtype surprise). Participants must reproduce with a one-branch fixture, fix, and leave the fixture as a regression test — the full canonical loop, unassisted.

**Code-review exercise.** Review a PR adding tests that (a) assert `clean(df) is not None`, (b) copy the implementation's formula into the test, and (c) regenerate the golden file in the same commit as a logic change, message "fix tests". Three findings; each maps to a rule from this module.

**Discussion questions.**
- Your manager asks "are we sure the dashboard numbers are right?" What artefact answers that better than confidence, and what does it cost to maintain? (the suite + golden files; minutes per change)
- Which single function in *your* pipeline would cost the most if silently wrong, and what is its first test? (each pair answers concretely — this becomes their capstone test plan)

## Case Study — The Quiet Quarter-End Bug at a Riyadh Retail Bank

**Scenario.** A Riyadh retail bank's analytics team maintains a Python job aggregating branch fee income for the monthly management pack. A refactor (performance-motivated, reviewed only by eye) changed a groupby key from `["branch", "product"]` to `["branch"]` in one intermediate step; a downstream merge then attributed all card-fee income to each branch's *first* product line. Totals stayed exactly right — the split was wrong. The error ran for two month-ends before a product manager challenged a number she knew from her own records.

**Business context.** The pack informs product-line investment decisions; two months of decisions were made on a wrong split. The post-incident review found: zero tests on the job, review performed on the diff only ("it looked equivalent"), and no fixture where the correct split was known. NDMO-aligned internal data-governance policy now requires demonstrable quality controls on management-reporting pipelines.

**Technical challenge.** Retrofit a test harness onto a 1,400-line untested job — without pausing the monthly run — such that the incident class (silent aggregation change) cannot recur.

**Constraints.** The job must keep running monthly during the retrofit; production data cannot leave the bank's environment (fixtures must be synthetic but structurally faithful); the team has two sprints; auditors want evidence they can re-run.

**Solution approach (facilitate, don't lecture).** (1) **Characterisation first:** run the current (now-fixed) job on a synthetic fixture and pin outputs as golden files — the job's behaviour is now *defined* before any refactor; (2) extract the three money-math functions into testable units (Module 1's surgery, performed late but possible); property tests: per-branch totals equal the sum of product splits — precisely the invariant the bug violated; (3) the review checklist gains a rule: any change to a groupby/merge key requires a fixture demonstrating the split; (4) the suite runs pre-merge (Module 5's PR gate) and its green run is archived with each month-end as the auditor's evidence. Cost of the whole harness: about three days. Cost of the incident: two months of misdirected decisions and a standing agenda item titled "can we trust the pack?"

**Discussion questions.**
1. The diff "looked equivalent" to a competent reviewer. Why did review fail where a test would not? (equivalence of *behaviour* is checkable only by execution on known answers)
2. Which single property test kills this bug class forever? Write its assert in one line.
3. Why characterise *before* refactoring, even though the current code was just proven wrong once? (you need a stable definition of "unchanged" to refactor against; deliberate changes then show up as deliberate diffs)
4. What makes a synthetic fixture "structurally faithful", and who validates that? (same keys, cardinalities, edge cases as production; the domain owner signs off)

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Suite runtime (unit + component) | Performance | ≤ 5 s on lab laptop | pytest duration |
| Coverage on cleaning/KPI modules | Quality | ≥ 80% branch-relevant lines, asserts reviewed | pytest-cov + PR review |
| Planted bugs found and regression-tested | Correctness | 3/3, each with a kept reproduction test | lab checkpoint |
| Golden-file governance | Process | regeneration in own commit with rationale, 100% of cases | history audit |
| ruff findings | Quality | 0 on `src/` and `tests/` | ruff check |
| Conservation invariant present | Quality | yes, and failing when counts drift | mutation spot-check |

**Example benchmark table (filled during lab):**

| Checkpoint | Tests | Coverage (gated modules) | Suite time | Bugs found |
|---|---|---|---|---|
| lab6-start | 0 | 0% | — | 0/3 |
| After task 3 | 9 | 71% | 1.4 s | 2/3 |
| End of lab | 14 | 84% | 2.3 s | 3/3 |

## Required Visuals and Training Assets

### Diagrams
1. **Loud vs silent failure map** — *Purpose:* the module's anchor. *Elements:* two failure paths from "bug introduced": loud → traceback → fixed same day; silent → plausible number → slide → decision → discovered by a human months later; a tests-gate icon intercepting the silent path. *Style:* branching timeline, the silent branch drawn longer and darker, English labels with Arabic subtitles.
2. **Testing pyramid for data pipelines** — *Elements:* unit (pure functions, ms) / component (steps on fixtures, s) / end-to-end (mini pipeline, s–min) with counts and runtimes from the golden thread. *Style:* pyramid with a stopwatch per layer.
3. **The canonical debugging loop** — *Elements:* traceback → hypothesis → cheapest observation → shrink → failing test → fix → green → regression test kept; drawn as a loop that *exits through the test suite*. *Style:* circular flow, printable A4.
4. **Golden-file lifecycle** — *Elements:* create (reviewed) → guard (every run) → red = question → deliberate regeneration (own commit, rationale) — with a red ✗ on the "edit file to make test pass" shortcut. *Style:* lifecycle with one forbidden path.

### Images (screenshots)
1. **pytest failure diff on a DataFrame comparison** — *why:* the assertion output is a skill to read; *content:* `assert_frame_equal` failure naming column, dtype, and first mismatching row.
2. **VS Code debugger paused inside `clean_sales`** — *why:* breakpoints over print-scatter; *content:* variables pane showing the masks, conditional breakpoint visible.
3. **`term-missing` coverage report** — *why:* shows *which* lines the number hides; *content:* the reject-path lines highlighted as uncovered.
4. **The golden-regeneration commit** — *why:* models the governance ritual; *content:* single-file diff of `expected_kpis.parquet` with a message explaining the rounding decision.

### Simulations
1. **Silent-drop mutation** — *Setup:* branch `sim-uncounted` where one rejection category is dropped uncounted. *Expected:* all tests pass *except* the conservation invariant — proving that specific test earns its place. *Learning objective:* invariants catch what example-based tests miss.
2. **Flaky time bomb** — *Setup:* a test using `date.today()` that passes all month and fails on the 1st. *Expected:* participants diagnose date-dependence and inject a clock. *Learning objective:* determinism; flaky tests erode trust.
3. **Coverage theatre** - *Setup:* branch with 95% coverage and assert-free tests; the fan-out bug reintroduced. *Expected:* green suite, wrong revenue; participants find the missing asserts. *Learning objective:* review asserts, not percentages.

### Interactive Activities
- **"Will a test catch it?" bug triage (15 min):** ten one-line bug descriptions from the week's modules; teams name the *cheapest* test type that catches each, or admit none does and design the invariant that would.
- **Traceback speed-reads (10 min):** four real tracebacks on screen; pairs have 60 seconds each to name the file/line to open first and the hypothesis to test.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tests/fixtures/mini_sales.parquet` | Course tooling: 200 crafted rows, every edge case represented and documented | Parquet | 200 rows | Unit/component fixture |
| `tests/fixtures/mini_weather.parquet` | Course tooling | Parquet | 21 rows | Merge tests |
| `tests/fixtures/expected_kpis.parquet` | Generated in-lab from reference solution | Parquet | 12 rows | Golden file (participants create it — ownership matters) |
| `lab6-start` planted bugs ×3 | Course repo branch | Git branch | — | The hunt |

### Demo Requirements
- **Instructor demo:** the silent-failure story told through Bug 2 live — breakpoint, mask inspection, the moment the uncounted drop appears; then the golden-regeneration ritual done properly on the projector.
- **Student demo:** one pair presents their favourite regression test and the bug biography behind it ("this test exists because…").
- **Expected outputs:** green 14-test suite, golden file committed with rationale, three regression tests — the safety net under Day 5's capstone refactoring.

---

# Module 7 — Environments and Dependency Management

## Module Overview

**Purpose.** "Works on my machine" is not a joke; it is the default state of Python projects that skip this module. Virtual environments isolate each project's dependencies; pinned requirements make installations reproducible; `pyproject.toml` turns a folder of scripts into an installable package; and a bound Jupyter kernel keeps notebooks honest about which environment they run in. This module makes the golden-thread pipeline *portable* — from author to teammate to server — and completes the professional-practice foundation the tracks build on.

**Business relevance.** Dependency chaos is a silent tax on every data team: onboarding that takes days ("install these 14 things, good luck"), analyses that cannot be reproduced when challenged, and the production incident where a routine `pip install` upgraded pandas and changed behaviour overnight. Reproducibility is also a governance property — an analysis that cannot be re-run is an analysis that cannot be audited. Teams that can say "clone, create venv, `pip install -e .`, done" ship; teams that cannot, explain.

**Industry use cases.**
- A consulting data team hands a ministry client a repository that reproduces the full analysis in three commands — the handover *is* the deliverable.
- A bank's model-validation unit re-runs a submitted analysis in a clean environment from the lock file; "cannot reproduce" is an automatic return-to-sender.
- A team of five analysts stops breaking each other's projects the week they abandon the shared global interpreter for per-project venvs.

**Expected competencies.** After this module a participant can create and manage venvs, install and inspect packages with pip, distinguish direct dependencies from a frozen lock, author a `pyproject.toml` and install their project editable, bind Jupyter kernels to specific environments, and diagnose the standard environment failure modes (wrong interpreter, stale install, version conflict).

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Explain why per-project isolation exists and what the shared-interpreter failure mode looks like | LO6 |
| 7.2 | Create, activate, and manage virtual environments with venv | LO6 |
| 7.3 | Pin dependencies for reproducibility: direct requirements vs frozen lock | LO6 |
| 7.4 | Package the project with pyproject.toml and install it editable | LO6, LO1 |
| 7.5 | Bind Jupyter kernels to environments and verify which interpreter a notebook uses | LO6, LO5 |

## Technical Content

### 1. The failure mode this module deletes

One global interpreter, five projects: project A needs pandas 2.x behaviour, project B's old scripts assume 1.5; a `pip install` for a tutorial upgrades NumPy and three transitive dependencies; six months later *nothing* is sure to run. The demonstrable symptoms participants have likely met: `ImportError` after an unrelated install, a script that ran in March failing in June with no code change, and the notebook that works for the author and ImportErrors for everyone else.

The model taught: **an environment is a disposable, per-project set of installed packages plus a specific interpreter.** Environments are cattle, not pets — cheap to create, cheap to destroy and rebuild; the *definition* (requirements, pyproject) is the asset and lives in Git; the environment folder itself never does (`.venv/` was in `.gitignore` from Day 2's birth ritual — now the class learns why).

### 2. venv and pip mechanics

- `python -m venv .venv` → activate (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` elsewhere) → the prompt changes → `which python`/`where python` proves the switch. The three-line diagnosis ritual for any weirdness: **which python, which pip, pip list.**
- `pip install pandas`, `pip list`, `pip show pandas` (version, dependencies, location), `pip uninstall`. Version specifiers: `==` exact, `>=` floor, `~=2.2` compatible-release; what a *transitive* dependency is (installing pandas brought NumPy — `pip show` reveals the graph).
- VS Code and the interpreter picker: the editor must point at `.venv` or every squiggle lies; the status-bar interpreter check becomes reflex.
- Deleting `.venv` and rebuilding from the definition is the fix for most corruption — rehearsed in the lab so it holds no fear. (uv/conda exist and are faster/heavier respectively; the course teaches stdlib venv because it is always available, and names the alternatives honestly.)

### 3. Pinning: the two-file discipline

- **`requirements.txt`** (curated, human-written): *direct* dependencies with sensible bounds — `pandas~=2.2`, `numpy~=2.0`, `requests~=2.32`. This states intent.
- **`requirements.lock`** (generated: `pip freeze > requirements.lock`): every package, exact versions, transitive included. This states *fact* — the environment that actually ran.
- The re-run contract: teammates and servers install from the lock (`pip install -r requirements.lock`) and get byte-identical dependency sets; upgrades happen deliberately — edit the curated file, rebuild, run the Module 6 suite (this is *why* the suite exists), regenerate the lock in a reviewed commit. Dependency upgrades become PRs like any other change.
- The overnight-pandas-upgrade incident type, named: unpinned production environments change without anyone deciding they should. Pinning converts surprise into decision.

### 4. pyproject.toml: from scripts to package

The file participants have carried since Module 1's layout now gets fully explained:

- `[project]` metadata (name, version, `requires-python`, dependencies) — the modern single home for what `requirements.txt` prototyped; optional dev extras (`[project.optional-dependencies] dev = ["pytest", "pytest-cov", "ruff"]`) split runtime from toolchain.
- **Editable install:** `pip install -e .` puts `wafr_pipeline` on the path *as a package* — and every `ModuleNotFoundError`/`python -m` workaround from the whole week dissolves at once. This is deliberately the module's payoff moment: three separate troubleshooting rows from Labs 1, 3, and 6 all pointed here.
- src-layout revisited with its real rationale: tests and notebooks import the *installed* package — the same import path a server will use — instead of whatever folder they happen to run from.
- `[project.scripts] wafr-report = "wafr_pipeline.cli:main"` — the pipeline becomes a command; small, but it changes how participants think about their code (a tool, not a script).
- Tool config consolidation (`[tool.ruff]`, `[tool.pytest.ini_options]`) — one reviewable file governs the project, already seen in Module 6.

### 5. Jupyter kernels and environment honesty

- A notebook runs against a **kernel**, and the kernel is bound to an interpreter — not necessarily the one your terminal has active. The classic mystery ("pip installed it but the notebook can't import it") is a kernel/interpreter mismatch, diagnosed in one cell: `import sys; sys.executable`.
- The fix taught as ritual: `pip install ipykernel` in the venv, `python -m ipykernel install --user --name wafr-pipeline`, select the named kernel in Jupyter/VS Code. One kernel per project venv, named after the project.
- Notebooks in the reproducible project: they *import* the installed package (Module 1's promise, now airtight), keep outputs stripped (Module 5's policy), and anything a notebook proves gets promoted into the package where tests can hold it (Module 6). The notebook is a front-end; the environment and package are the machine.

### 6. Common mistakes & production considerations

1. Installing into the wrong environment (venv not active, or VS Code terminal vs picker mismatch) — the which-python ritual catches it in seconds.
2. Committing `.venv/` — hundreds of MB of platform-specific binaries in history; the definition is the asset, never the folder.
3. `pip freeze` into the *curated* file — intent and fact merge, and nobody can tell direct from transitive again; keep the two files distinct.
4. `sudo pip install` / installing into the system interpreter — breaks OS tooling on Linux servers; venvs always, everywhere.
5. Requirements with no versions at all ("it installed today, ship it") — the overnight-upgrade incident, scheduled.
6. One giant "data-science" venv for every project — the shared-interpreter failure mode wearing a venv costume.

Production considerations: servers install from the lock inside a fresh environment on every deploy — reproducibility is not optional there; Python-version pinning matters too (`requires-python = ">=3.12"`; the venv records it); security patching is the *other* reason upgrades must be easy — a pinned-forever environment is as dangerous as an unpinned one, so the deliberate-upgrade loop (edit → rebuild → test → lock) must stay cheap; and containerisation (Docker) is this module's ideas hardened one level further — named as the road ahead in SDA-AIE-113, not covered here.

## Code Examples

### The reproducibility kit

```toml
# pyproject.toml — the project's single source of truth
[project]
name = "wafr-pipeline"
version = "0.5.0"
description = "Wafr Markets daily sales pipeline (SDA-FND-103 golden thread)"
requires-python = ">=3.12"
dependencies = [
    "numpy~=2.0",
    "pandas~=2.2",
    "pyarrow~=17.0",
    "requests~=2.32",
]

[project.optional-dependencies]
dev = ["pytest~=8.2", "pytest-cov~=5.0", "ruff~=0.5", "ipykernel~=6.29"]

[project.scripts]
wafr-report = "wafr_pipeline.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/wafr_pipeline"]
```

```bash
# The three-command handover (goes in README.md, verified in the lab)
python -m venv .venv && .venv\Scripts\activate     # Windows (POSIX: source .venv/bin/activate)
pip install -e ".[dev]"
pytest -q && wafr-report --week 2026-W23           # green suite, then the report
```

### The deliberate-upgrade loop

```bash
# Upgrading pandas is a CHANGE, reviewed like any other change
git switch -c chore/pandas-2.3
# 1. edit pyproject.toml:  "pandas~=2.3"
pip install -e ".[dev]" --upgrade
# 2. the suite is the safety net this loop exists for:
pytest -q                          # golden files catch behaviour drift
pip freeze > requirements.lock     # 3. new FACT, committed with the change
git add pyproject.toml requirements.lock
git commit -m "chore: pandas 2.2 -> 2.3; suite green, goldens unchanged"
# open PR — the diff shows intent (pyproject) and fact (lock) together
```

### Environment diagnosis, scripted

```python
# src/wafr_pipeline/doctor.py
"""`python -m wafr_pipeline.doctor` — the first command support asks you to run."""
import importlib.metadata as md
import sys


REQUIRED = ["numpy", "pandas", "pyarrow", "requests", "pytest"]


def main() -> None:
    print(f"interpreter : {sys.executable}")
    print(f"python      : {sys.version.split()[0]}")
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print(f"virtualenv  : {'yes' if in_venv else 'NO — you are in the system interpreter'}")
    for pkg in REQUIRED:
        try:
            print(f"{pkg:12}: {md.version(pkg)}")
        except md.PackageNotFoundError:
            print(f"{pkg:12}: MISSING")


if __name__ == "__main__":
    main()
```

```python
# The one-cell kernel check taught for every notebook (cell 1, always)
import sys
print(sys.executable)        # must point into THIS project's .venv
import wafr_pipeline
print(wafr_pipeline.__file__)  # must point into src/ via the editable install
```

## Hands-on Lab 7 — Make It Reproducible

| | |
|---|---|
| **Objective** | Rebuild the project in a clean venv from definitions alone, complete `pyproject.toml` with an editable install and CLI entry point, bind a named Jupyter kernel, and prove clone-to-run on a partner's machine |
| **Duration** | 50 minutes (Day 5 Hour 2, includes capstone kickoff) |
| **Setup** | The week's repo; Python 3.12; partner pairs retained from Day 4 |

**Instructions & tasks**

1. *(5 min)* Deliberate destruction: deactivate and delete any existing environment. Run `python -m wafr_pipeline.doctor` against the system interpreter and read the damage (`virtualenv: NO`, missing packages) — the before picture.
2. *(10 min)* `python -m venv .venv`, activate, run the which-python ritual; complete `pyproject.toml` (dependencies with `~=` bounds, dev extras, the `wafr-report` script); `pip install -e ".[dev]"`.
3. *(5 min)* The payoff tour: `pytest -q` green with no path tricks; `wafr-report --week 2026-W23` works from *any* directory; revisit the three troubleshooting rows from Labs 1/3/6 that this install just retired.
4. *(10 min)* Pinning: write the curated `requirements.txt` note into README (or rely on pyproject), generate `requirements.lock` with `pip freeze`; commit both with the README's three-command handover block.
5. *(10 min)* **The handover test:** partner clones your repo fresh, runs exactly the three README commands, and must reach a green suite + working report with zero questions asked. Every question they have to ask is a README bug — fix it and re-test.
6. *(5 min)* Jupyter: install the named kernel (`wafr-pipeline`), open the analysis notebook, run the kernel-check cell, confirm `sys.executable` points into `.venv`.
7. *(5 min)* Capstone kickoff: tag `v0.5-reproducible`; review the capstone checklist against your repo — most items are already green; plan the gaps.

**Expected output**
```
$ python -m wafr_pipeline.doctor
interpreter : C:\work\wafr-pipeline\.venv\Scripts\python.exe
python      : 3.12.4
virtualenv  : yes
numpy       : 2.0.1
pandas      : 2.2.3
pyarrow     : 17.0.0
requests    : 2.32.3
pytest      : 8.2.2

$ wafr-report --week 2026-W23
[kpi] 28 branch-days | revenue SAR 6,204,881.75 | report -> outputs/week23.json

# Partner's machine, from README alone:
$ pytest -q
.............. 14 passed in 2.40s
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `wafr-report: command not found` | venv not active, or entry point added after install | Activate; `pip install -e .` re-run picks up new scripts |
| Notebook can't import what the terminal has | Kernel bound to another interpreter | The kernel-check cell; select the named kernel — never trust the default |
| Partner's install fails on pyarrow | Their Python is 3.10 (below `requires-python`) | The error message names it; discuss why the pin is a *feature* |
| `pip install -e .` errors on build backend | Typo'd `[build-system]` table | Compare against the reference; TOML is picky about tables |
| Editable import points at stale code | Two clones, wrong one installed | `wafr_pipeline.__file__` tells the truth; reinstall from the right clone |
| Windows activation blocked by execution policy | PowerShell script policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (pre-course checklist item; floater assists) |

**Instructor notes.** Task 5 is the module: the partner-clone test converts "reproducibility" from concept into a pass/fail experience, and README bugs found here are capstone points saved. Keep the destruction in task 1 theatrical but safe (definitions are committed — that is the lesson). Fast finishers: add `python -m wafr_pipeline.doctor` as the README's first troubleshooting step, or time a full cold rebuild (venv + install + suite) and post it to the leaderboard — typical: under 4 minutes.

## Mini Exercises

**Quiz (5 questions)**
1. What exactly does `.venv` contain, and why is it never committed? → an interpreter link + installed packages (platform-specific artefacts); the *definition* is the asset, the folder is disposable.
2. `requirements.txt` vs `requirements.lock` — intent vs fact. Explain. → curated direct deps with bounds (what we mean) vs frozen exact snapshot incl. transitives (what actually ran).
3. Why did `pip install -e .` eliminate the week's `ModuleNotFoundError`s? → the package is on the path via the installed metadata, same import path everywhere — terminal, pytest, notebook, server.
4. A notebook can't import pandas but `pip show pandas` succeeds in the terminal. First cell to run? → `import sys; print(sys.executable)` — kernel/interpreter mismatch until proven otherwise.
5. Name the two opposite dependency dangers. → unpinned drift (surprise upgrades) and pinned-forever rot (unpatched CVEs); the answer to both is the cheap deliberate-upgrade loop.

**Debugging exercise.** `sim-two-pandas`: a machine with the project venv on pandas 2.2 and a stray user-site pandas 1.5; the notebook silently imports the old one and a `groupby(observed=True)` behaves differently. Participants must diagnose via `pandas.__version__` + `pandas.__file__` + `sys.path` order, then fix by rebuilding the kernel binding. The lesson: *where* an import comes from is always answerable.

**Code-review exercise.** Review a PR that adds `pandas==2.2.3` to pyproject's dependencies (exact-pins a library project), commits `.venv/` "so it works out of the box", and upgrades three packages in a commit titled "fix". Three findings, each tied to a rule from this module.

**Discussion questions.**
- Your team standardises on one shared venv per team "to keep things simple". Predict the timeline of its failure. (project-coupled upgrades collide; it is the global interpreter with extra steps)
- What is the *minimum* a reviewer should demand before merging a dependency upgrade? (green suite incl. goldens, lock regenerated, one-line rationale)

## Case Study — The Analysis That Could Not Be Re-Run

**Scenario.** A policy-analysis unit in a Saudi government entity produced an influential study on service-adoption patterns 14 months ago. A follow-up study is commissioned, and the new analyst is asked to first *reproduce* the original numbers. The original author has rotated out; what remains is a folder: nine notebooks, no environment definition, `import utils` resolving to a module that no longer exists, and a `pip list` from the author's old laptop screenshot in an email — the closest thing to a lock file the unit has.

**Business context.** The study's findings shaped a budget line. If the numbers cannot be reproduced, the unit faces an uncomfortable choice: silently re-derive something close and hope, or report that a published, decision-shaping analysis is unverifiable. Leadership has since adopted internal reproducibility requirements aligned with national data-governance direction (NDMO), making this the test case.

**Technical challenge.** Forensically reconstruct a working environment (the screenshot narrows pandas to 1.x — with materially different default behaviours), extract the logic from notebooks into a package, and re-produce the study — then institutionalise the practices that make the *next* reproduction a three-command exercise.

**Constraints.** The original data snapshot exists (properly archived — one thing done right); the analyst has four weeks; some notebook cells were clearly run out of order (Module 1's hidden-state smell at archaeological scale); the unit's new standard requires every future study to be re-runnable by a stranger.

**Solution approach (facilitate, don't lecture).** (1) Environment archaeology: build a candidate venv from the screenshot versions, binary-search the pandas version until the one legacy behaviour (silent dtype coercion the original relied on) reproduces a checkpoint number; (2) linearise the notebooks — extract logic into a package with the execution order made explicit as a pipeline function; golden-file the original's published tables as the reproduction target; (3) reproduce, documenting the two numbers that differ and *why* (an out-of-order cell in the original — now a finding, honestly reported); (4) institutionalise: the unit's study template becomes the golden-thread layout — pyproject, lock, tests, kernel-per-project, three-command README — and "reproducible by a stranger" becomes a sign-off checkbox, verified by the partner-clone test from Lab 7. The postscript participants should articulate: the 14-month-old mess cost four weeks; the practices cost minutes per study.

**Discussion questions.**
1. Rank the missing artefacts by how much of the four weeks each would have saved (lock file, pyproject, linear pipeline, tests/goldens).
2. Was the original author negligent, or was the *system* missing? What does the unit's template change about individual behaviour?
3. The reproduction differs in two numbers and the original is published. Draft the two-sentence honest disclosure.
4. Why is "reproducible by a stranger" the right bar, rather than "reproducible by the author"? (the author's machine and memory are exactly what rotates out)

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Cold rebuild (venv + editable install + suite) | Reproducibility | ≤ 5 min on lab laptop | timed in lab |
| Partner clone-to-green from README alone | Reproducibility | 100% pairs, zero questions asked | handover test |
| `doctor` output | Correctness | venv yes, all required packages versioned | lab checkpoint |
| Lock file freshness | Process | lock regenerated in every dependency-changing commit | history audit |
| Kernel binding | Correctness | notebook `sys.executable` inside project `.venv` | kernel-check cell |
| `.venv/` or data in Git history | Hygiene | 0 occurrences | history audit |

**Example benchmark table (filled during lab):**

| Checkpoint | Median | Slowest | Notes |
|---|---|---|---|
| venv create + activate | 40 s | 90 s | Windows execution-policy case |
| `pip install -e ".[dev]"` | 1 m 50 s | 4 m | venue bandwidth dependent |
| Suite green in fresh env | 2.4 s | 3.1 s | |
| Partner clone-to-green | 4 m 10 s | 7 m | two README bugs found and fixed |

## Required Visuals and Training Assets

### Diagrams
1. **One machine, many environments** — *Purpose:* the module's anchor. *Elements:* system interpreter (locked, hands-off) beside three project boxes, each with its own `.venv` (interpreter + packages at different versions); a red tangle diagram of the shared-interpreter alternative alongside. *Style:* boxes-and-versions schematic, English labels with Arabic subtitles.
2. **Intent vs fact: the two-file discipline** — *Elements:* pyproject/requirements (human-curated, bounded) flowing through `pip install` into an environment, `pip freeze` flowing out into the lock; the deliberate-upgrade loop drawn around them with the test suite as its gate. *Style:* cycle diagram; the suite gate visually reuses Module 6's pyramid icon.
3. **Where does an import come from?** — *Elements:* notebook → kernel → interpreter → site-packages → the package, with the two mismatch points (kernel binding, editable install) flagged; the `sys.executable` probe drawn as a stethoscope. *Style:* vertical resolution chain, printable A4.
4. **The handover** — *Elements:* repo (definitions only) crossing a machine boundary; three commands; green suite on the far side; a crossed-out `.venv` and data folder staying behind. *Style:* two-machine strip with the README as the bridge.

### Images (screenshots)
1. **`doctor` before/after** — *why:* the module's before/after anchor; *content:* system-interpreter damage report beside the healthy venv report.
2. **VS Code interpreter picker on `.venv`** — *why:* the mismatch most likely to bite in week one on the job; *content:* status bar + picker with the project venv selected.
3. **Jupyter kernel list with the named project kernel** — *why:* the binding ritual's target state; *content:* `wafr-pipeline` kernel selected, kernel-check cell output beneath.
4. **The upgrade PR diff** — *why:* models the deliberate-upgrade loop; *content:* pyproject one-liner + regenerated lock + green-suite note in the message.

### Simulations
1. **Two-pandas machine** — *Setup:* branch/VM with a stray user-site pandas 1.5 shadowing the venv's 2.2 in the notebook only. *Expected:* one groupby result differs between script and notebook; diagnosed via `__version__`/`__file__`/`sys.path`. *Learning objective:* import provenance is always answerable.
2. **The overnight upgrade** — *Setup:* unpinned scratch env; instructor installs a package that upgrades pandas mid-day. *Expected:* one golden test goes red "by itself"; participants trace it to the dependency change, not code. *Learning objective:* unpinned environments change without decisions; the suite notices.
3. **Broken venv, calm rebuild** — *Setup:* corrupt `.venv` (deleted DLL / mangled scripts). *Expected:* delete and rebuild from definitions in under five minutes, zero data loss. *Learning objective:* environments are cattle; definitions are the asset.

### Interactive Activities
- **README bug hunt (15 min):** pairs swap repos for the handover test; every question a partner must ask is logged as a README bug on the board; the pair with zero questions wins.
- **"Which file does this belong in?" sort (10 min):** twelve statements (pandas ~=2.2, exact pytest version, ipykernel, `.venv/`, ruff config, Python floor…) sorted onto pyproject / lock / .gitignore / nowhere posters.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| The week's own repo | Participants (Days 1–4) | Git repo | ~40 files | The reproducibility subject — golden thread |
| `sim-two-pandas` image/branch | Course tooling | VM snapshot / branch | — | Import-provenance debugging |
| Reference `pyproject.toml` + lock | Course repo | TOML/txt | 2 files | Comparison target |

### Demo Requirements
- **Instructor demo:** the deliberate destruction and five-minute rebuild, timed on the projector; the two-pandas diagnosis run live from symptoms to `sys.path`.
- **Student demo:** the winning zero-questions handover pair walks through what their README says that others' didn't.
- **Expected outputs:** every repo tagged `v0.5-reproducible` with a verified three-command handover — the exact state the capstone builds on that afternoon.

---

# Final Capstone Project

## Title: Wafr Markets End-to-End Daily Sales Pipeline (Mini-Project)

## Project Scenario

You are the data engineer for **Wafr Markets**, a Saudi neighbourhood-grocery chain whose messy point-of-sale exports you have been taming all week. Head office now wants the weekly KPI report *productionised*: a colleague in another city must be able to clone your repository, rebuild the environment, and run the full pipeline on a week of data they have never seen — with every rejected row counted, every number reconcilable, and the weather-sensitivity insight the merchandising team has started planning around.

The capstone is not a new build; it is the integration and proving of everything from Labs 1–7 against **a fresh, unseen week of data (`2026-W24`)** that the instructor releases at Day 5 Hour 3. The new week contains fresh dirt, each piece answerable by one module: a fifth branch (`MED-007`) opening mid-week (the expected-branches manifest must change), a six-hour weather-API outage window (retries + cache must ride it out), one replayed duplicate POS file (the dedup key earns its keep), and a third timestamp format (the parse table extends — and its parametrised test extends with it).

## Requirements

**Mandatory (maps to grading rubric):**

1. **Structured package (LO1):** src-layout `wafr_pipeline` package; frozen-dataclass records with boundary validation; functions with type hints; the `wafr-report` CLI entry point; no logic stranded in notebooks.
2. **Resilient acquisition (LO5, LO2):** `run_ingest` handles the full raw week — pathlib globbing, per-file encodings, quarantined rejections with counted reasons, weather client with timeout/retry/backoff/pagination/disk cache — and survives the outage window without manual intervention.
3. **Vectorised KPI engine (LO2):** NumPy revenue/discount statistics with the branch×hour matrix; the loop-vs-vector benchmark re-run on week 24 and recorded (≥ 50× target); `np.allclose` reconciliation against the pandas pivot.
4. **pandas transform layer (LO2):** `clean_sales` with counted decisions reconciled against the manifest; the weather merge with `validate="m:1"` and `indicator=True`; the daily-KPI frame written to `data/marts/` in parquet.
5. **Git evidence (LO3):** capstone work on a branch, submitted via pull request with a completed peer review; ≥ 10 meaningful commits across the week; tags `v0.5-reproducible` and `v1.0-capstone`; no data or `.venv/` anywhere in history.
6. **Test suite (LO4):** ≥ 80% coverage on `cleaning.py`, `clean_tables.py`, `kpi_tables.py`; the golden-file test, conservation invariant, fan-out property test, and every regression test from the week's bug hunts still green; ruff clean.
7. **Reproducibility (LO6):** complete `pyproject.toml` + `requirements.lock`; the three-command README handover verified by a partner on their machine; named Jupyter kernel; `python -m wafr_pipeline.doctor` reports a healthy environment.
8. **Notebook front-end + insight (LO5):** one analysis notebook that *imports* the installed package, runs top-to-bottom cleanly, and answers the temperature↔cold-drinks question for week 24 in one sentence a merchandiser could act on.

**One extension (choose at least one):**
- **Month mode:** `wafr-report --month 2026-06` aggregating four staged weeks, with one test covering the month boundary
- **Rejection report as a product:** quarantined rows written to `outputs/rejections_week24.csv` with reason codes + a per-source summary table for the ops team
- **Replay guard:** file-level dedup by content hash with a `[skip-replay]` log line, tested against the planted duplicate file
- **KPI enrichment:** price bands (`pd.cut`) or channel-mix percentages added to the daily-KPI frame, golden file regenerated in its own justified commit
- **`doctor` v2:** extend the diagnosis module to verify data folders, stub reachability, and kernel binding — the README's first troubleshooting step

## Architecture (target state)

```
data/raw/2026-W24/*.csv ──┐                        course weather stub (or cache)
      (5 branches, dirt)  │                                   │ retry·backoff·cache
                          ▼                                   ▼
              ingest_files.read_pos_file ──► records.SaleRecord ◄── weather_api.fetch_readings
                          │ quarantine + counted reasons
                          ▼
              data/staged/week24.jsonl ──► clean_tables.clean_sales (counted decisions)
                                                      │
                                   kpi_arrays (NumPy) ⇄ np.allclose ⇄ kpi_tables (pandas groupby
                                                      │                + validate="m:1" weather merge)
                                                      ▼
                                  data/marts/daily_kpis.parquet
                                                      │
                        wafr-report --week 2026-W24 ──┴──► outputs/week24.json + analysis notebook

Git: branch ──► PR ──► peer review ──► main        pytest suite + golden files gate the merge
Env: pyproject.toml + requirements.lock ──► clone-to-run in 3 commands on any machine
```

## Deliverables

1. Repository URL (classroom GitHub org) with the full week's history, tags, and the merged capstone PR
2. Terminal transcript (or screenshot) of the fresh-clone run: three README commands → green suite → `wafr-report --week 2026-W24` output
3. `outputs/week24.json` + `data/marts/daily_kpis.parquet` regenerated from raw by the pipeline (not hand-edited)
4. The analysis notebook, run top-to-bottom, ending with the one-sentence merchandiser insight
5. `DECISIONS.md`: three one-paragraph decisions with rationale (e.g., which merge side to dedupe, rounding boundary, what the new branch does to the manifest)
6. 5-minute demo: cold clone-to-run, one planted-dirt story ("here is how the pipeline caught it"), one test explained assert-by-assert

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: reproducible base — Lab 7 done, `v0.5-reproducible` tagged, capstone gaps listed | Day 5 end of Hour 2 | partner handover test passed |
| M-B: week-24 raw ingested end to end, rejections reconciled against manifest | Day 5 Hour 3 | `run_ingest` summary matches manifest |
| M-C: KPI mart built, suite green ≥ 80%, submission PR open | Day 5 Hour 4 (first half) | CI-style checklist self-audit |
| M-D: peer review exchanged and addressed, `v1.0-capstone` tagged | Day 5 end of Hour 4 | review comments resolved in commits |
| M-E: demo + rubric assessment | Day 5 Hour 5 | live scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| End-to-end correctness & reconciliation | 20 | Week 24 runs raw-to-report unattended; every count reconciles to the manifest; all four planted-dirt items caught and explained | Pipeline completes; one count unexplained or one dirt item handled manually | Manual patching between stages, unreconciled totals, or hand-edited outputs |
| Code structure & Python quality (LO1) | 15 | Clean package layout; validated records; typed, single-purpose functions; CLI works from any directory | Mostly clean; some logic still notebook-stranded or one god-function | Script sprawl, no boundary validation, copy-pasted logic |
| Data handling: NumPy + pandas (LO2) | 20 | Vectorised engine with recorded ≥ 50× benchmark; counted cleaning decisions; validated merge; NumPy⇄pandas reconciliation true | Vectorised but benchmark unrecorded, or one uncounted drop; merge validated | Python loops over rows, silent drops, unvalidated merge (or the fan-out present) |
| Version control & collaboration (LO3) | 10 | Meaningful history; PR with substantive peer review addressed; correct tags; clean history (no data/.venv) | History adequate; review shallow or tags late | Single end-of-day dump commits, no PR, or data in history |
| Testing & debugging evidence (LO4) | 15 | ≥ 80% gated coverage; golden + invariant + regression tests green; new timestamp format test-first; ruff clean | Coverage 70–80% or new format fixed without a test | Coverage theatre, goldens regenerated to silence red, ruff failures |
| Reproducibility & environment (LO6) | 10 | Partner clone-to-green from README alone, zero questions; lock fresh; doctor healthy; kernel bound | Handover needed one question; lock stale by one commit | Works only on author's machine; `.venv` committed; no lock |
| Demo, notebook & insight (LO5) | 10 | Cold demo lands; notebook runs top-to-bottom; insight stated as an actionable sentence | Demo works with a stumble; insight stated but not actionable | Cannot run own repo cold; notebook needs hidden state |

**Pass ≥ 70. Distinction ≥ 90.** The chosen extension earns up to +5 bonus (capped at 100) only if all mandatory items score ≥ 80%.

## Assessment Criteria Notes for Instructors

- Grade **from the repository first** (history, tags, PR review thread, coverage report in the last commit), the demo second — the week's thesis is that the repo carries the evidence.
- The four planted-dirt items are your fastest probe: ask "show me where the pipeline caught the replayed file" — participants who built the week's habits answer in one `git log` or one test name.
- Anti-pattern flags that cap a criterion at 70%: golden files regenerated in the same commit as logic changes; rejection counts that don't sum (`in ≠ out + rejected`); `validate=` removed to "make the merge work"; a README handover that failed on the partner but was not fixed.
- Verify one claim live per participant: break the casing of a branch code in a REPL and ask which test goes red, or ask for `wafr_pipeline.__file__` to prove the editable install.
- Score during the Hour 5 demos on the printed rubric; the repository URLs collected at end of Hour 4 give you the history inspection window.

## Bonus Tasks (for early finishers / distinction seekers)

1. **Second city, zero code changes:** add a `NEOM-001` branch to the manifest and raw folder and show the pipeline absorbs it — then write the one test that would have caught a hard-coded branch list
2. **Cold-rebuild race:** timed venv + editable install + suite from a fresh clone; post to the leaderboard (target: under 4 minutes)
3. **Lineage note:** a `LINEAGE.md` tracing one number in `week24.json` backwards through every function and file to the raw rows that produced it
4. **The pitch:** a 10-line summary to Wafr's (fictional) head of operations: what the pipeline replaces, what a rejected row now costs to investigate, and what SDA-FND-104's skills would add next

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** `prices = prices.sort()` — what is `prices` afterwards, and why? → `None`; `.sort()` mutates in place and returns None — assign nothing, or use `sorted()`.
**Q2.** Why is `SaleRecord` a *frozen* dataclass? → validated once at the boundary, then immutable — records can be shared, hashed, and trusted downstream.
**Q3.** Checking "seen this transaction key before?" 100k times — which collection and why? → `set`; O(1) hashed membership vs O(n) list scans.
**Q4.** Why open files with a context manager (`with`)? → guaranteed close on success *and* exception — no leaked handles, no half-flushed writes.
**Q5.** A required API field is absent. `payload["field"]` or `payload.get("field", 0)`? → `[...]`: required means a loud KeyError, not a silent plausible zero.
**Q6.** Why must every `requests` call carry a `timeout`? → the default waits forever; one hung call becomes a hung pipeline.
**Q7.** Why is `arr * 1.15` faster than a Python loop over the same values? → one C-level loop over contiguous typed memory; no per-element interpreter and object overhead.
**Q8.** `sub = arr[:100]; sub[:] = 0` — what happened to `arr`? → its first 100 elements are zero; basic slices are *views*, not copies.
**Q9.** Shapes `(4, 24)` and `(4, 1)` in an operation — legal? Result? → yes; the size-1 axis broadcasts to 24 → `(4, 24)`.
**Q10.** Why store a missing temperature as `NaN` rather than `-999`? → sentinels participate in arithmetic silently (a `-999` poisons a mean plausibly); NaN propagates loudly and has dedicated handling (`nanmean`, `isna`).
**Q11.** `df.loc[5]` vs `df.iloc[5]` — the difference? → label vs position; after filtering/sorting they usually point at different rows.
**Q12.** What does `validate="m:1"` promise on a merge, and when does it raise? → right-side keys unique; raises when the right side would fan rows out — the silent-duplication guard.
**Q13.** When is `fillna(0)` corruption rather than cleaning? → when 0 is not the true meaning — a measurement invented (temperature 0°C) vs a confirmed default (no discount).
**Q14.** Why load branch codes as `category` dtype? → repeated short strings stored once as codes — smaller frames, faster groupbys, and typo'd categories surface.
**Q15.** `git commit` vs `git push` — what does each change? → commit writes a snapshot to *local* history; push publishes local commits to the remote. Nothing is shared until push.
**Q16.** Why do `data/` and `.venv/` belong in `.gitignore`? → Git versions definitions, not artefacts: data is large/regenerable/possibly sensitive, `.venv` is platform-specific and rebuildable from the lock.
**Q17.** What does a merge conflict actually mean, and who resolves it? → two branches changed the same lines; Git refuses to guess — the human who understands both intents composes the result and commits it.
**Q18.** A suite with 96% coverage missed the double-revenue bug. How? → coverage measures *execution*, not *verification*; no assert examined row counts across the merge.
**Q19.** When is regenerating a golden file legitimate? → deliberate, explained behaviour change — its own commit with the business rule in the message, never to silence a red.
**Q20.** `requirements.txt` vs `requirements.lock` — intent vs fact. Explain. → curated direct dependencies with bounds (what we mean) vs frozen exact snapshot including transitives (what actually ran); servers and teammates install the fact.

## Practical Assessments

The catalog's assessment components — **daily labs, coding assignments, mini-project** — are operationalised as:

**Daily labs (Labs 1–7, in-course).** Checked off via end-of-day checkpoint commits (Day 1: checkpoint zip, pre-Git). A lab is complete when its expected output reproduces and its checkpoint criteria are met; instructors sample two labs per participant per day for a 2-minute desk check.

**CA-1 — Coding assignment, issued end of Day 2 (take-home, ~90 min, reviewed next morning).** A new supplier ("Manafeth Wholesale") delivers a CSV variant: different header names, `dd/mm/yyyy` dates, cp1256 encoding, and rows replayed across files. Extend the ingestion layer to accept it — mapping table, parse-table extension, dedup by `(branch, sku, sold_at)` — with counted rejections and no changes to downstream code. Scored: correct handling of all four differences (50%), rejection accounting reconciles (25%), code hygiene — pathlib, narrow excepts, no hard-coded paths (25%).

**CA-2 — Coding assignment, issued end of Day 4 (take-home, ~90 min, reviewed next morning).** A provided 30-cell notebook computes weekly KPIs wrongly (one chained-assignment no-op, one unvalidated fan-out merge). Refactor its logic into two tested package functions, find and fix both bugs, and leave each fix guarded by a regression test. Scored: both bugs found with cause stated (40%), refactor quality (30%), tests that would catch recurrence (30%).

**Mini-project.** The Final Capstone Project above, assessed live on Day 5 Hour 5 against the 100-point rubric.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Daily labs (7 labs) | 30% | checkpoint commits/zips + expected outputs |
| Coding assignments (CA-1, CA-2) | 20% | submitted branches + next-morning review |
| Quiz (10 of 20, Day 5) | 10% | closed-book, 15 min |
| Mini-project (capstone) | 40% | rubric, repository-first |

**Core technical badge** requires ≥ 70 overall **and** mini-project ≥ 70 **and** no academic-integrity flags (identical quarantine counts, golden files, or DECISIONS.md across repos are checked — pairs collaborate on labs, but capstone repos are individual). The badge counts toward the **AI & Data Foundations Certificate** (SDA-FND-101→105) and is the prerequisite gate for all track-level technical modules.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Course org repo ready: checkpoint tags (`lab2-start` … `lab7-start`, solutions), all `sim-*` branches (`sim-object-dtype`, `sim-fanout`, `sim-idload`, `sim-uncounted`, `sim-two-pandas`), and the Day 1 checkpoint **zips** (no Git exists yet on Day 1)
- [ ] Regenerate datasets and golden files against the pinned pandas/NumPy versions: `pos_sample.csv`, `data/raw/` week files (incl. the cp1256 file and missing-branch day), `pos_month.parquet`, `weather_month.json` (with the duplicated Jeddah day), `expected_kpis.parquet`, and the **week-24 capstone set** with its four planted-dirt items + manifest
- [ ] Verify the weather stub (`course_tools.weather_stub`) on the venue network, including the scripted 503 storm and the capstone outage window
- [ ] Dry-run all seven labs end-to-end on a clean Windows machine **and** on the Codespaces/devcontainer fallback
- [ ] Create the classroom GitHub org; send invites; test one PR round-trip with a dummy account
- [ ] Confirm venue network allows pypi.org, github.com, and the stub's port (or configure the offline wheel mirror and pre-cloned repos)
- [ ] Print A4 posters: the which-python ritual, split-apply-combine, the branch→PR→review loop, the debugging loop (reproduce → localise → fix → test), and the capstone rubric
- [ ] Prepare the leaderboard (Lab 3 speedups, cold-rebuild times, zero-questions handovers) and the CA-1/CA-2 model solutions

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 from python.org — tick **"Add python.exe to PATH"**; on Windows, disable the Microsoft Store `python` app-execution aliases
- [ ] VS Code + Python and Jupyter extensions
- [ ] Git for Windows (or system git); configure `user.name` / `user.email`; create a GitHub account and note the username
- [ ] PowerShell execution policy: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (venv activation needs it)
- [ ] `pip install numpy pandas pyarrow requests jupyter pytest pytest-cov ruff`
- [ ] Download and run the pre-check: `python course_precheck.py` — prints ✓/✗ for interpreter, packages, git identity, and VS Code; reply to the email with a screenshot of the output

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Multiple Pythons on PATH (Store alias, old 3.8, Anaconda) — pip installs into one, code runs in another | High | The which-python ritual from Hour 1; VS Code interpreter picker; disable Store aliases |
| PowerShell blocks venv activation | High | Execution-policy line from the pre-course email; floater carries it on a card |
| True beginners overwhelmed on Day 1 | High | Pairing policy (experienced + beginner); checkpoint zips let anyone fast-forward; Lab 1a's scope is deliberately narrow |
| Arabic text as mojibake or `?` in outputs | Medium | `encoding="utf-8"` + `ensure_ascii=False` — both taught in M1/M2; check the terminal's code page (`chcp 65001`) |
| GitHub auth failures (password removed, PAT confusion) | Medium | Pre-create PATs in the Day 3 Hour 4 warm-up; SSH for those comfortable; floater handles stragglers during the lecture |
| Golden tests red on a fresh cohort machine | Medium | pandas/NumPy version drift — reinstall from the course lock; this *is* the Module 7 lesson, name it |
| Notebook imports stale code after edits | Medium | Restart kernel (autoreload optional); check `wafr_pipeline.__file__`; editable install from M7 |
| Merge-conflict panic in Lab 5b | Medium | It is scripted — the conflict is the exercise; walk one pair through composition on the projector, others follow |
| Slow venue Wi-Fi during `pip install` | Low | Offline wheel mirror from the prep checklist; stagger installs; venvs created once on Day 5, not daily |

## Timing Recommendations

- Protect **Lab 1a** and **Lab 4** at full length — first contact with Python and pandas selection semantics are the two overrun magnets; everything downstream assumes their outputs exist.
- Module 5 is split across Days 2–3 **by design** (local Git while the repo is small, collaboration once there is something to collaborate on). Do not consolidate it into one day; the overnight gap is when commits become habit.
- If a cohort is strong: pull fast-finisher items into main scope (channel mix in Lab 1, `--force-refresh` in Lab 2, price bands in Lab 4) and require two capstone extensions.
- If a cohort is weak: compress Module 3's matrix demo to instructor-led, trim Lab 6 task 5's extra coverage test — but never cut the golden-file governance discussion or the Lab 7 partner handover; they are the course's thesis made visible.
- Hard rule: week-24 data drops at Day 5 Hour 3 sharp, and demos start on time in Hour 5 — cut discussion, never build time. Collect repo URLs at end of Hour 4.

## Discussion Prompts (use during transitions)

1. "How many spreadsheets in your organisation are actually pipelines — re-built by hand every week by someone who cannot take leave?"
2. "Your report says SAR 6.2M and the finance system says SAR 6.4M. Walk me through *how you would find out which is wrong* — which habit from this week is that?"
3. "Rejected rows: cost of investigating each one vs cost of silently dropping it. Where should Wafr set that dial, and who decides?"
4. "What is the oldest analysis in your team that still *runs*? What made the difference — the author, or the practices?"
5. "On Monday you inherit a colleague's project. List the three artefacts you now know to look for first — and what their absence tells you."

## Wrap-up (final day, last 15 minutes)

- One slide: each capstone rubric criterion mapped to the module that taught it — the mini-project *is* the syllabus, assembled.
- Forward pointers: this badge unlocks **SDA-FND-104** (the recommended next step — it assumes exactly this Python/pandas/Git fluency) and the track gateways **SDA-AIE-111**, **SDA-AIE-113**, **SDA-DSC-111**, and **SDA-DSC-214**; with SDA-FND-101/102/104/105 it completes the **AI & Data Foundations Certificate**.
- The pipeline is theirs: encourage keeping `wafr-pipeline` public in their own account as the first portfolio artefact — track modules will expect a repo that looks like this.
- Collect: repository URLs (verified from Hour 4), quiz papers, DECISIONS.md files; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, NumPy ≥ 2.0, pandas ≥ 2.2, pytest ≥ 8. Regenerate datasets and golden files against the pinned course lock file before each delivery.*



