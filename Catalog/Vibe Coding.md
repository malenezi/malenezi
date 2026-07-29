# Vibe Coding
## البرمجة التوليدية

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Vibe Coding |
| **Arabic Title** | البرمجة التوليدية |
| **Code** | SDA-AIE-240 |
| **Track** | AI Engineering — هندسة الذكاء الاصطناعي |
| **Level** | Practitioner |
| **Duration** | 5 days × 5 learning hours = **25 hours** (intensive training camp) |
| **Audience** | Software engineers, backend and full-stack developers, technical leads, QA engineers moving into development, and government digital-services teams adopting AI coding assistants |
| **Prerequisites** | SDA-FND-110 (Prompt Engineering and Responsible AI Use) — recommended |
| **Entry Requirements** | Bachelor degree in Computer Science; familiarity with programming fundamentals and proficiency in at least one programming language; familiarity with Git basics and version-control systems |
| **Assessment** | Eight graded labs; two timed practical assessments; the **Rukhsa** end-to-end application capstone |
| **Stackability** | AI-assisted software engineering badge; anchors the AI Engineering practitioner path. Derived from the SDAIA Vibe Coding intensive camp. Next: SDA-AIE-305 (Developing Generative AI Solutions) |
| **Tools & Platforms** | Python 3.11 · FastAPI · PostgreSQL · SQLAlchemy · pytest · Playwright · Git/GitHub · GitHub Actions · an AI coding assistant (Claude Code / Copilot / Cursor) · ruff · mypy · bandit · Semgrep |

## Course Description

An intensive five-day training camp that equips participants to use generative AI to develop software applications efficiently and professionally. The camp integrates programme planning, code generation and optimisation, debugging, security-first review, automated testing, technical documentation, and version control into one continuous engineering workflow. The pedagogical thesis is stated on the first morning and returned to in every module: **AI-assisted development multiplies both velocity and defect rate; the engineering discipline — specification, review, testing, security, documentation, version control — is what converts that velocity into shipped software rather than into technical debt.** "Vibe coding" in its degenerate form — accepting a generated diff because it runs — is the anti-pattern this course exists to correct. Participants leave able to generate ten times faster *and* merge cleaner code than they did by hand, because they hold the assistant to a contract.

The course is built around a single evolving artefact: **"Rukhsa" (رخصة)**, a municipal commercial-licensing portal. A citizen submits a licence application with supporting documents; a validation service checks eligibility against municipal rules; an inspector queue routes the application for field inspection; fees are calculated in SAR and paid; and a licence certificate is issued with a QR verification endpoint. The stack is FastAPI + PostgreSQL + SQLAlchemy on the backend, a small React front end, pytest + Playwright for tests, and GitHub Actions for CI. Every lab produces a Rukhsa component that is **generated, reviewed, and hardened with AI assistance** — never generated and merged — so by Day 5 each participant owns a working, tested, documented, version-controlled application behind a five-gate CI pipeline. Because applicants are identified by Saudi national ID and upload personal documents, **Saudi PDPL (Personal Data Protection Law) is a first-class design constraint from Hour 1**, including an explicit governance rule on what may and may not be pasted into a third-party assistant.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Apply a review contract to AI-generated code and quantify the velocity/defect trade-off it controls
2. **LO2** — Employ generative AI in software planning: translate requirements into specifications, architecture, and a technical roadmap
3. **LO3** — Generate, refactor, and optimise code with AI assistance in line with clean-code, complexity, and resource-consumption best practices
4. **LO4** — Analyse and debug software efficiently using AI-driven root-cause analysis, profiling, and bisection
5. **LO5** — Apply a security-first principle in code review and gate OWASP-class defects in CI
6. **LO6** — Design and implement automated unit, integration, property-based, and end-to-end tests that provably assert behaviour
7. **LO7** — Generate and maintain technical documentation — docstrings, OpenAPI, ADRs, and a handover-grade README
8. **LO8** — Build and ship a complete application using a professional Git workflow and an automated quality pipeline

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Discipline and planning | M1: The Discipline of AI-Assisted Development · M2: Generative AI in Software Planning | 55% | 45% | Rukhsa repository skeleton, `CLAUDE.md` project instructions, `SPEC-001..003`, `ADR-0001..0003`, domain model + first Alembic migration |
| **Day 2** | Generation and optimisation | M3: Code Generation and Optimisation with AI | 35% | 65% | Applications + documents API and the eligibility validation service, generated and hardened; N+1 removed (1,840 ms → 96 ms p95) |
| **Day 3** | Debugging and security | M4: AI-Assisted Debugging and Root-Cause Analysis · M5: Code Review and the Security-First Principle | 40% | 60% | Fee-calculation race condition fixed (37 → 0 duplicate payments); security gate green (0 HIGH from bandit/Semgrep, 0 secrets, 0 phantom packages) |
| **Day 4** | Proof — tests and documentation | M6: Generating Automated Tests · M7: Automated Documentation and Maintainability | 35% | 65% | 118 tests (94 unit / 17 integration / 7 E2E), 88% line coverage, mutation score ≥ 70%; OpenAPI + README + ADR set passing the handover test |
| **Day 5** | Ship it | M8: Building the Complete Application and Professional Git Workflow · Capstone | 20% | 80% | Complete Rukhsa application on `main` behind a green five-gate pipeline (4 m 12 s), tagged `v1.0.0`, plus capstone demo |

## Hour-by-Hour Breakdown

### Day 1 — Discipline and Planning

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **The velocity/defect equation** + camp kickoff (M1) | State the course thesis; read the velocity vs defect-rate benchmark; meet the Rukhsa golden thread and the PDPL rule on third-party assistants | Interactive lecture + live "vibe coding" failure demo | 80/20 |
| 2 | **The review contract and context management** (M1) | SPEC → GENERATE → READ → TEST → HARDEN → COMMIT; project instruction files; why a large diff degrades output | Lecture + assistant-configuration walkthrough | 70/30 |
| 3 | **Lab 1 — Bootstrap Rukhsa under the contract** | Create the repo, write `CLAUDE.md`, generate the same endpoint with and without a spec, measure the difference | Guided lab (pairs) | 20/80 |
| 4 | **Requirements → architecture → roadmap** (M2) | Elicit requirements with AI; write a spec an assistant can implement; candidate architectures; ADRs | Lecture + spec-writing clinic | 65/35 |
| 5 | **Lab 2 — Specify and design Rukhsa** | Produce `SPEC-001..003`, three ADRs, the domain model and the first Alembic migration | Guided lab (pairs) | 15/85 |

### Day 2 — Generation and Optimisation

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Prompt patterns: greenfield vs refactor** (M3) | Two distinct prompt shapes; scoping a diff; the seven-pass critical diff read | Lecture + live generation | 70/30 |
| 2 | **Lab 3a — Generate the applications API** | Generate `POST /applications`, `GET /applications`, document upload; review the diff pass-by-pass; reject two defects | Guided lab | 15/85 |
| 3 | **Complexity and resource review of generated code** (M3) | Big-O review of a generated function; the N+1 pattern; memory and connection-pool consumption | Lecture + complexity clinic | 60/40 |
| 4 | **Lab 3b — Profile and optimise** | `cProfile` + `py-spy` on the list endpoint; find the N+1; fix with eager loading; re-benchmark | Guided lab | 10/90 |
| 5 | **Hallucinated APIs and generated dead ends** | Assistant-invented methods and packages; how to verify an API exists before you build on it | Micro-lecture + lab wrap | 40/60 |

### Day 3 — Debugging and Security

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **AI-assisted root-cause analysis** (M4) | Reproduce before you ask; how to feed a stack trace safely; differential diagnosis; when the assistant is confidently wrong | Lecture + live trace triage | 65/35 |
| 2 | **Lab 4 — The fee-calculation race** | Reproduce a concurrency defect, bisect to the introducing commit, fix with a row lock + unique constraint | Guided lab | 15/85 |
| 3 | **Security-first review** (M5) | OWASP Top 10 mapped to concretely generated snippets; the AI-diff review checklist | Lecture + vulnerability gallery | 60/40 |
| 4 | **Lab 5 — Harden the generated code** | Run bandit + Semgrep + gitleaks + pip-audit; fix six planted vulnerabilities; add the CI security job | Guided lab | 10/90 |
| 5 | **Supply chain and slopsquatting** | Hallucinated packages, typosquats, pinning with hashes, PDPL and third-party assistants | Micro-lecture + discussion | 45/55 |

### Day 4 — Proof: Tests and Documentation

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **The test pyramid and what AI tests badly** (M6) | Unit/integration/E2E proportions; tests that assert nothing; mocking the system under test | Lecture + bad-test gallery | 65/35 |
| 2 | **Lab 6a — Generate and strengthen the unit suite** | Generate tests for the fee engine, run mutation testing, raise the score from 41% to ≥ 70% | Guided lab | 10/90 |
| 3 | **Property-based and end-to-end testing** (M6) | Hypothesis for the fee invariants; Playwright for the licence-issuance journey | Lecture + live Playwright run | 55/45 |
| 4 | **Lab 6b + Lab 7 — E2E and documentation gate** | Seven Playwright scenarios; docstring coverage, OpenAPI export, README handover test | Guided lab | 10/90 |
| 5 | **Documentation that survives handover** (M7) | ADRs, runbook, changelog from conventional commits, diagrams-as-code | Micro-lecture + peer handover drill | 40/60 |

### Day 5 — Ship It

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Trunk-based development and the AI-change PR** (M8) | Conventional commits, short-lived branches, feature flags, the AI-specific PR checklist, CODEOWNERS | Lecture + PR walkthrough | 55/45 |
| 2 | **Lab 8 — Assemble Rukhsa and green the pipeline** | Wire issuance + QR verification, open a PR, pass all five CI gates, tag `v1.0.0` | Guided lab | 10/90 |
| 3 | **Capstone assembly** | Integrate all lab components; complete the Rukhsa checklist; peer review round | Project work | 0/100 |
| 4 | **Capstone assembly (continued) + peer PR review** | Each participant reviews one peer's PR against the AI-change checklist and files findings | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos; rubric-based scoring; path to SDA-AIE-305 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same Rukhsa licensing portal. Never introduce a throwaway toy example — always evolve Rukhsa. This is what makes the capstone achievable on Day 5 Hour 3; each lab is a capstone component, not a detour. When a participant asks "can I build my own idea instead?", the answer is no until the capstone extension.
- **Pace control:** Labs 3b (profiling), 4 (the race condition) and 6a (mutation testing) are the overrun-prone ones. Publish checkpoint tags (`lab1-start`, `lab1-solution`, `lab4-start`, …) in the course repository so stragglers can fast-forward with `git checkout lab4-start`. Never let a participant fall a lab behind — the capstone assumes every component exists.
- **Pairing:** rotate pairs each day and enforce a strict driver/navigator split where **the navigator reads the generated diff aloud before the driver accepts it**. This single ritual teaches the review contract faster than any slide. Pair a strong-security participant with a strong-testing participant on Day 3 and swap them on Day 4.
- **Environment strategy:** primary = local Python 3.11 + `docker compose` PostgreSQL 16 + Node 20 for Playwright and the React front end; fallback = GitHub Codespaces with the provided devcontainer. Verify both the week before delivery. Assistant access is the real risk: confirm the classroom's approved assistant (Claude Code, Copilot or Cursor) is licensed and reachable through the corporate proxy *before* Day 1 Hour 3, and have a "manual mode" lab variant ready if access fails.
- **Data and tooling discipline:** all Rukhsa applicant data in the labs is synthetic. Say so out loud on Day 1 and again on Day 3. The synthetic national IDs use the reserved `1`/`2` prefixes with a valid Luhn-style check digit so they look real to validation code but map to no citizen.
- **Language:** deliver in English or Arabic; keep all code, table names, column names, branch names, and commit messages in English — production convention in Saudi enterprise environments, because mixed-language identifiers break SQL tooling, `grep`-based operations and CI log parsing. Rukhsa's *user-facing* strings are bilingual (`business_name_ar` / `business_name_en`) and that bilinguality is itself a lab exercise.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 5 is deliberately build-heavy and light on new theory so the buffer can absorb capstone overrun.
- **Assessment logistics:** rubric scoring happens live during Day 5 Hour 5 demos. Collect repository URLs at the end of Hour 4 so CI runs, coverage reports and mutation scores can be verified from the Actions tab before demos begin — the pipeline is the evidence, the demo is the narration.
- **Governance framing:** treat Saudi PDPL as a first-class constraint from Day 1. Two rules are non-negotiable and must be stated in Hour 1, repeated in M5, and audited in the capstone: (1) **no personal data** — real national IDs, applicant names, uploaded documents — is ever pasted into a third-party assistant; (2) **no government source code** is pasted into an assistant that is not on the organisation's approved list with an appropriate data-processing agreement. Participants who normalise this on synthetic data will do it correctly on real data.

---

# Module 1 — The Discipline of AI-Assisted Development: Velocity, Defect Rate, and the Review Contract
## انضباط التطوير بمساعدة الذكاء الاصطناعي

## Module Overview

**Purpose.** This module states the thesis the whole camp defends. An AI coding assistant is a velocity multiplier and a defect multiplier at the same time; whichever one dominates is decided entirely by the engineering process wrapped around it. Participants leave with a concrete, repeatable **review contract** — six named steps — and with the habit of measuring their own output rather than trusting the feeling of speed. They also configure the assistant properly for the first time: a project instruction file, a bounded working context, and a diff-size budget.

**Business relevance.** Saudi organisations are adopting coding assistants at speed, and the early results are bimodal. Teams with a review discipline report genuine multi-fold throughput gains; teams without one report the same throughput gain followed by a defect wave, a security incident, or a codebase nobody can maintain six months later. Under Vision 2030 the government digital-services backlog is enormous and the pressure to ship is real — which makes the *discipline*, not the tool, the scarce competitive asset. This module gives a technical lead the numbers and the vocabulary to defend a review gate against a delivery manager who has just seen a demo.

**Industry use cases.**
- A government digital-services unit adopts an assistant across 40 engineers and needs an adoption policy that names what may be generated, what must be reviewed by a human, and what may never be pasted into a third-party model.
- A fintech measures defect-escape rate before and after introducing an AI-diff review checklist to decide whether the checklist earns its cost in review minutes.
- A software house inherits a client codebase built by "vibe coding" and must estimate the remediation cost — a task that requires knowing exactly which defect classes assistants produce.

**Expected competencies.** After this module a participant can state and apply the six-step review contract; configure a project instruction file that measurably improves generation quality; explain why large diffs degrade assistant output and keep changes inside a diff budget; quantify velocity against defect rate for their own work; and apply the PDPL rules on personal data and government source code in an assistant workflow.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | State the velocity/defect thesis and read a velocity-versus-defect-rate benchmark critically | LO1 |
| 1.2 | Apply the six-step review contract (SPEC → GENERATE → READ → TEST → HARDEN → COMMIT) to a real change | LO1 |
| 1.3 | Write a project instruction file that constrains an assistant to a codebase's conventions | LO1, LO2 |
| 1.4 | Explain context-window economics and keep a generated change inside a reviewable diff budget | LO1, LO3 |
| 1.5 | Apply PDPL and source-code governance rules when using a third-party coding assistant | LO1, LO5 |

## Technical Content

### 1. What "vibe coding" actually means, and why the term is a warning

The phrase entered the industry to describe a genuinely new mode of work: you describe an outcome in natural language, an assistant produces code, you run it, and if it works you move on. The productivity of that loop is real and it is large. The failure is also real and it is specific: **the loop has no step in which anyone establishes that the code is correct for reasons other than "it ran once."**

That is the entire problem. Traditional development had accidental review built into it. You typed every line, so you understood every line; you looked up the API, so you knew it existed; you thought about the error path, because you had to write it. Generation removes the typing and therefore removes the accidental understanding. Nothing is wrong with that — typing was never the value — but the understanding has to be *reintroduced deliberately*, as a review step, or it is simply gone.

So the course does not oppose vibe coding. It opposes vibe coding **with no contract**. The corrected form — specify, generate, read, test, harden, commit — is faster than hand-writing *and* cleaner than hand-writing. That is the claim, and the next section is the evidence.

### 2. The velocity/defect equation

The following benchmark is drawn from a controlled exercise run with practitioner cohorts on a task equivalent to Rukhsa's `POST /applications` endpoint: a validated create endpoint with a database write, a uniqueness rule and an error path. Participants repeat this measurement themselves in Lab 1, and their numbers should land within roughly ±25% of these.

| Mode | Median time to first passing endpoint | Defects per kLOC at merge | Defects escaping to production | Weekly rework hours |
|---|---|---|---|---|
| Hand-written, no assistant | 96 min | 4.2 | 1.1 | 3.5 |
| AI-generated, accepted unreviewed ("vibe coding") | 11 min | 11.4 | 8.7 | 14.2 |
| AI-generated under the review contract | 27 min | 1.9 | 0.3 | 2.4 |

Three readings matter, and you should draw all three out of the room rather than assert them. **The velocity gain is real** — 96 minutes to 27 is a 3.6× improvement nobody should give up. **The unreviewed mode is not faster, it is 8.7 defects per kLOC into production**; the 11-minute number measures typing, not delivery, and once the rework hours are added it is the slowest of the three modes over any horizon longer than a fortnight. **The contract is cheap** — sixteen extra minutes removes 96% of escaping defects, and sixteen minutes is roughly the cost of *one* incident triage call.

The equation to write on the board and leave there all week:

```
shipped_value  =  velocity  ×  (1 − defect_rate)  −  rework
```

An assistant raises `velocity` unconditionally. It raises `defect_rate` unconditionally too. Only the process moves `defect_rate` back down. This is the course thesis and every subsequent module is one term in this equation: M2 and M3 protect velocity, M4–M6 attack defect_rate, M7 and M8 attack rework.

### 3. The review contract

The contract is six steps. It is deliberately short enough to memorise and to say out loud to a pair partner.

| Step | What you do | What it costs | What it prevents |
|---|---|---|---|
| **SPEC** | Write the intent, the inputs, the outputs, the error cases and the acceptance criteria *before* prompting | 3–8 min | The assistant inventing requirements; scope drift; unverifiable output |
| **GENERATE** | Prompt with the spec, the relevant existing code, and an explicit diff budget | 1–3 min | Oversized, unreviewable changes |
| **READ** | Read the diff critically, pass by pass (M3 §3) — never "accept all" | 4–10 min | Hallucinated APIs, N+1 queries, injection strings, silent behaviour changes |
| **TEST** | Run the existing suite, then add the test the spec's acceptance criteria imply | 3–8 min | Regressions; tests that only mirror the generated implementation |
| **HARDEN** | Run lint, types, and the security tools; fix what they surface | 2–5 min | Secrets, injection, over-broad CORS, unpinned dependencies |
| **COMMIT** | A conventional commit describing the *intent*, with the spec ID referenced | 1 min | An unnavigable history; a change nobody can bisect or revert |

Two rules govern the contract:

- **You are the author.** Whatever the assistant produced, your name is on the commit and you answer for every line in review. "The AI wrote it" is not a defence and must never be accepted as one in this classroom — instructors should shut it down the first time they hear it, warmly and unmistakably.
- **The contract is non-negotiable in size, negotiable in depth.** On a 12-line change READ takes ninety seconds. On a 400-line change READ is the whole afternoon — which is exactly why the diff budget exists.

### 4. Context management: what the assistant knows, and what it degrades on

An assistant's output quality is a function of the context you give it. Three levers matter operationally.

**The project instruction file.** Every serious assistant supports a repository-level instruction file (`CLAUDE.md`, `.github/copilot-instructions.md`, `.cursorrules`). This is the single highest-leverage artefact in an AI-assisted codebase, because it is applied to every generation without being re-typed. It should contain the things the assistant cannot infer and gets wrong by default:

| Include | Why | Rukhsa example |
|---|---|---|
| Stack and pinned versions | Prevents generation against the wrong major version | "FastAPI 0.115, SQLAlchemy 2.0 **declarative + Mapped[] style**, Pydantic v2" |
| Layering rules | Prevents business logic leaking into routers | "Routers call services; services own transactions; models never import routers" |
| Naming and language convention | Prevents mixed-language identifiers | "All identifiers, table names and commit messages in English; user-facing strings bilingual via `*_ar`/`*_en` columns" |
| Forbidden patterns | Pre-empts the assistant's favourite defects | "Never use raw f-string SQL. Never set `allow_origins=['*']`. Never read secrets with a literal default." |
| Test expectations | Makes the assistant produce tests you want | "Every new service function gets a unit test with at least one boundary case and one failure case" |
| Data-handling rules | PDPL enforcement at generation time | "`national_id` is personal data: never log it, never place it in a URL path, always store hashed" |

**Diff budget.** Assistant output quality and *human* review quality both fall as the diff grows, and they fall for different reasons. The assistant loses coherence because the change no longer fits comfortably in its working attention alongside the code it must remain consistent with; the reviewer loses attention because reading 400 unfamiliar lines is genuinely hard. The observed effect on cohorts:

| Generated diff size | Reviewer defect-detection rate | Median review time | Verdict |
|---|---|---|---|
| ≤ 50 lines | 84% | 4 min | Target |
| 51–150 lines | 71% | 11 min | Acceptable |
| 151–400 lines | 48% | 26 min | Split it |
| > 400 lines | 22% | "approved" in 6 min | Rubber-stamp — this is where defects enter |

The last row is the important one and it is not a joke: past a certain size, review time goes *down*, because reviewers give up. **Set a 150-line budget per generated change and split anything larger into staged prompts.** Rukhsa is built in roughly 40 such changes across the week.

**Context hygiene.** Give the assistant the two or three files the change actually touches plus the instruction file — not the whole repository. Irrelevant context dilutes attention and invites "helpful" edits to code you did not ask about. Heuristic: if you cannot name why a file is in context, take it out.

### 5. Governance: PDPL and what never leaves your machine

Rukhsa handles Saudi national IDs, applicant names, lease contracts and civil-defence certificates. Under the Saudi Personal Data Protection Law these are personal data, and some are sensitive. Two rules apply from Hour 1 and are audited in the capstone:

1. **Never paste personal data into a third-party assistant.** Not a real national ID, not a real applicant name, not the contents of an uploaded document, not a production database row, not a log line containing any of them. When you need the assistant to reason about a record, hand it a *synthetic* record with the same shape. This course ships a synthetic generator precisely so the habit is formed on safe data.
2. **Never paste government or client source code into an unapproved assistant.** Source code for a government system is frequently classified as confidential by contract and by policy. Use the organisation's approved, contracted assistant with a data-processing agreement, and confirm whether the vendor trains on submitted content. If the answer is unclear, the answer is no.

Operationally: maintain an approved-assistant list, disable "improve the product" telemetry in the IDE plug-in, and add a pre-commit secret scan (M5). PDPL also constrains the *system you are building*, not only how you build it — Rukhsa's own logging, retention and access rules are designed against it in M2 and enforced in M5.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Specification precedes generation.* If you cannot describe what "correct" means, you cannot review what you get. The spec is the acceptance criterion.
- *The diff is the unit of trust, not the prompt.* Nobody merges a prompt. Read what actually changed.
- *Measure your own output.* Perceived velocity is not velocity. Count merged changes and escaped defects, not accepted suggestions.
- *Small, staged changes beat one large generation* — for the assistant, for the reviewer, and for `git bisect` later.
- *Governance is a design input, not a compliance review.* PDPL rules go into the instruction file so they shape generation itself.

**Common mistakes (each appears in the Lab 1 starter deliberately)**
1. Prompting from a vague one-liner ("build the applications endpoint") and accepting whatever requirements the assistant invents — including an `is_admin` boolean nobody asked for.
2. Accepting a 380-line generated diff in a single review because the tests were green — the tests were also generated, from the same misunderstanding.
3. No project instruction file, so every generation re-invents the layering, the naming and the SQLAlchemy style; the codebase becomes three codebases.
4. A hardcoded secret in generated configuration (`SECRET_KEY = "changeme-in-prod"`) that survives to `main` because nobody read past the interesting part of the diff.
5. Pasting a production log line containing a real national ID into the assistant while debugging — a PDPL breach committed in the name of speed.

**Production considerations**
- Track two metrics from day one of adoption: **change failure rate** and **median PR review time**. If the first rises while the second falls, your team has stopped reviewing and you have three months before you find out the expensive way.
- Put the instruction file under CODEOWNERS review. It is executable policy; a careless edit to it changes the output of every future generation.
- Decide and document who is accountable for a generated change *before* the first incident, not during it. In every serious organisation the answer is the committing engineer.

### 7. Real-world example walkthrough

Narrate this (5 minutes, no slides). A Riyadh product team adopted an assistant and their sprint throughput rose from 23 to 61 story points in two sprints. Everyone celebrated. In sprint four, an outage: the customer-facing search endpoint had been generated with a query built by string concatenation, and a crafted search term dropped a table on a read replica. The post-mortem found the change had been merged as part of a 612-line PR approved in four minutes with the comment "LGTM, tests pass" — and the tests had been generated in the same session from the same misunderstanding, so they asserted the buggy behaviour faithfully. The team did not roll back the assistant; that would have been the wrong lesson. They introduced three rules: a 150-line diff budget, a mandatory human READ pass recorded in the PR, and a SAST gate in CI. Throughput settled at 52 points — still 2.3× the pre-assistant baseline — and change failure rate fell below where it had been *before* adoption. That is the shape of this entire course, and Rukhsa is where participants live it.

## Code Examples

### The project instruction file that governs every generation

```markdown
# CLAUDE.md
<!-- Repository-level instructions for any AI coding assistant working on Rukhsa.
     WHY: these are the facts an assistant cannot infer from a partial view of the
     codebase and gets wrong by default. Editing this file changes the output of
     every future generation, so it is CODEOWNERS-protected. -->

## Project
Rukhsa (رخصة) — municipal commercial-licensing portal. Citizens apply for a
commercial licence; the service validates eligibility, routes an inspection,
calculates fees in SAR, takes payment, and issues a certificate with a QR
verification endpoint.

## Stack (pinned — do not generate against other major versions)
- Python 3.11, FastAPI 0.115, Pydantic v2, SQLAlchemy 2.0 (`Mapped[]` declarative
  style ONLY — never the legacy `Column()` style), Alembic 1.13, PostgreSQL 16
- pytest 8.x, Hypothesis 6.x, Playwright 1.4x, ruff, mypy --strict, bandit, Semgrep

## Architecture rules
- Layering: `api/` routers -> `services/` business logic -> `repositories/` data
  access -> `models/` ORM. A router NEVER contains business logic or a query.
- Transactions are owned by the service layer, never by a router or a repository.
- All money is `Decimal` with `Numeric(12, 2)` in the database. NEVER float.
- All timestamps are timezone-aware UTC (`DateTime(timezone=True)`).

## Naming and language
- Every identifier, table name, column name, branch name and commit message is in
  English. User-facing content is bilingual through paired columns:
  `business_name_ar` / `business_name_en`.
- Commits follow Conventional Commits and reference a spec: `feat(fees): ... (SPEC-004)`

## Forbidden patterns (reject the generation if it produces these)
- Raw SQL built with f-strings or `%` formatting. Use bound parameters.
- `allow_origins=["*"]` on CORSMiddleware.
- Secrets with literal defaults, e.g. `os.getenv("SECRET_KEY", "dev")`.
- `except Exception: pass`, or any handler that swallows without logging.
- Lazy-loaded relationships inside a loop (N+1). Use `selectinload`.

## Data protection (Saudi PDPL — non-negotiable)
- `national_id` is personal data. Store it hashed (`sha256` + application salt),
  never log it, never place it in a URL path or a query string.
- Uploaded documents are referenced by object key only; never inline their bytes
  into a log, an error message or an API response.
- Any new column holding personal data must be added to `docs/DATA_INVENTORY.md`
  in the same change.

## Testing expectations
- Every new service function gets unit tests covering the happy path, at least one
  boundary case, and at least one failure case with an asserted exception type.
- Never assert only `is not None`. Assert the value.

## Change size
Keep any single generated change under 150 changed lines. If the request is
larger, propose a staged plan and generate the first stage only.
```

### Configuration done wrong by the assistant, and done right

```python
# app/rukhsa/core/config.py
"""Application settings for Rukhsa.

WHY this file exists: configuration is the single most common place where an
assistant produces something that runs perfectly in the lab and leaks a
credential in production. Centralising it means there is exactly one place to
review, and one place for the security gate (M5) to watch.
"""

# ❌ AI-GENERATED — DO NOT SHIP.
# Defect 1: a literal fallback secret. The application boots in production with a
#   publicly known signing key, so anyone can forge a session token.
# Defect 2: the database URL embeds a password and defaults to a real-looking host.
# Defect 3: DEBUG defaults to True, exposing tracebacks (and query fragments
#   containing personal data) to end users.
#
# class Settings:
#     SECRET_KEY = os.getenv("SECRET_KEY", "changeme-in-prod")
#     DATABASE_URL = os.getenv("DATABASE_URL",
#                              "postgresql://rukhsa:rukhsa123@db.rukhsa.gov.sa/rukhsa")
#     DEBUG = os.getenv("DEBUG", "True") == "True"

from functools import lru_cache

from pydantic import Field, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated settings. Missing required values fail fast at import time.

    Failing at boot is the point: a misconfigured deployment must not start and
    silently serve traffic with an insecure default.
    """

    model_config = SettingsConfigDict(
        env_file=".env",           # local development only; never committed
        env_prefix="RUKHSA_",
        extra="forbid",            # an unknown env var is a typo, not a feature
    )

    # No default -> pydantic raises ValidationError if the variable is absent.
    secret_key: SecretStr = Field(..., min_length=32)
    database_url: PostgresDsn = Field(...)

    # Safe defaults: the *secure* value is the one you get by doing nothing.
    debug: bool = False
    national_id_salt: SecretStr = Field(..., min_length=16)
    cors_allowed_origins: list[str] = Field(default_factory=list)
    fee_service_fee_rate: float = 0.05      # 5% municipal service fee, SPEC-004


@lru_cache
def get_settings() -> Settings:
    """Cached accessor so settings are validated exactly once per process."""
    return Settings()  # type: ignore[call-arg]  # values come from the environment
```

## Hands-on Lab 1 — Bootstrap Rukhsa Under the Review Contract

| | |
|---|---|
| **Objective** | Create the Rukhsa repository, author the `CLAUDE.md` project instruction file, then generate the same endpoint twice — once from a one-line prompt, once under the review contract — and measure the difference in defects, diff size and review time |
| **Duration** | 50 minutes |
| **Setup** | Python 3.11, Docker Desktop, Git, an approved AI assistant configured in the IDE, `docker compose up -d db` (PostgreSQL 16), course repo cloned, `git checkout lab1-start` |

**Instructions & tasks**

1. *(6 min)* Run `make doctor` to verify Python 3.11, PostgreSQL 16 reachable on 5432, the assistant plug-in authenticated, and `ruff`/`mypy`/`bandit` on PATH. Fix anything red before continuing — this environment carries the whole week.
2. *(8 min)* **Uncontracted generation.** In a scratch branch `lab1-vibe`, prompt your assistant with exactly: *"add an endpoint to create a licence application"*. Accept whatever it produces without editing. Record: diff size, wall-clock time, and how many requirements it invented that you never asked for.
3. *(10 min)* Author `CLAUDE.md` from the template in the Code Examples section. Add at least two forbidden patterns and one PDPL rule of your own beyond the template — you must be able to justify each in the debrief.
4. *(14 min)* **Contracted generation.** On branch `lab1-spec`, first write a six-line spec for the same endpoint (`docs/specs/SPEC-001-create-application.md`: intent, request shape, response shape, two error cases, acceptance criteria). Then generate with the spec and `CLAUDE.md` in context, READ the diff line by line, and fix everything you reject. Time each contract step separately.
5. *(7 min)* Fill `LAB1_METRICS.md` comparing the two branches: lines changed, review time, defects you can name in each, and requirements invented. Run `python scripts/diff_budget.py --limit 150` on both — note which one passes.
6. *(5 min)* Commit on `lab1-spec`: `feat(applications): create-application endpoint under review contract (SPEC-001)`.

**Expected output**
```
$ make doctor
✓ python 3.11.9        ✓ postgres 16 @ localhost:5432
✓ assistant: claude-code (authenticated)
✓ ruff 0.6.9  ✓ mypy 1.11.2  ✓ bandit 1.7.9  ✓ pytest 8.3.3

$ git diff --stat lab1-vibe
 app/rukhsa/api/applications.py | 214 ++++++++++++++++++
 app/rukhsa/models.py           | 166 +++++++++++++
 2 files changed, 380 insertions(+)
$ python scripts/diff_budget.py --limit 150
✗ diff budget exceeded: 380 reviewable lines (limit 150).

$ git diff --stat lab1-spec
 app/rukhsa/api/applications.py     |  61 ++++++
 app/rukhsa/schemas/application.py  |  38 +++++
 app/rukhsa/services/application.py |  44 +++++
 3 files changed, 143 insertions(+)
$ python scripts/diff_budget.py --limit 150
✓ diff budget ok: 143/150 reviewable lines
```

