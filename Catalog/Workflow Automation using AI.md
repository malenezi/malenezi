# Workflow Automation using AI
## الذكاء الاصطناعي لرفع الانتاجية

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Workflow Automation using AI |
| **Arabic Title** | الذكاء الاصطناعي لرفع الانتاجية |
| **Code** | SDA-FND-120 |
| **Track** | Data & AI Fluency — الطلاقة في البيانات والذكاء الاصطناعي |
| **Level** | Foundation |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Government employees who do not write code: administrators, correspondence and communications officers, HR and finance staff, procurement officers, analysts, executive-office coordinators, and team leads |
| **Entry Requirements** | Currently employed by a government entity; bachelor's degree; proficiency in English |
| **Prerequisites** | SDA-FND-110 (Prompt Engineering and Responsible AI Use) — strongly recommended; prompt quality determines automation quality and is assumed from Module 3 onward |
| **Assessment** | Eight built-and-running automations; two practical assessments; the Injaz automation portfolio capstone |
| **Stackability** | Workflow Automation badge; anchors the Data & AI Fluency productivity specialisation. Derived from the SDAIA Academy Data & AI Fluency programme. Next: SDA-DSC-212 (analytics path) / SDA-AIE-240 (building path) |
| **Tools & Platforms** | Microsoft Power Automate · Power Apps · SharePoint Lists · Excel · Outlook · Microsoft Forms · an LLM assistant · n8n (open-source alternative) · Power BI |

## Course Description

A practical, build-it-today course that teaches government employees to find the repetitive work inside their own job, quantify what it costs the agency in hours per year, and remove it with low-code automation and AI — without writing software. Participants learn to map a process with SIPOC and a swimlane, score automation candidates on volume, touch-time, standardisation, error cost and risk, then construct working flows in Power Automate with triggers, conditions, switches, loops, error handling and retries. From Day 2 the flows get intelligent: extracting and classifying Arabic and English correspondence including scanned letters, producing schema-constrained structured output, drafting grounded bilingual replies from an approved knowledge base, consolidating three systems into one reconciled report, and turning a meeting transcript into minutes that chase their own action items. Governance is not a closing lecture: Saudi PDPL, records retention, audit trails, accountability and a hard list of decisions that must never be automated are taught as design constraints from Hour 1.

The course is built around a single evolving artefact: **"Injaz" (إنجاز)**, the workflow-automation programme of the Shared Services Department of a Saudi government agency in Riyadh. Injaz has a backlog of six deliberately boring processes — incoming correspondence triage, leave and HR request routing, purchase-request intake, meeting minutes and action tracking, the weekly departmental report, and citizen enquiry response — that together consume **920 staff-hours every month**. Across five days participants automate them one by one; every lab ships an Injaz automation that actually runs, so the capstone on Day 5 is an *integration and measurement* exercise, not a from-scratch build. By the close, each participant owns a governed portfolio that returns **669 hours per month — 8,028 hours per year, roughly 4.6 full-time equivalents, about SAR 1.04M of redeployable capacity** — with an automation register, a handover pack, and a benefits dashboard that proves it. The spine running through all of it: **an automation in a government process never removes the accountable human decision. It removes the typing, the routing, the chasing, and the copying around that decision.**

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Map an existing manual process with SIPOC and a swimlane, and quantify its true effort in touch-minutes, hours per month, and hours per year
2. **LO2** — Score and rank automation candidates on volume, touch-time, standardisation, error cost and risk, and defend the ranking to a decision-maker
3. **LO3** — Build reliable no-code automations using triggers, conditions, switches, loops, error handling, retries and safe pre-production testing
4. **LO4** — Apply AI to documents: extract, classify and summarise Arabic and English correspondence — including scanned letters — into schema-constrained structured output with confidence thresholds and an exception queue
5. **LO5** — Produce grounded, cited, bilingual drafts from an approved knowledge base behind a mandatory human approval gate
6. **LO6** — Consolidate data from multiple systems into a single reconciled, trusted, formatted report with a written narrative summary
7. **LO7** — Govern automations against Saudi PDPL, records-management and audit-trail obligations, and identify the decisions that must never be automated
8. **LO8** — Measure benefits realisation against a baseline, operate an automation register with named owners and handover documentation, and plan an agency automation practice against a maturity model

**Catalogue objective traceability.** The SDAIA catalogue record for this programme states four objectives, tagged **CO1–CO4** and carried into every module's mapped-objectives table alongside the LO IDs:

| ID | Catalogue objective | Covered by |
|---|---|---|
| **CO1** | Enable employees to streamline their daily tasks using AI tools | LO1, LO3, LO4, LO5, LO6 — Modules 1–6 |
| **CO2** | Boost productivity, efficiency, and quality | LO2, LO3, LO6, LO8 — Modules 1, 2, 5, 8 |
| **CO3** | Raise awareness of the latest developments in the AI field | LO4, LO5 — Modules 3, 4, and the horizon section of Module 8 |
| **CO4** | Accelerate the digital transformation process | LO7, LO8 — Modules 7, 8 and the capstone |

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Choosing the work and building the first flow | M1: Finding the Work Worth Automating · M2: Automation Fundamentals | 55% | 45% | Injaz process map (SIPOC + swimlane), a 920 h/month effort baseline, a scored candidate register, and a running leave-request routing flow |
| **Day 2** | Reliability and documents | M2 (error handling) · M3: Documents and Correspondence | 45% | 55% | Hardened leave flow with retries, failure alerting and a chase loop (+90 h/month) and a correspondence triage flow classifying Arabic and English letters (+180 h/month) |
| **Day 3** | Drafting and reporting | M4: Drafting and Communication · M5: Data Consolidation and Reporting | 35% | 65% | Grounded bilingual enquiry-reply flow with an approval gate (+160 h/month) and a reconciled weekly departmental report (+46 h/month) |
| **Day 4** | Meetings, governance, and control | M6: Meetings, Minutes, and Action Tracking · M7: Governance, Risk, and Responsible Automation | 40% | 60% | Transcript-to-minutes flow with a chase loop (+88 h/month) and a fully governed purchase-request intake flow (+105 h/month) |
| **Day 5** | Measure, sustain, scale | M8: Measuring, Sustaining, and Scaling · Capstone | 25% | 75% | Benefits dashboard proving 669 h/month, an automation register, handover packs, and the integrated Injaz portfolio demo |

## Hour-by-Hour Breakdown

### Day 1 — Choosing the Work and Building the First Flow

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why automations fail in government** + course kickoff | Meet the Injaz golden thread and its six-process backlog; establish the human-in-the-loop spine and the never-automate principle; PDPL framed as a Day-1 constraint | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Process mapping and effort accounting** (M1) | SIPOC; a five-lane swimlane; touch-time vs wait-time; volume × touch-time → hours/month → hours/year; the automation candidate scorecard | Lecture + live mapping of correspondence triage | 70/30 |
| 3 | **Lab 1 — Map and score the Injaz backlog** | Produce SIPOC + swimlane for two processes, compute the 920 h/month baseline, score and rank all six candidates | Guided lab (pairs) | 20/80 |
| 4 | **Automation fundamentals without code** (M2) | Trigger types (scheduled, event, manual, form-submission); actions; idempotency in plain language; conditions and switch branching; `apply to each` and concurrency hazards | Lecture + live flow build | 65/35 |
| 5 | **Lab 2a — Build the leave-request routing flow** | Form trigger → validate → delegation-rule switch → approval → SharePoint record; run it end-to-end in test mode | Guided lab (pairs) | 15/85 |

### Day 2 — Reliability and Documents

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Error handling and safe testing** (M2) | `configure run after`; the failure-notification pattern; retry policies; scopes and try/catch/finally; testing against a mirror list before live data | Lecture + deliberate-failure demo | 60/40 |
| 2 | **Lab 2b — Harden the leave flow** | Wrap in scopes, add the failure notifier, tune retry policy, add the idle-chase loop, prove idempotency on a duplicate submission | Guided lab | 10/90 |
| 3 | **Document AI: extraction, OCR, and Arabic RTL** (M3) | Text-layer vs scanned PDFs; OCR for Arabic; RTL and diacritics pitfalls; classification prompts with a fixed label set and a mandatory `uncertain` class | Lecture + Arabic letter walkthrough | 70/30 |
| 4 | **Structured output and the exception queue** (M3) | JSON-schema-constrained extraction; the Parse JSON action; confidence thresholds; routing low-confidence cases to a human queue | Lecture + schema demo | 60/40 |
| 5 | **Lab 3 — Injaz correspondence triage** | PDF/email in → OCR → classify → schema-constrained extract → assign owner and due date → register entry; measure accuracy on the 200-letter gold set | Guided lab | 10/90 |

### Day 3 — Drafting and Reporting

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Grounded drafting and the citation obligation** (M4) | Approved knowledge base; retrieval before generation; mandatory source citation; refusal when no source supports an answer | Lecture + ungrounded-vs-grounded demo | 70/30 |
| 2 | **Bilingual output, formal Arabic register, and the approval gate** (M4) | Formal correspondence register in Arabic; Hijri/Gregorian dating; why the officer signs and the bot does not; approval-gate patterns | Lecture + register clinic | 60/40 |
| 3 | **Lab 4 — Citizen enquiry reply with a human gate** | Classify enquiry → retrieve approved answers → draft bilingual reply with citations → route to officer → send only on approval | Guided lab | 10/90 |
| 4 | **Consolidating three systems into one report** (M5) | SharePoint + Excel + mailbox as sources; keys and joins without SQL; reconciliation checks; the narrative summary and its guardrails | Lecture + reconciliation demo | 55/45 |
| 5 | **Lab 5 — The Injaz weekly departmental report** | Scheduled flow pulls three sources, reconciles, builds a bilingual formatted report with an AI narrative, publishes Sunday 08:00 | Guided lab | 10/90 |

### Day 4 — Meetings, Governance, and Control

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Transcript to minutes to action tracking** (M6) | Recording/transcript handling; decisions vs discussion; owners and due dates as structured fields; the chase loop and escalation ladder | Lecture + transcript walkthrough | 65/35 |
| 2 | **Lab 6 — Minutes and action tracking** | Transcript → schema-constrained minutes → chair approval → action items in SharePoint → automated chase and escalation | Guided lab | 10/90 |
| 3 | **PDPL, records management, and audit trails** (M7) | Personal data in automated flows; lawful basis and minimisation; retention of automated correspondence; who is accountable when an automation errs | Lecture + audit-trail demo | 70/30 |
| 4 | **What must never be automated** (M7) | Eligibility denials, disciplinary action, procurement award, anything with a statutory right of appeal; connector data residency and the agency boundary | Lecture + red-line card sort | 65/35 |
| 5 | **Lab 7 — Governed purchase-request intake** | Completeness check → budget coding → threshold routing → procurement record, wrapped in an audit trail, retention labels, and a documented never-automate boundary | Guided lab | 10/90 |

### Day 5 — Measure, Sustain, Scale

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Benefits realisation without fiction** (M8) | Before/after baselines; touch-time instrumentation; the difference between hours saved and headcount cut; what a credible benefits claim contains | Lecture + measurement demo | 60/40 |
| 2 | **Register, ownership, handover, maturity** (M8) | The automation register; named business and technical owners; handover documentation that survives a transfer; the five-level maturity model | Lecture + register walkthrough | 55/45 |
| 3 | **Lab 8 — Benefits dashboard and handover pack** | Instrument all seven automations, build the Power BI benefits dashboard, complete the register and one full handover pack | Guided lab | 10/90 |
| 4 | **Capstone assembly** | Integrate the portfolio, complete the governance checklist, run the peer-review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos; rubric scoring; paths to SDA-DSC-212 and SDA-AIE-240 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same Injaz backlog. Never invent a throwaway example process — always advance one of the six. This is what makes Day 5 achievable: by Hour 4 the participants are integrating seven working automations they already own, not building a portfolio from nothing. Write the six-process backlog on a flip chart on Day 1 and tick each one off as it is automated; the visible progress is a genuine motivator for a non-technical cohort.
- **Tenant permissions and licensing — the single most likely thing to derail delivery.** Assume it will go wrong and plan three layers of fallback. **(1) Training tenant:** book a dedicated Microsoft 365 Developer or training tenant with Power Automate Premium trial licences assigned to every seat, provisioned and *logged into by you* at least three days before delivery. Do not rely on participants' own agency tenants; most Saudi government tenants block third-party connectors, disable the AI Builder region, or require a Data Loss Prevention exception that takes weeks. **(2) Standard-connector-only lab variants:** every lab in this package ships an alternative path using only standard connectors (Outlook, SharePoint, Excel Online, Forms, Approvals, Teams, Notifications). Where a premium connector appears — AI Builder, HTTP, Azure Blob, Dataverse — the lab text names the standard substitute in the Troubleshooting table. Practise the standard path yourself; it is the one you will actually run. **(3) Offline flow-design exercise:** for a total tenant failure, each lab has a paper equivalent — participants design the flow on the printed action-card deck (trigger card, condition card, switch card, apply-to-each card, scope card, run-after card) and defend the design at the wall. Learning outcomes for M1, M2 error-handling design, M7 and M8 are fully achievable offline; only M3–M6 lose their build. Print two decks per table before Day 1 regardless of tenant confidence.
- **Pace control:** Labs 3 (correspondence triage) and 5 (weekly report) overrun most often — Lab 3 because Arabic OCR quality varies with the sample, Lab 5 because reconciliation always surfaces one real mismatch. Publish importable solution checkpoints (`Injaz_Lab3_Start_1_0_0_1.zip`, `Injaz_Lab3_Solution_1_0_0_1.zip`, and so on for every lab) on the shared drive so a stuck participant can import the start state and continue rather than fall a lab behind.
- **Pairing:** rotate pairs each day. Pair a participant who owns the *process* (a correspondence officer, an HR coordinator) with one who is comfortable with *tools* (an analyst, a systems coordinator). The domain knowledge is what makes the automation correct; the tool comfort is what makes it exist. Neither alone is sufficient, and the transfer in both directions is the point.
- **Data and tooling discipline:** all lab data is synthetic. The Injaz sample letters, leave requests, purchase requests, transcripts and enquiries carry realistic Saudi names, Riyadh/Jeddah/Dammam locations, SAR amounts and dual Hijri/Gregorian dates, but no real personal data ever enters a training tenant. State this explicitly on Day 1 Hour 1 and again before Lab 3: **participants must not upload a real letter from their own inbox, even to "test whether it works".** This is the most common integrity and PDPL breach in this course.
- **Language and identifier convention:** deliver in English or Arabic as the cohort prefers, but keep every flow name, action name, SharePoint list and column name, JSON key and variable name in English. Arabic belongs in the *content* — letter bodies, drafted replies, report headings, the formal correspondence register — not in the plumbing. Mixed-language identifiers break Power Automate expressions, ODATA filter queries and Excel table references in ways a non-developer cannot debug. This is standard Saudi enterprise production convention and is worth ninety seconds of explanation on Day 1.
- **Fenced-block convention:** JSON blocks in this package open with a `// path/to/file.json` comment line naming the artefact. That comment is a course convention for navigation and must be removed before importing a definition into Power Automate. Say this once at the first JSON block in Module 2 and participants will not trip on it again.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction plus a 10-minute buffer; schedule the long break around Dhuhr. Day 4 Hour 3 (PDPL) is deliberately placed after the break because it is the densest reading of the week and needs alert participants. Day 5 afternoon is build and demo only, with no new theory.
- **Assessment logistics:** collect flow-run histories, not screenshots. At the end of Day 5 Hour 4 take the Solution export (`.zip`), the automation register, and the benefits dashboard link so you can verify run counts and success rates before demos begin. A flow that "works on my screen" but has never completed a successful run in its history does not pass.
- **Governance framing:** open Module 1 with the human-in-the-loop principle and return to it in every single module — do not save governance for Module 7. The sentence to repeat until the cohort can finish it for you: *an automation in a government process never removes the accountable human decision; it removes the typing, routing, chasing and copying around it.* Saudi PDPL is a first-class constraint from Day 1; by Day 4 participants should already be uncomfortable with three things they built earlier, which is exactly the intended reaction.

---

# Module 1 — Finding the Work Worth Automating: Process Mapping, Effort Accounting, and the Automation Candidate Scorecard

## المحور الأول — تحديد الأعمال الجديرة بالأتمتة

## Module Overview

**Purpose.** Most failed automation programmes in government did not fail on technology. They failed because somebody automated the wrong process — usually the most visible one, or the one the loudest director complained about — and produced a fragile flow that saved four hours a month and broke every time a form changed. This module gives participants a disciplined way to *find* the work worth automating inside their own department: map it so it can be seen, count it so it can be argued for, and score it so the ranking survives contact with a decision-maker. It also establishes the constraint that governs everything else in the course: an automation removes typing, routing, chasing and copying — never the accountable human decision.

**Business relevance.** A Saudi government entity under Vision 2030 digital-transformation targets is measured on service cycle times and on the productive redeployment of staff capacity, not on how many flows it has built. A department that can say *"correspondence triage costs us 240 hours a month, here is the map, here is the count, here is the scorecard, and here is why it ranks above the leave process"* gets funded. A department that says *"we should use AI for correspondence"* does not. This module produces exactly that artefact, and every participant leaves with one for their own real department.

**Industry use cases.**
- A ministry's executive office discovers that the ritual of "logging the letter" — retyping sender, subject, reference number and date into a register that already exists as a PDF — consumes one full-time officer's week, every week.
- A regional authority's HR unit finds that 60% of leave-request cycle time is *wait* time (a request sitting unread in an inbox), not *touch* time, and correctly concludes that the automation to build is a chase-and-route flow, not a smarter form.
- A finance shared-service centre scores twelve candidate processes and deliberately drops the highest-volume one, because its error cost is a payment to the wrong vendor and its risk score disqualifies it from unattended automation.

**Expected competencies.** After this module a participant can draw a SIPOC and a five-lane swimlane for a real administrative process; distinguish touch-time from wait-time and measure both; compute annual effort in hours and SAR from volume and touch-time; score a candidate on volume, touch-time, standardisation, error cost and risk; rank a backlog defensibly; and state, for any candidate, which specific decision inside it must remain human.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Draw a SIPOC for an administrative process and identify where the effort actually sits | LO1, CO1 |
| 1.2 | Draw a five-lane swimlane and count hand-offs, wait states and rework loops | LO1, CO1 |
| 1.3 | Distinguish touch-time from wait-time and compute hours/month and hours/year from volume | LO1, CO2 |
| 1.4 | Score and rank automation candidates on volume × touch-time × standardisation × error cost × risk | LO2, CO2 |
| 1.5 | Identify, for each candidate, the accountable human decision that must not be automated | LO2, LO7, CO4 |

## Technical Content

### 1. The Injaz backlog: six processes chosen because they are boring

Injaz (إنجاز) is the workflow-automation programme of the Shared Services Department of a Saudi government agency in Riyadh. Its head deliberately refused the glamorous candidates — the AI chatbot, the predictive dashboard — and instead wrote down the six processes that staff complain about at every team meeting. They are boring, high-volume, rule-shaped, and enormous in aggregate.

| # | Injaz process | What actually happens today | Who does it |
|---|---|---|---|
| 1 | **Incoming correspondence triage** | An official letter arrives as PDF or email; an officer reads it, classifies it, summarises it, decides an owner, sets a due date, and types the whole thing into the correspondence register | Correspondence unit (3 officers) |
| 2 | **Leave and HR request routing** | A leave form arrives; a coordinator checks entitlement and dates, works out who the approver is under the delegation matrix, emails them, chases them, then records the outcome | HR coordination (2 staff) |
| 3 | **Purchase-request intake** | A request arrives with attachments; a buyer checks completeness, assigns a budget code, routes for approval by SAR threshold, and opens a procurement record | Procurement intake (2 buyers) |
| 4 | **Meeting minutes and action tracking** | A secretary listens back to a recording, writes minutes, extracts decisions and actions, emails owners, and chases them for weeks | Committee secretariat (2 staff) |
| 5 | **Weekly departmental report** | An analyst pulls figures from SharePoint, an Excel workbook and a mailbox, reconciles them by hand, formats a bilingual report, and writes the narrative | Performance unit (1 analyst + 3 contributors) |
| 6 | **Citizen enquiry response** | An enquiry arrives; an officer classifies it, finds the approved answer, writes a reply in formal Arabic, and sends it | Contact unit (4 officers) |

Note what is *not* on the list: nothing that decides whether a citizen is entitled to something, nothing that disciplines an employee, nothing that awards a contract. That exclusion is not an accident and is revisited in Module 7.

### 2. SIPOC: the five-column map you can draw in ten minutes

SIPOC — **S**uppliers, **I**nputs, **P**rocess, **O**utputs, **C**ustomers — is the cheapest useful process map in existence. It fits on one page, takes ten minutes with the people who do the work, and forces three questions that expose automation opportunities immediately: where does the input come from, what shape is it in, and who is waiting for the output?

**SIPOC for Injaz process 1 — incoming correspondence triage**

| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |
|---|---|---|---|---|
| Other government entities; the agency's own directorates; citizens via the portal; Saudi Post | Official letter (PDF, mostly Arabic, ~30% scanned); covering email; occasional physical letter scanned at reception | 1. Receive → 2. Read and classify → 3. Summarise → 4. Decide owning department → 5. Set due date from the SLA table → 6. Enter into the register → 7. Notify the owner | Register entry (reference number, class, summary, owner, due date); notification email; acknowledgement to sender | Owning department head; the sender; the DG's office weekly overdue report |

Three things jump out of that table before any measurement happens. The input is *already digital* in 100% of cases, which means no scanning project is needed. Step 6 — "enter into the register" — creates no new information; it is pure retyping of what steps 2 to 5 already determined. And step 4, "decide owning department", is the only step that involves judgement about the agency's structure, which makes it the candidate for AI *assistance* with human confirmation rather than silent automation.

**How to run a SIPOC session (teach this, participants will run one at their own desk next month).** Get the three people who actually do the work in a room with a whiteboard. Start in the middle — the Process column — and cap it at seven steps; if it needs more, you have two processes. Then fill Outputs, then Customers, then Inputs, then Suppliers. Do not let anyone describe the process as it is written in the policy document; write what happens on a Tuesday, including the workaround everyone uses.

### 3. Swimlanes: where the hand-offs and the waiting hide

SIPOC tells you what the process is. A **swimlane** tells you why it takes four days when it contains twenty minutes of work. Draw one horizontal lane per actor, place each step in the lane of whoever performs it, and draw an arrow every time work crosses a lane. Every arrow is a hand-off, and every hand-off is where a case sits in somebody's inbox.

```text
# injaz/process-maps/correspondence-triage-swimlane.txt
INCOMING CORRESPONDENCE TRIAGE — CURRENT STATE (as-is)
Legend:  [n min] = touch-time     ((n h)) = wait-time      >>> = hand-off (lane crossing)

SENDER        | (letter sent) ......................................>>>
              |                                                      |
MAILBOX/      |                                              (letter lands in
RECEPTION     |                                               shared mailbox)
              |                                                 ((14 h))  <- overnight + morning queue
              |                                                      v
CORRESPOND-   |   [2 min] open & read  ->  [4 min] classify  ->  [3 min] summarise
ENCE OFFICER  |        -> [1 min] pick owner -> [1 min] due date -> [3 min] type into register
              |        -> [1 min] send notification .............>>> total touch 15 min? see note
              |                                                      |
DEPARTMENT    |                                                 ((26 h))  <- sits unread
HEAD          |                                              [3 min] acknowledge / reassign
              |                                                      |
DG OFFICE     |                                                 ((32 h))  <- weekly overdue sweep
              |                                              [2 min] chase if overdue

TOTALS:  touch-time 12 min/letter (officer) + 5 min (others)   |   wait-time 72 h  |  cycle 3.2 days
HAND-OFFS: 4      REWORK LOOP: 1 (reassignment, occurs on ~11% of letters)
```

Note the discrepancy the diagram deliberately contains: the individual officer steps sum to 15 minutes, but the measured average is 12. That gap is a teaching moment — self-reported step times are almost always inflated because people describe the hard case, not the median case. Always reconcile the step sum against an observed total, and use the observed total.

The swimlane produces four numbers that matter for the rest of this course: **touch-time** (12 min), **wait-time** (72 h), **hand-offs** (4) and the **rework loop rate** (11%). Automation attacks all four differently: it compresses touch-time by removing typing, collapses wait-time by removing inbox queues, removes hand-offs by writing directly to the destination system, and reduces rework by making the classification consistent.

### 4. Effort accounting: turning minutes into a business case

The arithmetic is deliberately primary-school simple, because it has to survive being repeated by a director in a budget meeting.

```text
# injaz/effort-accounting/formula.txt
hours per month     = (monthly volume  ×  touch-time in minutes) / 60
hours per year      =  hours per month × 12
capacity in FTE     =  hours per year / 1,760        (1,760 = productive hours per staff-year:
                                                      260 working days − 30 leave/training days
                                                      = 230 days × 8 h × 0.955 utilisation)
annual value in SAR =  hours per year × 130          (blended loaded cost per staff-hour,
                                                      administrative grades, Riyadh, 2026)

WORKED EXAMPLE — incoming correspondence triage
  monthly volume    = 1,200 letters
  touch-time        = 12 minutes
  hours per month   = (1,200 × 12) / 60          = 240 hours
  hours per year    = 240 × 12                   = 2,880 hours
  value             = 2,880 × 130                = SAR 374,400 per year
```

Three rules keep this honest, and each one exists because somebody once broke it:

1. **Measure touch-time, do not ask for it.** Have three people log ten cases each with a stopwatch, take the median. Self-reported estimates run 20–40% high.
2. **Never claim wait-time as savings.** Removing 72 hours of queueing is a *cycle-time* benefit and it is real and valuable — but it is not staff hours you can redeploy. Report the two separately or your finance director will correctly reject the whole business case.
3. **Report residual effort, not just savings.** An automation that takes triage from 12 minutes to 3 minutes saves 9 minutes, not 12. The residual 3 minutes is the human review that must survive. A business case claiming 100% of the effort is a business case claiming there is no human in the loop, which for a government process is a governance failure disguised as an arithmetic error.

**The Injaz baseline (this table is the spine of the whole course — it reappears in the Module 8 benefits dashboard and the capstone rubric):**

| # | Injaz process | Volume / month | Touch-time before | Hours/month before | Touch-time after | Hours/month after | Hours/month saved | Hours/year saved |
|---|---|---|---|---|---|---|---|---|
| 1 | Correspondence triage | 1,200 letters | 12 min | 240 | 3 min | 60 | **180** | 2,160 |
| 2 | Leave / HR routing | 900 requests | 8 min | 120 | 2 min | 30 | **90** | 1,080 |
| 3 | Purchase-request intake | 350 requests | 24 min | 140 | 6 min | 35 | **105** | 1,260 |
| 4 | Minutes and actions | 160 meetings | 45 min | 120 | 12 min | 32 | **88** | 1,056 |
| 5 | Weekly departmental report | 4 reports | 900 min | 60 | 210 min | 14 | **46** | 552 |
| 6 | Citizen enquiry response | 1,600 enquiries | 9 min | 240 | 3 min | 80 | **160** | 1,920 |
| | **Total** | | | **920** | | **251** | **669** | **8,028** |

8,028 hours per year is **4.6 FTE** of capacity and **SAR 1.04M** at the blended rate. Say the sentence that must accompany that number every time it is spoken: *this is capacity redeployed to work that requires a person, not headcount removed.* In a Saudi government context this framing is not diplomacy; it is the difference between a programme that staff cooperate with and one they quietly sabotage.

### 5. The automation candidate scorecard

Volume alone ranks the wrong things. The scorecard multiplies benefit by feasibility and then subtracts risk, on five dimensions, each scored 1–5.

| Dimension | 1 | 3 | 5 | Why it matters |
|---|---|---|---|---|
| **Volume** | < 50 cases/month | 200–500 | > 1,000 | Benefit scales linearly with volume; below ~50/month almost nothing pays back |
| **Touch-time** | < 3 min | 8–15 min | > 30 min | Long manual tasks have more removable typing and routing |
| **Standardisation** | Every case different; no written rule | Rules exist but with frequent exceptions | Written rule, stable form, same steps every time | Unstandardised processes produce unmaintainable flows |
| **Error cost (inverted)** | An error is catastrophic and irreversible (wrong payment, wrong entitlement decision) | An error is embarrassing and correctable within a day | An error is trivial (a mistyped subject line) | High error cost does not forbid automation — it forbids *unattended* automation |
| **Risk (inverted)** | Statutory right of appeal, personal data, or a legal decision | Personal data with a clear lawful basis and a human gate | No personal data, internal only | PDPL and administrative-law exposure |

**Score = Volume + Touch-time + Standardisation + Error-cost + Risk**, out of 25. Bands: **20–25 automate now**; **14–19 automate with a human gate**; **9–13 redesign the process first, then reconsider**; **≤ 8 do not automate**.

**The Injaz scored backlog (produced in Lab 1):**

| Process | Volume | Touch | Standard. | Error cost | Risk | **Total** | Band | Human decision that must survive |
|---|---|---|---|---|---|---|---|---|
| Citizen enquiry response | 5 | 3 | 4 | 3 | 2 | **17** | Gate | The officer approves and signs the reply |
| Correspondence triage | 5 | 3 | 4 | 4 | 3 | **19** | Gate | The department head confirms ownership; reassignment stays human |
| Leave / HR routing | 4 | 2 | 5 | 4 | 3 | **18** | Gate | The delegated approver grants or refuses leave |
| Minutes and actions | 2 | 5 | 3 | 4 | 3 | **17** | Gate | The chair approves the minutes as a true record |
| Weekly departmental report | 1 | 5 | 4 | 4 | 4 | **18** | Gate | The head of performance signs the narrative |
| Purchase-request intake | 3 | 4 | 4 | 2 | 2 | **15** | Gate | Budget-code confirmation and every approval; **award is never automated** |
| *(rejected)* Disciplinary case processing | 2 | 5 | 2 | 1 | 1 | **11** | Redesign / never | The entire decision — excluded on principle, not on score |
| *(rejected)* Grant eligibility determination | 4 | 3 | 3 | 1 | 1 | **12** | Never | Statutory right of appeal; excluded regardless of score |

Two lessons live in the bottom two rows. First, the scorecard *ranks*; it does not *authorise*. A process can score 20 and still be forbidden. Second, the rejected candidates were scored anyway, and the score is recorded — because in eight months somebody will propose them again and the register must show they were considered and refused, with a reason.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Map before you build.* A flow built without a swimlane automates the process somebody imagines, not the one that happens.
- *Count in hours per year, argue in hours per year.* Minutes per case persuade nobody; 2,880 hours persuades everybody.
- *Separate touch-time savings from cycle-time savings.* Both are real; conflating them destroys the credibility of both.
- *Name the surviving human decision before you design anything.* If you cannot name it, you are about to automate a decision, and you must stop.
- *Automate the boring middle.* The intake and the final decision usually stay human; the classifying, routing, chasing, formatting and recording in between is where the hours are.

**Common mistakes (each is deliberately planted in the Lab 1 starter pack)**
1. The starter effort workbook uses *self-reported* touch-times (18 min for triage instead of the observed 12), inflating the baseline by 50% — participants must reconcile against the observation log in the same pack.
2. The starter scorecard omits the risk column entirely, so the disciplinary-case process ranks third. Somebody in the room must notice.
3. The starter swimlane counts wait-time as staff effort, producing a claim of 6,240 hours/year for triage instead of 2,880.
4. The starter map stops at "enter into the register" and never shows the 11% reassignment rework loop — so the flow designed from it has no exception path.
5. The starter backlog ranks purely on volume, putting citizen enquiries first and the weekly report last, ignoring that the report has the highest touch-time per case in the portfolio.

**Production considerations**
- Re-baseline every six months. Volumes drift; a 2026 baseline defended in 2028 is a liability.
- Keep the swimlane with the flow. When the automation breaks in eighteen months, the person fixing it will not be its author, and the map is the only artefact that explains intent.
- Get the baseline signed by the process owner *before* you build. A baseline agreed afterwards is always disputed; a baseline agreed beforehand is a contract.
- Record rejected candidates and the reason. This is the register's most under-appreciated function.

### 7. Real-world example walkthrough

Narrate this in five minutes, no slides. A municipality's licensing department was under ministerial pressure over a 21-day licence cycle time. The department proposed an AI system to "assess applications automatically" — the glamorous candidate, and the one with a statutory right of appeal attached to every outcome. A consultant insisted on a swimlane first. It took two hours and showed something nobody expected: the technical assessment itself averaged 40 minutes of touch-time, but applications spent **17 of the 21 days** in exactly two queues — waiting for a completeness check that took four minutes, and waiting for a signature that took ninety seconds. The department automated the completeness check and the signature routing, left the assessment entirely human, and the cycle time fell from 21 days to 6. Nothing about the decision changed; nothing with a right of appeal was touched; the ministerial target was met. The lesson to land: the map told them the assessment was not the problem, and the map is why they did not spend two years building the wrong thing.

## Code Examples

### The Injaz effort-accounting workbook definition

```text
# injaz/effort-accounting/InjazBaseline.xlsx — sheet "Baseline", column formulas
# One row per process. Columns A-D are entered; E-J are calculated.
# This workbook is the evidence base for the whole programme — version it, and
# have the process owner sign the printed version before any flow is built.

A  ProcessName          (text)      e.g. "Correspondence triage"
B  MonthlyVolume        (number)    counted from the source system, NOT estimated
C  TouchMinutesBefore   (number)    MEDIAN of 30 stopwatch observations (10 per officer × 3)
D  TouchMinutesAfter    (number)    target residual human time — must be > 0
E  HoursMonthBefore     =(B2*C2)/60
F  HoursMonthAfter      =(B2*D2)/60
G  HoursMonthSaved      =E2-F2
H  HoursYearSaved       =G2*12
I  FTEEquivalent        =H2/1760
J  AnnualValueSAR       =H2*130

# Guard formulas — these turn red and must be resolved before sign-off:
K  ObservationCheck     =IF(ABS(C2-StepSum!B2)/C2>0.25,"RECONCILE step sum vs observed","ok")
L  ResidualCheck        =IF(D2<=0,"INVALID: no human time left — you are automating a decision","ok")
M  WaitTimeCheck        =IF(C2>120,"Is this touch-time or wait-time? Wait-time is NOT a saving","ok")

# Totals row (row 9):
E9 =SUM(E2:E7)   -> 920      F9 =SUM(F2:F7)   -> 251
G9 =SUM(G2:G7)   -> 669      H9 =SUM(H2:H7)   -> 8,028
I9 =H9/1760      -> 4.56     J9 =H9*130       -> 1,043,640
```

### The candidate scorecard as a SharePoint list

```text
# injaz/registers/AutomationCandidates — SharePoint list column definition
# Created once per agency. This list becomes the Automation Register in Module 8,
# so create it with the governance columns from the start rather than retro-fitting.

Title                    Single line of text   (the process name, English)
ProcessNameAr            Single line of text   (Arabic name, for reporting)
OwningDepartment         Choice                (Correspondence, HR, Procurement, Secretariat,
                                                Performance, Contact Centre)
ProcessOwner             Person or Group       (the accountable manager — NOT the flow builder)
MonthlyVolume            Number, 0 decimals
TouchMinutesBefore       Number, 1 decimal
HoursMonthBefore         Calculated            =([MonthlyVolume]*[TouchMinutesBefore])/60
ScoreVolume              Number 1-5
ScoreTouchTime           Number 1-5
ScoreStandardisation     Number 1-5
ScoreErrorCost           Number 1-5            (inverted: 5 = trivial error)
ScoreRisk                Number 1-5            (inverted: 5 = no personal data, internal only)
ScoreTotal               Calculated            =[ScoreVolume]+[ScoreTouchTime]+
                                                [ScoreStandardisation]+[ScoreErrorCost]+[ScoreRisk]
Band                     Calculated            =IF([ScoreTotal]>=20,"Automate now",
                                                IF([ScoreTotal]>=14,"Automate with human gate",
                                                IF([ScoreTotal]>=9,"Redesign first","Do not automate")))
SurvivingHumanDecision   Multiple lines of text  MANDATORY — the list rejects a blank on submit
NeverAutomateFlag        Yes/No                (overrides Band; set by the governance forum only)
NeverAutomateReason      Multiple lines of text
DecisionDate             Date only
DecisionMinuteRef        Single line of text   (the governance forum minute that recorded it)

# View "Ranked backlog": filter NeverAutomateFlag = No, sort ScoreTotal descending.
# View "Refused": filter NeverAutomateFlag = Yes — kept forever, so a refused
#                 candidate cannot be quietly re-proposed six months later.
```

## Hands-on Lab 1 — Map and Score the Injaz Backlog

| | |
|---|---|
| **Objective** | Produce a SIPOC and a swimlane for two Injaz processes, compute the 920 h/month effort baseline from observation data, score and rank all six candidates plus two rejected ones, and name the surviving human decision for each |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab1_Start_1_0_0_1.zip` (creates the `AutomationCandidates` SharePoint list); open `InjazBaseline_start.xlsx` and `observation_log.xlsx` from the shared drive; one printed swimlane template and one action-card deck per pair. No premium licence required. |

**Instructions & tasks**

1. *(6 min)* Read `observation_log.xlsx` — 30 stopwatch observations for correspondence triage and 30 for leave routing. Compute the median for each. Note that the starter workbook's `TouchMinutesBefore` for triage says **18**; the observed median is **12**. Correct it and record why in the Notes column.
2. *(10 min)* Draw the SIPOC for **leave and HR request routing** on the printed template. Cap the Process column at seven steps. Identify the one step that creates no new information (the answer is the re-keying of form fields into the HR record).
3. *(12 min)* Draw the swimlane for the same process. Mark every step as touch-time `[n min]` or wait-time `((n h))`, count the hand-offs, and find the rework loop. Confirm your touch-time total reconciles with the observed median within 25%.
4. *(10 min)* Complete `InjazBaseline.xlsx` for all six processes. Resolve every red guard formula. Your total `HoursMonthBefore` must equal **920** and `HoursYearSaved` must equal **8,028**; if it does not, you have either used a self-reported time or counted wait-time.
5. *(8 min)* Score all six candidates plus the two rejected ones in the `AutomationCandidates` list. Add the risk column that the starter scorecard omits. For every row, complete `SurvivingHumanDecision` — the list will reject a blank.
6. *(4 min)* Export the ranked view and record the change in the register's version note: `feat(register): Injaz baseline 920 h/month, 6 candidates scored, 2 refused`.

**Expected output**
```text
InjazBaseline.xlsx — Baseline sheet, totals row
  HoursMonthBefore   920.0
  HoursMonthAfter    251.0
  HoursMonthSaved    669.0
  HoursYearSaved   8,028.0
  FTEEquivalent        4.56
  AnnualValueSAR 1,043,640