**Acceptance criteria**
- `CLAUDE.md` exists, is committed, and contains stack pins, layering rules, ≥ 2 additional forbidden patterns and ≥ 1 PDPL rule.
- `docs/specs/SPEC-001-create-application.md` states intent, request, response, two error cases and acceptance criteria.
- `LAB1_METRICS.md` names at least three concrete defects in the uncontracted branch (invented fields, oversized diff, missing error path are all acceptable).
- The contracted branch passes the diff budget; the uncontracted branch does not.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `make doctor` reports the assistant unauthenticated | Corporate proxy blocks the plug-in endpoint | Configure `HTTPS_PROXY` in the IDE; fall back to the browser-based assistant and paste diffs manually |
| Assistant ignores `CLAUDE.md` | File not at repository root, or the IDE session started before it existed | Move to root; restart the assistant session so the file is picked up |
| `psycopg` connection refused | Container not up, or port 5432 already in use locally | `docker compose up -d db`; if a local Postgres owns 5432, remap to 5433 and update `RUKHSA_DATABASE_URL` |
| Uncontracted branch produced a *small* diff | The assistant guessed a minimal shape this time | Keep the run — this is the real lesson: variance is the defect. Note what it silently omitted (validation, error path) |

**Instructor notes.** The comparison in step 2 vs step 4 is the entire module made visible; protect its time even if `make doctor` runs long. Walk the room during step 2 and note who is *already* editing the uncontracted output — stop them, gently: the point of the branch is to see what unreviewed generation actually looks like. Expect the uncontracted branch to invent an `is_admin` flag, a `status` field with an undocumented value set, and no `409` path for a duplicate reference. Fast finishers: have them add the `diff_budget.py` script as a `pre-commit` hook and demonstrate it blocking a deliberately oversized staged change.

## Mini Exercises

**Quiz (5 questions)**
1. Name the six steps of the review contract in order. → SPEC, GENERATE, READ, TEST, HARDEN, COMMIT.
2. Why does reviewer defect-detection *and* review time both fall on very large diffs? → reviewers disengage and rubber-stamp; detection drops to ~22%.
3. What is the highest-leverage single artefact in an AI-assisted repository, and why? → the project instruction file — it constrains every future generation without being re-typed.
4. Under PDPL, may you paste a production log line containing a national ID into a third-party assistant to debug it? → **No**; redact or use a synthetic equivalent.
5. In `shipped_value = velocity × (1 − defect_rate) − rework`, which term does an assistant *not* improve on its own? → `defect_rate` (it worsens it); only process moves it down.

**Debugging exercise.** Check out branch `lab1-hardcoded-secret`, where the generated `config.py` uses `os.getenv("SECRET_KEY", "changeme-in-prod")`. The application boots and all tests pass. Ask participants to explain precisely why the tests passing is *evidence of nothing* here, and to write the one-line assertion that would have caught it (`Settings` must raise when the variable is absent).

**Design exercise.** Draft the ten-line "AI assistant usage policy" you would attach to Rukhsa's repository README for a 25-engineer government unit. It must name: approved tools, what may never be pasted, who is accountable for a generated change, and the diff budget.

**Discussion questions.**
- Your delivery manager has seen the 11-minute number and wants the review gate removed for "simple changes." What evidence do you bring, and where is the honest boundary of "simple"?
- If the assistant wrote 80% of the lines, is the engineer's name on the commit dishonest — or is authorship now about the specification and the review rather than the typing?

## Case Study — Adoption Without a Contract at "Bunyan" (بنيان) Software House

**Scenario.** "Bunyan" (بنيان), a 90-engineer Riyadh software house building line-of-business systems for Saudi ministries and semi-government entities, rolled out an AI coding assistant to all delivery teams in a single quarter with no accompanying process change. Story-point throughput rose 2.7× in six weeks and leadership publicised the result. In the following quarter, client-reported defects rose 3.1×, two projects breached their warranty clauses, and a security assessment on a delivered portal found a SQL-injection defect and an over-broad CORS policy that had both entered through generated code.

**Business context.** Bunyan's contracts carry a 12-month warranty with penalty clauses; remediation is unbilled. The finance team calculated that the defect wave consumed SAR 2.1M of unbilled engineering — considerably more than the throughput gain had earned. Worse, a client's security review put Bunyan's pre-qualification for government tenders at risk, which is an existential rather than a financial problem.

**Technical challenge.** Bunyan has no per-team data on *where* the defects entered, because PRs are large (median 480 changed lines) and approvals are fast (median 5 minutes). The engineering director must design an intervention that recovers quality without discarding the throughput gain, and must be able to prove the intervention worked within one quarter.

**Constraints.** Cannot pause delivery on 14 active client projects. Cannot ban the assistant — engineers would (and did, in a pilot) revert to using it invisibly through personal accounts, which is a far worse governance outcome. Some client contracts prohibit source code leaving the client's approved tooling perimeter entirely. Any measurement must come from tooling the teams already have (GitHub + Jira), not a new reporting burden.

**Solution approach (facilitate, don't lecture).** Steer the room toward: (1) instrument first — change failure rate and PR size/review-time distributions from the existing GitHub data, giving a baseline before any intervention; (2) introduce a diff budget and split large PRs, which raises detection without adding process ceremony; (3) publish a per-repository instruction file encoding each client's stack and conventions, so generation stops fighting the codebase; (4) add a SAST + secret-scan gate in CI so the two vulnerability classes that caused the security finding cannot recur silently; (5) make the READ pass visible — a PR template checkbox with the reviewer naming one thing they changed or questioned; (6) for the perimeter-restricted clients, an on-premise or approved-vendor assistant, and where that is impossible, a documented manual mode. Then re-measure after one quarter against the baseline.

**Discussion questions.**
1. Bunyan's throughput gain was real and its defect wave was real. Which of the two should the engineering director report first to the board, and why does the ordering matter politically?
2. The pilot ban drove assistant use underground. What does that tell you about the difference between a policy and a control, and which of the six interventions above are actually controls?
3. Median PR review time of five minutes on 480 lines is the diagnostic signal here. What would you expect the number to become after the diff budget, and what would it mean if review time *did not* rise?
4. One client's contract forbids source code leaving their perimeter. Does that forbid the assistant, or forbid a particular deployment of it — and who at Bunyan is competent to answer that question?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Project instruction file present and enforced | Discipline | `CLAUDE.md` committed, ≥ 6 sections | file review |
| Contracted diff size | Reviewability | ≤ 150 reviewable lines | `scripts/diff_budget.py` |
| Requirements invented by the assistant | Specification quality | 0 in the contracted branch | spec-vs-diff comparison |
| Defects identified in the uncontracted branch | Review skill | ≥ 3 named in `LAB1_METRICS.md` | instructor review |
| Time-to-endpoint under contract | Velocity | ≤ 30 min | lab timing |

**Example benchmark table (filled during lab):**

| Branch | Mode | Diff lines | Wall-clock | Defects named | Invented requirements | Budget |
|---|---|---|---|---|---|---|
| `lab1-vibe` | Uncontracted | 380 | 11 min | 5 | 3 (`is_admin`, undocumented `status` set, soft-delete) | ✗ fail |
| `lab1-spec` | Review contract | 143 | 27 min | 0 remaining | 0 | ✓ pass |

## Required Visuals and Training Assets

### Diagrams
1. **The velocity/defect scissors** — *Purpose:* the anchor image of the whole camp. *Elements:* two curves against "assistant adoption" on the x-axis — velocity rising, defect rate rising with it; a third dashed curve showing defect rate pulled back down by the review contract, with the gap shaded as "shipped value". *Style:* flat vector, two-colour, English labels with Arabic subtitles. *Designer description:* "Two diverging lines opening like scissors; a dashed line closes them again, labelled 'the contract'."
2. **The six-step review contract loop** — *Purpose:* the mnemonic participants use all week. *Elements:* SPEC → GENERATE → READ → TEST → HARDEN → COMMIT arranged as a cycle, each step annotated with its typical minute cost and the defect class it prevents. *Style:* circular flow, one accent colour per step, reused as a slide footer in every module.
3. **Diff size versus detection rate** — *Purpose:* justify the 150-line budget with evidence. *Elements:* bar chart of detection rate (84/71/48/22%) with an overlaid line for review time showing the collapse past 400 lines. *Style:* clean chart, the > 400 bar in warning red.
4. **Rukhsa system context (Day 1 version)** — *Purpose:* introduce the golden thread. *Elements:* citizen → portal → application service → validation → inspector queue → fees/payment → licence + QR verify; PDPL-sensitive stores marked with a shield icon. *Style:* boxes-and-arrows context diagram, reused and elaborated in every module.

### Images (screenshots)
1. **An IDE session showing `CLAUDE.md` being applied** — *why:* participants must recognise when the instruction file is actually in context; *content:* the assistant panel listing the loaded instruction file before generating.
2. **A 612-line pull request approved in four minutes** — *why:* the case-study anti-pattern made concrete; *content:* GitHub PR header with the diff stat and the approval timestamp visible.
3. **`diff_budget.py` blocking a commit** — *why:* the budget as a control, not a suggestion; *content:* terminal showing the pre-commit hook failure.

### Simulations
1. **The invented-requirement drill** — *Setup:* every participant prompts the same vague one-liner and pastes the resulting field list into a shared board. *Expected behaviour:* the boards disagree — thirty engineers get thirty different schemas. *Learning objective:* an unspecified prompt does not have a correct answer, so it cannot have a correct review.
2. **The rubber-stamp experiment** — *Setup:* two branches, one 90-line and one 520-line, each containing exactly two planted defects; teams get four minutes on each. *Expected behaviour:* most teams find both defects in the small diff and neither in the large one. *Learning objective:* review capacity is a hard limit, not an attitude.

### Interactive Activities
- **Contract card-sort (15 min):** twelve engineering actions (write acceptance criteria, run mypy, rename a variable, run bandit, tag a release…) sorted onto the six contract steps; the arguments about the ambiguous cards are the value.
- **Instruction-file clinic (12 min):** teams draft three "forbidden patterns" for a codebase they actually work on, then trade lists and challenge each other to justify them from a real incident.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `data/seed/applicants.json` | Synthetic generator (Faker `ar_SA` + reserved-prefix national IDs with valid check digits) | JSON | 500 records | Safe stand-in for personal data; used in every lab |
| `data/seed/activities.csv` | ISIC-derived municipal activity codes with SAR base fees | CSV | 148 rows | Fee and eligibility rules from M2 onward |
| `benchmarks/velocity_defect.csv` | Anonymised cohort measurements | CSV | 3 rows | The Module 1 benchmark table participants reproduce |

### Demo Requirements
- **Instructor demo (8 minutes):** live-generate the create-application endpoint from a one-line prompt on the projector, accept it without reading, run the test suite green — then open the diff and find the hardcoded secret and the missing duplicate-reference path in front of the room. Do not soften it; the discomfort of "the tests passed and it was still wrong" is the memory the whole week is built on.

---

# Module 2 — Generative AI in Software Planning: Requirements → Architecture → Technical Roadmap
## الذكاء الاصطناعي التوليدي في التخطيط البرمجي

## Module Overview

**Purpose.** This module covers catalogue module 1 and delivers the first half of the review contract: the **SPEC** step. Participants learn to use an assistant where it is genuinely strongest — as a fast, tireless analyst that expands a vague requirement into candidate structures, edge cases and architectural options — while keeping the *decision* firmly human. The output is a set of artefacts an assistant can implement against: numbered specifications with acceptance criteria, architecture decision records, a domain model, and a sequenced technical roadmap.

**Business relevance.** The most expensive defects in a government digital service are never syntax errors; they are requirement errors discovered after launch. A licensing portal that computes fees against the wrong activity taxonomy, or that fails to model the "application returned for correction" state, costs a rebuild. An assistant used well shortens the requirements-to-design loop from days to hours and surfaces edge cases a workshop would have missed — but only if someone writes down what was decided. Specifications and ADRs are what make AI-assisted development auditable, which is exactly what a Saudi public-sector delivery assurance review will ask for.

**Industry use cases.**
- A ministry's digital unit converts a 40-page Arabic policy document into a structured requirements backlog with traceability from each regulation clause to a system rule.
- An architecture team generates three candidate designs for an event-driven integration and uses an ADR to record why the simplest one was chosen, so the decision survives the architect's departure.
- A delivery lead turns an approved specification into a dependency-ordered roadmap of 150-line changes that a team of five can parallelise without merge conflicts.

**Expected competencies.** After this module a participant can run an AI-assisted requirements elicitation that produces testable acceptance criteria; write a specification precise enough that two different engineers generate compatible implementations from it; produce and defend an architecture decision record; model a domain in SQLAlchemy 2.0 with a reviewed migration; and sequence work into a roadmap of reviewable increments.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Elicit and structure requirements with AI assistance, producing testable acceptance criteria | LO2 |
| 2.2 | Write a specification an assistant can implement against, with explicit non-goals and error cases | LO2, LO1 |
| 2.3 | Generate and evaluate candidate architectures, then record the decision in an ADR | LO2, LO7 |
| 2.4 | Translate a specification into a domain model, ORM mappings and a reviewed migration | LO2, LO3 |
| 2.5 | Sequence a technical roadmap into dependency-ordered, reviewable increments | LO2, LO8 |

## Technical Content

### 1. Requirements elicitation with an assistant: expand, then decide

Assistants are excellent at *divergence* and unreliable at *convergence*. Use them accordingly. The productive pattern is three moves:

1. **Expand.** Give the assistant the raw requirement and ask for the state machine, actors, failure modes and the questions a domain expert would ask. For "a citizen applies for a commercial licence" it will surface states you did not think of — `returned_for_correction`, `withdrawn`, `expired_before_payment` — and questions such as "can an application be submitted for a business that already holds an active licence at the same address?"
2. **Interrogate.** Take the expansion to the domain expert, not to the code. The list is a *checklist for a human conversation*, never an answer. Only a municipality can tell you that a returned application retains its reference and its paid fee for 30 days.
3. **Converge.** Write the decision down as a Given/When/Then acceptance criterion. That is the artefact; the chat transcript is not.

The failure mode to name explicitly: **an assistant will confidently invent domain rules**. Asked about Saudi municipal licensing it will produce plausible-sounding fee bands and validity periods that are simply fabricated. Treat every domain fact it emits as a *hypothesis to verify against a source*, and mark unverified ones in the spec with `[UNVERIFIED]` so they cannot silently become code.

### 2. Anatomy of a specification an assistant can implement

A specification for AI-assisted development is not a requirements document for humans. It is closer to a test plan with prose. It must be complete enough that a reviewer can judge the generated diff against it without asking the author a question.

| Section | Content | Why the assistant needs it |
|---|---|---|
| **ID and title** | `SPEC-004 — Fee calculation` | Referenced in the commit and the PR; makes the change traceable |
| **Intent** | One sentence: what capability this adds and for whom | Anchors generation; prevents scope drift |
| **Non-goals** | What this change explicitly does *not* do | The single most effective way to stop an assistant inventing features |
| **Inputs** | Types, units, ranges, nullability | Prevents wrong types (float money, naive datetimes) |
| **Outputs** | Exact response shape and status codes | Prevents an invented response envelope |
| **Rules** | Numbered, individually testable business rules | Each becomes a test; each becomes a review checkpoint |
| **Error cases** | Condition → status → error code | The part assistants omit most often |
| **Acceptance criteria** | Given/When/Then, with concrete values | Becomes the test suite verbatim |
| **Data protection** | Which fields are personal data and how they are handled | Makes PDPL a generation-time constraint |

Concrete values matter more than they look. "Fees are calculated from activity and area" generates something; "a food-and-beverage activity (ISIC 56xx) of 180 m² in Riyadh yields SAR 3,780" generates something *checkable*, and produces a test that fails when the rounding is wrong.

### 3. Rukhsa's domain, decided in this module

The specification set produced in Lab 2 fixes the domain for the rest of the week. The core entities and the one-line reason each exists:

| Entity | Grain | Key fields | Why it is separate |
|---|---|---|---|
| `applications` | One licence application | `reference` (RKH-2026-000123), `national_id_hash`, `business_name_ar/en`, `activity_code`, `city`, `area_sqm`, `status` | The aggregate root; every other entity hangs off it |
| `documents` | One uploaded supporting file | `application_id`, `doc_type`, `object_key`, `sha256`, `uploaded_at` | Files are stored by key, never inline; the hash proves integrity |
| `eligibility_checks` | One rule evaluation of one application | `application_id`, `rule_code`, `passed`, `detail` | An auditable record of *why* an application was rejected |
| `inspections` | One field inspection assignment | `application_id`, `inspector_id`, `scheduled_for`, `outcome` | The queue is a first-class workflow, not a status flag |
| `fee_assessments` | One priced assessment of one application | `application_id`, `base_fee`, `area_surcharge`, `service_fee`, `total`, `assessed_at` | Immutable pricing history — a re-assessment creates a row, never an update |
| `payments` | One payment attempt | `fee_assessment_id`, `sadad_reference`, `amount`, `status` | Money needs its own idempotency key and audit trail |
| `licences` | One issued licence | `application_id`, `licence_number`, `issued_at`, `expires_at`, `qr_token` | The output artefact; verified publicly by `qr_token` |

The application state machine, decided here and enforced from M3 onward:

```
draft ──submit──► submitted ──validate──► eligible ──assess──► awaiting_payment
                     │                        │                      │
                     │                   (fails rules)             (paid)
                     ▼                        ▼                      ▼
             returned_for_correction      rejected           awaiting_inspection
                     │                                               │
                  (resubmit)                                    (pass / fail)
                     └──────────────────────────────────►  issued  /  rejected
```

Two rules that will be tested all week: **status transitions are explicit and validated** (no endpoint sets `status` to an arbitrary string), and **`fee_assessments` and `payments` are append-only** — the M4 race condition exists precisely because the first generated implementation violated the second rule.

### 4. Architecture decision records

An ADR is a short, immutable document recording one decision, its context, the options considered and the consequences. It exists because in an AI-assisted codebase the *code no longer carries the reasoning*: when an assistant generates a caching layer in ninety seconds, nothing records why caching beat a materialised view, and six months later the only honest answer is "I don't know, it was generated."

Rukhsa's Day-1 ADR set:

| ADR | Decision | Rejected alternative | Consequence to live with |
|---|---|---|---|
| `0001` | PostgreSQL 16 as the single datastore | MongoDB; a separate document store for uploads | Relational integrity and row locks available (needed in M4); object storage still required for file bytes |
| `0002` | Synchronous FastAPI + SQLAlchemy 2.0 with a session-per-request | Fully async SQLAlchemy | Simpler transactions and easier debugging; must watch pool sizing under load (M3) |
| `0003` | Fees stored as `Numeric(12, 2)` and computed with `Decimal`, never float | Store minor units as integers | Readable SQL and exact arithmetic; every code path must avoid float coercion — enforced by a Semgrep rule in M5 |

The MADR-style format used here is deliberately short — a page maximum. An ADR nobody writes is worth nothing; the discipline is in the cadence, not the polish. Rule of thumb: **write an ADR whenever reversing the decision would cost more than a day.**

### 5. From specification to roadmap: sequencing reviewable increments

The roadmap converts specs into a dependency-ordered sequence of changes each small enough to pass the diff budget. This is where the assistant's planning ability pays off and where its optimism must be corrected — it will happily propose "implement the application service" as one step, which is 600 lines. The heuristic that works: **one specification rule per increment, one increment per commit, schema before service before router before test-hardening.** SPEC-004 decomposes into (a) `fee_assessments` table + migration ~70 lines; (b) the pure `calculate_fee()` ~60 lines; (c) the idempotent persistence service ~80 lines; (d) the router ~50 lines; (e) property tests ~90 lines — five increments, all under budget, each independently reviewable and revertable.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Non-goals are load-bearing.* The cheapest way to stop an assistant inventing a feature is to name the feature and say it is out of scope.
- *Acceptance criteria are the contract.* Written with concrete values, they become tests, review checkpoints and the definition of done simultaneously.
- *Decide once, record once.* An ADR is immutable; a superseding decision gets a new ADR that links back, never an edit.
- *Model the workflow, not the status column.* States with explicit transitions catch a whole class of defects that a free-text status never will.
- *Verify every domain fact the assistant asserts.* Plausibility is not provenance.

**Common mistakes (each appears in the Lab 2 starter deliberately)**
1. A spec with no non-goals, so the generated implementation also adds licence renewal, an admin panel and an email notifier nobody asked for.
2. Acceptance criteria written abstractly ("the fee is calculated correctly") that cannot fail, and therefore cannot become a test.
3. A domain model with `status: str` and no enum or transition validation, allowing `"Approved"`, `"approved"` and `"APPROVED"` to coexist in production data.
4. Money modelled as `Float`, generated by default because the assistant saw `amount` and reached for a float — with the resulting SAR 3,779.9999999999995 total.
5. An ADR written *after* the code, reverse-engineered to justify what was generated — which records nothing and misleads the next engineer.
6. `national_id` stored in plaintext and used as the natural key, so it appears in every foreign key, log line and URL — a PDPL failure baked into the schema.

**Production considerations**
- Keep specs in the repository, versioned with the code (`docs/specs/`), not in a wiki. A spec that drifts from the code is worse than no spec; co-location makes drift visible in review.
- Number specs and reference them in commits and PR titles. This is how an auditor traces a regulation clause to a running line of code — increasingly a requirement in Saudi public-sector assurance.
- Maintain `docs/DATA_INVENTORY.md` listing every field holding personal data, its lawful basis and its retention period. Generate the first draft with the assistant from the models file, then verify it by hand — it will miss the fields hidden in JSON columns.

### 7. Real-world example walkthrough

Narrate this (5 minutes). A municipal e-services team was rebuilding a permits system and used an assistant to accelerate design. In two hours it produced a complete data model, an API surface and a plausible fee schedule. The team built against it for three weeks. At the first business review the municipality's licensing director pointed out that the fee schedule was invented — the real one had a different structure entirely, with a per-activity minimum and a discount for renewals, neither of which the model could express. The rebuild cost four weeks. The correction that stopped it recurring was small and procedural: every domain fact in a spec carries a provenance tag — `[SOURCE: municipal fee circular 1447-14]` or `[UNVERIFIED]` — and no `[UNVERIFIED]` fact may be implemented. The assistant remained just as useful; it simply stopped being trusted as a source of truth about the world.

## Code Examples

### A specification an assistant can implement against

```markdown
# docs/specs/SPEC-004-fee-calculation.md
<!-- WHY this format: every section below removes one class of generation error.
     Non-goals stop invented features; concrete acceptance values make the
     criteria executable; the data-protection block makes PDPL a generation-time
     constraint rather than a review-time argument. -->

# SPEC-004 — Fee calculation for a licence application

**Status:** approved  **Owner:** licensing squad  **Related ADR:** 0003

## Intent
Given an eligible application, produce an immutable fee assessment in SAR that the
applicant can pay through SADAD.

## Non-goals
- No refunds, no partial payments, no instalments.
- No renewal pricing (SPEC-011, not yet approved).
- No currency other than SAR. No tax computation.

## Inputs
| Field | Type | Constraint |
|---|---|---|
| `application_id` | UUID | must exist, status == `eligible` |
| `activity_code` | str | 4-digit ISIC code, present in `activities` reference table |
| `area_sqm` | Decimal | > 0, <= 5000, two decimal places |
| `city` | str | one of the 13 supported municipalities |

## Rules
1. `base_fee` is looked up from the `activities` table by `activity_code`.
   [SOURCE: municipal fee circular 1447-14]
2. `area_surcharge` = SAR 15.00 × max(0, area_sqm − 100), rounded to 2 dp.
3. `service_fee` = 5% of (`base_fee` + `area_surcharge`), rounded HALF_UP to 2 dp.
4. `total` = `base_fee` + `area_surcharge` + `service_fee`.
5. All arithmetic uses `Decimal`. Float is forbidden anywhere in this path.
6. An assessment is immutable. Re-assessing creates a new row; it never updates one.
7. At most one assessment may be `active` per application at any time.

## Outputs
`201 Created` with `{assessment_id, base_fee, area_surcharge, service_fee, total,
currency: "SAR", assessed_at}`.

## Error cases
| Condition | Status | Error code |
|---|---|---|
| Application not found | 404 | `application_not_found` |
| Application status != `eligible` | 409 | `invalid_status_for_assessment` |
| `activity_code` not in reference table | 422 | `unknown_activity_code` |
| An active assessment already exists | 409 | `assessment_already_exists` |

## Acceptance criteria
- **AC1** Given activity `5610` (base SAR 2,400.00) and area 180.00 m²,
  when an assessment is created, then `area_surcharge` == 1,200.00,
  `service_fee` == 180.00 and `total` == 3,780.00.
- **AC2** Given area 100.00 m², then `area_surcharge` == 0.00.
- **AC3** Given an application with an active assessment, when assessment is
  requested again, then 409 `assessment_already_exists` and no new row is written.
- **AC4** Given two concurrent assessment requests for the same application,
  then exactly one row exists afterwards. (See SPEC-004-A, M4.)

## Data protection (PDPL)
No personal data is read or written by this path. `application_id` is an opaque
UUID; `national_id_hash` must not be joined into any response.
```

### The domain model, reviewed rather than accepted

```python
# app/rukhsa/models/application.py
"""SQLAlchemy 2.0 mappings for the Rukhsa application aggregate.

WHY these choices are explicit rather than left to the generator:
  - `ApplicationStatus` is an Enum, not a string, so the database rejects the
    "Approved"/"approved"/"APPROVED" drift that free-text status columns always
    develop (M2 common mistake #3).
  - Money is Numeric(12, 2) and never Float (ADR-0003) -- float SAR arithmetic
    produces totals like 3779.9999999999995 that fail reconciliation.
  - `national_id_hash` stores a salted SHA-256 digest, never the identifier
    itself: PDPL data minimisation applied at the schema level, so no downstream
    query, log or join can ever leak it.
"""
from __future__ import annotations

import enum
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import CheckConstraint, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy import UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.rukhsa.models.base import Base


class ApplicationStatus(str, enum.Enum):
    """The states of the licensing workflow (SPEC-001 §3)."""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    RETURNED_FOR_CORRECTION = "returned_for_correction"
    ELIGIBLE = "eligible"
    REJECTED = "rejected"
    AWAITING_PAYMENT = "awaiting_payment"
    AWAITING_INSPECTION = "awaiting_inspection"
    ISSUED = "issued"


class Application(Base):
    """A citizen's application for a commercial licence."""

    __tablename__ = "applications"
    __table_args__ = (
        # A human-facing reference must be unique: it is quoted in correspondence
        # and printed on the certificate.
        UniqueConstraint("reference", name="uq_applications_reference"),
        CheckConstraint("area_sqm > 0 AND area_sqm <= 5000", name="ck_applications_area"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    reference: Mapped[str] = mapped_column(String(20), nullable=False)

    # PDPL: the citizen's identifier is only ever stored as a salted digest.
    national_id_hash: Mapped[str] = mapped_column(String(64), nullable=False, index=True)

    business_name_ar: Mapped[str] = mapped_column(String(200), nullable=False)
    business_name_en: Mapped[str] = mapped_column(String(200), nullable=False)
    activity_code: Mapped[str] = mapped_column(String(4), nullable=False, index=True)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    area_sqm: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(ApplicationStatus, name="application_status", native_enum=True),
        nullable=False,
        default=ApplicationStatus.DRAFT,
        index=True,
    )

    submitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Documents live in their own table (see docs/specs/SPEC-001 §4): the row holds
    # only an object key and a sha256 digest, never the file bytes, so a document's
    # contents can never leak through a log line or an API response.
    documents: Mapped[list["Document"]] = relationship(
        back_populates="application", cascade="all, delete-orphan"
    )
```

### An explicit state machine instead of a free-text status

```python
# app/rukhsa/services/transitions.py
"""Validated state transitions for a licence application.

WHY a table rather than scattered `if status == ...` checks: a generated router
will happily assign any status string it thinks is reasonable. Centralising the
legal transitions means one reviewable place decides what the workflow permits,
and an illegal transition raises instead of corrupting the record.
"""
from __future__ import annotations

from app.rukhsa.models.application import Application, ApplicationStatus

# The edges of the state machine in SPEC-001 §3. Anything not listed is illegal.
_ALLOWED: dict[ApplicationStatus, frozenset[ApplicationStatus]] = {
    ApplicationStatus.DRAFT: frozenset({ApplicationStatus.SUBMITTED}),
    ApplicationStatus.SUBMITTED: frozenset({
        ApplicationStatus.ELIGIBLE,
        ApplicationStatus.REJECTED,
        ApplicationStatus.RETURNED_FOR_CORRECTION,
    }),
    ApplicationStatus.RETURNED_FOR_CORRECTION: frozenset({ApplicationStatus.SUBMITTED}),
    ApplicationStatus.ELIGIBLE: frozenset({ApplicationStatus.AWAITING_PAYMENT}),
    ApplicationStatus.AWAITING_PAYMENT: frozenset({ApplicationStatus.AWAITING_INSPECTION}),
    ApplicationStatus.AWAITING_INSPECTION: frozenset({
        ApplicationStatus.ISSUED,
        ApplicationStatus.REJECTED,
    }),
    ApplicationStatus.ISSUED: frozenset(),      # terminal
    ApplicationStatus.REJECTED: frozenset(),    # terminal
}


class IllegalTransition(Exception):
    """Raised when a caller attempts a transition the workflow does not permit."""

    def __init__(self, current: ApplicationStatus, target: ApplicationStatus) -> None:
        super().__init__(f"illegal transition {current.value} -> {target.value}")
        self.current = current
        self.target = target


def transition(application: Application, target: ApplicationStatus) -> None:
    """Move `application` to `target`, or raise IllegalTransition.

    The caller is responsible for the surrounding transaction; this function
    mutates the instance only, so it is trivially unit-testable without a
    database (see M6 -- 11 of the 94 unit tests exercise this table).
    """
    if target not in _ALLOWED[application.status]:
        raise IllegalTransition(application.status, target)
    application.status = target
```

## Hands-on Lab 2 — Specify and Design Rukhsa

| | |
|---|---|
| **Objective** | Produce the artefacts the rest of the week is generated from: three specifications with executable acceptance criteria, three ADRs, the SQLAlchemy domain model with an explicit state machine, and the first Alembic migration |
| **Duration** | 55 minutes |
| **Setup** | Lab 1 repository with `CLAUDE.md` committed, PostgreSQL 16 running, `pip install -r requirements.txt` (FastAPI 0.115, SQLAlchemy 2.0.35, Alembic 1.13, pydantic 2.9), `git checkout lab2-start` |

**Instructions & tasks**

1. *(8 min)* **Expand.** Prompt the assistant to enumerate the states, actors, failure modes and open questions for "a citizen applies for a commercial licence in a Saudi municipality." Capture the raw output in `docs/analysis/elicitation.md`. Mark every domain fact it asserts as `[UNVERIFIED]` — you will find at least four fabricated ones.
2. *(10 min)* **Converge.** Using the instructor-provided municipal fee circular extract as the source, write `SPEC-004-fee-calculation.md` following the template. It must contain non-goals, four error cases and **AC1 with the concrete SAR 3,780.00 figure**.
3. *(10 min)* Write `SPEC-001` (create application) and `SPEC-007` (licence issuance + QR verification) at the same level of precision, then have your pair partner read them and mark every place where two engineers could generate incompatible implementations. Fix those.
4. *(10 min)* Write `ADR-0001` (PostgreSQL as the single datastore), `ADR-0002` (synchronous SQLAlchemy) and `ADR-0003` (Decimal money). Each names the rejected alternative and a consequence you accept. Ask the assistant for a *fourth* candidate alternative you had not considered, and record whether it changed your decision.
5. *(12 min)* Generate the models from `SPEC-001` with `CLAUDE.md` in context, then READ the diff: check the `status` type, the money type, the `national_id` handling and the uniqueness constraint. Fix what fails review. Run `alembic revision --autogenerate -m "applications and documents"`, inspect the generated migration, and apply it.
6. *(5 min)* Commit: `feat(domain): applications + documents model and state machine (SPEC-001, ADR-0003)`.

**Expected output**
```
$ alembic upgrade head
INFO  [alembic.runtime.migration] Running upgrade  -> 7c1f9a2b4d10, applications and documents
$ psql $RUKHSA_DATABASE_URL -c "\d applications" | head -14
                          Table "public.applications"
      Column       |           Type           | Nullable |
-------------------+--------------------------+----------+
 id                | uuid                     | not null |
 reference         | character varying(20)    | not null |
 national_id_hash  | character varying(64)    | not null |
 business_name_ar  | character varying(200)   | not null |
 business_name_en  | character varying(200)   | not null |
 activity_code     | character varying(4)     | not null |
 city              | character varying(60)    | not null |
 area_sqm          | numeric(10,2)            | not null |
 status            | application_status       | not null |
Indexes: "uq_applications_reference" UNIQUE CONSTRAINT, btree (reference)
Check constraints: "ck_applications_area" CHECK (area_sqm > 0 AND area_sqm <= 5000)

$ pytest tests/unit/test_transitions.py -q
11 passed in 0.21s
```

**Acceptance criteria**
- Three specs exist with non-goals, ≥ 3 error cases each, and at least one acceptance criterion carrying a concrete SAR value.
- Three ADRs exist, each naming a rejected alternative and an accepted consequence.
- `applications.status` is a database enum and `area_sqm` is `numeric`; no column stores a raw national ID.
- `alembic upgrade head` applies cleanly and `alembic downgrade -1` reverses it.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `alembic revision --autogenerate` produces an empty migration | Models not imported in `env.py` | Import `app.rukhsa.models` in `alembic/env.py` so metadata is populated |
| Enum column generated as `VARCHAR` | Assistant used `Enum(..., native_enum=False)` | Set `native_enum=True`; regenerate the migration and check `CREATE TYPE` appears |
| `area_sqm` generated as `Float` | Assistant's default for a numeric-sounding field | Reject the diff; `Numeric(10, 2)` per ADR-0003. Add a Semgrep rule in M5 |
| Downgrade fails on the enum type | Autogenerate omits `DROP TYPE` | Add `sa.Enum(name="application_status").drop(op.get_bind())` to `downgrade()` |

**Instructor notes.** Step 1 is the module's teaching moment: collect the fabricated "facts" on a shared board — expect invented validity periods, an invented appeals window and an invented fee formula. Do not correct them privately; make the room see how *plausible* they were. Watch for participants writing acceptance criteria without numbers in step 2 — send them back; an AC that cannot fail is not an AC. Fast finishers: have them generate `docs/DATA_INVENTORY.md` from the models file and then hand-verify it, discovering that the assistant missed the personal data implied by `documents.object_key` when the key encodes an applicant name.

## Mini Exercises

**Quiz (5 questions)**
1. Which spec section most effectively prevents an assistant inventing features? → **Non-goals**.
2. Why must an acceptance criterion carry concrete values? → so it can fail, and so it converts directly into a test.
3. What is the rule of thumb for when to write an ADR? → when reversing the decision would cost more than a day.
4. Why is `status: str` a defect rather than a style choice? → it permits case and spelling drift the database cannot reject, corrupting workflow logic.
5. An assistant states that a Saudi commercial licence is valid for exactly three years. What do you do? → tag it `[UNVERIFIED]` and verify against the municipal source before it becomes code.

**Debugging exercise.** Branch `lab2-float-money` models `base_fee`, `service_fee` and `total` as `Float`. The unit tests pass because they were generated with the same assumption and assert with `pytest.approx`. Have participants add AC1 as an exact-equality test, watch it fail with `3779.9999999999995`, and discuss why a generated test suite that agrees with a generated implementation proves nothing.

**Design exercise.** The municipality asks for "an appeals process for rejected applications." Write the non-goals section for that specification — five bullets — before writing anything else, and defend each one.

**Discussion questions.**
- If the assistant proposes an architecture you would not have thought of and cannot fully evaluate, is adopting it courage or negligence? What in your ADR would make the difference?
- Specifications used to be a project-management artefact. In AI-assisted development, are they now an engineering artefact — and if so, who should own them?

## Case Study — Designing the Berth-Booking Rebuild at "Rawabi" (روابي) Port Services

**Scenario.** "Rawabi" (روابي), the digital services unit of a Saudi port operator in Jeddah, is rebuilding a 14-year-old berth-booking system. The legacy application has no documentation, its original team has left, and its behaviour is known only through 340 pages of user manuals in Arabic and English. The new team of six has an assistant and eleven weeks.

**Business context.** Berth allocation drives SAR 240M of annual throughput; a booking defect that double-allocates a berth costs demurrage charges of roughly SAR 90,000 per incident and damages the operator's service-level commitments to shipping lines.

**Technical challenge.** The team must reconstruct the requirements from documentation and legacy database schemas rather than from a specification, and must do it fast enough to leave time to build. Early attempts to have the assistant "read the manual and generate the system" produced a confident, coherent design that quietly omitted the tidal-window constraint and the pilot-availability dependency — two rules that exist only in an operational annexe and in the heads of two long-serving controllers.

**Constraints.** The legacy database cannot be modified during the transition; the two controllers are available for four hours per week total; port operations are 24/7 with no maintenance window longer than 90 minutes; documentation is bilingual and the Arabic annexes are the authoritative ones where the two disagree.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) use the assistant to *extract and structure* — turn 340 pages into a candidate rule catalogue with a page citation per rule, which is verifiable work rather than invented work; (2) tag every extracted rule with provenance and a confidence, and put `[UNVERIFIED]` rules at the top of the controllers' four hours so scarce expert time is spent only on ambiguity; (3) reconstruct the domain from the legacy schema *and* the rule catalogue, and treat disagreements between them as findings rather than noise; (4) write ADRs for the transition decisions (strangler pattern vs big-bang, dual-write vs read-through) because the rebuild will outlive its current team too; (5) sequence the roadmap so the tidal-window rule — the highest-consequence, least-documented rule — is implemented and validated first, not last.

**Discussion questions.**
1. The assistant's omission of the tidal-window rule was invisible because the design it produced was internally consistent. What review technique catches an omission rather than an error?
2. Provenance tagging costs real time. How would you justify it to a delivery manager who can see the assistant producing a rule catalogue in forty minutes without it?
3. The Arabic annexes are authoritative where they disagree with the English manual. What does that imply about how the assistant should be prompted, and about who must review its extraction?
4. Would you write an ADR for "we used an assistant to reconstruct the requirements"? What would its consequences section say?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Specifications with executable acceptance criteria | Specification quality | 3/3, each with ≥ 1 concrete value | peer + instructor review |
| Fabricated domain facts identified | Critical evaluation | ≥ 4 tagged `[UNVERIFIED]` | `docs/analysis/elicitation.md` |
| ADRs with a named rejected alternative | Decision hygiene | 3/3 | file review |
| Schema correctness | Domain modelling | enum status, `numeric` money, hashed national ID | `\d applications` |
| Migration reversibility | Operability | `downgrade -1` succeeds | live run |

**Example benchmark table (filled during lab):**

| Artefact | Lines | Generated / authored | Review findings | Outcome |
|---|---|---|---|---|
| `SPEC-004-fee-calculation.md` | 62 | authored, assistant-expanded | 2 vague ACs rewritten with SAR values | approved |
| `elicitation.md` | 148 | generated | 5 fabricated facts tagged `[UNVERIFIED]` | input only |
| `models/application.py` | 121 | generated | `Float` → `Numeric`, `str` status → Enum | accepted after fixes |
| `7c1f9a2b4d10_*.py` migration | 78 | autogenerated | missing `DROP TYPE` in downgrade | accepted after fix |

## Required Visuals and Training Assets

### Diagrams
1. **Expand → Interrogate → Converge** — *Purpose:* the requirements method in one image. *Elements:* an assistant fanning one requirement into many candidates, a human filter labelled "domain expert", and a narrow output labelled "acceptance criteria". *Style:* funnel, three bands, Arabic subtitles. *Designer description:* "A wide spray of candidate rules narrowing through a human-shaped gate into a short numbered list."
2. **Rukhsa application state machine** — *Purpose:* the workflow every later module enforces. *Elements:* the eight states with labelled transitions, terminal states shaded, illegal transitions shown as struck-through greyed arrows. *Style:* clean state chart, reused in M3, M6 and the capstone.
3. **Rukhsa entity-relationship diagram** — *Purpose:* the shared mental model of the data. *Elements:* the seven tables with cardinalities; `national_id_hash` and `documents` flagged with a PDPL shield; append-only tables marked. *Style:* crow's-foot ERD, two accent colours.
4. **Spec → increment → commit** — *Purpose:* show how a spec becomes a roadmap. *Elements:* SPEC-004 decomposed into its five increments with line estimates, each under the 150-line budget line drawn across the diagram. *Style:* horizontal decomposition tree with a budget threshold line.

### Images (screenshots)
1. **An assistant fabricating a fee schedule** — *why:* the module's central warning made concrete; *content:* the chat output presenting invented figures in an authoritative table.
2. **`\d applications` output in psql** — *why:* participants must learn to verify the schema rather than trust the model file; *content:* the enum type and `numeric(10,2)` visible.
3. **A rendered ADR in the repository** — *why:* shows the expected length and shape; *content:* a one-page ADR-0003 with context, decision, alternatives, consequences.

### Simulations
1. **The plausible-fabrication drill** — *Setup:* participants are given ten domain statements about Saudi municipal licensing, six true and four assistant-generated. *Expected behaviour:* the room cannot reliably tell them apart. *Learning objective:* fluency is not provenance; tag and verify.
2. **Two engineers, one spec** — *Setup:* two participants independently generate an implementation from the same spec, once from a vague version and once from the SPEC-004 template. *Expected behaviour:* the vague version yields incompatible response envelopes and different rounding; the precise version yields compatible ones. *Learning objective:* specification precision is measurable.

### Interactive Activities
- **Non-goals auction (12 min):** teams bid for the five non-goals they think prevent the most invented code; the instructor reveals what a live generation actually invented for each.
- **ADR speed-round (15 min):** three real decisions, five minutes each, one page each, then a peer challenge round where the other team argues the rejected alternative.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `data/reference/activities.csv` | ISIC-derived municipal activity codes with SAR base fees (retail 1,200 / F&B 2,400 / light industrial 4,800) | CSV | 148 rows | Fee lookup, used from M2 to the capstone |
| `data/reference/municipalities.csv` | 13 supported cities with zoning class | CSV | 13 rows | Eligibility rules in M3 |
| `docs/source/fee_circular_1447-14.md` | Instructor-provided extract standing in for the municipal circular | Markdown | 2 pages | The authoritative source that beats the assistant's invention |

### Demo Requirements
- **Instructor demo (7 minutes):** ask the assistant on the projector for "the standard fee structure for a commercial licence in Riyadh," receive a confident and entirely invented table, then open the fee circular extract beside it. Leave both on screen while you explain provenance tagging — the side-by-side is worth more than any slide about hallucination.

---

# Module 3 — Code Generation and Optimisation with AI
## توليد الكود وتحسينه بالذكاء الاصطناعي

## Module Overview

**Purpose.** This module covers catalogue module 2 and delivers the **GENERATE** and **READ** steps of the contract. Participants learn two distinct prompt shapes — greenfield and refactor — and then learn the skill the whole course turns on: reading a generated diff critically enough to reject it. They finish by reviewing generated code for algorithmic complexity and resource consumption, profiling it with `cProfile` and `py-spy`, and removing a real N+1 query that costs Rukhsa's list endpoint 1,744 ms of its 1,840 ms p95.

**Business relevance.** Generated code is idiomatic and readable and frequently *quadratic*. An assistant optimises for a plausible-looking solution to the sentence you wrote, not for the shape of your data; it does not know that `applications` will hold 400,000 rows or that the loop it wrote issues a query per iteration. In a public-facing government portal that difference is the gap between a page that loads and a page that times out during the first week of a licensing deadline. Reviewing generated code for complexity is now a core engineering skill, not an optimisation specialism.

**Industry use cases.**
- A national portal's search endpoint degrades from 90 ms to 4 s after a generated "improvement" replaced a single indexed query with a Python-side join.
- A billing service exhausts its database connection pool because a generated background job opens a session per record instead of per batch.
- A team refactors a 900-line legacy module with an assistant and must prove behaviour is unchanged before merging — a refactor prompt, not a greenfield one.

**Expected competencies.** After this module a participant can choose and write the right prompt shape for a task; perform a seven-pass critical read of a generated diff; identify N+1 access patterns and unnecessary complexity in generated code; profile a FastAPI endpoint with `cProfile` and `py-spy`; and verify that a suggested library API actually exists before building on it.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Write greenfield versus refactor prompts appropriate to the task and its risk | LO3 |
| 3.2 | Perform a seven-pass critical read of a generated diff and articulate each rejection | LO3, LO1 |
| 3.3 | Review generated code for algorithmic complexity and database access patterns | LO3 |
| 3.4 | Profile an endpoint with `cProfile` and `py-spy` and attribute time to a root cause | LO3, LO4 |
| 3.5 | Detect hallucinated library APIs and unverifiable package suggestions before they reach a commit | LO3, LO5 |

## Technical Content

### 1. Two prompt shapes, two risk profiles

Greenfield and refactor prompts are not variations of one technique; they optimise for opposite properties.

| | Greenfield prompt | Refactor prompt |
|---|---|---|
| Goal | New behaviour that matches a spec | Identical behaviour, better structure |
| Must include | The spec, the layering rules, the target file paths | The current code, the *invariant to preserve*, and the existing tests |
| Success test | The acceptance criteria pass | The existing tests pass **unchanged** |
| Main risk | Invented requirements and missing error paths | Silent behaviour change disguised as tidying |
| Diff budget | ≤ 150 lines | ≤ 150 lines **and** no test file modified in the same change |

The last row is the operational rule worth writing on the board: **a refactor that edits its own tests is not a refactor.** If the assistant must change a test to make a refactor pass, either the refactor changed behaviour or the test was asserting an implementation detail — and you must decide which before merging, not after.

A refactor prompt for Rukhsa's eligibility service looks like this in structure: *"Here is `eligibility.py` and `test_eligibility.py`. Extract the four rule checks into separate pure functions in the same module, keeping `evaluate()` as the only public entry point. Behaviour must be identical: all 14 existing tests must pass with no edits. Do not add new rules, do not change signatures, do not touch the database layer."* Three constraints, one invariant, and an explicit non-goal list — the same discipline as a specification, compressed.

### 2. The seven-pass critical diff read

Reading a generated diff is not reading code. You are hunting for specific, recurring defect classes, and doing it as seven fast passes catches far more than one slow pass. Total cost on a 150-line diff: four to ten minutes.

| Pass | Question | Typical finding in generated code |
|---|---|---|
| **1. Scope** | Did it change only what I asked for? | An unrelated "improvement" to a neighbouring function; a reformatted import block hiding a real change |
| **2. Contract** | Do signatures, types and the response shape match the spec? | An invented response envelope; `float` where the spec says `Decimal`; a nullable field silently made required |
| **3. Existence** | Does every API, method and package it uses actually exist? | `Session.get_or_404()`, `select().paginate()` — plausible, non-existent |
| **4. Data access** | How many queries does this issue, and how does that scale with input? | A query inside a loop; a `.all()` before a filter; a missing index on a new lookup column |
| **5. Failure** | What happens on the error path, and is it the path the spec names? | A bare `except Exception: pass`; a 500 where the spec requires 409; a partially committed transaction |
| **6. Security** | Injection, secrets, authorisation, exposure? | f-string SQL; a missing ownership check on `application_id`; personal data in a log line |
| **7. Consistency** | Does it look like the rest of this codebase? | The legacy `Column()` style beside `Mapped[]`; a second, different error-response format |

Teach this as a checklist a pair partner reads aloud. The navigator asks the seven questions; the driver answers them from the diff. It takes one lab to become automatic and it is the single highest-yield habit in this course.

### 3. Complexity review of generated code

Assistants produce correct-looking code with the wrong complexity class because the prompt describes *what*, and complexity is a consequence of *how much*. Three patterns account for most of what you will find.

**Nested membership tests.** "Check each application against the restricted activity codes" becomes a list scan inside a loop — O(n·m) where a `set` makes it O(n). At 400,000 applications × 148 codes that is 59.2M comparisons instead of 400,000. **Python-side joins.** The assistant fetches two tables and matches them in a dictionary comprehension: correct, readable, and it transfers the entire table over the network. **The N+1** is the most common and most costly — generated ORM code lazily loads a relationship inside a loop, so listing 100 applications with their documents issues 1 + 100 = 101 queries. Measured on the Rukhsa list endpoint:

| Implementation | Queries | p95 latency | Rows transferred |
|---|---|---|---|
| Generated (lazy load in loop) | 101 | 1,840 ms | 100 + 412 |
| `selectinload(Application.documents)` | 2 | 96 ms | 100 + 412 |
| `joinedload` with pagination | 1 | 88 ms | 512 (duplicated parents) |

19.2× on one line of change. Note that `joinedload` is marginally faster here but duplicates parent rows across the join, which breaks `LIMIT`-based pagination — the kind of trade-off a reviewer must actually think about rather than accept from a suggestion.

### 4. Profiling: attributing time before optimising

Never optimise from a hypothesis. `cProfile` is deterministic and in-process, answering "which functions consumed the wall time of this call?"; its 1.3–2× overhead distorts absolute numbers but preserves the ranking, which is what you need. `py-spy` is a sampling profiler that attaches to a *running* process without modifying it (`py-spy record -o profile.svg --pid 4711 --duration 30`), so it is the right tool for a service already under load, including in staging.

The workflow: reproduce under load → `py-spy` to find the hot area → `cProfile` on the isolated path to attribute precisely → fix → re-measure with the same harness. Re-measurement is not optional; roughly a third of the "optimisations" a cohort applies make things slower, and only the harness tells you. For database time neither profiler suffices, because the time is spent waiting on the server: turn on SQLAlchemy's `echo` or attach an event listener that counts statements per request. The query *count* is usually the diagnosis, and it is a number a test can assert (M6 does exactly that).

### 5. Hallucinated APIs and phantom packages

An assistant generating against an unfamiliar library produces method names that *should* exist. `session.get_or_404(Application, id)` is a Flask-SQLAlchemy idiom unavailable on a plain SQLAlchemy 2.0 `Session`; `select(Application).paginate(page=2)` is not a SQLAlchemy construct at all. These fail at import or call time, so they are cheap — annoying, not dangerous.

The dangerous variant is the **phantom package**. Asked for JWT handling, an assistant may confidently `pip install fastapi-jwt-auth-pro`, which does not exist. That is cheap to discover *unless* an attacker has already registered the name — the attack now called **slopsquatting**, publishing malicious packages under names assistants commonly hallucinate. Mitigations belong in M5; the review habit belongs here: **pass 3 exists for exactly this**, and any new dependency in a generated diff must be verified on the index and justified in the PR description before it is installed.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Generate small, review whole.* A 150-line change reviewed in seven passes beats a 600-line change reviewed once, every time.
- *A refactor is defined by its invariant.* State it in the prompt, prove it with unchanged tests.
- *Complexity is a review property, not a performance activity.* You look for it in the diff, not after the incident.
- *Measure before and after with the same harness.* An unmeasured optimisation is a guess with a commit message.
- *Verify existence before you build.* Every unfamiliar API and every new package.

**Common mistakes (each appears in the Lab 3 starter deliberately)**
1. An N+1 in the list endpoint: `for app in applications: doc_count = len(app.documents)` — 101 queries, 1,840 ms.
2. A generated `calculate_fee()` using `float`, producing SAR 3,779.9999999999995 and failing AC1 by exact comparison.
3. A restricted-activity check using a list membership test inside a loop — O(n·m) where a set is O(n).
4. A hallucinated call to `session.get_or_404()`, which raises `AttributeError` on first use.
5. A `pip install fastapi-jwt-auth-pro` line in the generated setup instructions for a package that does not exist.
6. A refactor prompt answered with a diff that also edits `test_eligibility.py` to match its new behaviour — the invariant silently broken.

**Production considerations**
- Add a per-request query counter in development and log any request exceeding a threshold (Rukhsa uses 10). This turns N+1 detection from a code-review skill into a runtime alarm.
- Set the connection pool deliberately (`pool_size`, `max_overflow`) and load-test to it. Generated code will not size your pool, and an N+1 exhausts it long before it saturates the database.
- Keep a `benchmarks/` harness in the repository so "before and after" is reproducible by anyone, including the reviewer. Rukhsa's is a `pytest-benchmark` module plus a `locust` file.

### 7. Real-world example walkthrough

Narrate this (5 minutes). A team shipped a generated "recently updated records" panel to a public portal. It passed review — the code was clean and the tests were green — and it worked perfectly against the 200-row development database. On launch day, with 380,000 rows, the panel issued one query per row to resolve a display name, and the endpoint's p95 went from 110 ms to 21 s; the connection pool saturated and took the *unrelated* login endpoint down with it. The fix was a single `selectinload` and shipped in eleven minutes. The lesson the team drew was not "review harder": it was that pass 4 of a diff read — *how many queries does this issue, and how does that scale?* — is a mechanical question that can be asked in fifteen seconds, and that a query-count assertion in the integration test would have failed in CI before any human had to notice.

## Code Examples

### The generated fee calculator, and the version that passes AC1

```python
# app/rukhsa/services/fees.py
"""Fee calculation for a licence application (SPEC-004).

WHY this file is pure: the calculation takes values and returns values, with no
session and no I/O. That makes every rule in SPEC-004 unit-testable in
microseconds and property-testable with Hypothesis in M6, and it keeps the
concurrency concern (M4) entirely in the persistence layer where it belongs.
"""

# ❌ AI-GENERATED — DO NOT SHIP.
# Defect 1: float arithmetic on money. 2400.0 + 1200.0 + 180.00000000000003 gives
#   3779.9999999999995, which fails SPEC-004 AC1 under exact comparison and
#   breaks reconciliation against SADAD to the halala.
# Defect 2: Python's round() is banker's rounding (round-half-to-even), so
#   round(2.675, 2) == 2.67. SPEC-004 rule 3 requires HALF_UP.
# Defect 3: no validation that area_sqm is positive, so a negative area silently
#   produces a negative surcharge and a discount.
#
# def calculate_fee(base_fee: float, area_sqm: float) -> dict:
#     surcharge = 15.0 * max(0, area_sqm - 100)
#     service = round((base_fee + surcharge) * 0.05, 2)
#     return {"total": base_fee + surcharge + service}

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

# SPEC-004 rule 2 and rule 3, as named constants rather than magic numbers.
SURCHARGE_PER_SQM = Decimal("15.00")
FREE_AREA_SQM = Decimal("100")
SERVICE_FEE_RATE = Decimal("0.05")
_TWO_PLACES = Decimal("0.01")


@dataclass(frozen=True)
class FeeBreakdown:
    """An immutable priced assessment. Currency is always SAR (SPEC-004 non-goals)."""

    base_fee: Decimal
    area_surcharge: Decimal
    service_fee: Decimal
    total: Decimal


def _round_half_up(value: Decimal) -> Decimal:
    """Round to two decimal places, half away from zero.

    Decimal.quantize with ROUND_HALF_UP is used rather than round(), which
    performs banker's rounding and would price 2.675 as 2.67.
    """
    return value.quantize(_TWO_PLACES, rounding=ROUND_HALF_UP)


def calculate_fee(base_fee: Decimal, area_sqm: Decimal) -> FeeBreakdown:
    """Price one application. Pure function -- no I/O, no session, no clock.

    Raises:
        ValueError: if area_sqm is not strictly positive (SPEC-004 inputs).
    """
    if area_sqm <= 0:
        raise ValueError("area_sqm must be greater than zero")

    chargeable_area = max(Decimal("0"), area_sqm - FREE_AREA_SQM)
    area_surcharge = _round_half_up(SURCHARGE_PER_SQM * chargeable_area)
    service_fee = _round_half_up((base_fee + area_surcharge) * SERVICE_FEE_RATE)
    total = base_fee + area_surcharge + service_fee

    # AC1: base 2400.00, area 180.00 -> surcharge 1200.00, service 180.00,
    #      total 3780.00 -- exactly, with no floating-point residue.
    return FeeBreakdown(
        base_fee=base_fee,
        area_surcharge=area_surcharge,
        service_fee=service_fee,
        total=_round_half_up(total),
    )
```

### The N+1 the assistant wrote, and the two-query version

```python
# app/rukhsa/repositories/applications.py
"""Read paths for the applications list (SPEC-002).

WHY eager loading is explicit here: SQLAlchemy's default lazy loading is correct
and invisible, which is the worst combination in generated code -- the loop reads
naturally and issues one query per iteration. Stating the load strategy at the
query makes the access pattern reviewable in pass 4 of the diff read.
"""
from __future__ import annotations

import uuid

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload

from app.rukhsa.models.application import Application, ApplicationStatus


# ❌ AI-GENERATED — DO NOT SHIP.
# Defect: N+1. `app.documents` is lazy-loaded, so listing 100 applications issues
# 1 query for the page plus 100 for the document collections = 101 round trips,
# measured at 1,840 ms p95. It is invisible in review unless pass 4 is performed.
#
# def list_applications(session: Session, limit: int = 100) -> list[dict]:
#     apps = session.scalars(select(Application).limit(limit)).all()
#     return [
#         {"reference": a.reference, "documents": len(a.documents)}  # <-- query here
#         for a in apps
#     ]


def _base_query(status: ApplicationStatus | None) -> Select[tuple[Application]]:
    """Shared filter so the list and count paths can never diverge."""
    stmt = select(Application)
    if status is not None:
        stmt = stmt.where(Application.status == status)
    return stmt


def list_applications(
    session: Session,
    *,
    status: ApplicationStatus | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[Application]:
    """Return one page of applications with documents already loaded.

    selectinload issues exactly one additional query (a WHERE ... IN over the
    page's ids), giving 2 queries total regardless of page size. joinedload would
    be one query but duplicates parent rows across the join, which corrupts
    LIMIT-based pagination -- hence the deliberate choice recorded here.
    """
    stmt = (
        _base_query(status)
        .options(selectinload(Application.documents))
        .order_by(Application.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(session.scalars(stmt).all())


def get_application(session: Session, application_id: uuid.UUID) -> Application | None:
    """Fetch one application.

    NOTE: an assistant will often suggest `session.get_or_404(...)`. That method
    does not exist on a SQLAlchemy 2.0 Session -- it is a Flask-SQLAlchemy idiom.
    Returning None and letting the service layer raise the domain error keeps
    HTTP concerns out of the repository.
    """
    return session.get(Application, application_id)
```

### A reproducible profiling harness and a query counter

```python
# benchmarks/profile_list_endpoint.py
"""Attribute the wall time of GET /applications, reproducibly.

WHY a committed harness rather than an ad-hoc timing script: the 'before' and
'after' numbers in a pull request must be produced the same way by the author and
the reviewer, or the optimisation claim is unverifiable. Run:

    python benchmarks/profile_list_endpoint.py --rows 100 --repeat 20
"""
from __future__ import annotations

import argparse
import cProfile
import pstats
import statistics
import time
from contextlib import contextmanager

from sqlalchemy import event

from app.rukhsa.db import SessionLocal, engine
from app.rukhsa.repositories.applications import list_applications


@contextmanager
def count_queries():
    """Count SQL statements executed inside the block.

    The query count -- not the elapsed time -- is the diagnosis for an N+1, and
    unlike a timing it is stable enough to assert in a test (see M6).
    """
    counter = {"n": 0}

    def _on_execute(conn, cursor, statement, params, context, executemany):
        counter["n"] += 1

    event.listen(engine, "before_cursor_execute", _on_execute)
    try:
        yield counter
    finally:
        event.remove(engine, "before_cursor_execute", _on_execute)


def measure(rows: int, repeat: int) -> None:
    timings: list[float] = []
    with SessionLocal() as session:
        # One warm run so connection setup and query planning are not measured.
        list_applications(session, limit=rows)

        with count_queries() as counter:
            list_applications(session, limit=rows)
        print(f"queries per call: {counter['n']}")

        for _ in range(repeat):
            start = time.perf_counter()
            list_applications(session, limit=rows)
            timings.append((time.perf_counter() - start) * 1000)

    timings.sort()
    p95 = timings[int(len(timings) * 0.95) - 1]
    print(f"median {statistics.median(timings):.1f} ms   p95 {p95:.1f} ms")


if __name__ == "__main__":
    # --cprofile wraps measure() in cProfile.Profile() and prints the top 12
    # frames by cumulative time -- the caller that owns the cost, not the leaf.
    measure(rows=100, repeat=20)
```

## Hands-on Lab 3 — Generate, Review, Profile and Optimise the Applications API

| | |
|---|---|
| **Objective** | Generate the applications and documents API under the contract, reject the planted defects in a seven-pass diff read, then profile the list endpoint and remove the N+1 (1,840 ms → 96 ms p95) |
| **Duration** | 100 minutes (Lab 3a 45 min, Lab 3b 55 min) |
| **Setup** | Lab 2 repository migrated, `pip install py-spy pytest-benchmark`, seed the database with `python -m app.rukhsa.seed --applications 400 --documents 1650`, `git checkout lab3-start` |

**Instructions & tasks**

1. *(12 min)* **Lab 3a — greenfield.** Generate `POST /applications` and `POST /applications/{id}/documents` from `SPEC-001` with `CLAUDE.md` in context. Do not read the code yet; only note the diff size.
2. *(18 min)* Perform the seven-pass read with your pair partner reading the questions aloud. Record every finding in `LAB3_REVIEW.md` with its pass number. You must find at least four of the six planted defects, including the hallucinated `session.get_or_404()` and the phantom `fastapi-jwt-auth-pro` dependency.
3. *(15 min)* **Lab 3a — refactor prompt.** The generated eligibility check is one 90-line function. Write a refactor prompt with an explicit invariant ("all 14 existing tests pass unchanged, no signature changes, no new rules") and apply it. If the assistant edits a test file, reject the whole diff and re-prompt.
4. *(20 min)* **Lab 3b — measure.** Run `python benchmarks/profile_list_endpoint.py --rows 100 --repeat 20` and record queries-per-call and p95. Then run the API under load and attach `py-spy record -o profile.svg --pid $(pgrep -f uvicorn) --duration 20`. Identify from the flame graph *where* the time is, and from the query counter *why*.
5. *(20 min)* **Lab 3b — fix and re-measure.** Apply `selectinload`, re-run the identical harness, and record the new numbers. Then fix the `float` fee calculator and the O(n·m) restricted-activity check; add the exact-equality AC1 test and watch it go from fail to pass.
6. *(15 min)* Update `benchmarks/RESULTS.md` with a before/after table, then commit: `perf(applications): eager-load documents, remove N+1 in list endpoint (SPEC-002)`.

**Expected output**
```
$ python benchmarks/profile_list_endpoint.py --rows 100 --repeat 20
queries per call: 101
median 1712.4 ms   p95 1840.2 ms

# ... after applying selectinload ...
$ python benchmarks/profile_list_endpoint.py --rows 100 --repeat 20
queries per call: 2
median 88.6 ms   p95 96.1 ms

$ pytest tests/unit/test_fees.py::test_ac1_fnb_180sqm -q
tests/unit/test_fees.py .                                              [100%]
1 passed in 0.04s
# asserted: base 2400.00 + surcharge 1200.00 + service 180.00 == Decimal("3780.00")
```

**Acceptance criteria**
- `LAB3_REVIEW.md` records ≥ 4 planted defects, each tagged with the diff-read pass that found it.
- Query count for the list endpoint falls from 101 to 2; p95 falls from 1,840 ms to ≤ 100 ms, measured with the committed harness.
- `calculate_fee` uses `Decimal` throughout and AC1 passes under exact equality.
- The refactor commit changes no test file.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `py-spy` reports "permission denied" | Ptrace restrictions on Linux/macOS | Run with `sudo`, or `docker run --cap-add SYS_PTRACE`; on macOS grant Terminal developer-tools access |
| Query count is 2 but latency barely improves | Database is not the bottleneck at this row count | Re-seed to 400 applications; confirm you are measuring the seeded set, not an empty table |
| `selectinload` raises `ArgumentError` | Passed the string `"documents"` instead of the mapped attribute | Use `selectinload(Application.documents)` |
| AC1 still fails by 0.0000000001 | A `float` survives somewhere upstream (often the seed data) | Grep the path for `float(`; ensure the reference CSV loads `base_fee` via `Decimal(str(...))` |

**Instructor notes.** The seven-pass read is the skill; protect its twenty minutes even if the profiling runs short. Walk the room during step 2 — most pairs find the N+1 and the float, and most miss the phantom package because it is in a comment in the generated setup instructions rather than in code. That miss is the teaching moment for M5's supply-chain section, so let it happen. Fast finishers: have them add a `pytest` fixture that fails any integration test issuing more than 10 queries, and watch it catch a second, smaller N+1 in the documents endpoint.

## Mini Exercises

**Quiz (5 questions)**
1. What single rule distinguishes a legitimate refactor diff from a behaviour change? → the existing tests pass **unchanged**.
2. Which diff-read pass catches an N+1? → pass 4, data access ("how many queries, and how does that scale?").
3. Why is `joinedload` not automatically better than `selectinload` here? → it duplicates parent rows across the join, breaking `LIMIT`-based pagination.
4. When would you reach for `py-spy` rather than `cProfile`? → to profile an already-running process under load without modifying or restarting it.
5. What is slopsquatting? → registering malicious packages under names that assistants commonly hallucinate, so a generated `pip install` fetches an attacker's code.

**Debugging exercise.** Branch `lab3-hallucinated-api` calls `session.get_or_404(Application, app_id)`. It fails with `AttributeError` on the first request. Ask participants: why is this the *cheapest* class of hallucination, which class is more dangerous, and what would have caught it before the commit (pass 3, or simply running the code once)?

**Design exercise.** The restricted-activity check must run against 148 codes for every one of 400,000 applications in a nightly job. Write the three-line prompt that produces an O(n) implementation, and state the invariant a reviewer should check.

**Discussion questions.**
- If a generated implementation is 19× slower but ships in eleven minutes, when is that the right trade — and what makes the difference between a deliberate trade and an accident?
- Should a query-count assertion be part of the definition of done for every list endpoint, or is that over-engineering?

## Case Study — The Generated Billing Engine at "Sahab" (سحاب) Cloud Services

**Scenario.** "Sahab" (سحاب), a Saudi cloud hosting provider in Riyadh, rebuilt its usage-metering and invoicing engine with heavy assistant use, delivering in five weeks what had been estimated at fourteen. The engine was correct: invoices reconciled to the halala against the legacy system for three months of back-data. Then it went live for the full customer base and the nightly billing run, which had taken 40 minutes in the legacy system, took 9 hours 20 minutes — overrunning into business hours and delaying invoice delivery for 4,100 customers.

**Business context.** Sahab bills monthly in arrears; a late invoice run delays revenue recognition and triggers manual finance work. Two enterprise customers with contractual invoice-delivery dates were affected, exposing Sahab to service-credit claims.

**Technical challenge.** The engine was generated function by function against a clear specification, and each function was reviewed and correct in isolation. The aggregate behaviour was not reviewed at all: the usage-aggregation step loaded each customer's meter readings with a lazy relationship inside a per-customer loop, and the rate-card lookup performed a linear scan of 2,300 rate entries per reading. Neither is visible in a 90-line diff of an individually sensible function.