Guard checks:
  K2 correspondence triage : ok   (was "RECONCILE step sum vs observed" at 18 min)
  L5 weekly report         : ok   (residual 210 min > 0 — the analyst still signs the narrative)
  M5 weekly report         : "Is this touch-time or wait-time?"  -> reviewed, 900 min is
                              genuine touch-time across 4 contributors, comment added

AutomationCandidates — view "Ranked backlog"
  Correspondence triage      19  Automate with human gate
  Leave / HR routing         18  Automate with human gate
  Weekly departmental report 18  Automate with human gate
  Citizen enquiry response   17  Automate with human gate
  Minutes and actions        17  Automate with human gate
  Purchase-request intake    15  Automate with human gate
AutomationCandidates — view "Refused"
  Grant eligibility determination  12  NeverAutomateFlag=Yes  (statutory right of appeal)
  Disciplinary case processing     11  NeverAutomateFlag=Yes  (legal decision affecting an employee)
```

**Acceptance criteria**
- Baseline totals are exactly 920 h/month before, 251 after, 669 saved, 8,028 h/year; no guard formula is left red without a written comment.
- Both a SIPOC and a swimlane exist for leave routing, with touch/wait time separated, hand-offs counted and the rework loop marked.
- All eight candidates are scored on five dimensions including risk; both refused candidates carry a `NeverAutomateReason`.
- Every row has a non-empty `SurvivingHumanDecision` naming a specific person or role, not "the manager".

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Baseline totals 1,140 h/month, not 920 | Used the starter's self-reported 18 min for triage | Use the observed median (12 min) from `observation_log.xlsx` |
| Triage saving looks like 6,240 h/year | Wait-time (72 h) counted as staff effort | Wait-time is a cycle-time benefit; report it in a separate column |
| `SurvivingHumanDecision` rejected on save | Field left blank or filled with "N/A" | Name the actual decision and role; if none exists, the candidate is unfit as designed |
| Disciplinary process ranks third | Risk column missing from the starter scorecard | Add `ScoreRisk`; then set `NeverAutomateFlag` regardless of the score |

**Instructor notes.** The planted 18-minute triage figure is the highest-value moment of Day 1 — walk the room and see who checks it against the observation log rather than trusting the workbook. Most pairs will not, and the resulting 50% inflation is the perfect illustration of why self-reported effort destroys business cases. When somebody finds it, stop the room. Second thing to watch: participants writing "the manager decides" in `SurvivingHumanDecision`. Push back until they name the role and the specific decision ("the delegated approver in the HR delegation matrix grants or refuses the leave"). Fast finishers: score two processes from their *own* real department and bring the scores to Day 5 — several participants each cohort discover a 1,000-hour candidate they had never counted.

## Mini Exercises

**Quiz (5 questions)**
1. What are the five columns of SIPOC? → Suppliers, Inputs, Process, Outputs, Customers.
2. A process takes 12 minutes of work but 3 days to complete. Which number goes in the hours-saved business case? → the 12 minutes (touch-time); the 3 days is a cycle-time benefit, reported separately.
3. Why is a self-reported touch-time usually wrong? → people describe the hard case, not the median; estimates run 20–40% high.
4. A candidate scores 22/25 but decides a citizen's entitlement. What happens? → it is refused; the scorecard ranks, it does not authorise. `NeverAutomateFlag` overrides the band.
5. What must `TouchMinutesAfter` never be? → zero — a residual of zero means no human is left in the loop.

**Debugging exercise.** Hand out a completed baseline claiming 14,400 hours/year saved from correspondence triage alone. Participants must find the two defects: wait-time counted as touch-time, and `TouchMinutesAfter` set to 0. Discussion this opens: what does a stakeholder conclude about *every other number you produce* once they find one inflated claim?

**Design exercise.** Take Injaz process 3 (purchase-request intake). Draw the swimlane and mark, in red, the single step that must remain human under any design. Then mark in amber the two steps where AI may *recommend* but a human confirms. Justify the boundary you drew.

**Discussion questions.**
- Your director wants the highest-volume process automated first because "that is where the numbers are". Citizen enquiries have the highest volume but the greatest reputational exposure. How do you argue the ranking without appearing obstructive?
- If an automation frees 4.6 FTE of capacity, and the agency has a hiring freeze rather than a reduction target, has the programme actually delivered value? What evidence would convince a sceptical finance director either way?

## Case Study — The Wrong Process at "Muwazanah" (موازنة)

**Scenario.** "Muwazanah" (موازنة), the finance shared-service centre of a regional development authority in Dammam, launched an automation programme with executive sponsorship and a two-year budget. Eighteen months later it had built fourteen flows, of which four still ran. The programme was quietly closed.

**Business context.** The centre processes supplier invoices, staff reimbursements, budget transfers and monthly closing packs for eleven client entities. The executive sponsor's brief was "automate finance", and the programme selected candidates by asking each department head which task annoyed them most.

**Technical challenge.** The four surviving flows are all high-volume, rule-shaped and low-risk. The ten dead ones share a pattern nobody diagnosed at the time: each automated a process with fewer than 40 cases a month, or one whose rules changed every quarter, or one whose "steps" were actually a professional judgement wearing a checklist. One flow — automated budget-transfer approval below SAR 50,000 — was switched off by the internal auditor after four months because no audit trail recorded who had authorised what.

**Constraints.** No baseline was ever taken, so the programme cannot prove what the four surviving flows saved. The centre must present to the authority's board in six weeks. The board has already heard the phrase "digital transformation" too many times and will want hours and SAR. The four surviving flows must not be disrupted while the case is rebuilt.

**Solution approach (facilitate, don't lecture).** Guide the room toward: (1) retrospectively baseline the four survivors by observing current touch-time and reconstructing the before-state from the process owners and old work instructions — imperfect but defensible if the method is stated; (2) run SIPOC and swimlane sessions on the top eight remaining manual processes, measured this time; (3) apply the five-dimension scorecard, expecting most of the ten dead flows to score below 14 and the budget-transfer flow to be refused outright on risk; (4) present the board with a *smaller* backlog and a real baseline rather than a larger backlog and a story. Let the room discover that the programme's failure was a selection failure, not a technology failure — the tooling was never the constraint.

**Discussion questions.**
1. Ten of fourteen flows died. What single artefact, produced before any build, would have prevented most of those builds?
2. The budget-transfer flow was switched off by the auditor, not by a user. What does that tell you about which stakeholder should have been in the design session?
3. How do you construct a retrospective baseline that a sceptical board will accept? What must you disclose about its method?
4. Presenting a *smaller* backlog to a board that funded an ambitious programme is politically hard. How would you frame it so it reads as maturity rather than retreat?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Processes mapped (SIPOC + swimlane) | Coverage | 2 of 2 required, both complete | template review |
| Touch-time reconciliation | Accuracy | observed median within 25% of step-sum, all rows | guard formula K |
| Baseline correctness | Accuracy | 920 h/month before, 669 h/month saved, 8,028 h/year | totals row check |
| Candidates scored on all 5 dimensions | Completeness | 8 of 8, including 2 refused | list view export |
| Surviving human decision named | Governance | 8 of 8, role-specific not generic | instructor review |

**Example benchmark table (filled during lab):**

| Process | Volume/month | Touch before | Touch after | h/month saved | h/year saved | Score | Band |
|---|---|---|---|---|---|---|---|
| Correspondence triage | 1,200 | 12 min | 3 min | 180 | 2,160 | 19 | Human gate |
| Leave / HR routing | 900 | 8 min | 2 min | 90 | 1,080 | 18 | Human gate |
| Purchase-request intake | 350 | 24 min | 6 min | 105 | 1,260 | 15 | Human gate |
| Minutes and actions | 160 | 45 min | 12 min | 88 | 1,056 | 17 | Human gate |
| Weekly departmental report | 4 | 900 min | 210 min | 46 | 552 | 18 | Human gate |
| Citizen enquiry response | 1,600 | 9 min | 3 min | 160 | 1,920 | 17 | Human gate |
| **Portfolio total** | | | | **669** | **8,028** | | 4.56 FTE / SAR 1.04M |

## Required Visuals and Training Assets

### Diagrams
1. **The Injaz six-process backlog wheel** — *Purpose:* the anchor image for the entire course, reused as a progress tracker in every module. *Elements:* six segments, one per process, each with its hours/month figure; segments fill in as they are automated across Days 1–4. *Style:* flat vector, agency-neutral palette, English labels with Arabic subtitles (المراسلات، الإجازات، المشتريات، المحاضر، التقرير الأسبوعي، استفسارات المستفيدين). *Designer description:* "A circle of six wedges around a central 'Injaz إنجاز' hub; each wedge shows an icon, a process name and an hours figure; a fill state indicates automated vs manual."
2. **Touch-time versus wait-time** — *Purpose:* prevent the single most common business-case error. *Elements:* a horizontal timeline of one correspondence case across 3.2 days, with 12 minutes of solid colour (touch) and 72 hours of hatched grey (wait); two labelled brackets showing which one is a staff-hours saving and which is a cycle-time saving. *Style:* single timeline, two textures, one red annotation reading "this is NOT a staff-hours saving".
3. **Swimlane anatomy** — *Purpose:* teach the notation before the lab. *Elements:* the five Injaz correspondence lanes with hand-off arrows numbered 1–4, one rework loop drawn as a curved return arrow labelled "11%", and wait states drawn as clock badges on the lane boundaries. *Style:* classic swimlane, monochrome with hand-offs in red. *Designer description:* "Five stacked horizontal lanes; steps as rounded rectangles; every lane crossing gets a red arrow and a number; the rework loop curves backward from the department-head lane to the officer lane."
4. **Scorecard radar** — *Purpose:* make the trade-off between benefit and risk visible. *Elements:* a five-axis radar (volume, touch-time, standardisation, error cost, risk) overlaying correspondence triage in blue and grant-eligibility determination in red, with the red shape collapsed on the risk and error-cost axes. *Style:* two-series radar with a hard "refused" stamp on the red shape.

### Images (screenshots)
1. **The `AutomationCandidates` SharePoint list, ranked view** — *why:* participants build exactly this in Lab 1 and need to see the target state; *content:* eight rows sorted by ScoreTotal, with the two refused rows greyed and flagged.
2. **The baseline workbook with a guard formula fired red** — *why:* the guard formulas are the lab's teaching mechanism; *content:* cell K2 showing "RECONCILE step sum vs observed" against the planted 18-minute value.
3. **A real completed swimlane photographed from a whiteboard** — *why:* to legitimise messy hand-drawn output; *content:* sticky notes, crossings-out, a visible argument about who owns step 4. Caption: "This is what a good first map looks like."

### Simulations
1. **The inflated baseline** — *Setup:* two teams receive the same process description; team A is given self-reported times, team B the stopwatch log. *Expected behaviour:* team A's business case is 40–50% larger. *Learning objective:* measurement method determines the number, and the number determines whether anyone believes you.
2. **The volume trap** — *Setup:* a backlog of eight candidates ranked by volume only, then re-ranked with the full scorecard. *Expected behaviour:* the top two swap places and one candidate is refused outright. *Learning objective:* volume is one dimension of five, and risk is a veto, not a weight.

### Interactive Activities
- **Ten-minute SIPOC race (15 min):** each pair maps one process from *their own* department on a printed template; three pairs present; the room votes on which map most obviously reveals removable work.
- **Red-line card sort (12 min):** twenty process cards (issue a parking permit, deny a grant, acknowledge a letter, dismiss an employee, chase an overdue action, award a tender…) sorted into "automate", "automate with a gate", and "never". The disagreements are the lesson; keep the cards for Module 7 Hour 4 where the same deck is used again.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `observation_log.xlsx` | Synthetic stopwatch log, 30 observations per process, realistic skew | XLSX | 180 rows | Establish the observed touch-time medians; the antidote to the planted self-reported values |
| `InjazBaseline_start.xlsx` | Course starter with the five planted defects | XLSX | 8 rows + guard formulas | Lab 1 build target |
| `injaz_backlog_descriptions.docx` | Six process narratives plus two refused candidates, written in agency voice | DOCX | 6 pages | Source material for SIPOC and scoring |
| `swimlane_template.pdf` | Five-lane printable template, A3 | 20 copies | Lab 1 mapping |

### Demo Requirements
- **Instructor demo (8 minutes):** take a live suggestion from the room — a process one participant actually does — and map it on the whiteboard in front of everyone: SIPOC in three minutes, swimlane in four, the hours-per-year figure in one. The point of doing it live and fast is to destroy the belief that process mapping is a consultant's six-week engagement. Finish by asking the owner of that process to name the surviving human decision; if they hesitate, that hesitation is the module's thesis.

---

# Module 2 — Automation Fundamentals: Triggers, Actions, Conditions, Loops, and Error Handling Without Code

## المحور الثاني — أساسيات الأتمتة بدون برمجة

## Module Overview

**Purpose.** This is the module where the cohort stops talking about automation and builds one. It teaches the six primitives that every no-code automation in the world is assembled from — trigger, action, condition, switch, loop, and error handler — using vocabulary a correspondence officer can hold in their head. It then teaches the three things that separate a flow that survives eighteen months in production from a flow that is switched off in week three: idempotency, error handling, and testing before you touch live data. By the end, participants own a running leave-request routing flow that saves Injaz **90 hours a month**.

**Business relevance.** In every Saudi government entity there is a folder of abandoned automations. They were not abandoned because the logic was wrong; they were abandoned because they ran twice on the same request and created two HR records, or because they failed silently for three weeks and nobody noticed until an employee's leave was never recorded. Reliability is not an advanced topic to be covered later — for a government process with an audit trail obligation, it is the *entry price*. This module makes reliability the second thing participants learn, not the last.

**Industry use cases.**
- A ministry's HR unit routes 900 leave requests a month through a delegation matrix that changes whenever a director travels; the routing rule lives in a maintained list, not in the flow, so the flow never needs editing.
- An executive office runs a nightly scheduled flow that sweeps overdue correspondence and produces a single digest at 07:30 rather than 40 individual emails at random hours.
- A finance team's approval flow fails when the finance system is unavailable at month-end; a retry policy and a failure notification mean the request is retried four times over eight minutes and, if it still fails, a named human is told within a minute rather than the request vanishing.

**Expected competencies.** After this module a participant can choose the right trigger type for a process; write a condition and a switch that route correctly; use `apply to each` without corrupting shared variables; make a flow idempotent so a duplicate trigger does no harm; wrap steps in scopes with `configure run after` to build try/catch/finally; configure a retry policy appropriately for the failure it is protecting against; and test a flow safely against a mirror list before it touches a live record.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Select the correct trigger type (scheduled, event, manual, form-submission) for a given process | LO3, CO1 |
| 2.2 | Build branching logic with conditions and a switch driven by a maintained rules list | LO3, CO1 |
| 2.3 | Use `apply to each` correctly, including concurrency settings and the shared-variable hazard | LO3, CO2 |
| 2.4 | Make a flow idempotent so that a duplicate or replayed trigger causes no duplicate record | LO3, CO2 |
| 2.5 | Implement error handling with scopes, `configure run after`, retry policies and a failure notifier | LO3, LO7, CO2 |
| 2.6 | Test an automation safely against mirror data before it is allowed near live records | LO3, LO7, CO4 |

## Technical Content

### 1. The six primitives

Everything in Power Automate, n8n, Zapier, Make or Google Apps Script decomposes into six things. Teach them in this order and do not add a seventh until Module 3.

| Primitive | What it does | Injaz example | The mistake it invites |
|---|---|---|---|
| **Trigger** | Starts the flow, exactly once per event | A leave form is submitted | Choosing a schedule when an event exists — introduces up to a full interval of delay |
| **Action** | Does one thing: read, write, send, call | Create an item in the `LeaveRequests` list | Doing three things in one action via a giant expression nobody can debug |
| **Condition** | Two-way branch on a true/false test | `Is the requested leave ≤ remaining balance?` | Nesting conditions five deep instead of using a switch |
| **Switch** | Multi-way branch on a value | Route by `RequestType`: Annual / Sick / Unpaid / Emergency | Forgetting the default case, so unknown values silently do nothing |
| **Loop** (`apply to each`) | Repeats actions over a collection | Chase each idle request in yesterday's list | Writing to a shared variable inside a concurrent loop |
| **Error handler** | Catches a failure and does something about it | Notify the flow owner and write a failure record | Not having one — the single most common defect in government flows |

### 2. Trigger types and when each is correct

| Trigger type | Fires when | Latency | Best for | Watch out for |
|---|---|---|---|---|
| **Event / automated** | Something changes: a file arrives, an item is created or modified, an email lands | Seconds | Correspondence arriving, forms submitted, list items created | "Item modified" triggers fire on *every* edit — including edits made by the flow itself, which creates infinite loops |
| **Scheduled / recurrence** | On a clock: every 15 min, daily 07:00, weekly Sunday | Up to one full interval | Chasing overdue items, nightly digests, the weekly report | Timezone and daylight handling; Power Automate recurrence is UTC unless you set the timezone explicitly |
| **Manual / instant** | A human presses a button in Teams, Power Apps or the mobile app | Immediate | Anything requiring a deliberate human act — "send this reply", "escalate this case" | Being used where an event trigger belongs, reintroducing the human typing you were removing |
| **Form submission** | A Microsoft Form or Power App submits | Seconds | Structured intake: leave requests, purchase requests, enquiry forms | Form questions renaming themselves breaks the flow silently; pin the form and version it |

**The infinite-loop trap, stated plainly.** A flow triggered on "when an item is modified" that then modifies the same item will trigger itself, forever, until the platform's loop protection stops it — typically after it has already written a few hundred junk versions. Three defences, in order of preference: trigger on *creation* rather than modification; add a trigger condition that excludes edits made by the service account; or write the flow's own updates to a *different* list. Show this failing live once; the cohort never forgets it.

```text
# injaz/flows/_shared/trigger-conditions.txt
# Trigger condition on a SharePoint "When an item is created or modified" trigger.
# Paste into Settings > Trigger Conditions. Excludes the flow's own service-account edits
# and anything already marked as processed. Both conditions must be true for the flow to run.

@not(equals(triggerOutputs()?['body/Editor/Email'], 'svc-injaz-flows@agency.gov.sa'))

@equals(triggerOutputs()?['body/ProcessingStatus/Value'], 'New')
```

### 3. Idempotency, in plain language

**Idempotent** means: running it twice does the same thing as running it once. That is the whole idea, and it matters because triggers fire twice more often than anyone expects — a network retry, a user double-clicking submit, a platform redelivery after an outage, or an administrator manually resubmitting a failed run.

The non-idempotent version of the Injaz leave flow does this: *trigger → create a new item in `LeaveRequests`*. Fire it twice and the employee has two leave records, two approvers are emailed, and one of them approves a request the other rejected.

The idempotent version does this: *trigger → look for an existing item with this `RequestId` → if found, stop → if not, create it*. Fire it a hundred times and there is one record.

```text
# injaz/flows/leave-request-routing/idempotency-guard.txt
# Step 1 of every Injaz flow that creates a record.
# 1) Build a deterministic key from the trigger payload — never from utcNow().
# 2) Look for it. 3) Terminate quietly if it already exists.

# --- Compose: RequestId (deterministic, survives replays) ---
@{concat(
    'LR-',
    formatDateTime(triggerOutputs()?['body/submitTime'], 'yyyyMMdd'),
    '-',
    toUpper(substring(triggerOutputs()?['body/responder'], 0, indexOf(triggerOutputs()?['body/responder'], '@'))),
    '-',
    substring(triggerOutputs()?['body/responseId'], 0, 8)
)}
# -> LR-20260517-A.ALMUTAIRI-3f9c1b7d

# --- Get items (SharePoint) — Filter Query ---
RequestId eq '@{outputs('Compose_RequestId')}'

# --- Condition: already processed? ---
@greater(length(body('Get_items')?['value']), 0)
#   If yes  -> Terminate, status = Succeeded, message = 'Duplicate trigger, no action taken'
#   If no   -> continue to Create item

# WRONG — the classic mistake, planted in the Lab 2a starter:
# @{concat('LR-', utcNow())}    <- a new key every run, so the guard NEVER matches
```

### 4. Conditions, switches, and keeping rules out of the flow

A condition is a two-way test. A switch is a multi-way test on a single value. Both are trivial. The design skill is knowing what *not* to put inside them.

The Injaz delegation matrix — who approves whose leave — changes constantly: a director travels and delegates, a department is restructured, a new grade band is introduced. If those rules live inside a switch in the flow, every change is a flow edit, and every flow edit is a change request, a test cycle, and a person who has left the agency. **Put the rules in a maintained SharePoint list and have the flow look them up.** The flow then encodes *how* routing works and never *who* routes.

```text
# injaz/registers/DelegationMatrix — SharePoint list, maintained by HR, not by the flow builder
Title                 Single line of text   e.g. "Annual / Grade 9-11 / Shared Services"
RequestType           Choice                Annual | Sick | Unpaid | Emergency | Study
GradeBandFrom         Number
GradeBandTo           Number
Department            Choice
PrimaryApprover       Person or Group
DelegateApprover      Person or Group       (used when DelegationActive = Yes)
DelegationActive      Yes/No
DelegationValidUntil  Date
EscalationApprover    Person or Group       (used after 48 h idle — see the chase loop)
SLAHours              Number                24 for Emergency, 48 for Annual/Sick, 72 for Unpaid/Study

# The flow's lookup — Get items, Filter Query:
RequestType eq '@{triggerOutputs()?['body/requestType']}'
  and GradeBandFrom le @{outputs('Get_employee')?['body/grade']}
  and GradeBandTo ge @{outputs('Get_employee')?['body/grade']}
  and Department eq '@{outputs('Get_employee')?['body/department']}'

# Choosing primary vs delegate, in one expression:
@{if(
    and(
      equals(first(body('Get_delegation_rule')?['value'])?['DelegationActive'], true),
      less(utcNow(), first(body('Get_delegation_rule')?['value'])?['DelegationValidUntil'])
    ),
    first(body('Get_delegation_rule')?['value'])?['DelegateApprover']?['Email'],
    first(body('Get_delegation_rule')?['value'])?['PrimaryApprover']?['Email']
)}
```

**Always include the switch default.** A switch on `RequestType` with five cases and no default will, when HR adds a sixth type next year, do absolutely nothing — silently, with a green successful run. The default case must route to a human queue and notify the flow owner. Teach the rule: *a switch without a default is a bug, not a style choice.*

### 5. Loops and the concurrency hazard

`Apply to each` repeats a set of actions over a collection. In Power Automate it defaults to running up to 20 iterations **in parallel**, which is fast and, for anything that touches a shared variable, wrong.

The classic failure: a chase flow loops over 40 idle requests, and inside the loop appends the request reference to a variable `varChaseSummary` for a digest email. With concurrency on, several iterations read the variable at the same moment, and the digest arrives with 26 of the 40 references. Nothing errors. Nobody notices for six months.

| Situation | Concurrency setting | Why |
|---|---|---|
| Each iteration is fully independent (send an email per row, create an item per row) | On, degree 20 | Fastest, and safe — no shared state |
| Iterations append to a variable, increment a counter, or build a string | **Off (degree 1)** | Parallel writes to a variable are not safe |
| Iterations write to the same SharePoint item or Excel row | **Off (degree 1)** | Last-write-wins corruption |
| Calling a rate-limited external service | On, degree 2–5 | Balance speed against throttling |

The better fix, where possible, is to avoid the shared variable altogether: build the digest with a `Select` action that projects the array into the shape you need, then a `Join` — no loop, no variable, no hazard, and about ten times faster.

```text
# injaz/flows/leave-chase/build-digest-without-a-loop.txt
# Replaces: apply-to-each + append-to-string-variable (the concurrency hazard)
# With:     Select (project) + Join (flatten). No shared state, deterministic order.

# --- Select action, "From" ---
@{body('Get_idle_requests')?['value']}

# --- Select action, "Map" (text mode) ---
@{concat(
    '• ', item()?['RequestId'],
    '  |  ', item()?['Requester']?['DisplayName'],
    '  |  idle ', string(div(sub(ticks(utcNow()), ticks(item()?['SubmittedOn'])), 36000000000)), ' h',
    '  |  approver: ', item()?['CurrentApprover']?['DisplayName']
)}

# --- Join action, Delimiter: \n ---
@{join(body('Select_digest_lines'), decodeUriComponent('%0A'))}

# Result (deterministic, complete, one action):
# • LR-20260517-A.ALMUTAIRI-3f9c1b7d  |  Abdullah Al-Mutairi  |  idle 52 h  |  approver: Nouf Al-Harbi
# • LR-20260518-S.ALQAHTANI-91b0e2af  |  Sara Al-Qahtani      |  idle 49 h  |  approver: Nouf Al-Harbi
```

### 6. Error handling: scopes, run-after, retries, and the failure notifier

Power Automate has no `try/catch` keyword, but it has the same thing built from two features: **scopes** (a container of actions) and **configure run after** (which controls whether an action runs on success, failure, skip, or timeout).

```text
Scope: TRY      -> the real work
Scope: CATCH    -> configure run after = [has failed, has timed out]  on TRY
Scope: FINALLY  -> configure run after = [is successful, has failed, is skipped, has timed out] on TRY and CATCH
```

The CATCH scope must do three things, in this order, every time: **write a failure record** to a `FlowFailures` list (so the failure is durable and countable, not just an email somebody deletes), **notify a named human** — a person, not a shared mailbox nobody reads — and **leave the case in a recoverable state**, meaning the record either was never created or is clearly marked as incomplete. A CATCH that only sends an email is half an error handler.

**Retry policies** are configured per action, and the right setting depends entirely on what kind of failure you are protecting against:

| Failure type | Example | Retry policy | Reasoning |
|---|---|---|---|
| Transient service unavailability | SharePoint returns 503 at month-end | Exponential, 4 retries, interval PT10S | It will probably work in 30 seconds; back off so you do not add load |
| Throttling (429) | Too many calls to Excel Online | Exponential, 4 retries, interval PT20S | The service is telling you to slow down; obey it |
| Timeout on a slow document operation | A 40-page scanned PDF | Fixed, 2 retries, interval PT30S | Worth one more attempt, but not four |
| Bad input (400, 404) | Malformed request payload; approver's account deleted | **None** | Retrying a wrong request four times just fails four times, eight minutes later |
| Permission denied (403) | Connector not authorised | **None** | Retrying will never fix authorisation; go straight to CATCH |

The default policy on most actions is exponential with 4 retries, which is wrong for the bottom two rows. Teach participants to *set it deliberately* on every action that calls another system, and to set it to **None** on anything whose failure means "the input was wrong".

### 7. Testing before you touch live data

The rule for this cohort, stated as an absolute: **no Injaz flow points at a live list until it has completed twenty consecutive successful runs against a mirror.**

The mirror pattern: every Injaz SharePoint list has a twin with a `_TEST` suffix and identical columns. The flow's list name is held in an environment variable, not hard-coded, so promoting from test to live is a configuration change, not a flow edit. The test data set contains eight deliberately awful cases: a request with a missing field, one with dates reversed, one from an employee whose approver has left the agency, one submitted twice within four seconds, one with an Arabic name containing a character the form encodes oddly, one exceeding the leave balance, one for a request type that does not exist in the delegation matrix, and one perfectly normal request so the happy path is proven too.

```text
# injaz/test-data/leave_requests_test_set.csv
# Eight cases. Every Injaz flow ships with an equivalent set. Expected outcome is
# part of the data, so the test is self-checking.
case,requestType,startDate,endDate,employeeId,grade,expected_outcome
T1-happy,Annual,2026-06-01,2026-06-05,EMP-4471,10,"routed to primary approver Nouf Al-Harbi; record created"
T2-missing-field,Annual,,2026-06-05,EMP-4471,10,"validation fails; requester notified; NO record created"
T3-dates-reversed,Annual,2026-06-05,2026-06-01,EMP-4471,10,"validation fails; requester notified; NO record created"
T4-approver-left,Sick,2026-06-02,2026-06-03,EMP-8823,9,"delegation lookup empty; routed to EscalationApprover; owner notified"
T5-duplicate,Annual,2026-06-01,2026-06-05,EMP-4471,10,"idempotency guard fires; run terminates Succeeded; ONE record total"
T6-arabic-name,Annual,2026-06-10,2026-06-12,EMP-6190,11,"record created; name renders as عبدالعزيز الشمري in the list and the email"
T7-over-balance,Annual,2026-06-01,2026-06-30,EMP-4471,10,"balance check fails; routed to HR exception queue; NOT auto-rejected"
T8-unknown-type,Sabbatical,2026-07-01,2026-07-30,EMP-4471,10,"switch DEFAULT case fires; routed to human queue; owner notified"
```

Note T7 carefully. A request exceeding the leave balance is **not automatically rejected** — that is a decision affecting an employee's entitlement, and it goes to a human. This is the human-in-the-loop spine appearing inside a technical test file, which is exactly where it should appear.

### 8. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *One action, one job.* A giant expression that does four transformations cannot be debugged by the person who inherits it.
- *Rules live in lists, logic lives in flows.* If a business person needs to change it, it is data.
- *Every flow is idempotent or it is a liability.* Deterministic key, look-up, terminate.
- *Every switch has a default; every default notifies a human.*
- *Name every action in English, descriptively.* `Get_delegation_rule` not `Get items 3`. Six months later this is the only documentation that exists.
- *Failure must be loud and durable.* A failure record in a list plus a named human notified within one minute.

**Common mistakes (each is deliberately planted in the Lab 2a/2b starter)**
1. The `RequestId` is built with `utcNow()`, so the idempotency guard never matches and duplicates are created every time.
2. The `apply to each` that builds the chase digest has concurrency on and appends to a shared variable — the digest is short by a random amount every run.
3. The switch on `RequestType` has no default case, so the `Sabbatical` test row completes "successfully" with nothing done.
4. The retry policy on the "get employee record" action is exponential/4 even though its failure mode is a 404 for a deleted employee — the flow takes eight minutes to fail.
5. The CATCH scope only sends an email and writes no failure record, so failures are invisible in any report and nobody can count them.
6. The list name is hard-coded to the live list rather than read from an environment variable, so the "test" run writes to production on the first attempt.

**Production considerations**
- Set the flow's **run-history retention** consciously: 28 days is the platform default and is shorter than most audit expectations. Write your own durable audit record (Module 7).
- Turn on **flow failure notifications to the owner** at minimum, but do not rely on them; owners change and the setting does not follow.
- Use a **service account**, not a personal account, for connections. When Abdullah transfers to another agency, his personal connections die and so do fourteen flows. This is the most common cause of mass automation failure in government tenants.
- Keep flows under about 40 actions. Beyond that, split into a parent flow and child flows so that each piece is testable and comprehensible.

### 9. Real-world example walkthrough

Narrate this in five minutes. A regional authority automated its overtime-claim routing. The flow worked beautifully for eleven weeks. In week twelve, the finance system had a two-hour outage on the 28th of the month — the busiest claim day. Forty-one claims triggered the flow; each one hit a 503 on the "post to finance" step; the flow had no CATCH scope; each run ended in a red "Failed" state in a run history nobody looked at. The claims had already been marked "Submitted to finance" by an earlier step. Six weeks later, forty-one employees had not been paid overtime, and nobody could produce a list of who because the run history had rolled off at 28 days. The fix was four actions long: wrap the finance call in a TRY scope, add a CATCH that writes a row to `FlowFailures` and emails the finance duty officer, set the "mark as submitted" step to run only *after* the finance call succeeds, and add an exponential retry. Total build time: twenty minutes. The lesson to land hard: **the error handler is not the polish you add if there is time. It is the reason anyone will still trust the flow next year.**

## Code Examples

### The complete Injaz leave-request routing flow definition

```json
// injaz/flows/leave-request-routing/definition.json  (core actions; full package in the lab solution)
// Remove this comment line before importing. Trigger: Microsoft Forms submission.
// Pattern: idempotency guard -> validate -> delegation lookup -> switch -> record -> approval.
{
  "definition": {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": { "listSuffix": { "type": "String", "defaultValue": "_TEST" } },
    "triggers": {
      "When_a_leave_form_is_submitted": {
        "type": "OpenApiConnectionWebhook",
        "inputs": { "host": { "connectionName": "shared_microsoftforms", "operationId": "CreateFormWebhook" },
                    "parameters": { "form_id": "INJAZ-LEAVE-2026" } },
        "splitOn": "@triggerOutputs()?['body/value']"
      }
    },
    "actions": {
      "TRY": { "type": "Scope", "runAfter": {}, "actions": {

        "Compose_RequestId": { "type": "Compose", "runAfter": {},
          "inputs": "@concat('LR-', formatDateTime(triggerOutputs()?['body/submitDate'],'yyyyMMdd'), '-', toUpper(split(triggerOutputs()?['body/responder'],'@')[0]), '-', substring(triggerOutputs()?['body/responseId'],0,8))" },

        "Get_existing_request": { "type": "OpenApiConnection",
          "runAfter": { "Compose_RequestId": ["Succeeded"] },
          "inputs": { "host": { "connectionName": "shared_sharepointonline", "operationId": "GetItems" },
            "parameters": { "table": "@concat('LeaveRequests', parameters('listSuffix'))",
              "$filter": "@concat('RequestId eq ', outputs('Compose_RequestId'))", "$top": 1 } },
          "retryPolicy": { "type": "exponential", "count": 4, "interval": "PT10S" } },

        "Condition_already_processed": { "type": "If",
          "runAfter": { "Get_existing_request": ["Succeeded"] },
          "expression": { "greater": ["@length(body('Get_existing_request')?['value'])", 0] },
          "actions": { "Terminate_duplicate": { "type": "Terminate", "inputs": { "runStatus": "Succeeded" } } },
          "else": { "actions": {} } },

        "Get_employee": { "type": "OpenApiConnection",
          "runAfter": { "Condition_already_processed": ["Succeeded"] },
          "inputs": { "host": { "connectionName": "shared_sharepointonline", "operationId": "GetItems" },
            "parameters": { "table": "EmployeeDirectory",
              "$filter": "@concat('EmployeeId eq ', triggerOutputs()?['body/employeeId'])" } },
          "retryPolicy": { "type": "none" } },

        "Switch_on_request_type": { "type": "Switch",
          "runAfter": { "Get_delegation_rule": ["Succeeded"] },
          "expression": "@triggerOutputs()?['body/requestType']",
          "cases": {
            "Annual":    { "case": "Annual",    "actions": { "SLA_48":  { "type": "Compose", "inputs": 48 } } },
            "Sick":      { "case": "Sick",      "actions": { "SLA_48s": { "type": "Compose", "inputs": 48 } } },
            "Emergency": { "case": "Emergency", "actions": { "SLA_24":  { "type": "Compose", "inputs": 24 } } },
            "Unpaid":    { "case": "Unpaid",    "actions": { "SLA_72":  { "type": "Compose", "inputs": 72 } } },
            "Study":     { "case": "Study",     "actions": { "SLA_72s": { "type": "Compose", "inputs": 72 } } } },
          "default": { "actions": { "Route_unknown_type_to_human": { "type": "OpenApiConnection",
            "inputs": { "host": { "connectionName": "shared_sharepointonline", "operationId": "PostItem" },
              "parameters": { "table": "ExceptionQueue", "item/Title": "@outputs('Compose_RequestId')",
                "item/Reason": "@concat('Unknown request type: ', triggerOutputs()?['body/requestType'])",
                "item/AssignedTo/Claims": "hr.duty@agency.gov.sa" } } } } } },

        "Start_approval": { "type": "OpenApiConnection",
          "runAfter": { "Create_leave_record": ["Succeeded"] },
          "inputs": { "host": { "connectionName": "shared_approvals", "operationId": "StartAndWaitForAnApproval" },
            "parameters": { "ApprovalCreationInput/assignedTo": "@body('Create_leave_record')?['CurrentApprover']?['Email']",
              "ApprovalCreationInput/details": "You are the accountable approver. This request has NOT been decided by the automation." } } }
      } },

      "CATCH": { "type": "Scope", "runAfter": { "TRY": ["Failed", "TimedOut"] }, "actions": {
        "Write_failure_record": { "type": "OpenApiConnection",
          "inputs": { "parameters": { "table": "FlowFailures",
            "item/FailedAction":  "@{first(where(result('TRY'), item()?['status'] eq 'Failed'))?['name']}",
            "item/ErrorMessage":  "@{first(where(result('TRY'), item()?['status'] eq 'Failed'))?['error']?['message']}",
            "item/RunId": "@workflow()['run']['name']" } } },
        "Notify_named_owner": { "type": "OpenApiConnection",
          "runAfter": { "Write_failure_record": ["Succeeded", "Failed"] },
          "inputs": { "parameters": { "emailMessage/To": "hr.automation.owner@agency.gov.sa",
            "emailMessage/Subject": "@concat('[Injaz FAILURE] leave-request-routing - ', outputs('Compose_RequestId'))" } } }
      } },

      "FINALLY": { "type": "Scope",
        "runAfter": { "TRY": ["Succeeded","Failed","Skipped","TimedOut"], "CATCH": ["Succeeded","Failed","Skipped"] },
        "actions": { "Write_audit_row": { "type": "OpenApiConnection",
          "inputs": { "parameters": { "table": "AutomationAuditLog",
            "item/FlowName": "leave-request-routing", "item/RunId": "@workflow()['run']['name']",
            "item/Outcome": "@result('TRY')[0]?['status']", "item/CompletedOn": "@utcNow()" } } } } }
    }
  }
}
```

### The same routing logic in n8n (open-source alternative)

```json
// injaz/flows/leave-request-routing/n8n-workflow.json
// For agencies without a Microsoft 365 estate, or where Power Automate premium
// connectors are blocked. Same six primitives, same idempotency guard, same switch default.
{
  "name": "Injaz — Leave Request Routing",
  "nodes": [
    { "name": "Form Submitted", "type": "n8n-nodes-base.webhook", "position": [200, 300],
      "parameters": { "path": "injaz-leave", "httpMethod": "POST", "responseMode": "onReceived" } },

    { "name": "Build RequestId", "type": "n8n-nodes-base.set", "position": [420, 300],
      "parameters": { "values": { "string": [ { "name": "requestId",
        "value": "=LR-{{ $json.submitDate.replaceAll('-','') }}-{{ $json.responder.split('@')[0].toUpperCase() }}-{{ $json.responseId.substring(0,8) }}" } ] } } },

    { "name": "Lookup Existing", "type": "n8n-nodes-base.postgres", "position": [640, 300],
      "parameters": { "operation": "executeQuery",
        "query": "SELECT id FROM leave_requests WHERE request_id = $1 LIMIT 1",
        "options": { "queryReplacement": "={{ $json.requestId }}" } },
      "retryOnFail": true, "maxTries": 4, "waitBetweenTries": 10000 },

    { "name": "Already Processed?", "type": "n8n-nodes-base.if", "position": [860, 300],
      "parameters": { "conditions": { "number": [ { "value1": "={{ $items().length }}", "operation": "larger", "value2": 0 } ] } } },

    { "name": "Stop — Duplicate", "type": "n8n-nodes-base.noOp", "position": [1080, 200] },

    { "name": "Route by Type", "type": "n8n-nodes-base.switch", "position": [1080, 400],
      "parameters": { "dataType": "string", "value1": "={{ $('Form Submitted').item.json.requestType }}",
        "rules": { "rules": [
          { "value2": "Annual", "output": 0 }, { "value2": "Sick", "output": 0 },
          { "value2": "Emergency", "output": 1 }, { "value2": "Unpaid", "output": 2 },
          { "value2": "Study", "output": 2 } ] },
        "fallbackOutput": 3 } },

    { "name": "Exception Queue (default)", "type": "n8n-nodes-base.postgres", "position": [1300, 560],
      "parameters": { "operation": "insert", "table": "exception_queue",
        "columns": "request_id,reason,source_flow,assigned_to" },
      "notesInFlow": true, "notes": "Switch fallback. NEVER leave this unwired." },

    { "name": "Create Record", "type": "n8n-nodes-base.postgres", "position": [1300, 400],
      "parameters": { "operation": "insert", "table": "leave_requests" },
      "retryOnFail": true, "maxTries": 4, "waitBetweenTries": 10000,
      "onError": "continueErrorOutput" },

    { "name": "Notify Owner on Failure", "type": "n8n-nodes-base.emailSend", "position": [1520, 540],
      "parameters": { "toEmail": "hr.automation.owner@agency.gov.sa",
        "subject": "=[Injaz FAILURE] leave-request-routing — {{ $json.requestId }}" } }
  ],
  "settings": { "errorWorkflow": "injaz-global-error-handler", "executionOrder": "v1" }
}
```

### The chase loop: a scheduled flow that pursues idle requests

```text
# injaz/flows/leave-chase/recurrence-and-filter.txt
# Trigger: Recurrence, every day at 08:00 Arab Standard Time.
# Purpose: find requests idle beyond their SLA, chase once, escalate after a second cycle.
# This flow is what converts the 4.5-day leave cycle time into 1.1 days.