**Constraints.** Cannot pause billing; a rewrite is not fundable after a five-week delivery; the finance team requires bit-identical invoice output before and after any change, so every optimisation must be behaviour-preserving and provable; the engine runs on a fixed-size database instance that cannot be scaled during the fiscal year.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) profile before touching anything — `py-spy` on the running job attributes 84% of the time to two call sites, which reframes a nine-hour problem as two defects; (2) fix the access pattern, not the algorithm — batch the meter-reading load and index the rate card in a dict, both behaviour-preserving; (3) prove equivalence by re-running the three months of back-data and diffing invoice output byte-for-byte, which satisfies finance without a manual review; (4) institutionalise the miss — a query-count budget per job step, asserted in CI, so a per-record query cannot reappear silently; (5) add an aggregate review step to the process: after a set of individually reviewed functions is composed into a job, someone reviews the *composition* for access patterns.

**Discussion questions.**
1. Every function passed review and the system was still 14× too slow. What does that tell you about the unit of review?
2. Sahab's fix took two days against a five-week build. Does that vindicate the generation-first approach, or does it depend on something the case does not tell you?
3. Finance required bit-identical output. How does that constraint change which optimisations are available, and is it a reasonable requirement?
4. What would a "query-count budget in CI" actually assert for a batch job, where the count legitimately scales with the number of customers?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Planted defects found in the diff read | Review skill | ≥ 4 of 6, each tagged with a pass | `LAB3_REVIEW.md` |
| Queries per list-endpoint call | Data access | 2 (from 101) | committed query counter |
| List endpoint p95 | Performance | ≤ 100 ms at 100 rows (from 1,840 ms) | `benchmarks/profile_list_endpoint.py` |
| Money arithmetic | Correctness | AC1 passes under exact `Decimal` equality | `pytest tests/unit/test_fees.py` |
| Refactor invariant held | Discipline | 14/14 existing tests pass, 0 test files edited | `git diff --stat` on the refactor commit |

**Example benchmark table (filled during lab):**

| Change | Queries | Median | p95 | Speed-up | Verified by |
|---|---|---|---|---|---|
| Generated baseline | 101 | 1,712 ms | 1,840 ms | — | harness run 1 |
| `selectinload(documents)` | 2 | 88.6 ms | 96.1 ms | 19.2× | harness run 2 |
| Restricted-activity set lookup | 2 | 84.1 ms | 91.4 ms | 20.1× | harness run 3 |
| `Decimal` fee path | 2 | 84.3 ms | 91.7 ms | 20.1× (no regression) | harness run 4 |

## Required Visuals and Training Assets

### Diagrams
1. **The seven-pass diff read** — *Purpose:* the checklist participants use for the rest of the week. *Elements:* seven numbered lenses over a diff, each labelled with its question and its typical finding. *Style:* vertical checklist card, printable A5, one accent colour per pass. *Designer description:* "A code diff on the left, seven magnifying glasses stacked on the right, each annotated."
2. **N+1 visualised** — *Purpose:* make the cost of a lazy load physical. *Elements:* left panel showing 101 arrows between app and database; right panel showing 2; latency bars 1,840 ms vs 96 ms beneath. *Style:* side-by-side, red/green, numbers large.
3. **Greenfield versus refactor prompt anatomy** — *Purpose:* show that these are different techniques. *Elements:* two prompt templates side by side with their required inputs, invariants and success tests highlighted. *Style:* two-column comparison card.
4. **Flame graph reading guide** — *Purpose:* participants must interpret `py-spy` output, not just produce it. *Elements:* an annotated flame graph of the Rukhsa list endpoint with the lazy-load plateau circled and labelled. *Style:* annotated screenshot with callouts.

### Images (screenshots)
1. **`py-spy record` flame graph of the N+1** — *why:* the wide plateau of repeated ORM calls is unmistakable once seen; *content:* `lazy_load` frames dominating the width.
2. **SQLAlchemy `echo=True` log showing 101 statements** — *why:* the count is the diagnosis; *content:* the repeating `SELECT documents WHERE application_id = ...`.
3. **A phantom package on the index** — *why:* slopsquatting made real; *content:* a package-index search returning no result for the name the assistant suggested.

### Simulations
1. **Scale-up surprise** — *Setup:* the generated list endpoint against 200 rows, then against 400,000. *Expected behaviour:* imperceptible, then unusable. *Learning objective:* development-database performance is not evidence.
2. **The tidy refactor that wasn't** — *Setup:* branch `lab3-refactor-drift` where a "cleanup" refactor also relaxed a validation and edited its test. *Expected behaviour:* the suite is green and the behaviour changed. *Learning objective:* the invariant, not the green tick, defines a refactor.

### Interactive Activities
- **Complexity gallery (15 min):** six generated snippets on the wall; teams label each with its complexity class and the input size at which it becomes a problem.
- **Pass-4 speed drill (10 min):** four diffs, sixty seconds each, one question only — "how many queries?" Scores are read out; the room discovers the question is fast and the answers are not obvious.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Seeded `applications` | `python -m app.rukhsa.seed` | PostgreSQL | 400 rows | Profiling target for the list endpoint |
| Seeded `documents` | Same seeder, 3–5 per application | PostgreSQL | 1,650 rows | The N+1's second query |
| `data/reference/restricted_activities.csv` | Municipal restricted-activity list | CSV | 148 rows | The O(n·m) versus O(n) exercise |

### Demo Requirements
- **Instructor demo (8 minutes):** run the list endpoint against the seeded database with `echo=True` on the projector, let the 101 statements scroll past, then add one `selectinload` line and run it again. The visual contrast between a scrolling wall of SQL and two statements does more for pass-4 discipline than any explanation.

---

# Module 4 — AI-Assisted Debugging and Root-Cause Analysis
## تصحيح الأخطاء وتحليل الأسباب الجذرية بالذكاء الاصطناعي

## Module Overview

**Purpose.** This module covers catalogue module 3. An assistant is a superb debugging partner and a dangerous one: given a stack trace it will produce a confident diagnosis within seconds, and that diagnosis is right often enough to make participants stop verifying it. The module therefore teaches a **debugging contract** — reproduce, isolate, hypothesise, verify — and shows where the assistant genuinely accelerates each step. The concrete target is Rukhsa's hardest defect: a race condition that lets a double-submitted payment create two fee assessments for one application.

**Business relevance.** In a licensing portal, a concurrency defect on the money path is not a bug report; it is a citizen charged twice and a reconciliation exception that finance resolves by hand. Defects that only appear under concurrency are also exactly the class an assistant will not find by reading code, because nothing in the source is wrong — the interleaving is. Teaching engineers to reproduce before they ask, and to verify a proposed fix under load, is what separates a fixed defect from a hidden one.

**Industry use cases.**
- A payments team receives 37 duplicate charge reports in a week and must find the interleaving that produces them before the next billing cycle.
- An on-call engineer has a production stack trace, a PDPL obligation not to paste it anywhere, and fifteen minutes.
- A regression appears somewhere in 240 commits since the last good release, and `git bisect` must find it without a human reading 240 diffs.

**Expected competencies.** After this module a participant can construct a minimal reproduction before asking anyone (human or model) for help; redact and structure a stack trace so an assistant can be useful without a PDPL breach; run a differential diagnosis rather than accepting the first plausible cause; automate a regression hunt with `git bisect run`; and fix a race condition with a row lock plus a database constraint, proving the fix under concurrent load.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Construct a minimal, deterministic reproduction before diagnosing | LO4 |
| 4.2 | Prepare a stack trace and context for an assistant safely and effectively | LO4, LO5 |
| 4.3 | Run a differential diagnosis and reject a plausible-but-wrong AI hypothesis | LO4 |
| 4.4 | Automate a regression hunt with `git bisect run` | LO4, LO8 |
| 4.5 | Diagnose and fix a concurrency defect, proving the fix under load | LO4, LO3 |

## Technical Content

### 1. The debugging contract

| Step | Rule | Where the assistant helps | Where it misleads |
|---|---|---|---|
| **Reproduce** | A failure you cannot reproduce is a rumour | Generating a reproduction script from a bug report | It will happily "explain" a bug it cannot see, from the description alone |
| **Isolate** | Shrink until every remaining line is necessary | Suggesting what to remove next; writing the harness | It suggests fixes before isolation is done |
| **Hypothesise** | Name at least two candidate causes | Enumerating candidates you did not think of — its real strength | It ranks by plausibility, not by evidence |
| **Verify** | Confirm the mechanism, not just the symptom's absence | Writing the assertion that distinguishes the candidates | "It works now" is accepted as verification |

The failure mode to name out loud: **the assistant always answers.** Given a trace with no cause in it, it will still produce a fix, because producing text is what it does. A fix that makes the symptom disappear without a confirmed mechanism is the most expensive outcome in debugging — the defect is now invisible and still present.

### 2. Feeding a stack trace to an assistant, safely and well

Include: the full traceback with all frames; the source of the frames in *your* code (not the library internals); the exact versions of the relevant packages; what you expected; and what you have already ruled out. That last item removes most of the assistant's wasted guesses.

Exclude, always: personal data of any kind. A Rukhsa traceback routinely carries a national ID in a bound SQL parameter, an applicant name in a validation error, or a document object key in a storage exception. Under PDPL none of that may go to a third-party assistant. The practical answer is not "don't use the assistant" but **redact structurally**: log with a redacting formatter so traces never contain personal data in the first place, and keep a `scripts/redact_trace.py` for the cases that slip through.

A trace that has been through redaction still contains everything diagnostically useful — frames, line numbers, exception types, SQL shape — because the diagnosis was never in the values.

### 3. Differential diagnosis, and rejecting the confident wrong answer

Rukhsa's real Day-3 defect: finance reports that some applications have two `fee_assessments` rows and two SADAD references. The traceback available is an `IntegrityError` from a *different* code path, which is a red herring.

Give an assistant the symptom and it will typically propose, in order: (a) the front end submits twice on a double click; (b) a retry in the HTTP client; (c) a missing unique constraint. All three are plausible. Only evidence separates them:

| Candidate | Prediction if true | Test | Result |
|---|---|---|---|
| Double click in the UI | Two requests with the same idempotency key, milliseconds apart | Access log inspection | ✓ two requests, 40 ms apart |
| HTTP retry | Duplicate requests would carry a retry header | Header inspection | ✗ no retry headers |
| Missing constraint | Duplicates possible even from a single request path | Schema inspection | ✓ no unique constraint on `application_id` |

Both surviving candidates are *contributing* causes, and this is the lesson: the UI double-submit is the trigger, the missing constraint plus the read-then-write in the service is the defect. Fixing only the UI hides it until a retry or a load balancer replay produces the same interleaving. **Fix the invariant, not the trigger.**

### 4. The race condition, precisely

The generated `create_assessment` service does the natural thing: check whether an active assessment exists, and if not, create one. Under two concurrent requests the interleaving is:

```
T1: SELECT ... WHERE application_id = X AND active   -> 0 rows
T2: SELECT ... WHERE application_id = X AND active   -> 0 rows   (T1 has not committed)
T1: INSERT fee_assessment (X, 3780.00)               -> ok
T2: INSERT fee_assessment (X, 3780.00)               -> ok       <-- duplicate
T1: COMMIT      T2: COMMIT
```

This is a **read-then-write** across a transaction boundary with no serialisation. Two defences are needed and both belong in the fix:

- **A database constraint** — a partial unique index on `(application_id) WHERE active` — makes the duplicate *impossible* regardless of application logic. This is the invariant.
- **A row lock** — `SELECT ... FOR UPDATE` on the parent `applications` row before the check — makes the second transaction wait rather than fail, so the user sees a clean 409 rather than a 500 from a constraint violation. This is the ergonomics.

Constraint without lock is correct but ugly; lock without constraint is pleasant and still broken, because any future code path that forgets the lock reintroduces the defect. Measured on Rukhsa with 200 concurrent double-submits: 37 duplicates before, 0 after.

### 5. `git bisect run`: automating the regression hunt

When a defect appeared "sometime in the last three weeks," bisect finds the introducing commit in log₂(n) steps — 8 builds for 240 commits. The critical requirement is a **test script that exits 0 for good and 1 for bad**, and that is where an assistant genuinely helps: converting a manual reproduction into a deterministic script is a mechanical task it does well.

Two rules that make bisect work in practice: the script must be *robust to the commit being broken for unrelated reasons* (exit 125 to skip), and it must not depend on the current working tree — copy it out of the repository first, because bisect checks out old code over it.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Reproduce first, always.* The reproduction is the artefact; it becomes the regression test.
- *Fix the invariant, not the trigger.* Triggers multiply; invariants are finite.
- *Two candidates minimum.* One hypothesis is a belief, not a diagnosis.
- *Verify the mechanism.* "The symptom stopped" is not evidence the cause is gone.
- *Redact structurally.* Personal data should not be in the log to begin with.

**Common mistakes (each appears in the Lab 4 starter deliberately)**
1. Accepting the assistant's first diagnosis (the UI double-click) and shipping a front-end disable-on-submit — which hides the defect until a load-balancer replay reproduces it.
2. Adding the unique constraint without the row lock, converting duplicate rows into 500-level `IntegrityError` responses shown to citizens.
3. `except IntegrityError: pass` around the insert, which "fixes" the symptom by silently discarding the second assessment — and any other integrity failure with it.
4. Pasting a raw production traceback containing a national ID into the assistant.
5. A bisect script that depends on files in the working tree, so every bisect step tests the same code and the result is meaningless.
6. A "fix" verified with a single sequential request, which cannot fail and therefore proves nothing.

**Production considerations**
- Structured logging with correlation IDs is the prerequisite for all of this. Rukhsa attaches a request ID to every log line and returns it in the error response, so a citizen's complaint maps to a trace in one query.
- Keep the reproduction. Every concurrency fix in Rukhsa ships with its load-based regression test; without it the next refactor silently removes the lock.
- Alert on the invariant, not the symptom: a scheduled check counting applications with more than one active assessment catches a regression that no unit test would.

### 7. Real-world example walkthrough

Narrate this (5 minutes). A government payments integration produced roughly one duplicate charge per 4,000 transactions. The team's assistant, given the error report, proposed idempotency keys — a correct and excellent suggestion that took three weeks to implement. Duplicates continued at the same rate. The actual mechanism was a read-then-write in the reconciliation job, unrelated to the request path, which the assistant had never seen because nobody gave it the job's code; it had diagnosed the code it *was* shown. The eventual fix was eleven lines: a `FOR UPDATE` and a partial unique index. The idempotency keys were kept, because they were genuinely good, but the three weeks were spent because nobody asked "what evidence would distinguish this hypothesis from the alternatives?" before starting work.

## Code Examples

### Structured logging that cannot leak personal data

```python
# app/rukhsa/core/logging.py
"""Structured logging with a redacting processor.

WHY redaction is structural rather than manual: a traceback containing a national
id cannot be pasted into an assistant under PDPL, and the engineer under time
pressure at 02:00 is not a reliable redactor. Making the log incapable of
carrying personal data removes the decision from the incident entirely.
"""
from __future__ import annotations

import re
from typing import Any

import structlog

# Saudi national ids are 10 digits beginning 1 or 2. SADAD references are 15-20
# digits. Both are matched conservatively -- over-redaction is cheap, a leak is not.
_NATIONAL_ID = re.compile(r"\b[12]\d{9}\b")
_LONG_DIGITS = re.compile(r"\b\d{15,20}\b")

# Keys whose values are always personal data, whatever they contain.
_SENSITIVE_KEYS = frozenset({
    "national_id", "applicant_name", "business_name_ar", "business_name_en",
    "phone", "email", "object_key", "address",
})


def redact(_logger: Any, _method: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """Remove personal data from every log event before it is rendered."""
    for key in list(event_dict):
        if key in _SENSITIVE_KEYS:
            event_dict[key] = "[REDACTED]"
        elif isinstance(event_dict[key], str):
            value = _NATIONAL_ID.sub("[NID]", event_dict[key])
            event_dict[key] = _LONG_DIGITS.sub("[REF]", value)
    return event_dict


def configure_logging(debug: bool = False) -> None:
    """Install the Rukhsa logging pipeline.

    `merge_contextvars` carries the request id bound by the middleware into every
    log line in the request, which is what makes a citizen complaint traceable to
    a stack trace in one query.
    """
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            redact,                                   # before rendering, always
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer() if debug else structlog.processors.JSONRenderer(),
        ],
        cache_logger_on_first_use=True,
    )
```

### The race condition, and the fix that removes the invariant violation

```python
# app/rukhsa/services/assessment.py
"""Create the single active fee assessment for an application (SPEC-004 AC3, AC4).

WHY both a lock and a constraint: the lock serialises the concurrent path so the
loser gets a clean 409; the constraint makes the duplicate impossible even from a
code path that forgets the lock. Neither alone is sufficient -- the constraint
alone yields a 500 in the user's face, the lock alone is one refactor away from
being removed.
"""
from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.rukhsa.models.application import Application, ApplicationStatus
from app.rukhsa.models.fees import FeeAssessment
from app.rukhsa.services.fees import calculate_fee
from app.rukhsa.services.transitions import transition


class AssessmentAlreadyExists(Exception):
    """Raised when an active assessment already exists (SPEC-004: 409)."""


# ❌ AI-GENERATED — DO NOT SHIP.
# Defect: read-then-write with no serialisation. Two concurrent requests both see
# zero rows and both insert. Measured: 37 duplicates in 200 concurrent
# double-submits. The code is correct when read sequentially, which is exactly
# why review alone does not catch it.
#
# def create_assessment(session, application_id):
#     existing = session.scalar(
#         select(FeeAssessment).where(
#             FeeAssessment.application_id == application_id,
#             FeeAssessment.active.is_(True),
#         )
#     )
#     if existing:
#         raise AssessmentAlreadyExists()
#     assessment = FeeAssessment(application_id=application_id, ...)
#     session.add(assessment)
#     session.commit()
#     return assessment


def create_assessment(
    session: Session, application_id: uuid.UUID, base_fee_lookup: dict[str, "Decimal"]
) -> FeeAssessment:
    """Assess one application exactly once, safely under concurrency.

    The parent application row is locked FOR UPDATE before the existence check,
    so a second concurrent transaction blocks until the first commits and then
    observes the row it created. Paired with the partial unique index created in
    migration 9f3c2e77a104, a duplicate is impossible at the storage layer.
    """
    application = session.scalar(
        select(Application)
        .where(Application.id == application_id)
        .with_for_update()          # serialises concurrent assessment attempts
    )
    if application is None:
        raise LookupError("application_not_found")
    if application.status is not ApplicationStatus.ELIGIBLE:
        raise ValueError("invalid_status_for_assessment")

    existing = session.scalar(
        select(FeeAssessment).where(
            FeeAssessment.application_id == application_id,
            FeeAssessment.active.is_(True),
        )
    )
    if existing is not None:
        # The second request of a double-submit lands here and gets a clean 409.
        raise AssessmentAlreadyExists()

    breakdown = calculate_fee(
        base_fee=base_fee_lookup[application.activity_code],
        area_sqm=application.area_sqm,
    )
    assessment = FeeAssessment(
        application_id=application_id,
        base_fee=breakdown.base_fee,
        area_surcharge=breakdown.area_surcharge,
        service_fee=breakdown.service_fee,
        total=breakdown.total,
        active=True,
    )
    session.add(assessment)
    transition(application, ApplicationStatus.AWAITING_PAYMENT)
    session.commit()          # the lock is released here, not before
    return assessment
```

```sql
-- app/rukhsa/migrations/versions/9f3c2e77a104_active_assessment_unique.sql
-- WHY a PARTIAL unique index: SPEC-004 rule 6 makes assessments append-only, so
-- an application legitimately accumulates superseded rows. Uniqueness applies
-- only to the single active row, which a plain UNIQUE constraint cannot express.
CREATE UNIQUE INDEX CONCURRENTLY uq_fee_assessments_one_active
    ON fee_assessments (application_id)
    WHERE active;
```

### A bisect script the regression hunt can run unattended

```bash
#!/usr/bin/env bash
# scripts/bisect_duplicate_assessment.sh
# WHY this exists: converting a manual reproduction into an exit-code contract is
# what lets `git bisect run` search 240 commits in 8 builds instead of a person
# reading 240 diffs. Copy it OUTSIDE the repository before running, because
# bisect overwrites the working tree at every step.
#
#   cp scripts/bisect_duplicate_assessment.sh /tmp/
#   git bisect start HEAD v0.4.0
#   git bisect run /tmp/bisect_duplicate_assessment.sh
set -uo pipefail

# 125 tells bisect to SKIP a commit that cannot be evaluated (e.g. broken deps),
# rather than scoring it as good or bad and corrupting the search.
pip install -q -r requirements.txt || exit 125
alembic upgrade head            || exit 125

# The reproduction: 200 concurrent double-submits against one application.
python -m tests.load.duplicate_assessment --concurrency 200 --application-count 1
duplicates=$?

if [ "$duplicates" -eq 0 ]; then
  exit 0     # good commit: no duplicate rows produced
else
  exit 1     # bad commit: the defect is present
fi
```

## Hands-on Lab 4 — Reproduce, Bisect and Fix the Fee-Calculation Race

| | |
|---|---|
| **Objective** | Take a vague "finance sees duplicate charges" report to a proven root cause: build a deterministic reproduction, reject the assistant's first diagnosis, bisect to the introducing commit, and fix the invariant — 37 duplicates to 0 |
| **Duration** | 55 minutes |
| **Setup** | Lab 3 repository, PostgreSQL 16, `pip install structlog httpx`, seeded database, `git checkout lab4-start` (history contains 60 commits with the defect introduced at an unknown point) |

**Instructions & tasks**

1. *(8 min)* Read `docs/incidents/INC-0007.md` — the finance report, with no traceback. Before touching code, write down two candidate causes and the evidence that would distinguish them. Then ask the assistant for candidates and add any you missed to your list.
2. *(12 min)* Build the reproduction: `tests/load/duplicate_assessment.py` firing 200 concurrent `POST /applications/{id}/assessment` requests against one application with `httpx.AsyncClient`. It must exit non-zero when more than one active assessment row exists. Run it and record the duplicate count.
3. *(8 min)* Run the differential diagnosis table from the content section against your reproduction: check the access log for double requests, check for retry headers, check the schema for a unique constraint. Record which candidates survive in `LAB4_DIAGNOSIS.md`. **Explicitly record one assistant hypothesis you rejected and the evidence that rejected it.**
4. *(10 min)* Bisect: copy `scripts/bisect_duplicate_assessment.sh` to `/tmp`, then `git bisect start HEAD lab4-known-good` and `git bisect run /tmp/bisect_duplicate_assessment.sh`. Record the introducing commit SHA and read its diff — note that the diff looks entirely reasonable.
5. *(12 min)* Fix both layers: add `with_for_update()` to the parent read, and add the partial unique index migration. Re-run the reproduction and confirm 0 duplicates and that the losing requests return 409, not 500. Add the load reproduction to `tests/load/` as a permanent regression test.
6. *(5 min)* Commit: `fix(fees): serialise assessment creation with row lock + partial unique index (INC-0007, SPEC-004 AC4)`.

**Expected output**
```
$ python -m tests.load.duplicate_assessment --concurrency 200 --application-count 1
sent 200 requests: 200 x 201 Created
active fee_assessments for application: 38
DUPLICATES: 37
exit code 1

$ git bisect run /tmp/bisect_duplicate_assessment.sh
Bisecting: 29 revisions left to test after this (roughly 5 steps)
...
a41d0c8f9b2e is the first bad commit
    feat(fees): create fee assessment on eligibility (SPEC-004)
bisect found first bad commit in 8 steps

# ... after the fix ...
$ python -m tests.load.duplicate_assessment --concurrency 200 --application-count 1
sent 200 requests: 1 x 201 Created, 199 x 409 assessment_already_exists
active fee_assessments for application: 1
DUPLICATES: 0
exit code 0
```

**Acceptance criteria**
- The reproduction is deterministic: it produces duplicates on `lab4-start` and none after the fix, across three consecutive runs.
- `LAB4_DIAGNOSIS.md` names ≥ 2 candidates, the distinguishing evidence for each, and one rejected assistant hypothesis.
- Bisect identifies the introducing commit in ≤ 8 steps.
- Losing concurrent requests return **409**, not 500 — proving the lock, not only the constraint, is in place.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Reproduction never produces duplicates | Requests are serialised by a single worker | Run uvicorn with `--workers 4`, or add a small `asyncio.sleep` between the read and write to widen the window |
| `CREATE INDEX CONCURRENTLY` fails inside the migration | Alembic wraps migrations in a transaction | Set `op.get_context().autocommit_block()` or drop `CONCURRENTLY` for the lab database |
| Losing requests return 500 not 409 | Constraint added, lock missing | Add `.with_for_update()` to the parent application read |
| Bisect marks every commit bad | Script depends on files from the working tree | Copy the script outside the repository before starting bisect |

**Instructor notes.** Step 1 is where the module is won or lost: participants who go straight to the code will spend the lab fixing the front end. Insist on the two-candidate rule before anyone opens an editor. During step 4, point out that the "first bad commit" diff is clean, reviewed code — the defect is in what it *does not* say, which is why bisect exists. Fast finishers: have them add a scheduled invariant check (`SELECT application_id FROM fee_assessments WHERE active GROUP BY 1 HAVING count(*) > 1`) and wire it as a failing test, so a future regression is caught by the invariant rather than by finance.

## Mini Exercises

**Quiz (5 questions)**
1. Why is "the symptom stopped" insufficient verification? → the mechanism may be unchanged and merely hidden; it will recur under a different trigger.
2. What must a `git bisect run` script return to skip an unevaluable commit? → exit code **125**.
3. Why is a unique constraint alone an incomplete fix here? → the loser gets a 500 `IntegrityError` rather than a clean 409; the lock provides the ergonomics.
4. Name two things you must never include when sharing a Rukhsa traceback with a third-party assistant. → a national ID; an applicant name, document object key or any bound personal parameter.
5. In the interleaving shown, what is the defect class? → a read-then-write race across a transaction boundary with no serialisation.

**Debugging exercise.** Branch `lab4-swallowed` wraps the insert in `except IntegrityError: pass`. The duplicate rows disappear and the load test passes. Have participants find what else that handler now swallows (a foreign-key violation from a deleted application, and a check-constraint failure on `area_sqm`) and discuss why a passing test made the codebase less safe.

**Design exercise.** Design the alert that would have told Rukhsa's team about duplicates before finance did. Specify the query, the schedule, the threshold and who is paged — and justify why it watches the invariant rather than the error rate.

**Discussion questions.**
- The assistant's idempotency-key suggestion in the walkthrough was genuinely good engineering and cost three weeks. How do you distinguish "good advice" from "the right next action"?
- If structured redaction means your logs can never contain a national ID, have you made incident response harder? What do you use instead to link a complaint to a trace?

## Case Study — The Intermittent Claim Duplication at "Yaqeen" (يقين) Health Insurance

**Scenario.** "Yaqeen" (يقين), a Saudi health-insurance technology provider in Dammam, processes claim submissions from 340 clinics. Once or twice a week a claim is adjudicated twice, producing a duplicate payment to the provider. The defect resists diagnosis for two months: it never reproduces in staging, the logs show a single submission, and every engineer who reads the adjudication code finds it correct.

**Business context.** Duplicate adjudications average SAR 3,100 each and are recovered manually from providers, which damages relationships that took years to build. The regulator requires an explanation of any systematic payment error within 30 days of detection.

**Technical challenge.** The team fed the logs and code to an assistant repeatedly and received four different confident diagnoses across two months, each internally coherent, none correct. The real mechanism was a retry inside a message consumer: when adjudication took longer than the visibility timeout, the queue redelivered the message and a second consumer processed it concurrently. Nothing in the adjudication source was wrong; the defect lived in the interaction between a timeout value and a p99 latency that had grown slowly over a year.

**Constraints.** Claims processing cannot pause; the message broker is managed and its timeout is configurable but shared across six consumers; PDPL prohibits patient data leaving the environment, so raw messages cannot be shared with the assistant vendor; the regulator's 30-day clock has already started.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) stop asking for diagnoses and start building a reproduction — a load harness that pushes adjudication latency past the visibility timeout reproduces the defect in minutes, which reframes two months of speculation; (2) once reproducible, the assistant becomes useful again, because it is now reasoning about observed behaviour rather than imagining it; (3) fix the invariant — a unique constraint on `(claim_id, adjudication_round)` and a claimed-by lock — rather than the trigger (raising the timeout, which only moves the threshold); (4) redact structurally so the assistant can see traces at all under PDPL; (5) add an invariant monitor for double adjudications so the next occurrence is detected by the system rather than by a provider's complaint.

**Discussion questions.**
1. Four confident, coherent, wrong diagnoses in two months. What is the process defect here, and is it the assistant's or the team's?
2. Raising the visibility timeout would have stopped the symptom within a day. Under regulatory pressure, is that the wrong action — and how would you defend not taking it?
3. The p99 latency grew slowly over a year until it crossed the timeout. What monitoring would have made this a scheduled maintenance item instead of an incident?
4. PDPL prevented sharing raw messages. How much diagnostic value is actually lost by redaction, and what does that suggest about where diagnostic value lives?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Reproduction determinism | Method | duplicates on 3/3 runs before fix, 0/3 after | repeated harness runs |
| Duplicate assessments under load | Correctness | 0 (from 37) at concurrency 200 | `tests/load/duplicate_assessment.py` |
| Losing-request status code | Ergonomics | 409 (not 500) | load harness response tally |
| Bisect efficiency | Method | introducing commit found in ≤ 8 steps | `git bisect` log |
| Rejected AI hypotheses documented | Critical evaluation | ≥ 1 with distinguishing evidence | `LAB4_DIAGNOSIS.md` |

**Example benchmark table (filled during lab):**

| Stage | Concurrency | 201 responses | 409 responses | Active rows | Duplicates |
|---|---|---|---|---|---|
| `lab4-start` (generated) | 200 | 200 | 0 | 38 | 37 |
| Constraint only | 200 | 1 | 0 (199 × 500) | 1 | 0 |
| Constraint + `FOR UPDATE` | 200 | 1 | 199 | 1 | 0 |
| Regression re-run (post-fix) | 200 | 1 | 199 | 1 | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **The interleaving that creates the duplicate** — *Purpose:* make the race visible. *Elements:* two swimlanes T1/T2 with the SELECT/INSERT/COMMIT sequence, the unsafe window shaded red, and the same diagram with `FOR UPDATE` showing T2 blocked. *Style:* sequence diagram, before/after pair. *Designer description:* "Two vertical timelines with crossing arrows; a red band marks where both see zero rows."
2. **The debugging contract** — *Purpose:* the method card for the module. *Elements:* Reproduce → Isolate → Hypothesise → Verify, each annotated with where the assistant helps and where it misleads. *Style:* four-step card, printable, reused in the capstone rubric.
3. **`git bisect` search tree** — *Purpose:* show why 240 commits is 8 builds. *Elements:* a commit range halving across eight steps to a single highlighted commit. *Style:* binary-search tree, one accent colour.
4. **Structural redaction pipeline** — *Purpose:* show PDPL enforced in the log pipeline. *Elements:* a raw log event passing through the redact processor, with the national ID and object key replaced before rendering. *Style:* left-to-right pipeline with a shield icon at the redaction stage.

### Images (screenshots)
1. **The load harness reporting 37 duplicates** — *why:* the reproduction is the artefact; *content:* the terminal output with the duplicate count and exit code.
2. **`git bisect run` converging** — *why:* participants rarely see bisect automated; *content:* the eight steps and the "first bad commit" line.
3. **A redacted versus unredacted traceback side by side** — *why:* shows that diagnostic value survives redaction; *content:* identical frames, values replaced.

### Simulations
1. **The plausible wrong diagnosis** — *Setup:* the room is given the incident report and asked to accept the assistant's first answer, then shown the reproduction disproving it. *Expected behaviour:* most of the room had already started fixing the front end. *Learning objective:* plausibility is the trap, evidence is the exit.
2. **Constraint-only fix** — *Setup:* branch `lab4-constraint-only`. *Expected behaviour:* zero duplicates and 199 error responses shown to citizens. *Learning objective:* correctness and ergonomics are separate obligations.

### Interactive Activities
- **Two-candidate drill (10 min):** five one-line bug reports; teams must produce two candidate causes and the distinguishing evidence for each in ninety seconds per report.
- **Trace triage relay (12 min):** three tracebacks, one containing personal data; teams must redact, structure and produce the prompt they would send — the one they should refuse to send is the point.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `docs/incidents/INC-0007.md` | Instructor-authored finance report | Markdown | 1 page | The vague starting point — deliberately traceback-free |
| `lab4-start` commit range | Course repository | Git history | 60 commits | The bisect search space |
| `tests/load/duplicate_assessment.py` | Built by participants in step 2 | Python | ~70 lines | Reproduction, then permanent regression test |

### Demo Requirements
- **Instructor demo (7 minutes):** run the load harness live to produce 37 duplicates, paste the incident report into the assistant on the projector and read its confident front-end diagnosis aloud, then run the schema check that disproves it. The gap between the fluency of the answer and the evidence is the memory participants keep.

---

# Module 5 — Code Review and the Security-First Principle
## مراجعة الكود ومبدأ "الأمن أولاً"

## Module Overview

**Purpose.** This module covers catalogue module 4 and delivers the **HARDEN** step. Generated code is not more malicious than hand-written code; it is more *conventional*, and the conventions in its training data include a great many insecure patterns that were once normal. Participants map the OWASP Top 10 onto concretely generated Rukhsa snippets, then build the automated gate — bandit, Semgrep with project-specific rules, secret scanning, dependency audit — that stops those classes from ever reaching `main` again.

**Business relevance.** A commercial-licensing portal holds national IDs, business ownership records and payment references, and is internet-facing. Under Saudi PDPL a breach involving personal data carries regulatory and reputational consequences that dwarf any delivery saving, and public-sector security assessments now explicitly probe for injection and access-control defects. "Security by design" is the catalogue's phrasing and it is exact: the security properties must be constraints on generation, not findings from a penetration test three weeks before launch.

**Industry use cases.**
- A government portal fails a pre-launch security assessment on an over-broad CORS policy and an IDOR that generated code introduced in a single sprint.
- A bank's secret-scanning gate catches an API key committed inside a generated example configuration before it reaches a public mirror.
- A team discovers an AI-suggested dependency that does not exist on the index — and learns the name has since been registered by someone else.

**Expected competencies.** After this module a participant can apply an AI-specific review checklist; recognise the six OWASP-mapped defect classes that generated code produces most often; write a Semgrep rule enforcing a project convention; configure bandit, gitleaks and pip-audit as a blocking CI gate; and assess an AI-suggested dependency for existence, provenance and supply-chain risk.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Apply a review checklist specific to AI-generated changes | LO5, LO1 |
| 5.2 | Map OWASP Top 10 categories to concrete defects in generated code and remediate them | LO5 |
| 5.3 | Configure SAST (bandit, Semgrep) and secret scanning as a blocking CI gate | LO5, LO8 |
| 5.4 | Write a project-specific Semgrep rule enforcing an architectural convention | LO5, LO3 |
| 5.5 | Assess AI-suggested dependencies for existence and supply-chain risk | LO5 |

## Technical Content

### 1. The AI-diff review checklist

An ordinary review checklist assumes a human author with intent. An AI-diff checklist assumes a fluent author with none, and targets the specific ways that goes wrong.

| # | Check | Why it is AI-specific |
|---|---|---|
| 1 | Does every changed line trace to a requirement in the spec? | Generated diffs contain unrequested "improvements" |
| 2 | Does every referenced API and package exist, at the pinned version? | Hallucinated APIs and phantom packages |
| 3 | Is any string interpolated into SQL, a shell command, a path or HTML? | Concatenation is the most common pattern in training data |
| 4 | Is every resource access authorised against the *caller*, not just authenticated? | Assistants generate authentication readily and authorisation rarely |
| 5 | Are secrets absent, and is every configuration value required rather than defaulted? | Literal fallback secrets are a default habit |
| 6 | Does the error path reveal only what the spec permits? | Generated handlers return internal detail helpfully |
| 7 | Is personal data absent from logs, URLs and responses? | The assistant does not know your PDPL classification unless told |
| 8 | Do the tests in this diff assert values, and were they written from the spec? | Tests generated alongside code encode the same misunderstanding |

Checks 1, 2 and 8 are the ones that do not appear on a conventional checklist, and they catch defects a conventional review would pass.

### 2. OWASP Top 10 mapped to generated Rukhsa code

Each row below corresponds to a snippet planted in the Lab 5 starter branch. This is the gallery participants walk before they fix anything.

| OWASP (2021) | What the assistant generated | Consequence in Rukhsa | Fix |
|---|---|---|---|
| **A01 Broken Access Control** | `GET /applications/{id}` returns the row if it exists, with no ownership check | Any authenticated citizen reads any other citizen's application, including `national_id_hash` and documents | Filter by the caller's subject in the query, not after it |
| **A02 Cryptographic Failures** | `national_id` stored plaintext "for lookup convenience" | PDPL breach on any database disclosure | Salted SHA-256 digest; index the digest |
| **A03 Injection** | `f"SELECT ... WHERE reference = '{ref}'"` in a search helper | Data disclosure or destruction from a crafted reference | Bound parameters via `text(...).bindparams()` or the ORM |
| **A05 Security Misconfiguration** | `allow_origins=["*"]` with `allow_credentials=True` | Any site can make credentialed calls as a logged-in citizen | Explicit origin list from settings; never `*` with credentials |
| **A07 Identification & Auth Failures** | JWT decoded with `verify_signature: False` to "make tests pass" | Forged tokens accepted in production | Verify signature and audience; fix the test, not the verifier |
| **A09 Logging Failures** | `logger.info(f"application for {national_id}")` | Personal data in log aggregation, indefinitely retained | Structural redaction (M4) plus a Semgrep rule banning the pattern |

Two of these deserve emphasis because they are the least visible. The **A05 CORS pair** is dangerous only in combination — `allow_origins=["*"]` alone is merely permissive; with `allow_credentials=True` it is an account-takeover primitive, and browsers reject the combination precisely because it is so bad. And **A07's disabled signature verification** is the archetype of a defect introduced to make something pass: the assistant was asked to fix a failing test and chose the shortest path.

### 3. SAST, secret scanning and dependency audit as a gate

Four tools, four distinct jobs, all blocking:

| Tool | Finds | Runs in | Rukhsa gate |
|---|---|---|---|
| `bandit` | Python-specific insecure patterns (`assert` in production paths, `subprocess` with shell, weak hashes, hardcoded passwords) | 8 s | Fails on HIGH or MEDIUM |
| `semgrep` | Semantic patterns including *your* conventions | 46 s | Fails on any rule in `.semgrep/rukhsa.yml` |
| `gitleaks` | Secrets in the diff and in history | 4 s | Fails on any finding |
| `pip-audit` | Known CVEs in pinned dependencies | 9 s | Fails on HIGH; warns on MEDIUM |

The distinction worth teaching: bandit encodes *general* Python security knowledge; Semgrep is where you encode what is true about *this* codebase — that money is `Decimal`, that routers never contain queries, that `national_id` never appears in an f-string. Generated code violates project conventions far more often than it violates general security rules, because the conventions are not in the training data. **Every convention in `CLAUDE.md` that matters should have a Semgrep rule behind it**, because an instruction file is guidance and a CI rule is a control.

Baseline on the Rukhsa Lab 5 starter: bandit reports 6 findings (2 HIGH, 4 MEDIUM), Semgrep 4, gitleaks 1, pip-audit 1 HIGH plus 1 package that does not resolve at all. After remediation: 0 across all four.

### 4. Supply chain: hallucinated packages and slopsquatting

An assistant asked to add JWT handling to Rukhsa suggested `fastapi-jwt-auth-pro`. The package does not exist. That is normally harmless — `pip install` fails and you move on — but the failure mode has been weaponised. Because assistants hallucinate the *same* plausible names repeatedly, an attacker can register those names and wait; the technique is called **slopsquatting**, distinct from classic typosquatting in that the victim never mistyped anything. The assistant suggested a name, the name resolved, and the developer had no reason to doubt it.

The controls are unglamorous and effective:

1. **Verify every new dependency at review time** — check the index page, the source repository, the release history and the download pattern. A package with one release from last week and no repository is a finding, not a dependency.
2. **Pin with hashes.** `pip-compile --generate-hashes` produces a lock file where a substituted artefact fails installation. This also defeats a compromised release of a legitimate package.
3. **Justify new dependencies in the PR description.** "The assistant suggested it" is not a justification; "we need RFC 7519 validation and `pyjwt` is the maintained implementation" is.
4. **Audit continuously**, not once — `pip-audit` in CI catches a CVE published after you merged.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Security properties are constraints on generation, not findings from a test.* Put them in the instruction file and enforce them with rules.
- *Authentication is not authorisation.* Every resource access must be scoped to the caller in the query.
- *Encode your conventions as rules.* Guidance drifts; a failing pipeline does not.
- *A dependency is a trust decision.* Someone must own it, and "the assistant suggested it" identifies nobody.
- *The secure default is the one you get by doing nothing.* No fallback secrets, no permissive CORS, no `verify=False`.

**Common mistakes (each appears in the Lab 5 starter deliberately)**
1. An f-string SQL query in the reference-search helper — the injection point.
2. `allow_origins=["*"]` combined with `allow_credentials=True` in the CORS middleware.
3. `jwt.decode(token, options={"verify_signature": False})`, introduced to make a test pass.
4. `SADAD_API_KEY = "sk_live_7a3f..."` committed in `app/rukhsa/integrations/sadad.py`.
5. `GET /applications/{id}` with authentication but no ownership check — the IDOR.
6. `pip install fastapi-jwt-auth-pro` in the generated setup documentation — a package that does not exist.
7. A generated `except Exception as e: return {"error": str(e)}` handler returning the raw SQL statement, including bound parameter values, to the caller.

**Production considerations**
- Run SAST on the pull request, not on a schedule. A finding that arrives after merge is a ticket; a finding that blocks a merge is a control.
- Maintain a triaged baseline for legacy findings so the gate stays at zero for *new* code. A gate that always fails is a gate everyone bypasses.
- Scan git *history*, not only the diff. A secret rotated but not purged is still disclosed, and `gitleaks detect` on the full history is the only way to know.
- Keep the Semgrep rule set in the repository under CODEOWNERS. It is executable architecture policy.

### 6. Real-world example walkthrough

Narrate this (5 minutes). A municipality's e-services team shipped a document-download endpoint generated in an afternoon. It authenticated the caller correctly, checked that the document existed, and streamed it — and it never checked that the document belonged to the caller. Any logged-in citizen could enumerate integer document IDs and download other citizens' lease contracts and identity documents. Nobody had been careless: the endpoint was reviewed by two engineers, and the missing check is not visible as an *absence* unless you are specifically looking for it. It was found by a security assessment eleven weeks after launch, and the disclosure notification obligation under PDPL was the most expensive part. The team's remediation was structural: an ownership predicate in the repository layer that every resource query must call, and a Semgrep rule that fails any query against `documents` which does not include it. Check 4 on the AI-diff checklist exists because of endpoints exactly like this one.

## Code Examples

### The vulnerable generated code, and the hardened version

```python
# app/rukhsa/api/applications.py
"""Application read endpoints (SPEC-002).

WHY the ownership predicate lives in the query rather than in a post-fetch check:
an `if` after the fetch can be removed by a later refactor without any test
failing, and it still loads the row (and any relationship) into memory before
deciding. Scoping the query means an unauthorised row is never materialised, and
the Semgrep rule below can prove structurally that the scope was applied.
"""
from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.rukhsa.api.deps import CurrentCitizen, get_session
from app.rukhsa.models.application import Application
from app.rukhsa.schemas.application import ApplicationRead

router = APIRouter(prefix="/applications", tags=["applications"])


# ❌ AI-GENERATED — DO NOT SHIP.
# Defect 1 (OWASP A01, IDOR): authenticated but not authorised. Any citizen can
#   read any application by id, including the national_id_hash and documents.
# Defect 2 (OWASP A03, injection): the reference is interpolated into SQL, so
#   `?reference=' OR '1'='1` returns every row in the table.
# Defect 3 (OWASP A09): the exception handler returns the raw database error,
#   which contains the statement and its bound parameters.
#
# @router.get("/{application_id}")
# def get_application(application_id: str, session: Session = Depends(get_session)):
#     try:
#         row = session.execute(
#             text(f"SELECT * FROM applications WHERE id = '{application_id}'")
#         ).first()
#         return dict(row._mapping)
#     except Exception as e:
#         return {"error": str(e)}


@router.get("/{application_id}", response_model=ApplicationRead)
def get_application(
    application_id: uuid.UUID,            # parsed and validated before any query
    citizen: CurrentCitizen,
    session: Session = Depends(get_session),
) -> Application:
    """Return one application belonging to the calling citizen.

    Returns 404 (not 403) for an application owned by someone else: revealing
    that a reference exists but belongs to another citizen is itself a small
    disclosure, and enumeration is cheaper when the two cases differ.
    """
    stmt = select(Application).where(
        Application.id == application_id,
        # The ownership predicate. Both conditions are part of the query, so an
        # unauthorised row is never loaded.
        Application.national_id_hash == citizen.national_id_hash,
    )
    application = session.scalar(stmt)
    if application is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="application_not_found")
    return application


@router.get("", response_model=list[ApplicationRead])
def search_applications(
    reference: str,
    citizen: CurrentCitizen,
    session: Session = Depends(get_session),
) -> list[Application]:
    """Search the caller's own applications by reference.

    Raw SQL is retained here deliberately to demonstrate the correct form: the
    value is BOUND, never interpolated, so a crafted reference is data and can
    never become syntax.
    """
    stmt = text(
        "SELECT * FROM applications "
        "WHERE reference = :reference AND national_id_hash = :owner"
    ).bindparams(reference=reference, owner=citizen.national_id_hash)
    rows = session.execute(stmt).mappings().all()
    return [Application(**dict(row)) for row in rows]
```

### Project-specific Semgrep rules — conventions as controls

```yaml
# .semgrep/rukhsa.yml
# WHY project rules rather than only the community rule set: generated code
# violates THIS codebase's conventions far more often than it violates general
# security rules, because the conventions are not in any training data. Each rule
# below corresponds to a line in CLAUDE.md, turning guidance into a control.
rules:
  - id: rukhsa-no-fstring-sql
    languages: [python]
    severity: ERROR
    message: >-
      SQL built by string interpolation (OWASP A03). Use bound parameters:
      text("... WHERE x = :x").bindparams(x=value).
    patterns:
      - pattern-either:
          - pattern: text(f"...")
          - pattern: $SESSION.execute(f"...")
          - pattern: $SESSION.execute("..." % $ARGS)

  - id: rukhsa-no-wildcard-cors
    languages: [python]
    severity: ERROR
    message: >-
      allow_origins=["*"] is forbidden (OWASP A05). Read the explicit origin list
      from settings.cors_allowed_origins.
    pattern: |
      CORSMiddleware(..., allow_origins=["*"], ...)

  - id: rukhsa-no-unverified-jwt
    languages: [python]
    severity: ERROR
    message: >-
      JWT signature verification disabled (OWASP A07). Fix the test fixture, not
      the verifier.
    pattern: jwt.decode(..., options={..., "verify_signature": False, ...})


  - id: rukhsa-no-personal-data-in-logs
    languages: [python]
    severity: ERROR
    message: >-
      Personal data must not be interpolated into a log message (PDPL, OWASP
      A09). Log the application id; the redacting processor handles the rest.
    patterns:
      - pattern-either:
          - pattern: $LOG.$LEVEL(f"...{$X.national_id}...")
          - pattern: $LOG.$LEVEL(f"...{$X.applicant_name}...")
          - pattern: $LOG.$LEVEL(..., national_id=$X, ...)

```

### The blocking security job

```yaml
# .github/workflows/security.yml
# WHY a separate workflow from the test suite: security findings must block the
# merge independently of whether tests pass, and the job must run on the pull
# request rather than after merge -- a finding that arrives post-merge is a
# ticket, while one that blocks a merge is a control.
name: security

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  static-analysis:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0          # gitleaks needs full history, not just the diff

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - name: Install security tooling (pinned)
        run: pip install bandit==1.7.9 semgrep==1.85.0 pip-audit==2.7.3

      # Python-specific insecure patterns. -ll = report MEDIUM and above; the
      # exit code is non-zero on any finding, which is what blocks the merge.
      - name: bandit
        run: bandit -r app/rukhsa -ll -f txt --exit-zero-on-skipped false

      # Project conventions (.semgrep/rukhsa.yml) plus the community Python and
      # OWASP Top-10 rule packs.
      - name: semgrep
        run: |
          semgrep --error --metrics=off \
            --config .semgrep/rukhsa.yml \
            --config p/python \
            --config p/owasp-top-ten

      # Known CVEs in pinned dependencies. Runs against the hashed lock file, so
      # it audits exactly what will be installed.
      - name: pip-audit
        run: pip-audit --requirement requirements.lock --strict

      - name: gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # Supply-chain check for AI-suggested dependencies: every requirement must
      # resolve on the index AND be present in the reviewed allow-list.
      - name: verify dependency provenance
        run: python scripts/verify_dependencies.py --requirements requirements.in
```

## Hands-on Lab 5 — Harden the Generated Rukhsa Code

| | |
|---|---|
| **Objective** | Find and remediate seven planted vulnerabilities in generated Rukhsa code, write two project-specific Semgrep rules, and stand up the blocking security job — from 12 findings to 0 |
| **Duration** | 50 minutes |
| **Setup** | Lab 4 repository, `pip install bandit==1.7.9 semgrep==1.85.0 pip-audit==2.7.3`, `gitleaks` binary on PATH, `git checkout lab5-start` |

**Instructions & tasks**

1. *(6 min)* Run the four tools locally and record the baseline in `LAB5_FINDINGS.md`: `bandit -r app/rukhsa -ll`, `semgrep --config p/python --config p/owasp-top-ten`, `gitleaks detect`, `pip-audit -r requirements.in`. Expect 6 + 4 + 1 + 1 findings.
2. *(8 min)* Walk the OWASP mapping table against the actual code. For each of the six categories, open the offending file and write one sentence in `LAB5_FINDINGS.md` describing the *consequence for a citizen* — not the tool's message. This is the review skill; the tools only point.
3. *(12 min)* Remediate A01 (ownership predicate in the query), A03 (bound parameters) and A05 (explicit CORS origins from settings). Re-run the tools after each fix rather than at the end, so you see which finding each change clears.
4. *(10 min)* Remediate A02 (hash the national ID), A07 (restore signature verification and fix the *test fixture* that motivated disabling it) and A09 (remove personal data from the log call). Rotate and remove the committed SADAD key, then run `gitleaks detect --log-opts="--all"` and observe that history still contains it — discuss what rotation actually requires.
5. *(9 min)* Write two Semgrep rules of your own beyond those provided — one security rule and one convention rule from your `CLAUDE.md` — and prove each fires by writing a violating line, then deleting it. Add `.github/workflows/security.yml` and push.
6. *(5 min)* Verify the phantom dependency: attempt `pip download fastapi-jwt-auth-pro`, record the result, replace it with `pyjwt`, and commit: `fix(security): remediate OWASP A01/A02/A03/A05/A07/A09 in generated code`.

**Expected output**
```
$ bandit -r app/rukhsa -ll
Run started: 2026-03-10 09:12:44
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'sk_live_7a3f...'
   Severity: High   Location: app/rukhsa/integrations/sadad.py:14
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector
   Severity: Medium Location: app/rukhsa/api/applications.py:38
Total issues (by severity): High: 2  Medium: 4  Low: 0

$ semgrep --config .semgrep/rukhsa.yml --config p/owasp-top-ten
  rukhsa-no-fstring-sql            app/rukhsa/api/applications.py:38
  rukhsa-no-wildcard-cors          app/rukhsa/main.py:27
  rukhsa-no-unverified-jwt         app/rukhsa/api/deps.py:52
  rukhsa-no-personal-data-in-logs  app/rukhsa/services/application.py:71
Findings: 4

$ pip download fastapi-jwt-auth-pro
ERROR: Could not find a version that satisfies the requirement fastapi-jwt-auth-pro
ERROR: No matching distribution found for fastapi-jwt-auth-pro

# ... after remediation ...
$ bandit -r app/rukhsa -ll && semgrep --error --config .semgrep/rukhsa.yml \
    --config p/owasp-top-ten && gitleaks detect --no-banner && pip-audit -r requirements.lock
No issues identified.
Findings: 0
no leaks found
No known vulnerabilities found
```

**Acceptance criteria**
- All four tools report zero findings on the working tree; the security workflow runs green on the pull request.
- `LAB5_FINDINGS.md` describes the citizen-facing consequence of all six OWASP categories, not the tool messages.
- Two participant-written Semgrep rules exist and are demonstrated firing.
- The IDOR fix scopes the **query**, not a post-fetch `if`; the 409/404 choice is justified in a comment.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Semgrep reports zero findings on obviously bad code | Rule file path wrong, or `--config` pointing at a directory without `.yml` | Run `semgrep --validate --config .semgrep/rukhsa.yml`; check the `languages:` key |
| gitleaks passes but the key is still in history | Scanning the working tree only | `gitleaks detect --log-opts="--all"`; rotation requires a new key **and** history rewrite or acceptance |
| bandit flags `assert` in test files | Tests legitimately use `assert` | Exclude `tests/` with `-x tests` — never disable B101 globally |
| `pip-audit` fails on a transitive CVE with no fix available | Upstream has not released a patch | Document in `SECURITY.md` with a compensating control and a review date; do not silently ignore |

**Instructor notes.** Step 2 is the module's centre: a participant who can only repeat the tool's message has not learned review, they have learned to run a tool. Insist on the citizen-facing sentence. During step 4 the gitleaks history discovery reliably produces a useful argument about whether rotation is enough — let it run, then land the point that rotation is mandatory and history rewriting is a separate, harder decision. Fast finishers: have them add the `p/secrets` Semgrep pack and a `detect-secrets` pre-commit hook, then attempt to commit a fake key and watch it blocked locally rather than in CI.

## Mini Exercises

**Quiz (5 questions)**
1. Why is `allow_origins=["*"]` with `allow_credentials=True` worse than either alone? → it permits any site to make credentialed cross-origin calls as the logged-in user; browsers reject the combination for this reason.
2. What distinguishes slopsquatting from typosquatting? → the developer never mistyped; an assistant suggested a plausible name an attacker had pre-registered.
3. Why scope authorisation in the query rather than after the fetch? → the unauthorised row is never loaded, and a later refactor cannot silently drop an `if` without a structural rule noticing.
4. What does Semgrep give you that bandit cannot? → enforcement of *your* project conventions, which are absent from any general rule set.
5. Is rotating a leaked key sufficient? → no — it is necessary; the value remains in git history until purged or formally accepted.

**Debugging exercise.** Branch `lab5-verify-false` disabled JWT signature verification so an expired fixture token would pass in tests. All tests are green and the API accepts forged tokens. Ask participants to fix the *test fixture* instead, and to write the Semgrep rule that would have blocked the shortcut.

**Design exercise.** Write the five-line "new dependency" section for Rukhsa's pull-request template: what a reviewer must verify before approving a PR that adds a package, phrased so that "the assistant suggested it" cannot satisfy it.

**Discussion questions.**
- Your SAST gate blocks a release for a MEDIUM finding on a code path that is unreachable in production. Do you ship? What makes your answer a policy rather than an improvisation?
- If every convention in `CLAUDE.md` should have a Semgrep rule behind it, what is the instruction file actually for?

## Case Study — The Pre-Launch Assessment at "Hisn" (حصن) Security Services

**Scenario.** "Hisn" (حصن), a Riyadh-based managed security provider, runs pre-launch assessments for Saudi government digital services. Over eighteen months its assessors observed a change in what they find: injection and access-control defects, long in decline, rose sharply in systems built by teams that had recently adopted coding assistants — while code-style and complexity findings fell. One portal assessment produced 23 findings, of which 19 traced to code committed in a single six-week sprint.

**Business context.** A failed pre-launch assessment delays a service launch by six to ten weeks and requires re-assessment at the client's cost. Hisn's clients increasingly ask a question the firm cannot answer well: "how do we prevent these instead of finding them?"

**Technical challenge.** Hisn's assessment methodology is manual, sample-based and post-hoc. It scales to a release, not to a team generating thirty pull requests a day. The firm must decide whether to build a productised "AI-assisted development assurance" offering — shifting from finding defects to installing controls — and what such an offering would actually contain that a free rule pack does not.

**Constraints.** Assessors cannot access client source repositories continuously under most contracts; several clients' code cannot leave their environment at all; Hisn's revenue model is priced per assessment, so a control that reduces findings reduces billable remediation work; the National Cybersecurity Authority's controls framework must be mapped to whatever is proposed.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) characterise the shift with data — which OWASP categories rose, in which codebases, correlated with what adoption date; that evidence is the product; (2) shift left with controls the client runs themselves: a curated Semgrep rule set mapped to the client's architecture, a secret-scanning gate, a dependency-provenance check; (3) sell the *rule set and the review methodology*, not the scan — a rule pack encoding a client's conventions cannot be downloaded free because it does not exist yet; (4) address the incentive conflict openly — reprice from per-assessment to a retained assurance model, or the firm will always profit from finding rather than preventing; (5) map every control to the NCA framework so procurement can buy it.

**Discussion questions.**
1. Style findings fell while injection findings rose. What does that pattern tell you about what assistants are good and bad at, and does it match your own experience?
2. Hisn profits from remediation work. How much should that shape your reading of their recommendations — and how would you structure a contract that removes the conflict?
3. A curated rule set encoding a client's conventions is the proposed product. Who at the client must contribute to it, and what happens to it when their architecture changes?
4. Several clients forbid code leaving their environment. Does that constrain the offering, or is it actually the reason the offering must be a control rather than a scan?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| bandit HIGH/MEDIUM findings | Security | 0 (from 2 HIGH / 4 MEDIUM) | `bandit -r app/rukhsa -ll` |
| Semgrep findings | Convention + security | 0 (from 4) | `semgrep --error` with the project rule set |
| Secrets in working tree | Security | 0 (from 1) | `gitleaks detect` |
| Dependencies failing provenance | Supply chain | 0 (from 1 phantom, 1 CVE) | `pip-audit` + `verify_dependencies.py` |
| Participant-authored Semgrep rules | Control ownership | ≥ 2, each demonstrated firing | rule file + demonstration |

**Example benchmark table (filled during lab):**

| Tool | Baseline | After A01/A03/A05 | After A02/A07/A09 | Final | Runtime |
|---|---|---|---|---|---|
| bandit | 2 HIGH, 4 MEDIUM | 2 HIGH, 2 MEDIUM | 0 | 0 | 8 s |
| semgrep | 4 | 2 | 0 | 0 | 46 s |
| gitleaks | 1 | 1 | 0 | 0 | 4 s |
| pip-audit | 1 HIGH + 1 unresolvable | 1 HIGH + 1 unresolvable | 0 | 0 | 9 s |

## Required Visuals and Training Assets

### Diagrams
1. **OWASP Top 10 mapped to generated snippets** — *Purpose:* the module's gallery in one image. *Elements:* six OWASP categories, each with a two-line generated snippet and its Rukhsa consequence. *Style:* six-panel grid, red snippet / green fix on hover in the slide version. *Designer description:* "A wall of six code cards, each with a red seal and a citizen-impact caption."
2. **The five-gate pipeline, security highlighted** — *Purpose:* place SAST in the merge path. *Elements:* lint → type → security → test → e2e, with the security gate expanded into bandit/Semgrep/gitleaks/pip-audit and their runtimes. *Style:* horizontal pipeline, one gate exploded.
3. **IDOR: post-fetch check versus scoped query** — *Purpose:* show why the fix location matters. *Elements:* two data-flow paths, one loading the row then rejecting, one never loading it. *Style:* side-by-side flow with the loaded-row path shaded as exposure.
4. **Slopsquatting attack chain** — *Purpose:* make an abstract risk concrete. *Elements:* assistant suggests a name → attacker has registered it → `pip install` succeeds → post-install script executes. *Style:* four-step chain with the branch point where verification would break it.

### Images (screenshots)
1. **bandit output with the hardcoded SADAD key** — *why:* participants must recognise the B105 signature; *content:* the HIGH finding with file and line.
2. **A blocked pull request** — *why:* the gate as a control, not a report; *content:* GitHub's merge button disabled with the failing security check listed.
3. **gitleaks finding a key in history after rotation** — *why:* the rotation-is-not-removal lesson; *content:* the commit SHA and date of a key rotated weeks earlier.

### Simulations
1. **Enumerate the portal** — *Setup:* the `lab5-start` API with the IDOR present and 40 seeded applications. *Expected behaviour:* a five-line script retrieves every application, including other citizens' data. *Learning objective:* an absent check is invisible in review and trivial to exploit.
2. **The helpful error handler** — *Setup:* the generated `except Exception: return {"error": str(e)}` handler with a crafted request. *Expected behaviour:* the response contains the SQL statement and bound parameters. *Learning objective:* error paths are an attack surface.

### Interactive Activities
- **Vulnerability gallery walk (15 min):** seven printed generated snippets on the wall; teams tag each with its OWASP category and its citizen-facing consequence, then defend disagreements.
- **Write-a-rule clinic (12 min):** each team converts one line of their `CLAUDE.md` into a Semgrep rule and demonstrates it firing on a violating line they write themselves.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `lab5-start` branch | Course repository | Git branch | 7 planted vulnerabilities | The remediation target |
| `.semgrep/rukhsa.yml` | Course repository, extended by participants | YAML | 6 rules → ≥ 8 | Conventions as controls |
| `requirements.in` / `requirements.lock` | `pip-compile --generate-hashes` | Text | 41 direct / 96 pinned | Supply-chain exercise, including the phantom package |

### Demo Requirements
- **Instructor demo (8 minutes):** exploit the IDOR live on the projector with a five-line script that dumps forty citizens' applications, then apply the one-line ownership predicate and run the same script to a wall of 404s. Follow immediately with `pip download fastapi-jwt-auth-pro` failing, and explain what would have happened had the name resolved.

---

# Module 6 — Generating Automated Tests: Unit, Integration, and End-to-End
## توليد الاختبارات الآلية

## Module Overview

**Purpose.** This module covers catalogue module 5 and delivers the **TEST** step. Assistants generate tests faster than any other artefact and generate *weak* tests more reliably than any other artefact: tests that assert nothing, tests that mock the code under test, tests written from the implementation rather than the specification. Participants learn the test pyramid, then learn to *prove* their generated tests have value using mutation testing — raising Rukhsa's mutation score from 41% to above 70% — before adding property-based tests for the fee invariants and Playwright end-to-end coverage of the licence-issuance journey.

**Business relevance.** The catalogue promises that automated test generation "significantly reduces QA cycles." It does — but only if the tests detect defects. A suite with 88% coverage and a 41% mutation score reduces QA cycles by giving false confidence, which is worse than no suite at all because it removes the manual testing that was catching things. For a licensing portal where a fee error is a financial defect and an issuance error is a legal one, the question "do these tests actually assert anything?" is a governance question, not a craft preference.

**Industry use cases.**
- A team's coverage rises from 40% to 85% in a week of generated tests, and its escaped-defect rate does not move — mutation testing explains why.
- A payments service needs confidence in rounding behaviour across the full input domain, which example-based tests cannot provide.
- A government service must demonstrate to an assurance reviewer that the end-to-end citizen journey is tested, not just the units.

**Expected competencies.** After this module a participant can size a test suite against the pyramid; recognise and repair the four weak-test patterns assistants produce; write integration tests against a real PostgreSQL with transactional isolation; express invariants as Hypothesis properties; interpret a mutation report and use it to strengthen assertions; and automate a multi-step browser journey with Playwright.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Size and structure a test suite against the pyramid, with justified proportions | LO6 |
| 6.2 | Identify and repair weak generated tests (vacuous, tautological, over-mocked, implementation-derived) | LO6, LO1 |
| 6.3 | Write integration tests against a real database with transactional isolation | LO6 |
| 6.4 | Express business invariants as property-based tests with Hypothesis | LO6, LO3 |
| 6.5 | Use mutation testing to prove assertion strength, and treat coverage as a floor | LO6 |
| 6.6 | Automate the licence-issuance journey end-to-end with Playwright | LO6, LO8 |

## Technical Content

### 1. The pyramid, sized for Rukhsa

| Layer | Count | Runtime | What it proves | What it cannot |
|---|---|---|---|---|
| **Unit** | 94 | 3.4 s | Rules in isolation — fee arithmetic, state transitions, eligibility predicates | That the pieces are wired together |
| **Integration** | 17 | 22 s | Real SQL against real PostgreSQL — constraints, locks, transactions, query counts | That a citizen can complete the journey |
| **End-to-end** | 7 | 2 m 48 s | The browser journey through the real stack | Anything cheaply, or precisely |

118 tests, 3 m 13 s of test time. The proportions matter more than the totals: unit tests are where you can afford to be exhaustive, E2E is where you can afford exactly the journeys that must never break. **An inverted pyramid — mostly E2E — is the classic outcome of asking an assistant for "tests for this feature"**, because end-to-end tests are the easiest to describe in a sentence.

The Rukhsa E2E set is deliberately small and deliberately specific: submit an application; upload a document; fail eligibility and see the reason in Arabic; pass eligibility and receive an assessment of SAR 3,780.00; pay and reach `awaiting_inspection`; record an inspection pass and receive a licence; scan the QR token and see a valid certificate. Seven journeys, each of which would be a public incident if it broke.

### 2. The four weak-test patterns

| Pattern | What it looks like | Why the assistant produces it | Repair |
|---|---|---|---|
| **Vacuous** | `assert result is not None` | It satisfies "write a test" with minimal information about the domain | Assert the value: `assert result.total == Decimal("3780.00")` |
| **Tautological** | `assert calculate_fee(a, b) == calculate_fee(a, b)` or re-implementing the formula in the assertion | It was shown the implementation, not the spec | Assert against the specification's concrete numbers |
| **Over-mocked** | Mocking `calculate_fee` inside the test *of* `create_assessment` | Mocking is the conventional pattern in its training data | Mock only what crosses a boundary you do not own (SADAD, object storage) |
| **Implementation-derived** | Tests that pass on buggy code because they were generated from it | Generated after the code, from the code | Generate tests from the spec's acceptance criteria, before or independently of the implementation |

The fourth is the most dangerous because it is invisible: the tests are green, thorough-looking, and confirm the defect. The single procedural defence is to **generate tests from the specification, not from the implementation** — paste `SPEC-004`'s acceptance criteria, not `fees.py`.

### 3. Coverage is a floor; mutation score is the measurement

Line coverage answers "was this line executed?" A test with no assertion executes every line it touches and detects nothing. Rukhsa's generated suite reached **88% line coverage** and a **41% mutation score** — meaning that of the small behavioural changes injected into the code, 59% were not detected by any test.