# --- Recurrence trigger settings ---
Frequency:  Day
Interval:   1
Time zone:  Arab Standard Time            <- NOT UTC. Set this explicitly or it fires at 11:00.
At these hours: 8
At these minutes: 0

# --- Get items: LeaveRequests, Filter Query ---
ProcessingStatus eq 'AwaitingApproval' and DueBy lt '@{utcNow()}'

# --- Compute idle hours for each item (inside Select, no loop needed) ---
@{div(sub(ticks(utcNow()), ticks(item()?['Created'])), 36000000000)}

# --- Condition: first chase or escalate? ---
@greater(int(item()?['ChaseCount']), 0)
#   true  -> escalate to EscalationApprover from DelegationMatrix, set ChaseCount = 2
#   false -> chase CurrentApprover, set ChaseCount = 1

# --- Apply to each: CONCURRENCY OFF (degree 1) ---
# Reason: each iteration increments ChaseCount on the item and appends to the digest.
# With concurrency ON the digest silently loses rows. This is planted in the Lab 2b starter.

# --- Expected run output, 2026-06-18 ---
# Get items: 14 requests past SLA
#   first chase   : 9   (ChaseCount 0 -> 1)
#   escalated     : 5   (ChaseCount 1 -> 2, EscalationApprover notified)
#   digest email  : 14 lines to hr.duty@agency.gov.sa   <- must equal 14, not 11
```

## Hands-on Lab 2 — Build and Harden the Injaz Leave-Request Routing Flow

| | |
|---|---|
| **Objective** | Build a leave-request routing flow with a form trigger, validation, an idempotency guard, a delegation-matrix lookup, a switch with a default, and an approval — then harden it with TRY/CATCH/FINALLY scopes, deliberate retry policies, a failure notifier and a chase loop; prove all eight test cases pass and claim the 90 h/month saving |
| **Duration** | Lab 2a 50 min (Day 1 Hour 5) + Lab 2b 50 min (Day 2 Hour 2) = 100 minutes |
| **Setup** | Import `Injaz_Lab2_Start_1_0_0_1.zip` into the **training tenant** (creates `LeaveRequests_TEST`, `EmployeeDirectory`, `DelegationMatrix`, `ExceptionQueue`, `FlowFailures`, `AutomationAuditLog` and the Injaz leave Form). Standard connectors only — Forms, SharePoint, Outlook, Approvals. Environment variable `listSuffix` set to `_TEST`. |

**Instructions & tasks**

1. *(12 min)* **Lab 2a — trigger and guard.** Wire the Forms trigger, build `Compose_RequestId`, and add `Get_existing_request` + `Condition_already_processed`. The starter builds the key with `utcNow()`; fix it to the deterministic form. Submit test case **T5-duplicate** twice within four seconds and confirm exactly one record exists.
2. *(14 min)* **Lab 2a — validation and routing.** Add the `Validate_request` condition (T2, T3 must fail cleanly with the requester notified and no record created), the `Get_delegation_rule` lookup, and the `Switch_on_request_type`. Add the **default case** the starter omits and route it to `ExceptionQueue`. Run T8-unknown-type and confirm the exception row appears.
3. *(14 min)* **Lab 2a — record and approve.** Add `Create_leave_record`, `Start_approval` and `Record_outcome`. Confirm the approval card text contains the sentence *"You are the accountable approver. This request has NOT been decided by the automation."* Run T1-happy and T6-arabic-name; verify عبدالعزيز الشمري renders correctly in both the list and the email.
4. *(10 min)* **Lab 2a — the balance trap.** Run T7-over-balance. The starter auto-rejects it. Change the behaviour: route to the HR exception queue instead, and write in `LAB2_NOTES.md` one sentence explaining why an entitlement refusal must not be automated.
5. *(16 min)* **Lab 2b — scopes and retries.** Move all work into a `TRY` scope; add `CATCH` (run after Failed/TimedOut) writing to `FlowFailures` and notifying the named owner; add `FINALLY` writing to `AutomationAuditLog`. Set `retryPolicy` deliberately on all four external actions — **none** on `Get_employee` (404 for a deleted employee) and on the invalid-request notification, exponential/4/PT10S on the three SharePoint calls. Break the flow on purpose by pointing `Get_delegation_rule` at a non-existent list and confirm CATCH fires within 60 seconds.
6. *(16 min)* **Lab 2b — the chase loop and the concurrency hazard.** Build the daily 08:00 recurrence chase flow. Run it against 14 seeded idle requests with `apply to each` concurrency **on** and count the digest lines (you will get 10–13). Turn concurrency off, re-run, confirm 14. Then replace the loop entirely with `Select` + `Join` and confirm 14 again, faster. Record the run in the register: `feat(leave): routing + chase with TRY/CATCH, idempotent, 90 h/month`.

**Expected output**
```text
=== Lab 2a — test set results (LeaveRequests_TEST) ===
T1-happy          PASS  record LR-20260601-A.ALMUTAIRI-3f9c1b7d created, approver Nouf Al-Harbi
T2-missing-field  PASS  validation failed, requester notified, 0 records created
T3-dates-reversed PASS  validation failed, requester notified, 0 records created
T4-approver-left  PASS  delegation empty -> EscalationApprover Faisal Al-Dossari, owner notified
T5-duplicate      PASS  2 runs, 1 record. Run 2 terminated Succeeded "Duplicate trigger"
T6-arabic-name    PASS  عبدالعزيز الشمري rendered correctly in list + email body
T7-over-balance   PASS  routed to ExceptionQueue (NOT auto-rejected)  <- corrected from starter
T8-unknown-type   PASS  switch DEFAULT fired, ExceptionQueue row created, owner notified
8/8 passing — flow eligible for promotion to live (listSuffix -> '')

=== Lab 2b — deliberate failure drill ===
Get_delegation_rule -> 404 (list 'DelegationMatrixX' not found)
  retryPolicy: none      -> failed in 0.8 s (correct; a 404 is not transient)
  TRY status: Failed
  CATCH fired at +2.1 s  -> FlowFailures row 41 written
                         -> email to hr.automation.owner@agency.gov.sa delivered +11 s
  FINALLY fired          -> AutomationAuditLog row written, Outcome = Failed
  No orphan record in LeaveRequests_TEST                        <- recoverable state confirmed

=== Lab 2b — chase loop, concurrency drill ===
run 1  concurrency ON  (degree 20)  : 14 items processed, digest contained 11 lines  ** DEFECT **
run 2  concurrency OFF (degree 1)   : 14 items processed, digest contained 14 lines
run 3  Select + Join, no loop       : 14 items processed, digest contained 14 lines, 6.2 s -> 0.7 s

=== Benefit claimed ===
Leave / HR routing: 900 requests/month × (8 min -> 2 min) = 90 h/month, 1,080 h/year
Cycle time: 4.5 days -> 1.1 days (chase loop)
```

**Acceptance criteria**
- All eight test cases pass, including T5 producing exactly one record and T7 routing to the exception queue rather than auto-rejecting.
- The switch has a default case that creates an `ExceptionQueue` row and notifies a named owner.
- CATCH writes a durable `FlowFailures` record *and* notifies a named person; FINALLY writes an audit row on every path including success.
- Retry policies are set deliberately per action, with `none` on the two actions whose failures are non-transient, and the participant can explain each choice.
- The chase digest contains exactly 14 lines, and the participant can state why the concurrent version lost rows.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Duplicate records created on every submission | `RequestId` built with `utcNow()` — a new key every run | Build the key from trigger fields only: date + responder + responseId |
| Flow triggers itself repeatedly, hundreds of versions | "When an item is modified" trigger + the flow modifies the same item | Trigger on creation, or add the service-account trigger condition, or write to a different list |
| `Sabbatical` request completes green but nothing happens | Switch has no default case | Add the default; route to `ExceptionQueue` and notify |
| Flow takes 8 minutes to report a deleted employee | Exponential retry on an action whose failure is a 404 | Set `retryPolicy: none` on `Get_employee` |
| Chase digest is short by a random number of lines | `apply to each` concurrency on + append-to-variable | Concurrency off, or replace the loop with `Select` + `Join` |
| "You do not have a licence for this connector" | Premium connector (HTTP, Dataverse, AI Builder) in the starter | Use the standard-connector variant: SharePoint + Outlook + Approvals only. Instructor has the training-tenant fallback |
| Chase flow fires at 11:00 instead of 08:00 | Recurrence trigger defaulted to UTC | Set Time zone = Arab Standard Time explicitly on the trigger |

**Instructor notes.** The concurrency drill in task 6 is the emotional peak of Day 2 morning — participants watch a flow report a completely successful run while silently producing wrong output, and the room goes quiet. Do not skip it even if you are behind; cut task 4 instead and cover the balance trap verbally. Second thing to watch: participants will set every retry policy to exponential/4 because it is the default and it feels safe. Stop the room and ask what happens when you retry a 404 four times — the answer, *"you wait eight minutes to find out something you knew in one second"*, is the point. Fast finishers: add a second child flow that runs the eight-case test set on demand and posts a pass/fail summary to Teams — that becomes the regression harness for the capstone, and several participants will take it back to their own agency.

## Mini Exercises

**Quiz (5 questions)**
1. What does idempotent mean, and what makes a key idempotent? → running twice does the same as running once; the key is built deterministically from the trigger payload, never from `utcNow()`.
2. A switch has five cases and the business adds a sixth value. What happens with no default? → the flow completes successfully and does nothing — a silent failure.
3. When should a retry policy be `none`? → when the failure is not transient: 400, 404, 403 — bad input or permissions.
4. Why must `apply to each` concurrency be off when appending to a variable? → parallel iterations overwrite each other's writes; output is silently incomplete.
5. What three things must a CATCH scope do? → write a durable failure record, notify a named human, leave the case recoverable.

**Debugging exercise.** Provide the `lab2-broken` solution: the trigger is "when an item is created or modified", the flow patches the same item, and there is no trigger condition. Symptom: 340 versions of one list item in ninety seconds and a throttled connection. Participants must diagnose the self-trigger loop and fix it three different ways, then argue which fix they would use in production and why.

**Design exercise.** The HR director wants leave requests over 20 days routed to the DG rather than the department head. Design the change so that no flow edit is required — then state what would have to be true of the `DelegationMatrix` list for that to work, and who owns maintaining it.

**Discussion questions.**
- Your flow has run 2,400 times with a 99.2% success rate. Nineteen runs failed. Is that a good flow? What would you need to know about those nineteen before answering?
- Every automation in your department is connected using one senior officer's personal account. He is transferring to another entity in six weeks. What is your remediation plan, and what does this incident say about how automations should be provisioned in the first place?

## Case Study — The Self-Triggering Flow at "Tanseeq" (تنسيق)

**Scenario.** "Tanseeq" (تنسيق), the inter-ministerial coordination office supporting a national programme in Riyadh, built a flow to stamp a tracking reference onto every task item created in its coordination list. The flow was triggered on "when an item is created or modified" and wrote the reference back to the same item.

**Business context.** The list holds 4,000 live coordination tasks across nine ministries, and its version history is the office's evidence of who committed to what and when. The office is audited annually on that history.

**Technical challenge.** The flow triggered itself. Each write produced a modification, which produced a trigger, which produced a write. Platform loop protection stopped it after roughly 40 minutes — during which 1,850 list items accumulated between 90 and 300 versions each, the SharePoint connection was throttled for the tenant, and four unrelated flows in other departments failed because they shared the connection.

**Constraints.** Version history cannot be bulk-deleted without a records-management approval, because the same history is the audit evidence. The list is used live by nine ministries and cannot be taken offline during working hours. The office's automation was built by a coordinator who has since moved to another role and left no documentation.

**Solution approach (facilitate, don't lecture).** Steer the room toward: (1) stop the flow immediately and confirm the throttle window; (2) diagnose the loop — the trigger condition is the missing control, and there are three valid fixes with different trade-offs; (3) decide the records question deliberately, involving the records officer, rather than deleting history to make the problem look smaller; (4) reflect that the *technical* fix is one expression, while the *organisational* fix is a change-control rule that no flow triggering on modification may write to its own source list without a documented trigger condition; and (5) note that a shared service account and a documented handover would have made the diagnosis a ten-minute job instead of a two-day one.

**Discussion questions.**
1. Three fixes exist for a self-triggering flow. Name them and rank them for a list that genuinely must be updated by the flow.
2. Four unrelated flows in other departments failed. What does that reveal about how connections and throttling are shared in a tenant, and what governance follows from it?
3. Should the junk versions be deleted? Argue both sides, then say who in the agency actually has authority to decide.
4. The builder had left. What single artefact would have reduced the diagnosis from two days to ten minutes, and whose job is it to require that artefact exists?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Test cases passing | Correctness | 8 / 8 | test-set run summary |
| Idempotency | Correctness | duplicate submission produces exactly 1 record | T5 run, list count |
| Exception handling coverage | Reliability | every failure path writes a `FlowFailures` row and notifies a named human | failure drill |
| Time to human notification on failure | Reliability | ≤ 60 seconds | failure drill timestamps |
| Hours saved per month (leave routing) | Benefit | 90 h/month (1,080 h/year) | baseline 8 min → 2 min × 900/month |
| Cycle time (leave request) | Benefit | 4.5 days → ≤ 1.2 days | list Created → DecidedOn median |

**Example benchmark table (filled during lab):**

| Drill | Configuration | Result | Correct? |
|---|---|---|---|
| Duplicate submission | `RequestId` from `utcNow()` | 2 records | No |
| Duplicate submission | deterministic `RequestId` | 1 record, run 2 terminated Succeeded | Yes |
| Deleted-employee lookup | retry exponential/4/PT10S | failed after 8 min 04 s | No |
| Deleted-employee lookup | retry none | failed after 0.8 s, CATCH at 2.1 s | Yes |
| Chase digest, 14 idle items | concurrency 20, append to variable | 11 lines, run green | No |
| Chase digest, 14 idle items | `Select` + `Join`, no loop | 14 lines, 0.7 s | Yes |

## Required Visuals and Training Assets

### Diagrams
1. **The six primitives** — *Purpose:* the mental model for the whole course. *Elements:* six labelled blocks (trigger, action, condition, switch, loop, error handler) with one Injaz example beneath each, and the Arabic term in a subtitle (مشغّل، إجراء، شرط، مبدّل، حلقة، معالج أخطاء). *Style:* flat blocks in a single row, colour-coded and reused as icons in every later module diagram.
2. **TRY / CATCH / FINALLY with run-after arrows** — *Purpose:* make `configure run after` visible. *Elements:* three stacked scopes; green arrow (Succeeded), red arrow (Failed/TimedOut), grey arrow (Skipped), each labelled with the exact run-after configuration. *Style:* flowchart with the arrow legend as a key. *Designer description:* "Three rounded containers stacked vertically; arrows drawn between them, each annotated with its run-after states; the CATCH box contains three sub-items: write record, notify human, leave recoverable."
3. **The self-trigger loop** — *Purpose:* prevent the Tanseeq incident. *Elements:* a circular arrow from "flow writes item" back to "item modified trigger", with a version counter spinning up to 300 and a red throttle badge; three labelled exits showing the three fixes. *Style:* single vicious circle with escape routes.
4. **Concurrency hazard** — *Purpose:* make the invisible defect visible. *Elements:* four parallel loop iterations reading the same variable at the same instant, with two writes overwriting each other and the resulting digest showing 11 of 14 lines. *Style:* timeline with four parallel tracks and collision markers.

### Images (screenshots)
1. **A red run history with CATCH fired** — *why:* participants must recognise what a healthy failure looks like; *content:* the run detail showing TRY failed, CATCH succeeded, FINALLY succeeded, and the resulting `FlowFailures` row.
2. **The retry policy panel** — *why:* it is buried in Settings and most participants never find it; *content:* the panel open on `Get_employee` with Type = None selected and an annotation explaining why.
3. **`apply to each` settings with concurrency control on and degree 1** — *why:* the exact toggle that fixes the digest defect; *content:* the settings pane with the slider and a caption naming the hazard.

### Simulations
1. **The runaway trigger** — *Setup:* branch `sim-selftrigger` on a 20-item list. *Expected behaviour:* version counts climb into the hundreds within two minutes; the connection throttles. *Learning objective:* modification triggers plus self-writes equal a production incident; trigger conditions are not optional.
2. **Silent partial output** — *Setup:* the chase digest with concurrency on, run three times over 14 items. *Expected behaviour:* 11, 13 and 12 lines on successive runs, all reported green. *Learning objective:* a green run is not proof of a correct result.

### Interactive Activities
- **Human flow (15 min):** six volunteers hold the six primitive cards and physically enact a leave request walking through the room. Then the instructor hands the trigger volunteer a *second identical* request four seconds later and the room discovers idempotency the hard way.
- **Retry-policy card sort (12 min):** twelve failure scenarios (503 at month-end, deleted approver, malformed date, 429 throttle, expired connection, missing permission…) sorted onto exponential / fixed / none. Disagreements about the expired connection are the productive ones.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `leave_requests_test_set.csv` | Course-authored, eight cases with expected outcomes embedded | CSV | 8 rows | Self-checking test set for every run of Lab 2 |
| `EmployeeDirectory.xlsx` | Synthetic Saudi employee directory (names, grades, departments, leave balances) | XLSX | 240 rows | Lookup source for `Get_employee` |
| `DelegationMatrix.xlsx` | Synthetic delegation rules incl. two active delegations and one expired | XLSX | 22 rows | Routing rules; deliberately contains a gap that T4 exposes |
| `idle_requests_seed.xlsx` | 14 requests seeded past their SLA with varying idle hours | XLSX | 14 rows | The chase-loop and concurrency drill |

### Demo Requirements
- **Instructor demo (10 minutes):** build a four-action flow live from nothing — Forms trigger, create item, send email — run it, then submit the same form twice and show the two duplicate records appearing in the list. Then add the three-action idempotency guard in front and submit twice more, showing one record. Finish by deliberately renaming the SharePoint list so the flow fails, and show the CATCH scope firing and the email arriving on the projector within a minute. Ten minutes, three lessons, no slides.

---

# Module 3 — Documents and Correspondence: Extraction, Classification, Summarisation, and Structured Output

## المحور الثالث — المستندات والمراسلات

## Module Overview

**Purpose.** This is the module where AI enters the flow. Injaz receives 1,200 official letters a month, mostly in Arabic, roughly 30% of them scanned images of signed and stamped paper. Today an officer reads each one, decides what it is, writes a two-line summary, picks an owning department, applies an SLA, and types all of it into the register. This module replaces the reading-and-typing with extraction, classification and schema-constrained structured output — and keeps the confirming human exactly where they belong. It saves Injaz **180 hours a month**.

**Business relevance.** Official correspondence is the circulatory system of a Saudi government entity, and its register is a legal record. Arabic-language document processing is also the single most requested AI capability in the Saudi public sector and the one most often demonstrated badly — on clean, typed, English-adjacent PDFs that bear no resemblance to a scanned letter from a regional directorate with a stamp across the reference number. This module works with the hard case deliberately.

**Industry use cases.**
- A ministry's executive office classifies incoming letters into eight categories and assigns SLAs automatically, cutting acknowledgement time from 26 working hours to 8 minutes while the department head still confirms ownership.
- A regulatory authority extracts entity name, licence number, request type and deadline from scanned applications, populating the case system without re-keying and eliminating a 4% transcription error rate.
- A municipality's complaints unit summarises long Arabic complaint letters into a three-line brief with the original always one click away, so a supervisor triages 60 cases in the time that previously covered 20.

**Expected competencies.** After this module a participant can tell a text-layer PDF from a scanned image and route each correctly; run OCR on an Arabic document and judge whether its output is usable; write a classification prompt with a closed label set including a mandatory `uncertain` class; define a JSON schema and constrain extraction to it; parse that output in a flow; set a confidence threshold; and design an exception queue that a human actually works.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Distinguish text-layer from scanned PDFs and route each to the correct extraction path | LO4, CO1 |
| 3.2 | Run and evaluate OCR on Arabic RTL documents, including stamped and skewed scans | LO4, CO3 |
| 3.3 | Write a classification prompt with a closed label set and a mandatory `uncertain` class | LO4, CO3 |
| 3.4 | Define a JSON schema and constrain extraction output to it; parse it in a flow | LO4, CO1 |
| 3.5 | Set confidence thresholds and route low-confidence cases to a worked exception queue | LO4, LO7, CO2 |
| 3.6 | Summarise a letter faithfully without introducing information the letter does not contain | LO4, CO3 |

## Technical Content

### 1. Two kinds of PDF, two completely different problems

A **text-layer PDF** was produced digitally: the characters are in the file and can be read directly. A **scanned PDF** is a photograph of paper wrapped in a PDF container; there are no characters, only pixels, and getting text out requires OCR. Of Injaz's 1,200 monthly letters, roughly 840 are text-layer and 360 are scans.

The first action in any document flow must therefore be a **triage step**, because sending a scan down the text path yields an empty string and a flow that reports success while extracting nothing — a silent failure of exactly the kind Module 2 warned about.

| Property | Text-layer PDF | Scanned PDF |
|---|---|---|
| How to detect | Extracted text length > ~50 characters for page 1 | Extracted text is empty or a few stray characters |
| Extraction method | Direct text extraction (standard connector or `Get file content`) | OCR (AI Builder, Azure AI Document Intelligence, or an LLM with vision) |
| Typical accuracy | ~100% character fidelity | 88–97% for clean Arabic print; 60–80% for stamped, skewed or faxed |
| Cost per document | Negligible | Metered per page — budget it |
| Arabic-specific risk | Ligature and diacritic normalisation | Stamps overlaying text; RTL word order scrambled by naive readers |

### 2. Arabic, RTL, and the scanned-letter reality

Four failure modes recur in Arabic document automation and every participant should be able to name them:

**Reversed or reordered text.** Some extractors emit logical-order characters, some visual-order. A reference number `2026/م/4471` can come back as `4471/م/2026`. Always test with a document containing digits inside Arabic text, because that is where the reordering shows.

**Ligatures and letter forms.** Arabic letters change shape by position. Poor OCR emits presentation forms rather than canonical letters, so `الإدارة` looks right on screen but does not match a search for `الإدارة`. Normalise to canonical Unicode (NFKC) before storing or matching.

**Diacritics and hamza variants.** `أ`, `إ`, `ا` and `آ` are distinct code points that officials use interchangeably. Normalise alef variants and strip tashkeel before comparing names or subjects. Never normalise the *stored original* — normalise a copy used for matching, and keep the original byte-exact for the record.

**Stamps, signatures and skew.** The circular stamp lands on the reference number more often than chance would suggest. Accept that ~6% of scans will yield an unusable reference and design for it: that is what the exception queue is for, not a reason to abandon the automation.

```text
# injaz/prompts/classify_correspondence.md
# Classification prompt — closed label set, mandatory uncertain class, confidence required.
# Used by: injaz/flows/correspondence-triage. Model temperature: 0.

SYSTEM
You are a correspondence classification assistant for a Saudi government agency.
You classify incoming official letters. You do NOT decide anything, recommend any
action, or write to anyone. A human officer confirms every classification you produce.

You MUST choose exactly one label from this closed set. Never invent a label.

  official_directive      A binding instruction from a higher authority or minister
  information_request     A request for data, a report, a statistic, or a status update
  complaint               An expression of dissatisfaction about a service or a decision
  invitation              An invitation to a meeting, committee, event, or ceremony
  contract_or_procurement Anything about tenders, contracts, suppliers, or purchase orders
  hr_personnel            Secondment, transfer, training nomination, or staffing matters
  financial               Budget, payment, allocation, or financial settlement matters
  uncertain               USE THIS whenever the letter fits two labels equally, fits none,
                          or the extracted text is too damaged to read confidently

RULES
1. If your confidence in the chosen label is below 0.75, return "uncertain" instead.
2. "uncertain" is a correct and valued answer. It routes the letter to a human officer.
   You are never penalised for it. You ARE penalised for a confident wrong label.
3. Base the label only on the letter text supplied. Do not use outside knowledge about
   the sending entity.
4. Never classify a letter as "official_directive" unless the text contains an explicit
   instruction directed at this agency. A letter merely mentioning a ministerial decision
   is "information_request" or "uncertain".

OUTPUT — return only this JSON object, nothing else:
{ "label": "<one of the eight labels>",
  "confidence": <number between 0 and 1>,
  "evidence_quote": "<the exact phrase from the letter that decided the label, max 25 words>",
  "language": "ar" | "en" | "mixed" }

USER
--- LETTER TEXT BEGINS ---
{{ extracted_text }}
--- LETTER TEXT ENDS ---
```

### 3. The closed label set and why `uncertain` is mandatory

An open-ended "what kind of letter is this?" prompt returns a different taxonomy every day and cannot drive a switch. A **closed label set** — eight values, written down, versioned — makes the output routable and makes accuracy measurable against a gold set.

The `uncertain` class is not a concession to weak models; it is the mechanism that keeps the human in the loop where the machine is not competent. Without it, the model must pick something, and a forced choice on an ambiguous letter produces a *confident* wrong answer that flows straight to the wrong department. Three design rules follow:

1. **Reward `uncertain` explicitly in the prompt.** Models trained to be helpful will avoid it unless told it is a valid, valued answer.
2. **Set a numeric threshold and enforce it in the flow, not only in the prompt.** A model's self-reported confidence is a signal, not a guarantee; the flow re-checks it.
3. **Monitor the `uncertain` rate as a health metric.** Below ~3% suggests the model is over-confident or the threshold is too low. Above ~15% suggests the label set does not match reality and needs revising. Injaz targets **≤ 8%**.

### 4. Schema-constrained structured extraction

Classification tells you what kind of letter it is. **Extraction** pulls the fields the register needs. Free-text extraction produces a different shape every time; a **JSON schema** fixes the shape so the Parse JSON action can bind the fields and the rest of the flow can use them as first-class dynamic content.

```json
// injaz/schemas/correspondence_extract.schema.json
// Used by (a) the extraction prompt as the required output contract and
// (b) the Power Automate "Parse JSON" action. Keep the two identical — if they
// drift, Parse JSON fails at runtime with "required property missing".
{
  "type": "object",
  "required": ["reference_number", "sender_entity", "subject_ar", "subject_en",
               "letter_date_gregorian", "summary_ar", "summary_en",
               "suggested_owner", "extraction_confidence", "fields_uncertain"],
  "properties": {
    "reference_number":      { "type": ["string", "null"],
                               "description": "As printed. null if obscured by a stamp." },
    "sender_entity":         { "type": "string" },
    "sender_entity_en":      { "type": ["string", "null"] },
    "subject_ar":            { "type": "string", "maxLength": 200 },
    "subject_en":            { "type": "string", "maxLength": 200 },
    "letter_date_hijri":     { "type": ["string", "null"], "pattern": "^[0-9]{4}/[0-9]{2}/[0-9]{2}$" },
    "letter_date_gregorian": { "type": ["string", "null"], "format": "date" },
    "summary_ar":            { "type": "string", "maxLength": 400 },
    "summary_en":            { "type": "string", "maxLength": 400 },
    "requested_action":      { "type": ["string", "null"], "maxLength": 200 },
    "stated_deadline":       { "type": ["string", "null"], "format": "date" },
    "suggested_owner":       { "type": "string",
                               "enum": ["Legal", "Finance", "HR", "Procurement",
                                        "Operations", "Communications", "DG Office", "Unassigned"] },
    "extraction_confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "fields_uncertain":      { "type": "array", "items": { "type": "string" },
                               "description": "Names of fields the model could not read reliably. Drives the exception queue." }
  },
  "additionalProperties": false
}
```

Four schema design decisions worth stating aloud. `reference_number` is **nullable** because stamps really do obscure it — a schema that forbids null forces the model to hallucinate a number, which is far worse than a null. `suggested_owner` is an **enum**, so the value can drive a switch without normalisation, and `Unassigned` exists so the model has a legal escape. `fields_uncertain` is an **array**, which lets a letter be 90% usable and 10% queued rather than all-or-nothing. And `additionalProperties: false` stops the model adding a helpful extra field that Parse JSON has never seen.

### 5. Confidence thresholds and the exception queue

Injaz uses two thresholds and one queue.

| Path | Condition | Destination | Expected share |
|---|---|---|---|
| **Auto-register** | `label != uncertain` AND `confidence ≥ 0.75` AND `extraction_confidence ≥ 0.70` AND `fields_uncertain` is empty | Register entry created; owner notified; officer confirms in one click | ~80% |
| **Partial** | Above thresholds but `fields_uncertain` is non-empty | Register entry created as `Draft`; only the uncertain fields are presented to the officer to complete | ~12% |
| **Exception** | `label == uncertain` OR either confidence below threshold OR the source is an unusable scan | `CorrespondenceExceptions` queue with the original attached, no register entry | ~8% |

The exception queue only works if somebody works it. Design rules: it must be a **named person's queue with an SLA** (Injaz: 4 working hours), it must show the **original document first** and the machine's attempt second, the officer's correction must be **captured as labelled data** for improving the prompt, and the queue depth must appear on the same dashboard as the savings — because a growing exception queue is how an automation quietly transfers work rather than removing it.

### 6. Summarisation without invention

A summary that adds a fact the letter does not contain is worse than no summary, because it enters a legal register. Three controls: instruct extractive-leaning behaviour (prefer the letter's own phrasing), require an `evidence_quote` so a reviewer can verify the basis in two seconds, and cap length so the model cannot pad. Injaz's rule: the Arabic summary must be ≤ 400 characters, must not contain any entity name absent from the letter, and must never state a deadline that is not printed in the letter.

### 7. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Triage the document before you process it.* Text-layer and scan are different problems.
- *Closed label set, always, with `uncertain` as a first-class member.*
- *Schema first, prompt second.* The schema is the contract; the prompt serves it.
- *Null is better than invented.* Every field that can be obscured must be nullable.
- *Keep the original byte-exact.* Normalise a copy for matching; the register cites the original.
- *An exception queue with no SLA and no owner is a landfill.*

**Common mistakes (each is planted in the Lab 3 starter)**
1. No document triage — scans go down the text path and produce empty extractions with green runs.
2. The label set omits `uncertain`, so ambiguous letters get confident wrong labels.
3. `reference_number` is marked required and non-nullable, so stamped letters yield invented reference numbers.
4. The Parse JSON schema is copied from a sample output rather than the canonical schema file, so it lacks `fields_uncertain` and fails on the first partial extraction.
5. The confidence threshold is enforced in the prompt but not re-checked in the flow, so a model returning `confidence: 0.4` with a label still auto-registers.
6. Arabic subject text is stored normalised (alef variants collapsed), so the register no longer matches the letter it cites.

**Production considerations**
- OCR is metered. 360 scans a month at ~3 pages each is ~1,080 pages; check the licensing before you design.
- Version the prompt and the schema together, with the label-set version stamped on every register row, so accuracy can be attributed to a version when it changes.
- Re-measure accuracy on the gold set monthly. Letter styles drift as entities restructure.
- Never send the original letter outside the agency boundary without checking the connector's data residency — this is Module 7 material and it starts biting here.

### 8. Real-world example walkthrough

Narrate in five minutes. A regulatory authority automated licence-application intake and reported 96% extraction accuracy in its pilot. Three months into production, staff had quietly reverted to manual entry. The audit found the pilot had used 200 applications submitted through the online portal — all text-layer, all clean. Production reality was 45% scanned submissions from regional offices, many faxed. On that population, accuracy was 61%, and because the schema forbade nulls, the system had *invented* licence numbers for obscured fields — plausible ones, in the right format, wrong. Staff learned within a fortnight not to trust it. The rebuild changed three things: triage scans from text-layer at the front door, make every obscurable field nullable, and route anything with a null critical field to a human queue. Accuracy on the auto-registered subset went to 94% with a 14% exception rate, and staff trusted it because when it was unsure, it said so. The lesson: **measure on the population you will actually receive, and let the system say "I don't know".**

## Code Examples

### Document triage: text-layer or scan?

```text
# injaz/flows/correspondence-triage/triage-expression.txt
# First decision in the flow. Runs immediately after "Get file content".
# Standard-connector path: use "Convert file" (OneDrive/SharePoint) to text, then measure.
# Premium path: AI Builder "Read text in image or PDF" handles both, but is metered.

# --- Compose: ExtractedTextLength ---
@{length(trim(coalesce(body('Convert_file_to_text'), '')))}

# --- Condition: is this a text-layer PDF? ---
@greater(int(outputs('Compose_ExtractedTextLength')), 50)

#   TRUE  -> Set variable varSourceText = body('Convert_file_to_text')
#            Set variable varSourcePath = 'text-layer'
#   FALSE -> Run OCR action (AI Builder / Document Intelligence / LLM-with-vision)
#            Set variable varSourceText = body('OCR')?['content']
#            Set variable varSourcePath = 'ocr'
#            Set variable varOcrPageCount = length(body('OCR')?['pages'])   # for cost tracking

# --- Guard: OCR produced nothing usable ---
@less(length(trim(variables('varSourceText'))), 120)
#   TRUE  -> straight to CorrespondenceExceptions, reason 'unreadable_source',
#            original attached, NO register entry, officer SLA 4 h.
#            Roughly 2% of scans land here. That is expected, not a defect.

# --- Normalisation for MATCHING ONLY. The original is stored byte-exact. ---
# Alef variants -> bare alef; strip tashkeel; collapse whitespace.
@{trim(replace(replace(replace(replace(variables('varSourceText'),
    'أ','ا'), 'إ','ا'), 'آ','ا'), '  ', ' '))}
```

### The extraction prompt bound to the schema

```text
# injaz/prompts/extract_correspondence.md
# Extraction prompt. The schema in injaz/schemas/correspondence_extract.schema.json
# is pasted verbatim into the OUTPUT SCHEMA block below — keep them identical.
# Model temperature: 0. Max output tokens: 900.

SYSTEM
You extract register fields from an official letter received by a Saudi government
agency. You are a transcription assistant, not a decision-maker. An officer confirms
every record you produce before it becomes an official register entry.

HARD RULES
1. Extract only what is present in the letter text. Never infer, complete, or guess.
2. If a field is illegible, obscured by a stamp, or absent, return null for it AND add
   its name to "fields_uncertain". A null is always better than a plausible invention.
3. Reference numbers are transcribed EXACTLY as printed, including slashes and Arabic
   letters (e.g. "2026/م/4471"). Do not reformat, reorder, or convert digits.
4. Dates: if the letter shows a Hijri date, put it in letter_date_hijri as YYYY/MM/DD and
   convert to Gregorian in letter_date_gregorian. If only one calendar is shown, leave
   the other null. Never invent the second date.
5. summary_ar must use the letter's own phrasing where possible, must be <= 400 characters,
   and must not mention any entity, person, amount or deadline that is not in the letter.
   summary_en is a faithful translation of summary_ar, not a separate summary.
6. suggested_owner is a SUGGESTION only. Use "Unassigned" whenever the letter does not
   clearly belong to one department. The department head confirms ownership; you do not
   assign work to anyone.
7. extraction_confidence is your honest confidence that every non-null field is correct.
   Below 0.70 the record will be routed to a human queue, which is a correct outcome.

OUTPUT SCHEMA (return one JSON object matching this exactly, no prose, no markdown fence)
{{ contents of injaz/schemas/correspondence_extract.schema.json }}

USER
Language of letter: {{ detected_language }}
Source path: {{ varSourcePath }}          # 'text-layer' or 'ocr' — OCR text may contain errors
--- LETTER TEXT BEGINS ---
{{ varSourceText }}
--- LETTER TEXT ENDS ---
```

### Parse JSON and the threshold gate in the flow

```json
// injaz/flows/correspondence-triage/parse-and-gate.json
// The two actions that turn model output into routable flow data.
// Parse JSON schema MUST be the canonical schema file, not a sample-generated one.
{
  "Parse_extraction": {
    "type": "ParseJson",
    "runAfter": { "Extract_fields": ["Succeeded"] },
    "inputs": {
      "content": "@body('Extract_fields')?['text']",
      "schema": "@{json(outputs('Get_schema_file')?['body'])}"
    },
    "runtimeConfiguration": { "secureData": { "properties": ["inputs", "outputs"] } }
  },

  "Gate_auto_register": {
    "type": "If",
    "runAfter": { "Parse_extraction": ["Succeeded"] },
    "expression": {
      "and": [
        { "not": { "equals": ["@body('Parse_classification')?['label']", "uncertain"] } },
        { "greaterOrEquals": ["@body('Parse_classification')?['confidence']", 0.75] },
        { "greaterOrEquals": ["@body('Parse_extraction')?['extraction_confidence']", 0.70] }
      ]
    },
    "actions": {
      "Branch_on_completeness": {
        "type": "If",
        "expression": { "equals": ["@length(body('Parse_extraction')?['fields_uncertain'])", 0] },
        "actions":  { "Create_register_entry_confirmed": { "type": "OpenApiConnection" } },
        "else": { "actions": { "Create_register_entry_draft": { "type": "OpenApiConnection" } } }
      }
    },
    "else": {
      "actions": {
        "Queue_exception": {
          "type": "OpenApiConnection",
          "inputs": {
            "host": { "connectionName": "shared_sharepointonline", "operationId": "PostItem" },
            "parameters": {
              "table": "CorrespondenceExceptions",
              "item/Title": "@triggerOutputs()?['body/subject']",
              "item/Reason": "@concat('label=', body('Parse_classification')?['label'],
                              ' conf=', string(body('Parse_classification')?['confidence']),
                              ' extconf=', string(body('Parse_extraction')?['extraction_confidence']))",
              "item/SourcePath": "@variables('varSourcePath')",
              "item/AssignedTo/Claims": "correspondence.duty@agency.gov.sa",
              "item/DueBy": "@addHours(utcNow(), 4)"
            }
          }
        }
      }
    }
  }
}
```

### Parse JSON failure handling — the action that fails most often

```text
# injaz/flows/correspondence-triage/parse-failure-handling.txt
# Parse JSON is the most failure-prone action in any AI flow. Three causes, three fixes.

# CAUSE 1: the model wrapped its JSON in a markdown fence (```json ... ```)
# FIX: strip fences before parsing. Compose action, input:
@{if(
   startsWith(trim(body('Extract_fields')?['text']), '```'),
   trim(replace(replace(trim(body('Extract_fields')?['text']), '```json', ''), '```', '')),
   trim(body('Extract_fields')?['text'])
)}

# CAUSE 2: a required property is missing (model omitted fields_uncertain)
# FIX: do not relax the schema. Configure run-after on a repair branch:
#   Parse_extraction  runAfter: Extract_fields [Succeeded]
#   Retry_extraction  runAfter: Parse_extraction [Failed]   <- one retry with a stricter
#                     reminder appended: "You omitted required fields. Return ALL of:
#                     reference_number, sender_entity, subject_ar, ... fields_uncertain."
#   Queue_exception   runAfter: Retry_extraction [Failed]   <- second failure = human queue

# CAUSE 3: additionalProperties:false rejected a helpful extra field
# FIX: keep additionalProperties:false. The rejection is the schema doing its job.
#      Tighten the prompt's OUTPUT SCHEMA block instead of loosening the contract.

# Observed rates over 1,200 letters/month after tuning:
#   Parse succeeded first attempt : 1,163  (96.9%)
#   Repaired on retry             :    29  ( 2.4%)
#   Queued to human               :     8  ( 0.7%)
```

## Hands-on Lab 3 — Build the Injaz Correspondence Triage Flow

| | |
|---|---|
| **Objective** | Build an end-to-end triage flow: letter arrives → triage text-layer vs scan → OCR if needed → classify with a closed label set → extract to a JSON schema → gate on confidence → create a register entry or an exception; then measure classification accuracy on the 200-letter gold set and claim the 180 h/month saving |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab3_Start_1_0_0_1.zip` (creates `CorrespondenceRegister`, `CorrespondenceExceptions`, the shared mailbox rule and the prompt/schema library). Gold set `injaz_letters_gold_200/` on the shared drive. Premium path uses AI Builder; **standard-connector path** uses the pre-OCR'd text sidecar files supplied for all 200 letters. |

**Instructions & tasks**

1. *(7 min)* Build the triage step: `Get file content` → convert to text → measure length → branch. Run letters `L-0007` (text-layer) and `L-0041` (scanned, stamped) and confirm they take different paths. The starter has no triage; observe first that `L-0041` extracts an empty string and reports success.
2. *(9 min)* Wire the classification call using `classify_correspondence.md`. Add the `uncertain` label the starter omits, and add the confidence field. Run the 12-letter smoke set and record the labels.
3. *(11 min)* Wire extraction with `extract_correspondence.md` and the canonical schema. Fix the starter's Parse JSON, which was generated from a sample and lacks `fields_uncertain`. Run `L-0041` (stamped reference) and confirm `reference_number` comes back **null** with `"reference_number"` in `fields_uncertain` — not an invented number.
4. *(9 min)* Build the three-way gate: auto-register, draft-with-gaps, exception. Enforce the thresholds **in the flow**, not only the prompt — the starter trusts the prompt. Prove it by feeding `L-0113`, whose model output carries `confidence: 0.41` with a confident-looking label.
5. *(10 min)* Run the full 200-letter gold set. Fill the benchmark table: top-label accuracy, `uncertain` rate, exception rate, field-level accuracy for `reference_number` and `sender_entity`. Compare Arabic vs English and text-layer vs OCR subsets.
6. *(4 min)* Record in the register: `feat(correspondence): triage + classify + schema extract, 180 h/month, 92.5% accuracy`.

**Expected output**
```text
=== Gold set run: 200 letters (140 ar / 60 en; 140 text-layer / 60 scanned) ===
Routing
  auto-registered (confirmed)   161   80.5%
  registered as draft (gaps)     24   12.0%
  exception queue                15    7.5%   <- target <= 8%

Classification (against 200 human-assigned gold labels)
  top-label accuracy            92.5%   (185/200)   <- target >= 92%
  accuracy, text-layer subset   96.4%   (135/140)
  accuracy, OCR subset          83.3%   (50/60)     <- the honest number
  uncertain rate                 7.0%   (14/200)    <- target <= 8%
  confident-wrong (conf>=0.75)   1.5%   (3/200)     <- the number that matters most

Field-level extraction accuracy
  reference_number   91.0%  correct | 6.5% null+flagged | 2.5% wrong   <- 0 invented on nulls
  sender_entity      97.5%
  letter_date_hijri  94.0%
  subject_ar         96.0%  (exact-match after NFKC normalisation of the comparison copy)

Parse JSON
  first attempt 194 | repaired on retry 5 | queued 1

=== Benefit claimed ===
Correspondence triage: 1,200 letters/month × (12 min -> 3 min) = 180 h/month, 2,160 h/year
Acknowledgement time: 26 working hours -> 8 minutes
Cycle time (arrival -> owner assigned with due date): 3.2 days -> 0.4 days
```

**Acceptance criteria**
- Triage routes text-layer and scanned documents down different paths; an unreadable scan reaches the exception queue with the original attached and no register entry.
- The label set includes `uncertain`; the flow re-checks both confidence thresholds independently of the prompt.
- `L-0041` produces `reference_number: null` with the field named in `fields_uncertain`; no invented reference number appears anywhere in the run.
- Gold-set accuracy ≥ 92% overall with the OCR subset reported separately and honestly; exception rate ≤ 8%.
- The stored `subject_ar` matches the original letter byte-exactly; normalisation appears only on the matching copy.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Scanned letters extract as empty and the run is green | No triage step | Add the length test; route < 50 characters to OCR |
| Parse JSON fails "required property missing" | Schema generated from a sample output | Point Parse JSON at the canonical schema file |
| Model returns a fenced code block | Chat-style formatting habit | Strip fences in a Compose before Parse JSON |
| Reference numbers appear that are not on the letter | `reference_number` non-nullable in the schema | Make it nullable; require it in `fields_uncertain` when null |
| Register search cannot find a letter by its subject | Arabic normalised before storage | Store the original; normalise only the matching copy |
| Everything auto-registers, including confidence 0.4 | Threshold enforced only in the prompt | Re-check both thresholds in the flow's gate condition |
| "AI Builder is not available in this environment" | Premium/region licensing | Use the supplied OCR sidecar text files; the rest of the lab is unchanged |

**Instructor notes.** Task 3 is the module's thesis in one action: watch faces when a stamped letter returns `null` and someone says "but it should have got that". Ask what the alternative is, and let the room arrive at *an invented reference number in a legal register* on its own. Second watch-point: several participants will report the headline 92.5% and hide the 83.3% OCR figure. Insist both appear. The single most valuable professional habit this course can install is reporting the subset where the system is weakest. Fast finishers: compute a confusion matrix for the eight labels and identify which pair the model conflates most (it is `official_directive` vs `information_request`) then propose one prompt sentence to separate them — that edit typically buys 1.5 points of accuracy.

## Mini Exercises

**Quiz (5 questions)**
1. How do you detect a scanned PDF before processing it? → extract text and measure length; under ~50 characters on page 1 means it is a scan.
2. Why must `uncertain` be in the label set? → it keeps ambiguous cases with a human instead of forcing a confident wrong answer.
3. Why is a nullable `reference_number` safer than a required one? → a required field forces invention; null plus a flag routes it to a human.
4. Where must a confidence threshold be enforced? → in the flow's gate, not only in the prompt.
5. What is the danger of storing normalised Arabic in the register? → the stored record no longer matches the letter it cites.

**Debugging exercise.** Provide a run where 14 letters carry sequential-looking reference numbers `2026/م/1001` to `2026/م/1014` that do not exist. Participants must trace it to a non-nullable schema field on a batch of stamped scans and explain why nothing in the run history looked wrong.

**Design exercise.** The agency adds a ninth letter type: `judicial_correspondence`, with a statutory 5-day response obligation. Specify every artefact that must change (label set, prompt, schema enum, SLA table, gold set) and state how you would prove the change did not degrade the other eight labels.

**Discussion questions.**
- Your classifier is 92.5% accurate overall but 83.3% on scans. A director asks for "the accuracy number" for a board slide. What do you put on the slide, and what do you say?
- Should the exception queue depth appear on the same dashboard as the hours saved? Argue both sides, then decide.

## Case Study — The Register That Filled With Fiction at "Mirsal" (مرسال)

**Scenario.** "Mirsal" (مرسال), the official correspondence platform of a Saudi ministry in Jeddah, automated register entry for 3,400 incoming letters a month. Nine months later, an internal audit sampled 120 register entries against their source letters and found 31 with a reference number that did not appear anywhere on the letter.

**Business context.** The correspondence register is the ministry's authoritative record of what it was asked to do and when. Reference numbers are how a letter is cited in later correspondence, in escalations, and in responses to oversight bodies. Thirty-one wrong references in a 120 sample implies roughly 800 defective entries.

**Technical challenge.** The extraction schema marked `reference_number` as a required string with no null permitted. On scanned letters where a stamp overlaid the reference, the model produced a well-formed, plausible, entirely fabricated number in the correct format. Because the format was correct, no validation rule fired, and because the register was the only record, nothing downstream contradicted it.

**Constraints.** The register cannot be bulk-corrected without a records-management decision — amending an official register has its own procedure. Some defective entries have already been cited in outgoing letters to other entities. The platform serves eleven directorates and cannot be paused. The team must present a remediation plan to the ministry's records committee in three weeks.