Mutation testing works by making one small change (mutant) — `>` to `>=`, `+` to `-`, a constant to another constant, a return value to `None` — running the suite, and recording whether any test failed. A mutant that survives is a behaviour nothing asserts.

| Suite state | Line coverage | Branch coverage | Mutants killed | Mutation score |
|---|---|---|---|---|
| Generated, unrepaired | 88% | 74% | 61 / 149 | 41% |
| After repairing vacuous + tautological tests | 88% | 79% | 96 / 149 | 64% |
| After adding boundary + property tests | 88% | 81% | 114 / 149 | 77% |

Note that line coverage does not move at all across those rows. That is the lesson: **coverage measures reach, mutation score measures grip.** Rukhsa gates coverage at 85% (a floor, to catch entirely untested modules) and mutation score at 70% on the two modules where correctness is financial — `services/fees.py` and `services/transitions.py`. Gating mutation score across the whole codebase is impractical; gating it where money and legal status live is proportionate.

Surviving mutants are also *informative*. On Rukhsa, `max(Decimal("0"), area_sqm - FREE_AREA_SQM)` mutated to `min(...)` survived — because no test used an area below 100 m². The mutant did not just reveal a weak test; it revealed a missing boundary case, which is AC2 in the spec, which nobody had implemented as a test.

### 4. Property-based testing for the fee invariants

Example-based tests check the points you thought of. Property-based tests check the properties that must hold everywhere, across inputs generated by the framework — and Hypothesis will shrink any counterexample it finds to the smallest failing input, which is usually the whole diagnosis.

Rukhsa's fee invariants, each independently valuable:

1. **Monotonicity** — a larger area never produces a smaller total.
2. **Exactness** — the total always has exactly two decimal places; no floating-point residue can appear.
3. **Composition** — `total == base + surcharge + service`, always, for every input.
4. **Threshold** — any area at or below 100 m² yields a surcharge of exactly zero.
5. **Rejection** — a non-positive area always raises `ValueError`, never returns.

Property 2 is the one that would have caught the `float` implementation from M3 on the first run, without anyone thinking of a specific failing value. That is the argument for properties in one sentence: they find the inputs you would not have chosen.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Generate tests from the spec, never from the implementation.* Otherwise the suite ratifies the defect.
- *Assert values, not existence.* `is not None` is the signature of a test that cannot fail.
- *Mock only across boundaries you do not own.* SADAD and object storage, yes; your own service, no.
- *Coverage is a floor, mutation score is the goal* — and only where correctness is expensive.
- *E2E tests are a scarce resource.* Seven journeys, chosen because their failure is a public incident.

**Common mistakes (each appears in the Lab 6 starter deliberately)**
1. `def test_create_assessment(): assert create_assessment(...) is not None` — vacuous, kills zero mutants.
2. A fee test that recomputes the formula in its assertion, so any arithmetic defect is reproduced in the check.
3. `@patch("app.rukhsa.services.assessment.calculate_fee")` inside the assessment service's own test, so the fee is never exercised.
4. An integration test that commits and never rolls back, so test order determines outcomes and the suite is green locally and red in CI.
5. Twelve E2E Playwright tests and eleven unit tests — an inverted pyramid taking 9 minutes to say very little.
6. A `time.sleep(2)` in the E2E test instead of a web-first assertion, producing a suite that is slow *and* flaky.

**Production considerations**
- Run unit tests on every save, integration on every push, E2E on every pull request. Feedback latency determines whether a suite is used or endured.
- Keep a fixed test database per CI job with a transactional fixture rather than recreating the schema per test — 22 s versus 4 minutes for Rukhsa's 17 integration tests.
- Quarantine flaky E2E tests immediately and fix them within a sprint. One tolerated flake teaches the team to ignore red, and a suite that is ignored is worse than none.
- Store the mutation baseline in the repository so the score can only go up. Ratcheting is the only thing that survives delivery pressure.

### 6. Real-world example walkthrough

Narrate this (5 minutes). A team was asked to raise coverage from 44% to 80% before a release gate. They generated tests for a week and hit 83%. The release shipped and the escaped-defect rate was unchanged — three of the four defects found in production were in files with 100% coverage. A retrospective mutation run scored the suite at 38%. Reading the surviving mutants was more useful than any code review had been: they clustered entirely in error paths and boundary conditions, which is exactly what a generated test derived from an implementation's happy path will never touch. The team kept the tests, repaired the twenty worst files by adding assertions the mutants demanded, and adopted a rule that has served since — **coverage may be a gate, but only mutation score may be a target**, because coverage is trivially gameable and grip is not.

## Code Examples

### Weak generated tests and their repairs

```python
# tests/unit/test_fees.py
"""Unit tests for the fee engine, written from SPEC-004's acceptance criteria.

WHY from the spec and not from fees.py: a test generated from an implementation
asserts what the code does, which is exactly the wrong question. Each test below
names the acceptance criterion it enforces, so a reviewer can check coverage of
the SPEC rather than coverage of the lines.
"""
from decimal import Decimal

import pytest

from app.rukhsa.services.fees import calculate_fee

# ❌ AI-GENERATED — DO NOT SHIP.
# Defect 1 (vacuous): passes against any implementation that returns an object.
#   Kills 0 of the 149 mutants.
# Defect 2 (tautological): re-implements the formula in the assertion, so an
#   arithmetic error in fees.py is faithfully reproduced by the check.
#
# def test_calculate_fee_works():
#     result = calculate_fee(Decimal("2400"), Decimal("180"))
#     assert result is not None
#
# def test_calculate_fee_total():
#     r = calculate_fee(Decimal("2400"), Decimal("180"))
#     assert r.total == r.base_fee + r.area_surcharge + r.service_fee


def test_ac1_fnb_180sqm() -> None:
    """SPEC-004 AC1: activity 5610 (SAR 2,400.00) at 180 m² prices at 3,780.00."""
    result = calculate_fee(base_fee=Decimal("2400.00"), area_sqm=Decimal("180.00"))
    # Every component asserted against the spec's numbers, not against each other.
    assert result.base_fee == Decimal("2400.00")
    assert result.area_surcharge == Decimal("1200.00")   # 15.00 × 80 m²
    assert result.service_fee == Decimal("180.00")       # 5% of 3,600.00
    assert result.total == Decimal("3780.00")
    assert result.total.as_tuple().exponent == -2        # exactly two places


def test_ac2_threshold_area_has_no_surcharge() -> None:
    """SPEC-004 AC2: at exactly the 100 m² threshold the surcharge is zero.

    This boundary was missing from the generated suite, which is why the
    `max()` -> `min()` mutant survived the first mutation run.
    """
    result = calculate_fee(base_fee=Decimal("1200.00"), area_sqm=Decimal("100.00"))
    assert result.area_surcharge == Decimal("0.00")
    assert result.total == Decimal("1260.00")            # 1200 + 0 + 5%


@pytest.mark.parametrize("area", [Decimal("0"), Decimal("-1"), Decimal("-0.01")])
def test_non_positive_area_is_rejected(area: Decimal) -> None:
    """SPEC-004 inputs: area must be strictly positive. Assert the exception TYPE."""
    with pytest.raises(ValueError, match="area_sqm"):
        calculate_fee(base_fee=Decimal("1200.00"), area_sqm=area)

```

### Property-based tests and the transactional integration fixture

```python
# tests/unit/test_fees_properties.py
"""Invariants of the fee engine, checked across the whole input domain.

WHY properties in addition to examples: the float implementation from M3 passed
three example tests and fails `test_total_always_two_places` on Hypothesis's
first few dozen inputs, without anyone having to guess a failing value.
"""
from decimal import Decimal

from hypothesis import assume, given, settings
from hypothesis import strategies as st

from app.rukhsa.services.fees import calculate_fee

# Areas across the legal domain (SPEC-004: 0 < area <= 5000, two decimal places).
areas = st.decimals(
    min_value=Decimal("0.01"), max_value=Decimal("5000.00"),
    places=2, allow_nan=False, allow_infinity=False,
)
# The three real activity bands plus the space between them.
base_fees = st.decimals(
    min_value=Decimal("500.00"), max_value=Decimal("10000.00"), places=2,
)


@given(base=base_fees, area=areas)
@settings(max_examples=300, deadline=None)
def test_total_always_two_places(base: Decimal, area: Decimal) -> None:
    """Invariant 2 (exactness): no float residue can ever appear in a SAR total."""
    result = calculate_fee(base_fee=base, area_sqm=area)
    assert result.total == result.total.quantize(Decimal("0.01"))


@given(base=base_fees, area=areas)
@settings(max_examples=300, deadline=None)
def test_components_sum_to_total(base: Decimal, area: Decimal) -> None:
    """Invariant 3 (composition): the breakdown always reconciles to the total."""
    r = calculate_fee(base_fee=base, area_sqm=area)
    assert r.base_fee + r.area_surcharge + r.service_fee == r.total


@given(base=base_fees, small=areas, large=areas)
@settings(max_examples=300, deadline=None)
def test_larger_area_never_costs_less(base: Decimal, small: Decimal, large: Decimal) -> None:
    """Invariant 1 (monotonicity): pricing must never reward a larger premises."""
    assume(small <= large)
    assert calculate_fee(base, small).total <= calculate_fee(base, large).total
```

```python
# tests/conftest.py
"""Shared fixtures. The integration fixture is the load-bearing one.

WHY a nested transaction rolled back per test rather than recreating the schema:
17 integration tests run in 22 s instead of ~4 minutes, and no test can leak
state into another -- which is the defect that makes a suite green locally and
red in CI, or green in isolation and red in parallel.
"""
from collections.abc import Iterator

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.rukhsa.core.config import get_settings
from app.rukhsa.models.base import Base

_engine = create_engine(str(get_settings().database_url), future=True)
_Session = sessionmaker(bind=_engine, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
def _schema() -> Iterator[None]:
    """Create the schema once for the whole session, not once per test."""
    Base.metadata.create_all(_engine)
    yield
    Base.metadata.drop_all(_engine)


@pytest.fixture
def session() -> Iterator[Session]:
    """A Session whose work is always rolled back.

    The outer transaction is never committed. A `session.commit()` inside the
    code under test commits the SAVEPOINT only, so real transaction behaviour --
    including the FOR UPDATE lock from M4 -- is genuinely exercised while the
    database is left untouched.
    """
    connection = _engine.connect()
    outer = connection.begin()
    db = _Session(bind=connection, join_transaction_mode="create_savepoint")

    @event.listens_for(db, "after_transaction_end")
    def _restart_savepoint(sess: Session, trans) -> None:
        if trans.nested and not trans._parent.nested:
            sess.begin_nested()

    try:
        yield db
    finally:
        db.close()
        outer.rollback()          # nothing this test did survives
        connection.close()
```

### The licence-issuance journey, end to end

```typescript
// tests/e2e/licence_issuance.spec.ts
// WHY web-first assertions and no sleeps: Playwright's expect() retries until the
// condition holds or the timeout expires, so the test is fast when the app is
// fast and stable when it is slow. A time.sleep(2) is both slower and flakier.
import { test, expect } from '@playwright/test';
import { seedEligibleApplication, inspectorPass } from './fixtures/rukhsa';

test.describe('Rukhsa licence issuance', () => {
  test('a citizen submits, pays SAR 3,780.00, and receives a verifiable licence', async ({ page, request }) => {
    // Arrange: a synthetic applicant. No real national id ever enters a test.
    const { reference, citizenToken } = await seedEligibleApplication({
      activityCode: '5610',        // food & beverage, SAR 2,400.00 base
      areaSqm: '180.00',
      city: 'Riyadh',
    });

    await page.goto(`/applications/${reference}`);
    await expect(page.getByTestId('status')).toHaveText('eligible');

    // Act 1: request the fee assessment and check the SPEC-004 AC1 breakdown.
    await page.getByRole('button', { name: 'Calculate fee' }).click();
    await expect(page.getByTestId('fee-base')).toHaveText('SAR 2,400.00');
    await expect(page.getByTestId('fee-surcharge')).toHaveText('SAR 1,200.00');
    await expect(page.getByTestId('fee-service')).toHaveText('SAR 180.00');
    await expect(page.getByTestId('fee-total')).toHaveText('SAR 3,780.00');

    // Act 2: pay through the stubbed SADAD sandbox (a boundary we do not own).
    await page.getByRole('button', { name: 'Pay via SADAD' }).click();
    await expect(page.getByTestId('status')).toHaveText('awaiting_inspection');

    // Act 3: the inspector passes the field inspection.
    await inspectorPass(request, reference);
    await page.reload();
    await expect(page.getByTestId('status')).toHaveText('issued');

    // Assert: the certificate exists and its QR token verifies publicly.
    const licenceNumber = await page.getByTestId('licence-number').innerText();
    expect(licenceNumber).toMatch(/^RKH-LIC-2026-\d{6}$/);

    const qrToken = await page.getByTestId('qr-token').getAttribute('data-token');
    const verify = await request.get(`/verify/${qrToken}`);   // unauthenticated
    expect(verify.status()).toBe(200);
    const body = await verify.json();
    expect(body.valid).toBe(true);
    expect(body.licence_number).toBe(licenceNumber);
    // PDPL: the public verification response must never expose the applicant.
    expect(body).not.toHaveProperty('national_id_hash');
    expect(body).not.toHaveProperty('applicant_name');
  });
});
```

## Hands-on Lab 6 — Prove the Tests Actually Test

| | |
|---|---|
| **Objective** | Generate a test suite from the specifications, measure its real strength with mutation testing, raise the score from 41% to ≥ 70%, add property-based tests for the fee invariants, and automate the licence-issuance journey with Playwright |
| **Duration** | 100 minutes (Lab 6a 50 min, Lab 6b 50 min) |
| **Setup** | Lab 5 repository, `pip install pytest==8.3.3 pytest-cov hypothesis==6.112.* mutmut==2.5.*`, `npm i -D @playwright/test@1.47 && npx playwright install chromium`, `git checkout lab6-start` |

**Instructions & tasks**

1. *(10 min)* **Lab 6a.** Run the generated suite: `pytest --cov=app/rukhsa --cov-branch`. Record coverage (expect 88% line, 74% branch). Then read `tests/unit/test_fees.py` and classify each test against the four weak patterns in `LAB6_TESTS.md`.
2. *(12 min)* Run `mutmut run --paths-to-mutate app/rukhsa/services/fees.py,app/rukhsa/services/transitions.py` and then `mutmut results`. Record the baseline score (expect 61/149 = 41%). Inspect three surviving mutants with `mutmut show <id>` and write down, for each, the behaviour nothing asserts.
3. *(18 min)* Repair the suite: replace vacuous and tautological assertions with the specification's concrete values, remove the mock of `calculate_fee` from the assessment service test, and add AC2 (the 100 m² boundary the `max`→`min` mutant exposed). Re-run mutation and record the new score (expect ~64%).
4. *(10 min)* Add the five Hypothesis property tests. Re-run mutation; the score should reach ≥ 70% (expect 77%). Note in `LAB6_TESTS.md` that line coverage did **not** change across steps 3 and 4 — this is the module's point.
5. *(30 min)* **Lab 6b.** Write the licence-issuance Playwright journey from the example, then add two more of the seven: the Arabic eligibility-failure message, and the QR verification of a *revoked* licence returning `valid: false`. Run headed once (`--headed`) to watch, then headless.
6. *(20 min)* Add `pytest.ini` gates (`--cov-fail-under=85`), commit the mutation baseline, and commit: `test(fees): strengthen assertions and add property tests, mutation 41% -> 77% (SPEC-004)`.

**Expected output**
```
$ pytest --cov=app/rukhsa --cov-branch -q
118 passed in 3.41s
TOTAL                     2914   349   1102   214    88%   (branch 81%)

$ mutmut results
Killed 61 out of 149 mutants  (41%)     <-- baseline, generated suite
# ... after repair and property tests ...
Killed 114 out of 149 mutants (77%)

$ mutmut show 47
--- app/rukhsa/services/fees.py
+++ app/rukhsa/services/fees.py
@@ -41,7 +41,7 @@
-    chargeable_area = max(Decimal("0"), area_sqm - FREE_AREA_SQM)
+    chargeable_area = min(Decimal("0"), area_sqm - FREE_AREA_SQM)
# SURVIVED: no test exercises an area at or below the 100 m² threshold (AC2).

$ npx playwright test
Running 7 tests using 3 workers
  7 passed (2.8m)
```

**Acceptance criteria**
- Mutation score on `fees.py` + `transitions.py` ≥ 70% (from 41%), with the baseline committed.
- Zero vacuous (`is not None`-only) and zero tautological assertions remain in `tests/unit/`.
- Five Hypothesis properties pass at `max_examples=300`.
- Three Playwright journeys pass headless, with no `sleep` and no fixed waits.
- Line coverage ≥ 85% and demonstrably *unchanged* by the assertion strengthening.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `mutmut run` takes over ten minutes | Mutating the whole package | Restrict `--paths-to-mutate` to the two services; that is the proportionate gate |
| Integration tests pass alone, fail together | A test commits without rollback | Use the `session` fixture; never create a second engine inside a test |
| Hypothesis fails with `DeadlineExceeded` | Database or import work inside the property | Keep properties pure; `deadline=None` only after confirming there is no I/O |
| Playwright times out on `getByTestId` | The front end has no `data-testid` attributes | Add them — stable test hooks are production code, not test scaffolding |

**Instructor notes.** Step 2 is the module. Do not let anyone skip to the repair: reading three surviving mutants and naming the unasserted behaviour is what converts "write better tests" from advice into a procedure. Watch for participants who try to raise the score by deleting mutants' code paths rather than adding assertions — call that out publicly, warmly, once. The fact that line coverage is identical at 41% and 77% should be put on the board and left there. Fast finishers: have them run mutation on `services/eligibility.py` and discover a surviving mutant in a rule nobody tested because it "obviously works."

## Mini Exercises

**Quiz (5 questions)**
1. What does a surviving mutant tell you? → some behaviour is changeable without any test failing; that behaviour is unasserted.
2. Why did line coverage stay at 88% while mutation score went 41% → 77%? → coverage measures execution, not assertion; the same lines were always executed.
3. When is mocking appropriate? → only across a boundary you do not own — SADAD, object storage — never your own service under test.
4. Which property would have caught the `float` fee implementation without a specific failing value? → exactness: the total always quantises to exactly two decimal places.
5. Why is an inverted pyramid the natural output of asking an assistant for "tests for this feature"? → an end-to-end journey is the easiest thing to describe in a sentence, so it is what a one-line request produces.

**Debugging exercise.** Branch `lab6-mocked-service` mocks `calculate_fee` inside `test_create_assessment`. Introduce a defect into the real `calculate_fee` (change `0.05` to `0.15`) and observe that the assessment test still passes while a citizen is now charged three times the service fee. Discuss where the mock boundary should have been.

**Design exercise.** Choose the seventh Playwright journey Rukhsa should have (six are given). Justify it by the incident it prevents, and estimate its runtime cost against the 2 m 48 s budget.

**Discussion questions.**
- If mutation score is the better measurement, why does almost every organisation gate on coverage instead? Is the answer purely cost?
- A generated test suite that ratifies a defect is worse than no suite. Does that argue for writing tests by hand, or for changing what you paste into the assistant?

## Case Study — The Green Suite at "Sadad" (سداد) Payments

**Scenario.** "Sadad" (سداد), a Saudi payments-reconciliation provider in Jeddah, processes settlement files for 60 merchants. Under a compliance deadline it raised automated test coverage from 51% to 89% in three weeks using generated tests, and passed its audit. Four months later a rounding defect in a currency-conversion path under-settled 11,400 transactions by a few halalas each — SAR 84,000 in aggregate — over six weeks before a merchant's own reconciliation caught it. The affected file had 100% line coverage and nineteen tests.

**Business context.** Sadad's contracts guarantee settlement accuracy; the shortfall was reimbursed with interest and triggered a mandatory report to the client's finance function. The reputational cost of "our tests said it was fine" exceeded the financial one.

**Technical challenge.** The nineteen tests had been generated from the implementation. Every one asserted what the code did, including its rounding behaviour; several were tautological, recomputing the conversion in the assertion. A retrospective mutation run scored the file at 22%. The team must now decide what a "tested" file means for their audit evidence, and re-establish confidence across 340 similar files without a three-month rewrite.

**Constraints.** Cannot re-audit; the compliance framework the auditor uses specifies coverage thresholds and has no concept of mutation score; engineering capacity is four people; the settlement path cannot be paused; some merchants' files are the only source of truth for their transactions, so behaviour must be preserved exactly while tests are strengthened.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) triage by consequence, not by coverage — run mutation only on the 22 files where an error is financial, which is a two-day job rather than a three-month one; (2) regenerate tests from the specifications and settlement rules, explicitly not from the code, and diff the new expectations against current behaviour — the disagreements are the findings; (3) add properties for the invariants that must hold across all currencies and amounts, which is where a rounding defect lives; (4) keep coverage as the audit-facing gate because that is what the framework speaks, and add mutation score as the internal target, documenting the relationship for the next auditor; (5) change the generation procedure so tests are produced from acceptance criteria before the implementation exists.

**Discussion questions.**
1. The auditor's framework recognises coverage and not mutation score. Do you change the framework, satisfy it and exceed it, or argue? What is realistic within one audit cycle?
2. Tests generated from an implementation ratified its rounding. Is that a tooling failure, a process failure, or a specification failure?
3. Sadad triaged by consequence rather than by coverage. What is the general rule that produces the list of 22 files, and could you produce it for Rukhsa?
4. Six weeks passed before a merchant noticed. What non-test control would have caught a systematic few-halala shortfall sooner?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Mutation score (`fees`, `transitions`) | Assertion strength | ≥ 70% (from 41%) | `mutmut results` |
| Line / branch coverage | Reach floor | ≥ 85% line, ≥ 78% branch | `pytest --cov --cov-branch` |
| Vacuous or tautological assertions | Test quality | 0 remaining | review + `LAB6_TESTS.md` |
| Property tests passing | Domain coverage | 5 properties at 300 examples | `pytest tests/unit/test_fees_properties.py` |
| E2E journeys green, no fixed waits | Journey safety | 3 of 7 in lab, 7 by capstone | `npx playwright test` |

**Example benchmark table (filled during lab):**

| Stage | Tests | Line cov | Branch cov | Mutants killed | Score | Suite time |
|---|---|---|---|---|---|---|
| Generated baseline | 71 | 88% | 74% | 61 / 149 | 41% | 2.9 s |
| Assertions repaired | 78 | 88% | 79% | 96 / 149 | 64% | 3.1 s |
| Properties + boundaries added | 94 | 88% | 81% | 114 / 149 | 77% | 3.4 s |
| With integration + E2E | 118 | 88% | 81% | 114 / 149 | 77% | 3 m 13 s |

## Required Visuals and Training Assets

### Diagrams
1. **The Rukhsa test pyramid, to scale** — *Purpose:* make proportion visceral. *Elements:* 94/17/7 as proportional bands with runtimes and "what it proves / cannot prove" captions; an inverted pyramid shown beside it as the anti-pattern. *Style:* two pyramids side by side, one upright and one inverted and red.
2. **Coverage versus mutation score** — *Purpose:* the module's central distinction. *Elements:* two gauges over the same code — coverage pinned at 88% while mutation moves 41% → 64% → 77%. *Style:* dual-gauge before/after, coverage needle visibly frozen.
3. **How a mutant survives** — *Purpose:* explain mutation testing in one image. *Elements:* the `max`→`min` mutation on the surcharge line, the test suite running green, and the missing AC2 boundary case highlighted as the gap. *Style:* code diff with a green tick and a red gap marker.
4. **The seven E2E journeys** — *Purpose:* justify E2E scarcity. *Elements:* the licence lifecycle with the seven tested transitions marked and their runtimes summing to 2 m 48 s. *Style:* the state machine from M2, annotated with test coverage.

### Images (screenshots)
1. **`mutmut results` at 41%** — *why:* the number that reframes an 88% coverage report; *content:* the killed/survived tally.
2. **A Hypothesis shrunk counterexample** — *why:* shrinking is what makes properties diagnostic; *content:* the falsifying example reduced to its minimal form.
3. **The Playwright trace viewer on the issuance journey** — *why:* participants must know the debugging tool exists; *content:* the timeline with the SAR 3,780.00 assertion selected.

### Simulations
1. **The 100%-covered defect** — *Setup:* a file at 100% coverage with a deliberate off-by-one, and its nineteen generated tests. *Expected behaviour:* all green. *Learning objective:* coverage is reach, not grip.
2. **Mock the world** — *Setup:* branch `lab6-mocked-service` with `calculate_fee` mocked in the assessment test; change the service-fee rate to 15%. *Expected behaviour:* the suite passes while every citizen is overcharged. *Learning objective:* a mock is a promise you stop checking.

### Interactive Activities
- **Assertion autopsy (12 min):** ten generated assertions on cards; teams sort them into "would fail on a real defect" and "would not," then run them against a planted defect to score themselves.
- **Property hunt (15 min):** teams write three invariants for the inspector-queue assignment logic, then run them and see which ones the current implementation violates.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tests/` generated suite | `lab6-start` branch | Python | 71 tests | The weak baseline to be measured and repaired |
| `tests/e2e/fixtures/rukhsa.ts` | Course repository | TypeScript | 6 helpers | Synthetic seeding for Playwright; no real personal data |
| `mutmut_baseline.json` | Produced in the lab, committed | JSON | 149 mutants | The ratchet — the score may only rise |

### Demo Requirements
- **Instructor demo (8 minutes):** show the coverage report at 88% and let the room feel satisfied, then run `mutmut results` at 41% in the same breath. Open one surviving mutant, add the single assertion that kills it, and re-run to show the score move while coverage does not. Eight minutes, one idea, and it reframes every coverage conversation the participants will have afterwards.

---

# Module 7 — Automated Documentation and Maintainability
## التوثيق البرمجي التلقائي وقابلية الصيانة

## Module Overview

**Purpose.** This module covers catalogue module 6. Documentation is the artefact AI assistants generate most willingly and most uselessly: a docstring restating the function signature costs nothing to produce and answers no question anyone has. Participants learn which documentation is *derived* (generated from source and therefore never stale) and which is *decided* (written once by a human because it records a judgement), and build Rukhsa's documentation set — docstrings gated by coverage, an OpenAPI contract generated from Pydantic models, ADRs, a runbook, and a README that passes a handover test performed by a peer.

**Business relevance.** In Saudi public-sector delivery, systems outlive their teams by years and are routinely handed to a different supplier at contract renewal. The catalogue's phrasing — "to facilitate seamless software maintenance and future scalability" — is a procurement requirement, not a nicety. AI-assisted development sharpens it: when the code was generated in ninety seconds, the reasoning behind it was never written down anywhere, and the next team inherits a system that works for reasons nobody recorded.

**Industry use cases.**
- A ministry hands a portal to a new supplier at contract renewal and the transition is priced by how much of the system must be reverse-engineered.
- A team publishes an OpenAPI contract that integration partners generate clients from, so a breaking change must be detected before it ships, not after.
- An on-call engineer at 03:00 needs the runbook entry for "payments are queued but not settling," and needs it to be accurate.

**Expected competencies.** After this module a participant can distinguish derived from decided documentation and choose the right mechanism for each; write docstrings that record *why* and gate their coverage in CI; generate and diff an OpenAPI contract to detect breaking changes; write a README that a peer can use to run and understand the system unaided; and maintain ADRs, a runbook and a changelog generated from conventional commits.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Distinguish derived from decided documentation and choose the mechanism for each | LO7 |
| 7.2 | Write and gate docstrings that record intent and constraints, not signatures | LO7 |
| 7.3 | Generate, version and diff an OpenAPI contract to detect breaking changes | LO7, LO8 |
| 7.4 | Produce a README, runbook and ADR set that survive a handover test | LO7 |
| 7.5 | Generate a changelog from conventional commits and keep it honest | LO7, LO8 |

## Technical Content

### 1. Derived versus decided documentation

| | Derived | Decided |
|---|---|---|
| Source of truth | The code | A human judgement at a point in time |
| Examples | OpenAPI schema, ERD from models, API reference, changelog from commits, dependency inventory | ADRs, README's "why this exists", runbook procedures, the data inventory's lawful basis, the threat model |
| Staleness risk | Zero if generated in CI | High — must be reviewed on a cadence |
| AI's role | Generate the generator, once | Draft and challenge; never decide |
| Failure mode | Nobody regenerates it, so it silently drifts | Written after the fact to justify what exists |

The engineering rule that follows: **never hand-maintain anything that can be derived.** Rukhsa's API reference, ERD and changelog are all produced in CI and committed by the pipeline, so a pull request that changes a response model changes the contract in the same diff — visibly, reviewably. Everything else is a decision and must be written by a person who made it.

### 2. Docstrings that answer a question

An assistant asked to "add docstrings" will produce a wall of prose restating the signature: *"get_application. Args: application_id: The application ID. Returns: The application."* This is worse than nothing, because it occupies the space where the real answer would go and makes the file look documented.

A docstring earns its lines when it records at least one of: **why this exists** (the alternative that was rejected), **what invariant it maintains**, **what it does not do**, or **what will surprise you** (a constraint, a lock, a rounding rule, a PDPL obligation). Compare the two forms on Rukhsa's assessment service: the generated version says it "creates an assessment"; the useful version says the parent row is locked `FOR UPDATE` before the existence check and that the partial unique index is the real guarantee — which is what a maintainer removing the lock in six months needs to read.

Gating is what makes this stick. `interrogate` measures docstring *presence* and is gated at 90% on `app/rukhsa/services/` and `app/rukhsa/api/`; `ruff`'s pydocstyle rules enforce the format; `darglint` verifies that documented arguments and raised exceptions match the signature, which catches the most common drift — a docstring describing parameters that no longer exist.

Presence is checkable and usefulness is not, which is a real limit. The compensating control is a review question, not a tool: **"which of these docstrings would have changed what you did?"** Ask it in the handover drill and the weak ones are obvious.

### 3. The OpenAPI contract as a reviewable artefact

FastAPI derives an OpenAPI document from the Pydantic models and route signatures, which means the contract is free — and therefore usually unversioned, unreviewed and invisible. Rukhsa exports it to `docs/openapi.json` in CI and fails the build if the committed file differs from the generated one. Two consequences follow, both valuable:

1. **A breaking change appears in the diff.** Removing a field, tightening a type or changing a status code shows up as a reviewable change to a committed file, so a reviewer sees it without reading the router.
2. **Integration partners have a stable artefact.** The municipality's inspector mobile app generates its client from this file; a silent change is an outage on someone else's roadmap.

The quality of the derived contract depends entirely on what the models say. Response models with `Field(..., description=..., examples=[...])` produce a document an integrator can use; bare types produce one they cannot. This is where an assistant is genuinely excellent — asked to add descriptions and realistic Saudi examples to a Pydantic model, it does careful, tedious work well — provided the examples are checked for invented domain facts (M2) and for personal data (a real-looking national ID in an OpenAPI example is a PDPL problem even if it is synthetic, because nobody downstream can tell).

### 4. The handover test

A README passes when **a competent engineer who has never seen the repository can, using only the README: run it, run its tests, understand what it does and why, make a small change, and know who to ask.** That is the whole standard, and it is testable — Rukhsa's Day 4 drill is that participants swap repositories and attempt exactly that in twenty minutes, recording every point at which they were blocked.

The sections that survive contact with that test:

| Section | The question it answers | Failure signature |
|---|---|---|
| What and why | What problem does this solve, for whom? | Reader can run it but cannot tell if a change is appropriate |
| Quick start | Can I run it in ten minutes? | Missing a service, an env var, or a seed step |
| Architecture in one diagram | Where does my change go? | Reader edits the router because they cannot find the service layer |
| Decisions | Why is it like this? | Reader "fixes" a deliberate choice — links to `docs/adr/` |
| Operations | How do I run tests, migrations, the pipeline? | Reader cannot reproduce CI locally |
| Data protection | What is personal data here and what are the rules? | Reader logs a national ID |
| Ownership | Who do I ask, and where do issues go? | Reader is blocked for a day |

The runbook is separate and answers a different question — not "how do I develop this" but "it is broken at 03:00, what do I do." Rukhsa's has six entries, each with a symptom, a diagnostic query, an action and an escalation. They are written from the incidents in M4 and M5, which is the only honest source for a runbook.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Derive everything derivable; decide the rest deliberately.* Two mechanisms, two staleness profiles.
- *A docstring must change what a reader does.* Otherwise delete it.
- *The contract is a committed artefact.* If a breaking change is not visible in a diff, it is not reviewed.
- *Documentation is tested by use, not by inspection.* Run the handover drill.
- *Write the ADR when you decide, not when you are asked for it.* A retrospective ADR records a rationalisation.

**Common mistakes (each appears in the Lab 7 starter deliberately)**
1. Generated docstrings restating signatures on all 34 service functions — 90% `interrogate` coverage and zero information.
2. `docs/openapi.json` committed once and never regenerated, so it describes an API that no longer exists.
3. A README quick-start missing the `alembic upgrade head` step, so a new engineer's first run fails on a missing table.
4. An ADR written after the code to justify it, whose "alternatives considered" section lists options nobody actually weighed.
5. A generated OpenAPI example containing a real-looking Saudi national ID — synthetic, but indistinguishable downstream, and copied into a partner's test fixtures.
6. A `CHANGELOG.md` hand-maintained beside conventional commits, so the two disagree within a fortnight.

**Production considerations**
- Regenerate derived documentation in CI and fail on drift. `git diff --exit-code docs/openapi.json` after regeneration is a two-line gate that prevents an entire failure class.
- Review decided documentation on a cadence tied to change, not to the calendar: an ADR is reviewed when a pull request touches the area it governs, enforced through CODEOWNERS.
- Keep `docs/DATA_INVENTORY.md` current as a PDPL obligation, not a documentation nicety — it is the artefact a regulator asks for, and it must name every field, its lawful basis and its retention period.
- Publish the API reference from the committed contract so integrators consume a versioned document rather than a live environment.

### 6. Real-world example walkthrough

Narrate this (5 minutes). A supplier handed a working, well-tested government portal to a successor team at contract end. The code was clean, coverage was 86%, and every function had a docstring. The transition still took five months, because none of the documentation answered a single question the new team actually had: why is there a nightly reconciliation job (because the payment gateway's callback is unreliable); why does the fee table have an effective-date column nobody uses (because a fee change is scheduled for the next fiscal year); why is one endpoint deliberately synchronous (because the integration partner cannot handle a 202). All three were decisions, none had an ADR, and the two engineers who made them had moved on. The successor team's first act was to write the ADRs retrospectively from git archaeology and interviews — nine weeks of work that would have been ninety minutes at the time. The rule that came out of it: **if you had to think about it, write down why.**

## Code Examples

### Documentation as a derived, gated artefact

```python
# scripts/export_openapi.py
"""Export the OpenAPI contract so it becomes a reviewable, versioned artefact.

WHY export rather than rely on the live /openapi.json: a contract that exists only
at runtime is never reviewed. Committing it means a breaking change -- a removed
field, a tightened type, a changed status code -- appears in the pull-request diff
where a human and the integration partners' CI can both see it.

CI runs this and then `git diff --exit-code docs/openapi.json`; drift fails the build.
"""
from __future__ import annotations

import json
from pathlib import Path

from app.rukhsa.main import create_app

OUTPUT = Path("docs/openapi.json")


def export() -> None:
    """Write the generated contract with stable key ordering.

    sort_keys is essential: without it the JSON key order varies between Python
    runs and every CI build reports spurious drift, which trains the team to
    ignore the gate -- the worst possible outcome for a control.
    """
    schema = create_app().openapi()
    schema["info"]["x-generated-by"] = "scripts/export_openapi.py"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    paths = len(schema["paths"])
    schemas = len(schema.get("components", {}).get("schemas", {}))
    print(f"wrote {OUTPUT}: {paths} paths, {schemas} schemas")


if __name__ == "__main__":
    export()
```

```python
# app/rukhsa/schemas/fees.py
"""Response models for the fee endpoints.

WHY descriptions and examples live on the model rather than in prose: they are
the source of the OpenAPI contract, so documenting here documents the integrator
experience automatically and cannot drift from the implementation.
"""
from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class FeeAssessmentRead(BaseModel):
    """A priced assessment of one licence application (SPEC-004).

    Amounts are exact decimals in SAR. Clients must not parse them as floats:
    JSON numbers are serialised as strings for this reason, so that a client in a
    language with binary floating point cannot silently lose a halala.
    """

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={Decimal: str},
        json_schema_extra={
            # A complete, realistic example. PDPL: no national id, no applicant
            # name -- an example is copied into partner fixtures and must never
            # carry anything resembling personal data.
            "examples": [
                {
                    "assessment_id": "6f1c4e8a-9d2b-4c31-8f70-1a2b3c4d5e6f",
                    "application_reference": "RKH-2026-000123",
                    "base_fee": "2400.00",
                    "area_surcharge": "1200.00",
                    "service_fee": "180.00",
                    "total": "3780.00",
                    "currency": "SAR",
                    "assessed_at": "2026-03-10T09:14:22Z",
                }
            ]
        },
    )

    assessment_id: uuid.UUID = Field(description="Opaque identifier of this assessment.")
    application_reference: str = Field(
        description="Human-facing application reference, format RKH-YYYY-NNNNNN.",
        pattern=r"^RKH-\d{4}-\d{6}$",
    )
    base_fee: Decimal = Field(description="Activity base fee (SPEC-004 rule 1).")
    area_surcharge: Decimal = Field(description="SAR 15.00/m² above 100 m² (rule 2).")
    service_fee: Decimal = Field(description="5% service fee, HALF_UP (rule 3).")
    total: Decimal = Field(description="base_fee + area_surcharge + service_fee.")
    currency: str = Field(default="SAR", description="Always SAR (SPEC-004 non-goals).")
    assessed_at: datetime = Field(description="UTC timestamp; assessments are immutable.")
```

```yaml
# .github/workflows/docs.yml
# WHY a gate rather than a task: derived documentation that nobody regenerates is
# worse than none, because readers trust it. Failing the build on drift is the
# only mechanism that survives delivery pressure.
name: docs

on: [pull_request]

jobs:
  documentation-gate:
    runs-on: ubuntu-latest
    timeout-minutes: 6
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11", cache: pip }
      - run: pip install -r requirements.lock interrogate==1.7.0 darglint==1.8.1

      # Presence: every public service and API function carries a docstring.
      - name: docstring coverage
        run: interrogate -c pyproject.toml app/rukhsa/services app/rukhsa/api --fail-under 90

      # Consistency: documented args/raises must match the actual signature.
      - name: docstring accuracy
        run: darglint -v 2 app/rukhsa/services

      # Derivation: the committed contract must equal the generated one.
      - name: openapi contract is current
        run: |
          python scripts/export_openapi.py
          git diff --exit-code docs/openapi.json \
            || { echo "::error::openapi.json is stale - run scripts/export_openapi.py"; exit 1; }

      # Honesty: the changelog is derived from conventional commits, not typed.
      - name: changelog is derived
        run: |
          npx --yes conventional-changelog-cli -p conventionalcommits -i CHANGELOG.md -s -r 2
          git diff --exit-code CHANGELOG.md \
            || { echo "::error::CHANGELOG.md is hand-edited or stale"; exit 1; }
```

## Hands-on Lab 7 — Documentation That Survives a Handover

| | |
|---|---|
| **Objective** | Replace generated signature-restating docstrings with docstrings that record intent, derive and gate the OpenAPI contract, write the README and runbook, then pass a peer handover test in twenty minutes |
| **Duration** | 50 minutes |
| **Setup** | Lab 6 repository, `pip install interrogate==1.7.0 darglint==1.8.1`, `npx` available for conventional-changelog, `git checkout lab7-start` |

**Instructions & tasks**

1. *(8 min)* Run `interrogate app/rukhsa --fail-under 90` on the starter and observe it *passes* at 91% — then read five of the generated docstrings and record in `LAB7_DOCS.md` how many would have changed what you did. Expect zero to one.
2. *(12 min)* Rewrite the docstrings on the six functions that carry a non-obvious decision — `create_assessment` (the lock), `calculate_fee` (HALF_UP), `transition` (the table), `get_application` (404 vs 403), `redact` (PDPL), `list_applications` (selectinload vs joinedload). Each must answer why, what invariant, what it does not do, or what will surprise you. Run `darglint` and fix any signature drift it reports.
3. *(10 min)* Add descriptions and PDPL-safe examples to `FeeAssessmentRead` and `ApplicationRead`, run `python scripts/export_openapi.py`, commit `docs/openapi.json`, then deliberately remove a response field and observe the drift gate fail. Restore it.
4. *(10 min)* Write `README.md` against the seven-section table and `docs/RUNBOOK.md` with three entries drawn from the M4 and M5 incidents (duplicate assessments; payments queued not settling; a leaked key). Generate `CHANGELOG.md` from your conventional commits and confirm it reads coherently — if it does not, your commit messages were poor, which is the real finding.
5. *(15 min)* **Handover test.** Swap repositories with another pair. Using *only* the README, run the application, run its tests, make a one-line change (add a city to the supported list) and get it committed. Record every blocker with a timestamp in the owner's `LAB7_HANDOVER.md`.
6. *(5 min)* Fix the top three blockers your peer found and commit: `docs(rukhsa): handover-grade README, runbook and gated OpenAPI contract`.

**Expected output**
```
$ interrogate -c pyproject.toml app/rukhsa/services app/rukhsa/api --fail-under 90
RESULT: PASSED (minimum: 90.0%, actual: 91.4%)      <-- presence, not usefulness

$ python scripts/export_openapi.py
wrote docs/openapi.json: 14 paths, 22 schemas
$ git diff --exit-code docs/openapi.json
diff --git a/docs/openapi.json b/docs/openapi.json
-            "service_fee": { "type": "string", "description": "5% municipal ..." },
::error::openapi.json is stale - run scripts/export_openapi.py

$ darglint -v 2 app/rukhsa/services
app/rukhsa/services/assessment.py:create_assessment
  DAR401: missing exception in Raises section: AssessmentAlreadyExists
```

**Acceptance criteria**
- Six docstrings rewritten to record a decision, an invariant, a non-goal or a surprise; `darglint` clean.
- `docs/openapi.json` committed, current, and the drift gate demonstrated failing and passing.
- README covers all seven sections; a peer completes run + test + one-line change in ≤ 20 minutes.
- `docs/RUNBOOK.md` has three entries with symptom, diagnostic query, action, escalation.
- `CHANGELOG.md` is generated, not hand-edited.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `interrogate` passes with useless docstrings | It measures presence only | Accept the limit; use the peer review question and `darglint` for accuracy |
| OpenAPI drift on every run with no change | Non-deterministic key ordering | `json.dumps(..., sort_keys=True)`; pin the FastAPI version |
| `darglint` reports DAR003 on every function | Indentation style mismatch | Set `docstring_style=google` in `setup.cfg`; align with `ruff`'s pydocstyle config |
| Peer cannot run the app despite the README | A step that is implicit on your machine (`docker compose up -d db`, `alembic upgrade head`, seed) | This *is* the finding — add it verbatim |

**Instructor notes.** The handover test in step 5 is the module and it is the most enjoyable forty minutes of the week; protect it. Insist that the peer uses *only* the README — no asking, no Slack. Collect the blocker lists and read three aloud; the most common are a missing migration step and an undocumented environment variable, and every room believes their README was fine until this point. Fast finishers: have them add an ERD generated from the SQLAlchemy metadata into `docs/` with a drift gate, proving the derived/decided distinction generalises beyond OpenAPI.

## Mini Exercises

**Quiz (5 questions)**
1. Give two examples each of derived and decided documentation. → derived: OpenAPI, changelog, ERD; decided: ADRs, runbook, README rationale.
2. What must a docstring do to earn its lines? → answer why, name an invariant, state a non-goal, or warn about a surprise.
3. Why commit `docs/openapi.json` rather than serve it live? → so a breaking change appears in a reviewable diff before it reaches integrators.
4. What is the handover test? → a competent stranger runs, tests, understands and changes the system using only the README, unaided.
5. Why is an ADR written after the code untrustworthy? → it rationalises the outcome; the alternatives listed were never actually weighed.

**Debugging exercise.** Branch `lab7-stale-contract` has an `openapi.json` committed four weeks ago describing `service_fee` as a number rather than a string, and an integrator's client fails on parsing. Have participants find the drift, then add the CI gate, then explain why the gate is more valuable than the fix.

**Design exercise.** Write the runbook entry for "citizens report their payment succeeded but the application is still `awaiting_payment`." Include the symptom, one diagnostic SQL query, the action, and the escalation path — and note which of the M4 controls would have raised it before a citizen did.

**Discussion questions.**
- If an assistant can produce a plausible ADR in thirty seconds, has the ADR lost its value — or has its value moved entirely into the act of deciding?
- Your README passes the handover test today. What process keeps it passing in a year, and is documentation review a realistic ask under delivery pressure?

## Case Study — The Contract Handover at "Fahras" (فهرس) Records Systems

**Scenario.** "Fahras" (فهرس), a Riyadh supplier of records and archival systems to Saudi government entities, won a five-year contract to take over a document-management platform built by a previous supplier over four years. The platform works, has 84% test coverage and an ostensibly complete documentation set — 340 pages generated largely by an assistant in the outgoing supplier's final quarter. Fahras budgeted six weeks for transition and spent nineteen.

**Business context.** Transition overrun is unbilled under a fixed-price takeover, and the client's service levels applied from week seven regardless. Fahras absorbed roughly SAR 1.4M and, more damagingly, entered the contract in breach.

**Technical challenge.** The 340 pages were derivable content: an API reference, a class inventory, a database dictionary — all accurate, all regenerable in an afternoon, all answering questions Fahras did not have. Nothing recorded a decision. Why does ingestion retry three times with a nine-second backoff? Why is one collection sharded by year and another by entity? Why does the retention job exclude a specific document class? Each answer existed only in someone's memory at the outgoing supplier, and the transition clause obliged them to provide documentation, which they had.

**Constraints.** The outgoing supplier's obligation ended at 30 days; two of their engineers were available for four hours each; the platform holds records subject to statutory retention, so behaviour cannot be changed while it is understood; the client's procurement framework specifies documentation by page count and completeness, not by usefulness.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) triage the 340 pages into derived and decided, discovering that the decided set is nearly empty — that gap is the transition risk, quantified; (2) spend the outgoing engineers' eight hours exclusively on decisions, recorded as ADRs live during the call, not on walkthroughs of code Fahras can read; (3) reconstruct the highest-consequence decisions from git archaeology where nobody is available, tagging each reconstructed ADR with its confidence; (4) run a handover test against the platform's own README and let the blockers set the transition backlog; (5) change what Fahras writes into future contracts — a decided-documentation deliverable (ADR set, runbook, data inventory) specified separately from the derived kind, because the procurement framework's page count is precisely what produced 340 useless pages.

**Discussion questions.**
1. The outgoing supplier met their contractual documentation obligation completely. Is this an ethics problem, a specification problem, or a procurement problem?
2. Eight hours of the previous engineers' time was the scarcest resource in the transition. How would you spend it, and what would you refuse to spend it on?
3. Reconstructed ADRs carry a confidence tag. Is a low-confidence ADR better or worse than no ADR, and what does the answer depend on?
4. How would you write the documentation clause into the next contract so that a supplier cannot satisfy it with 340 generated pages?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Docstring coverage | Presence floor | ≥ 90% on `services/` and `api/` | `interrogate` |
| Docstring accuracy | Consistency | 0 `darglint` findings | `darglint -v 2` |
| OpenAPI contract drift | Derivation | 0 (gate demonstrated firing) | `git diff --exit-code docs/openapi.json` |
| Handover test | Maintainability | peer runs, tests and changes in ≤ 20 min | peer `LAB7_HANDOVER.md` |
| Decided-documentation set | Knowledge retention | README (7 sections) + ≥ 4 ADRs + 3 runbook entries | instructor review |

**Example benchmark table (filled during lab):**

| Artefact | Kind | Before | After | Gate |
|---|---|---|---|---|
| Docstrings | Derived presence / decided content | 91.4% present, 1/5 useful | 91.8% present, 5/5 useful on decision points | `interrogate` + review |
| `docs/openapi.json` | Derived | absent | 14 paths, 22 schemas, gated | `git diff --exit-code` |
| `README.md` | Decided | 18 lines, 2 sections | 96 lines, 7 sections | handover test |
| Peer handover | Outcome | blocked at step 2 (missing migration) | completed in 16 min | peer record |
| `CHANGELOG.md` | Derived | hand-edited, 3 commits behind | generated, current | drift gate |

## Required Visuals and Training Assets

### Diagrams
1. **Derived versus decided** — *Purpose:* the module's organising distinction. *Elements:* two columns with their artefacts, staleness risk, mechanism (CI generation versus human review cadence) and the AI's role in each. *Style:* two-column card, one accent colour per kind. *Designer description:* "Left column with a gear icon feeding artefacts automatically; right column with a person icon and a review clock."
2. **The documentation gate in the pipeline** — *Purpose:* show drift detection as a control. *Elements:* the docs job with its four steps and the diff-exit-code mechanism expanded. *Style:* pipeline segment with the failing-diff path highlighted.
3. **The handover test** — *Purpose:* make the standard concrete. *Elements:* five checkpoints (run, test, understand, change, know who to ask) with the typical blocker at each. *Style:* horizontal checkpoint track with red blocker flags.
4. **Rukhsa documentation map** — *Purpose:* show where each artefact lives and who maintains it. *Elements:* repository tree with `docs/adr/`, `docs/specs/`, `docs/RUNBOOK.md`, `docs/openapi.json`, `docs/DATA_INVENTORY.md`, each tagged derived or decided and with an owner. *Style:* annotated file tree.

### Images (screenshots)
1. **A generated docstring wall** — *why:* recognisable, and the reason `interrogate` alone is insufficient; *content:* six consecutive functions with signature-restating docstrings.
2. **The OpenAPI drift gate failing** — *why:* the control in action; *content:* the CI log with the JSON diff and the error annotation.
3. **The rendered API reference** — *why:* what integrators actually consume; *content:* the fee endpoint with the SAR 3,780.00 example.

### Simulations
1. **Stale contract, broken integrator** — *Setup:* branch `lab7-stale-contract` plus a client generated from the old schema. *Expected behaviour:* the client fails parsing `service_fee`. *Learning objective:* an ungated derived artefact is a liability, not documentation.
2. **The blind handover** — *Setup:* pairs swap repositories with README-only access for twenty minutes. *Expected behaviour:* most are blocked within four minutes on an undocumented setup step. *Learning objective:* documentation is validated by use.

### Interactive Activities
- **Docstring triage (12 min):** twelve docstrings on cards; teams sort into "would change what I did" and "delete it," then rewrite three of the deleted ones to earn their place.
- **ADR archaeology (15 min):** teams are given three commits with no explanation and must reconstruct the decision and write the ADR, then compare with the real one held by the instructor.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `lab7-start` docstrings | Course repository | Python | 34 generated docstrings | The presence-without-usefulness baseline |
| `docs/openapi.json` (stale) | Course repository | JSON | 14 paths | The drift-gate exercise |
| Peer repositories | Participants' own Lab 6 output | Git | ~4,100 LOC | The handover test subject |

### Demo Requirements
- **Instructor demo (6 minutes):** open the starter's docstring wall on the projector and read three aloud in a flat voice until the room laughs, then show `interrogate` reporting 91.4% and passing. Rewrite one docstring live to record the `FOR UPDATE` lock, and ask who would now hesitate before removing that line. That contrast is the module in six minutes.

---

# Module 8 — Building the Complete Application and Professional Git Workflow
## بناء تطبيق متكامل وإدارة النسخ باستخدام Git

## Module Overview

**Purpose.** This module covers catalogue module 7 and delivers the **COMMIT** step, closing the contract. Everything built across the week becomes one application behind one pipeline. Participants wire the final Rukhsa components — inspection outcome, licence issuance, the public QR verification endpoint — then adopt the version-control practices that make high-velocity AI-assisted change safe: conventional commits, trunk-based development with short-lived branches, an AI-specific pull-request checklist, CODEOWNERS, and a five-gate CI pipeline that runs in 4 m 12 s.

**Business relevance.** Generation speed only becomes delivery speed if the path from a working change to production is fast and safe. A team producing forty reviewable changes a day against a long-lived branch model will spend its gains on merge conflicts; the same team on trunk-based development with a gating pipeline ships them. For a government service, the pipeline is also the audit evidence: it demonstrates that every merged change passed lint, types, security, tests and end-to-end verification, which is precisely what an assurance reviewer asks a supplier to prove.

**Industry use cases.**
- A team's AI-assisted throughput triples and its merge-conflict rate quadruples, because branches still live for two weeks.
- A regulator asks a supplier to demonstrate that no code reached production without a security scan; the answer is a branch-protection configuration and a pipeline history.
- A release must be rolled back at 22:00 and the team needs the tag, the changelog entry and the migration reversal to all exist and agree.

**Expected competencies.** After this module a participant can write conventional commits that support an automated changelog and a clean bisect; work trunk-based with short-lived branches and feature flags; review a pull request against an AI-specific checklist; configure CODEOWNERS and branch protection; and build a CI pipeline that gates lint, types, security, tests and E2E in under five minutes.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 8.1 | Write conventional commits that support automated changelogs and effective bisection | LO8, LO7 |
| 8.2 | Work trunk-based with short-lived branches and feature flags under high change volume | LO8 |
| 8.3 | Review a pull request against a checklist specific to AI-generated changes | LO8, LO1, LO5 |
| 8.4 | Configure branch protection, CODEOWNERS and a five-gate CI pipeline | LO8, LO5, LO6 |
| 8.5 | Integrate all Rukhsa components into one running, verifiable application | LO8, LO3 |

## Technical Content

### 1. Conventional commits, and why they matter more with an assistant

A conventional commit is `type(scope): subject`, optionally with a body and footers. Rukhsa uses `feat`, `fix`, `perf`, `refactor`, `test`, `docs`, `build`, `ci`, `chore`, and requires a spec or incident reference in the subject or footer.

The discipline earns three distinct things: an automated changelog (M7), a `git log --grep` that actually finds things, and — most importantly under AI assistance — **a history you can bisect**. M4's bisect worked because commits were small and each did one thing. A history of "wip", "fixes" and "generated updates" is not bisectable, and at forty changes a day it accumulates faster than any team can retrofit.

The rule that matters most: **the subject describes intent, not mechanism.** `feat(fees): assess application fee on eligibility (SPEC-004)` tells a reviewer why the change exists. `feat(fees): add create_assessment function` restates the diff, which the reader can already see. Assistants reliably produce the second form when asked to write a commit message, because they are looking at the diff and not at the specification — so the commit message is one more place where the human supplies what the assistant cannot.

### 2. Trunk-based development under high change volume

| | Long-lived feature branches | Trunk-based, short-lived branches |
|---|---|---|
| Branch lifetime | Days to weeks | Hours, at most one day |
| Integration | A large, painful merge at the end | Continuous, small |
| Conflict rate at 40 changes/day | Severe — the dominant cost | Low |
| Incomplete work | Hidden on a branch | On trunk behind a feature flag |
| Bisect quality | Poor — merge commits hide the introduction | Good — linear, small commits |
| Requires | Little | A fast, trustworthy pipeline |

The last row is the honest constraint: trunk-based development is only safe when the pipeline genuinely catches what it claims to. That is why this module comes after M5 and M6 rather than before them — a gate that does not test is a merge-approval machine.

Incomplete work goes to trunk behind a flag rather than living on a branch. Rukhsa's inspector-queue auto-assignment shipped disabled for three days while the assignment rule was tuned:

```python
if settings.feature_auto_assign_inspector:
    assign_inspector(session, application)
```

Two rules make flags a benefit rather than a new form of debt: every flag has an owner and a removal date recorded in `docs/FLAGS.md`, and a flag that survives its removal date is a bug with a ticket. Flags that outlive their purpose are how a codebase acquires a combinatorial explosion of untested paths.

### 3. The AI-change pull-request checklist

Rukhsa's PR template carries a section that a conventional template does not, and it is the operational residue of this entire course:

| Item | What the reviewer confirms |
|---|---|
| Spec reference | Every changed behaviour traces to a numbered spec or incident |
| Generation disclosure | Which parts were AI-generated, so review attention is allocated correctly |
| Diff budget | ≤ 150 reviewable lines, or a stated justification |
| Existence check | Every new API and dependency verified to exist, with the dependency justified |
| Assertion check | New tests assert values; none are vacuous or tautological |
| Data protection | No personal data in logs, URLs, responses or OpenAPI examples |
| Read record | The reviewer names one thing they questioned or changed |

The last item is deliberately unfalsifiable-proof: a reviewer who has read the diff can always name something, and a reviewer who has not, cannot. It is the cheapest available control against rubber-stamping and it changed Bunyan's median review time from five minutes to nineteen in the M1 case study.

Generation disclosure sometimes provokes an objection — that it stigmatises AI use. Frame it correctly: it is not a confession, it is **attention routing**. A reviewer who knows which hunk was generated allocates the seven-pass read to it and skims the rest, which is exactly what you want.

### 4. The five-gate pipeline

| Gate | Job | Runtime | Blocks on |
|---|---|---|---|
| 1. Lint & types | `ruff check`, `ruff format --check`, `mypy --strict` | 52 s | Any error |
| 2. Security | bandit, Semgrep, pip-audit, gitleaks | 1 m 09 s | Any HIGH/MEDIUM or any secret |
| 3. Tests | pytest unit + integration, coverage ≥ 85%, mutation on `fees`/`transitions` ≥ 70% | 1 m 47 s | Failure or threshold breach |
| 4. End-to-end | Playwright, 7 journeys against a booted stack | 3 m 58 s | Any journey failure |
| 5. Docs | interrogate, darglint, OpenAPI and changelog drift | 41 s | Drift or coverage breach |

Jobs run in parallel, so **pipeline wall time is 4 m 12 s** — the E2E job plus 14 s of runner start-up. That number is a design target, not an outcome: past roughly ten minutes, engineers begin working around the pipeline instead of with it, and every control in this course depends on the pipeline being something people wait for rather than avoid.

Branch protection converts the pipeline from advice to a control: `main` requires all five checks, at least one approving review, CODEOWNERS review on `.semgrep/`, `CLAUDE.md`, `docs/adr/` and `migrations/`, a linear history, and no force pushes. Without branch protection the pipeline is a dashboard.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *The commit subject states intent.* The diff already shows the mechanism.
- *Branches live hours, not weeks.* Integration cost grows superlinearly with branch age.
- *Incomplete work ships behind a flag, with an owner and a removal date.*
- *Disclose generation to route attention*, not to apportion blame.
- *A pipeline nobody waits for is a pipeline nobody obeys.* Keep it under five minutes.

**Common mistakes (each appears in the Lab 8 starter deliberately)**
1. A commit titled `feat: updates` covering three unrelated changes, which destroys bisect and the changelog simultaneously.
2. A feature branch six days old with 940 changed lines, presented as one pull request.
3. A feature flag with no owner and no removal date, still present four months later with both paths untested.
4. Branch protection configured to require checks but with "allow administrators to bypass" enabled — the control that is not one.
5. A pipeline where the E2E job runs *after* the unit tests sequentially, taking 9 m 40 s, so the team routinely merges without waiting.
6. A migration merged without its reverse, so the release cannot be rolled back.

**Production considerations**
- Tag releases with semantic versions and generate release notes from the commits. Rukhsa's `v1.0.0` is tagged at the end of Lab 8 and its notes are derived, not written.
- Every migration ships with a tested `downgrade`. The Day-5 drill is `alembic downgrade -1` followed by `upgrade head` on a seeded database.
- Cache dependency installs and Playwright browsers in CI; on Rukhsa this alone takes the pipeline from 7 m 30 s to 4 m 12 s, which is the difference between a control and an obstacle.
- Keep the pipeline definition under CODEOWNERS. A change that removes a gate must be as visible as a change to the security rules.

### 6. Real-world example walkthrough

Narrate this (5 minutes). A team adopted an assistant, tripled its change volume, and kept its two-week feature-branch model. Within a month, merge conflicts consumed more engineering time than the generation had saved: each branch had been generated against a `main` that no longer existed, and the conflicts were not textual but semantic — two branches had independently generated a `fee` helper with different rounding. Nothing in git could resolve that. They moved to trunk-based development with a hard rule that no branch survives a night, put incomplete work behind flags, and invested two days in cutting the pipeline from eleven minutes to four. Change volume stayed tripled; the conflict cost went to near zero. The lesson they articulated afterwards is the one to leave the room with: **AI assistance is a change-volume multiplier, and every part of your process that scales badly with change volume will fail first.** Branching strategy fails first. Review capacity fails second.

## Code Examples

### Licence issuance and the public QR verification endpoint

```python
# app/rukhsa/services/issuance.py
"""Issue a licence certificate after a passed inspection (SPEC-007).

WHY the QR token is a random secret rather than the licence number: the verify
endpoint is public and unauthenticated, so a guessable token would let anyone
enumerate every licence in the kingdom. The token proves possession of the
certificate; the licence number identifies it. Those are different jobs.
"""
from __future__ import annotations

import secrets
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.rukhsa.models.application import Application, ApplicationStatus
from app.rukhsa.models.licence import Licence
from app.rukhsa.services.transitions import transition

LICENCE_VALIDITY = timedelta(days=365)


def issue_licence(session: Session, application_id: uuid.UUID) -> Licence:
    """Issue exactly one licence for an application that passed inspection.

    The application row is locked FOR UPDATE for the same reason as the fee
    assessment (M4): two concurrent inspection callbacks would otherwise both
    observe "no licence yet" and issue two certificates for one business.

    Raises:
        LookupError: the application does not exist.
        ValueError: the application is not awaiting inspection.
    """
    application = session.scalar(
        select(Application).where(Application.id == application_id).with_for_update()
    )
    if application is None:
        raise LookupError("application_not_found")
    if application.status is not ApplicationStatus.AWAITING_INSPECTION:
        raise ValueError("invalid_status_for_issuance")

    year = datetime.now(UTC).year
    # Sequence per year, computed inside the lock so the number cannot collide.
    issued_this_year = session.scalar(
        select(func.count()).select_from(Licence).where(
            func.extract("year", Licence.issued_at) == year
        )
    ) or 0

    licence = Licence(
        application_id=application.id,
        licence_number=f"RKH-LIC-{year}-{issued_this_year + 1:06d}",
        issued_at=datetime.now(UTC),
        expires_at=datetime.now(UTC) + LICENCE_VALIDITY,
        # 32 bytes of entropy: not guessable, not enumerable, safe in a QR code.
        qr_token=secrets.token_urlsafe(32),
    )
    session.add(licence)
    transition(application, ApplicationStatus.ISSUED)
    session.commit()
    return licence
```

```python
# app/rukhsa/api/verify.py
"""Public licence verification (SPEC-007).

WHY this router is unauthenticated and deliberately minimal: an inspector, a
landlord or a customer scans the QR code on a printed certificate. The response
must prove the licence is genuine and current, and must expose nothing about the
applicant -- PDPL data minimisation applied to a public surface.
"""
from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.rukhsa.api.deps import get_session
from app.rukhsa.models.licence import Licence
from app.rukhsa.schemas.licence import LicenceVerification

router = APIRouter(tags=["verification"])


@router.get("/verify/{qr_token}", response_model=LicenceVerification)
def verify_licence(qr_token: str, session: Session = Depends(get_session)) -> LicenceVerification:
    """Verify a licence from its QR token.

    Returns the same 404 for an unknown token and a revoked licence's token, so
    the endpoint cannot be used to probe which tokens have ever existed. A valid
    but expired licence returns 200 with valid=false, because "this certificate
    is real and out of date" is genuinely different information for the scanner.
    """
    licence = session.scalar(select(Licence).where(Licence.qr_token == qr_token))
    if licence is None or licence.revoked_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="licence_not_found")

    now = datetime.now(UTC)
    return LicenceVerification(
        valid=licence.expires_at > now,
        licence_number=licence.licence_number,
        business_name_ar=licence.application.business_name_ar,
        business_name_en=licence.application.business_name_en,
        activity_code=licence.application.activity_code,
        city=licence.application.city,
        issued_at=licence.issued_at,
        expires_at=licence.expires_at,
        # Deliberately absent: national_id_hash, applicant name, documents,
        # fee amounts, inspection notes. A public endpoint returns the minimum
        # that answers the scanner's question.
    )
```

### The five-gate pipeline

```yaml
# .github/workflows/ci.yml
# WHY five parallel jobs rather than one sequential one: wall time is the E2E job
# (3 m 58 s) plus runner start-up = 4 m 12 s, instead of 8 m 27 s sequential. Past
# ~10 minutes engineers work around the pipeline, and every control in this course
# depends on the pipeline being something people wait for.
name: ci

on:
  pull_request:
  push:
    branches: [main]

concurrency:                 # a new push cancels the previous run on the same ref
  group: ci-${{ github.ref }}
  cancel-in-progress: true

env:
  RUKHSA_DATABASE_URL: postgresql://rukhsa:rukhsa@localhost:5432/rukhsa_test
  RUKHSA_SECRET_KEY: ${{ secrets.CI_SECRET_KEY }}
  RUKHSA_NATIONAL_ID_SALT: ${{ secrets.CI_NID_SALT }}

jobs:
  lint-and-types:                                   # gate 1 -- 52 s
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11", cache: pip }
      - run: pip install -r requirements.lock
      - run: ruff check app tests
      - run: ruff format --check app tests
      - run: mypy --strict app/rukhsa

  security:                                         # gate 2 -- 1 m 09 s
    uses: ./.github/workflows/security.yml
    secrets: inherit

  tests:                                            # gate 3 -- 1 m 47 s
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: rukhsa
          POSTGRES_PASSWORD: rukhsa
          POSTGRES_DB: rukhsa_test
        ports: ["5432:5432"]
        # Without a healthcheck the suite races the container and fails ~1 run in 5.
        options: >-
          --health-cmd "pg_isready -U rukhsa" --health-interval 5s
          --health-timeout 5s --health-retries 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11", cache: pip }
      - run: pip install -r requirements.lock
      - run: alembic upgrade head
      - name: unit + integration with coverage floor
        run: pytest -q --cov=app/rukhsa --cov-branch --cov-fail-under=85
      # Mutation runs only where correctness is financial or legal (M6).
      - name: mutation ratchet
        run: |
          mutmut run --paths-to-mutate app/rukhsa/services/fees.py,app/rukhsa/services/transitions.py
          python scripts/check_mutation_score.py --min 70

  e2e:                                              # gate 4 -- 3 m 58 s
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_USER: rukhsa, POSTGRES_PASSWORD: rukhsa, POSTGRES_DB: rukhsa_test }
        ports: ["5432:5432"]
        options: >-
          --health-cmd "pg_isready -U rukhsa" --health-interval 5s --health-retries 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11", cache: pip }
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: npm, cache-dependency-path: web/package-lock.json }
      - run: pip install -r requirements.lock && alembic upgrade head && npm ci --prefix web
      # Cached browsers: this single cache step removes ~2 minutes from the job.
      - uses: actions/cache@v4
        with: { path: ~/.cache/ms-playwright, key: pw-${{ hashFiles('web/package-lock.json') }} }
      - run: npx --prefix web playwright install --with-deps chromium
      - run: npx --prefix web playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with: { name: playwright-trace, path: web/test-results/ }

  docs:                                             # gate 5 -- 41 s
    uses: ./.github/workflows/docs.yml