**Solution approach (facilitate, don't lecture).** Guide toward: (1) stop the bleeding — make the field nullable, add `fields_uncertain`, and gate anything with a null critical field into a human queue, deployed within days; (2) quantify the damage by re-running all nine months of source documents through the corrected extractor and diffing against the register, producing an exact defect list rather than an estimate; (3) treat correction as a records process with the records officer, not an IT bulk update, and preserve the original erroneous entry with an annotation rather than overwriting it; (4) address the citations already sent, which is a correspondence problem, not a technical one; (5) institute a monthly gold-set audit so the next drift is caught in weeks. The deeper lesson the room should reach: the model behaved exactly as instructed, and the defect was designed in by a schema author who thought a required field meant a reliable one.

**Discussion questions.**
1. Nothing in the run history looked wrong for nine months. What monitoring would have caught this in week two, and why is run success rate useless here?
2. The model produced a correctly formatted fabrication. What does that tell you about format validation as a quality control?
3. Who is accountable for the 800 defective entries — the schema author, the flow owner, the records officer, or the director who approved go-live? Defend your answer.
4. Overwriting the wrong entries would make the register look clean. Why is that the wrong remediation, and what is the right one?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Classification accuracy (top label) | Quality | ≥ 92% overall; OCR subset reported separately | 200-letter gold set |
| Confident-wrong rate | Quality | ≤ 2% (label wrong with confidence ≥ 0.75) | gold-set comparison |
| `uncertain` / exception rate | Quality | 3–8% | routing counts |
| Invented values on obscured fields | Correctness | 0 | manual audit of all null-eligible fields |
| Hours saved per month (triage) | Benefit | 180 h/month (2,160 h/year) | 1,200 letters × (12 → 3 min) |
| Acknowledgement time | Benefit | 26 working hours → ≤ 15 minutes | register timestamps |

**Example benchmark table (filled during lab):**

| Subset | Letters | Top-label accuracy | Uncertain rate | Ref-number accuracy | Exception rate |
|---|---|---|---|---|---|
| All | 200 | 92.5% | 7.0% | 91.0% | 7.5% |
| Arabic, text-layer | 100 | 96.0% | 4.0% | 97.0% | 3.0% |
| English, text-layer | 40 | 97.5% | 2.5% | 98.0% | 2.5% |
| Arabic, scanned (OCR) | 50 | 84.0% | 12.0% | 80.0% | 14.0% |
| Arabic, scanned + stamped | 10 | 80.0% | 20.0% | 60.0% (6 nulls, 0 invented) | 30.0% |

## Required Visuals and Training Assets

### Diagrams
1. **The document triage fork** — *Purpose:* the first design decision of any document flow. *Elements:* one inbound letter splitting into a text-layer path and an OCR path, rejoining at a common `varSourceText`, with a third exit to the exception queue for unreadable scans. *Style:* single fork-and-merge, with the character-count test annotated on the branch.
2. **Three-way confidence gate** — *Purpose:* make thresholds concrete. *Elements:* a funnel splitting 200 letters into 161 auto-registered, 24 draft-with-gaps, 15 exceptions, with the exact conditions on each path and the percentage on each arm. *Style:* proportional funnel with real numbers, reused in Module 8's dashboard.
3. **Anatomy of a Saudi official letter** — *Purpose:* teach participants where each extracted field physically lives. *Elements:* a redacted synthetic Arabic letter with callouts to reference number, Hijri and Gregorian dates, sender entity, subject line, body, requested action, signature block and stamp; the stamp deliberately overlapping the reference number. *Style:* annotated document scan, RTL layout preserved. *Designer description:* "A full-page synthetic letter in Arabic with eight numbered callout bubbles; callout 1 (reference number) is partly covered by a circular stamp and carries a red 'this is why the field is nullable' note."
4. **Schema as a contract** — *Purpose:* connect the schema file, the prompt, and the Parse JSON action. *Elements:* one schema document with two arrows — one into the prompt's OUTPUT SCHEMA block, one into the Parse JSON action — and a red X on a third arrow from a "sample output" box. *Style:* three-node diagram with the anti-pattern struck through.

### Images (screenshots)
1. **`fields_uncertain` populated on a stamped letter** — *why:* this is the behaviour the whole module argues for; *content:* the run output showing `reference_number: null` and the array containing it, next to the source scan.
2. **The exception queue with an SLA clock** — *why:* proves the queue is worked, not a landfill; *content:* `CorrespondenceExceptions` with due-by times, assigned officer, and the original attached.
3. **A Parse JSON failure and its repair branch** — *why:* the most common runtime failure in AI flows; *content:* the failed action, the run-after configuration, and the successful retry.

### Simulations
1. **The invented reference number** — *Setup:* branch `sim-nonnull-schema` with `reference_number` required; run 20 stamped scans. *Expected behaviour:* 20 well-formed, entirely fabricated references, and a completely green run history. *Learning objective:* required does not mean reliable; format validation catches nothing.
2. **Threshold bypass** — *Setup:* thresholds stated in the prompt but not enforced in the flow; feed letters with self-reported confidence between 0.3 and 0.6. *Expected behaviour:* all auto-register. *Learning objective:* the model advises, the flow enforces.

### Interactive Activities
- **Label the letters (15 min):** each table receives ten printed synthetic letters and the eight-label set, and assigns labels independently. Inter-rater disagreement among humans is typically 10–15%, which reframes the model's 92.5% honestly and productively.
- **Write the `uncertain` rule (12 min):** teams draft the single prompt sentence that makes `uncertain` attractive to a helpful model, then test their sentences against three ambiguous letters and compare which wording actually raises the uncertain rate.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_letters_gold_200/` | Synthetic Saudi official letters with human gold labels and gold field values | PDF + JSON labels | 200 letters (140 ar / 60 en; 60 scanned; 10 stamped) | Accuracy measurement; the module's evidence base |
| `injaz_letters_ocr_sidecar/` | Pre-OCR'd text for all 200 letters | TXT | 200 files | Standard-connector fallback when AI Builder is unavailable |
| `correspondence_extract.schema.json` | Canonical schema | JSON | 1 file | Bound to both the prompt and Parse JSON |
| `label_set_v3.md` | The eight-label taxonomy with definitions and boundary cases | MD | 2 pages | Prompt source and human labelling guide |

### Demo Requirements
- **Instructor demo (8 minutes):** project a scanned Arabic letter with a stamp across the reference number. Run it through a schema with `reference_number` required and show the confident fabrication. Change one word in the schema — `"string"` to `["string","null"]` — re-run, and show the null with the field flagged. One-word change, entirely different system. Close by asking which version you would want in a register that an oversight body will read.

---

# Module 4 — Drafting and Communication: Grounded Bilingual Drafting with a Human Approval Gate

## المحور الرابع — الصياغة المستندة إلى مصادر معتمدة وبوابة الاعتماد البشري

## Module Overview

**Purpose.** Injaz's contact unit answers 1,600 citizen enquiries a month. The answers already exist — in the approved services catalogue, the published fee schedule, the FAQ approved by the legal directorate. The work is finding the right approved answer and rendering it in correct formal Arabic. This module teaches **grounded drafting**: retrieve the approved source first, generate only from it, cite it, and put the draft in front of an officer who signs. It saves **160 hours a month** and it is the module where the human-approval gate stops being a slogan and becomes a flow action.

**Business relevance.** An ungrounded model answering a citizen enquiry about a fee will produce a fluent, well-formatted, confidently wrong number, and the agency will be held to it. Grounding is not a quality improvement; it is the difference between an automation a legal directorate can approve and one it must forbid. Every Saudi entity building citizen-facing AI is on one side of this line.

**Industry use cases.**
- A services authority drafts replies to fee and eligibility enquiries strictly from the published catalogue, with the source article cited in the officer's review pane so verification takes eight seconds.
- A ministry's communications office drafts bilingual acknowledgements to inter-entity correspondence in the correct formal register, with dual Hijri/Gregorian dating, and the director signs.
- A municipality routes any enquiry whose answer is not in the approved knowledge base straight to a subject-matter officer rather than letting the model improvise — and reports that refusal rate as a knowledge-base coverage gap, not a failure.

**Expected competencies.** After this module a participant can build an approved knowledge base with citable units; retrieve before generating; write a drafting prompt that refuses when unsupported; produce parallel Arabic and English text in correct official register with dual dating; design an approval gate that captures who approved what and when; and measure first-pass approval rate and edit distance.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Build an approved knowledge base of citable answer units with owners and review dates | LO5, CO1 |
| 4.2 | Retrieve before generating and constrain the draft to retrieved sources only | LO5, CO3 |
| 4.3 | Require citation of the source unit and refusal when no source supports an answer | LO5, LO7, CO3 |
| 4.4 | Produce bilingual output in correct formal Arabic register with dual Hijri/Gregorian dating | LO5, CO1 |
| 4.5 | Implement an approval gate that records the approving officer, the version approved, and any edits | LO5, LO7, CO4 |
| 4.6 | Measure first-pass approval rate, edit rate, and knowledge-base coverage | LO5, LO8, CO2 |

## Technical Content

### 1. Grounded versus ungrounded, demonstrated not asserted

Ask a model, with no sources, what the fee is for a particular municipal service. It will answer. It will give a number in SAR, formatted correctly, with a confident sentence around it. That number is a guess shaped like a fact. Now supply the approved fee schedule and require the answer to quote it. The model becomes a very fast, very literate clerk that finds the right paragraph — which is exactly the job.

| Property | Ungrounded generation | Grounded generation |
|---|---|---|
| Source of the answer | Model's training data and inference | A retrieved, approved, versioned document unit |
| Verifiability | None — nothing to check against | The citation; a reviewer checks in seconds |
| Behaviour when it does not know | Produces a plausible answer | Refuses and routes to a human |
| Failure mode | Confident fabrication reaching a citizen | Refusal rate rises — visible, measurable, fixable |
| Legal defensibility | Indefensible | The agency's own approved text, quoted |
| What "improving it" means | Better prompt wording | Better knowledge base |

The last row is the strategic point for this cohort. In a grounded system, **the way you improve answer quality is by improving the approved knowledge base**, which is a content-governance activity that administrative staff can own — not a machine-learning activity requiring engineers.

### 2. The approved knowledge base: units, owners, review dates

A knowledge base for grounded drafting is not a folder of policy PDFs. It is a list of **answer units**, each small enough to be quoted, each with an identifier that can be cited, an owner who is accountable for its correctness, and a review date after which it is treated as stale.

```text
# injaz/registers/ApprovedKnowledgeBase — SharePoint list definition
UnitId              Single line of text   KB-SVC-0142   <- cited verbatim in every draft
TitleAr             Single line of text   رسوم إصدار الرخصة التجارية
TitleEn             Single line of text   Commercial licence issuance fee
BodyAr              Multiple lines        The approved Arabic text, quotable verbatim
BodyEn              Multiple lines        The approved English text
ServiceCode         Choice                links the unit to a service in the catalogue
EnquiryLabels       Multi-choice          fees | eligibility | documents | timelines |
                                          status | complaint | appointment | other
ApprovedBy          Person or Group       the accountable content owner (NOT the flow builder)
ApprovedOn          Date
ReviewDueOn         Date                  ApprovedOn + 365 days
Status              Choice                Active | UnderReview | Retired
Version             Number                incremented on every text change
LegalReference      Single line of text   the regulation or decision the unit rests on

# Retrieval filter used by the flow (standard connector, no vector database required):
Status eq 'Active'
  and ReviewDueOn ge '@{utcNow()}'
  and EnquiryLabels/Id eq @{outputs('Compose_LabelId')}
  and ServiceCode eq '@{body('Parse_classification')?['service_code']}'

# Coverage metric — the number that drives knowledge-base investment:
#   coverage = 1 - (enquiries where retrieval returned 0 units / total enquiries)
#   Injaz baseline 71%  ->  after two KB sprints  91%  ->  target 95%
```

For a foundation cohort, keyword-and-metadata retrieval over a well-labelled SharePoint list is the right teaching choice: it is transparent, debuggable by a non-developer, needs no premium licence, and makes the coverage gap visible as an empty result set rather than as a subtly irrelevant vector match.

### 3. The refusal rule

A grounded drafting prompt must contain an explicit, unmissable refusal instruction, and the flow must handle refusal as a normal outcome rather than an error. Injaz's rule: **if retrieval returns zero active units, the model is never called at all** — the enquiry goes straight to a subject-matter officer with a note that no approved answer exists. This is cheaper, faster, and removes the temptation entirely.

When retrieval returns units but they do not cover the specific question, the model must say so. The prompt makes refusal safe and the schema makes it structured, so the flow can route it.

### 4. Formal Arabic register and dual dating

Official Saudi correspondence has a register that a fluent Arabic speaker recognises instantly and that a general-purpose model does not produce by default. Teach the specifics:

- **Opening and closing formulas** are conventional, not creative: `السلام عليكم ورحمة الله وبركاته` opening; `وتفضلوا بقبول فائق التحية والتقدير` closing. The model must be given them, not asked to invent them.
- **Address the entity, not the individual**, in inter-entity correspondence: `سعادة مدير عام ...` with the correct honorific for the grade.
- **Dual dating**: Hijri first, Gregorian in parentheses — `١٤٤٧/١١/٢٥هـ الموافق ٢٠٢٦/٠٥/١٧م`. Both must be present and must actually correspond; a mismatched pair is the most common and most embarrassing defect.
- **No contractions, no colloquialism, no first-person singular.** The agency writes, not the officer.
- **English is a parallel text, not a translation of convenience.** Where the two must agree — an amount, a date, a deadline — the flow computes the value once and inserts it into both, rather than letting the model render it twice.

### 5. The approval gate

The gate is where accountability is created. Four requirements, all non-negotiable in a government context:

1. **The draft is never sent by the flow.** The flow sends the draft *to an officer*. The officer's approval action is what triggers sending.
2. **The approval record captures identity, time, and exact content.** Who approved, when, and a hash or stored copy of the precise text approved — because "I approved a different version" is the argument that follows every incident.
3. **Edits are captured, not discarded.** When an officer changes the draft before approving, the delta is the most valuable training signal the agency has for improving the knowledge base and the prompt.
4. **Rejection is a first-class outcome with a reason code.** `wrong_source`, `wrong_register`, `incomplete`, `not_applicable`, `tone`. Reason codes turn complaints into a prioritised backlog.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Retrieve, then generate. Never generate, then look for support.*
- *No sources, no model call.* Route to a human before spending a token.
- *Every factual sentence carries a `UnitId`.* If it cannot be cited, it must not be written.
- *The officer signs, the bot drafts.* Say it in the approval card text so the officer reads it every time.
- *Compute shared values once.* Amounts and dates are inserted, not generated twice.
- *Refusal rate is a knowledge-base metric, not a model failure.*

**Common mistakes (each is planted in the Lab 4 starter)**
1. The prompt supplies the enquiry but not the retrieved units, so the model answers from memory and cites a `UnitId` that does not exist.
2. The flow calls the model even when retrieval returns zero units.
3. The approval action is `Send an email` with the officer merely copied — no gate at all, just a witness.
4. The Hijri and Gregorian dates are both generated by the model and do not correspond.
5. Officer edits are discarded: the flow sends the *original* draft after approval rather than the edited text.
6. Retired knowledge-base units are retrieved because the filter omits `Status eq 'Active'`.

**Production considerations**
- Store the approved text with the case, not just a pointer. Knowledge-base units change; the record must show what was actually sent.
- Put the citation in the *officer's* view, never in the citizen's reply. Internal provenance, external plain language.
- Track knowledge-base staleness: units past `ReviewDueOn` should stop being retrieved automatically, which converts a silent risk into a visible coverage gap.
- Measure first-pass approval rate weekly. A sustained fall is the earliest signal that the knowledge base has drifted from reality.

### 7. Real-world example walkthrough

Narrate in five minutes. A services authority piloted AI-drafted replies to citizen enquiries with a strict rule: officers must review before sending. Within three weeks first-pass approval was 88% and the pilot was declared a success. A supervisor then sampled 40 approved-and-sent replies against the source policy. Six contained a fee figure that was correct in the previous year's schedule and wrong in the current one — the model had answered from training data, and the officers, reviewing dozens of fluent drafts an hour, had approved them. The gate existed and had failed, because a human reviewing an unsourced fluent draft is not a control; they are a rubber stamp with a job title. The fix was to ground the drafting in the current schedule and put the cited article *next to* the draft in the review pane. First-pass approval fell to 79% — and the six errors became zero, because the officer was now checking a quotation against a source rather than assessing plausibility. The lesson: **a human gate over ungrounded output is theatre. Grounding is what makes the gate a control.**

## Code Examples

### The grounded bilingual drafting prompt

```text
# injaz/prompts/draft_enquiry_reply.md
# Grounded drafting. Called ONLY when retrieval returned >= 1 active knowledge-base unit.
# Model temperature: 0.2. The officer approves; this prompt never sends anything.

SYSTEM
You draft replies to citizen enquiries on behalf of a Saudi government agency. An officer
reviews, edits if needed, and signs every reply. You never send anything to anyone.

GROUNDING RULES — these override every other instruction
1. Every factual statement in your draft MUST come from the APPROVED SOURCES below and
   MUST carry the UnitId it came from, in the citations array.
2. If the sources do not answer the enquiry, or answer only part of it, set
   "sufficient": false and explain precisely what is missing in "gap_note".
   Refusal is a correct, valued outcome. Do not fill a gap with general knowledge.
3. Never state a fee, a duration, a deadline, an eligibility condition or a document
   requirement that is not written verbatim in the sources.
4. Never cite a UnitId that is not in the sources supplied. Inventing a citation is the
   most serious error you can make.

DRAFTING RULES — formal Saudi official register
5. Arabic is the primary text. Open with: السلام عليكم ورحمة الله وبركاته
   Close with:  وتفضلوا بقبول فائق التحية والتقدير
6. Write in the third person on behalf of the agency. No first-person singular, no
   colloquial forms, no contractions, no exclamation marks, no emoji.
7. English is a parallel text of equal standing, not a loose translation.
8. Do NOT write any date, amount or reference number yourself. Use these placeholders
   exactly and the flow will substitute them:  {{HIJRI_DATE}}  {{GREGORIAN_DATE}}
   {{CASE_REFERENCE}}  {{OFFICER_NAME}}   (this prevents mismatched dual dates)
9. Do not include citations in the body text. They go in the citations array only —
   the officer sees them, the citizen does not.

OUTPUT — one JSON object, no prose, no markdown fence:
{ "sufficient": true|false,
  "gap_note": "<empty when sufficient>",
  "body_ar": "<the full Arabic reply, with placeholders>",
  "body_en": "<the full English parallel text, with placeholders>",
  "citations": [{ "unit_id": "KB-SVC-0142", "quote_ar": "<=30 words, verbatim" }],
  "draft_confidence": <0..1> }

USER
ENQUIRY (as received, language {{enquiry_language}}):
{{enquiry_text}}

APPROVED SOURCES (the only permitted basis for any factual statement):
{{#each retrieved_units}}
[{{UnitId}}] v{{Version}} — {{TitleAr}} / {{TitleEn}}
AR: {{BodyAr}}
EN: {{BodyEn}}
{{/each}}
```

### Dual dating and placeholder substitution in the flow

```text
# injaz/flows/enquiry-reply/date-and-placeholder-substitution.txt
# The model NEVER writes dates. The flow computes them once and substitutes into both
# language versions, so the Hijri and Gregorian dates cannot disagree.

# --- Gregorian, Arabic-locale numerals, Riyadh time ---
@{formatDateTime(convertFromUtc(utcNow(), 'Arab Standard Time'), 'yyyy/MM/dd')}
# -> 2026/05/17

# --- Hijri: read from the maintained HijriCalendar list, not computed in an expression ---
#     (Hijri conversion in a low-code expression is unreliable across month boundaries;
#      a maintained lookup list is boring, correct, and auditable.)
# Get items: HijriCalendar, Filter Query:
GregorianDate eq '@{formatDateTime(convertFromUtc(utcNow(),'Arab Standard Time'),'yyyy-MM-dd')}'
# -> first(body('Get_hijri'))?['HijriDate']  =  1447/11/25

# --- Substitution: one Compose per language, chained replaces ---
@{replace(replace(replace(replace(
    body('Parse_draft')?['body_ar'],
    '{{HIJRI_DATE}}',     concat(first(body('Get_hijri'))?['HijriDate'], 'هـ')),
    '{{GREGORIAN_DATE}}', concat(formatDateTime(convertFromUtc(utcNow(),'Arab Standard Time'),'yyyy/MM/dd'), 'م')),
    '{{CASE_REFERENCE}}', outputs('Compose_CaseReference')),
    '{{OFFICER_NAME}}',   outputs('Get_assigned_officer')?['body/DisplayName'])}

# --- Verification guard: no placeholder may survive into an approved reply ---
@and(
  not(contains(outputs('Compose_BodyAr'), '{{')),
  not(contains(outputs('Compose_BodyEn'), '{{'))
)
# false -> do not present to the officer; write FlowFailures row; notify owner.
#          A leaked "{{HIJRI_DATE}}" in a citizen reply is a visible, humiliating defect.

# --- Rendered heading, as it appears in the approved reply ---
#   التاريخ: ١٤٤٧/١١/٢٥هـ الموافق ٢٠٢٦/٠٥/١٧م
#   الإشارة: ENQ-2026-004718
```

### The approval gate with edit capture and reason codes

```json
// injaz/flows/enquiry-reply/approval-gate.json
// The officer approves; the flow sends. Edits and rejections are both captured.
{
  "Start_officer_approval": {
    "type": "OpenApiConnection",
    "runAfter": { "Verify_no_placeholders": ["Succeeded"] },
    "inputs": {
      "host": { "connectionName": "shared_approvals", "operationId": "StartAndWaitForAnApproval" },
      "parameters": {
        "approvalType": "Custom Responses - Wait for one response",
        "ApprovalCreationInput/title": "@concat('Draft reply — ', outputs('Compose_CaseReference'))",
        "ApprovalCreationInput/assignedTo": "@outputs('Get_assigned_officer')?['body/Mail']",
        "ApprovalCreationInput/responseOptions": "Approve as drafted,Approve with my edits,Reject — wrong source,Reject — wrong register,Reject — incomplete,Reject — not applicable",
        "ApprovalCreationInput/details": "@concat(
            '**You are the signing officer. This reply has NOT been sent and will not be sent unless you approve it.**\n\n',
            '### Draft (AR)\n', outputs('Compose_BodyAr'), '\n\n',
            '### Draft (EN)\n', outputs('Compose_BodyEn'), '\n\n',
            '### Sources this draft is based on — verify before approving\n',
            join(body('Select_citation_lines'), '\n'), '\n\n',
            '### Original enquiry\n', triggerOutputs()?['body/enquiryText'])",
        "ApprovalCreationInput/enableNotifications": true,
        "ApprovalCreationInput/enableReassignment": true
      }
    }
  },

  "Switch_on_officer_decision": {
    "type": "Switch",
    "runAfter": { "Start_officer_approval": ["Succeeded"] },
    "expression": "@body('Start_officer_approval')?['outcome']",
    "cases": {
      "Approve as drafted": { "case": "Approve as drafted", "actions": {
        "Record_approval_unedited": { "type": "OpenApiConnection" },
        "Send_reply_unedited":      { "type": "OpenApiConnection",
          "runAfter": { "Record_approval_unedited": ["Succeeded"] } } } },

      "Approve with my edits": { "case": "Approve with my edits", "actions": {
        "Capture_edit_delta": { "type": "OpenApiConnection", "inputs": {
          "parameters": {
            "table": "DraftEditLog",
            "item/CaseReference": "@outputs('Compose_CaseReference')",
            "item/DraftText":     "@outputs('Compose_BodyAr')",
            "item/ApprovedText":  "@body('Start_officer_approval')?['responses'][0]['comments']",
            "item/CitedUnits":    "@join(body('Parse_draft')?['citations'], ';')",
            "item/EditedBy":      "@body('Start_officer_approval')?['responses'][0]['responder']['displayName']" } } },
        "Send_reply_edited": { "type": "OpenApiConnection",
          "runAfter": { "Capture_edit_delta": ["Succeeded"] },
          "inputs": { "parameters": {
            "emailMessage/Body": "@body('Start_officer_approval')?['responses'][0]['comments']" } } } } }
    },
    "default": { "actions": {
      "Record_rejection_with_reason": { "type": "OpenApiConnection", "inputs": { "parameters": {
        "table": "DraftRejectionLog",
        "item/ReasonCode": "@body('Start_officer_approval')?['outcome']",
        "item/CitedUnits": "@join(body('Parse_draft')?['citations'], ';')" } } },
      "Route_to_subject_officer": { "type": "OpenApiConnection",
        "runAfter": { "Record_rejection_with_reason": ["Succeeded"] } } } }
  }
}
```

## Hands-on Lab 4 — Grounded Bilingual Enquiry Reply with a Human Gate

| | |
|---|---|
| **Objective** | Build the citizen-enquiry reply flow: classify the enquiry, retrieve approved knowledge-base units, refuse when coverage is absent, draft bilingual formal text with computed dual dates, gate on an officer's approval capturing edits and reason codes, and send only on approval; then measure first-pass approval rate and coverage, and claim the 160 h/month saving |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab4_Start_1_0_0_1.zip` (creates `ApprovedKnowledgeBase` with 84 units, `HijriCalendar`, `DraftEditLog`, `DraftRejectionLog`, and the enquiry intake Form). Enquiry test set `injaz_enquiries_120.csv`. Standard connectors only; the LLM call uses the shared course endpoint. |

**Instructions & tasks**

1. *(8 min)* Wire retrieval: classify the enquiry into one of the eight `EnquiryLabels`, then `Get items` from `ApprovedKnowledgeBase` with the full filter. Fix the starter's filter, which omits `Status eq 'Active'` and retrieves three retired fee units. Run `ENQ-014` and confirm the retired unit no longer appears.
2. *(8 min)* Add the zero-results gate **before** the model call: if retrieval returns no units, route straight to the subject-matter officer with a coverage-gap note and never call the model. Run `ENQ-062` (an enquiry about a service not in the knowledge base) and confirm zero model calls in the run history.
3. *(10 min)* Wire the drafting prompt with the retrieved units injected. Run `ENQ-007` and verify every factual sentence carries a `UnitId` that exists in the list. Then deliberately remove the sources from the prompt, re-run, and observe the model citing `KB-SVC-0199`, which does not exist.
4. *(8 min)* Implement placeholder substitution and the Hijri lookup. Confirm the rendered heading reads `التاريخ: ١٤٤٧/١١/٢٥هـ الموافق ٢٠٢٦/٠٥/١٧م` and that the placeholder guard blocks any draft still containing `{{`.
5. *(11 min)* Build the approval gate with six response options. Approve one draft unedited, approve one with edits, and reject one as `wrong_register`. Confirm the *edited* text is what gets sent, that `DraftEditLog` captured the delta, and that the rejection wrote a reason code. Run the 120-enquiry set and fill the benchmark table.
6. *(5 min)* Record in the register: `feat(enquiry): grounded bilingual drafting + approval gate, 160 h/month, 74% first-pass`.

**Expected output**
```text
=== Enquiry test set: 120 enquiries (84 ar / 36 en) ===
Retrieval
  units retrieved, >=1        109   90.8%   <- knowledge-base coverage
  zero units, routed to SME    11    9.2%   <- coverage gap, 0 model calls made
  retired units retrieved       0            (was 3 before the Status filter fix)

Drafting (109 drafted)
  sufficient = true            97   89.0%
  sufficient = false, gap_note 12   11.0%   -> routed to SME with the gap recorded
  invented citations            0            <- the number that must be zero
  placeholder guard blocks      2            (model wrote a date despite rule 8; caught)

Officer gate (97 presented)
  approved as drafted          72   74.2%   <- first-pass approval rate, target >= 70%
  approved with edits          19   19.6%   -> deltas captured in DraftEditLog
  rejected                      6    6.2%   -> wrong_source 1, wrong_register 4, incomplete 1
  median officer review time   1 min 48 s   (was 9 min manual drafting)
  sent without approval         0            <- must be exactly 0

Top rejection reason: wrong_register (4) — all four on English-primary enquiries where the
Arabic parallel text drifted informal. Prompt rule 6 strengthened; retest next cohort.

=== Benefit claimed ===
Citizen enquiry response: 1,600/month × (9 min -> 3 min) = 160 h/month, 1,920 h/year
Cycle time (enquiry -> reply sent): 5.0 days -> 1.4 days
```

**Acceptance criteria**
- Retrieval filters on `Status eq 'Active'` and on the review date; no retired unit is ever retrieved.
- Zero knowledge-base results produce zero model calls and a routed case with a recorded coverage gap.
- Every factual statement in every draft carries a `UnitId` that exists; invented citations = 0.
- The Hijri and Gregorian dates are computed by the flow, correspond correctly, and no `{{` placeholder survives to an officer.
- Approving with edits sends the *edited* text and logs the delta; every rejection carries a reason code; nothing is ever sent without an approval outcome.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Draft cites `KB-SVC-0199`, which does not exist | Sources not injected into the prompt | Inject retrieved units; add rule 4; treat any invented citation as a blocking defect |
| A retired fee is quoted to a citizen | Retrieval filter missing `Status eq 'Active'` | Add the status and review-date filters |
| Hijri and Gregorian dates disagree | Both generated by the model | Compute in the flow; use the `HijriCalendar` lookup; substitute placeholders |
| `{{GREGORIAN_DATE}}` appears in a sent reply | Placeholder guard not wired | Add the `contains('{{')` guard before the approval action |
| Officer's edits are lost; the original is sent | Send action reads the draft, not the approval response | Send `responses[0].comments` on the "with my edits" branch |
| Approval "gate" is just a CC on the outgoing email | Send action does not depend on the approval outcome | Make the send action `runAfter` the approval switch, on approval branches only |

**Instructor notes.** Task 3's deliberate un-grounding is the demonstration the whole module rests on — do it as a room-wide moment rather than letting pairs run it privately, and read the invented `KB-SVC-0199` citation aloud. It lands harder than any slide. Watch for participants who wire the approval action but then place the send action outside the switch so it runs regardless; this is the most common and most serious lab defect, and it looks correct in the designer. Check every pair's send action's `runAfter` explicitly before they claim completion. Fast finishers: build a weekly digest of `DraftRejectionLog` grouped by reason code and `DraftEditLog` grouped by cited unit — that is the knowledge-base improvement backlog, and it is the artefact that turns this flow into a self-improving system.

## Mini Exercises

**Quiz (5 questions)**
1. What must happen when retrieval returns zero approved units? → route to a human; do not call the model at all.
2. Why does the flow, not the model, write the dates? → so Hijri and Gregorian cannot disagree, and the value is computed once for both languages.
3. Where do citations appear? → in the officer's review pane, never in the citizen's reply.
4. What makes a human approval gate a real control rather than theatre? → the officer verifies a citation against a source, instead of judging the plausibility of unsourced fluent text.
5. Is a rising refusal rate a model problem? → no — it is a knowledge-base coverage gap, and it is measurable and fixable.

**Debugging exercise.** Provide a run where 11 replies were sent with an obsolete fee. Participants must trace it to the missing `Status` filter, then answer the harder question: the officers approved all 11 — why did the gate not catch it, and what would have made it catch it?

**Design exercise.** The legal directorate demands that no reply mentioning an appeal right may be sent without a legal officer's second approval. Design the change: what detects such replies, what does the second gate look like, and what happens if the legal officer does not respond within the SLA?

**Discussion questions.**
- First-pass approval fell from 88% to 79% when grounding was introduced, while errors fell to zero. How do you present that to a director who tracks the 88%?
- If officers approve 74% of drafts unedited within 1 minute 48 seconds, are they reviewing or rubber-stamping? What evidence would settle it, and what would you change if the answer is uncomfortable?

## Case Study — The Fee That Was Never Approved at "Sada" (صدى)

**Scenario.** "Sada" (صدى), the citizen contact centre of a Saudi services authority in Riyadh, deployed AI-drafted enquiry replies with officer approval. Four months in, a citizen escalated: he had been told in writing that a service cost SAR 300 and had budgeted accordingly; the actual fee was SAR 750. The reply carried an officer's name and the authority's letterhead.

**Business context.** Sada answers 9,000 enquiries a month across 40 services. Written replies are treated by citizens — reasonably — as authoritative statements of the authority's position. The escalation reached the authority's governor's office within a week.

**Technical challenge.** The knowledge base contained the correct SAR 750 unit. It also contained a retired unit from the previous fee schedule showing SAR 300. The retrieval filter matched on service code and enquiry label but never on `Status`, so both units were retrieved, and the model — instructed to ground its answer in the sources — grounded it in the wrong one. Every rule was followed. The citation was real. The answer was wrong.

**Constraints.** Sada cannot suspend the service; enquiry volume does not pause. The authority's legal directorate must be able to state precisely how many citizens received obsolete information and about what. Retired units cannot simply be deleted, because they are the record of what the fee was during the period they applied.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) the immediate fix is one filter clause, deployable the same day; (2) the deeper fix is that the retrieval contract must include validity — status *and* effective-date range — because a fee schedule is time-bounded, not merely current or retired; (3) quantify exposure by re-running four months of enquiry logs against the corrected retrieval and diffing the cited unit, producing an exact list of affected citizens; (4) the officer gate did not fail through negligence — the draft cited a real unit and looked perfect, so the control that was missing was in retrieval, not in review; (5) add a knowledge-base health check that flags any service with more than one active unit for the same label, which is the structural smell that caused this.

**Discussion questions.**
1. The model followed every grounding rule and still produced a wrong answer. What does this say about where quality controls must sit in a grounded system?
2. Retired units cannot be deleted, because they are historical record. How do you keep them retrievable for audit but unreachable for drafting?
3. The officer approved a draft with a valid citation to a real unit. Design a change to the review pane that would have given them a fighting chance of catching it.
4. Sada must tell the governor's office how many citizens were affected. What exactly do you run, and what will you have to disclose about the limits of the estimate?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Invented citations | Correctness | 0 | every cited `UnitId` checked against the list |
| Knowledge-base coverage | Quality | ≥ 90% of enquiries retrieve ≥ 1 active unit | retrieval counts over the 120-enquiry set |
| First-pass approval rate | Quality | ≥ 70% approved as drafted | approval outcomes |
| Replies sent without approval | Governance | 0 | send-action run-after audit |
| Hours saved per month (enquiries) | Benefit | 160 h/month (1,920 h/year) | 1,600 × (9 → 3 min) |
| Cycle time (enquiry → reply) | Benefit | 5.0 days → ≤ 1.5 days | intake to send timestamps |

**Example benchmark table (filled during lab):**

| Segment | Enquiries | Coverage | Sufficient | First-pass approval | Median review time | Rejections |
|---|---|---|---|---|---|---|
| Arabic, fees | 34 | 97.1% | 94.1% | 81.3% | 1 min 21 s | 1 |
| Arabic, eligibility | 26 | 92.3% | 87.5% | 76.2% | 2 min 04 s | 1 |
| Arabic, documents | 24 | 91.7% | 90.9% | 75.0% | 1 min 46 s | 1 |
| English, mixed | 36 | 83.3% | 83.3% | 64.0% | 2 min 31 s | 3 |
| **All** | **120** | **90.8%** | **89.0%** | **74.2%** | **1 min 48 s** | **6** |

## Required Visuals and Training Assets

### Diagrams
1. **Grounded versus ungrounded, side by side** — *Purpose:* the module's opening argument. *Elements:* the same enquiry answered twice; the ungrounded reply with a fabricated SAR figure circled in red, the grounded reply with a `UnitId` badge and the quoted source beside it. *Style:* two-column comparison, red versus green, Arabic reply text shown RTL.
2. **Retrieve → draft → gate → send** — *Purpose:* the flow's shape in one image. *Elements:* four stages with the two exits drawn explicitly — zero-results exit before the model, and the rejection exit after the gate — plus a padlock on the send stage labelled "opens only on approval". *Style:* linear pipeline with two side exits.
3. **Anatomy of an approval card** — *Purpose:* show what a good gate looks like to the officer. *Elements:* the card with four zones: the accountability sentence, the bilingual draft, the cited sources with quotes, and the original enquiry; the six response options along the bottom. *Style:* annotated UI mock-up, English and Arabic.
4. **Knowledge-base lifecycle** — *Purpose:* make content governance visible as the real quality lever. *Elements:* a unit moving through Draft → Active → UnderReview → Retired, with `ReviewDueOn` as a gate and a branch showing retired units remaining searchable for audit but excluded from retrieval. *Style:* state diagram.

### Images (screenshots)
1. **The invented citation** — *why:* the most persuasive artefact in the module; *content:* an ungrounded draft citing `KB-SVC-0199` next to a knowledge-base search returning "no results".
2. **`DraftEditLog` with three deltas** — *why:* shows edits as an asset; *content:* draft text and approved text side by side with the changed phrases highlighted.
3. **A rendered bilingual reply** — *why:* the register and dual dating must be seen to be learned; *content:* the Arabic reply RTL with `التاريخ: ١٤٤٧/١١/٢٥هـ الموافق ٢٠٢٦/٠٥/١٧م` and the English parallel text beneath.

### Simulations
1. **The retired unit** — *Setup:* branch `sim-no-status-filter` with both the SAR 300 retired unit and the SAR 750 active unit present. *Expected behaviour:* roughly half of fee enquiries quote the obsolete figure with a perfectly valid citation. *Learning objective:* grounding is only as good as the retrieval contract.
2. **The rubber stamp** — *Setup:* present twenty ungrounded drafts to participants acting as approving officers under a five-minute time limit. *Expected behaviour:* three planted factual errors are approved by most participants. *Learning objective:* human review of unsourced fluent text is not a control.

### Interactive Activities
- **Register clinic (15 min):** three drafted replies in Arabic — one correct formal register, one subtly colloquial, one over-formal to the point of obscurity. Teams rank them and articulate the specific markers. Arabic-first speakers lead; this is the activity where they carry the room.
- **Write the refusal (12 min):** teams draft the prompt clause that makes refusal attractive, then test it against four enquiries the knowledge base cannot answer. Compare which wordings actually produce `sufficient: false` rather than a confident partial answer.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ApprovedKnowledgeBase.xlsx` | Synthetic approved answer units incl. 3 retired fee units and 2 past review date | XLSX | 84 units | Retrieval source; contains the planted retrieval defect |
| `injaz_enquiries_120.csv` | Synthetic citizen enquiries, 84 Arabic / 36 English, 11 outside knowledge-base coverage | CSV | 120 rows | Coverage, drafting and approval measurement |
| `HijriCalendar.xlsx` | Gregorian–Hijri mapping for 2026–2027 | XLSX | 730 rows | Reliable dual dating without expression arithmetic |
| `formal_register_examples.docx` | Six real-style Arabic official replies with the conventional formulas annotated | DOCX | 6 pages | The register clinic and prompt tuning |

### Demo Requirements
- **Instructor demo (8 minutes):** ask the room for a service and a question about its fee. Run it ungrounded on the projector — get a confident SAR figure — and ask the room whether they believe it. Then run it grounded, show the cited unit, open the unit, and read the quoted sentence. Finally, click Approve and show that nothing was sent until that click. Three moves, eight minutes, and the module's entire argument is made in front of them rather than at them.

---

# Module 5 — Data Consolidation and Reporting: Pulling from Multiple Systems into One Trusted Report

## المحور الخامس — تجميع البيانات وإعداد التقارير الموثوقة

## Module Overview

**Purpose.** Every Tuesday afternoon an analyst in Injaz's performance unit opens a SharePoint list, an Excel workbook maintained by finance, and a mailbox of returns from three sections, copies figures into a template, notices two numbers disagree, emails to ask which is right, waits, and publishes on Wednesday. Fifteen hours of work per report, across four people. This module replaces the copying and the chasing with a scheduled flow that pulls, joins, **reconciles**, formats bilingually, drafts a narrative, and publishes Sunday 08:00 — while the head of performance still signs the narrative. It saves **46 hours a month**.

**Business relevance.** Consolidated reporting is where a government department's numbers become official, and where they most often become wrong. The failure is rarely arithmetic; it is that three systems answer the same question differently and nobody reconciles them. A report automation that skips reconciliation industrialises the disagreement instead of resolving it. This module teaches reconciliation as the non-negotiable middle step.

**Industry use cases.**
- A regional authority publishes a weekly performance pack drawn from a case system, a finance workbook and section email returns, with a reconciliation panel that shows any variance before the report is issued rather than after.
- A ministry's programme office consolidates twelve directorate returns into one bilingual dashboard, and the automation refuses to publish while any return is missing rather than silently reporting eleven-twelfths of reality.
- A shared-service centre produces a monthly pack whose narrative is drafted from the figures in the pack and cites each claim to the table it came from, so no sentence can survive a figure changing.

**Expected competencies.** After this module a participant can pull data from SharePoint, Excel and a mailbox in one flow; join without SQL using a shared key; write reconciliation checks that block publication; build a bilingual formatted output; constrain a narrative to the figures present; and design a completeness gate.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Pull data from SharePoint, Excel Online and a mailbox in a single scheduled flow | LO6, CO1 |
| 5.2 | Join datasets on a shared key without SQL, and handle missing and duplicate keys | LO6, CO1 |
| 5.3 | Write reconciliation checks that compare independent sources and block publication on variance | LO6, CO2 |
| 5.4 | Build a bilingual formatted report with correct number, date and currency rendering | LO6, CO1 |
| 5.5 | Generate a narrative summary constrained to the figures in the report, with no new facts | LO6, LO5, CO3 |
| 5.6 | Implement a completeness gate that refuses to publish an incomplete report | LO6, LO7, CO2 |

## Technical Content

### 1. Three sources, three different truths

| Source | What Injaz keeps there | Refresh | Key | Characteristic failure |
|---|---|---|---|---|
| SharePoint list `CorrespondenceRegister` | Every letter, its class, owner, due date, closure | Real time | `ReferenceNumber` | Items edited after the reporting cut-off change last week's number |
| Excel Online `Finance_Commitments.xlsx` | Committed and spent SAR by section and budget line | Weekly, manual | `SectionCode` + `BudgetLine` | The workbook is open and locked by a finance officer when the flow runs |
| Outlook shared mailbox `sections@agency.gov.sa` | Three weekly section returns as email tables | Weekly, by Thursday | `SectionCode` | A section does not send; or sends twice with different figures |

The reporting rule that follows: **every figure in the report must be attributable to one named source and one cut-off timestamp.** Injaz stamps every report with `DataAsOf` and freezes a snapshot of each source at pull time, so a report is reproducible next month even after the underlying list has moved on.

### 2. Joining without SQL

Low-code joins are done with a lookup pattern: build a dictionary-shaped array from the smaller source, then project the larger source through it. Two hazards dominate: **missing keys** (a section in the register that finance has never heard of) and **duplicate keys** (a section that sent its return twice). Both must be detected, never silently absorbed — an inner join that quietly drops unmatched rows is how a report loses a whole section.

### 3. Reconciliation: the step that is always skipped

Reconciliation compares two independent measurements of the same quantity and reports the variance. Injaz runs four checks before any report is published:

| Check | Compares | Tolerance | On breach |
|---|---|---|---|
| **Volume** | Letters closed this week per the register vs the total in the three section returns | 0 items | Block publication; list the discrepant sections |
| **Financial** | Sum of section spend in the returns vs finance workbook total | SAR 0 (must match exactly) | Block; produce a variance line per section |
| **Completeness** | Section returns received vs sections expected | 0 missing | Block; chase the missing sections; state which are absent |
| **Continuity** | This week's opening balance vs last week's closing balance | 0 items | Warn and annotate; do not block, but the narrative must mention it |

The distinction between **block** and **warn** is the design judgement to teach. A financial mismatch is a blocker because publishing it makes the agency's numbers wrong. A continuity break is a warning because it usually reflects a legitimate late closure, and blocking on it would stop the report every second week — which trains everyone to bypass the gate.

### 4. Bilingual formatting that survives contact with Arabic

- **Numbers stay in Western Arabic numerals in tables** for both languages; Injaz uses Eastern Arabic-Indic numerals only in formal correspondence dates, not in report tables, because mixed numeral systems in a table break sorting and comparison.
- **Currency** is written `SAR 1,240,500` in English and `1,240,500 ريال` in Arabic — the symbol position differs and the thousands separator does not.
- **Dates** carry both calendars in the report header once, not in every row.
- **Table direction** flips: the Arabic table's first column is on the right. Build two rendered tables, not one table with translated headers, or the Arabic version will read backwards.

### 5. The narrative, constrained

The narrative is the paragraph the head of performance reads first and the one most likely to contain an invented fact. Three controls: the model receives **only the finished report tables**, never the raw sources; every quantitative claim must reference a table and row; and comparative language (`rose`, `fell`, `improved`) is permitted only where the report actually contains the prior period's figure.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Snapshot at pull time, stamp `DataAsOf`, and never recompute a published report.*
- *Detect unmatched and duplicate keys explicitly; an inner join is a silent data-loss device.*
- *Reconcile before you format.* Formatting a wrong number faster is not an improvement.
- *Block on money, warn on continuity.* Choose deliberately and document the choice.
- *The narrative reads the report, not the sources.*
- *Publication is a decision.* The head of performance signs; the flow assembles.

**Common mistakes (each is planted in the Lab 5 starter)**
1. The join is an inner join, so the section whose return arrived late disappears from the report entirely — and the total looks plausible.
2. No `DataAsOf` stamp, so two people running the report an hour apart get different numbers and neither can prove which was right.
3. Reconciliation is computed and displayed but does not block publication, so a SAR 41,300 variance is published with a small amber note nobody reads.
4. The Excel action fails when the workbook is locked by a finance officer, with an exponential retry that eventually gives up silently.
5. The narrative is generated from the raw sources rather than the finished tables, and states a figure that appears nowhere in the report.
6. The Arabic table is the English table with translated headers, so the column order reads backwards.

**Production considerations**
- Schedule the pull **after** the source cut-offs, not before: Injaz pulls Saturday 22:00 for a Sunday 08:00 publication, giving a four-hour window for failures to be noticed and fixed by a human.
- Keep a published-report archive with its snapshot. When someone disputes a figure four months later, the snapshot is the answer.
- Excel Online concurrency is a real constraint: prefer a copy-then-read pattern over reading a workbook people are editing.
- Report the reconciliation result *in* the report. A report that says "all four checks passed at 22:04" earns trust that a silent report never does.

### 7. Real-world example walkthrough

Narrate in five minutes. A programme office automated a weekly directorate report and cut production from two days to twenty minutes. Six weeks later the programme director noticed the completion percentage had not moved in a month despite visible progress. The join was on directorate name as free text; three directorates had been renamed in a restructuring; their rows stopped matching and were silently dropped by an inner join. The report had been reporting nine directorates out of twelve, with a denominator that also dropped, so every percentage looked reasonable. The fix took an hour: join on a stable code, and add an explicit unmatched-key check that blocks publication. The lesson: **the dangerous data defect is not the one that makes the report look broken; it is the one that makes it look fine.**

## Code Examples

### Reconciliation checks with a publication gate

```text
# injaz/flows/weekly-report/reconciliation.txt
# Runs after all three sources are pulled and joined, BEFORE any formatting.
# Two blocking checks, one blocking completeness check, one warning check.

# --- CHECK 1: volume (blocking) ---
@equals(
  length(body('Filter_register_closed_this_week')),
  sum(body('Select_section_closed_counts'))
)
# false -> varBlockers += 'VOLUME: register 214 vs returns 209 (delta 5)'

# --- CHECK 2: financial (blocking, exact match required) ---
@equals(
  formatNumber(body('Compose_returns_spend_total'), 'F2'),
  formatNumber(first(body('Get_finance_rows'))?['TotalSpendSAR'], 'F2')
)
# false -> varBlockers += 'FINANCE: returns SAR 3,118,700.00 vs workbook SAR 3,160,000.00
#                          (delta SAR 41,300.00)'

# --- CHECK 3: completeness (blocking) ---
@equals(length(body('Get_section_returns')), 3)
# false -> varBlockers += concat('MISSING RETURNS: ',
#            join(body('Select_missing_section_codes'), ', '))

# --- CHECK 4: continuity (warning only, annotates the narrative) ---
@equals(
  body('Compose_opening_open_items'),
  first(body('Get_last_week_snapshot'))?['ClosingOpenItems']
)
# false -> varWarnings += 'CONTINUITY: opening 88 vs last week closing 91 (3 late closures)'

# --- PUBLICATION GATE ---
@equals(length(variables('varBlockers')), 0)
#  TRUE  -> format report -> approval to Head of Performance -> publish
#  FALSE -> DO NOT FORMAT. Send a blocker notice to the analyst + the owning sections,
#           write a ReportBlocked row, and terminate Succeeded.
#           A blocked report is a correct outcome, not a failed run.

# --- Duplicate and unmatched key detection (run before the checks) ---
# duplicates: a section that returned twice
@greater(length(body('Get_section_returns')), length(union(body('Select_section_codes'), body('Select_section_codes'))))
# unmatched: a register section absent from finance
@length(body('Filter_register_sections_not_in_finance'))    # must be 0
```

### The narrative prompt, constrained to the report

```text
# injaz/prompts/report_narrative.md
# Receives ONLY the finished report tables. Never the raw sources.
# Model temperature: 0.2. The Head of Performance approves before publication.

SYSTEM
You write the executive narrative for a Saudi government department's weekly report.
The Head of Performance reviews and signs it. You never publish anything.

HARD RULES
1. Use ONLY figures that appear in the TABLES below. Every number you write must be
   copied from a table, and you must name the table it came from in "sources".
2. Never compute a new figure — no percentages, ratios, averages or projections that
   are not already printed in a table.
3. Comparative words (rose, fell, improved, worsened) are permitted ONLY where the table
   contains both this period and the prior period. Otherwise describe the level only.
4. If the RECONCILIATION block contains warnings, you MUST mention each warning in one
   sentence. Do not soften it and do not explain it away.
5. Maximum 140 words per language. Arabic is primary; English is a parallel text.
6. No recommendations, no causal claims, no attribution of performance to any named
   person or section beyond what the tables state.

OUTPUT — one JSON object:
{ "narrative_ar": "<=140 words",
  "narrative_en": "<=140 words",
  "sources": ["Table 1 — Correspondence", "Table 3 — Commitments"],
  "warnings_mentioned": ["CONTINUITY: opening 88 vs last week closing 91"] }

USER
REPORTING WEEK: {{week_label}}    DATA AS OF: {{data_as_of}}
RECONCILIATION: {{reconciliation_block}}
TABLES:
{{rendered_report_tables}}
```

### Bilingual table rendering

```text
# injaz/flows/weekly-report/render-bilingual-tables.txt
# Build TWO tables, not one with translated headers. Arabic column order is reversed.

# --- English table: Create HTML table action, Columns = Custom ---
Section        : @{item()?['SectionNameEn']}
Letters closed : @{item()?['ClosedCount']}
Open > SLA     : @{item()?['OverdueCount']}
Spend          : @{concat('SAR ', formatNumber(item()?['SpendSAR'], 'N0'))}

# --- Arabic table: same data, REVERSED column order, Arabic currency form ---
المصروفات      : @{concat(formatNumber(item()?['SpendSAR'], 'N0'), ' ريال')}
متجاوز المدة   : @{item()?['OverdueCount']}
المعاملات المغلقة : @{item()?['ClosedCount']}
القسم          : @{item()?['SectionNameAr']}

# --- Wrap the Arabic table for correct rendering in Outlook and SharePoint ---
@{concat('<div dir="rtl" style="text-align:right;font-family:''Segoe UI'',Tahoma;">',
         body('Create_HTML_table_ar'),
         '</div>')}

# --- Header stamped once, both calendars, both languages ---
@{concat(
  'Data as of ', formatDateTime(variables('varDataAsOf'), 'yyyy/MM/dd HH:mm'), ' AST',
  '  |  البيانات حتى ', first(body('Get_hijri'))?['HijriDate'], 'هـ',
  '  |  Reconciliation: ', if(equals(length(variables('varBlockers')),0),
                              'PASSED', 'BLOCKED'),
  ' (', string(length(variables('varWarnings'))), ' warning(s))')}
# -> Data as of 2026/05/16 22:04 AST | البيانات حتى 1447/11/24هـ | Reconciliation: PASSED (1 warning(s))
```

## Hands-on Lab 5 — Build the Injaz Weekly Departmental Report

| | |
|---|---|
| **Objective** | Build a scheduled flow that pulls three sources, detects unmatched and duplicate keys, runs four reconciliation checks with a publication gate, renders bilingual tables, drafts a constrained narrative, obtains the Head of Performance's approval, and publishes — then claim the 46 h/month saving |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab5_Start_1_0_0_1.zip` (creates `WeeklyReportArchive`, `ReportBlocked`, seeds `Finance_Commitments.xlsx` and three section-return emails, one of which is a duplicate and one of which is missing). Standard connectors only. |

**Instructions & tasks**

1. *(8 min)* Build the Saturday 22:00 recurrence (Arab Standard Time) and the three pulls. Snapshot each source to `WeeklyReportArchive` with a `DataAsOf` stamp. Confirm the Excel pull handles a locked workbook by copying the file first rather than reading it in place.
2. *(9 min)* Join register data to finance on `SectionCode`. Replace the starter's inner join. Add explicit unmatched-key and duplicate-key detection; the seeded data contains one duplicate section return and one section present in the register but absent from finance. Both must be reported, not absorbed.
3. *(11 min)* Implement all four reconciliation checks and the publication gate. The seeded data breaches the financial check by SAR 41,300 and is missing one section return. Confirm the flow **blocks**, writes a `ReportBlocked` row, notifies the analyst and the owning sections, and terminates Succeeded — with no formatted report produced.
4. *(8 min)* Correct the seeded finance workbook and add the missing return, then re-run. Confirm the gate passes with one continuity warning remaining, and that the warning survives into the header.
5. *(9 min)* Render both tables, generate the narrative from the finished tables only, and route to the Head of Performance for approval. Verify every figure in the narrative appears in a table and that the continuity warning is mentioned. Deliberately feed the narrative prompt the raw sources instead and observe it citing a figure that is not in the report.
6. *(5 min)* Record: `feat(report): 3-source consolidation with blocking reconciliation, 46 h/month`.

**Expected output**
```text
=== Run 1 — Saturday 2026-05-16 22:00 AST ===
Pulled: CorrespondenceRegister 1,204 rows | Finance_Commitments 18 rows | Section returns 3 emails
Key checks
  duplicate section returns : 1   (SEC-OPS returned twice, figures differ by 6 items)
  register sections not in finance : 1   (SEC-COM)
Reconciliation
  1 VOLUME       FAIL  register 214 closed vs returns 209 (delta 5)
  2 FINANCE      FAIL  returns SAR 3,118,700.00 vs workbook SAR 3,160,000.00 (delta SAR 41,300.00)
  3 COMPLETENESS FAIL  missing returns: SEC-LEG
  4 CONTINUITY   WARN  opening 88 vs last week closing 91 (3 late closures)
PUBLICATION GATE: BLOCKED (3 blockers)
  -> ReportBlocked row 12 written; notices sent to analyst + SEC-OPS, SEC-COM, SEC-LEG
  -> no report formatted, run status Succeeded

=== Run 2 — after corrections, 2026-05-16 23:15 AST ===
Reconciliation: 1 PASS | 2 PASS | 3 PASS | 4 WARN (continuity, 3 late closures)
PUBLICATION GATE: PASSED (1 warning)
Narrative: 128 words AR / 134 words EN | sources: Table 1, Table 3 | warning mentioned: yes
Approval: Head of Performance approved 2026-05-17 07:41 AST, unedited
Published 2026-05-17 08:00 AST to the department SharePoint page + 41 recipients

Narrative accuracy check: 9 figures cited, 9 present in tables, 0 not in report
Un-grounded control run (task 5): cited "average closure 4.2 days" — appears in NO table

=== Benefit claimed ===
Weekly report: 4 reports/month × (900 min -> 210 min) = 46 h/month, 552 h/year
Publication: Wednesday (variable) -> Sunday 08:00 (fixed)
```

**Acceptance criteria**
- All three sources are snapshotted with a single shared `DataAsOf`; the Excel read survives a locked workbook.
- Duplicate and unmatched keys are detected and reported explicitly; no row is silently dropped.
- The financial and completeness breaches **block** publication and produce a notice; a continuity breach warns and is carried into the report header and the narrative.
- Two separately rendered tables exist with correct direction, currency form and column order per language.
- Every figure in the narrative appears in a rendered table; the flow publishes only after the Head of Performance's approval.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| A section vanishes from the report and totals look fine | Inner join dropped an unmatched key | Detect unmatched keys explicitly and report them |
| Two people get different numbers an hour apart | No `DataAsOf` snapshot | Snapshot at pull time; never recompute a published report |
| Excel action fails "file is locked" | Finance officer has the workbook open | Copy the file to a working folder, then read the copy |
| SAR 41,300 variance published with a small amber note | Reconciliation displayed but not gating | Make the gate a condition on publication, not a formatting flourish |
| Arabic table reads backwards | One table with translated headers | Render two tables; reverse column order; wrap in `dir="rtl"` |
| Narrative cites a figure not in the report | Prompt fed the raw sources | Feed only the rendered tables; require a `sources` array |

**Instructor notes.** Task 3 is the module — most participants will build the reconciliation panel and then wire publication to run regardless, because that is how every report they have ever seen behaves. Check the gate condition on every pair's flow personally. The second thing to watch: several will "fix" the SAR 41,300 variance by changing the tolerance to SAR 50,000. Stop that immediately and ask what the tolerance means: a tolerance on a financial reconciliation is a statement that the agency does not know where up to SAR 50,000 went. Fast finishers: add a fifth check comparing this week's snapshot against the previous week's archive to detect retrospective edits to closed items — a real and common source of "the number changed" disputes.

## Mini Exercises

**Quiz (5 questions)**
1. Why is an inner join dangerous in a report flow? → it silently drops unmatched rows, and the resulting totals still look plausible.
2. What does `DataAsOf` protect against? → two runs at different times producing different numbers with no way to say which was right.
3. Which reconciliation breaches should block publication and which should warn? → money and completeness block; continuity warns, because blocking on it trains people to bypass the gate.
4. Where must the narrative's figures come from? → the finished report tables only, with each claim attributed to a table.
5. Why render two tables rather than translate headers? → Arabic column order reverses; a translated header row reads backwards.

**Debugging exercise.** Provide a report whose completion percentage has been static for four weeks while activity visibly increased. Participants must find the free-text join key broken by a renaming, and then explain why both numerator and denominator dropping made the defect invisible.

**Design exercise.** Finance wants the tolerance on the financial check raised to SAR 5,000 "to stop blocking on rounding". Decide, and specify what would have to be true for a non-zero tolerance to be defensible — and what must be recorded when one is set.

**Discussion questions.**
- Blocking publication makes the automation look unreliable to a director who only sees "the report didn't come out". How do you make a blocked report read as the system working?
- Should the reconciliation result appear in the published report, visible to all 41 recipients? What changes about the department if it does?

## Case Study — The Report That Was Right Every Week and Wrong All Along at "Hasilah" (حصيلة)

**Scenario.** "Hasilah" (حصيلة), the performance and reporting unit of a regional water authority in Al-Ahsa, automated a weekly operations report drawn from a maintenance system, a finance workbook and eleven area-office returns. It ran flawlessly for seven months: green runs, on time, no complaints.

**Business context.** The report drives resource allocation across eleven areas and is the basis of a quarterly submission to the authority's board. Areas are funded partly on reported workload.

**Technical challenge.** Two area offices had been merged in a restructuring nine months earlier. Their return emails continued to arrive under the old area codes for three weeks, then stopped. The join was an inner join. From week four onward the report covered nine areas of eleven, and because both the workload numerator and the funded-area denominator came from the same joined set, every ratio, average and percentage remained entirely plausible. Two areas received no allocation for six months and their supervisors' escalations were dismissed as complaints about a system that was demonstrably working.

**Constraints.** Six months of board submissions rest on the affected figures. The restructuring is real and the old codes should not be reinstated. The unit must present a correction to the board, and the two areas are owed a retrospective allocation review. The report cannot stop.

**Solution approach (facilitate, don't lecture).** Guide toward: (1) the technical fix is small — an explicit unmatched-key check that blocks, plus joining on a stable code that survives restructuring; (2) the organisational fix is larger, namely that the *completeness* check must be against an authoritative list of areas maintained outside the report, so a missing area is detected by absence rather than inferred from the data itself; (3) exposure must be quantified by re-running seven months of archived snapshots against the corrected logic; (4) the supervisors' escalations were the only working detector the system had, and the unit ignored them because the automation looked healthy — which is the real cultural finding; (5) add a standing rule that any structural change to the organisation triggers a review of every automation that joins on organisational identifiers.

**Discussion questions.**
1. Every run was green for seven months. What monitoring, specifically, would have caught this in week four?
2. Both numerator and denominator dropped together. Why does that make a data defect so much more dangerous than one that produces an obviously wrong number?
3. The supervisors raised it and were dismissed. What process should exist so that a human contradiction of an automated report is investigated rather than explained away?
4. Who is accountable — the flow builder, the performance unit head, or the restructuring team who never told anyone the codes changed? What governance follows from your answer?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Reconciliation checks implemented | Coverage | 4 of 4, with correct block/warn behaviour | gate test on seeded breaches |
| Silent row loss | Correctness | 0 — every unmatched and duplicate key reported | key-check output |
| Narrative figures not present in the report | Correctness | 0 | figure-by-figure audit |
| Report published without approval | Governance | 0 | publish-action run-after audit |
| Hours saved per month (weekly report) | Benefit | 46 h/month (552 h/year) | 4 × (900 → 210 min) |
| Publication predictability | Benefit | Wednesday (variable) → Sunday 08:00 (fixed) | archive timestamps |

**Example benchmark table (filled during lab):**

| Run | Blockers | Warnings | Rows dropped silently | Narrative figures / in-report | Published |
|---|---|---|---|---|---|
| 1 (seeded breaches) | 3 (volume, finance, completeness) | 1 | 0 | — | No — blocked, notices sent |
| 2 (after correction) | 0 | 1 (continuity) | 0 | 9 / 9 | Yes — 2026-05-17 08:00 AST |
| 3 (control: raw sources to narrative) | 0 | 1 | 0 | 10 / 9 | Blocked by instructor — invented figure |
| 4 (control: inner join restored) | 0 | 1 | 47 (SEC-COM) | 9 / 9 | Would have published — the dangerous case |

## Required Visuals and Training Assets

### Diagrams
1. **Three sources, one report** — *Purpose:* the module's shape. *Elements:* SharePoint, Excel and mailbox feeding a snapshot layer stamped `DataAsOf`, then a join, then a reconciliation gate drawn as a physical barrier, then formatting, narrative, approval and publication. *Style:* left-to-right pipeline with the gate visually heavier than everything else.
2. **Block versus warn** — *Purpose:* the design judgement. *Elements:* four checks with two drawn as red stop-bars and two as amber annotations, each labelled with the reasoning. *Style:* four-lane comparison with the rationale printed under each.
3. **The silent inner join** — *Purpose:* make invisible data loss visible. *Elements:* eleven area rows entering, nine leaving, and a ratio computed from the nine that still reads 94% — with the two lost rows greyed at the bottom. *Style:* funnel with a plausible-looking output badge.
4. **Bilingual report layout** — *Purpose:* the formatting standard. *Elements:* the report page with the dual-calendar header, the English table LTR, the Arabic table RTL with reversed columns, the reconciliation stamp, and the narrative block. *Style:* annotated page mock-up.

### Images (screenshots)
1. **A blocked run with its notice** — *why:* participants must see that blocked is a success state; *content:* the `ReportBlocked` row, the notice email listing three blockers, and a green run status.
2. **The reconciliation stamp in a published report** — *why:* trust is built by publishing the check result; *content:* the header line reading `Reconciliation: PASSED (1 warning)`.
3. **Two tables side by side** — *why:* the column-reversal rule is easier seen than described; *content:* the English and Arabic tables of the same data, with the direction difference highlighted.

### Simulations
1. **The vanishing section** — *Setup:* branch `sim-inner-join` with one section's code changed. *Expected behaviour:* the section disappears; all percentages remain plausible; the run is green. *Learning objective:* the dangerous defect is the one that looks fine.
2. **Tolerance creep** — *Setup:* the financial tolerance raised to SAR 50,000 over three simulated weeks with growing variances. *Expected behaviour:* nothing blocks; the variance reaches SAR 47,800 unnoticed. *Learning objective:* a tolerance is a statement about what you are willing not to know.

### Interactive Activities
- **Design the checks (15 min):** teams receive a different three-source report (procurement, HR headcount, or fleet) and must specify four reconciliation checks, each labelled block or warn, with the reasoning. Cross-team critique focuses on the block/warn judgements.
- **Find the figure (10 min):** a printed narrative and a printed report pack; teams race to verify every number in the narrative against a table. One planted figure is not in the pack.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `CorrespondenceRegister` (from Lab 3) | Carried forward | SharePoint list | 1,204 rows | Volume and closure figures |
| `Finance_Commitments.xlsx` | Synthetic finance workbook with a seeded SAR 41,300 variance | XLSX | 18 rows | Financial reconciliation |
| `section_returns_week20/` | Three return emails: one duplicate, one missing, one clean | EML | 3 files | Completeness and duplicate-key detection |
| `weekly_report_archive_sample/` | Twelve prior weekly snapshots | JSON | 12 files | Continuity checks and retrospective-edit detection |

### Demo Requirements
- **Instructor demo (7 minutes):** run the report with the seeded breaches and let it block on the projector. Read the notice aloud. Then ask the room what the alternative was: publish a report in which SAR 41,300 is unaccounted for and one section is missing. Correct the workbook live, re-run, and show it publish with the continuity warning visible in the header. The contrast between a blocked run and a green wrong report is the whole module in seven minutes.

---

# Module 6 — Meetings, Minutes, and Action Tracking

## المحور السادس — الاجتماعات والمحاضر ومتابعة الإجراءات

## Module Overview

**Purpose.** Injaz's committee secretariat supports 160 meetings a month. For each one a secretary listens back to a recording, writes minutes, separates the decisions from the discussion, extracts action items with owners and dates, emails them out, and then chases for weeks. Forty-five minutes of work per meeting, and actions that surface only when someone remembers them. This module turns a transcript into schema-constrained minutes with decisions, owners and due dates, obtains the chair's approval, creates tracked action items, and chases them automatically with an escalation ladder. It saves **88 hours a month**.

**Business relevance.** In Saudi government practice the minute is the artefact that makes a decision real — it is cited, escalated against, and audited. Minutes that arrive four days late have already lost their steering value, and action items that live in the body text of an email are, operationally speaking, not tracked at all. This module converts a document into a workflow, which is the single highest-leverage change available to any secretariat.

**Industry use cases.**
- A council secretariat issues approved minutes the same day, with action items already in a tracked list and owners already notified.
- A programme office turns weekly steering-committee transcripts into a decisions log that can be searched across a year — "when did we decide the phase-2 scope?" becomes a two-second query.
- A directorate's action tracker chases owners automatically at 48 hours before due, on the due date, and escalates to the chair at 72 hours overdue, cutting the proportion of actions closed late from 46% to 12%.

**Expected competencies.** After this module a participant can process a recording or transcript into structured minutes; distinguish decisions from discussion in a prompt and a schema; extract owners and dates reliably including relative dates; route minutes through a chair's approval before they become the record; generate tracked action items; and build a chase-and-escalate loop that does not become spam.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Convert a recording or transcript into schema-constrained minutes | LO4, LO6, CO1 |
| 6.2 | Separate decisions from discussion and attributed positions in prompt and schema | LO4, CO3 |
| 6.3 | Extract action owners and due dates reliably, including relative and unstated dates | LO4, CO1 |
| 6.4 | Route minutes through the chair's approval before they become the official record | LO5, LO7, CO4 |
| 6.5 | Generate tracked action items and a chase-and-escalate loop with humane cadence | LO3, LO6, CO2 |

## Technical Content

### 1. Three artefacts, not one

A meeting produces three separate things that are routinely conflated, and separating them is most of the design.

| Artefact | Purpose | Audience | Lifespan | Approval |
|---|---|---|---|---|
| **Transcript** | Raw record of what was said | Nobody, normally | Delete after minutes approved (PDPL: minimisation) | None |
| **Minutes** | The official record of attendance, discussion summary and decisions | Members, auditors, successors | Permanent record series | The chair approves |
| **Action items** | Tracked commitments with owner and date | The owner, the secretariat, the chair | Until closed, then archived with the minutes | Owner accepts or disputes |

The transcript is the most sensitive and the least valuable. It contains verbatim attributed statements, often about people, and it exists only to be processed. Injaz's rule: **the transcript is deleted within seven days of the minutes being approved**, and this is stated in the meeting invitation so participants know.

### 2. Decisions versus discussion

The hardest extraction judgement in this module is what counts as a decision. Teach a three-part test the model is given explicitly: a decision has (a) an outcome that is settled rather than explored, (b) an authority — the committee, the chair, or a named delegate — and (c) an effect on someone outside the room. "We discussed extending the deadline and Ahmed thought it was risky" is discussion. "The committee approved extending the deadline to 30 Ramadan" is a decision. "The chair asked Finance to prepare options" is an action, not a decision.

Attribution is a governance question, not a stylistic one. Injaz's rule: decisions are attributed to the **committee or the chair**, never to an individual member; individual positions are recorded only where a member explicitly asks for their dissent to be minuted. This protects members and matches Saudi committee practice.

### 3. Dates that are not dates

Meeting language expresses deadlines relatively: "by next Sunday", "before the end of the month", "within two weeks", "before the Eid break", "at the next meeting". A model asked for a date will produce one, and if it guesses the reference point it will be wrong. Three controls: supply the meeting date explicitly in the prompt as the anchor for all relative expressions; require the model to return **both** the original phrase and the resolved date so a human can check the resolution; and permit `null` with a `date_basis` of `unstated`, which routes the action to the secretary to confirm with the owner rather than inventing a deadline nobody agreed.

### 4. The chase ladder

An action tracker that emails owners daily is switched off within a fortnight. A humane, effective cadence has four rungs and stops escalating once the action moves:

| Rung | Trigger | Recipient | Tone |
|---|---|---|---|
| 1 | 48 hours before due | Owner only | Reminder, single line, no CC |
| 2 | On the due date | Owner only | Request for status; offers "request extension" as a one-click reply |
| 3 | 72 hours overdue | Owner, CC secretary | Formal, names the minute reference and the committee |
| 4 | 7 days overdue | Chair, with the owner CC'd | Escalation, appears in the next meeting's overdue annex |

Two rules make it humane. **Never chase on a weekend or a public holiday** — a Thursday-due action is chased Sunday, not Friday. And **an owner who requests an extension with a reason moves to a new due date without escalation**, because the point is visibility of the real date, not punishment for a slipped one.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Three artefacts, three lifetimes.* Transcript is transient; minutes are permanent; actions are tracked until closed.
- *The chair approves; the flow drafts.* Minutes are not the record until a human says they are.
- *Return the phrase and the resolved date.* Never just the date.
- *Null beats invention for a deadline nobody stated.*
- *Attribute decisions to the committee, positions only on request.*
- *Escalation stops when the action moves.*

**Common mistakes (each is planted in the Lab 6 starter)**
1. The transcript is retained indefinitely alongside the minutes, creating a permanent verbatim record of attributed statements — a PDPL and a political problem.
2. Discussion is minuted as decisions, so the minutes record four "decisions" the committee never took.
3. Relative dates are resolved against the *processing* date rather than the meeting date, shifting every deadline by however long the flow took to run.
4. Action items are created before the chair approves the minutes, so owners receive tasks from a draft that later changes.
5. The chase loop runs daily with no escalation ceiling, sending an owner 14 identical emails about one overdue action.
6. Chasing ignores weekends, so Thursday-due actions are chased on Friday and everyone learns to ignore the sender.

**Production considerations**
- Recording consent is a meeting-practice matter, not a flow setting: the invitation must state that the meeting is recorded, why, and when the recording is deleted.
- Store the approved minutes as the record and keep the model's draft separately for a defined period; the difference between draft and approved is audit-relevant.
- Give every action a stable identifier tied to the minute reference (`MIN-2026-041/A3`) so it can be cited in the next meeting.
- Carry forward open actions into the next meeting's agenda automatically. This is a five-action addition that changes the culture of a committee more than anything else in the module.

### 6. Real-world example walkthrough

Narrate in five minutes. A programme steering committee automated its minutes and was delighted for a month. Then a member objected in a meeting that the previous minutes recorded him as having "agreed to absorb the cost within his directorate's budget" — something he had raised as a question, not a commitment. The transcript, still retained, was produced, and it showed he had said "could we absorb that within the directorate budget?". The model had converted an interrogative into a commitment, the chair had approved minutes he had skimmed, and the directorate had been carrying an unfunded SAR 400,000 line for six weeks. Three changes followed: the decision test was written into the prompt explicitly, every extracted decision now carries a verbatim `evidence_quote` shown to the chair beside it, and the chair's approval card presents decisions and actions first with discussion collapsed. Approval time went *up* by ninety seconds and disputes went to zero. The lesson: **the chair cannot approve what the chair cannot see, and a wall of fluent prose is designed to be skimmed.**

## Code Examples

### The minutes extraction schema

```json
// injaz/schemas/meeting_minutes.schema.json
// Bound to injaz/prompts/extract_minutes.md and to the Parse JSON action.
// Note: decisions and actions are separate arrays with different required fields.
{
  "type": "object",
  "required": ["meeting_reference", "meeting_date", "attendees", "apologies",
               "discussion_summary_ar", "discussion_summary_en", "decisions", "actions"],
  "properties": {
    "meeting_reference": { "type": "string", "pattern": "^MIN-[0-9]{4}-[0-9]{3}$" },
    "meeting_date":      { "type": "string", "format": "date" },
    "attendees":         { "type": "array", "items": { "type": "string" } },
    "apologies":         { "type": "array", "items": { "type": "string" } },
    "discussion_summary_ar": { "type": "string", "maxLength": 1200 },
    "discussion_summary_en": { "type": "string", "maxLength": 1200 },
    "decisions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["decision_id", "text_ar", "text_en", "authority", "evidence_quote"],
        "properties": {
          "decision_id":    { "type": "string", "pattern": "^D[0-9]+$" },
          "text_ar":        { "type": "string", "maxLength": 300 },
          "text_en":        { "type": "string", "maxLength": 300 },
          "authority":      { "type": "string", "enum": ["Committee", "Chair", "Delegated"] },
          "delegate_name":  { "type": ["string", "null"] },
          "evidence_quote": { "type": "string", "maxLength": 200,
                              "description": "Verbatim transcript text that settles this as a decision. Shown to the chair." },
          "dissent_recorded": { "type": ["string", "null"],
                              "description": "Only where a member explicitly asked for dissent to be minuted." }
        },
        "additionalProperties": false
      }
    },
    "actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["action_id", "text_ar", "text_en", "owner_name",
                     "due_phrase", "due_date", "date_basis", "evidence_quote"],
        "properties": {
          "action_id":   { "type": "string", "pattern": "^A[0-9]+$" },
          "text_ar":     { "type": "string", "maxLength": 300 },
          "text_en":     { "type": "string", "maxLength": 300 },
          "owner_name":  { "type": "string" },
          "owner_email": { "type": ["string", "null"],
                           "description": "null when the name cannot be matched to the directory — routes to the secretary." },
          "due_phrase":  { "type": "string",
                           "description": "The words actually used, e.g. 'before the end of the month'." },
          "due_date":    { "type": ["string", "null"], "format": "date" },
          "date_basis":  { "type": "string",
                           "enum": ["explicit", "relative_to_meeting_date", "unstated"] },
          "evidence_quote": { "type": "string", "maxLength": 200 }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

### The minutes extraction prompt

```text
# injaz/prompts/extract_minutes.md
# Input: transcript + meeting metadata. Output: the minutes schema, nothing else.
# Model temperature: 0. The chair approves before anything becomes the record.

SYSTEM
You produce draft minutes for a Saudi government committee. The chair reviews and
approves every minute before it becomes the official record. You never issue anything.

THE DECISION TEST — apply it to every candidate. It is a DECISION only if all three hold:
  (a) the outcome is settled, not being explored;
  (b) an authority settled it — the committee, the chair, or a named delegate;
  (c) it has an effect on someone outside this room.
"We discussed X and Y thought it risky"        -> discussion, NOT a decision
"The committee approved X"                     -> decision, authority = Committee
"The chair asked Finance to prepare options"   -> ACTION, not a decision
A question ("could we absorb that?")           -> NEVER a decision or a commitment

RULES
1. Every decision and every action MUST carry a verbatim evidence_quote from the transcript.
   If you cannot quote it, it did not happen and you must not record it.
2. Attribute decisions to "Committee" or "Chair". Never attribute a decision to an
   individual member. Record dissent ONLY where a member explicitly asked for it to be minuted.
3. Dates: MEETING_DATE below is the anchor for every relative expression. Return the words
   actually used in due_phrase AND the resolved date in due_date.
   - "by next Sunday"          -> date_basis = relative_to_meeting_date
   - "by 12 June"              -> date_basis = explicit
   - no deadline stated        -> due_date = null, date_basis = unstated
   Never invent a deadline. A null routes the action to the secretary to confirm.
4. owner_email: match owner_name against the ATTENDEE DIRECTORY. No confident match -> null.
5. discussion_summary is a neutral summary of the debate. Do not repeat decisions there.
6. Do not add anything not present in the transcript: no context, no background, no
   recommendation, no "it was noted that" unless it was actually noted.

OUTPUT: one JSON object matching the schema below. No prose, no markdown fence.
{{ contents of injaz/schemas/meeting_minutes.schema.json }}

USER
MEETING_REFERENCE: {{meeting_reference}}
MEETING_DATE: {{meeting_date}}          # anchor for ALL relative dates
ATTENDEE DIRECTORY: {{attendee_directory}}
--- TRANSCRIPT BEGINS ---
{{transcript}}
--- TRANSCRIPT ENDS ---
```

### The chase-and-escalate loop

```text
# injaz/flows/action-tracking/chase-ladder.txt
# Recurrence: daily 08:00 Arab Standard Time, Sunday to Thursday only.
# Escalates once per rung, stops when the action moves. Never chases on a weekend.

# --- Working-day guard: skip Friday and Saturday, and public holidays ---
@and(
  not(contains(createArray('Friday','Saturday'),
      dayOfWeek(convertFromUtc(utcNow(),'Arab Standard Time')))),
  equals(length(body('Get_holiday_today')?['value']), 0)
)
# false -> Terminate Succeeded. No chase today.

# --- Get items: ActionItems, Filter Query ---
Status eq 'Open' and MinutesApproved eq 1 and DueDate ne null
#   NOTE 'MinutesApproved eq 1' — actions from unapproved draft minutes are NEVER chased.

# --- Rung selection, one expression, evaluated per item ---
@{if(greaterOrEquals(div(sub(ticks(utcNow()), ticks(item()?['DueDate'])), 864000000000), 7),
     'R4-escalate-chair',
  if(greaterOrEquals(div(sub(ticks(utcNow()), ticks(item()?['DueDate'])), 864000000000), 3),
     'R3-formal-cc-secretary',
  if(greaterOrEquals(ticks(utcNow()), ticks(item()?['DueDate'])),
     'R2-due-today',
  if(lessOrEquals(div(sub(ticks(item()?['DueDate']), ticks(utcNow())), 864000000000), 2),
     'R1-reminder',
     'none'))))}

# --- Idempotency of chasing: never send the same rung twice ---
@not(equals(item()?['LastRungSent'], outputs('Compose_Rung')))
# After sending: patch LastRungSent = rung, LastChasedOn = utcNow(), ChaseCount + 1

# --- Extension request: one-click reply moves the date, no escalation ---
# Approval option "Request extension" -> writes RequestedDueDate + Reason,
# routes to the secretary for a 1-click confirm, then:
#   DueDate = RequestedDueDate ; LastRungSent = '' ; ExtensionCount + 1
# ExtensionCount >= 2 -> the action appears in the next meeting's agenda regardless.

# --- Observed effect over one quarter (480 actions) ---
#   closed on or before due date : 46% -> 79%
#   closed >7 days late          : 21% ->  6%
#   emails sent per action       : 11.4 -> 2.3     <- the humane-cadence result
```

## Hands-on Lab 6 — Transcript to Minutes to Tracked Actions

| | |
|---|---|
| **Objective** | Build the meetings flow: transcript in → schema-constrained minutes with decisions, actions and evidence quotes → chair approval → tracked action items → chase ladder with escalation and extension handling; verify against the gold minutes for three meetings and claim the 88 h/month saving |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab6_Start_1_0_0_1.zip` (creates `MinutesRegister`, `ActionItems`, `PublicHolidays`, the attendee directory and the transcript drop folder). Transcripts `injaz_meetings_3/` with human gold minutes. Standard connectors only; transcription is pre-supplied as text. |

**Instructions & tasks**

1. *(9 min)* Wire the transcript trigger and the extraction call with the minutes schema. Run meeting `MIN-2026-041` and compare decisions against the gold minutes. The starter prompt lacks the decision test; observe it recording four "decisions" that are discussion, including a question rendered as a commitment.
2. *(8 min)* Add the decision test and the mandatory `evidence_quote`. Re-run and confirm the four false decisions disappear and each surviving decision carries a quotable line. Confirm no decision is attributed to an individual member.
3. *(9 min)* Fix date resolution: the starter anchors relative dates to `utcNow()`. Anchor to `meeting_date`, return `due_phrase` alongside `due_date`, and confirm the action "before the end of the month" resolves to the month of the meeting. Verify the one action with no stated deadline returns `due_date: null` with `date_basis: unstated`.
4. *(8 min)* Build the chair's approval card presenting decisions and actions **first**, each with its evidence quote, and the discussion summary collapsed beneath. Approve `MIN-2026-041` and confirm `ActionItems` rows are created only *after* approval — the starter creates them before.
5. *(11 min)* Build the chase ladder. Seed 18 actions across all four rungs plus one due on a Thursday. Run for a simulated Friday (nothing sent), a Sunday (Thursday action chased), and three consecutive days (each rung sent once, not repeatedly). Exercise one extension request and confirm it moves the date without escalation.
6. *(5 min)* Record: `feat(minutes): transcript to approved minutes + chase ladder, 88 h/month`.

**Expected output**
```text
=== MIN-2026-041 — Shared Services Committee, 2026-05-12 ===
Extraction (starter prompt, no decision test)
  decisions extracted 9  | gold 5  | 4 false positives:
    D3 "Directorate to absorb the cost"  <- source was a QUESTION. The Mudawala defect.
    D6, D7, D9 were discussion positions
Extraction (with decision test + evidence_quote)
  decisions 5 / gold 5   | precision 100% | recall 100%
  actions   7 / gold 7   | owners matched 6, 1 null -> routed to secretary
  date_basis: explicit 3 | relative_to_meeting_date 3 | unstated 1
  "before the end of the month" -> 2026-05-31   (anchored to meeting date, not run date)
  attribution: Committee 4, Chair 1, individual members 0

Chair approval
  presented: 5 decisions + 7 actions with evidence quotes, discussion collapsed
  approved 2026-05-12 16:22 AST with 1 edit (D4 wording)
  ActionItems created: 7, all AFTER approval    <- starter created them before

=== Chase ladder drill, 18 seeded actions ===
simulated Friday  : 0 sent (working-day guard)
simulated Sunday  : 6 sent  (R1 x3, R2 x2 incl. the Thursday-due action, R3 x1)
simulated Monday  : 3 sent  (no repeats of yesterday's rungs — LastRungSent guard held)
simulated Tuesday : 2 sent  (R4 escalation to chair x1, R1 x1)
extension request : ACT-0114 moved 2026-05-20 -> 2026-05-27, LastRungSent cleared, no escalation
total emails over 4 days: 11 for 18 actions   (naive daily loop would have sent 54)

=== Benefit claimed ===
Minutes and actions: 160 meetings/month × (45 min -> 12 min) = 88 h/month, 1,056 h/year
Minutes issued: 4.5 days after meeting -> same day (0.3 days)
Actions closed on time: 46% -> 79%
```

**Acceptance criteria**
- The decision test is in the prompt; extracted decisions match the gold minutes with no discussion recorded as a decision and no decision attributed to an individual member.
- Every decision and action carries a verbatim `evidence_quote` that is visible on the chair's approval card.
- Relative dates are anchored to the meeting date; an unstated deadline yields `null` with `date_basis: unstated` and routes to the secretary.
- `ActionItems` are created only after the chair approves; unapproved minutes generate no chases.
- The chase ladder sends each rung at most once, skips Friday and Saturday and holidays, and an extension request moves the date without escalation.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Minutes record decisions the committee never took | No decision test in the prompt | Add the three-part test and require `evidence_quote` |
| A member's question is minuted as a commitment | Same cause; no quote to check against | Evidence quote plus decisions-first approval card |
| Every deadline is a few days late | Relative dates anchored to the run time | Anchor to `meeting_date`; return `due_phrase` too |
| Owners get tasks that later change | Actions created from draft minutes | Gate creation on `MinutesApproved` |
| An owner receives 14 emails about one action | No rung memory | Store `LastRungSent`; send each rung once |
| Chases arrive on Friday | No working-day guard | Skip Friday/Saturday and the `PublicHolidays` list |
| Owner name does not match anyone | Directory match failed | Return `owner_email: null`; route to the secretary — never guess a recipient |

**Instructor notes.** Task 1 versus task 2 is the demonstration: run the same transcript twice and read the false decision `D3` aloud, then show the source line was a question. Ask the room what would have happened if the chair had approved it — the Mudawala case study answers that in the next section, so let the room arrive there first. Watch for pairs who add the evidence quote to the schema but do not surface it on the approval card; the quote is worthless if the chair cannot see it. Fast finishers: build the carry-forward — open actions from the previous meeting automatically appearing as agenda item 2 of the next. It is five actions long and it is the change that most alters a committee's behaviour.

## Mini Exercises

**Quiz (5 questions)**
1. State the three-part decision test. → settled outcome, an authority settled it, effect outside the room.
2. Why must a relative date be anchored to the meeting date? → anchoring to run time shifts every deadline by the processing delay.
3. What happens when no deadline was stated? → `due_date: null`, `date_basis: unstated`, routed to the secretary — never invented.
4. Why are action items created only after chair approval? → owners must not receive tasks from a draft that can still change.
5. How long is the transcript retained? → until seven days after the minutes are approved, then deleted — minimisation.

**Debugging exercise.** Provide a run where every action's due date is three days later than the gold minutes. Participants must find the `utcNow()` anchor and explain why the error was uniform and therefore invisible to spot-checking.

**Design exercise.** The committee wants dissent recorded whenever a member votes against. Specify the schema change, the prompt rule, the approval-card change, and the governance question you would raise before implementing it.

**Discussion questions.**
- Same-day minutes change how a committee behaves. Is that always an improvement? What is lost when there is no longer a four-day gap in which people reconsider?
- The transcript is deleted seven days after approval. A member later disputes a minute. Are you comfortable with the deletion policy, and what would change your mind?

## Case Study — The Commitment That Was Never Made at "Mudawala" (مداولة)

**Scenario.** "Mudawala" (مداولة), the secretariat of a national governance council in Riyadh, automated minutes for 22 standing committees. In month three, a directorate general disputed a minute recording that his directorate would fund a SAR 400,000 integration from its own budget. He had asked whether it could be funded that way. The minute said he had agreed.

**Business context.** Council minutes are cited across entities and are the basis of budget commitments. The directorate had been carrying the unfunded line for six weeks and had deferred two other commitments to accommodate it.

**Technical challenge.** The extraction prompt asked for "decisions and agreements" with no test for what constitutes one, and the schema required no evidence. The model, doing what a helpful summariser does, converted an interrogative into a declarative commitment. The chair had approved minutes presented as eleven paragraphs of continuous prose with decisions embedded in the flow of the text.

**Constraints.** The minute has been issued and cited in two subsequent meetings. Amending an issued council minute has its own procedure and creates a visible correction. The transcript still exists, which is fortunate here but sits uneasily against the retention policy the council had just adopted. Twenty-two committees are running on the same automation.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) the extraction fix — an explicit decision test, a mandatory verbatim `evidence_quote`, and never attributing decisions to individuals; (2) the *presentation* fix, which matters more, because the chair approved what he could not see: decisions and actions first, each beside its quote, discussion collapsed; (3) a re-run of three months of transcripts against the corrected extractor to find other converted interrogatives before someone else discovers them; (4) the uncomfortable retention discussion — the transcript saved them this time, and the room should sit with the tension between minimisation and evidential value rather than resolving it glibly; (5) the recognition that "the chair approved it" was never a control while the approval artefact was designed to be skimmed.

**Discussion questions.**
1. The chair approved the minutes. Why was that not a control, and what specifically makes an approval artefact reviewable?
2. The transcript resolved the dispute but the policy says delete it. Where would you set the retention period, and what is your justification to both the records officer and the legal directorate?
3. A model converting a question into a commitment is a predictable behaviour, not a freak event. What other predictable conversions should you test for before deploying a minutes extractor?
4. Twenty-two committees run on this automation. What is your rollout order for the fix, and what do you tell the other twenty-one chairs today?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Decision extraction precision | Quality | ≥ 95%, 0 discussion recorded as a decision | against gold minutes, 3 meetings |
| Actions with a verifiable evidence quote | Correctness | 100% | schema and card audit |
| Date resolution accuracy | Correctness | 100% of relative dates anchored to the meeting date; 0 invented deadlines | gold comparison |
| Actions created before approval | Governance | 0 | run-order audit |
| Hours saved per month (minutes) | Benefit | 88 h/month (1,056 h/year) | 160 × (45 → 12 min) |
| Actions closed on or before due date | Benefit | 46% → ≥ 75% | `ActionItems` closure dates |

**Example benchmark table (filled during lab):**

| Meeting | Gold decisions | Extracted (starter) | Extracted (with test) | Actions | Owners matched | Dates unstated |
|---|---|---|---|---|---|---|
| MIN-2026-041 | 5 | 9 (4 false) | 5 | 7 | 6 / 7 | 1 |
| MIN-2026-042 | 3 | 6 (3 false) | 3 | 5 | 5 / 5 | 0 |
| MIN-2026-043 | 8 | 11 (3 false) | 8 | 12 | 10 / 12 | 2 |
| **Total** | **16** | **26 (10 false)** | **16** | **24** | **21 / 24** | **3** |

## Required Visuals and Training Assets

### Diagrams
1. **Three artefacts, three lifetimes** — *Purpose:* the module's organising idea. *Elements:* transcript, minutes and actions as three boxes with different retention bars beneath them — 7 days after approval, permanent, until closed — and different approval markers. *Style:* three columns with a timeline bar under each.
2. **The decision test** — *Purpose:* the extraction judgement. *Elements:* four transcript snippets flowing through three gates (settled? authority? external effect?) with three falling out as discussion and one emerging as a decision. *Style:* filter cascade with the rejected snippets shown greyed.
3. **The chase ladder** — *Purpose:* humane escalation. *Elements:* four rungs with trigger, recipient and tone, plus two exits — action closed, and extension granted — and a weekend/holiday guard drawn across the bottom. *Style:* ascending staircase with exit arrows.
4. **The chair's approval card, before and after** — *Purpose:* presentation as a control. *Elements:* left, eleven paragraphs of prose; right, decisions and actions first with evidence quotes and discussion collapsed. *Style:* side-by-side UI mock-up with the disputed decision highlighted in both.

### Images (screenshots)
1. **A decision beside its evidence quote** — *why:* this is what makes the chair's approval real; *content:* the card row with the decision text and the verbatim transcript line beneath it.
2. **`ActionItems` with the chase ladder state** — *why:* shows the tracker working; *content:* the list with `LastRungSent`, `ChaseCount`, `ExtensionCount` and one escalated row.
3. **The working-day guard skipping Friday** — *why:* small detail, large adoption effect; *content:* the run history showing Friday's run terminating with zero sends.

### Simulations
1. **The interrogative commitment** — *Setup:* branch `sim-no-decision-test` on a transcript containing three questions phrased as suggestions. *Expected behaviour:* all three appear as decisions. *Learning objective:* summarisation converts questions into commitments unless explicitly forbidden.
2. **Chase spam** — *Setup:* daily loop with no rung memory over 18 actions for 14 days. *Expected behaviour:* 154 emails; owners begin filtering the sender. *Learning objective:* an automation people mute has a benefit of zero.

### Interactive Activities
- **Decision or discussion (12 min):** twenty transcript lines on cards; teams sort them and defend the borderline six. The disagreements map exactly onto where the model fails.
- **Design your ladder (15 min):** each team designs a chase cadence for a different action type — a statutory deadline, an internal courtesy request, a ministerial commitment — and defends the differences. The point is that one cadence does not fit all.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_meetings_3/transcripts/` | Synthetic Arabic-English committee transcripts, one containing the planted interrogative | TXT | 3 files, ~4,000 words each | Extraction and gold comparison |
| `injaz_meetings_3/gold_minutes/` | Human-written gold minutes with 16 decisions and 24 actions | JSON | 3 files | Precision and recall measurement |
| `attendee_directory.xlsx` | 41 committee members incl. two whose names do not match the transcript spelling | XLSX | 41 rows | Owner matching and the null path |
| `seeded_actions_18.xlsx` | 18 actions across all four rungs incl. one due Thursday | XLSX | 18 rows | Chase-ladder drill |
| `PublicHolidays.xlsx` | Saudi public holidays 2026–2027 | XLSX | 24 rows | Working-day guard |

### Demo Requirements
- **Instructor demo (8 minutes):** project the transcript line "could we absorb that within the directorate budget?" Run the starter extractor and show it emerge as a decision. Add the decision test and the evidence quote, re-run, and show it classified as discussion. Then show the two approval cards side by side and ask the room, honestly, which one they would actually read at 16:20 on a Thursday. That question is the module.

---

# Module 7 — Governance, Risk, and Responsible Automation: PDPL, Records Management, Audit Trails, and What Must Never Be Automated

## المحور السابع — الحوكمة والمخاطر والأتمتة المسؤولة

## Module Overview

**Purpose.** By this point participants have built six automations that read letters, draft replies to citizens, minute committee decisions and consolidate financial figures. This module makes them accountable for what they have built. It covers Saudi PDPL obligations for personal data in automated flows, records-management and retention of automated correspondence, audit trails that answer *who decided this*, connector data-residency and the agency boundary, and the hard list of decisions that must never be automated. The lab builds the last Injaz process — purchase-request intake — with the full governance wrapper from the start, saving **105 hours a month**.

**Business relevance.** A Saudi government automation that mishandles personal data is a PDPL matter for the entity, not a technical incident for the team. An automation that cannot say who authorised an outcome fails internal audit. And an automation that decides something a citizen may appeal against is administratively void regardless of how well it works. These three constraints determine what may be built at all — which is why they are taught before the programme scales in Module 8, and why they have appeared in every module since Hour 1.

**Industry use cases.**
- A ministry classifies every field in every automated flow as personal, sensitive or non-personal, and discovers that a "harmless" correspondence flow was copying national ID numbers into an email subject line.
- An authority applies a retention label to automated correspondence at creation, so the records officer's schedule is enforced by the platform rather than by an annual clean-up nobody performs.
- A shared-service centre publishes a one-page never-automate list, and it is the artefact most frequently cited by department heads proposing new automations — because it tells them what they *can* propose.

**Expected competencies.** After this module a participant can classify data in a flow against PDPL categories and identify a lawful basis; apply minimisation and retention to an automated process; build an audit trail that survives run-history expiry; name the accountable human for any automated outcome; assess whether a connector moves data outside the agency boundary; and apply the never-automate list to a proposal and defend the answer.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Classify data handled by a flow under PDPL and identify the lawful basis and minimisation obligations | LO7, CO4 |
| 7.2 | Apply records retention and disposition to automatically generated correspondence and records | LO7, CO4 |
| 7.3 | Build a durable audit trail that outlives platform run-history retention and answers "who decided" | LO7, CO4 |
| 7.4 | Assess connector data residency and what may cross the agency boundary | LO7, CO4 |
| 7.5 | Apply the never-automate list to a proposal and defend the boundary drawn | LO7, LO2, CO4 |
| 7.6 | Build a fully governed intake automation with threshold routing and an audit trail | LO3, LO7, CO2 |

## Technical Content

### 1. PDPL in an automated flow, concretely

Saudi Arabia's Personal Data Protection Law applies to the automations in this course from the first module. Five obligations translate directly into flow design decisions:

| PDPL obligation | What it means in a flow | Injaz implementation |
|---|---|---|
| **Lawful basis** | You must be able to state why the entity processes this personal data | Every automation register entry names a basis: performance of a public task, legal obligation, or explicit consent |
| **Purpose limitation** | Data collected for one purpose is not reused for another | The leave flow's employee data is not reused for the performance report |
| **Minimisation** | Collect and carry only what the process needs | The correspondence flow stores the sender's entity, not the signatory's national ID; the transcript is deleted after approval |
| **Retention limitation** | Personal data is kept only as long as needed | Retention labels applied at creation, not at clean-up |
| **Data subject rights** | Access, correction, and objection must be actionable | The audit trail makes it possible to find every automated record about a person, which is what makes a rights request answerable at all |

The design habit to install: **for every field a flow touches, ask whether the process would still work without it.** Most flows carry two or three personal fields purely because they were in the source payload, and each one is an obligation with no benefit.

### 2. The field-level data classification, done once per flow

```text
# injaz/governance/data-classification-purchase-intake.md
# Completed for EVERY automation before go-live. One row per field the flow touches.
# Classification: NP = non-personal | P = personal | SP = sensitive personal

field                    class  source            purpose                     retention   crosses boundary?
------------------------ -----  ----------------  --------------------------  ----------  -----------------
RequestId                NP     generated         identity of the record      10 years    no
RequesterName            P      Forms             routing + accountability     10 years    no
RequesterEmail           P      Forms             notification                 10 years    no
RequesterNationalId      SP     Forms             ** NOT NEEDED — REMOVED **   n/a         n/a
SectionCode              NP     directory         budget coding                10 years    no
ItemDescription          NP     Forms             procurement record           10 years    no
EstimatedValueSAR        NP     Forms             threshold routing            10 years    no
BudgetLine               NP     finance list      budget coding                10 years    no
SupplierSuggestion       NP     Forms             information only             10 years    no
AttachmentQuotation      NP*    Forms             completeness check           10 years    no
                                                  * may contain a supplier contact name -> treated as P
ApproverName             P      Approvals         accountability               10 years    no
ApproverDecision         NP     Approvals         accountability               10 years    no
ExtractedTextForAI       varies flow              completeness check           transient   ** REVIEW **

LAWFUL BASIS: performance of a public task (procurement of goods and services by a
              government entity under its mandate).
MINIMISATION FINDING: RequesterNationalId was collected by the paper form out of habit and
              is used by no step. Removed from the digital form. This is the whole exercise.
BOUNDARY FINDING: ExtractedTextForAI is sent to the LLM endpoint. It must therefore contain
              no personal data. Mitigation: extraction operates on the quotation's line items
              only; supplier contact blocks are stripped before the call. Verified in Lab 7 task 4.
RETENTION: 10 years from contract completion or request rejection, per the agency's records
              schedule series PR-04. Applied as a label at item creation.
```

### 3. Records management: retention applied at creation

An automation that creates official records creates a records-management obligation. Three rules:

1. **Label at creation, not at clean-up.** A retention label applied when the item is created is enforced by the platform; an annual review is enforced by nobody.
2. **Automated correspondence is correspondence.** A reply drafted by AI and signed by an officer enters the same record series as a typed letter. It is not a lesser artefact.
3. **Disposition must be as auditable as creation.** When a record reaches the end of its retention, the deletion is itself an event that is logged.

The subtlety worth an extra minute in class: the *transcript* in Module 6 and the *raw extraction text* in Module 3 are working copies, not records, and should have short retention — but only if the record they produced is complete enough to stand alone. If the minutes omit the evidence, the transcript quietly becomes the record, and deleting it destroys evidence. Completeness of the record is what earns you the right to delete the working copy.

### 4. Audit trails: who decided this?

Power Automate run history expires — 28 days by default. Any question asked after that ("who approved this purchase in March?") cannot be answered from the platform. Every Injaz flow therefore writes its own durable audit row. The minimum viable audit record answers six questions:

| Question | Field | Why it matters |
|---|---|---|
| What happened? | `Outcome`, `FlowName`, `FlowVersion` | Behaviour changes between versions; the version is part of the answer |
| To what? | `RecordReference` | Ties the audit row to the business record |
| When? | `OccurredOn` (UTC + AST) | Disputes are usually about sequence |
| Who triggered it? | `TriggeredBy` | The requester, or the schedule |
| **Who decided it?** | `DecidedBy`, `DecisionType` | The accountable human, or `system-rule` where a documented rule applied |
| On what basis? | `RuleApplied`, `SourceCited` | The delegation row, the threshold, the knowledge-base unit |

`DecidedBy` is the field that matters. If it ever reads `automation` for an outcome affecting a person's rights, entitlements or obligations, the design is wrong — not the logging.

### 5. Connector data residency and the agency boundary

Every connector is a door in the agency's perimeter. Three questions for each one, answered before it is used and recorded in the register: **where does the data physically go**, **is it retained there**, and **is it used to train anything**. Standard Microsoft 365 connectors operating within the tenant's region keep data inside the tenant boundary. HTTP connectors, third-party SaaS connectors and LLM endpoints may not. The controls: a tenant Data Loss Prevention policy that blocks non-approved connectors outright; a documented approval for each connector that leaves the boundary; and — the control participants can apply themselves — **minimise what is sent**, because a payload with no personal data in it raises far fewer questions than a residency argument.

### 6. What must never be automated

This list is not a technical judgement. It is administrative law and public accountability expressed as a design constraint. Injaz's published list, one page, cited by every proposal:

| Never automated | Why | What may be automated around it |
|---|---|---|
| **Eligibility denial** for a benefit, licence or service | The citizen has a right to a reasoned decision by an accountable official, and usually a right of appeal | Completeness checking, document gathering, drafting the reasoning for an officer, notification after the officer decides |
| **Disciplinary action** against an employee | A legal decision affecting a person's employment and reputation | Case-file assembly, deadline tracking, scheduling |
| **Procurement award** | Public money, competitive rights, and a statutory challenge route | Completeness, compliance checklists, threshold routing, evaluation scheduling, record creation |
| **Any decision with a statutory right of appeal** | An appeal must be against a decision a named official made | Everything up to the decision, and everything after it |
| **Adverse HR outcomes** — leave refusal, promotion refusal, termination | Affects entitlement; requires reasons | Validation, routing, chasing, recording |
| **Final classification of a citizen complaint as unfounded** | Closes a person's grievance | Triage, evidence gathering, drafting, tracking |

The framing that makes this land with a productivity-focused cohort: **the list does not shrink the automation opportunity, it locates it.** In every row, the removable typing, routing, chasing and copying is on the right-hand side, and it is where the hours are. Injaz's own scorecard proves it: 669 hours a month, with not one automated decision.

### 7. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Classify every field before you build; delete what the process does not need.*
- *Label retention at creation.* Anything else is an intention, not a control.
- *Run history is not an audit trail.* Write your own, durably.
- *`DecidedBy` is never `automation` for a decision affecting a person.*
- *Minimise the payload rather than argue about residency.*
- *The never-automate list is published, cited, and owned by a governance forum — not by the builder.*

**Common mistakes (each is planted in the Lab 7 starter)**
1. The purchase form collects the requester's national ID, which no step uses; it is then carried into the record and the notification email subject.
2. No retention label is applied; items accumulate indefinitely in a list holding personal data.
3. The audit row records `Outcome` but not `DecidedBy`, so an approval cannot be attributed after 28 days.
4. Requests below SAR 5,000 are auto-approved by a condition — an automated award, however small.
5. The completeness check sends the entire quotation PDF, including supplier contact details, to the LLM endpoint.
6. The flow version is not recorded on the audit row, so behaviour changes cannot be attributed to a release.

**Production considerations**
- Governance artefacts belong with the flow: classification, lawful basis, retention, boundary assessment and named owners are part of the solution package, not a separate document that ages.
- Review classification whenever the source form changes. A new form field is a new obligation.
- Test data must never be real personal data, including in a training tenant — this course's Day 1 rule, restated as a production rule.
- Where an automation's outcome is contested, the audit trail is the entity's defence. Design it for the person who will read it in two years without you.

### 8. Real-world example walkthrough

Narrate in five minutes. An authority automated small-value purchase approvals: anything under SAR 5,000 was approved automatically to relieve buyers of trivial paperwork. It was popular, it was fast, and it ran for fourteen months. An internal audit then observed that 41% of that year's requests were between SAR 4,500 and SAR 4,999 — against 6% in the two years before. Requests were being split. No individual had done anything provably improper, and no automated approval was individually wrong; the *rule* had created an incentive and removed the human who would have noticed the pattern. The remediation was not a better threshold. It was to stop automating the approval and instead automate everything around it: completeness, budget coding, routing, and a splitting-pattern alert that flags repeated same-supplier requests just below the threshold. Buyer touch-time still fell by three quarters. The lesson: **automating a decision removes the person who would have noticed the pattern, and the pattern is usually the point.**

## Code Examples

### The durable audit trail

```text
# injaz/registers/AutomationAuditLog — SharePoint list definition + write pattern
# Written by the FINALLY scope of every Injaz flow, on every path including failure.
# Outlives the 28-day run-history window. Retention: 10 years, label applied at creation.

FlowName          Single line of text    'purchase-request-intake'
FlowVersion       Single line of text    '1.4.0'   <- from an environment variable, bumped on release
RunId             Single line of text    @workflow()['run']['name']
RecordReference   Single line of text    'PR-2026-00318'
Outcome           Choice                 Succeeded | Failed | Blocked | Terminated-Duplicate
OccurredOnUtc     Date and Time          @utcNow()
OccurredOnAst     Single line of text    @formatDateTime(convertFromUtc(utcNow(),'Arab Standard Time'),'yyyy-MM-dd HH:mm')
TriggeredBy       Single line of text    the requester's UPN, or 'recurrence'
DecidedBy         Single line of text    the approver's UPN — or 'system-rule' ONLY for
                                         non-adverse, documented, reversible routing
DecisionType      Choice                 human-approval | system-rule | no-decision
RuleApplied       Single line of text    'DelegationMatrix row 14; threshold band 50k-250k'
SourceCited       Single line of text    'KB-SVC-0142 v3'  (drafting flows) or ''
PersonalDataTouched Choice               none | personal | sensitive-personal
RetentionLabel    Single line of text    'PR-04-10yr'

# --- The write, in the FINALLY scope (runs after TRY and CATCH, all statuses) ---
item/DecidedBy: @{coalesce(
    body('Start_threshold_approval')?['responses'][0]['responder']['userPrincipalName'],
    if(equals(outputs('Compose_DecisionType'), 'system-rule'), 'system-rule', 'none'))}

# --- The guard that must exist in every governed flow ---
@if(and(
      equals(outputs('Compose_DecisionType'), 'system-rule'),
      equals(outputs('Compose_OutcomeIsAdverse'), true)),
    'GOVERNANCE VIOLATION — adverse outcome decided by rule. Blocked.',
    'ok')
# 'GOVERNANCE VIOLATION' -> Terminate Failed, notify the automation governance forum.
# This guard exists so a future edit cannot quietly turn a routing rule into a decision.
```

### Threshold routing that routes but never awards

```text
# injaz/flows/purchase-request-intake/threshold-routing.txt
# Routes by SAR band. Every band ends at a NAMED HUMAN. There is no auto-approve branch.
# Bands are read from the ProcurementThresholds list, not hard-coded.

# --- Switch expression: the band, computed from a maintained list ---
@{first(filter(body('Get_thresholds')?['value'],
    and(lessOrEquals(item()?['MinSAR'], triggerOutputs()?['body/estimatedValueSAR']),
        greater(item()?['MaxSAR'],      triggerOutputs()?['body/estimatedValueSAR']))))?['BandCode']}

# BAND-A   SAR      0 -  50,000   -> Section Head            approval, SLA 24 h
# BAND-B   SAR 50,001 - 250,000   -> Department Director     approval, SLA 48 h
# BAND-C   SAR 250,001 - 1,000,000-> Procurement Committee   approval, SLA 5 working days
# BAND-D   SAR > 1,000,000        -> Tender Committee        approval, SLA per regulation
# DEFAULT  (value missing/non-numeric) -> ExceptionQueue, buyer notified. Never a band.

# --- REMOVED from the starter, deliberately: ---
# BAND-Z  SAR 0 - 5,000  -> auto-approve
#   This is an automated procurement award. It is on the never-automate list.
#   Replaced by BAND-A with a 24-hour SLA and a one-click approval card.
#   Buyer touch-time is unchanged; accountability is restored.

# --- Splitting-pattern detector (the control that replaces the auto-approve convenience) ---
# Get items: PurchaseRequests, Filter Query
SectionCode eq '@{triggerOutputs()?['body/sectionCode']}'
  and Created gt '@{addDays(utcNow(), -30)}'
  and EstimatedValueSAR ge 40000
  and EstimatedValueSAR lt 50000
# Condition: @greaterOrEquals(length(body('Get_near_threshold')?['value']), 3)
#   true -> flag the request for the internal-audit liaison, do NOT block it,
#           and record the flag on the audit row. A pattern is a question, not a verdict.

# --- Completeness check payload minimisation (boundary control) ---
# Send ONLY the line-item table to the LLM, never the whole quotation PDF:
@{body('Extract_table_from_quotation')?['lineItems']}
# Supplier contact block, signatures and letterhead are excluded before the call.
```

### The never-automate assertion, enforced in the solution

```text
# injaz/governance/never-automate-assertions.md
# A pre-go-live checklist completed by the builder and countersigned by the process owner.
# Any 'yes' in section A blocks deployment until the governance forum rules on it.

SECTION A — decision boundary (any YES blocks deployment)
[ ] Does any branch produce a refusal, denial or rejection affecting a person's
    entitlement, licence, benefit, or employment, without a named human approving it?
[ ] Does any branch award, allocate or commit public funds without a named human approving it?
[ ] Does any branch close, dismiss or classify-as-unfounded a citizen complaint or grievance?
[ ] Does any branch produce an outcome against which a statutory right of appeal exists?
[ ] Could DecidedBy ever be written as 'system-rule' for an adverse outcome?

SECTION B — data (any NO blocks deployment)
[ ] Has every field been classified NP / P / SP and unnecessary fields removed?
[ ] Is a lawful basis recorded in the automation register?
[ ] Is a retention label applied at item creation, not by later clean-up?
[ ] Has every connector been assessed for data residency and approved?
[ ] Is the payload sent outside the tenant free of personal data?

SECTION C — accountability (any NO blocks deployment)
[ ] Does the flow write a durable audit row on every path, including failure?
[ ] Does the audit row record DecidedBy, RuleApplied and FlowVersion?
[ ] Is a named business owner AND a named technical owner recorded in the register?
[ ] Does the CATCH scope notify a named person within 60 seconds?
[ ] Is there a documented manual fallback if the automation is unavailable for a week?

Signed (builder): ______________  Countersigned (process owner): ______________
Governance forum minute reference: ______________   Date: ______________
```

## Hands-on Lab 7 — Build the Governed Purchase-Request Intake

| | |
|---|---|
| **Objective** | Build the purchase-request intake flow with the governance wrapper from the start: field classification with minimisation, retention labels at creation, threshold routing that never awards, a splitting-pattern detector, payload minimisation at the boundary, a durable audit trail with `DecidedBy`, and a completed never-automate assertion; claim the 105 h/month saving |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab7_Start_1_0_0_1.zip` (creates `PurchaseRequests`, `ProcurementThresholds`, `AutomationAuditLog`, the intake Form with the national-ID field, and 90 days of seeded request history including a splitting pattern). Standard connectors only. |

**Instructions & tasks**

1. *(8 min)* Complete the field classification for all 13 fields. Identify `RequesterNationalId` as collected-but-unused, remove it from the form, the flow and the record, and note the finding. Record the lawful basis in the register.
2. *(8 min)* Build the completeness check and apply the retention label `PR-04-10yr` at item creation. Confirm the label is present on a newly created item before any human touches it.
3. *(10 min)* Build threshold routing from `ProcurementThresholds`. **Delete the starter's `BAND-Z` auto-approve branch** for requests under SAR 5,000 and replace it with `BAND-A` plus a 24-hour SLA. Confirm every band, including the default, terminates at a named human. Write one sentence in `LAB7_NOTES.md` on why a SAR 4,000 auto-approval is still an automated award.
4. *(8 min)* Apply payload minimisation: send only the extracted line-item table to the LLM, never the full quotation. Verify with a request whose quotation contains a supplier contact block, and confirm the block does not appear in the outbound payload.
5. *(11 min)* Build the durable audit row in `FINALLY` with `DecidedBy`, `RuleApplied` and `FlowVersion`, plus the governance guard that blocks an adverse outcome decided by rule. Test the guard by temporarily reintroducing an auto-reject branch and confirming deployment is blocked. Then run the splitting-pattern detector against the seeded history and confirm it flags `SEC-OPS` (four requests between SAR 44,000 and 49,500 in 30 days) without blocking anything.
6. *(5 min)* Complete and sign the never-automate assertion. Record: `feat(procurement): governed intake, no automated award, 105 h/month`.

**Expected output**
```text
=== Field classification ===
13 fields classified: NP 8 | P 4 | SP 1
MINIMISATION: RequesterNationalId (SP) removed — used by 0 steps, was carried into the
              record and the notification subject line. Form, flow and list updated.
LAWFUL BASIS: performance of a public task. Recorded in AutomationCandidates row 3.
RETENTION: PR-04-10yr applied at creation. Verified on PR-2026-00318 at t+0.4 s.

=== Threshold routing (60 seeded requests) ===
BAND-A  SAR 0-50,000        41 requests -> Section Head,          median approval 4 h 12 m
BAND-B  SAR 50,001-250,000  13 requests -> Department Director,   median approval 19 h 40 m
BAND-C  SAR 250,001-1M       5 requests -> Procurement Committee, median 3.1 working days
BAND-D  SAR > 1M             1 request  -> Tender Committee
DEFAULT (non-numeric value)  0 requests -> ExceptionQueue
auto-approved without a human: 0        <- the number this module exists to protect

=== Governance guard test ===
temporarily added auto-reject branch for incomplete requests
  -> Compose_DecisionType = 'system-rule', OutcomeIsAdverse = true
  -> guard fired: "GOVERNANCE VIOLATION — adverse outcome decided by rule. Blocked."
  -> run terminated Failed, governance forum notified. Branch removed.

=== Boundary check ===
outbound LLM payload for PR-2026-00318: 412 tokens, line items only
  supplier contact block present in source quotation : yes
  present in outbound payload                        : no
  personal data in outbound payload                  : none

=== Splitting-pattern detector, 90-day seeded history ===
SEC-OPS  4 requests SAR 44,200 / 47,900 / 49,500 / 46,100 in 30 days, same supplier
  -> flagged to internal-audit liaison, recorded on audit row, request NOT blocked
all other sections: no pattern

=== Audit trail ===
60 audit rows written, 60 with DecidedBy populated, 0 reading 'automation'
FlowVersion 1.4.0 stamped on all rows

=== Benefit claimed ===
Purchase-request intake: 350 requests/month × (24 min -> 6 min) = 105 h/month, 1,260 h/year
Cycle time (submission -> procurement record): 6.0 days -> 2.2 days

=== PORTFOLIO TOTAL AFTER LAB 7 ===
180 + 90 + 105 + 88 + 46 + 160 = 669 h/month | 8,028 h/year | 4.56 FTE | SAR 1,043,640
```

**Acceptance criteria**
- All 13 fields classified; the national-ID field removed from form, flow and record; lawful basis recorded.
- Retention label applied at item creation and verifiable before any human interaction.
- No branch approves, rejects or awards anything without a named human; the `BAND-Z` auto-approve is removed and the reasoning is written down.
- The outbound LLM payload contains no personal data and no supplier contact block.
- Every run writes an audit row with `DecidedBy`, `RuleApplied` and `FlowVersion`; the governance guard blocks an adverse system-rule outcome; the never-automate assertion is completed and countersigned.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| National ID appears in a notification subject line | Field collected out of habit and carried through | Remove from the form; re-run classification after any form change |
| Retention label missing on some items | Label applied by a later flow step that sometimes skips | Apply at creation in the same action, not afterwards |
| Cannot say who approved a March request | Only run history existed; it expired at 28 days | Write the durable audit row in `FINALLY` on every path |
| Requests cluster just under a threshold | An auto-approve band created an incentive | Remove the band; add the splitting detector; flag, do not block |
| Supplier contact details in the LLM payload | Whole PDF sent to the model | Send extracted line items only |
| "This connector is blocked by tenant policy" | DLP policy — correct behaviour, not a fault | Use the approved standard connector; if none exists, the design must change, not the policy |

**Instructor notes.** Task 3 divides the room. Removing the SAR 5,000 auto-approve feels to many participants like removing the point of the automation, and the argument that follows is the most valuable twenty minutes of Day 4. Let it run. Land it with the numbers: buyer touch-time falls from 24 minutes to 6 either way, so the auto-approve bought almost nothing and cost accountability entirely. Second watch-point: participants who complete the never-automate assertion without reading it. Pick two at random and ask them to justify a specific tick. Fast finishers: audit one of their *own* earlier labs — Lab 3 or Lab 4 — against Section A of the assertion. Most cohorts find at least one participant whose Lab 3 flow auto-closes low-confidence correspondence, which is a small but real decision.

## Mini Exercises

**Quiz (5 questions)**
1. What is the first PDPL question to ask about a field in a flow? → would the process still work without it (minimisation)?
2. Why is run history not an audit trail? → it expires (28 days by default); audit questions arrive later.
3. What must `DecidedBy` never say for an adverse outcome? → `automation` or `system-rule`.
4. Give two things that must never be automated and say what may be automated around them. → e.g. eligibility denial (automate completeness, gathering, drafting, notification) and procurement award (automate compliance checks, routing, scheduling, record creation).
5. What is the cheapest control against a connector data-residency problem? → minimise the payload so nothing personal leaves.

**Debugging exercise.** Provide a flow whose audit row lacks `DecidedBy` and whose approval action was replaced six months ago with a condition. Participants must determine, from the artefacts alone, whether any outcome was decided without a human — and then explain why they cannot be sure, which is the finding.

**Design exercise.** A department proposes automating the rejection of leave requests that exceed the employee's balance, arguing it is arithmetic, not judgement. Write the governance forum's response: what may be automated, what may not, and what the officer's card should show.

**Discussion questions.**
- Removing the SAR 5,000 auto-approve costs almost no time and restores accountability. Why do organisations resist this so strongly, and what argument actually works?
- The splitting detector flags a pattern but blocks nothing. Is a control that only raises a question a real control? What would change your answer?

## Case Study — The Records That Could Not Be Explained at "Sijil" (سجل)

**Scenario.** "Sijil" (سجل), the records and archives function of a Saudi government entity in Madinah, was asked by an oversight body to produce, for a twelve-month period, every outgoing communication generated with AI assistance, who approved each one, and the source each was based on. The entity had eleven such automations running across six departments.

**Business context.** The request was routine oversight, not an investigation. The entity had thirty days to respond. Sijil is accountable for the completeness of the entity's records.

**Technical challenge.** Nine of the eleven automations wrote no durable audit record. Their run histories retained 28 days. Six months of approvals existed only as Approvals-connector history, which had also aged out for the earlier period. Three flows had been edited without version stamping, so the entity could not state which logic produced which output. One flow, built by a department that had since restructured, had no identified owner at all.

**Constraints.** The response cannot be "we do not know" without consequence. Reconstructing records retrospectively is not possible where the data was never written. The entity must respond in thirty days and must also say what it will do differently — and that second part is the one the oversight body will actually assess.

**Solution approach (facilitate, don't lecture).** Guide toward: (1) separate what is genuinely recoverable — outgoing items themselves exist in mailboxes and lists — from what is not, namely the approval and provenance chain, and be precise about the boundary rather than vague; (2) respond with an honest gap statement plus a dated remediation plan, which is a far stronger position than a padded partial answer; (3) the remediation is a mandatory audit-row standard applied to all eleven flows, retro-fitted within weeks, plus version stamping and named owners in a register; (4) the ownerless flow raises the harder question of how an automation came to exist with no owner, which is a provisioning and change-control failure, not a records failure; (5) note that Sijil's own position improves permanently — after this, the entity has an artefact it never had before, which is why the oversight request is best treated as a gift rather than an attack.

**Discussion questions.**
1. What exactly is recoverable and what is permanently lost? Draw the line precisely and say how you would evidence each side of it.
2. An honest gap statement with a remediation plan versus a padded partial answer — which serves the entity better, and what does your answer say about institutional maturity?
3. One flow had no owner. How does that happen, and what provisioning control prevents it?
4. What is the minimum audit standard you would mandate entity-wide tomorrow, knowing that anything too heavy will be quietly ignored?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Fields classified and minimised | Governance | 100% classified; unnecessary personal fields removed | classification document |
| Retention labels at creation | Governance | 100% of created items | list audit at t+0 |
| Audit rows with `DecidedBy` | Governance | 100%; 0 reading `automation` | audit log query |
| Automated adverse decisions | Governance | 0 | never-automate assertion + branch audit |
| Personal data in outbound payloads | Governance | 0 | payload inspection |
| Hours saved per month (purchase intake) | Benefit | 105 h/month (1,260 h/year) | 350 × (24 → 6 min) |

**Example benchmark table (filled during lab):**

| Governance control | Before (starter) | After (Lab 7) | Evidence |
|---|---|---|---|
| Sensitive fields carried | 1 (national ID) | 0 | classification table |
| Retention labelled at creation | 0% | 100% | item inspection at t+0.4 s |
| Audit rows with `DecidedBy` | 0 / 60 | 60 / 60 | audit log |
| Auto-approved requests | 27 / 60 (BAND-Z) | 0 / 60 | routing report |
| Personal data in LLM payload | present | none | payload diff |
| Splitting patterns detected | not detected | 1 (SEC-OPS) flagged | detector output |

## Required Visuals and Training Assets

### Diagrams
1. **The agency boundary** — *Purpose:* make residency physical. *Elements:* a perimeter around the tenant with each connector drawn as a door; standard M365 connectors inside, an LLM endpoint and an HTTP connector as doors in the wall, each labelled with what passes through and what has been stripped. *Style:* castle-wall metaphor, deliberately literal.
2. **The never-automate line** — *Purpose:* the module's central artefact. *Elements:* six process rows, each split by a vertical red line, with removable work (typing, routing, chasing, copying) on the left and the protected decision on the right, and the hours figure printed on the left side of each row. *Style:* split table, hours prominent — the point is that the benefit lives on the automatable side.
3. **Audit trail versus run history** — *Purpose:* the durability argument. *Elements:* a 28-day run-history bar next to a 10-year audit-row bar, with an audit question arriving at month nine landing in the gap. *Style:* two timelines with a question mark at the failure point.
4. **Field classification flow** — *Purpose:* the pre-build routine. *Elements:* each field passing through "is it needed?" → "is it personal?" → "does it cross the boundary?" with the national-ID field visibly falling out at the first gate. *Style:* decision tree.

### Images (screenshots)
1. **A retention label applied at creation** — *why:* proves the control is real, not intended; *content:* the item properties showing the label at a timestamp before any human action.
2. **The governance guard blocking a run** — *why:* shows a control acting; *content:* the terminated run with the `GOVERNANCE VIOLATION` message.
3. **The splitting-pattern flag** — *why:* pattern detection replacing an auto-approve; *content:* the four near-threshold requests with the audit-liaison flag.

### Simulations
1. **Threshold splitting** — *Setup:* branch `sim-band-z` with auto-approve under SAR 5,000, run against 12 months of synthetic requests. *Expected behaviour:* the distribution piles up just under the threshold. *Learning objective:* an automated decision removes the person who notices patterns.
2. **The expired audit question** — *Setup:* ask participants to determine who approved a specific request from 90 days ago using only run history. *Expected behaviour:* impossible. *Learning objective:* durability is a design decision made before you need it.

### Interactive Activities
- **Red-line card sort, round two (15 min):** the same twenty cards from Module 1, re-sorted now that participants have built six automations. Compare against the Day 1 photograph of their first sort; the movement in the room's judgement is the assessment.
- **Classify a real flow (15 min):** each participant classifies the fields of one of their own earlier labs and identifies at least one field to remove. Most find one.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `purchase_requests_90d.xlsx` | 90 days of synthetic requests with a seeded SEC-OPS splitting pattern | XLSX | 60 rows | Routing, detector and audit measurement |
| `ProcurementThresholds.xlsx` | Four SAR bands with approvers and SLAs | XLSX | 4 rows | Threshold routing from data, not code |
| `quotation_samples/` | Supplier quotations incl. contact blocks and letterheads | PDF | 8 files | Payload minimisation exercise |
| `records_schedule_PR04.pdf` | Synthetic agency records schedule for procurement | PDF | 3 pages | Retention justification |
| `never_automate_list_v2.pdf` | The published one-page list | PDF | 1 page | Assertion, card sort, and take-home artefact |

### Demo Requirements
- **Instructor demo (8 minutes):** open the `AutomationAuditLog` and ask the room to tell you who approved `PR-2026-00214`. They can. Then open the platform run history for the same request from 90 days ago and show it is gone. Then delete the `DecidedBy` value on one row and ask the same question again. Three states — durable, expired, incomplete — in eight minutes, and the room will never again treat the audit row as optional paperwork.

---

# Module 8 — Measuring, Sustaining, and Scaling: Benefits Realisation and Building an Agency Automation Practice

## المحور الثامن — القياس والاستدامة والتوسع

## Module Overview

**Purpose.** Injaz now has seven working automations returning 669 hours a month. This module makes that claim *provable*, makes the portfolio *survivable*, and makes the practice *scalable*. It covers benefits realisation against the Day-1 baseline, touch-time instrumentation, the automation register as an operating asset, ownership models, handover documentation that survives its author's transfer, and a five-level maturity model for an agency automation practice. The lab builds the benefits dashboard and one complete handover pack.

**Business relevance.** The most common cause of death for a government automation is not failure — it is the transfer of the person who built it. The second most common is the inability to prove value when budgets are reviewed. Both are solved by artefacts that take a morning to produce and are almost never produced. This module is where a participant stops being someone who built a flow and becomes someone who runs a practice.

**Industry use cases.**
- A ministry's automation office reports quarterly to its executive committee in hours, SAR and cycle time against a signed baseline, and its funding has never been questioned.
- An authority mandates a handover pack before any automation goes live; when a builder transfers, the successor is productive in two hours instead of rebuilding from scratch.
- A shared-service centre uses a maturity model to decide, deliberately, that it is at level 2 and that the correct next investment is a register and a governance forum — not more flows.

**Expected competencies.** After this module a participant can instrument an automation to measure its own benefit; build a before/after benefits dashboard against a signed baseline; distinguish credible from inflated benefit claims; operate an automation register with business and technical owners; produce a handover pack; and place an organisation on a maturity model and name its next correct investment.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 8.1 | Instrument automations to measure touch-time, cycle time, exception and rework rates | LO8, CO2 |
| 8.2 | Build a benefits dashboard comparing actuals against a signed baseline | LO8, CO2 |
| 8.3 | Distinguish a credible benefits claim from an inflated one and state what each contains | LO8, LO2, CO2 |
| 8.4 | Operate an automation register with named business and technical owners | LO8, LO7, CO4 |
| 8.5 | Produce a handover pack sufficient for a successor to operate the automation unaided | LO8, CO4 |
| 8.6 | Place an organisation on a maturity model and identify its next correct investment | LO8, CO4 |

## Technical Content

### 1. Measuring what you claimed

The Day-1 baseline was 920 hours a month across six processes, signed by the process owners. The claim is 669 hours saved. Proving it requires measuring four things, and only the first is about hours.

| Measure | Definition | How Injaz captures it | Trap |
|---|---|---|---|
| **Touch-time per case** | Human minutes actually spent | Sampled quarterly by stopwatch on 30 cases per process — not estimated, not inferred from timestamps | Timestamps measure elapsed time, not attention |
| **Cycle time** | Intake to completion | Automatically, from record timestamps | Improving cycle time while touch-time is unchanged means you removed waiting, not work |
| **Exception rate** | Share of cases needing human rescue | From the exception queues | A falling hours claim with a rising exception rate means work moved, not disappeared |
| **Rework rate** | Share of outputs corrected after completion | From edit and rejection logs | Rework is where quality claims go to die |

**The residual rule:** an automation's claim is `volume × (before − after)`, where `after` is measured, not designed. Injaz's designed `after` for correspondence triage was 3 minutes; the measured figure in month three was 3.4 minutes, and the claim was restated at 168 hours a month rather than 180. That downward restatement is the single most credibility-building act available to an automation programme.

### 2. What a credible benefit claim contains

| Element | Credible claim | Inflated claim |
|---|---|---|
| Baseline | Measured before build, signed by the process owner | Reconstructed afterwards from memory |
| After-state | Measured in production, sampled | Assumed equal to the design target |
| Residual human time | Stated explicitly and non-zero | Omitted or zero |
| Wait-time | Reported separately as cycle time | Added to the hours saved |
| Exception rate | Reported alongside | Not mentioned |
| Redeployment | Named — what the freed hours now do | "Efficiency gains" |
| Restatements | Shown, with reasons | Never restated downward |

### 3. The automation register as an operating asset

The register created in Module 1 as a scoring list becomes, by Module 8, the operating record of the practice. Every automation carries: a business owner (accountable for the process and the benefit) and a technical owner (accountable for the flow working); the lawful basis, retention label and boundary assessment from Module 7; the baseline and the current measured benefit; the run success rate and exception rate; the review date; and the handover pack link. **An automation without both named owners is switched off at the next review.** That rule, enforced twice, permanently changes provisioning behaviour.

### 4. Handover documentation that survives a transfer

The test is brutal and simple: **can a competent colleague who has never seen this automation operate it, fix a common failure, and explain it to an auditor, using only the pack?** Seven sections, roughly four pages:

1. **What it does and why**, in the process owner's language, with the SIPOC and swimlane from Module 1.
2. **The surviving human decision** — who decides what, and what the automation must never do.
3. **How it runs** — trigger, schedule, dependencies, connections and the service account.
4. **Where it can break** — the four most likely failures with symptom, cause and fix (the lab troubleshooting table, promoted to production).
5. **The manual fallback** — exactly how the process runs for a week without the automation. Every pack must have one; an automation with no fallback is a single point of failure for a government service.
6. **Governance** — classification, lawful basis, retention, boundary assessment, never-automate assertion.
7. **Change history** — versions, what changed, who approved.

### 5. The maturity model

| Level | Name | Characteristics | Next correct investment |
|---|---|---|---|
| **1** | Individual | Enthusiasts build flows on personal accounts; nothing is registered; benefit is anecdotal | A register and a service-account standard — not more flows |
| **2** | Repeatable | A register exists; some flows have owners; baselines are inconsistent | Mandatory baselines and a governance forum |
| **3** | Governed | Every automation registered with owners, classification, retention and an audit trail; benefits measured against signed baselines | A reusable component library and a citizen-developer training path |
| **4** | Scaled | A community of builders with shared components, standards and a support model; a benefits dashboard reviewed by the executive | Portfolio-level prioritisation; process redesign before automation |
| **5** | Optimising | Automation is the default consideration in process design; benefits are redeployed deliberately; the practice retires automations as readily as it builds them | Continuous re-baselining and workforce-capability planning |

The most common and most expensive error is a level-1 organisation buying level-4 tooling. Injaz at the end of this course is at **level 3**, and its next investment is a component library and a citizen-developer path — not another twenty flows.

### 6. The horizon, briefly and honestly

Participants will be asked about agentic automation — systems that plan multi-step work rather than executing a fixed flow. Say three things. It is real and it is arriving in the same platforms they used this week. It changes the *builder's* job more than the *governance*: an agent that can act still needs a named accountable human, an audit trail, a never-automate boundary and a payload that respects the agency perimeter — everything in Module 7 applies unchanged and matters more. And the correct sequencing for a government entity is to reach maturity level 3 on deterministic flows first, because an organisation that cannot say who approved a purchase order will not be able to say why an agent did something. For those continuing, `SDA-AIE-240` (Vibe Coding) is the building path and `SDA-DSC-212` the analytics path.

### 7. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Measure the after-state; never assume the design target.*
- *Restate downward when the evidence says so.* It buys more credibility than any dashboard.
- *Two named owners or the automation is switched off.*
- *Every automation has a written manual fallback.*
- *Report exception rate beside hours saved, always, on the same screen.*
- *Buy tooling for the maturity level you have, not the one on the slide.*

**Common mistakes (each is planted in the Lab 8 starter)**
1. The dashboard shows hours saved with no exception-rate tile, so a growing queue is invisible beside a growing benefit.
2. The after-state touch-time is the design target rather than the sampled measurement, overstating the portfolio by 6%.
3. Cycle-time improvement is added to hours saved, inflating the claim by 3,100 hours a year.
4. Two automations have a technical owner but no business owner, so nobody is accountable for whether they still matter.
5. The handover pack has no manual fallback section, so an outage becomes a service outage.
6. The register's benefit figures are typed in manually and have not been updated since go-live.

**Production considerations**
- Re-baseline annually; a two-year-old baseline defended today is a liability.
- Review the register quarterly and **retire** automations whose process has changed. A practice that never retires anything is accumulating liability, not value.
- Publish the dashboard internally. Departments propose better candidates when they can see what good looks like.
- Track builder capability as an asset: the number of trained builders and the bus factor of each automation are portfolio risks.

### 8. Real-world example walkthrough

Narrate in five minutes. An automation office reported 14,000 hours a year saved and won an award. Eighteen months later a new director asked what those hours were now doing. Nobody could say. The baseline had been reconstructed after the fact, the after-state was the design target, wait-time was included, and no exception rates had ever been reported. An independent review re-measured four of the eleven automations and found real savings of about 5,200 hours a year — genuinely valuable, and about a third of the claim. The programme's funding survived, its credibility did not, and every subsequent number it produced was discounted by everyone who read it. The lesson, and the last one of the course: **an honest 5,200 defended with evidence is worth more than an unverifiable 14,000, because the honest number is the one you can still spend next year.**

## Code Examples

### Instrumenting an automation to measure itself

```text
# injaz/flows/_shared/benefit-instrumentation.txt
# Added to every Injaz flow. Writes one row per case to BenefitTelemetry.
# Automatic fields are timestamps; touch-time is SAMPLED, never inferred.

# --- Written by the FINALLY scope of each flow ---
ProcessName        'correspondence-triage'
RecordReference    @{outputs('Compose_Reference')}
IntakeAt           @{triggerOutputs()?['body/receivedDateTime']}
AutomationDoneAt   @{utcNow()}
HumanTouchStartAt  @{body('Start_officer_confirmation')?['createdDate']}
HumanTouchEndAt    @{body('Start_officer_confirmation')?['completionDate']}
Outcome            @{result('TRY')[0]?['status']}
ExceptionRouted    @{if(equals(outputs('Compose_Route'),'exception'), 1, 0)}
ReworkFlag         0     # set to 1 later by the correction flow if the output is amended
FlowVersion        @{parameters('flowVersion')}

# --- Derived in Power BI, not in the flow ---
CycleTimeHours     = (AutomationDoneAt - IntakeAt) / 3600
ApprovalWaitHours  = (HumanTouchEndAt - HumanTouchStartAt) / 3600
#   NOTE: ApprovalWaitHours is WAIT time. It is NOT touch-time and NEVER enters the
#   hours-saved calculation. It belongs to the cycle-time story only.

# --- Touch-time: the quarterly sampling protocol (this is the honest part) ---
# 30 cases per process, 10 each from 3 officers, stopwatch, median.
# Recorded in TouchTimeSamples: ProcessName | SampledOn | OfficerId | CaseRef | Minutes
# The dashboard reads the MEDIAN OF THE LATEST SAMPLE, never the design target.

# --- The claim, computed from measured values only ---
HoursSavedPerMonth = MonthlyVolume * (TouchBeforeMedian - TouchAfterMedian) / 60
# Correspondence triage, Q3 sample:
#   1,200 * (12.0 - 3.4) / 60 = 172 h/month   <- restated down from the designed 180
```

### The benefits dashboard specification

```text
# injaz/dashboard/InjazBenefits.pbix — page 1 "Portfolio", tile specification
# Data sources: BenefitTelemetry, TouchTimeSamples, AutomationCandidates (baseline),
#               ExceptionQueue, DraftEditLog, FlowFailures.

TILE 1  Hours saved per month (measured)      big number + 12-month trend
        = SUM over processes of MonthlyVolume * (TouchBefore - TouchAfterMeasured) / 60
        Q1 design claim 669  ->  Q3 measured 651   (shown together, both labelled)

TILE 2  Annual value SAR                      = HoursSavedPerYear * 130
        651 * 12 * 130 = SAR 1,015,560         (design claim was SAR 1,043,640)

TILE 3  Exception rate by process             bar, MANDATORY beside tile 1
        correspondence 7.5% | enquiry 9.2% | purchase 4.1% | leave 2.8%
        Red threshold at 12%. A rising bar beside a rising tile 1 is the alarm.

TILE 4  Cycle time before / after             dumbbell chart, hours — NOT added to tile 1
        correspondence 3.2d -> 0.4d | leave 4.5d -> 1.1d | enquiry 5.0d -> 1.4d
        purchase 6.0d -> 2.2d | minutes 4.5d -> 0.3d | report Wed(var) -> Sun 08:00

TILE 5  First-pass quality                    enquiry first-pass approval 74.2%
                                              classification accuracy 92.5%
                                              rework rate 3.1%
TILE 6  Run health                            success rate 99.2% | failures notified <60s 100%
TILE 7  Register health                       7 automations | 7 with both owners
                                              | 7 with handover packs | 0 past review date
TILE 8  Redeployment                          named destinations for the freed capacity:
        "case-file quality review (2.1 FTE), citizen outreach (1.2 FTE),
         records digitisation backlog (1.3 FTE)"   <- typed by the department head, quarterly

RULE ENFORCED IN THE MODEL: tiles 1 and 3 cannot be filtered independently. Anyone who
sees the benefit sees the exception rate. This is a design decision, not a limitation.
```

### The handover pack template

```text
# injaz/handover/HANDOVER-correspondence-triage-v1.4.md
# Four pages. Test: a competent colleague operates, fixes and explains it from this alone.

1. WHAT IT DOES AND WHY
   Triages incoming official correspondence: classifies, summarises, suggests an owner and
   due date, creates the register entry. 1,200 letters/month. Baseline 12.0 min/letter
   (signed by Head of Correspondence, 2026-05-04). Measured after: 3.4 min. 172 h/month.
   Attached: SIPOC, swimlane, signed baseline.

2. THE SURVIVING HUMAN DECISION
   The department head confirms ownership and may reassign. The automation NEVER assigns
   final ownership, never closes a letter, and never decides an SLA breach is acceptable.
   Never-automate assertion signed 2026-05-14, forum minute GOV-2026-11.

3. HOW IT RUNS
   Trigger: new mail in correspondence@agency.gov.sa (event).
   Connections: SharePoint, Outlook, Approvals, OCR — all on svc-injaz-flows@agency.gov.sa.
   Dependencies: CorrespondenceRegister, CorrespondenceExceptions, label_set_v3,
   correspondence_extract.schema.json v2. Runs ~40x/working day. Version 1.4.0.

4. WHERE IT BREAKS (top four, from 6 months of FlowFailures)
   Symptom                          Cause                        Fix
   Empty extraction, green run      triage threshold too low     raise char test; check OCR quota
   Parse JSON fails                 model returned a fence       fence-strip Compose is action 7
   Exception queue growing >12%     letter styles drifted        re-measure on gold set; retune prompt
   All runs fail 401                service account password     rotate + reconnect all 4 connections

5. MANUAL FALLBACK (one week without the automation)
   Officers triage from the shared mailbox using the printed label set and SLA table
   (Annex B) and enter the register manually. Capacity: 3 officers x 1,200 letters =
   240 h/month, i.e. the pre-automation state. Notify the Head of Correspondence on day 1.

6. GOVERNANCE
   Lawful basis: performance of a public task. Classification: 11 fields, 3 personal,
   0 sensitive. Retention: CR-02-perm on register entries; extraction text transient (7 days).
   Boundary: extracted text only to the LLM endpoint; no personal data. Assessed 2026-05-14.

7. CHANGE HISTORY
   1.0.0 2026-05-14 initial      | 1.2.0 2026-06-02 uncertain threshold 0.70 -> 0.75
   1.3.0 2026-07-11 fence-strip  | 1.4.0 2026-08-19 owner enum + DG Office
   Business owner: Head of Correspondence. Technical owner: Senior Coordinator, Shared Services.
   Reviewed quarterly; next review 2026-11-19.
```

## Hands-on Lab 8 — Benefits Dashboard, Register, and Handover Pack

| | |
|---|---|
| **Objective** | Instrument all seven Injaz automations, run the touch-time sampling protocol, build the eight-tile benefits dashboard against the signed baseline, complete the automation register with both owners for every automation, and produce one full handover pack that passes the successor test |
| **Duration** | 50 minutes |
| **Setup** | Import `Injaz_Lab8_Start_1_0_0_1.zip` (creates `BenefitTelemetry`, `TouchTimeSamples` with three quarters of seeded samples, and the starter dashboard with the six planted defects). Power BI Desktop or the Power BI service; the register from Lab 1 carried forward. |

**Instructions & tasks**

1. *(8 min)* Add the instrumentation block to two of your existing flows and confirm `BenefitTelemetry` rows appear with intake, automation-done and human-touch timestamps. Verify that `ApprovalWaitHours` is computed but excluded from the hours calculation.
2. *(9 min)* Load `TouchTimeSamples` and compute the measured after-state median per process. The starter dashboard uses design targets; switch it to measured medians and observe the portfolio claim fall from 669 to 651 hours a month. Write one sentence on why you would present the lower number.
3. *(9 min)* Fix the inflated claim: the starter adds cycle-time improvement to hours saved, adding 3,100 hours a year. Remove it and move cycle time to its own tile. Confirm the annual figure returns to SAR 1,015,560.
4. *(8 min)* Add the exception-rate tile and enforce the model rule that tiles 1 and 3 cannot be filtered independently. Test it by filtering to correspondence only and confirming both tiles move together.
5. *(11 min)* Complete the register: both named owners for all seven automations (two are missing a business owner), review dates, and handover links. Then write the full handover pack for one automation and hand it to another pair, who must answer three questions from it alone: how does it run, what is the manual fallback, and what must it never do.
6. *(5 min)* Place Injaz on the maturity model with evidence, and name the next investment. Record: `feat(practice): benefits dashboard + register + handover, 651 h/month measured`.

**Expected output**
```text
=== Touch-time sampling, Q3 (30 cases per process) ===
process                 designed after   measured after   claim (design)  claim (measured)
correspondence triage        3.0 min          3.4 min          180 h/mo        172 h/mo
citizen enquiry              3.0 min          3.1 min          160 h/mo        157 h/mo
purchase intake              6.0 min          6.2 min          105 h/mo        104 h/mo
leave routing                2.0 min          2.0 min           90 h/mo         90 h/mo
minutes and actions         12.0 min         12.4 min           88 h/mo         87 h/mo
weekly report              210    min        222    min           46 h/mo         41 h/mo
PORTFOLIO                                                       669 h/mo        651 h/mo
                                                              8,028 h/yr      7,812 h/yr
                                                          SAR 1,043,640   SAR 1,015,560
Restatement: -18 h/month (-2.7%). Reason: measured residual exceeds design in 5 of 6
processes, chiefly officer confirmation time on the correspondence and report flows.

=== Dashboard defects corrected ===
1 exception-rate tile missing              -> added, locked to tile 1
2 after-state = design target              -> switched to sampled median (-18 h/mo)
3 cycle time added to hours saved          -> removed (-3,100 h/yr inflation)
4 business owner missing on 2 automations  -> assigned; both would have failed review
5 handover pack has no fallback section    -> added; 7/7 packs now complete
6 register benefits typed manually         -> bound to BenefitTelemetry

=== Portfolio health ===
automations 7 | both owners 7/7 | handover packs 7/7 | past review date 0
run success 99.2% | failures notified <60s 100% | exception rate 5.9% portfolio
rework rate 3.1% | classification accuracy 92.5% | first-pass approval 74.2%
redeployment named: case-file quality review 2.1 FTE, citizen outreach 1.2 FTE,
                    records digitisation backlog 1.3 FTE   (total 4.6 FTE)

=== Maturity assessment ===
Level 3 (Governed). Evidence: register complete with owners, classification and retention
on all 7; audit trails durable; benefits measured against signed baselines; forum operating.
NOT level 4: no shared component library, no citizen-developer path, no executive review cadence.
Next investment: component library + citizen-developer training — NOT more flows.

=== Successor test ===
pack handed to pair 4: all three questions answered correctly from the pack alone in 6 min.
```

**Acceptance criteria**
- Instrumentation writes telemetry per case; wait-time is computed but excluded from hours saved.
- The dashboard reports the **measured** after-state, showing 651 h/month and SAR 1,015,560, with the design claim shown alongside and the restatement explained.
- Cycle time appears only on its own tile; the exception-rate tile cannot be filtered away from the benefit tile.
- All seven automations have both named owners, a review date and a handover link; no automation would fail a review.
- The handover pack passes the successor test: another pair answers how it runs, the manual fallback, and what it must never do, from the pack alone.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Claim is 8,028 h/yr but sampling says otherwise | Dashboard using design targets | Bind to the median of the latest `TouchTimeSamples` |
| Annual figure ~3,100 h too high | Cycle-time improvement added to hours saved | Separate tiles; wait-time is never hours saved |
| Growing queue invisible beside growing benefit | No exception tile / independently filterable | Add the tile and lock the filter relationship |
| Two automations have no accountable business owner | Register never enforced it | Make both owner fields mandatory; enforce at quarterly review |
| Successor cannot answer "what happens if it stops?" | No manual fallback section | Every pack must carry one; it is not optional for a public service |
| Register benefits are stale | Manually typed | Bind the register's benefit column to telemetry |

**Instructor notes.** Task 2 is the ethical centre of the course. Some participants will resist reporting 651 when 669 is defensible on paper — walk the room and ask each pair what happens to every future number they publish if someone else re-measures first. Task 5's successor test is the most reliable assessment instrument in this package: a pack that cannot answer three questions in six minutes is not a handover pack, regardless of length. Fast finishers: run the maturity assessment on their *own* agency, with evidence for the level claimed, and bring it to the capstone demo. This is the item most likely to turn into a real programme when they return to work.

## Mini Exercises

**Quiz (5 questions)**
1. Why must the after-state be measured rather than assumed? → the residual human time is almost always larger than the design target; assuming it overstates the claim.
2. Where does cycle-time improvement belong? → its own metric; never added to hours saved.
3. Why must exception rate sit beside hours saved? → a rising exception rate means work moved to a queue rather than disappearing.
4. What happens to an automation with only a technical owner? → it is switched off at the next review; nobody is accountable for whether it still matters.
5. What does a level-1 organisation most need? → a register and a service-account standard — not more flows or better tooling.

**Debugging exercise.** Provide a dashboard claiming 11,400 hours a year for a six-automation portfolio. Participants must find the three inflations — wait-time included, design targets used, one automation counted twice under two names — and produce the corrected figure with a one-paragraph restatement note.

**Design exercise.** Design the quarterly review agenda for the Injaz automation forum: what is reviewed, what evidence is required, what decisions can be taken, and what specifically causes an automation to be retired.

**Discussion questions.**
- Restating a benefit downward is professionally uncomfortable and institutionally rare. What would have to be true of your organisation for it to be safe? Can you create any of that yourself?
- If freed capacity is not visibly redeployed to named work, has the programme delivered value? What is the honest answer, and what does it mean for how you report next quarter?

## Case Study — The Award-Winning Number at "Irtiqa" (ارتقاء)

**Scenario.** "Irtiqa" (ارتقاء), the automation centre of excellence of a Saudi ministry in Riyadh, reported 14,000 hours a year saved across eleven automations and won a national digital-transformation award. Eighteen months later a new director-general asked a single question: what are those 14,000 hours doing now?

**Business context.** Irtiqa employs six people and has a growing budget request before the ministry's finance committee. The award is displayed in its office. Two departments have begun quoting Irtiqa's methodology in their own business cases.

**Technical challenge.** No baseline had been signed before any build; all were reconstructed afterwards from process-owner recollection. After-states were the design targets, never sampled. Wait-time reductions were included in the hours figure. Exception rates were never reported and, when finally measured, ran at 19% on the two largest automations — meaning almost a fifth of cases were being rescued by humans in a queue that had never appeared in any report. Two automations had been counted under both an old and a new name.

**Constraints.** The award cannot be un-won and the methodology is already being copied. The budget request is live. Two of the eleven automations are genuinely excellent and their real benefit is substantial. The centre's six staff are competent and acted in good faith; nobody falsified anything, they simply never measured.

**Solution approach (facilitate, don't lecture).** Steer toward: (1) re-measure four automations properly — sampled touch-time, exception rates, deduplicated — before saying anything, so the correction is evidence-led rather than defensive; (2) restate publicly with the method disclosed, and expect roughly a third of the original claim to survive, which is still a large real number; (3) fix the causes structurally — signed baselines before build, sampled after-states, exception rate mandatory beside benefit, one automation one identity; (4) recognise that the exception rate is the most damaging omission, because a 19% rescue rate means the automation transferred work rather than removing it and nobody was looking; (5) the harder organisational question is what pressure made an unmeasured claim rational in the first place, and whether the ministry's incentives reward reported benefit over measured benefit. That last question is where the room should end.

**Discussion questions.**
1. Nobody falsified anything, yet the number was wrong by a factor of nearly three. Which single missing practice caused most of the gap?
2. A 19% exception rate means work moved rather than disappeared. Why is that worse for staff than no automation at all, and how would you have detected it in month two?
3. How do you restate publicly without destroying a competent team? What exactly do you say to the finance committee?
4. Two departments are copying the methodology. What is your obligation to them, and how soon?

## Benchmarks and Evaluation

| Metric | Category | Target after M8 | How measured |
|---|---|---|---|
| Automations instrumented | Coverage | 7 of 7 writing telemetry | `BenefitTelemetry` row counts |
| Benefit claim basis | Integrity | 100% from sampled after-states; wait-time excluded | dashboard model audit |
| Register completeness | Governance | 7/7 with both owners, review date, handover link | register export |
| Handover packs passing the successor test | Sustainability | 7/7, three questions answered in ≤ 10 min | peer test |
| Measured portfolio benefit | Benefit | 651 h/month, 7,812 h/year, SAR 1,015,560 | dashboard tile 1 |
| Portfolio exception rate | Quality | ≤ 8% | dashboard tile 3 |

**Example benchmark table (filled during lab):**

| Process | Volume/mo | Before (min) | After designed | After measured | h/mo measured | Exception rate | Cycle time |
|---|---|---|---|---|---|---|---|
| Correspondence triage | 1,200 | 12.0 | 3.0 | 3.4 | 172 | 7.5% | 3.2d → 0.4d |
| Citizen enquiry | 1,600 | 9.0 | 3.0 | 3.1 | 157 | 9.2% | 5.0d → 1.4d |
| Purchase intake | 350 | 24.0 | 6.0 | 6.2 | 104 | 4.1% | 6.0d → 2.2d |
| Leave routing | 900 | 8.0 | 2.0 | 2.0 | 90 | 2.8% | 4.5d → 1.1d |
| Minutes and actions | 160 | 45.0 | 12.0 | 12.4 | 87 | 5.6% | 4.5d → 0.3d |
| Weekly report | 4 | 900 | 210 | 222 | 41 | n/a | Wed → Sun 08:00 |
| **Portfolio** | | | **669** | | **651** | **5.9%** | |

## Required Visuals and Training Assets

### Diagrams
1. **Baseline to claim** — *Purpose:* the measurement chain. *Elements:* signed baseline → build → sampled after-state → claim, with a red side-branch showing wait-time being excluded and a second showing design-target substitution being rejected. *Style:* linear chain with two rejected shortcuts drawn as struck-through arrows.
2. **The benefits dashboard layout** — *Purpose:* the lab's target. *Elements:* the eight tiles with tiles 1 and 3 visually bound by a bracket labelled "cannot be separated". *Style:* wireframe with the binding annotation prominent.
3. **The maturity model** — *Purpose:* strategic placement. *Elements:* five levels with characteristics and the next correct investment at each, and a marker showing Injaz at level 3 with the level-4 gap named. *Style:* ascending steps with the anti-pattern "level-1 organisation buying level-4 tooling" drawn as a fall.
4. **Handover pack anatomy** — *Purpose:* what survives a transfer. *Elements:* the seven sections with the successor's three test questions arrowed to the sections that answer them. *Style:* document map with the fallback section highlighted as most often missing.

### Images (screenshots)
1. **The restatement** — *why:* the course's ethical high point made concrete; *content:* the tile showing 669 design and 651 measured side by side with the reason text.
2. **Register row with both owners and a handover link** — *why:* the operating record; *content:* one complete row including lawful basis, retention, review date and benefit bound to telemetry.
3. **Exception rate rising beside benefit** — *why:* the alarm this module exists to install; *content:* a 12-month trend where hours saved and exception rate rise together.

### Simulations
1. **The inflated portfolio** — *Setup:* branch `sim-inflated-claim` with wait-time included, design targets used, and one automation double-counted. *Expected behaviour:* 11,400 h/yr against a true 7,812. *Learning objective:* three ordinary shortcuts compound into a 46% overstatement.
2. **The transfer** — *Setup:* pairs swap automations with only the handover pack, and must fix a seeded failure. *Expected behaviour:* packs with a complete "where it breaks" section succeed in minutes; others do not succeed at all. *Learning objective:* the pack is the automation's survival mechanism.

### Interactive Activities
- **Rate the claim (12 min):** five benefit claims from real-sounding programmes; teams score each against the seven credibility elements and rank them. The highest-scoring claim is also the smallest number, which is the point.
- **Maturity self-placement (15 min):** each participant places their own department on the model with written evidence and names the next investment. Collect these; they are the strongest predictor of which participants will start a real programme.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `BenefitTelemetry_seed.xlsx` | Six months of synthetic per-case telemetry across seven automations | XLSX | 41,200 rows | Dashboard build |
| `TouchTimeSamples.xlsx` | Three quarters of stopwatch samples, 30 per process per quarter | XLSX | 540 rows | Measured after-state |
| `InjazBenefits_start.pbix` | Starter dashboard with the six planted defects | PBIX | 1 file | Lab 8 correction exercise |
| `handover_pack_template.md` | Seven-section template | MD | 4 pages | Handover production and successor test |
| `maturity_model_selfassessment.xlsx` | Five-level rubric with evidence prompts | XLSX | 25 rows | Self-placement activity |

### Demo Requirements
- **Instructor demo (7 minutes):** open the starter dashboard showing 669 hours and SAR 1.04M. Switch one measure from design target to sampled median and watch it fall to 651. Then remove the wait-time inclusion and watch the annual figure fall by 3,100 hours. Ask the room which version they would rather defend in front of a finance committee that has its own analyst. Then reveal that this is exactly what happened at Irtiqa, and that the difference between the two dashboards is about four minutes of work.

---

# Final Capstone Project

## Title: Injaz — The Governed Automation Portfolio of a Saudi Government Shared-Services Department

## Project Scenario

You are the automation lead for **Injaz (إنجاز)**, the workflow-automation programme of the Shared Services Department of a Saudi government agency in Riyadh. Five days ago the department was spending **920 staff-hours a month** on six processes that consist almost entirely of typing, routing, chasing and copying. You have since built seven automations, one per lab, and each one runs.

Your mandate now is not to build more. It is to deliver an **integrated, measured, governed portfolio** that the department's director can defend to the agency's executive committee, that internal audit can inspect, that survives your own transfer to another entity next quarter, and in which **not one accountable human decision has been automated**. The capstone is the integration, the evidence and the governance — the components already exist.

## Requirements

**Mandatory (maps to the grading rubric):**

1. **Baseline and candidate register (LO1, LO2).** A signed 920 h/month baseline built from observed touch-times, with SIPOC and swimlane for at least two processes; all six candidates plus two refused candidates scored on five dimensions; every row naming its surviving human decision.
2. **Reliable automation fundamentals (LO3).** Every flow idempotent with a deterministic key; every switch with a default routing to a human; TRY/CATCH/FINALLY on all seven; deliberate retry policies; a demonstrated failure drill notifying a named human within 60 seconds.
3. **Document intelligence (LO4).** Correspondence triage with text-layer/scan triage, a closed label set including `uncertain`, schema-constrained extraction with nullable obscurable fields, dual confidence thresholds enforced in the flow, and a worked exception queue. Gold-set accuracy ≥ 92% with the OCR subset reported separately.
4. **Grounded bilingual drafting with a human gate (LO5).** Citizen enquiry replies drawn only from the approved knowledge base with cited units, zero invented citations, flow-computed dual Hijri/Gregorian dates, and a send action that cannot execute without an approval outcome. Edits and rejection reason codes captured.
5. **Consolidated reporting with reconciliation (LO6).** The weekly report pulling three sources with `DataAsOf` snapshots, explicit unmatched/duplicate key detection, four reconciliation checks with correct block/warn behaviour, bilingual tables, and a narrative constrained to the report's own figures.
6. **Minutes and action tracking (LO4, LO6).** Transcript to schema-constrained minutes applying the decision test with evidence quotes, chair approval before action creation, and a four-rung chase ladder with working-day guard and extension handling.
7. **Governance and accountability (LO7).** Field classification with a demonstrated minimisation removal, lawful basis, retention labels at creation, durable audit rows carrying `DecidedBy`, `RuleApplied` and `FlowVersion`, a boundary assessment for every connector, and a signed never-automate assertion for all seven automations.
8. **Benefits realisation and sustainability (LO8).** Instrumented telemetry, sampled after-state touch-times, the eight-tile dashboard reporting the **measured** 651 h/month with the design claim shown alongside, a complete register with both named owners, and handover packs passing the successor test.

**One extension (choose at least one):**
- Build the eighth automation on a process from your **own** department, with a measured baseline and a full governance pack.
- Add the carry-forward: open actions from one meeting automatically becoming agenda item 2 of the next.
- Add a regression harness that runs every flow's test set on demand and posts a pass/fail summary to Teams.
- Build the n8n equivalent of one automation and write a one-page comparison of the two platforms for an agency without a Microsoft estate.
- Add a knowledge-base improvement loop: weekly digest of rejection reason codes and edited units, feeding a prioritised content backlog.

## Architecture (target state)

```
INTAKE                    AUTOMATION LAYER                    HUMAN DECISION           RECORD
 mailbox  ─letter──►  triage ─► classify ─► extract ─►[gate]─► dept head confirms ──► CorrespondenceRegister
 Form     ─leave───►  validate ─► delegation ─► SLA ──►[gate]─► approver decides ────► LeaveRequests
 Form     ─purchase►  complete ─► budget ─► threshold►[gate]─► band approver ────────► PurchaseRequests
 folder   ─transcript► minutes ─► decisions ─► actions►[gate]─► chair approves ──────► MinutesRegister
 3 systems─data────►  join ─► RECONCILE ─► format ────►[gate]─► head signs narrative ► WeeklyReportArchive
 portal   ─enquiry─►  classify ─► retrieve ─► draft ──►[gate]─► officer signs ───────► EnquiryCases
                                                                     │
   every path ─► TRY/CATCH/FINALLY ─► FlowFailures + AutomationAuditLog (DecidedBy, FlowVersion, 10 yr)
   every path ─► BenefitTelemetry ─► InjazBenefits dashboard (651 h/mo measured, exception rate locked beside it)
   governance ─► classification · lawful basis · retention at creation · boundary · never-automate assertion
   [gate] = a named accountable human. NOTHING crosses a gate without one.
```

## Deliverables

1. A Power Platform **Solution export** (`.zip`) containing all seven automations, environment variables and the supporting lists — importable and runnable by the instructor.
2. `INJAZ_BASELINE.xlsx` — the signed 920 h/month baseline with observation logs, SIPOC and swimlanes.
3. The **automation register** export: seven rows plus two refused candidates, with owners, classification, lawful basis, retention, review dates and benefit figures bound to telemetry.
4. `INJAZ_BENEFITS.pbix` (or a published dashboard link) reporting the measured portfolio benefit with the exception-rate tile locked beside it.
5. Seven **handover packs**, one of which is tested live by another team during the demo.
6. `GOVERNANCE.md`: field classifications, lawful bases, retention decisions, connector boundary assessments, and the seven signed never-automate assertions with forum minute references.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: baseline signed + candidates scored + leave flow running | End Day 1 | totals equal 920 / 669; 8 candidates scored with surviving decisions named |
| M-B: hardened leave flow + correspondence triage on the gold set | End Day 2 | 8/8 test cases; ≥ 92% accuracy; failure drill notifies in ≤ 60 s |
| M-C: enquiry drafting with gate + weekly report with blocking reconciliation | End Day 3 | 0 invented citations; report blocks on the seeded breaches |
| M-D: minutes + chase ladder + governed purchase intake | End Day 4 | 0 automated decisions; audit rows carry `DecidedBy`; assertions signed |
| M-E: dashboard + register + handover packs + demo | Day 5 H5 | measured 651 h/mo; successor test passed; rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Baseline, candidate scoring, and surviving human decisions | 12 | Observed touch-times, signed baseline reconciling to 920/669, all 8 candidates scored on 5 dimensions, every surviving decision named to a specific role | Baseline sound but one dimension thin or two decisions generic | Self-reported times, wait-time counted as savings, or risk dimension absent |
| Automation reliability (idempotency, branching, error handling) | 15 | All flows idempotent, every switch defaulted to a human, TRY/CATCH/FINALLY throughout, deliberate retries, failure notified ≤ 60 s | Mostly present; one flow non-idempotent or one retry policy unconsidered | Duplicate records on replay, a switch with no default, or a CATCH that only emails |
| Document intelligence and structured output | 15 | Triage correct, `uncertain` class working, nullable obscurable fields with zero inventions, thresholds enforced in the flow, ≥ 92% with OCR subset reported honestly | Works; accuracy 88–92% or the OCR subset under-reported | No triage, invented values on obscured fields, or thresholds only in the prompt |
| Grounded drafting and the approval gate | 15 | Zero invented citations, retrieval filtered on status and validity, flow-computed dual dates, send impossible without approval, edits and reason codes captured | Grounded and gated; edit capture or reason codes thin | An invented citation, a retired source quoted, or a send action outside the approval branch |
| Consolidation, reconciliation, and reporting | 12 | Snapshots stamped, unmatched and duplicate keys reported, four checks with correct block/warn, bilingual tables, narrative fully in-report | Reconciliation present but one check mis-classified or narrative thin | Inner join dropping rows silently, or reconciliation displayed without gating |
| Governance, PDPL, and accountability | 16 | Full classification with a real minimisation removal, retention at creation, durable audit with `DecidedBy` never `automation`, boundary assessed, all seven assertions signed | Governance solid with one artefact incomplete | Any automated adverse decision, personal data in an outbound payload, or audit rows without `DecidedBy` |
| Benefits realisation, register, handover, and demo | 15 | Measured 651 h/mo with the restatement explained, exception tile locked beside benefit, 7/7 packs passing the successor test, crisp 6-minute demo | Measured and registered; one pack weak or the demo unfocused | Design targets reported as measured, wait-time added to hours, or a pack with no manual fallback |

**Pass ≥ 70. Distinction ≥ 90.** The chosen extension adds up to +5 bonus (capped at 100) only if mandatory scope scores ≥ 80.

## Assessment Criteria Notes for Instructors

- **Grade from the running portfolio and its evidence first, the demo second.** Import the Solution, trigger two flows, open the audit log, open the dashboard. A portfolio that only exists in screenshots does not pass, and a flow with no successful runs in its history has not been built.
- **Anti-pattern flags that cap the relevant criterion at 70%:** any automated adverse decision or automated award, however small; an invented citation or an invented value in an obscurable field; a send or publish action that can execute without an approval outcome; wait-time counted as hours saved; a design target reported as a measured after-state; an audit row where `DecidedBy` reads `automation`; a handover pack with no manual fallback; a switch with no default.
- **Verify one claim live.** Pick one at random: ask the participant to submit the same form twice and show one record; or to break a connection and show the failure notification arrive; or to name who approved a specific purchase request from the audit log; or to hand their handover pack to another team and let that team answer the three successor questions unaided.

## Bonus Tasks (for early finishers / distinction seekers)

1. Build the regression harness that runs every flow's test set on demand and posts a pass/fail summary to Teams — then break one flow deliberately and show the harness catch it.
2. Add the splitting-pattern detector to a second process and show what pattern it surfaces in the seeded history.
3. Produce the maturity self-assessment for your own department with written evidence and a costed next investment, and present it in your demo.
4. Rebuild one automation in n8n and write the one-page platform comparison an agency without a Microsoft estate would actually need.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** What are the five columns of a SIPOC? → Suppliers, Inputs, Process, Outputs, Customers.
**Q2.** A process takes 12 minutes of work over 3 days. Which figure enters the hours-saved case? → the 12 minutes; the 3 days is cycle time, reported separately.
**Q3.** What must `TouchMinutesAfter` never be, and why? → zero — it would mean no human remains in the loop.
**Q4.** What makes a flow key idempotent? → it is derived deterministically from the trigger payload, never from `utcNow()`.
**Q5.** A switch has five cases and the business adds a sixth value. What happens with no default? → the run completes successfully and does nothing — a silent failure.
**Q6.** When should a retry policy be `none`? → for non-transient failures: 400, 404, 403.
**Q7.** Why must `apply to each` concurrency be off when appending to a variable? → parallel iterations overwrite each other; output is silently incomplete.
**Q8.** Name the three things a CATCH scope must do. → write a durable failure record, notify a named human, leave the case recoverable.
**Q9.** How do you detect a scanned PDF before processing it? → extract text and measure length; under ~50 characters means it is a scan.
**Q10.** Why must `uncertain` be in the label set? → it keeps ambiguous cases with a human rather than forcing a confident wrong label.
**Q11.** Why is a nullable `reference_number` safer than a required one? → required forces invention; null plus a flag routes it to a human.
**Q12.** Where must a confidence threshold be enforced? → in the flow's gate, not only in the prompt.
**Q13.** What must happen when retrieval returns zero approved knowledge-base units? → route to a human; do not call the model at all.
**Q14.** Why does the flow, not the model, compute the dates? → so Hijri and Gregorian cannot disagree; the value is computed once for both languages.
**Q15.** Which reconciliation breaches block publication and which warn? → money and completeness block; continuity warns, because blocking on it trains people to bypass the gate.
**Q16.** Why is an inner join dangerous in a report flow? → it silently drops unmatched rows and the totals still look plausible.
**Q17.** State the three-part decision test for minutes. → settled outcome; an authority settled it; effect outside the room.
**Q18.** What must `DecidedBy` never read for an adverse outcome? → `automation` or `system-rule`.
**Q19.** Name two things that must never be automated, and what may be automated around each. → e.g. eligibility denial (completeness, gathering, drafting, notification) and procurement award (compliance checks, routing, scheduling, record creation).
**Q20.** Why must the after-state touch-time be measured rather than assumed? → the residual human time almost always exceeds the design target; assuming it overstates the claim.

## Practical Assessments

**PA-1 (30 min, Day 2, 15% of course grade).** You are given a flow that creates duplicate records on replay, has a switch with no default, sets exponential retries on a 404-prone lookup, and whose CATCH scope only sends an email. Restore reliability: make the key deterministic, add a default routing to a human queue, set retry policies deliberately, and complete the CATCH with a durable failure record and a named recipient. Prove it with a duplicate submission, an unknown switch value, and a deliberate failure drill. Scored on diagnosis notes (30%), fixes (45%), verification evidence (25%).

**PA-2 (30 min, Day 4, 15% of course grade).** You are given a purchase-intake flow with an auto-approve band under SAR 5,000, an unused national-ID field carried into the notification, no retention label, and audit rows without `DecidedBy`. Restore governance: complete the field classification and remove the unnecessary field, apply retention at creation, replace the auto-approve band, add the durable audit row and the governance guard, and complete the never-automate assertion. Scored on the classification and minimisation finding (30%), the decision-boundary fix (40%), audit and assertion completeness (30%).

**PA-3:** The Injaz capstone portfolio, scored against the rubric above — **40%** of the course grade. Labs 1–8 completion — **20%**. Quiz — **10%**.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (8 labs) | 20% | Running flows with successful run histories, test-set results, benchmark tables filled from own runs |
| PA-1 (reliability) | 15% | Repaired flow, duplicate/default/failure drills, diagnosis notes |
| PA-2 (governance) | 15% | Classification, decision-boundary fix, audit rows, signed assertion |
| Quiz | 10% | 10-question selection, closed book |
| Capstone portfolio | 40% | Rubric; graded portfolio-first from the imported Solution and its evidence |

Badge issuance (Workflow Automation badge, Data & AI Fluency track) requires **≥ 70 overall**, **capstone ≥ 70**, **zero academic-integrity flags** — identical benchmark tables, audit-log exports or handover packs across submissions are checked — and **zero governance red flags**: no automated adverse decision or award, no real personal data in any training-tenant artefact, no personal data in an outbound payload, and no audit row where `DecidedBy` reads `automation`. A governance red flag blocks the badge regardless of the numerical score; this mirrors how the agency itself would treat the same finding.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Book and provision the **training tenant**; assign Power Automate Premium trial licences to every seat plus two spares; log in as a participant yourself and complete Lab 2 end to end
- [ ] Verify the tenant's Data Loss Prevention policy permits every connector the labs use; where AI Builder or the LLM endpoint is blocked, confirm the **standard-connector variant** of Labs 3, 4 and 6 runs using the supplied OCR sidecars and transcripts
- [ ] Import and test all eight `Injaz_LabN_Start` and `Injaz_LabN_Solution` solution packages into a clean environment; confirm every planted defect is present and every solution passes its acceptance criteria
- [ ] Regenerate the synthetic Injaz datasets (200 gold letters, 120 enquiries, 3 transcripts, 90 days of purchase requests, 6 months of telemetry) and verify every count quoted in the labs matches
- [ ] Print the **action-card decks** (trigger, action, condition, switch, loop, scope, run-after) — two per table — and the red-line card sort deck; these carry the course if the tenant fails entirely
- [ ] Print A3 posters: the six-process backlog wheel, touch-time vs wait-time, TRY/CATCH/FINALLY, the three-way confidence gate, the never-automate line, the maturity model
- [ ] Confirm the shared drive holds the swimlane templates, observation logs, handover template, schemas and prompt library, and that participants can reach it from the classroom network
- [ ] Prepare the flip-chart backlog tracker (six processes, ticked off as automated) and the shared benefits leaderboard
- [ ] Rehearse the four instructor demos that carry the week: the duplicate-record demo (M2), the stamped-letter null demo (M3), the ungrounded-citation demo (M4), and the dashboard restatement demo (M8)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Sign in once to the **training tenant** with the credentials supplied and confirm you can open Power Automate, SharePoint and Teams — do this before Day 1, not on Day 1
- [ ] Confirm you can create a test flow with a manual trigger and a "send me an email" action, and that the email arrives
- [ ] Install Power BI Desktop (Day 5 only; the web service is an acceptable alternative)
- [ ] Bookmark the shared drive and confirm you can open `InjazBaseline_start.xlsx` and one PDF from `injaz_letters_gold_200/`
- [ ] Bring a device with a browser and a working keyboard for Arabic input if you intend to work in Arabic
- [ ] **Do not bring, upload or use any real letter, request, transcript or personal data from your own entity at any point during this course.** All data is supplied and synthetic

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| "You don't have a licence for this connector" / premium connector blocked | High | Switch to the standard-connector lab variant; the training tenant's premium trial covers the rest. Have the variant open on screen before Lab 3 |
| Participant's own agency account used instead of the training tenant | High | Insist on the training tenant at Day 1 Hour 1 and again before Lab 3; a personal-tenant flow will fail on DLP and burn twenty minutes |
| Duplicate records because the key uses `utcNow()` | High | The planted Lab 2 defect; make the fix a room-wide checkpoint before anyone proceeds |
| Recurrence trigger fires three hours late | High | Time zone left at UTC; set Arab Standard Time explicitly on the trigger |
| Parse JSON fails on a fenced code block | Medium | Add the fence-strip Compose; it is in the Module 3 code examples |
| Switch built without a default case | Medium | Walk the room during Lab 2 and Lab 7; check every switch personally |
| Send or publish action placed outside the approval branch | Medium | The most serious lab defect; check `runAfter` on every pair's send action in Labs 4 and 5 |
| Arabic text renders left-to-right or reversed in an email | Medium | Wrap in `<div dir="rtl">`; render two tables rather than translating headers |
| Apply-to-each concurrency producing short digests | Medium | The Lab 2b drill; if skipped, participants will not believe a green run can be wrong |
| Shared drive or classroom network blocking the LLM endpoint | Low | Fall back to the supplied pre-generated model outputs for each lab; the flow logic is still fully exercised |

## Timing Recommendations

- Protect Lab 2b (error handling and the concurrency drill) and Lab 7 (governed intake) at full length. They carry the two ideas — reliability and accountability — that the whole course rests on.
- If a cohort is strong: pull the carry-forward extension into Lab 6 and the regression harness into Lab 8 as main scope, and run the Module 7 red-line card sort as a debate rather than a sort.
- If a cohort is weak: run Lab 5's reconciliation as a guided whole-room build rather than a paired lab, but never skip the *blocked run* — seeing publication refused is the module's entire argument.
- **Hard rule:** Day 5 Hour 4 (capstone assembly) starts on time regardless of what is unfinished. Cut discussion, cut the bonus tasks, cut Module 8 theory — never cut assembly time. A participant who leaves with an unassembled portfolio leaves with nothing they can show their director.
- Reserve the Module 8 restatement demo (669 → 651) even under maximum time pressure. It takes four minutes and it is the lesson participants quote back a year later.

## Discussion Prompts (use during transitions)

1. "You have just built something that will still be running when you have moved to another entity. Who fixes it, and how do they know how?"
2. "Your automation completed successfully and produced the wrong answer. Which of your seven flows could do that today, and what would tell you?"
3. "A citizen received a written reply from your agency with a wrong fee in it. Walk me back from the citizen to the design decision that caused it."
4. "If your automation removes the person who would have noticed the pattern, what have you actually optimised?"
5. "You freed 4.6 FTE of capacity. Your director asks what those people are doing now. What is your answer, and when did you decide it?"

## Wrap-up (Day 5 final 15 minutes)

- **Map each capstone requirement to the module that taught it**, on one slide: baseline and scoring (M1), reliability (M2), document intelligence (M3), grounded drafting and the gate (M4), reconciliation and reporting (M5), minutes and action tracking (M6), governance and accountability (M7), benefits and sustainability (M8). Then show the six-process backlog wheel fully filled and the single number under it: **651 measured hours a month, and zero automated decisions.**
- **Forward pointers:** `SDA-DSC-212` (Data Quality and Data Warehousing & Business Intelligence) for participants whose weekly report revealed that their real problem is data quality upstream; `SDA-AIE-240` (Vibe Coding) for those who found themselves wanting to build rather than configure. Both assume the governance instincts installed here. Remind the room that `SDA-FND-110` (Prompt Engineering and Responsible AI Use) is the prerequisite they should recommend to colleagues before sending them here.
- **Collect:** the Solution export, `INJAZ_BASELINE.xlsx`, the register export, the benefits dashboard link, the seven handover packs, and `GOVERNANCE.md`. Confirm every participant has taken away their own department's maturity self-assessment and at least one scored candidate from their real job. Badge recommendations issued within **5 working days**.

---

*End of instructor package. All flow definitions target Power Automate cloud flows on the 2016-06-01 workflow-definition schema, SharePoint Online lists, Excel Online (Business), Microsoft Forms, the Approvals connector and Power BI, with n8n 1.4x shown as the open-source alternative; verify connector availability and premium licensing in the training tenant before each delivery, since tenant policy — not capability — is the usual constraint. All flow names, action names, list and column names, JSON keys and variable names remain in English per Saudi enterprise production convention; Arabic appears in letter content, drafted correspondence, report headings and slide subtitles, where it belongs. Saudi PDPL, records-retention and audit obligations are treated as first-class design constraints from Day 1 Hour 1, and no accountable human decision is automated anywhere in this package.*