```

## Hands-on Lab 8 — Assemble Rukhsa and Green the Pipeline

| | |
|---|---|
| **Objective** | Wire the final components (inspection outcome, licence issuance, QR verification), adopt trunk-based practices, open a pull request against the AI-change checklist, pass all five gates in under five minutes, and tag `v1.0.0` |
| **Duration** | 55 minutes |
| **Setup** | Lab 7 repository, GitHub repository with Actions enabled, `commitlint` hook installed, `git checkout lab8-start` |

**Instructions & tasks**

1. *(8 min)* Configure the workflow: install the `commit-msg` hook enforcing conventional commits, add `.github/PULL_REQUEST_TEMPLATE.md` with the seven-item AI-change checklist, add `CODEOWNERS` covering `.semgrep/`, `CLAUDE.md`, `docs/adr/`, `migrations/` and `.github/workflows/`. Attempt a commit titled `updates` and confirm it is rejected.
2. *(15 min)* On a branch named `feat/licence-issuance`, generate and harden `issue_licence` and the `/verify/{qr_token}` endpoint from `SPEC-007`. Apply the full contract: spec, generate, seven-pass read, tests, security tools, commit. Keep the diff under 150 lines — split into two commits if needed.
3. *(8 min)* Add the inspector auto-assignment behind `settings.feature_auto_assign_inspector`, defaulting to off, and record it in `docs/FLAGS.md` with an owner and a removal date. Prove both paths run by toggling the flag in a test.
4. *(12 min)* Add `.github/workflows/ci.yml` with all five gates and push. Fix whatever fails — expect at least the mutation ratchet and a `mypy --strict` finding on the generated issuance code. Record the wall time; if it exceeds 5 minutes, add the Playwright browser cache and re-measure.
5. *(7 min)* Open the pull request, complete the checklist honestly (including the generation disclosure), and have your pair partner review it and name one thing they questioned. Enable branch protection requiring all five checks, one approval and a linear history — with administrator bypass **disabled**.
6. *(5 min)* Merge, then tag and verify the release: `git tag -a v1.0.0 -m "Rukhsa v1.0.0"`, generate release notes from the commits, and prove rollback with `alembic downgrade -1 && alembic upgrade head` on the seeded database.

**Expected output**
```
$ git commit -m "updates"
✗ subject may not be empty / type may not be empty [subject-empty, type-empty]
husky - commit-msg hook exited with code 1

$ git commit -m "feat(licence): issue certificate with QR verification (SPEC-007)"
[feat/licence-issuance 4b91c7e] feat(licence): issue certificate with QR verification (SPEC-007)
 4 files changed, 138 insertions(+)

$ gh pr checks
lint-and-types   pass   52s
security         pass   1m9s
tests            pass   1m47s
e2e              pass   3m58s
docs             pass   41s
All checks passed — wall time 4m12s

$ curl -s localhost:8000/verify/8Kx2mQ...  | jq '{valid, licence_number, national_id_hash}'
{ "valid": true, "licence_number": "RKH-LIC-2026-000001", "national_id_hash": null }
```

**Acceptance criteria**
- A non-conventional commit message is rejected locally by the hook.
- All five gates pass on the pull request with a wall time ≤ 5 minutes.
- Branch protection requires all five checks and one approval, with administrator bypass disabled.
- The feature flag is recorded in `docs/FLAGS.md` with owner and removal date, and both paths are tested.
- `v1.0.0` is tagged; `alembic downgrade -1 && upgrade head` succeeds on seeded data.
- The public verification response contains no personal data beyond the bilingual business name.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| E2E job flaky, ~1 run in 5 | Suite races the Postgres container | Add the `pg_isready` healthcheck with retries — never a `sleep` |
| Pipeline wall time 7 m 30 s | Playwright browsers downloaded every run | Cache `~/.cache/ms-playwright` keyed on the lock file |
| `mypy --strict` fails only in CI | Local run used a looser config or a stale cache | Run `mypy --strict` locally; delete `.mypy_cache`; pin the version in the lock file |
| Merge allowed despite a red check | Administrator bypass enabled | Disable it — a bypassable gate is a dashboard |

**Instructor notes.** Step 5's peer review is the closing ritual of the week: insist the reviewer names one concrete thing, and read two of them to the room. Step 4 will produce genuine CI failures — resist fixing them for participants; a first red pipeline that they green themselves is the strongest possible end to the course. Watch the wall-time numbers on the board; the pairs who cached the browsers finish at 4 m 12 s and the ones who did not at 7 m 30 s, which makes the "pipelines must be fast to be obeyed" argument for you. Fast finishers: have them add a `release` workflow that tags and publishes derived release notes automatically on a merge to `main`.

## Mini Exercises

**Quiz (5 questions)**
1. Why does branch age matter more under AI assistance? → change volume is higher, so divergence accumulates faster and conflicts become semantic, not textual.
2. What does the "read record" item on the PR checklist actually control? → rubber-stamping; a reviewer who read the diff can always name something, one who did not cannot.
3. Why is generation disclosure attention routing rather than blame? → it tells the reviewer where to spend the seven-pass read.
4. Why must every feature flag have a removal date? → otherwise untested code paths accumulate combinatorially.
5. What makes branch protection a control rather than advice? → required checks with administrator bypass disabled and no force pushes.

**Debugging exercise.** Branch `lab8-bypass` has all five gates configured and "allow administrators to bypass" enabled; a change with a failing security gate is on `main`. Have participants find how it got there from the merge history and write the two configuration changes that make it impossible.

**Design exercise.** Rukhsa must ship a change to the fee formula that takes effect on a future date. Design the rollout: flag or migration, how it is tested, how it is rolled back, and which of the five gates proves it is safe.

**Discussion questions.**
- Trunk-based development requires trusting the pipeline. What would have to be true of your current pipeline before you would trust it that far — and is the honest answer "nothing, because we do not test enough"?
- If disclosure of AI generation routes reviewer attention, will teams under delivery pressure disclose honestly? What makes the answer yes?

## Case Study — Scaling Change Volume at "Thabat" (ثبات) Industrial Systems

**Scenario.** "Thabat" (ثبات), a Dammam supplier of industrial monitoring systems for petrochemical plants, adopted coding assistants across 34 engineers on four products. Change volume rose from roughly 40 to 130 merged pull requests a week within two months. Nothing about the branching model, review process or pipeline changed. By month three, the median pull request waited 3.1 days for review, merge conflicts consumed an estimated 22% of engineering time, and two releases were rolled back because a change had merged with a red pipeline through an administrator bypass that had been enabled during an unrelated incident and never disabled.

**Business context.** Thabat's systems run in safety-relevant plant environments; a defective release is not merely a service issue, and the client's assurance regime requires evidence that every change passed the defined controls. The bypassed merges made that evidence untrue for a period the firm had to disclose.

**Technical challenge.** Every individual practice at Thabat was defensible at 40 pull requests a week and none of them survived 130. The pipeline took 14 minutes, which was tolerable at the old volume and became the reason engineers batched changes into larger branches — which raised conflicts, which raised review time, which raised branch age. The team must break that loop without reducing change volume, and must restore the integrity of its assurance evidence.

**Constraints.** Cannot reduce delivery commitments; the assurance regime's control set is fixed and auditable, so gates can be made faster but not removed; four products share a monorepo with a single pipeline; two of the four have long-running hardware-in-the-loop tests that genuinely take 20 minutes and cannot be shortened.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) measure the loop, not the symptoms — branch age, pipeline duration, review latency and conflict rate on one chart, because they drive each other; (2) attack pipeline duration first since it is upstream of everything else: parallelise, cache, and split the hardware-in-the-loop suite into a required-but-asynchronous gate that blocks the release rather than the merge; (3) cap branch age with a hard rule and feature flags for incomplete work; (4) distribute review capacity with CODEOWNERS by area rather than a central reviewer pool, and adopt the AI-change checklist so reviews are faster *and* better targeted; (5) remove administrator bypass permanently and treat the incident that enabled it as a runbook gap — the emergency path must be a documented, logged procedure, not a toggle someone forgets.

**Discussion questions.**
1. Every practice at Thabat was defensible at the old volume. What is the general lesson about adopting a velocity multiplier into an unchanged process?
2. The 20-minute hardware test cannot be shortened. Where in the delivery path does it belong, and what do you give up by moving it?
3. The bypass was enabled during an incident and forgotten. Design the emergency-merge procedure that makes this impossible without preventing genuine emergency response.
4. Thabat had to disclose that its assurance evidence was untrue for a period. What automated evidence would you keep so that such a claim is verifiable rather than reconstructed?

## Benchmarks and Evaluation

| Metric | Category | Target after M8 | How measured |
|---|---|---|---|
| Pipeline wall time | Delivery speed | ≤ 5 min (target 4 m 12 s) | GitHub Actions run duration |
| Gates passing on the PR | Quality | 5/5 | `gh pr checks` |
| Conventional-commit compliance | History quality | 100% on the branch | `commitlint` hook + `git log` |
| Branch protection | Control | 5 checks required, bypass disabled, linear history | repository settings review |
| Rollback proven | Operability | `downgrade -1` + `upgrade head` succeed on seeded data | live run |

**Example benchmark table (filled during lab):**

| Job | Runtime | Blocks on | Cached |
|---|---|---|---|
| lint-and-types | 52 s | ruff / mypy --strict error | pip |
| security | 1 m 09 s | any HIGH/MEDIUM, any secret, phantom dependency | pip |
| tests | 1 m 47 s | failure, coverage < 85%, mutation < 70% | pip |
| e2e | 3 m 58 s | any of 7 Playwright journeys | pip, npm, browsers |
| docs | 41 s | docstring < 90%, OpenAPI or changelog drift | pip |
| **Pipeline wall time** | **4 m 12 s** | any gate | — |

## Required Visuals and Training Assets

### Diagrams
1. **The five-gate pipeline** — *Purpose:* the closing image of the course. *Elements:* five parallel jobs with runtimes, converging on a protected `main`, with the wall-time calculation shown. *Style:* parallel-lane pipeline, protected branch drawn as a gate. *Designer description:* "Five horizontal lanes of differing length feeding one locked door labelled main."
2. **Branch age versus conflict cost** — *Purpose:* justify trunk-based development quantitatively. *Elements:* conflict cost curve against branch age, with Thabat's 40 and 130 PR/week points marked. *Style:* single curve, two annotated points.
3. **The contract, closed** — *Purpose:* tie all eight modules together. *Elements:* the six-step contract loop from M1 with each step labelled by the module that taught it and the Rukhsa artefact it produced. *Style:* the M1 loop, completed and annotated — the final slide of the course.
4. **Rukhsa, complete** — *Purpose:* what the participants built. *Elements:* the full system from the M1 context diagram with every component now shaded as delivered, tests and gates attached to each. *Style:* the Day-1 diagram, filled in.

### Images (screenshots)
1. **`gh pr checks` all green at 4 m 12 s** — *why:* the target state made concrete; *content:* the five checks with their durations.
2. **A rejected commit message** — *why:* the hook as a local control; *content:* the commitlint error for `updates`.
3. **Branch protection settings** — *why:* participants must configure this exactly; *content:* required checks listed, administrator bypass unchecked.

### Simulations
1. **The bypassed gate** — *Setup:* branch `lab8-bypass` with a red security check merged to `main` by an administrator. *Expected behaviour:* the history shows a merge with a failing check. *Learning objective:* a bypassable control is not a control.
2. **The slow pipeline** — *Setup:* the same suite without caching, running sequentially at 9 m 40 s. *Expected behaviour:* pairs begin merging without waiting within two rounds. *Learning objective:* pipeline duration determines whether the pipeline is obeyed.

### Interactive Activities
- **Commit-message rewrite (10 min):** ten real commit subjects from a messy history; teams rewrite them as conventional commits stating intent, then check whether the resulting changelog reads coherently.
- **Peer PR review round (15 min):** each participant reviews one peer's Lab 8 pull request against the seven-item checklist and must name one concrete question — this doubles as capstone preparation.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `lab8-start` history | Course repository | Git | 6 planted workflow defects | The workflow remediation target |
| `.github/workflows/` | Course repository, completed by participants | YAML | 3 workflows | The five-gate pipeline |
| Seeded Rukhsa database | `python -m app.rukhsa.seed` | PostgreSQL | 400 applications, 1,650 documents | Rollback and E2E verification |

### Demo Requirements
- **Instructor demo (8 minutes):** open a pull request live, let all five gates run on the projector while narrating what each proves, then merge, tag `v1.0.0`, and scan the QR code on the generated certificate with a phone to hit the public verify endpoint. Ending the course with a physical scan of a certificate the room built in five days is the right final image.

---

# Final Capstone Project

## Title: Rukhsa v1.0 — Shipping a Municipal Licensing Portal with an AI Assistant and an Engineering Contract

## Project Scenario

You are the engineer accountable for **Rukhsa (رخصة)**, a municipality's commercial-licensing portal. A citizen applies for a licence with supporting documents; the service validates eligibility against municipal rules, routes a field inspection, prices the application in SAR, takes payment, and issues a certificate that anyone can verify from a QR code. You built every component this week with an AI assistant — and you reviewed, tested, hardened and documented every one of them. The capstone is the integration plus your own extension, and it is graded on the *evidence* your repository produces, not on the demo narration. The thesis of the course is the grading philosophy: velocity is assumed; the discipline is what is assessed.

## Requirements

**Mandatory (maps to grading rubric):**

1. **The review contract, evidenced (LO1):** `CLAUDE.md` with stack pins, layering rules, forbidden patterns and PDPL rules; a 150-line diff budget enforced by a hook; every pull request carries the AI-change checklist with a completed generation disclosure and a named reviewer question.
2. **Specification and architecture (LO2):** ≥ 4 numbered specs with non-goals, error tables and concrete-value acceptance criteria; ≥ 4 ADRs each naming a rejected alternative; a domain model with an enum-typed state machine and `Numeric(12,2)` money; `docs/DATA_INVENTORY.md` listing every personal-data field with its lawful basis and retention.
3. **Generation and optimisation (LO3):** the applications, documents, eligibility, fees, inspection and issuance components built under the contract; the list endpoint at 2 queries and ≤ 100 ms p95 (from 101 / 1,840 ms), evidenced by the committed benchmark harness; no `float` on any money path.
4. **Debugging and root cause (LO4):** the fee race condition fixed with `FOR UPDATE` **and** a partial unique index; a deterministic load reproduction retained as a regression test proving 0 duplicates at concurrency 200 with losing requests receiving 409; `LAB4_DIAGNOSIS.md` recording one rejected AI hypothesis and its disproving evidence.
5. **Security-first (LO5):** all six OWASP classes remediated; bandit, Semgrep (with ≥ 2 of your own rules), gitleaks and pip-audit at zero findings and blocking on the pull request; every dependency justified and pinned with hashes; no phantom packages.
6. **Tests that assert (LO6):** ≥ 110 tests in pyramid proportion; ≥ 85% line coverage; mutation score ≥ 70% on `fees` and `transitions` with the baseline committed as a ratchet; ≥ 5 Hypothesis properties; ≥ 5 Playwright journeys including issuance and QR verification.
7. **Documentation that survives (LO7):** `docs/openapi.json` derived and drift-gated; docstring coverage ≥ 90% with `darglint` clean; a README passing a peer handover test in ≤ 20 minutes; a runbook with ≥ 3 entries; a derived `CHANGELOG.md`.
8. **Ship it (LO8):** trunk-based history of conventional commits; branch protection requiring all five gates with administrator bypass disabled; pipeline wall time ≤ 5 minutes; `v1.0.0` tagged; a proven migration rollback.

**One extension (choose at least one):**
- Arabic/English bilingual rejection reasons rendered end-to-end, with a Playwright journey asserting the Arabic string.
- An inspector mobile view consuming the committed OpenAPI contract via a generated client, with a contract-drift test.
- A scheduled invariant monitor (duplicate active assessments, licences without payments) that fails CI on a seeded violation.
- Fee-schedule versioning with an effective date, an ADR, and property tests proving historic assessments are unaffected.
- A `slopsquat-guard` CI step that resolves every requirement against the index and fails on any package younger than 90 days without an allow-list entry.

## Architecture (target state)

```
citizen (web)                    RUKHSA API (FastAPI)                    PostgreSQL 16
   │  submit + documents   ┌──────────────────────────────┐        ┌────────────────────┐
   ├──────────────────────►│ api/  routers (no logic)     │        │ applications (enum │
   │                       │   │                          │        │   status, uq ref)  │
   │  status / fee         │   ▼                          │◄──────►│ documents (sha256) │
   ◄───────────────────────┤ services/ transactions       │        │ eligibility_checks │
   │                       │   transitions · eligibility  │        │ inspections        │
   │  pay (SADAD stub)     │   fees(Decimal) · assessment │        │ fee_assessments    │
   ├──────────────────────►│   issuance (FOR UPDATE)      │        │   (partial uq      │
   │                       │   │                          │        │    WHERE active)   │
inspector ──inspection────►│   ▼                          │        │ payments           │
   │                       │ repositories/ (selectinload) │        │ licences (qr_token)│
public  ──GET /verify/{t}─►│ minimal, unauthenticated     │        └────────────────────┘
                           └──────────────────────────────┘
  CONTRACT: SPEC ─► GENERATE ─► READ(7 passes) ─► TEST ─► HARDEN ─► COMMIT
  GATES:  lint+types 52s │ security 1m09s │ tests 1m47s │ e2e 3m58s │ docs 41s  =  4m12s
  PDPL:   national_id hashed · structural log redaction · minimal public verify response
```

## Deliverables

1. Git repository URL with full conventional-commit history, branch protection configured, and `v1.0.0` tagged.
2. A running Rukhsa application startable with one command (`make up`) and seedable with one more, completing the full citizen journey to a verifiable licence.
3. `BENCHMARKS.md` with the course benchmark tables filled from *your own* runs: query counts and p95 before/after, mutation score progression, the four security tools' baseline and final counts, and pipeline job timings.
4. `docs/` containing ≥ 4 specs, ≥ 4 ADRs, the derived OpenAPI contract, `DATA_INVENTORY.md`, `RUNBOOK.md`, `FLAGS.md` and a derived `CHANGELOG.md`.
5. A 6-minute demo: one-command start, the citizen journey to an issued licence, a live QR verification, the load reproduction proving 0 duplicates, and the pull-request page showing five green gates.
6. `DECISIONS.md`: five one-paragraph engineering decisions with rationale — for example the `selectinload` versus `joinedload` choice, the 404-not-403 IDOR response, the mutation-gate scope, the flag removal date, and one thing you refused to let the assistant do.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: `CLAUDE.md`, specs, ADRs, domain model migrated | End Day 1 | instructor spot-check of specs and ADRs |
| M-B: applications/documents/eligibility API under the contract, N+1 removed | End Day 2 | benchmark harness shows 2 queries, ≤ 100 ms p95 |
| M-C: race fixed with lock + constraint; security gate at zero | End Day 3 | load reproduction 0 duplicates; four tools green |
| M-D: 110+ tests, mutation ≥ 70%, docs gated, handover test passed | End Day 4 | mutation report + peer handover record |
| M-E: assembled, five gates green, tagged, demo | Day 5 H5 | rubric scoring from the repository first |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Review contract & AI discipline | 15 | Contract evidenced in every PR; disclosure and reviewer question present; diff budget held throughout | Contract mostly applied; one or two oversized or unreviewed changes | Accepted generations; no disclosure; rubber-stamped PRs |
| Specification & architecture | 15 | ≥ 4 specs with non-goals and concrete ACs; ≥ 4 ADRs with real alternatives; clean layering; data inventory complete | Specs present but some ACs vague; ADRs thin or partly retrospective | No non-goals; unverifiable ACs; ADRs written to justify the code |
| Generation quality & performance | 15 | 2 queries, ≤ 100 ms p95, measured with the committed harness; no float money; complexity reviewed | Optimised but evidence partial, or one complexity defect remains | N+1 present; float money; unmeasured claims |
| Debugging & root cause | 10 | Deterministic reproduction retained; 0 duplicates at concurrency 200 with 409s; rejected hypothesis documented | Fixed but reproduction weak, or only the constraint applied (500s) | Symptom hidden; swallowed exception; no reproduction |
| Security-first | 15 | All four tools zero and blocking; ≥ 2 own Semgrep rules; dependencies justified and hash-pinned; PDPL respected end-to-end | Findings cleared but gate non-blocking, or dependency justification thin | Any HIGH finding, secret in history, IDOR, or personal data exposed |
| Tests that assert | 15 | ≥ 110 tests in proportion; ≥ 85% coverage; mutation ≥ 70% ratcheted; ≥ 5 properties; ≥ 5 E2E journeys | Thresholds met but mutation near the floor, or E2E thin | Vacuous or tautological tests; inverted pyramid; mutation < 50% |
| Documentation, workflow & demo | 15 | Handover test passed ≤ 20 min; OpenAPI drift-gated; conventional history; protection with no bypass; ≤ 5 min pipeline; crisp demo | Documentation good but handover blocked once; pipeline 5–8 min | Stale contract; unusable README; bypassable protection; unclear demo |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository first, demo second*: open the Actions tab, the pull-request history, the mutation report and the benchmark file before watching anything. The whole course argues that the evidence is in the pipeline, and the grading must model that.
- Anti-pattern flags that cap a criterion at 70%: any `float` on a money path; a vacuous `is not None` assertion in a new test; a security gate configured as non-blocking; administrator bypass enabled; a PR with no generation disclosure or reviewer question; a retrospective ADR; personal data in a log, URL, OpenAPI example or the public verify response.
- Verify one claim live per participant. Good choices: run their load reproduction and watch for 409s rather than 500s; ask them to add one field to a response model and show the OpenAPI drift gate catching it; or ask them to name one thing they refused to let the assistant do and why.

## Bonus Tasks (for early finishers / distinction seekers)

1. Add a contract test that generates a client from `docs/openapi.json` and fails CI when a response model changes incompatibly.
2. Extend mutation testing to `services/eligibility.py` and raise its score above 70% without adding E2E tests.
3. Implement the slopsquat guard: resolve every requirement against the index and fail on any package under 90 days old that is not allow-listed with a justification.
4. Add an invariant monitor job (duplicate active assessments, licences without a settled payment, applications stuck in `awaiting_payment` beyond 30 days) and prove it fails on a seeded violation.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Name the six steps of the review contract in order. → SPEC, GENERATE, READ, TEST, HARDEN, COMMIT.
**Q2.** In `shipped_value = velocity × (1 − defect_rate) − rework`, which term does an assistant worsen? → defect_rate.
**Q3.** Why does reviewer defect-detection fall to ~22% on diffs over 400 lines? → reviewers disengage and rubber-stamp; hence the 150-line budget.
**Q4.** Which specification section most effectively prevents invented features? → non-goals.
**Q5.** Why must an acceptance criterion carry concrete values? → so it can fail, and so it converts directly into a test.
**Q6.** When do you write an ADR? → when reversing the decision would cost more than a day.
**Q7.** Which diff-read pass catches an N+1? → pass 4, data access.
**Q8.** What single change took the Rukhsa list endpoint from 101 queries to 2? → `selectinload(Application.documents)`.
**Q9.** Why is `joinedload` not automatically better? → it duplicates parent rows, breaking `LIMIT`-based pagination.
**Q10.** What is slopsquatting? → registering packages under names assistants commonly hallucinate, so a generated install fetches attacker code.
**Q11.** What defines a legitimate refactor diff? → the existing tests pass unchanged.
**Q12.** What exit code makes `git bisect run` skip an unevaluable commit? → 125.
**Q13.** Why is a unique constraint alone an incomplete fix for the fee race? → the losing request gets a 500; the `FOR UPDATE` lock gives it a clean 409.
**Q14.** Why is `allow_origins=["*"]` with `allow_credentials=True` especially dangerous? → any site can make credentialed cross-origin calls as the logged-in citizen.
**Q15.** Why scope authorisation in the query rather than after the fetch? → the unauthorised row is never loaded, and the scope is structurally checkable.
**Q16.** What does a surviving mutant prove? → some behaviour can change with no test failing — it is unasserted.
**Q17.** Why did coverage stay at 88% while mutation went 41% → 77%? → coverage measures execution, not assertion.
**Q18.** When is mocking appropriate? → only across a boundary you do not own, such as SADAD or object storage.
**Q19.** Give two derived and two decided documentation artefacts. → derived: OpenAPI, changelog; decided: ADRs, runbook.
**Q20.** What makes branch protection a control rather than advice? → required checks with administrator bypass disabled and no force pushes.

## Practical Assessments

**PA-1 (30 min, Day 3):** Given a branch containing a generated endpoint with an IDOR, an f-string SQL query and a hardcoded key, perform a seven-pass diff read, remediate all three, and make the four security tools green. Scored on the review record naming the pass that found each defect (40%), correctness of the fixes including query-scoped authorisation (40%), and the CI evidence (20%).

**PA-2 (30 min, Day 4):** Given a generated test suite at 88% coverage and 41% mutation score, raise the mutation score above 70% without touching the implementation. Scored on the strength of the added assertions (50%), the boundary and property cases identified from surviving mutants (30%), and the reasoning recorded about why coverage did not move (20%).

**PA-3:** Capstone (rubric above) — 40% of the course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (8 labs) | 30% | checkpoint commits, benchmark tables, expected outputs reproduced |
| PA-1 + PA-2 | 20% | remediated branches, review records, mutation report |
| Quiz | 10% | 10-question selection |
| Capstone (Rukhsa v1.0) | 40% | rubric, repository-and-pipeline first |

Badge issuance (AI-assisted software engineering badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical `LAB3_REVIEW.md`, `LAB4_DIAGNOSIS.md` or benchmark artefacts across repositories are checked, as are commits authored outside the camp window) **and** no PDPL red flags — personal data in logs, URLs, OpenAPI examples or the public verification response, or any evidence that real personal data or non-synthetic source code was submitted to a third-party assistant.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course organisation repositories; push all checkpoint tags (`lab1-start` … `lab8-start`, `lab1-solution` … `lab8-solution`) and the defect branches (`lab1-hardcoded-secret`, `lab2-float-money`, `lab3-hallucinated-api`, `lab3-refactor-drift`, `lab4-swallowed`, `lab4-constraint-only`, `lab5-verify-false`, `lab6-mocked-service`, `lab7-stale-contract`, `lab8-bypass`)
- [ ] Regenerate the synthetic Rukhsa dataset with the pinned seed; verify 500 applicants, 148 activities, 400 seeded applications and 1,650 documents, and confirm every national ID is synthetic with a valid check digit
- [ ] Dry-run all 8 labs end-to-end on a clean machine **and** in the Codespaces devcontainer; confirm Lab 4's race reproduces (it needs ≥ 4 uvicorn workers) and Lab 8's pipeline lands at ~4 m 12 s with caches warm
- [ ] Confirm assistant licensing and proxy access for every participant; prepare the "manual mode" lab variant in case access fails on Day 1
- [ ] Verify the pinned toolchain installs from the lock file: FastAPI 0.115, SQLAlchemy 2.0.35, Alembic 1.13, pytest 8.3.3, Hypothesis 6.112, mutmut 2.5, Playwright 1.47, ruff 0.6.9, mypy 1.11.2, bandit 1.7.9, Semgrep 1.85.0
- [ ] Print A4 posters: the six-step contract, the seven-pass diff read, the OWASP-to-generated-snippet gallery, the test pyramid with mutation gauges, the five-gate pipeline
- [ ] Load fixtures to the shared drive: `INC-0007.md`, the fee circular extract, the ten plausible-fabrication statements, the twelve assertion cards, the stale OpenAPI client
- [ ] Prepare the shared leaderboard (p95 improvement, mutation score, pipeline wall time) and the fabricated-facts board for Day 1
- [ ] Confirm the classroom network allows the package index, the container registry, GitHub Actions and Playwright browser downloads; pre-pull images and browsers to a local mirror in restricted environments

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.11, Node 20, Docker Desktop (WSL2 on Windows) or Colima, git, and a GitHub account with Actions enabled on a personal repository
- [ ] `pip install -r requirements.lock` from the course repository (FastAPI, SQLAlchemy, Alembic, pytest, Hypothesis, mutmut, ruff, mypy, bandit, semgrep, pip-audit, structlog, py-spy)
- [ ] `npm ci --prefix web && npx playwright install chromium`; verify `npx playwright --version`
- [ ] `docker compose up -d db` and verify `psql` connectivity on 5432; install `gitleaks` on PATH
- [ ] An approved AI coding assistant configured in the IDE and authenticated (Claude Code, Copilot or Cursor) — confirm it works through your corporate proxy
- [ ] Clone the course repository and run `make doctor`; it validates every tool above and prints ✓/✗ per item

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Assistant blocked by the corporate proxy | High | Pre-verify on Day 0; configure `HTTPS_PROXY` in the IDE; browser-based fallback with manual diff paste |
| Participants accept generated diffs without reading | High | Enforce the navigator-reads-aloud pairing ritual from Lab 1 Hour 3; make the read record a PR requirement |
| Lab 4 race will not reproduce | High | Run uvicorn with `--workers 4`; widen the window with a small sleep between read and write |
| `mutmut` run exceeds ten minutes | Medium | Restrict `--paths-to-mutate` to `fees.py` and `transitions.py` — the proportionate gate |
| Integration tests pass alone, fail together | Medium | The transactional `session` fixture; never a second engine inside a test |
| Playwright flakiness / fixed waits | Medium | Web-first `expect()` assertions only; ban `sleep`; add the Postgres healthcheck |
| `mypy --strict` fails only in CI | Medium | Pin the version in the lock file; clear `.mypy_cache`; run strict locally before pushing |
| Pipeline wall time over eight minutes | Medium | Cache pip, npm and `~/.cache/ms-playwright`; parallelise the five jobs |
| `CREATE INDEX CONCURRENTLY` fails in Alembic | Low | Use `autocommit_block()`, or drop `CONCURRENTLY` for the lab database |
| Participants paste real data into the assistant | Low but critical | Say the rule in Hour 1 and again on Day 3; use only synthetic fixtures; treat any occurrence as a teaching moment, immediately and without embarrassment |

## Timing Recommendations

- Protect the seven-pass diff read (Lab 3a, 20 min) and the mutation-testing baseline (Lab 6a, 12 min) at full length; they are the two skills the capstone is graded on most heavily.
- If a cohort is strong: pull the slopsquat guard and the contract-drift test into main scope on Day 5, and run the Day-4 handover test across three repositories instead of two.
- If a cohort is weak: run Lab 4's bisect as a guided demo rather than a solo exercise, but never skip the *reproduction* — building it is the module's thesis made physical.
- **Hard rule:** Lab 8's pipeline work (Day 5 Hour 2) must start on time. A participant who has never seen their own pipeline go green has not completed this course. Cut discussion, not pipeline time.
- Reserve Day 1 Hour 3's uncontracted-versus-contracted comparison even if `make doctor` overruns; every later module refers back to those two branches.

## Discussion Prompts (use during transitions)

1. "You generated that in eleven minutes. How long would it take you to convince a regulator it is correct — and which of those two numbers is your actual delivery time?"
2. "Your assistant just told you something confident about Saudi municipal licensing. What would it look like if that were invented, and how would you know?"
3. "Your test suite is green, your coverage is 88%, and the defect shipped. What did the suite actually measure?"
4. "If the assistant wrote 80% of the lines, what exactly is your name on the commit claiming?"
5. "Which part of your current process would break first if your team's change volume tripled next Monday?"

## Wrap-up (Day 5 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it, on one slide: the contract (M1), specification and architecture (M2), generation and optimisation (M3), debugging and root cause (M4), security-first (M5), tests that assert (M6), documentation (M7), workflow and pipeline (M8). Then show the M1 contract loop completed — the same image that opened the camp.
- Forward pointer: **SDA-AIE-305 (Developing Generative AI Solutions)** takes this discipline and applies it to building systems whose *runtime* is a generative model rather than only whose development is — the same review, testing and governance obligations, now applied to non-deterministic behaviour in production. Participants who enjoyed M5 and M6 should also revisit **SDA-FND-110** for the responsible-use foundations underpinning the PDPL rules used all week.
- Collect: repository URLs, `BENCHMARKS.md`, `DECISIONS.md`, the `docs/` folder and the pull-request links showing five green gates. Issue badge recommendations within 5 working days, and send each participant their peer's handover-test blocker list — it is the most actionable feedback in the course.

---

*End of instructor package. All code samples target Python 3.11, FastAPI 0.115, SQLAlchemy 2.0, Alembic 1.13, PostgreSQL 16, pytest 8.3, Hypothesis 6.112, mutmut 2.5, Playwright 1.47, ruff 0.6.9, mypy 1.11.2, bandit 1.7.9 and Semgrep 1.85.0; verify the pinned versions in the course lock file before each delivery. City names and business terms carry Arabic subtitles in slides; all code, table names, identifiers, branch names and commit messages remain in English per Saudi enterprise convention, while user-facing content is bilingual through paired `*_ar`/`*_en` fields. Saudi PDPL obligations are treated as first-class constraints throughout — including the standing rule that no personal data and no non-approved source code is ever submitted to a third-party AI assistant.*
