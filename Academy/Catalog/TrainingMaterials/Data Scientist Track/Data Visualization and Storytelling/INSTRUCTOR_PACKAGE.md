# Data Visualization and Storytelling
## تصور البيانات وسرد القصص

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Data Visualization and Storytelling |
| **Arabic Title** | تصور البيانات وسرد القصص |
| **Course Code** | SDA-DSC-112 |
| **Track** | Data Scientist (عالم البيانات) |
| **Level** | Practitioner |
| **Duration** | 3 days × 5 learning hours = **15 hours** |
| **Audience** | Data scientists, analysts, BI professionals |
| **Prerequisites** | SDA-FND-104 |
| **Assessment** | Dashboard project; storytelling presentation |
| **Stackability** | Communication badge · Required for Data Scientist Practitioner certificate · Next: SDA-DSC-211 |
| **Tools & Platforms** | Plotly · Power BI/Tableau · Matplotlib/Seaborn |

## Course Description

A craft-focused module on turning analysis into influence. Participants apply perception science to design honest, compelling visualisations, build interactive dashboards, and structure data narratives for executive audiences. The module closes the last mile between analytical work and organisational decisions — the point where a correct analysis either changes a decision or dies in a slide nobody understood.

The course is built around a single evolving artefact: the **"Tayseer" (تيسير) National Digital Services Program**, a Vision 2030 initiative to move government service delivery from branches to digital channels. Participants receive one realistic dataset — `tayseer_services.csv`, monthly service metrics across the 13 administrative regions of Saudi Arabia — and carry it through every lab. Module 1 audits how it is perceived; Module 2 chooses honest chart types for it; Module 3 declutters and annotates it; Module 4 turns it into an interactive dashboard; Module 5 wraps it in a narrative; Module 6 delivers it to a simulated Steering Committee. By the end of Day 3 each participant owns a decision-ready executive dashboard **and** a seven-minute data story recommending where the program should invest its next SAR 40 million — the exact shape of deliverable expected in the workplace this course feeds.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Apply visual-perception principles to select effective chart types
2. **LO2** — Design clear, honest visualisations that avoid distortion and clutter
3. **LO3** — Develop interactive dashboards for self-service exploration
4. **LO4** — Construct data narratives structured around audience and decision
5. **LO5** — Evaluate visualisations through critique and iterative refinement
6. **LO6** — Present analytical findings persuasively to executive stakeholders

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Seeing clearly | M1: Perception Science & Visual Encoding · M2: Chart Selection & Design Principles | 45% | 55% | A perception audit + a defensible chart-choice set for the Tayseer dataset, drawn honestly |
| **Day 2** | Craft and interactivity | M3: Colour, Annotation & Decluttering · M4: Interactive Dashboards & BI Tools | 40% | 60% | A before/after redesign pair + a working interactive Tayseer dashboard with filters and drill-down |
| **Day 3** | Narrative and the room | M5: Data Storytelling Structure & Flow · M6: Executive Communication & Presentation Lab · Capstone | 30% | 70% | A storyboarded narrative + a rehearsed 7-minute executive presentation + capstone submission |

## Hour-by-Hour Breakdown

### Day 1 — Seeing Clearly

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why most dashboards fail** + course kickoff + Tayseer dataset tour | Recognise the analysis-to-decision gap; identify the 6 craft skills covered; understand the golden-thread dataset | Interactive lecture + "worst chart you've seen" discussion | 80/20 |
| 2 | **Perception science and visual encoding** (M1) | Pre-attentive attributes; the encoding-accuracy ranking; channels and their honesty | Lecture + live perception demos | 70/30 |
| 3 | **Lab 1 — Perception audit & five encodings** | Encode one Tayseer metric five ways; rank by decoding accuracy; run a pre-attentive test | Guided lab (pairs) | 15/85 |
| 4 | **Chart selection and design principles** (M2) | Matching question-type to chart; the design-principles checklist; small multiples | Lecture + chart-chooser walkthrough | 70/30 |
| 5 | **Lab 2 — Chart chooser + first honest chart** | Pick and build the right chart in matplotlib/Plotly for four Tayseer questions | Guided lab (pairs) | 10/90 |

### Day 2 — Craft and Interactivity

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Colour, annotation, and decluttering** (M3) | Colour semantics & accessibility; the data-ink ratio; annotation as the argument | Lecture + live redesign demo | 65/35 |
| 2 | **Lab 3 — Before/after redesign** | Redesign a deliberately cluttered Tayseer chart; measure the improvement | Guided lab (pairs) | 10/90 |
| 3 | **Interactive dashboards and BI tools** (M4) | Dashboard layout; interaction patterns; Plotly vs Power BI/Tableau; self-service design | Lecture + tool demo | 60/40 |
| 4 | **Lab 4a — Build the Tayseer dashboard** | Compose a multi-view dashboard with KPI headline, trend, regional breakdown | Guided lab | 10/90 |
| 5 | **Lab 4b — Interactivity & drill-down** | Add cross-filtering, region drill-down, and a channel toggle; usability test | Guided lab | 10/90 |

### Day 3 — Narrative and the Room

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Data storytelling structure and flow** (M5) | Audience-decision framing; narrative arcs; the Big Idea; annotation-led sequencing | Lecture + story-deconstruction | 60/40 |
| 2 | **Lab 5 — Storyboard the Tayseer narrative** | Turn dashboard findings into a storyboarded 7-slide arc with one Big Idea | Guided lab (pairs) | 15/85 |
| 3 | **Executive communication** (M6) | Executive attention economics; the BLUF/top-line; handling Q&A; slide craft | Lecture + delivery clinic | 50/50 |
| 4 | **Capstone assembly** | Integrate dashboard + story; rehearse; peer critique round | Project work | 0/100 |
| 5 | **Capstone presentations + assessment + wrap-up** | 7-minute executive presentations; rubric-based peer + instructor scoring; path to SDA-DSC-211 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module operates on the same Tayseer dataset. Never introduce a throwaway example dataset — always evolve the Tayseer artefact. This is what makes the Day 3 capstone (dashboard + executive story) achievable, because the analysis is already done; only the *communication* is being graded across three days.
- **Pace control:** Lab 3 (before/after redesign) and Lab 4b (interactivity) are the most overrun-prone. Publish checkpoint notebooks and `.pbix`/`.twbx` starter files (`lab3_start`, `lab3_solution`, `lab4_start`, …) so stragglers can fast-forward without falling behind the narrative.
- **Pairing:** rotate pairs each day. Pair a strong-coder participant with a strong-design-sense participant; the skill transfer between "can build it" and "can see it" is the entire point of a craft course.
- **Environment strategy:** primary = local Jupyter + Plotly + a BI tool (Power BI on Windows, Tableau Public cross-platform); fallback = Google Colab for the Python labs and Tableau Public (browser) for the BI labs. Verify licences and both paths the week before delivery.
- **Language:** deliver in English or Arabic; keep code, identifiers, and column names in English. For any Arabic-facing chart, teach right-to-left axis ordering and Arabic numeral choices explicitly (M3) — a Saudi executive audience will notice a mirrored axis immediately.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. The Day 3 afternoon is deliberately presentation-heavy and low on new theory.
- **Assessment logistics:** collect dashboard files and slide decks at the end of Day 3 Hour 4 so the instructor can pre-load them; rubric scoring happens live during Hour 5. Record presentations (with consent) — reviewing one's own delivery is the single most effective feedback in M6.
- **Critique culture:** establish the critique norms on Day 1 Hour 1 (critique the chart, not the person; propose a fix with every criticism). Every module contains a critique exercise; a safe critique culture is a prerequisite, not a nicety.

---

# Module 1 — Perception Science and Visual Encoding

## Module Overview

**Purpose.** A visualisation is a machine for offloading cognition onto the visual system. Whether it works is not a matter of taste — it is a matter of how human perception actually decodes marks on a screen. This module gives participants the perceptual foundation that every later design decision rests on: which visual channels the eye reads accurately, which it reads only approximately, and which it barely reads at all. Get this wrong and no amount of colour or polish will save the chart; get it right and honest, effective design becomes almost mechanical.

**Business relevance.** In Saudi organisations pushing analytics into executive and ministerial decision-making under Vision 2030, the cost of a misperceived chart is a misinformed decision. A dashboard that encodes the most important comparison as an angle in a pie chart, or as colour saturation, forces the executive to work — and busy executives do not work at charts, they glance at them. Teams that understand encoding accuracy ship dashboards that are read correctly in three seconds; teams that do not ship decoration that gets ignored or, worse, misread.

**Industry use cases.**
- A national program office needs a Deputy Minister to grasp, at a glance, that three regions lag on digital adoption — this must be a position/length comparison, not a colour one.
- A bank's risk dashboard must let an analyst spot the one branch out of 400 that is an outlier — a task that only a well-chosen position encoding (or a pre-attentive colour pop) makes possible.
- A hospital operations screen must communicate "wait times are rising" to nurses in peripheral vision — motion and position, never a data table.

**Expected competencies.** After this module a participant can name the pre-attentive visual attributes, rank the common encoding channels by decoding accuracy (the Cleveland–McGill hierarchy), predict which chart a given comparison task demands, explain why pie/3D/dual-axis charts mislead, and audit an existing chart for perceptual honesty.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Identify pre-attentive visual attributes and use them to direct attention | LO1 |
| 1.2 | Rank encoding channels by decoding accuracy and choose accordingly | LO1 |
| 1.3 | Explain why specific chart types (pie, 3D, dual-axis) systematically mislead | LO1, LO2 |
| 1.4 | Match a comparison task to the visual channel that supports it | LO1 |
| 1.5 | Audit an existing visualisation for perceptual accuracy and honesty | LO5 |

## Technical Content

### 1. How the visual system reads a chart

Perception happens in two stages, and good design exploits both. **Pre-attentive processing** is the massively parallel, sub-250-millisecond stage: before you consciously "look", your visual system has already registered certain attributes across the entire field — colour hue, orientation, size, motion, and a handful of others. This is why one red dot among grey dots "pops" with zero effort, while finding the digit 5 among other digits requires slow serial search. **Attentive processing** is the slow, serial, effortful stage — reading text, comparing exact values, following a legend.

The design consequence is direct: **encode the thing you want noticed in a pre-attentive channel, and encode everything else quietly.** The single most common failure in enterprise dashboards is spending pre-attentive channels (bright colour, heavy borders, 3D) on chrome and gridlines, leaving the actual signal to be found by slow serial search.

The pre-attentive attributes worth naming in class: **hue**, **colour intensity/saturation**, **size**, **orientation/angle**, **length**, **position (2D location)**, **shape**, **enclosure**, **added marks**, and **motion**. Not all are equal — the next subsection ranks them by *accuracy*, which is a different question from *salience*.

**Instructor note:** run the "find the 3" pre-attentive demo (a grid of grey 3s and 8s, then the same grid with the 3s in red). Time the room. The gasp when the red version resolves instantly *is* the lesson — perception, not preference.

### 2. The encoding-accuracy hierarchy (Cleveland–McGill)

In 1984 Cleveland and McGill measured how accurately people decode quantitative values from different visual channels. The ranking, from most to least accurate, is the single most important table in this course:

| Rank | Channel | Example | Decoding accuracy |
|---|---|---|---|
| 1 | **Position on a common scale** | Dots/bars on the same axis | Best — use for your most important comparison |
| 2 | **Position on non-aligned scales** | Small multiples with separate axes | Very good |
| 3 | **Length** | Bar length (not starting at a common baseline) | Good |
| 4 | **Angle / slope** | Pie slices, line slope | Moderate — routinely misjudged |
| 5 | **Area** | Bubble size | Poor — perceived as ~0.7 power of true value |
| 6 | **Volume** | 3D bars, spheres | Worse |
| 7 | **Colour saturation / intensity** | Heatmap shade | Worst for exact values (fine for pattern) |

The operational rule: **match the accuracy of the channel to the precision the task requires.** If the executive must rank regions precisely, use position (a sorted bar or dot plot). If they only need the gestalt of "hot vs cold across a matrix", saturation (a heatmap) is legitimate because exact decoding is not the task. The error is using a low-accuracy channel for a high-precision task — encoding budget figures as bubble areas, for instance, guarantees misreading.

### 3. Why pie, 3D, and dual-axis charts mislead

These three deserve explicit treatment because they are ubiquitous in the workplace and each fails for a *perceptual* reason participants must be able to articulate:

- **Pie charts** force angle/area decoding (rank 4–5) for what is almost always a part-to-whole comparison better served by a sorted bar (rank 1). They become unreadable past ~5 slices and are hopeless for comparing two pies side by side. Legitimate use: a single, memorable "roughly half vs the rest" split — rare.
- **3D charts** add a volume/perspective distortion (rank 6) that changes apparent values with viewing angle; a back bar is foreshortened, occlusion hides data, and the "depth" encodes nothing. There is essentially no honest use of a 3D bar or pie in analytics. Ban them.
- **Dual-axis charts** (two Y-axes) let the designer manufacture any correlation they like by independently scaling the axes; the crossing point is an artefact of axis choice, not data. Prefer indexed lines (both series to a common base = 100) or two small multiples.

**Common mistake to pre-empt:** participants will defend pies because "executives like them". Reframe: executives like *understanding quickly*. A sorted bar delivers that better; the pie is habit, not preference.

### 4. Matching the task to the channel

Encoding is chosen by the *question*, not the data type alone. Teach this task-to-channel mapping:

| Analytical question | Best encoding | Typical chart |
|---|---|---|
| "How do these categories rank?" | Position, common scale | Sorted bar / dot plot |
| "How has this changed over time?" | Position along X + line | Line chart |
| "How is this distributed?" | Position + density | Histogram / box / strip |
| "How do two variables relate?" | Position (X,Y) | Scatter |
| "Where is this, geographically?" | Position on a map | Choropleth (carefully) |
| "What is the part-to-whole split?" | Length | Stacked/100% bar (rarely pie) |
| "What is the pattern across a matrix?" | Colour saturation | Heatmap |

For the Tayseer program, "which regions lag on digital adoption?" is a ranking question → sorted bar or dot plot on a common scale, never a choropleth as the primary view (maps encode *where* well but *how much* poorly, because area and colour dominate).

### 5. Perceptual honesty: distortion and the lie factor

A chart is honest when the ratio of the visual effect to the data effect is 1. Tufte's **lie factor** = (size of effect shown in graphic) ÷ (size of effect in data). Sources of distortion to teach and forbid:

- **Truncated axes on bar charts.** Bars encode value by *length from zero*; a bar chart that starts its axis at 60 instead of 0 multiplies the apparent difference. (Line charts, which encode via position/slope, may legitimately truncate — the baseline is not part of the encoding. This distinction trips up almost everyone; teach it explicitly.)
- **Inconsistent or reversed scales**, dual axes (subsection 3), and cumulative-vs-rate switches mid-chart.
- **Area-encoded quantities** where the designer scaled the radius by the value (doubling the value quadruples the area) instead of scaling area by value.
- **Cherry-picked time windows** that hide the trend before the chosen start.

Honesty is not only ethics; in a SAMA- or government-audited context, a distorted chart in a decision pack is a governance finding.

### 6. Real-world example walkthrough

Narrate this (5 minutes): the Tayseer program's first quarterly review used a slide with a 3D exploded pie of "transactions by channel" and a dual-axis line overlaying satisfaction and cost. The committee spent eight minutes arguing about whether branch usage was "about a third or about a quarter" (the 3D perspective made it ambiguous) and drew the wrong conclusion that rising satisfaction was *caused* by rising cost (the dual axis had been scaled to make the lines cross). The redesign — one sorted bar for channel mix, two indexed lines for satisfaction and cost — ended the same debate in ninety seconds and reversed the conclusion. Same data, different perception. This module is the reason the redesign worked.

## Code Examples

### Loading the golden-thread dataset and a pre-attentive demo

```python
# notebooks/m1_perception.ipynb
"""Module 1 — perception & encoding on the Tayseer dataset.
Rules for this notebook: every chart states the *task* it serves in a comment."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# One dataset, reused all course. Monthly service metrics by region/category/channel.
df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])
print(df.columns.tolist())
# ['month','region','service_category','channel','transactions','unique_users',
#  'digital_adoption_pct','csat','avg_completion_min','first_time_resolution_pct',
#  'cost_per_txn_sar','sla_breach_pct']

# Pre-attentive demo: the SAME ranking, encoded as colour (hard) vs position (easy).
latest = (df[df.month == df.month.max()]
          .groupby("region", as_index=False)["digital_adoption_pct"].mean())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# LEFT — colour saturation encoding (rank 7): "find the lowest region" is slow.
axes[0].scatter(range(len(latest)), np.ones(len(latest)),
                c=latest["digital_adoption_pct"], cmap="Blues", s=600)
axes[0].set_title("Encoded as colour — try to rank the regions")
axes[0].axis("off")

# RIGHT — position on a common scale (rank 1): ranking is instant.
s = latest.sort_values("digital_adoption_pct")
axes[1].barh(s["region"], s["digital_adoption_pct"], color="#4C78A8")
axes[1].set_title("Encoded as position/length — ranking is pre-attentive")
axes[1].set_xlabel("Digital adoption (%)")
plt.tight_layout()
plt.savefig("out/m1_encoding_contrast.png", dpi=150)
```

### Directing attention with a single pre-attentive pop

```python
# Highlight ONE region (the lagging one) using hue as a pre-attentive channel.
# Everything else is quiet grey; the eye lands on the signal with zero search.
s = latest.sort_values("digital_adoption_pct")
worst = s.iloc[0]["region"]
colors = ["#E45756" if r == worst else "#D3D3D3" for r in s["region"]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(s["region"], s["digital_adoption_pct"], color=colors)
ax.set_xlabel("Digital adoption (%)  —  latest month")
ax.set_title(f"{worst} lags every other region on digital adoption")  # title = the point
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("out/m1_attention_pop.png", dpi=150)
# Teaching point: colour spent on ONE mark that carries the message,
# not sprinkled across all 13 bars as decoration.
```

### A quick lie-factor / truncated-axis demonstration

```python
# Same two regions, honest vs distorted — measure the lie factor.
two = s[s["region"].isin([worst, s.iloc[-1]["region"]])].reset_index(drop=True)
a, b = two["digital_adoption_pct"]
data_ratio = b / a                               # true ratio in the data

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].bar(two["region"], two["digital_adoption_pct"], color="#4C78A8")
ax[0].set_ylim(0, 100); ax[0].set_title("Honest: baseline at 0")

ax[1].bar(two["region"], two["digital_adoption_pct"], color="#E45756")
ax[1].set_ylim(55, 75); ax[1].set_title("Distorted: truncated baseline")

# Visual ratio on the truncated chart (bar heights above the clipped baseline):
vis_ratio = (b - 55) / (a - 55)
print(f"data ratio={data_ratio:.2f}  visual ratio(truncated)={vis_ratio:.2f}  "
      f"lie factor={vis_ratio / data_ratio:.1f}x")
plt.tight_layout(); plt.savefig("out/m1_lie_factor.png", dpi=150)
```

## Hands-on Lab 1 — Perception Audit and Five Encodings

| | |
|---|---|
| **Objective** | Encode a single Tayseer metric five different ways, rank the encodings by decoding accuracy for a stated task, and run a pre-attentive audit on a supplied "bad" dashboard |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, Jupyter, `pip install pandas matplotlib seaborn`; `data/tayseer_services.csv` and `assets/bad_dashboard_m1.png` provided; `git checkout lab1_start` (or open `lab1_start.ipynb`) |

**Instructions & tasks**

1. *(5 min)* Load `tayseer_services.csv`; compute latest-month `digital_adoption_pct` by region. State the task in one sentence: *"Let a Deputy Minister rank the 13 regions and spot the laggards."*
2. *(15 min)* Encode that same series five ways: (a) sorted horizontal bar, (b) unsorted vertical bar, (c) pie chart, (d) bubble/area, (e) single-row heatmap. Save all five.
3. *(10 min)* For the stated task, rank your five charts from most to least effective and justify each ranking with the Cleveland–McGill hierarchy in a markdown cell.
4. *(10 min)* Take the supplied `bad_dashboard_m1.png` and write a perception audit: list every place a pre-attentive channel is wasted (borders, 3D, rainbow gridlines) and every place the signal is under-encoded.
5. *(5 min)* Produce one corrected chart that spends exactly one pre-attentive pop on the real message.
6. *(5 min)* Commit / save notebook as `lab1_solution.ipynb`.

**Expected output**
```
Task: rank 13 regions on digital adoption, spot laggards.
Ranking of my five encodings (best→worst) with reason:
1. sorted bar      — position on common scale (rank 1), sorted = ranking is free
2. unsorted bar    — same channel, but eye must search for order
3. single heatmap  — saturation (rank 7); pattern OK, exact rank guesswork
4. bubble/area     — area (rank 5); Najran vs Jazan indistinguishable
5. pie             — angle (rank 4) + 13 slices = unreadable
Audit of bad_dashboard_m1.png: 7 wasted pre-attentive channels, signal under-encoded (see cells 9-12).
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Pie chart "looks fine to me" | Only 4–5 regions shown; distortion hides at low N | Plot all 13; the argument becomes self-evident |
| Bars all similar height, "no story" | Truncated/auto axis exaggerated differences before | Set `ylim(0, 100)`; discuss whether the story survives honesty |
| Heatmap looks most impressive | Confusing salience with accuracy | Re-ask: could you read the *exact* rank of region #6? |
| Region names overlap on X axis | Vertical bars with long Arabic/English labels | Use horizontal bars — a perception fix, not just cosmetic |

**Instructor notes.** The intended "aha" is that the *sorted bar*, the least flashy chart, wins — because it matches channel accuracy to task. Walk the room and find someone who ranked the heatmap #1; use them (kindly) to surface the salience-vs-accuracy confusion for everyone. Fast finishers: have them add a pre-attentive highlight to the sorted bar (one red laggard) as a bridge to Module 3.

## Mini Exercises

**Quiz (5 questions)**
1. Rank these by decoding accuracy for exact values: area, position on common scale, angle, length. → position > length > angle > area.
2. Which processing stage lets you find one red dot among grey instantly? → pre-attentive.
3. May a *line* chart truncate its Y axis? A *bar* chart? → line yes (encodes slope/position), bar no (encodes length from zero).
4. Why is a 3D bar chart never acceptable in analytics? → perspective/volume distortion changes apparent value with viewing angle; depth encodes nothing.
5. A task needs only "hot vs cold across a 13×6 matrix." Is a heatmap legitimate? → yes — exact decoding is not the task; saturation conveys pattern.

**Chart-critique exercise.** Project `critique_m1.png` (a 3D exploded pie of Tayseer channel mix). Each pair writes ≥4 critique comments naming the *perceptual* failure and a one-line fix each. Compare against the instructor's model critique.

**Before/after redesign (mini).** Give participants a truncated-axis bar chart of adoption by region. In 10 minutes, redesign it honestly (baseline at 0, sorted, one highlight) and compute the lie factor of the original.

**Discussion questions.**
- Your executive sponsor insists on pie charts "because the board likes them." How do you win this without a fight? (offer a sorted bar labelled with the same percentages; let comprehension speed decide)
- When is colour saturation the *right* primary channel, not a compromise? (dense matrices where pattern, not exact value, is the task)

## Case Study — The Misread Quarterly Review at a National Program Office

**Scenario.** The Tayseer program office presents quarterly to a Steering Committee chaired by a Deputy Minister. Last quarter's deck used a 3D exploded pie for channel mix and a dual-axis line for satisfaction-vs-cost. The committee misjudged branch usage and inferred a false causal link between cost and satisfaction, nearly approving a budget increase for the wrong reason.

**Business context.** The program is a Vision 2030 flagship; its budget re-allocation decisions move tens of millions of riyals and are audited. A chart that misleads the committee is not a cosmetic issue — it is a governance and public-money issue.

**Technical challenge.** Diagnose *why* each chart misled (perceptually, not stylistically) and specify honest replacements that a non-technical committee reads correctly in seconds.

**Constraints.** The committee has ~15 minutes total; no interactive tooling in the room (static slides); charts must work in both Arabic and English versions of the deck; the underlying numbers may not be changed — only the encoding.

**Solution approach (facilitate, don't lecture).** (1) Name the perceptual failure of each chart using the accuracy hierarchy. (2) Replace the pie with a single sorted/stacked bar; replace the dual axis with two indexed lines (base = 100) or two small multiples. (3) Move the message into the chart title. (4) Verify the redesign passes a 5-second comprehension test with a colleague who has not seen the data.

**Discussion questions.**
1. Which single chart in the old deck caused the most decision risk, and why?
2. Why does the indexed-line redesign remove the false-causality reading that the dual axis created?
3. The sponsor "loves" the 3D pie. What one-sentence business argument retires it?
4. How would you prove to an auditor that the redesign is a faithful representation of the same data?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Time to correctly rank top-3 laggard regions | Comprehension | < 5 s from a sorted bar | Stopwatch peer test |
| Encoding-accuracy quiz score | Knowledge | ≥ 4/5 | Quiz |
| Wasted pre-attentive channels in participant's chart | Design quality | 0 | Instructor audit |
| Lie factor of participant's final chart | Honesty | 1.0 (± 0.05) | Computed in notebook |
| Correct axis-truncation rule applied (bar vs line) | Knowledge | 100% | Lab review |

**Example benchmark table (filled during lab):**

| Chart | Task-match | Decode accuracy rank | 5-sec comprehension | Verdict |
|---|---|---|---|---|
| 3D exploded pie (original) | poor | 5–6 | fail | reject |
| Sorted horizontal bar (redesign) | excellent | 1 | pass | ship |
| Single-row heatmap | pattern-only | 7 | partial | supporting view only |

## Required Visuals and Training Assets

### Diagrams
1. **Encoding-accuracy staircase** — *Purpose:* anchor image for the whole course. *Elements:* a descending staircase from "Position (common scale)" down to "Colour saturation", each step labelled with an example chart and a decoding-accuracy note; a green zone (top) and red zone (bottom). *Style:* flat vector, English labels with Arabic subtitles. *Designer description:* "Seven descending steps, top step brightest, each step holds a small chart icon; arrow labelled 'accuracy decreases' running down the side."
2. **Pre-attentive attributes grid** — *Purpose:* memorisable reference. *Elements:* a 2×5 grid of the pre-attentive channels (hue, size, orientation, length, position, shape, enclosure, added marks, motion, intensity), each cell a tiny "spot the odd one out" mini-demo. *Style:* printable A4 poster.
3. **Lie-factor before/after** — *Purpose:* make distortion tangible. *Elements:* the same two bars shown honestly (baseline 0) and distorted (truncated), with the computed lie factor between them. *Style:* side-by-side split panel.
4. **Task-to-channel decision strip** — *Purpose:* Lab 1 / Module 2 bridge. *Elements:* seven analytical questions each mapped by an arrow to its best encoding and chart. *Style:* horizontal flow strip.

### Images (screenshots)
1. **"Find the 3" pre-attentive demo — plain vs highlighted**: *why:* the opening gasp moment; *content:* two grids, one all-grey digits, one with red 3s.
2. **Notebook screenshot — `m1_encoding_contrast.png` output**: *why:* expected-output reference for Lab 1; *content:* colour-encoded vs position-encoded ranking side by side.
3. **Bad dashboard for the audit (`bad_dashboard_m1.png`)**: *why:* the audit target; *content:* a deliberately over-decorated dashboard with 3D, rainbow gridlines, truncated axes.
4. **Attention-pop bar (`m1_attention_pop.png`)**: *why:* shows one honest pre-attentive highlight; *content:* grey bars with a single red laggard and a message-carrying title.

### Simulations
1. **Truncated-axis manipulator** — *Setup:* a notebook slider that moves the bar-chart baseline from 0 upward and live-computes the lie factor. *Expected behaviour:* as the baseline rises, the apparent gap balloons while the data is unchanged. *Learning objective:* distortion is a design choice, and it is measurable.
2. **Encoding race** — *Setup:* the same 13 values shown in a random encoding (bar/pie/bubble/heatmap); participants race to rank the top 3 and their times are logged. *Expected behaviour:* position wins by a wide margin every run. *Learning objective:* accuracy hierarchy is empirical, not opinion.

### Interactive Activities
- **Perception audit round-table (15 min):** pairs exchange their Lab 1 corrected charts and score each other against a 10-item perception checklist; each pair reports one wasted-channel find.
- **"Rank the encodings" card sort (10 min):** seven printed chart cards (bar, line, pie, bubble, heatmap, scatter, 3D bar) physically sorted onto the accuracy staircase poster.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | Synthetic, generated by course tooling (realistic KSA regions, service categories, channels; seeded trends) | CSV | ~28,000 rows × 12 cols | The golden-thread dataset; used in every module and the capstone |
| `bad_dashboard_m1.png` | Course team (deliberately over-decorated) | PNG | 1 image | Perception-audit target |
| `data_dictionary.md` | Course team | Markdown | 1 page | Column definitions, units, and known seasonality for all labs |

### Demo Requirements
- **Instructor demo:** live-build the colour-vs-position contrast (subsection 1 code) in under 6 minutes; the moment the sorted bar renders and the room can instantly rank the regions *is* the message.
- **Student demo:** two volunteer pairs present their five-encoding ranking at end of Hour 3; the class challenges one ranking decision each.
- **Expected outputs:** a saved `m1_attention_pop.png`, a written perception audit, and a lie-factor computation of 1.0 on the corrected chart.

---

# Module 2 — Chart Selection and Design Principles

## Module Overview

**Purpose.** Module 1 established *how* the eye decodes marks; this module turns that into a repeatable decision procedure: given an analytical question and a data shape, which chart type is correct, and how do you compose it so the data — not the decoration — carries the meaning. The goal is to replace "what chart looks nice?" with "what chart does this comparison require?" — a shift from decoration to argument.

**Business relevance.** Analysts waste enormous time re-styling the wrong chart. A team that can choose the right chart in ten seconds, and knows the five design principles that make any chart readable, ships analysis at a pace that keeps up with decisions. In a national-program context, chart selection is also a trust signal: a committee that sees the *right* chart for each question learns to trust the analyst; a committee that sees a wall of default Excel pies learns to discount the analysis.

**Industry use cases.**
- A demand-planning team must show forecast vs actual over 24 months — a line chart with a clear reference band, never clustered bars.
- A retail analytics team compares conversion across 40 stores — a sorted dot plot, not a 40-slice pie or a rainbow bar.
- A public-health dashboard shows the distribution of clinic wait times — a box or strip plot that reveals the spread and outliers, not a single average bar that hides them.

**Expected competencies.** After this module a participant can select the correct chart family for any of the common analytical questions, apply the five core design principles (baseline, sorting, direct labelling, reference lines, small multiples), avoid the classic chart-selection traps, and build the chosen chart correctly in matplotlib/Plotly.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Map an analytical question to the correct chart family | LO1 |
| 2.2 | Apply the five core design principles to any chart | LO2 |
| 2.3 | Use small multiples to compare across a dimension without clutter | LO2 |
| 2.4 | Avoid chart-selection anti-patterns (clustered bars, spaghetti lines, dual axes) | LO2 |
| 2.5 | Build the selected chart correctly and honestly in code | LO1, LO2 |

## Technical Content

### 1. The chart-selection decision procedure

Chart choice is a function of the *question*, moderated by the *data shape*. Teach this as a two-step lookup, not a chart gallery:

**Step 1 — name the question type:** comparison, trend-over-time, distribution, relationship, part-to-whole, or geospatial. **Step 2 — apply the data shape** (how many categories, how many series, how many points) to pick within the family.

| Question type | Default chart | If many categories | If many series |
|---|---|---|---|
| Comparison (ranking) | Sorted bar / dot plot | Dot plot (compact) | Small multiples |
| Trend over time | Line chart | Small multiples | Highlight one, grey the rest |
| Distribution | Histogram / box | Violin / strip | Ridgeline / faceted box |
| Relationship | Scatter | Scatter + trend | Faceted scatter |
| Part-to-whole | 100% stacked bar | Treemap (carefully) | Small-multiple stacked bars |
| Geospatial *how-much* | Sorted bar first, map second | Bar + supporting map | — |

The recurring insight: **"too many" is a design signal, not a licence to cram.** When a comparison has 40 categories or a line chart has 13 overlapping series (one per region — exactly the Tayseer case), the answer is small multiples or highlight-one, never a denser single chart.

### 2. The five core design principles

Every chart in this course obeys five principles. They are the design equivalent of Module 1's encoding rules:

1. **Honest baseline.** Bars start at zero; if you must show small differences, switch to a dot plot or a line, do not truncate a bar (Module 1).
2. **Sort by value, not alphabetically.** A sorted bar makes ranking free; alphabetical order forces serial search. Sort unless the category has an inherent order (time, age bands).
3. **Direct labelling over legends.** Put the series name at the end of its line; kill the legend. Every legend is a round trip the reader's eye must make; direct labels remove it.
4. **Reference lines and bands.** A target, an average, or a "national mean" line turns a chart of numbers into a chart of *judgements* ("above/below target"). This is where analysis becomes decision-support.
5. **Small multiples for a third dimension.** Instead of cramming region × time × channel into one chart, repeat a small chart across the categories of one dimension. The eye compares shapes across a grid effortlessly.

### 3. Small multiples: the anti-clutter workhorse

Small multiples (also "trellis" or "faceting") repeat the same chart, same scales, across the levels of one categorical variable. For Tayseer, "digital adoption trend for each of 13 regions" is unreadable as 13 overlapping lines (spaghetti) but immediately legible as a 13-panel grid of identical small line charts sharing one Y-axis. The rules: **shared scales** (so panels are comparable), **consistent ordering** (sort panels by a summary statistic, e.g. latest value), and **one highlight colour** if a reference is needed. Small multiples trade a little space for an enormous gain in comparability — usually the right trade for an analyst's exploratory view and often for the final view too.

### 4. Chart-selection anti-patterns

Name and forbid these explicitly; each appears in a Lab 2 starter chart deliberately:

- **Clustered ("grouped") bars beyond 2–3 series:** the eye cannot track a category across clusters. Use small multiples or a slope chart.
- **Spaghetti line charts:** >5 overlapping lines. Highlight one and grey the rest, or facet.
- **Dual-axis charts** (Module 1): manufacture correlation. Use indexed lines.
- **Stacked bars for comparison of non-first segments:** only the bottom segment sits on a common baseline; the rest float and cannot be compared. Fine for part-to-whole totals, wrong for comparing middle segments.
- **Pie charts for anything but a single "half vs rest" split** (Module 1).
- **Choropleth as the primary "how much" view:** area and colour dominate; big empty regions (geographically large, low population) shout. Lead with a sorted bar; use the map as a locator.

### 5. Composition, alignment, and the reading path

Beyond the single chart, composition guides the eye:

- **Aspect ratio matters.** "Bank to 45°" — line-chart trends read most accurately when the average slope of the line is near 45 degrees; a too-flat or too-tall aspect ratio hides or exaggerates the trend.
- **Alignment and a single reading direction.** Left-to-right, top-to-bottom for LTR decks; **right-to-left** for Arabic decks — including the *order of bars and the direction of the time axis*. A time axis running left-to-right in an Arabic slide reads backwards to the audience; this is a frequent, avoidable error in bilingual Saudi decks.
- **Title as the takeaway.** The chart title states the *conclusion* ("Digital adoption crossed 65% nationally, but three regions stalled"), not the *topic* ("Digital adoption by region"). This single habit does more for executive comprehension than any styling.

### 6. Common mistakes & production considerations

1. Choosing the chart before naming the question — leads to re-styling the wrong chart.
2. Sorting alphabetically or by the data's incidental order.
3. Keeping default legends when direct labelling is possible.
4. No reference line, so the reader cannot tell good from bad.
5. Fixed single-chart thinking where small multiples are the answer.
6. Ignoring RTL layout for Arabic audiences.

Production: standardise a **chart component library** (a `viz/` module of functions like `sorted_bar()`, `trend_lines()`, `small_multiples()`) so every analyst produces consistent, principle-compliant charts; this is the visual analogue of a shared feature module and pays off exactly as much.

## Code Examples

### A reusable, principle-compliant sorted bar

```python
# src/viz/charts.py
"""Course chart library: every function bakes in the five design principles.
Analysts call these instead of raw matplotlib so consistency is automatic."""
import matplotlib.pyplot as plt
import pandas as pd


def sorted_bar(data: pd.DataFrame, cat: str, val: str, *,
               highlight: str | None = None, title: str = "",
               reference: float | None = None, ax=None):
    """Horizontal sorted bar with honest baseline, direct value labels,
    optional single highlight and reference line."""
    d = data.sort_values(val)
    ax = ax or plt.subplots(figsize=(8, 5))[1]
    colors = ["#E45756" if c == highlight else "#B8C4D9" for c in d[cat]]
    ax.barh(d[cat], d[val], color=colors)
    ax.set_xlim(0, max(d[val]) * 1.15)               # principle 1: baseline at 0
    for y, v in enumerate(d[val]):                    # principle 3: direct labels
        ax.text(v + max(d[val]) * 0.01, y, f"{v:.0f}", va="center", fontsize=9)
    if reference is not None:                          # principle 4: reference line
        ax.axvline(reference, color="#333", ls="--", lw=1)
        ax.text(reference, len(d) - 0.3, "national mean", fontsize=8, color="#333")
    ax.set_title(title, loc="left", fontsize=13, weight="bold")  # takeaway title
    ax.spines[["top", "right"]].set_visible(False)
    return ax
```

### Small multiples: 13 regional trends without spaghetti

```python
# notebooks/m2_chart_selection.ipynb
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])

# Monthly national-vs-region adoption; ONE line per region is spaghetti (13 lines).
# Small multiples make the SAME data instantly comparable.
monthly = (df.groupby(["region", "month"], as_index=False)["digital_adoption_pct"]
             .mean())

# Order panels by latest value so the grid itself encodes ranking.
order = (monthly[monthly.month == monthly.month.max()]
         .sort_values("digital_adoption_pct", ascending=False)["region"].tolist())

g = sns.relplot(
    data=monthly, x="month", y="digital_adoption_pct",
    col="region", col_wrap=4, col_order=order,
    kind="line", height=1.8, aspect=1.3, color="#4C78A8",
    facet_kws={"sharey": True},                       # shared scale = comparable
)
national = monthly.groupby("month")["digital_adoption_pct"].mean()
for ax in g.axes.flat:                                # reference: national mean
    ax.plot(national.index, national.values, color="#D3D3D3", lw=1, zorder=0)
    ax.axhline(65, color="#E45756", ls="--", lw=0.8)  # target line
g.set_titles("{col_name}")
g.set_axis_labels("", "Adoption %")
g.fig.suptitle("Digital adoption trend by region (target = 65%)", y=1.02,
               ha="left", x=0.05, weight="bold")
g.savefig("out/m2_small_multiples.png", dpi=150)
```

### Killing a dual axis with indexed lines

```python
# Instead of satisfaction (1-5) on a left axis and cost (SAR) on a right axis
# (which manufactures a crossing), index BOTH to their first month = 100.
import matplotlib.pyplot as plt

nat = (df.groupby("month")[["csat", "cost_per_txn_sar"]].mean())
idx = nat / nat.iloc[0] * 100                          # common base = 100

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(idx.index, idx["csat"], color="#4C78A8", lw=2)
ax.plot(idx.index, idx["cost_per_txn_sar"], color="#E45756", lw=2)
ax.text(idx.index[-1], idx["csat"].iloc[-1], " Satisfaction", color="#4C78A8",
        va="center", weight="bold")                    # direct labels, no legend
ax.text(idx.index[-1], idx["cost_per_txn_sar"].iloc[-1], " Cost/txn",
        color="#E45756", va="center", weight="bold")
ax.axhline(100, color="#999", lw=0.8)
ax.set_title("Since program start: satisfaction up 12%, cost per transaction down 34%",
             loc="left", weight="bold")
ax.spines[["top", "right"]].set_visible(False)
fig.savefig("out/m2_indexed_lines.png", dpi=150)
# Teaching point: indexing makes the two series honestly comparable on ONE axis.
```

## Hands-on Lab 2 — Chart Chooser and the First Honest Charts

| | |
|---|---|
| **Objective** | For four real Tayseer questions, select the correct chart via the decision procedure and build each one honestly in matplotlib/Plotly using the course chart library |
| **Duration** | 50 minutes |
| **Setup** | `pip install pandas matplotlib seaborn plotly`; `src/viz/charts.py` starter provided; `git checkout lab2_start` |

**Instructions & tasks**

1. *(5 min)* Read the four questions in `lab2_questions.md`: (Q1) which regions lag on adoption? (Q2) how has national adoption trended? (Q3) how does completion time vary by service category? (Q4) how do satisfaction and cost relate across regions?
2. *(10 min)* For each question, write the question-type and chosen chart in a markdown cell, justified by the decision table. (Expected: Q1 sorted bar, Q2 line, Q3 box/strip, Q4 scatter.)
3. *(20 min)* Build all four using `charts.py` where applicable; apply all five design principles; give every chart a takeaway title.
4. *(5 min)* Add a reference line to Q1 (national mean) and Q2 (target 65%).
5. *(5 min)* Convert Q2 to an interactive Plotly line as a preview of Module 4; hover shows exact monthly value.
6. *(5 min)* Save as `lab2_solution.ipynb`; export the four charts to `out/`.

**Expected output**
```
Q1 -> sorted_bar (comparison/ranking): Najran, Jazan, Al-Bahah below national mean
Q2 -> line (trend): national adoption 41% -> 68% over the period, crosses 65% in month 21
Q3 -> box plot (distribution): 'social support' has the widest spread + high outliers
Q4 -> scatter (relationship): weak negative cost~satisfaction; Riyadh is an outlier
All four charts: baseline honest, sorted where applicable, direct-labelled, titled with the takeaway.
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Q3 built as a bar of averages | Averaged away the distribution | A distribution question needs a box/strip; the average hides the spread |
| Q1 alphabetical | Forgot to sort by value | `sort_values(val)`; sorting *is* the analysis |
| Line chart looks flat / no trend | Bad aspect ratio | Widen the figure; "bank to 45°" |
| Legend covers the plot | Kept default legend | Direct-label the last point; remove legend |
| Arabic labels reversed | Default LTR layout | Set RTL / mirror axis for the Arabic export (foreshadows M3) |

**Instructor notes.** The highest-value moment is Q3: many will default to a bar of average completion time and be genuinely surprised that a box plot reveals a completely different story (the outliers). Let that surprise land — it teaches "the chart choice changes the conclusion." Fast finishers: build the Q1 sorted bar as a small-multiples version faceted by channel.

## Mini Exercises

**Quiz (5 questions)**
1. Question: "compare 40 store conversion rates." Chart? → sorted dot plot (compact ranking), not pie/clustered bar.
2. When are clustered bars acceptable? → 2–3 series max; beyond that use small multiples or slope charts.
3. Why direct-label instead of a legend? → removes the eye's round trip between legend and data.
4. What does a reference line convert a chart *into*? → a chart of judgements (above/below target), i.e. decision-support.
5. 13 overlapping regional lines — fix? → small multiples (shared scale, sorted panels) or highlight-one.

**Chart-critique exercise.** Project `critique_m2.png` (a clustered bar chart with 6 series × 13 regions). Each pair names the selection failure and proposes the correct chart with a one-line reason.

**Before/after redesign.** Give a spaghetti line chart (13 regional adoption lines). In 12 minutes, redesign as small multiples *or* highlight-one; state which and why. Capture the reduction in "time to find the laggard region."

**Discussion questions.**
- When is a choropleth map the *right* primary chart, and when is it a trap? (right for genuinely spatial patterns/routing; trap for ranking "how much")
- Your stakeholder wants "everything on one slide." How do small multiples honour that without cramming? (one comparable grid reads as a single gestalt)

## Case Study — Choosing Charts for a Regional Service-Performance Review

**Scenario.** The Tayseer analytics team must produce a one-page regional performance review comparing all 13 regions across four metrics (adoption, satisfaction, completion time, cost) for the operations directorate. The first draft is four clustered bar charts, each with 13 bars × 4 colours — visually loud, analytically unreadable.

**Business context.** The operations directorate uses this page monthly to decide where to send improvement teams. If the page is unreadable, the decision defaults to "wherever complained loudest", not "wherever the data points."

**Technical challenge.** Present four metrics × 13 regions on one page such that a reader can (a) rank regions on any metric and (b) spot a region that is good on one metric but bad on another — all in under a minute.

**Constraints.** One page (print + screen); works in Arabic and English; no interactivity (it is printed and tabled); colour-blind-safe; the four metrics have different units and directions (lower cost is good, higher satisfaction is good).

**Solution approach (facilitate, don't lecture).** (1) Replace four clustered bars with four small-multiple columns of sorted dot plots, one column per metric, regions on a shared row order (sorted by adoption). (2) Add a national-mean reference line to each. (3) Encode "good/bad direction" consistently (e.g., a subtle green/grey where the region beats the mean). (4) A single takeaway title per column. The shared row order lets the eye scan across a region's four dots to see its profile.

**Discussion questions.**
1. Why does a shared region order across the four panels enable the "good here, bad there" reading that four independent charts destroy?
2. How do you handle "lower is better" (cost, completion time) so all four columns read consistently?
3. What would you lose, and gain, by making this interactive instead? (gain drill-down; lose print-ability and the at-a-glance whole)
4. How do you keep the page colour-blind-safe while still signalling direction?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Correct chart family chosen for 4 questions | Selection skill | 4/4 | Lab review |
| Design principles applied per chart | Design quality | 5/5 | Principle checklist |
| Time to find laggard region (small multiples) | Comprehension | < 8 s | Peer stopwatch |
| Charts with a takeaway (not topic) title | Communication | 100% | Instructor review |
| Anti-patterns present in final charts | Design quality | 0 | Audit |

**Example benchmark table (filled during lab):**

| Question | Chosen chart | Principles applied | Anti-pattern avoided | Verdict |
|---|---|---|---|---|
| Q1 ranking | Sorted bar | 5/5 | not a pie | ship |
| Q2 trend | Line + target | 5/5 | not clustered bars | ship |
| Q3 distribution | Box plot | 4/5 (add labels) | not a mean bar | revise labels |
| Q4 relationship | Scatter + trend | 5/5 | not dual-axis | ship |

## Required Visuals and Training Assets

### Diagrams
1. **Chart-selection decision tree** — *Purpose:* the module's spine. *Elements:* start node "What is the question?" branching to six question-types, each to its default chart and the "if too many" fallback. *Style:* clean flowchart, English + Arabic labels. *Designer description:* "Top node question mark, six coloured branches to chart icons, small 'small-multiples' escape hatch on the crowded branches."
2. **Five design principles poster** — *Purpose:* pin-up reference. *Elements:* five numbered panels (baseline, sort, direct label, reference line, small multiples), each a tiny before/after. *Style:* printable A4.
3. **Spaghetti → small multiples transformation** — *Purpose:* motivate faceting. *Elements:* left: 13 tangled lines; right: 13 clean panels. *Style:* before/after split.
4. **Anti-pattern rogues' gallery** — *Purpose:* recognition training. *Elements:* clustered bars, dual axis, 3D pie, spaghetti, floating stacked segments — each with a red stamp and the correct alternative. *Style:* grid of six.

### Images (screenshots)
1. **`m2_small_multiples.png` output**: *why:* Lab 2 reference; *content:* the 13-panel regional adoption grid with target line.
2. **`m2_indexed_lines.png` output**: *why:* the dual-axis fix; *content:* satisfaction and cost indexed to 100, direct-labelled.
3. **Clustered-bar starter (`critique_m2.png`)**: *why:* critique target; *content:* an unreadable 6×13 clustered bar.
4. **The four-panel regional review (case study)**: *why:* worked solution; *content:* four sorted dot-plot columns sharing region order with mean lines.

### Simulations
1. **Aspect-ratio "bank to 45°" slider** — *Setup:* a notebook slider changing a line chart's aspect ratio while showing the average slope. *Expected behaviour:* trend appears/disappears with aspect; near 45° reads truest. *Learning objective:* aspect ratio is a perception decision, not a default.
2. **"Too many series" escalator** — *Setup:* incrementally add regional lines to one chart (2 → 5 → 13). *Expected behaviour:* readability collapses past ~5; the small-multiples version stays readable. *Learning objective:* clutter is a threshold, and small multiples are the release valve.

### Interactive Activities
- **Chart-chooser speed round (10 min):** the instructor calls out analytical questions; pairs hold up the correct chart card within 5 seconds; mis-picks are discussed.
- **Small-multiples build-off (15 min):** pairs race to convert the same spaghetti chart to small multiples; fastest correct build presents its ordering choice.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | (as Module 1 — same golden thread) | CSV | ~28,000 rows | Source for all four Lab 2 questions |
| `lab2_questions.md` | Course team | Markdown | 1 page | The four analytical questions to answer |
| `src/viz/charts.py` | Course team (starter with `sorted_bar` stub) | Python | ~1 file | Reusable chart library extended through the course |

### Demo Requirements
- **Instructor demo:** live-convert the spaghetti regional line chart to small multiples in under 7 minutes; the readability jump is the message.
- **Student demo:** two pairs present their Q3 chart; the class debates whether a box plot or a strip plot serves the operations directorate better.
- **Expected outputs:** four principle-compliant charts with takeaway titles, plus one interactive Plotly line as an M4 preview.

---

# Module 3 — Colour, Annotation, and Decluttering

## Module Overview

**Purpose.** With the right chart chosen (M2), this module is about finishing craft: using colour as meaning rather than decoration, using annotation to make the argument explicit, and stripping everything that does not carry information. This is where a technically-correct chart becomes a *persuasive* one — and where the largest, cheapest gains in clarity live. Decluttering and annotation routinely improve comprehension more than any change of chart type.

**Business relevance.** Colour is the most abused channel in enterprise reporting: rainbow categorical palettes, red/green that excludes colour-blind viewers (roughly 1 in 12 men), and saturation used decoratively. In a Saudi government or banking context, a chart that fails accessibility or mis-signals with colour is both a comprehension failure and, increasingly, a compliance one. Annotation — the explicit "this is the point" callout — is what lets a chart survive being forwarded without its presenter.

**Industry use cases.**
- An executive scorecard must use one accent colour for "needs attention" and grey for everything else, so the eye lands on the exception.
- A public-facing Vision 2030 progress chart must be colour-blind-safe and readable in both Arabic and English.
- A monitoring dashboard uses a diverging palette centred on the SLA target so "above/below" is pre-attentive.

**Expected competencies.** After this module a participant can choose the correct palette type (categorical, sequential, diverging) for a data type, build colour-blind-safe and brand-aligned palettes, apply annotation to state the takeaway on the chart, compute and improve the data-ink ratio, and handle Arabic/RTL and numeral conventions.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Choose the correct palette type (categorical/sequential/diverging) for the data | LO2 |
| 3.2 | Build colour-blind-safe, accessible, brand-aligned palettes | LO2 |
| 3.3 | Use annotation to make a chart's argument explicit | LO2, LO4 |
| 3.4 | Increase the data-ink ratio by removing non-data ink | LO2 |
| 3.5 | Apply Arabic/RTL layout and numeral conventions correctly | LO2 |

## Technical Content

### 1. Colour as meaning: the three palette types

Colour must be chosen by the *data type*, not by aesthetics. There are exactly three palette families and using the wrong one lies to the reader:

| Data type | Palette | Example | Failure if wrong |
|---|---|---|---|
| **Categorical** (regions, channels) | Distinct hues, ≤ 7 | Channel = app/web/branch | A sequential palette implies a false order |
| **Sequential** (0 → high) | One hue, light → dark | Adoption 0–100% | A rainbow implies false category breaks |
| **Diverging** (below ↔ above a midpoint) | Two hues from a neutral centre | Cost vs target | A sequential palette hides the meaningful midpoint |

The two most common colour lies: using a rainbow (categorical) palette on ordered data, which invents category boundaries the data does not have; and using a sequential palette on data that has a meaningful centre (variance from target), which hides the "above/below" that is the entire point. Diverging palettes must be *centred on the meaningful value* — for Tayseer cost-vs-target, the neutral colour sits at the target, not at the data mean.

### 2. Accessibility and brand

- **Colour-blind safety:** ~8% of men have red-green colour vision deficiency. Never encode meaning by red-vs-green alone; add a second channel (position, shape, label) or use a colour-blind-safe palette (Okabe–Ito, viridis). Test with a simulator.
- **Never rely on colour alone.** Colour should be *redundant* with another cue for any critical distinction — the WCAG principle applied to charts.
- **Sufficient contrast** against the background for text and key marks.
- **Brand alignment:** in a national-program deck, align to the organisation's palette but do not let brand override function — reserve the brand accent for the *signal*, use greys for context. A common trap is using the full brand palette (five vivid colours) as a categorical scheme, which spends all the salience on chrome.

### 3. The data-ink ratio and decluttering

Tufte's **data-ink ratio** = data-ink ÷ total ink. Maximise it by erasing non-data ink, in this order (the "decluttering ladder"):

1. Remove chart junk: 3D, gradients, drop shadows, background images.
2. Remove or lighten gridlines; keep at most faint horizontal guides.
3. Remove the plot border/box; drop top and right spines.
4. Remove redundant axes and tick marks; label directly.
5. Remove the legend (direct-label instead).
6. Mute everything that is context to grey; reserve saturation for the signal.

Decluttering is not minimalism for its own sake — every erased element frees attention for the data. The test: remove an element; if the chart still answers its question, the element was junk.

### 4. Annotation: making the argument explicit

An unannotated chart says "here is some data"; an annotated chart says "here is what it means." Annotation types to teach:

- **Takeaway title** (from M2): the conclusion, top-left, bold.
- **Callout annotations:** a short text + leader line pointing at the specific data point that carries the argument ("Najran plateaued after the March outage").
- **Reference lines/bands** (from M2): target, average, acceptable range.
- **Highlight + mute:** the pre-attentive pop (M1) — one series in colour, the rest grey — combined with a label.
- **Direct value labels** where exact numbers matter (executive audiences want the number *and* the shape).

The design rule: **annotate the point you are making, not everything.** One or two annotations that state the argument beat twenty that restate the axis.

### 5. Arabic, RTL, and numeral conventions

For a Saudi executive audience this is not optional polish:

- **Right-to-left reading order.** In an Arabic chart the natural scan is right-to-left; a categorical/ranking axis should be ordered so the "first/best" sits on the right, and a **time axis should run right-to-left** (earliest on the right). A left-to-right time axis reads backwards to an Arabic-first audience.
- **Bilingual labelling.** Decide a convention (Arabic primary with English secondary, or matched pairs) and apply it consistently; mixing directions within one deck is the tell of a rushed job.
- **Numerals.** Choose Arabic-Indic (٠١٢٣) or Western Arabic (0123) numerals deliberately and consistently; Saudi government decks commonly use Western Arabic numerals in analytics but Arabic-Indic in formal text — confirm the house style.
- **Font and text rendering.** Ensure the plotting stack renders Arabic glyphs and joins correctly (matplotlib needs an Arabic-capable font plus a reshaper/bidi step); broken, disconnected Arabic letters are worse than English-only.

### 6. Common mistakes & production considerations

1. Rainbow palette on ordered/sequential data.
2. Red/green as the only distinction (colour-blind exclusion).
3. Diverging palette not centred on the meaningful midpoint.
4. Decoration ink (gridlines, borders, shadows) dominating data ink.
5. No annotation — the reader must infer the point.
6. LTR time axis in an Arabic deck; broken Arabic glyphs.

Production: encode the organisation's palette and RTL settings into the `viz/` library and a matplotlib/Plotly theme (`style.mplstyle`, Plotly template) so accessibility and brand are defaults, not per-chart heroics. Ship a colour-blind simulation check in the review process.

## Code Examples

### A colour-blind-safe theme and palette helpers

```python
# src/viz/theme.py
"""Course visual theme: accessible defaults so every chart is brand + a11y safe.
Set once; every chart inherits it."""
import matplotlib.pyplot as plt

# Okabe-Ito: colour-blind-safe categorical palette.
CATEGORICAL = ["#0072B2", "#E69F00", "#009E73", "#CC79A7",
               "#56B4E9", "#D55E00", "#F0E442"]
GREY = "#B8B8B8"          # context colour
ACCENT = "#D55E00"        # reserve for the ONE signal
SEQUENTIAL = "Blues"      # single-hue, light->dark
DIVERGING = "RdBu_r"      # two-hue, centre on the meaningful midpoint


def apply_theme():
    plt.rcParams.update({
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": "#EEEEEE", "grid.linewidth": 0.8,
        "axes.titlelocation": "left", "axes.titleweight": "bold",
        "figure.dpi": 130, "font.size": 11,
    })


def highlight_palette(categories, signal):
    """One accent for the signal category, grey for context (M1 pop, M3 colour)."""
    return [ACCENT if c == signal else GREY for c in categories]
```

### Diverging palette centred on the target (cost vs SLA)

```python
# notebooks/m3_colour_declutter.ipynb
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
from src.viz.theme import apply_theme, DIVERGING
apply_theme()

df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])
latest = (df[df.month == df.month.max()]
          .groupby("region", as_index=False)["cost_per_txn_sar"].mean())

TARGET = 18.0                                   # SAR per transaction, program target
# Diverging colour CENTRED on the target: below target = blue (good), above = red.
norm = mcolors.TwoSlopeNorm(vmin=latest.cost_per_txn_sar.min(),
                            vcenter=TARGET,
                            vmax=latest.cost_per_txn_sar.max())
cmap = plt.get_cmap(DIVERGING)
s = latest.sort_values("cost_per_txn_sar")
colors = [cmap(norm(v)) for v in s.cost_per_txn_sar]

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(s.region, s.cost_per_txn_sar, color=colors)
ax.axvline(TARGET, color="#333", ls="--", lw=1)
ax.text(TARGET, len(s) - 0.4, " target 18 SAR", fontsize=9)
ax.set_title("Five regions still exceed the 18 SAR cost-per-transaction target",
             fontsize=13)
ax.set_xlabel("Cost per transaction (SAR)")
fig.savefig("out/m3_diverging_cost.png", dpi=150)
```

### Before/after declutter with annotation

```python
# The "after": muted context, one accent series, callout annotation, no junk.
monthly = (df.groupby(["region", "month"], as_index=False)["digital_adoption_pct"]
             .mean())
naj = monthly[monthly.region == "Najran"]
others = monthly[monthly.region != "Najran"]

fig, ax = plt.subplots(figsize=(9, 5))
for r, g in others.groupby("region"):           # context: grey, thin
    ax.plot(g.month, g.digital_adoption_pct, color="#DADADA", lw=1, zorder=1)
ax.plot(naj.month, naj.digital_adoption_pct, color="#D55E00", lw=2.5, zorder=3)
ax.text(naj.month.iloc[-1], naj.digital_adoption_pct.iloc[-1], " Najran",
        color="#D55E00", weight="bold", va="center")     # direct label

# Callout annotation: state the argument, point at the evidence.
outage = naj[naj.month == "2024-03-01"]
ax.annotate("Plateaued after the March 2024\nservice outage",
            xy=(outage.month.iloc[0], outage.digital_adoption_pct.iloc[0]),
            xytext=(0.35, 0.25), textcoords="axes fraction", fontsize=10,
            arrowprops=dict(arrowstyle="->", color="#555"))
ax.set_title("Najran's digital adoption stalled while every other region climbed",
             fontsize=13)
ax.set_ylabel("Adoption %")
fig.savefig("out/m3_after_annotated.png", dpi=150)
```

## Hands-on Lab 3 — Before/After Redesign

| | |
|---|---|
| **Objective** | Take a deliberately cluttered, mis-coloured Tayseer chart and redesign it: correct palette, decluttered, annotated with the takeaway; measure the improvement |
| **Duration** | 50 minutes |
| **Setup** | `apply_theme()` from `src/viz/theme.py`; `assets/cluttered_m3.png` and its source data provided; `git checkout lab3_start` |

**Instructions & tasks**

1. *(5 min)* Study `cluttered_m3.png` (rainbow 3D bars, heavy gridlines, red/green channel colours, no title, legend covering the plot). List every violation.
2. *(10 min)* Rebuild the chart honestly: choose the correct palette type; if the data is sequential/diverging, fix it.
3. *(10 min)* Apply the decluttering ladder: remove junk, lighten gridlines, drop spines, remove the legend via direct labels.
4. *(10 min)* Add annotation: a takeaway title and exactly one callout pointing at the argument.
5. *(5 min)* Run a colour-blind simulation on your result (`assets/cvd_sim.py`) and fix any red/green-only distinction.
6. *(5 min)* Produce an Arabic version with RTL axis ordering and a correctly-rendered Arabic title.
7. *(5 min)* Compute the improvement: count data-ink vs total-ink elements before/after; note the time-to-takeaway change from a peer.

**Expected output**
```
Violations found in cluttered_m3.png: 9 (3D, rainbow-on-ordered, red/green, legend overlap, no title,
   heavy gridlines, plot border, truncated axis, duplicate axis labels).
After: sequential Blues palette, spines off, gridlines faint, direct labels, 1 callout, takeaway title.
Colour-blind sim: passed (distinction no longer relies on hue alone).
Arabic version: time axis runs right-to-left, Arabic title renders joined correctly.
Data-ink elements before: 6 data / 22 total.  After: 6 data / 8 total.  Peer time-to-takeaway: 14s -> 4s.
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Arabic text shows disconnected letters | No reshaper/bidi step | `arabic_reshaper` + `python-bidi` before setting the string; Arabic-capable font |
| Diverging colours look off-centre | `vcenter` at data mean, not target | Set `TwoSlopeNorm(vcenter=TARGET)` |
| Chart still "busy" after declutter | Removed data ink, kept junk | Re-run the ladder in order; junk first, then lighten, never remove data |
| Colour-blind sim still fails | Distinction is hue-only | Add a second channel: position, label, or shape |
| Callout clutters the plot | Too many annotations | One argument = one callout; move the rest to the title |

**Instructor notes.** This is the module's signature exercise and the highest-satisfaction moment of the course — participants routinely photograph their before/after. Enforce the "one callout" rule strictly; the instinct is to annotate everything, which recreates clutter. The Arabic-rendering step catches almost everyone the first time — budget floater support. Fast finishers: theme the chart to a supplied brand palette while keeping accessibility.

## Mini Exercises

**Quiz (5 questions)**
1. Data is "variance from target." Which palette? → diverging, centred on the target.
2. Why is red/green-only encoding a defect? → excludes ~8% of men (colour-blindness); violates redundancy.
3. Data-ink ratio — how to raise it? → remove non-data ink (junk, gridlines, borders, legend) without touching data ink.
4. How many callout annotations should carry the argument? → one (maybe two); state the point, don't restate the axis.
5. In an Arabic chart, which way does the time axis run? → right-to-left (earliest on the right).

**Chart-critique exercise.** Project `critique_m3.png` (rainbow sequential heatmap + red/green table). Pairs name the colour lie and the accessibility failure, and propose the correct palette.

**Before/after redesign.** (The lab is itself the graded redesign.) Mini-version: hand a chart that is *only* mis-coloured (correct type, cluttered palette) and have participants fix palette + accessibility in 8 minutes.

**Discussion questions.**
- Brand guidelines mandate five vivid colours. How do you keep accessibility and signal-focus? (use brand accent for the signal, greys for context; don't use all five as categories)
- When is *more* ink justified — when is a gridline or annotation actually data-serving? (when reading exact values off the axis is the task; sparingly)

## Case Study — Making the National Progress Chart Accessible and Bilingual

**Scenario.** The Tayseer program's flagship "national digital adoption progress" chart appears in a public Vision 2030 update, in both Arabic and English. The current version uses a red-to-green gradient across regions and a left-to-right time axis in the Arabic edition; an accessibility review and an Arabic-first stakeholder both flagged it.

**Business context.** This is a public-facing artefact tied to a national program's credibility. An inaccessible or awkwardly-localised chart in a Vision 2030 communication is a reputational issue, not just a design nit.

**Technical challenge.** Redesign the chart to be colour-blind-safe, correctly localised for Arabic (RTL, numerals, glyphs), and still on-brand — without changing the underlying message.

**Constraints.** Must exist in matched Arabic and English versions; must pass a colour-blind simulator; must use the program's brand palette; numerals per government house style; renders correctly in the publishing pipeline (PDF + web).

**Solution approach (facilitate, don't lecture).** (1) Replace red-green with a colour-blind-safe sequential/diverging palette and add a redundant cue. (2) Build a proper RTL Arabic version (mirror the time axis, reshape/bidi the labels, set numerals). (3) Reserve the brand accent for the national trend line; grey the context. (4) Annotate the milestone (crossing 65%). (5) Verify both editions against the simulator and an Arabic-first reader.

**Discussion questions.**
1. Why is mirroring the *entire* time axis necessary, not just translating the labels?
2. Which redundant cue best replaces red/green here, and why?
3. How do you keep the Arabic and English editions provably identical in message?
4. Where does brand colour help, and where would it hurt comprehension?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Correct palette type for data type | Colour literacy | 100% | Lab review |
| Colour-blind simulator pass | Accessibility | Pass | `cvd_sim.py` |
| Data-ink ratio improvement | Decluttering | ≥ 2× fewer non-data elements | Element count |
| Argument-carrying annotations | Clarity | 1–2 (not 0, not 20) | Instructor review |
| Arabic RTL + glyph correctness | Localisation | Correct | Native-reader check |

**Example benchmark table (filled during lab):**

| Aspect | Before | After |
|---|---|---|
| Palette | rainbow on ordered data | sequential Blues |
| Non-data ink elements | 16 | 3 |
| Annotations | 0 | 1 callout + takeaway title |
| Colour-blind safe | no | yes |
| Peer time-to-takeaway | 14 s | 4 s |

## Required Visuals and Training Assets

### Diagrams
1. **Palette decision chart** — *Purpose:* end colour guesswork. *Elements:* three branches (categorical/sequential/diverging) with data-type triggers and example swatches; a red "rainbow-on-ordered" anti-example. *Style:* swatch-based flow, Arabic + English.
2. **Decluttering ladder** — *Purpose:* an ordered checklist. *Elements:* six rungs (junk → gridlines → border → axes → legend → mute-to-grey) with a before/after thumbnail at top and bottom. *Style:* vertical ladder poster.
3. **Annotation anatomy** — *Purpose:* teach callout craft. *Elements:* one chart labelled with takeaway title, callout+leader, reference band, highlight+mute, value labels. *Style:* annotated exemplar.
4. **RTL/Arabic layout guide** — *Purpose:* localisation reference. *Elements:* mirrored time axis, numeral options, reshaped-vs-broken Arabic glyph comparison. *Style:* side-by-side LTR/RTL panels.

### Images (screenshots)
1. **`m3_diverging_cost.png`**: *why:* target-centred diverging done right; *content:* cost bars coloured around the 18 SAR target.
2. **`cluttered_m3.png` (the "before")**: *why:* the redesign target; *content:* rainbow 3D bars, junk, red/green.
3. **`m3_after_annotated.png`**: *why:* the exemplar "after"; *content:* muted context, one accent line, one callout.
4. **Colour-blind simulator output**: *why:* proves accessibility; *content:* the chart under deuteranopia simulation, before and after the fix.

### Simulations
1. **Colour-blindness simulator (`cvd_sim.py`)** — *Setup:* wraps any saved chart and renders deuteranopia/protanopia versions. *Expected behaviour:* red/green-only charts become unreadable; redundant-cue charts survive. *Learning objective:* accessibility is testable, not a judgement call.
2. **Data-ink eraser** — *Setup:* a notebook that progressively strips ink elements from a chart and recomputes the data-ink ratio. *Expected behaviour:* clarity rises as ratio rises, up to a point; over-stripping removes data. *Learning objective:* declutter to the data, not past it.

### Interactive Activities
- **Declutter relay (15 min):** teams take turns removing one element from a cluttered chart on the projector; the round ends when removing anything else would delete data.
- **Palette-match card game (10 min):** data-type cards matched to palette-swatch cards; mismatches (rainbow-on-sequential) are the teaching moments.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | (golden thread) | CSV | ~28,000 rows | Cost/adoption series for colour and annotation labs |
| `cluttered_m3.png` + source | Course team (deliberately bad) | PNG + CSV | 1 chart | Before/after redesign target |
| `brand_palette.json` | Course team (mock national-program brand) | JSON | 1 file | Brand-alignment exercise |
| Arabic-capable font bundle | Course team | TTF | few files | Correct Arabic glyph rendering |

### Demo Requirements
- **Instructor demo:** live before/after redesign of `cluttered_m3.png` in under 8 minutes, ending with the Arabic RTL version — rehearse the Arabic-rendering step so it does not stall.
- **Student demo:** two pairs present their redesign with the colour-blind simulation running live.
- **Expected outputs:** a decluttered, accessible, annotated chart in English and Arabic, plus a before/after data-ink count.

---

# Module 4 — Interactive Dashboards and BI Tools

## Module Overview

**Purpose.** Modules 1–3 produced honest, well-crafted *static* charts. This module turns a set of charts into a **system** — an interactive dashboard that lets a user explore the Tayseer program's performance without an analyst in the room. The craft shifts from "compose one view" to "compose a layout, choose interaction patterns, and design for self-service." A dashboard is not a slide with more charts on it; it is a small piece of software with a job, an audience, and a failure mode (the "wall of gauges" that answers no question). This module teaches participants to build one that answers questions, in Plotly for programmatic control and in a BI tool (Power BI / Tableau) for the self-service reality of most Saudi organisations.

**Business relevance.** Executives and operations directorates increasingly expect a live dashboard, not a monthly PDF. A good Tayseer dashboard lets the operations directorate answer "which region needs an intervention *this week*?" themselves, at 8am, without waiting for the analytics team — that is the entire value proposition of business intelligence. A bad one becomes shelfware in a fortnight because it shows twenty KPIs and answers none. In a Vision 2030 context where every ministry is standing up performance dashboards, the difference between a dashboard that drives weekly decisions and one that is opened once is almost entirely design, not data.

**Industry use cases.**
- A national program office wants a single screen the Deputy Minister opens each morning: one headline KPI, the trend, and the three regions needing attention — nothing else above the fold.
- An operations directorate needs to filter the same view by service category and channel and drill from national → region → service, self-service, with no code.
- A public-sector analytics team must publish an embedded, mobile-legible dashboard to a leadership portal with row-level security so each region director sees their own region by default.

**Expected competencies.** After this module a participant can design a dashboard layout around a primary question and an inverted-pyramid information hierarchy, choose the right interaction pattern (filter, cross-filter, drill-down, toggle) for a task, build a multi-view interactive dashboard in Plotly (Dash or Plotly figures with widgets), reproduce the core of it in a BI tool with a measures/calculated-field layer, and run a usability check that proves a non-analyst can answer the target question unaided.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Design a dashboard layout around a primary question and information hierarchy | LO3 |
| 4.2 | Select the correct interaction pattern (filter, cross-filter, drill-down, toggle) for a task | LO3 |
| 4.3 | Build a multi-view interactive dashboard in Plotly with linked views | LO3, LO2 |
| 4.4 | Reproduce a dashboard in a BI tool using a measures / calculated-field layer | LO3 |
| 4.5 | Apply self-service and accessibility principles (RLS, mobile, performance) | LO3 |
| 4.6 | Usability-test a dashboard against a target question and iterate | LO3, LO5 |

## Technical Content

### 1. What a dashboard is for (and the "wall of gauges" failure)

A dashboard has exactly one job: let its audience answer a *recurring* question fast enough to act. Before any chart is placed, name three things: **who** opens it, **what decision** it feeds, and **how often**. The Tayseer executive dashboard answers "is the program on track, and where is it not?" for a Deputy Minister, weekly. That single sentence dictates everything — one headline number (national digital adoption vs the 65% target), one trend, one "where is it not" ranking, and a filter set. Everything that does not serve that question is clutter with a refresh button.

The classic failure is the **wall of gauges**: twenty tiles because twenty metrics exist, each a speedometer or a donut, none prioritised. It fails for the Module 1 reason — no pre-attentive hierarchy, so the eye has no entry point — compounded by interaction the user never learns. Teach the inverse: a dashboard is an *argument with controls*, not a data dump with chrome.

### 2. Layout and information hierarchy: the inverted pyramid

Dashboards are read in a Z or F pattern (top-left first for LTR; top-right for Arabic/RTL — the same mirroring discipline from Module 3 applies to whole layouts, not just axes). Structure the layout as an **inverted pyramid**:

1. **Headline band (top):** one to four big-number KPIs with a target/delta and a tiny sparkline — the "am I on track?" answer in one glance.
2. **Primary view (centre):** the single most important chart — for Tayseer, the national adoption trend against the 65% target line.
3. **Breakdown band (below):** the "where?" — a sorted regional bar or dot plot (Module 2), the operative comparison.
4. **Detail / drill (bottom or on demand):** service-category and channel splits, revealed on interaction, not shown by default.

The rule: **the top of the dashboard answers the question; the bottom explains it.** A user who reads only the top band should already know whether to worry.

### 3. The four interaction patterns

Interaction is chosen by *task*, exactly like encoding (Module 1). There are four workhorse patterns; name each and its right use:

| Pattern | User task | Tayseer example | Watch-out |
|---|---|---|---|
| **Filter / slicer** | "Show me only this subset" | Filter to one service category | Filters that silently exclude and hide the fact |
| **Cross-filter (linked views)** | "Click here, update everything" | Click a region bar → trend + details re-scope | Cross-filter loops; unclear what is selected |
| **Drill-down / hierarchy** | "Go from summary to detail" | National → region → service | Drilling with no breadcrumb / no way back |
| **Toggle / parameter** | "Switch the measure or view" | Adoption ↔ cost ↔ CSAT on the same chart | Toggles that change meaning without relabelling |

The design discipline: **make the current state legible.** Every active filter must be visible ("Service: Social support · Channel: App"), every drill level must show a breadcrumb, and every cross-filter selection must be obviously selected. The commonest self-service bug is not a broken chart — it is a user misreading a filtered view as the whole.

### 4. Plotly vs Power BI / Tableau: choosing the tool

Both live in this course because both live in the workplace.

- **Plotly (with Dash or ipywidgets):** programmatic, version-controlled, reproducible, embeddable in Python apps; the analyst's tool when the dashboard is part of a data product or needs custom logic. Cost: you write and host code.
- **Power BI:** dominant in Microsoft-centric Saudi government and enterprise environments; strong data modelling (star schema + DAX measures), row-level security, and a self-service authoring experience for non-coders. Cost: licensing, Windows-centric authoring.
- **Tableau:** best-in-class exploratory authoring and visual polish; Tableau Public is a cross-platform, licence-free fallback for teaching. Cost: licensing for the server/governed features.

The teaching stance: **the design principles are identical across tools; only the mechanics differ.** A star schema and a measure in Power BI is the same idea as a tidy dataframe and an aggregation function in Plotly. Participants build the Tayseer dashboard once in Plotly (to own the logic) and reproduce its core in a BI tool (to meet the organisation where it is).

### 5. Data modelling for dashboards: the semantic layer

Interactive dashboards break when the data model is wrong, not when the chart is wrong. Teach the minimum modelling discipline:

- **Tidy / star shape:** a fact table (`tayseer_services` at month × region × category × channel grain) plus small dimension tables (region → admin-area, category → sector). This is what makes slicers and drill-downs cheap.
- **Measures, not baked numbers:** define `Digital Adoption %`, `Cost per Txn`, and `Δ vs target` as *measures* (DAX in Power BI, calculated fields in Tableau, aggregation functions in Plotly) computed at query time, so they respond correctly to every filter. A hard-coded national average that does not re-compute when the user filters to one region is the single most common BI defect.
- **Consistent grain and additivity:** know which measures are additive (transactions) and which are not (percentages, ratios — must be re-aggregated from components, never averaged-of-averages). `digital_adoption_pct` averaged across regions ≠ national adoption; recompute from `unique_users`.

### 6. Performance, self-service, and common mistakes

Production considerations that decide whether a dashboard is used:

- **Performance:** pre-aggregate where possible; a dashboard that takes eight seconds per click is abandoned. Cache the monthly rollups; do not scan 28,000 rows per interaction.
- **Row-level security (RLS):** each region director should see their region by default; RLS in Power BI / user filters in Tableau. A national dashboard without RLS often cannot be shared at all in government.
- **Mobile and accessibility:** executives open dashboards on phones; design a mobile layout (stacked, headline-first) and keep the Module 3 accessibility rules (colour-blind-safe, redundant cues, RTL).
- **Common mistakes:** (1) wall of gauges, no hierarchy; (2) averages-of-averages on percentages; (3) invisible active filters; (4) drill with no breadcrumb; (5) 3D/donut tiles imported from habit (Modules 1–2 still apply); (6) no default state that answers the question before any click.

The dashboard must **answer its question in its default, unfiltered state** — interaction refines the answer, it is not required to get one.

## Code Examples

### An interactive Tayseer dashboard in Plotly (linked KPI + trend + regional bar)

```python
# notebooks/m4_dashboard.ipynb  — programmatic dashboard with linked views
"""Module 4 — Tayseer executive dashboard in Plotly.
Design: headline KPI band -> national trend -> regional breakdown (the inverted pyramid).
Every measure is computed at query time so filters stay honest."""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])
TARGET_ADOPT, TARGET_COST = 65.0, 18.0

def national_adoption(frame: pd.DataFrame) -> pd.Series:
    """Percentages are NON-additive: recompute from users, never average regions."""
    g = frame.groupby("month").apply(
        lambda x: 100 * (x["digital_adoption_pct"] / 100 * x["unique_users"]).sum()
                  / x["unique_users"].sum())
    return g

nat = national_adoption(df)
latest_val = nat.iloc[-1]
delta = latest_val - TARGET_ADOPT

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "indicator"}, {"type": "xy"}],
           [{"type": "xy", "colspan": 2}, None]],
    row_heights=[0.45, 0.55], vertical_spacing=0.12,
    subplot_titles=("", "National digital adoption vs 65% target",
                    "Regions below target — where to intervene"))

# (1) Headline KPI: the "am I on track?" glance.
fig.add_trace(go.Indicator(
    mode="number+delta", value=round(latest_val, 1),
    number={"suffix": "%"}, delta={"reference": TARGET_ADOPT, "position": "bottom"},
    title={"text": "National adoption (latest)"}), row=1, col=1)

# (2) Primary view: trend + target reference line.
fig.add_trace(go.Scatter(x=nat.index, y=nat.values, mode="lines",
                         line=dict(color="#0072B2", width=3), name="National"),
              row=1, col=2)
fig.add_hline(y=TARGET_ADOPT, line_dash="dash", line_color="#D55E00", row=1, col=2)

# (3) Breakdown: sorted regional bar, laggards highlighted (Module 1 pop).
reg = (df[df.month == df.month.max()]
       .groupby("region").apply(lambda x: 100*(x.digital_adoption_pct/100*x.unique_users).sum()
                                / x.unique_users.sum())
       .sort_values().reset_index(name="adoption"))
colors = ["#D55E00" if v < TARGET_ADOPT else "#B8C4D9" for v in reg["adoption"]]
fig.add_trace(go.Bar(x=reg["adoption"], y=reg["region"], orientation="h",
                     marker_color=colors, name="Region"), row=2, col=1)
fig.add_vline(x=TARGET_ADOPT, line_dash="dash", line_color="#D55E00", row=2, col=1)

fig.update_layout(height=720, template="plotly_white", showlegend=False,
                  title_text="Tayseer — Digital Adoption Executive Dashboard")
fig.write_html("out/m4_dashboard.html")   # shareable, self-contained
```

### Cross-filtering and a measure toggle with Dash

```python
# app/dashboard.py  — Dash app: click a region to cross-filter; toggle the measure.
"""Self-service Tayseer dashboard. Active filter is ALWAYS shown (state legibility).
Run: python app/dashboard.py  ->  http://127.0.0.1:8050"""
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])
MEASURES = {"digital_adoption_pct": "Digital adoption %",
            "cost_per_txn_sar": "Cost per txn (SAR)",
            "csat": "CSAT (1-5)"}

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H3("Tayseer operations dashboard"),
    dcc.Dropdown(id="measure", options=[{"label": v, "value": k} for k, v in MEASURES.items()],
                 value="digital_adoption_pct", clearable=False),        # toggle pattern
    html.Div(id="filter-state", style={"fontWeight": "bold", "margin": "8px 0"}),
    dcc.Graph(id="region-bar"),      # click a bar -> cross-filter the trend
    dcc.Graph(id="trend"),
])

@app.callback(Output("region-bar", "figure"), Output("filter-state", "children"),
              Input("measure", "value"))
def bar(measure):
    latest = df[df.month == df.month.max()].groupby("region", as_index=False)[measure].mean()
    fig = px.bar(latest.sort_values(measure), x=measure, y="region", orientation="h",
                 template="plotly_white")
    return fig, f"Measure: {MEASURES[measure]} · Filter: (click a region to scope the trend)"

@app.callback(Output("trend", "figure"),
              Input("region-bar", "clickData"), Input("measure", "value"))
def trend(click, measure):
    frame = df if not click else df[df.region == click["points"][0]["y"]]   # cross-filter
    scope = "National" if not click else click["points"][0]["y"]
    monthly = frame.groupby("month", as_index=False)[measure].mean()
    fig = px.line(monthly, x="month", y=measure, template="plotly_white",
                  title=f"{MEASURES[measure]} — {scope}")   # state made legible in title
    if measure == "digital_adoption_pct":
        fig.add_hline(y=65, line_dash="dash", line_color="#D55E00")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
```

### The same dashboard's measures in a BI tool (Power BI DAX + Tableau)

```python
# bi/tayseer_measures.md  — the semantic layer, tool-agnostic then tool-specific.
# Grain of the fact table: month x region x service_category x channel.

# ---- Power BI (DAX) ----
# Non-additive percentage: recompute from components, never AVERAGE the column.
# Digital Adoption % :=
#   DIVIDE(
#       SUMX(tayseer, tayseer[digital_adoption_pct] / 100 * tayseer[unique_users]),
#       SUM(tayseer[unique_users])) * 100
#
# Delta vs Target :=  [Digital Adoption %] - 65
#
# Regions Below Target :=
#   CALCULATE(DISTINCTCOUNT(tayseer[region]),
#             FILTER(VALUES(tayseer[region]), [Digital Adoption %] < 65))
#
# Row-level security role "RegionDirector":
#   [region] = LOOKUPVALUE(UserRegion[region], UserRegion[email], USERPRINCIPALNAME())

# ---- Tableau (calculated fields) ----
# Digital Adoption %:
#   SUM([digital_adoption_pct]/100 * [unique_users]) / SUM([unique_users]) * 100
# Below Target flag:
#   IF [Digital Adoption %] < 65 THEN "Below" ELSE "On/above" END
# User filter for RLS: USERNAME() mapped via a region-director lookup.
```

## Hands-on Lab 4 — Build the Interactive Tayseer Dashboard

| | |
|---|---|
| **Objective** | Compose a multi-view interactive Tayseer dashboard (KPI headline, national trend, regional breakdown) in Plotly/Dash, add cross-filtering, drill-down and a measure toggle, then reproduce its core in a BI tool and usability-test it |
| **Duration** | 100 minutes (two hours: Lab 4a build, Lab 4b interactivity) |
| **Setup** | `pip install pandas plotly dash`; Power BI Desktop (Windows) *or* Tableau Public; `data/tayseer_services.csv`; `git checkout lab4_start` (or open `lab4_start.ipynb` / `lab4_start.pbix`) |

**Instructions & tasks**

*Lab 4a — build (50 min):*
1. *(5 min)* Write the one-sentence dashboard brief: audience, decision, cadence. Confirm the primary question is "is the program on track, and where is it not?"
2. *(15 min)* Build the inverted-pyramid layout in Plotly `make_subplots`: KPI indicator (adoption vs 65%), national trend with target line, sorted regional bar with laggards highlighted.
3. *(10 min)* Implement `national_adoption()` correctly — recompute the percentage from `unique_users`; prove it differs from a naive `mean()` of the column in a markdown cell.
4. *(10 min)* Add a target reference line to trend and bar; give the dashboard a takeaway title.
5. *(10 min)* Export to a self-contained `out/m4_dashboard.html`; open it and confirm the default state answers the question with zero clicks.

*Lab 4b — interactivity (50 min):*
6. *(15 min)* Convert to a Dash app: add a measure toggle (adoption/cost/CSAT) and click-to-cross-filter from the regional bar to the trend.
7. *(10 min)* Make state legible: show the active measure and selected region as text; add a "reset" affordance.
8. *(10 min)* Add a drill path (national → region → service category) with a breadcrumb.
9. *(10 min)* Reproduce the KPI + regional bar in Power BI/Tableau using the provided measures; add row-level security so a region role sees only its region.
10. *(5 min)* Usability test: hand your dashboard to a pair who has not seen it; time how long to answer "which two regions need intervention?" Save as `lab4_solution`.

**Expected output**
```
Brief: Deputy Minister, weekly "on track & where not" decision.
Default state answers the question with 0 clicks (KPI 63.8% vs 65% target, 3 regions below).
national_adoption() = 63.8%  vs  naive mean-of-column = 61.2%  (averages-of-averages bug demonstrated).
Cross-filter: click "Najran" -> trend re-scopes, title reads "Digital adoption % — Najran".
Toggle: adoption -> cost -> CSAT re-renders; target line only on adoption.
BI reproduction: Power BI KPI + bar with RLS role 'RegionDirector' (region director sees 1 region).
Usability: naive peer answered "which two regions?" in 9 s.
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| National number changes when filtering to one region "wrongly" | Averaging the percentage column | Recompute from `unique_users` (non-additive measure) |
| Cross-filter selection not obvious | State not surfaced | Echo selection in the chart title + highlight the selected bar |
| Dash callback error "nonexistent object" | Output id typo / duplicate | One `Output` per component-property; check ids match layout |
| BI KPI blank after adding RLS | Role filters everything out | Map the test user to a real region in the lookup table |
| Dashboard slow on every click | Scanning 28k rows per interaction | Pre-aggregate monthly rollups; cache |
| Donut/gauge crept back in | Habit over principle | Modules 1–2 still apply inside a dashboard; replace with bar/number |

**Instructor notes.** The averages-of-averages bug (task 3) is the highest-value moment — most participants have shipped it in production without knowing. Make them print both numbers. The second "aha" is the usability test: watching a naive peer struggle (or breeze) through their dashboard teaches more than any critique. Fast finishers: add a mobile-stacked layout or a `/metrics`-style export. Protect Lab 4b's cross-filter task; it is the most overrun-prone in the course.

## Mini Exercises

**Quiz (5 questions)**
1. A dashboard shows 20 gauges. Name the core failure and the fix. → no pre-attentive hierarchy / no primary question; restructure as an inverted pyramid around one question.
2. Which interaction pattern for "click a region, update every view"? → cross-filter (linked views).
3. Why can you not `AVERAGE` `digital_adoption_pct` across regions? → it is non-additive; recompute from `unique_users` components.
4. What must a dashboard answer with zero clicks? → its primary question, in the default state; interaction only refines.
5. What does RLS give a national dashboard? → each viewer sees only their permitted rows (e.g. region director sees their region), enabling safe sharing.

**Chart-critique exercise.** Project `critique_m4.png` (a wall-of-gauges Tayseer dashboard: 18 donuts, no hierarchy, invisible filter). Pairs identify the missing primary question and re-lay-out the top band on paper.

**Interaction-pattern match.** Give five user tasks; participants label each with filter / cross-filter / drill / toggle and justify.

**Discussion questions.**
- Your directorate wants "every metric on one screen." How do you honour the request without a wall of gauges? (headline band + progressive disclosure via drill; the whole is one gestalt, detail on demand)
- When is Plotly/Dash the right choice over Power BI, and vice versa? (data product / custom logic / version control → code; self-service authoring, RLS, Microsoft estate → BI tool)

## Case Study — From Monthly PDF to a Weekly Self-Service Dashboard

**Scenario.** The Tayseer operations directorate currently receives a 30-page monthly PDF built by two analysts over three days. Decisions lag the data by up to five weeks. Leadership asks for a live dashboard the directorate can open weekly and filter themselves. The first prototype from a vendor is a wall of 18 gauges that no one can use to answer "where do we send an improvement team this week?"

**Business context.** The directorate dispatches improvement teams to regions; a five-week data lag means teams are sent based on last month's problems, sometimes already resolved. A weekly self-service view directly shortens the decision loop and re-allocates field effort — real money and real service outcomes.

**Technical challenge.** Replace a static PDF and a failed gauge-wall with a dashboard that (a) answers "which regions need intervention this week?" in its default state, (b) lets a non-analyst filter by service and channel, drill to detail, and (c) is fast and secure enough to share directorate-wide.

**Constraints.** Non-analyst users; weekly cadence; must run in the ministry's Power BI estate with RLS; mobile-legible for field managers; bilingual (Arabic RTL); no per-click wait over ~2 seconds.

**Solution approach (facilitate, don't lecture).** (1) Write the one-sentence brief and kill the gauge wall. (2) Inverted-pyramid layout: adoption-vs-target KPI band, national trend, sorted "regions below target" bar as the operative view. (3) Slicers for service/channel with visible active-state; drill national→region→service. (4) Correct non-additive measures; pre-aggregated model for speed. (5) RLS so each region director defaults to their region. (6) Usability-test with a real field manager and iterate the top band.

**Discussion questions.**
1. Why does the "regions below target" sorted bar belong above the fold, but the 18-metric detail does not?
2. How do you prevent a filtered view being misread as the national picture?
3. What breaks first when this dashboard scales from 13 regions to 13 regions × 6 services × 3 channels, and how does the data model absorb it?
4. Where does moving from monthly PDF to weekly dashboard change *who* makes the intervention decision — and is that intended?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Default-state answers the primary question | Design | Yes (0 clicks) | Instructor review |
| Time for a naive user to answer the target question | Usability | < 15 s | Peer stopwatch |
| Non-additive measures computed correctly | Correctness | 100% | Compare vs naive mean in notebook |
| Active filter / drill state legibility | Self-service | Always visible | Heuristic check |
| Per-interaction latency | Performance | < 2 s | Timed clicks |
| Accessibility + RTL retained from M3 | Accessibility | Pass | Simulator + native check |

**Example benchmark table (filled during lab):**

| Aspect | Gauge-wall prototype | Redesigned dashboard |
|---|---|---|
| Primary question answered in default state | no | yes (KPI + laggard bar) |
| Interaction patterns used | none meaningful | cross-filter + drill + toggle |
| National % correctness | averages-of-averages (61.2%) | recomputed (63.8%) |
| Naive-user time to answer | > 60 s (gave up) | 9 s |
| Shareable with RLS | no | yes |

## Required Visuals and Training Assets

### Diagrams
1. **Dashboard inverted-pyramid layout** — *Purpose:* the module's spine. *Elements:* four stacked bands (KPI headline → primary view → breakdown → detail/drill) with an eye-path arrow and an Arabic RTL mirror. *Style:* annotated wireframe, English + Arabic. *Designer description:* "Four horizontal bands top-to-bottom, biggest number at top, a faint Z/F eye-path overlay, a small mirrored RTL variant beside it."
2. **Four interaction patterns matrix** — *Purpose:* pattern selection. *Elements:* filter, cross-filter, drill, toggle — each a mini before/after of the user task and the watch-out. *Style:* 2×2 grid.
3. **Semantic layer / star schema** — *Purpose:* teach the data model. *Elements:* central `tayseer_services` fact table linked to region, category, channel dimensions; a measure box (`Digital Adoption %`, `Δ vs target`). *Style:* star-schema diagram.
4. **Tool decision strip (Plotly vs Power BI vs Tableau)** — *Purpose:* choosing the tool. *Elements:* three columns with strengths, costs, and "use when". *Style:* comparison strip.

### Images (screenshots)
1. **`m4_dashboard.html` output**: *why:* Lab 4a reference; *content:* KPI + trend + laggard bar in the inverted pyramid.
2. **Dash cross-filter in action**: *why:* Lab 4b reference; *content:* region clicked, trend re-scoped, state shown in title.
3. **Power BI reproduction with RLS**: *why:* BI-tool exemplar; *content:* KPI + bar, RLS role dropdown, region-director view.
4. **Wall-of-gauges anti-example (`critique_m4.png`)**: *why:* critique target; *content:* 18 donuts, no hierarchy.

### Simulations
1. **Averages-of-averages demonstrator** — *Setup:* a notebook that shows the national percentage computed both correctly and naively as the user filters. *Expected behaviour:* the two numbers diverge under filtering; only the recomputed one is stable. *Learning objective:* non-additive measures must be recomputed, not averaged.
2. **Filter-state fog** — *Setup:* a dashboard where the active filter can be hidden or shown by a switch. *Expected behaviour:* with state hidden, testers misread a filtered view as national. *Learning objective:* state legibility is a correctness feature, not a nicety.

### Interactive Activities
- **Dashboard teardown (15 min):** teams critique a real public-sector dashboard against the inverted-pyramid and interaction-pattern checklists; each reports the missing primary question.
- **Usability relay (15 min):** pairs swap dashboards and race to answer each other's target question; the "time to answer" and any misreads are logged and discussed.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | (golden thread) | CSV | ~28,000 rows × 12 cols | Source for all dashboard views and measures |
| `tayseer_model.pbix` / `.twbx` starter | Course team | Power BI / Tableau | 1 file | BI-tool starter with fact + dimension model |
| `region_directors.csv` | Course team (mock) | CSV | 13 rows | Email→region lookup for the RLS exercise |

### Demo Requirements
- **Instructor demo:** live-build the inverted-pyramid Plotly dashboard and add one cross-filter in under 10 minutes; the moment a click re-scopes every view *is* the message. Then flip to Power BI to show the identical logic as a DAX measure.
- **Student demo:** two pairs present their dashboards and run a live usability test on a volunteer; the class notes any misread of filter state.
- **Expected outputs:** a self-contained interactive `m4_dashboard.html`, a running Dash app with cross-filter + toggle + drill, and a BI reproduction with RLS.

---

# Module 5 — Data Storytelling Structure and Flow

## Module Overview

**Purpose.** A dashboard lets someone *explore*; a story makes someone *decide*. Modules 1–4 built the visual craft and the interactive system; this module supplies the missing structure — the narrative that carries a specific audience from "here is a chart" to "therefore we should act." Exploration is analyst-driven and open-ended; a story is author-driven, linear, and pointed at one decision. The skill is not decoration bolted onto charts; it is the deliberate sequencing of evidence around a single Big Idea, so that by the last slide the recommendation feels inevitable. This is where the Tayseer dashboard becomes a seven-slide case for where the program should invest its next SAR 40 million.

**Business relevance.** In a Saudi executive context, analytical work is judged not by its rigour but by the decision it changes. A correct analysis with no narrative dies in a slide nobody follows; a well-structured story moves budget. The difference between a data scientist who is "the person who makes the charts" and one who is "in the room when decisions are made" is almost entirely narrative structure. Vision 2030 governance runs on steering committees and decision memos — venues that reward a clear Big Idea and punish a data dump — so storytelling is not a soft skill here, it is the mechanism by which analysis becomes policy.

**Industry use cases.**
- A program office must turn a quarter of dashboard data into a seven-minute case for reallocating budget to three lagging regions — one Big Idea, three supporting acts, one ask.
- An analytics team writes a one-page decision memo (BLUF-first) that a Deputy Minister reads in ninety seconds and can act on without the deck.
- A public-health team sequences a rising-wait-times story so the "so what" and the recommended intervention land before any methodology.

**Expected competencies.** After this module a participant can frame a narrative around a specific audience and decision, distil an analysis into a single Big Idea sentence, choose a narrative arc and sequence charts as annotated "scenes," write a BLUF/top-line, storyboard a seven-slide executive arc, and self-edit ruthlessly against the "does this slide advance the decision?" test.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Frame a data narrative around a specific audience and decision | LO4 |
| 5.2 | Distil an analysis into a single Big Idea sentence | LO4 |
| 5.3 | Select and apply a narrative arc to sequence evidence | LO4 |
| 5.4 | Convert charts into annotation-led narrative scenes | LO4, LO2 |
| 5.5 | Write a BLUF/top-line that states the recommendation first | LO4, LO6 |
| 5.6 | Storyboard a seven-slide executive arc and self-edit against the decision | LO4, LO5 |

## Technical Content

### 1. Exploration vs explanation: two different jobs

The foundational distinction: an **exploratory** artefact (the Module 4 dashboard) is built for the analyst to *find* the story and for a user to *interrogate* it — it is open, interactive, and non-linear. An **explanatory** artefact (this module's deliverable) is built for a decision-maker to *receive* a specific conclusion — it is closed, linear, and author-controlled. The commonest failure of technical people is presenting the exploratory artefact *as* the explanation: dumping the dashboard on the committee and narrating every filter. The move is to **do the exploration privately, then throw almost all of it away** and build a tight, linear case from the two or three findings that matter. If you show it, it must earn its place by advancing the decision.

### 2. Audience and decision framing: the pre-narrative questions

Before a single slide, answer four questions:

1. **Who is the audience, and what do they already believe?** A Deputy Minister who thinks the program is on track needs a different opening than one who thinks it is failing.
2. **What decision does this feed, and what are the options?** For Tayseer: where to direct the next SAR 40 million — three named options (lagging regions, channel infrastructure, or the highest-volume services).
3. **What is the one thing they must remember?** (The Big Idea — subsection 3.)
4. **What will make them say no, and what evidence pre-empts it?** Anticipate the objection ("aren't those regions just small?") and seat its rebuttal in the arc.

Framing is the highest-leverage step. A technically perfect deck aimed at the wrong belief or the wrong decision fails completely; time spent here saves ten slides later.

### 3. The Big Idea: one sentence, one decision

Borrowed from Nancy Duarte and Cole Nussbaumer Knaflic, the **Big Idea** is a single sentence that states (a) your unique point of view, (b) what is at stake, and (c) implies the action. Not "here is our Q3 adoption data" (topic) but *"Three regions are dragging national adoption below the 65% target, and directing the next SAR 40 million there — rather than to channel infrastructure — is the fastest way to close the gap by year-end"* (idea + stakes + action). Every slide in the deck must be defensible as "this earns its place because it builds toward that sentence." If a slide does not advance the Big Idea, it is cut, no matter how interesting the chart. The Big Idea is also the answer to "if they remember only one sentence, what is it?" — and it becomes the BLUF (subsection 5) and the presentation's opening line (Module 6).

### 4. Narrative arcs: structures that carry evidence

Stories have shape. Teach three arcs and when each fits:

| Arc | Shape | Best when | Tayseer application |
|---|---|---|---|
| **Situation–Complication–Resolution (SCR / "Minto")** | context → tension → answer | Recommending an action to a committee | "Program on track nationally (situation), but three regions stall it (complication), so invest there (resolution)" |
| **What is / What could be** (Duarte) | oscillate current reality ↔ better future, ending on the ask | Motivating change or investment | Contrast today's 63.8% and the year-end 65%+ if the gap is closed |
| **Chronological / journey** | beginning → middle → now | Explaining how a situation arose | How the March outage created the Najran plateau |

The default for an executive investment decision is **SCR**: it front-loads shared context, introduces one clear complication, and resolves to the ask — matching how committees actually decide. The arc is the skeleton; the charts (subsection 4) are the flesh hung on it.

### 5. Charts as scenes: annotation-led sequencing

In a story, a chart is not a reference exhibit — it is a **scene** making one point. This reuses Module 3's annotation discipline at the deck level:

- **One chart, one message, one takeaway title.** The title is the sentence the audience should think; the chart is the evidence.
- **Progressive reveal / build.** Introduce a complex chart in layers (show the trend, then reveal the target line, then highlight the laggards) so the audience thinks one thought at a time, rather than decoding a finished dense chart cold.
- **Highlight and mute per scene** (Modules 1, 3): the same regional bar can be a different scene each time by highlighting a different region, guiding attention to the current point.
- **Callouts carry the argument** (Module 3): "Najran plateaued after the March outage" annotated on the exact point, so the slide survives being forwarded without you.

The sequencing rule: **each scene sets up the next.** The trend scene ("nationally we're just below target") *creates the question* the breakdown scene answers ("because of these three regions"), which *creates* the recommendation scene. Sequence is argument.

### 6. BLUF, the seven-slide arc, and ruthless editing

- **BLUF — Bottom Line Up Front.** Executives may not reach slide seven; put the recommendation on slide one, then support it. This inverts the analyst's instinct (methodology → results → conclusion) into the decision-maker's need (conclusion → evidence → method-on-request). The BLUF *is* the Big Idea stated as a recommendation.
- **A seven-slide executive arc (the course template):** (1) BLUF / the ask; (2) situation — where the program stands; (3) complication — the three lagging regions; (4) evidence — why they lag (the outage, the channel gap); (5) options — the three uses of SAR 40 million, compared; (6) recommendation — the chosen option and expected effect; (7) the ask + next step. Appendix holds the dashboard and methodology for Q&A.
- **Ruthless editing.** The single test for every slide, sentence, and chart: *does this advance the decision?* If not, cut it to the appendix. Executives punish density; a seven-slide deck that respects their attention beats a thirty-slide deck that exhausts it. Data storytelling is as much subtraction as construction.

## Code Examples

### Turning a chart into a narrative scene (progressive build)

```python
# notebooks/m5_story_scenes.ipynb
"""Module 5 — build the SAME regional chart as a SEQUENCE of scenes.
Each scene = one message, one takeaway title, one highlight (Modules 1/3 at deck level)."""
import pandas as pd
import matplotlib.pyplot as plt
from src.viz.theme import apply_theme, ACCENT, GREY
apply_theme()

df = pd.read_csv("data/tayseer_services.csv", parse_dates=["month"])
TARGET = 65.0
reg = (df[df.month == df.month.max()]
       .groupby("region").apply(lambda x: 100*(x.digital_adoption_pct/100*x.unique_users).sum()
                                / x.unique_users.sum())
       .sort_values().reset_index(name="adoption"))
laggards = reg[reg.adoption < TARGET]["region"].tolist()

def scene(highlight, title, fname):
    """One scene: highlight the regions this point is about, grey the rest."""
    colors = [ACCENT if r in highlight else GREY for r in reg["region"]]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(reg["region"], reg["adoption"], color=colors)
    ax.axvline(TARGET, color="#333", ls="--", lw=1)
    ax.text(TARGET, len(reg) - 0.4, " target 65%", fontsize=9)
    ax.set_title(title, fontsize=13)      # the takeaway = the thought we want
    ax.set_xlabel("Digital adoption (%)")
    fig.savefig(f"out/{fname}", dpi=150)

# Scene 2 (situation): nothing highlighted — "here is where we stand."
scene([], "Most regions clear the 65% adoption target", "m5_scene_situation.png")
# Scene 3 (complication): highlight the laggards — "but three do not."
scene(laggards, "But three regions sit below target and hold the national number down",
      "m5_scene_complication.png")
# Scene 4 (evidence): highlight just Najran — "and one stalled for a known reason."
scene(["Najran"], "Najran's plateau traces to the March 2024 service outage",
      "m5_scene_evidence.png")
```

### A storyboard-as-code: the seven-slide arc as a spec

```python
# story/tayseer_storyboard.py
"""The seven-slide executive arc as a checkable spec.
Each scene declares its message, arc-role, the asset, and WHY it earns its place.
A slide with no decision_role is a candidate for the appendix."""
from dataclasses import dataclass

@dataclass
class Scene:
    n: int
    arc_role: str          # SCR role or 'BLUF'/'ask'
    message: str           # the ONE sentence the audience should think (= the title)
    asset: str             # the chart/scene file
    advances_decision: bool

BIG_IDEA = ("Three lagging regions hold national adoption below 65%; directing the next "
            "SAR 40M there, not to channel infrastructure, closes the gap by year-end.")

STORYBOARD = [
    Scene(1, "BLUF",         "Invest the next SAR 40M in three lagging regions to hit 65% by December", "m5_bluf.png", True),
    Scene(2, "situation",    "Most regions clear the 65% adoption target",                              "m5_scene_situation.png", True),
    Scene(3, "complication", "But three regions sit below target and drag the national number down",    "m5_scene_complication.png", True),
    Scene(4, "evidence",     "Najran's plateau traces to the March outage; Jazan/Al-Bahah to channel gaps", "m5_scene_evidence.png", True),
    Scene(5, "options",      "SAR 40M: regions vs channel infrastructure vs high-volume services",       "m5_options_compare.png", True),
    Scene(6, "resolution",   "Region-targeted spend closes the gap fastest for the lowest cost",         "m5_recommendation.png", True),
    Scene(7, "ask",          "Approve reallocation; first review in 90 days",                            "m5_ask.png", True),
]

def audit(storyboard):
    assert storyboard[0].arc_role == "BLUF", "Recommendation must lead (BLUF)."
    weak = [s.n for s in storyboard if not s.advances_decision]
    assert not weak, f"Slides not advancing the decision -> appendix: {weak}"
    assert len(storyboard) <= 7, "Executive arc is 7 scenes; the rest is appendix."
    print(f"Storyboard OK. Big Idea:\n  {BIG_IDEA}")

if __name__ == "__main__":
    audit(STORYBOARD)
```

### A BLUF / decision-memo generator

```python
# story/bluf.py  — the one-page top-line an executive reads in 90 seconds.
"""BLUF first, evidence second, methodology on request. This is the Big Idea as a memo."""
def render_bluf(recommendation, because, stakes, ask, evidence: list[str]) -> str:
    lines = [f"# Recommendation\n**{recommendation}**\n",
             f"**Why now:** {stakes}\n",
             f"**Rationale:** {because}\n",
             "**Evidence (one line each):**"]
    lines += [f"- {e}" for e in evidence]
    lines += [f"\n**The ask:** {ask}",
              "\n_Full analysis and dashboard in appendix; methodology available on request._"]
    return "\n".join(lines)

print(render_bluf(
    recommendation="Direct the next SAR 40M to Najran, Jazan, and Al-Bahah adoption programs.",
    because="These three regions account for the entire national shortfall against the 65% target.",
    stakes="At current pace the program misses its year-end adoption commitment.",
    ask="Approve the reallocation; first checkpoint in 90 days.",
    evidence=["National adoption 63.8% vs 65% target — gap is concentrated, not diffuse.",
              "Najran plateaued after the March 2024 outage (a fixable, known cause).",
              "Region-targeted spend closes the gap ~2x faster than channel infrastructure per riyal."]))
```

## Hands-on Lab 5 — Storyboard the Tayseer Narrative

| | |
|---|---|
| **Objective** | Turn the Module 4 dashboard findings into a storyboarded seven-slide executive arc built on one Big Idea, with each chart rendered as an annotation-led scene and a BLUF memo |
| **Duration** | 50 minutes |
| **Setup** | `data/tayseer_services.csv`, the Module 4 dashboard/findings, `src/viz/theme.py`, `story/` starter; `git checkout lab5_start` |

**Instructions & tasks**

1. *(5 min)* Answer the four framing questions in `framing.md`: audience (Deputy Minister), decision (where to put SAR 40M), Big Idea sentence, the anticipated objection.
2. *(5 min)* Write your Big Idea as one sentence containing POV + stakes + implied action. Peer-check it against a neighbour: can they restate the recommendation from it alone?
3. *(10 min)* Choose an arc (default SCR) and fill the seven-scene storyboard in `tayseer_storyboard.py`; run `audit()` until it passes (BLUF leads, ≤ 7 scenes, every scene advances the decision).
4. *(15 min)* Render at least three scenes with the `scene()` builder: situation, complication, evidence — each with a takeaway title and a single highlight; build the progressive-reveal version of the complication scene.
5. *(5 min)* Write the BLUF memo with `bluf.py`; confirm a peer can act on it in 90 seconds without the deck.
6. *(5 min)* Self-edit: move every non-advancing slide to an appendix list; justify each cut in one line.
7. *(5 min)* Save the storyboard + rendered scenes + BLUF as `lab5_solution`.

**Expected output**
```
Framing: Deputy Minister · decide SAR 40M allocation · objection "aren't those regions just small?"
Big Idea (peer restated correctly): invest SAR 40M in 3 lagging regions -> hit 65% by December.
Storyboard audit: PASS (BLUF leads, 7 scenes, 0 non-advancing).
Scenes rendered: situation, complication (progressive build), evidence (Najran callout).
BLUF memo: peer acted in ~70 s without the deck.
Cut to appendix: methodology slide, per-service breakdown, data-quality note (justified).
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Big Idea reads as a topic, not an idea | No POV / no action | Rewrite to include stakes + implied action; the test is "can a peer restate the recommendation?" |
| Deck is 15 slides | Presenting exploration as explanation | Cut to 7; everything else → appendix for Q&A |
| Charts feel like exhibits | Topic titles, no highlight | Give each a takeaway title and one highlight; make it a scene |
| Audience "would ask why" mid-deck | Sequence doesn't set up next scene | Reorder so each scene raises the question the next answers |
| Objection lands unanswered | Rebuttal not seated in the arc | Add the "aren't they just small?" rebuttal (per-capita, not absolute) as evidence |

**Instructor notes.** The peer-restatement test on the Big Idea (task 2) is the make-or-break moment — if a neighbour cannot restate the recommendation from the sentence alone, the sentence is a topic and the whole deck will wander. Do not let pairs proceed until their Big Idea passes. The second high-value moment is the appendix cut (task 6); technical participants resist cutting "good analysis" and must feel that subtraction *is* the storytelling. Fast finishers: build the "What is / What could be" version and compare which arc lands harder.

## Mini Exercises

**Quiz (5 questions)**
1. Exploratory vs explanatory — which is linear and author-controlled? → explanatory; exploration is open and user-driven.
2. Name the three parts of a Big Idea. → point of view, what's at stake, implied action.
3. Which arc best fits recommending an investment to a committee? → Situation–Complication–Resolution (SCR).
4. What does BLUF invert, and why? → methodology-first → conclusion-first; executives may not reach the last slide.
5. The single test for keeping a slide? → does it advance the decision? If not, appendix.

**Big-Idea clinic.** Each participant writes their Tayseer Big Idea; three are read aloud and the room votes "idea or topic," rewriting the topics live.

**Arc-fit exercise.** Give three scenarios; participants pick SCR / What-is-What-could-be / chronological and justify.

**Discussion questions.**
- Your analysis is nuanced with five findings. How do you honour the nuance while committing to one Big Idea? (lead with the idea; the nuance lives in evidence scenes and the appendix, not the headline)
- When is it dishonest to lead with the recommendation (BLUF)? (never for the ordering; only if the evidence doesn't support it — BLUF demands the conclusion be earned)

## Case Study — Turning a Quarter of Dashboard Data into a SAR 40M Case

**Scenario.** The Tayseer analytics team has a rich Module 4 dashboard and a Steering Committee slot next week to recommend how to spend the next SAR 40 million. The first draft deck is the dashboard exported to twenty-two slides, one per view, ending with "questions?" The committee chair has fifteen minutes and a habit of deciding in the first three.

**Business context.** SAR 40 million will go to one of three uses; the committee's decision is effectively made by whoever frames it most clearly. The analytics team's credibility — and its seat in future decisions — rides on whether this lands.

**Technical challenge.** Compress a quarter of exploratory analysis into a seven-slide, BLUF-first explanatory arc that makes one recommendation feel inevitable, survives a three-minute attention span, and pre-empts the "those regions are just small" objection.

**Constraints.** Fifteen-minute slot (assume three); bilingual deck; static slides (no live dashboard in the room — that is the appendix); the committee chair is numerate and impatient; the recommendation must be defensible to an auditor.

**Solution approach (facilitate, don't lecture).** (1) Framing: audience belief, the three options, the Big Idea. (2) SCR arc, BLUF on slide one. (3) Each of the seven slides a single annotated scene with a takeaway title. (4) Seat the "just small" rebuttal as a per-capita evidence scene. (5) Options slide compares the three uses on gap-closed-per-riyal. (6) Appendix holds the dashboard and methodology for Q&A. (7) Dry-run against the three-minute test.

**Discussion questions.**
1. Why does exporting the dashboard to slides fail, even though every chart is individually good?
2. Where in the arc does the "those regions are just small" objection belong, and what evidence retires it?
3. How does BLUF change the committee's experience of the same fifteen minutes?
4. What goes in the appendix, and how do you use it in Q&A without derailing the arc?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Big Idea passes peer-restatement | Framing | Peer restates recommendation | Peer test |
| Deck length | Structure | ≤ 7 scenes (rest in appendix) | Slide count |
| Slides advancing the decision | Focus | 100% | Storyboard audit |
| Scenes with takeaway titles + one highlight | Craft | 100% | Instructor review |
| BLUF actionable without the deck | Communication | Peer acts in < 90 s | Peer test |
| Anticipated objection seated in arc | Persuasion | Present | Review |

**Example benchmark table (filled during lab):**

| Aspect | First draft | Storyboarded arc |
|---|---|---|
| Slides | 22 (dashboard export) | 7 + appendix |
| Recommendation position | slide 22 | slide 1 (BLUF) |
| Big Idea | absent (topic deck) | one sentence, peer-restated |
| Objection handling | none | per-capita rebuttal seated in evidence |
| Peer time to grasp the ask | did not finish | 70 s from BLUF alone |

## Required Visuals and Training Assets

### Diagrams
1. **Exploration → explanation funnel** — *Purpose:* the module's core distinction. *Elements:* a wide exploratory dashboard narrowing to a tight linear seven-scene arc, with "throw most of it away" labelled at the neck. *Style:* funnel, English + Arabic. *Designer description:* "Left: a busy dashboard; a funnel narrows rightward to seven ordered slide cards; discarded charts fall away at the funnel's neck."
2. **Big Idea anatomy** — *Purpose:* teach the one-sentence test. *Elements:* one sentence dissected into POV / stakes / action, with a topic counter-example struck through. *Style:* annotated sentence.
3. **Three narrative arcs** — *Purpose:* arc selection. *Elements:* SCR, What-is/What-could-be, chronological — each a shape sketch with its "best when." *Style:* three side-by-side shape diagrams.
4. **The seven-slide executive arc** — *Purpose:* the deck template. *Elements:* seven numbered slide thumbnails (BLUF → situation → complication → evidence → options → recommendation → ask) with the appendix beneath. *Style:* storyboard strip.

### Images (screenshots)
1. **The three rendered scenes (`m5_scene_*.png`)**: *why:* Lab 5 reference; *content:* situation/complication/evidence versions of the same regional bar.
2. **Progressive-reveal build**: *why:* one-thought-at-a-time; *content:* the complication chart in three reveal layers.
3. **BLUF memo output**: *why:* the 90-second top-line exemplar; *content:* the rendered one-page recommendation.
4. **Before/after deck**: *why:* the whole module in one image; *content:* 22-slide export vs 7-slide arc thumbnails.

### Simulations
1. **Big Idea vs topic sorter** — *Setup:* a set of candidate sentences; participants classify idea vs topic and the tool reveals the POV/stakes/action test. *Expected behaviour:* topics fail the "restate the action" test. *Learning objective:* an idea implies a decision; a topic does not.
2. **Storyboard auditor** — *Setup:* `audit()` runs against a participant's storyboard. *Expected behaviour:* fails if the recommendation isn't first, or if any slide doesn't advance the decision. *Learning objective:* structure is checkable, not vibes.

### Interactive Activities
- **Big Idea slam (10 min):** participants read their one-sentence Big Idea; the room votes idea/topic and rewrites the weakest live.
- **Cut-to-seven (15 min):** pairs are handed a 20-slide deck and must cut it to a seven-scene arc plus appendix, defending each cut in one line.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | (golden thread) | CSV | ~28,000 rows | Source for the narrative scenes |
| `dashboard_findings.md` | Course team (from M4) | Markdown | 1 page | The raw findings to be storyfied |
| `story/` starter (`storyboard.py`, `bluf.py`) | Course team | Python | few files | Storyboard + BLUF scaffolding |

### Demo Requirements
- **Instructor demo:** live-convert three dashboard views into three narrative scenes (retitle, highlight, sequence) in under 8 minutes; then read a topic-deck title and its Big-Idea rewrite back to back — the difference *is* the lesson.
- **Student demo:** two pairs present their seven-slide storyboard as thumbnails and defend one appendix cut each.
- **Expected outputs:** a passing storyboard, at least three rendered scenes, and a BLUF memo that a peer can act on in under 90 seconds.

---

# Module 6 — Executive Communication and Presentation Lab

## Module Overview

**Purpose.** The storyboard from Module 5 is a plan; this module is about delivering it in the room. It is the course's final mile: the moment a data scientist stands in front of a Steering Committee, has three minutes of attention, and either changes a decision or does not. The craft here is different from everything before — it is delivery, not design: opening with the ask, controlling a slide's reveal while speaking, fielding a hostile question without losing the thread, and handling the specific dynamics of a senior Saudi government audience. This is a *lab*, not a lecture: participants rehearse, are recorded, receive critique, and iterate, because executive delivery improves only through reps and feedback, never through slides about delivery.

**Business relevance.** The entire value chain of this course — perception, chart choice, colour, dashboards, narrative — converges on one event: the executive briefing. A brilliant analysis delivered nervously, buried in setup, or derailed by the first tough question, produces the same outcome as no analysis. Conversely, a data scientist who can open with the recommendation, hold a committee's attention, and answer a Deputy Minister's challenge calmly becomes the trusted advisor who is invited back. In Vision 2030 delivery units, this skill is the difference between analytics that informs decisions and analytics that decorates them.

**Industry use cases.**
- A data scientist presents the SAR 40 million recommendation to a Deputy Minister-chaired committee, opens with the ask, and defends it under challenge in a fifteen-minute slot.
- An analytics lead delivers a two-minute stand-up top-line to a program director between meetings — recommendation, one reason, one number.
- A team fields a "your numbers are wrong" objection in a review by separating the challenged number from the recommendation and routing detail to the appendix.

**Expected competencies.** After this module a participant can open a briefing with the BLUF, manage executive attention and pacing, deliver a chart while controlling its reveal, handle Q&A including hostile and off-topic questions, navigate senior Saudi government-audience dynamics (protocol, bilingual delivery, hierarchy), and improve measurably across recorded rehearsal rounds.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Open a briefing with a BLUF and a clear ask | LO6 |
| 6.2 | Manage executive attention, pacing, and time discipline | LO6 |
| 6.3 | Deliver a chart while controlling its reveal and narration | LO6, LO4 |
| 6.4 | Handle Q&A, including hostile, off-topic, and "your data is wrong" questions | LO6 |
| 6.5 | Navigate senior-audience dynamics and bilingual delivery appropriately | LO6 |
| 6.6 | Iterate delivery measurably using recorded self-review and critique | LO6, LO5 |

## Technical Content

### 1. Executive attention economics

An executive audience is not a hostile audience, but it is a *scarce* one: senior decision-makers arrive with partial attention, competing priorities, and a habit of deciding early. Three consequences shape delivery:

- **The first thirty seconds decide the frame.** Open with the recommendation and the ask (BLUF), not with "thank you, let me give some background." Background spent before the ask is attention spent before the point.
- **Attention decays; front-load value.** Put the most decision-relevant slide first, not last. Assume they may be interrupted or called away at minute three — the recommendation must already have landed.
- **They will decide with less than you gave them.** Design for the executive who acts on the top-line alone; the deck's depth exists to *survive scrutiny*, not to be fully traversed. This is Module 5's BLUF, now a delivery behaviour.

### 2. Structuring the spoken briefing (vs the deck)

The spoken briefing has its own structure, layered on the seven-slide arc:

1. **The top-line (0:00–0:30):** "I'm recommending we direct the next SAR 40 million to three lagging regions to hit 65% adoption by December. Here's why in three points."
2. **Three supporting beats (0:30–5:00):** situation, complication, evidence — one chart each, one message each, narrated as scenes (Module 5).
3. **The options and the recommendation (5:00–6:30):** the three uses compared, the choice, the expected effect.
4. **The ask and next step (6:30–7:00):** an explicit, decidable request — "I'm asking the committee to approve the reallocation, with a checkpoint in 90 days."

The rule: **say the ask twice** — once at the top (BLUF) and once at the end (close). Everything between earns the second ask.

### 3. Delivering a chart out loud

A chart on a screen is not self-explanatory when you are talking over it; presenting a chart is a distinct skill:

- **Orient before you assert.** One sentence on what the axes are before the point — "each bar is a region, longer is higher adoption" — then the takeaway. Executives who are still decoding the axes do not hear the conclusion.
- **Control the reveal.** Use progressive build (Module 5) so the audience looks where you are speaking; a fully-rendered dense chart invites them to read ahead and stop listening.
- **Point at the evidence, not the whole chart.** Name and gesture to the specific mark that carries the argument (the annotated laggard), consistent with the slide's one callout.
- **Never read the chart aloud.** The title states the takeaway; you add the *why* and the *so what*, you do not narrate every bar.

### 4. Handling Q&A

Q&A is where credibility is won or lost, and it is coachable:

| Question type | Technique | Tayseer example |
|---|---|---|
| **Clarifying** | Answer briefly, return to the arc | "Yes, latest month is June." |
| **Hostile / "your data is wrong"** | Separate the number from the recommendation; acknowledge, route to appendix, hold the thread | "Let me show the source in the appendix — note the recommendation holds even at the lower estimate." |
| **Off-topic / rabbit hole** | Acknowledge, park, redirect | "Important for the roadmap — can we take channel costs offline and stay on the allocation decision?" |
| **The un-known** | Say so, commit to follow up | "I don't have that to hand; I'll send it by Thursday." |
| **The leading question** | Answer the question, not the trap | Restate assumptions before agreeing. |

Two master rules: **bridge back to the Big Idea** after every answer, and **never bluff a number** — a fabricated figure that unravels destroys the whole briefing's credibility. Preparing a Q&A appendix (the cut slides from Module 5) is what makes calm answers possible.

### 5. Senior Saudi government-audience dynamics

Delivering to a Deputy Minister-chaired committee has specific, teachable norms:

- **Protocol and hierarchy.** Address the chair; be aware of seniority order in the room; senior figures may not ask questions directly but through aides — read the room's actual decision flow.
- **Bilingual delivery.** Be ready to deliver or answer in Arabic or English; keep the deck's bilingual discipline (Module 3 RTL) consistent; do not code-switch mid-sentence unless the room does.
- **Formality and brevity.** Senior government audiences reward concision and respect for their time; over-familiarity or padding reads poorly. The BLUF is also a courtesy.
- **Decision culture.** The visible decision may be deferred to private consultation; your job is to make the recommendation and its rationale unambiguous enough to survive a conversation you are not in — which is exactly why the annotated, self-contained scenes (Module 3/5) matter.

### 6. Rehearsal, recording, and iteration (the lab method)

Delivery is improved by reps, not advice. The lab method:

- **Record every rehearsal.** Watching one's own delivery is the single most effective feedback in the course — filler words, pace, and eye contact are undeniable on video in a way no critique achieves.
- **Time discipline.** Rehearse to the slot with a visible timer; overrunning a Deputy Minister's slot is itself a failure. Practise the "cut to the ask" move for when time is halved on the spot.
- **Structured critique.** Use a fixed rubric (opening/BLUF, one-message-per-slide, chart delivery, Q&A, time, presence) so feedback is specific and kind (critique the delivery, not the person — the Day 1 norm).
- **Iterate across rounds.** Two recorded rounds with critique between them produce visible improvement; the benchmark is the *delta*, not the first attempt.

Common mistakes to pre-empt: burying the ask; reading slides; defending a challenged number to the death instead of bridging back; running over time; apologising ("sorry, this is a busy slide" — then why is it up?).

## Code Examples

### A speaker-notes and timing generator from the storyboard

```python
# story/speaker_notes.py
"""Module 6 — generate timed speaker notes + the twice-stated ask from the M5 storyboard.
Delivery is a plan too: every scene gets a time box and a one-line narration cue."""
from story.tayseer_storyboard import STORYBOARD, BIG_IDEA

TIME_BOX = {"BLUF": 30, "situation": 45, "complication": 60, "evidence": 75,
            "options": 90, "resolution": 60, "ask": 30}   # seconds, sums to 7 min

def build_notes(storyboard):
    total = 0
    print(f"OPEN (say the ask): {BIG_IDEA}\n")
    for s in storyboard:
        secs = TIME_BOX.get(s.arc_role, 45); total += secs
        print(f"[{total//60}:{total%60:02d}] Slide {s.n} ({s.arc_role}, {secs}s)")
        print(f"   Orient: state axes in one line, then the takeaway: \"{s.message}\"")
        print(f"   Point at: the highlighted mark only. Do NOT read the chart.\n")
    assert total <= 7*60, f"Over slot by {total-420}s — cut, don't rush."
    print("CLOSE (say the ask AGAIN): Approve the reallocation; 90-day checkpoint.")
    print(f"Total: {total//60}:{total%60:02d} / 7:00")

if __name__ == "__main__":
    build_notes(STORYBOARD)
```

### A Q&A preparation matrix

```python
# story/qa_prep.py
"""Pre-build answers to the questions a committee will actually ask.
Each answer: acknowledge -> respond briefly -> BRIDGE back to the Big Idea."""
QA = [
    {"q": "Aren't those regions just small? (hostile/leading)",
     "answer": "Per-capita, not absolute — see appendix A2. The gap is real adoption, not size.",
     "bridge": "which is exactly why targeted spend, not blanket infrastructure, closes it."},
    {"q": "Your adoption number looks high vs finance's. (data-wrong)",
     "answer": "We recompute from unique users, not a column average — appendix A5 reconciles it.",
     "bridge": "and the recommendation holds even at finance's lower figure."},
    {"q": "Why not spend it on the app instead? (off-topic-ish)",
     "answer": "Channel infra is option 2 on the compare slide; slower gap-close per riyal.",
     "bridge": "so region-targeting stays the fastest route to 65% by December."},
    {"q": "What's the ROI in year two? (the un-known)",
     "answer": "I don't have year-two modelling to hand; I'll send it Thursday.",
     "bridge": "the 90-day checkpoint is designed to catch exactly that."},
]

def drill(qa):
    for i, item in enumerate(qa, 1):
        print(f"Q{i}: {item['q']}\n  A: {item['answer']}\n  ->bridge: ...{item['bridge']}\n")

if __name__ == "__main__":
    drill(QA)
```

### A rehearsal critique rubric as a scorer

```python
# story/rehearsal_score.py  — the fixed critique rubric, applied to two recorded rounds.
"""Score delivery the SAME way each round so the DELTA is the learning signal."""
CRITERIA = ["opening_bluf", "one_message_per_slide", "chart_delivery",
            "qa_handling", "time_discipline", "presence"]   # each 0-5

def score_round(scores: dict, notes: str = "") -> dict:
    assert set(scores) == set(CRITERIA), "score every criterion"
    total = sum(scores.values()); pct = 100 * total / (5*len(CRITERIA))
    return {"total": total, "pct": round(pct), "notes": notes}

r1 = score_round({"opening_bluf": 2, "one_message_per_slide": 3, "chart_delivery": 2,
                  "qa_handling": 2, "time_discipline": 3, "presence": 3},
                 "buried the ask; ran 40s over")
r2 = score_round({"opening_bluf": 5, "one_message_per_slide": 4, "chart_delivery": 4,
                  "qa_handling": 4, "time_discipline": 5, "presence": 4},
                 "led with ask; on time; bridged the hostile Q")
print(f"Round 1: {r1['pct']}%   Round 2: {r2['pct']}%   Delta: +{r2['pct']-r1['pct']} pts")
```

## Hands-on Lab 6 — The Executive Delivery Clinic

| | |
|---|---|
| **Objective** | Deliver the Module 5 seven-slide narrative to a simulated Steering Committee in a 7-minute slot, handle a Q&A round, and improve measurably across two recorded rehearsal rounds |
| **Duration** | 50 minutes (runs into capstone rehearsal) |
| **Setup** | The M5 storyboard + scenes; `story/speaker_notes.py`, `qa_prep.py`, `rehearsal_score.py`; a recording device (phone/laptop) per pair; a visible timer; consent forms for recording |

**Instructions & tasks**

1. *(5 min)* Generate timed speaker notes with `speaker_notes.py`; confirm the ask is stated at open and close and the total is ≤ 7:00.
2. *(5 min)* Build your Q&A matrix in `qa_prep.py`: at least four questions including one hostile and one "your data is wrong," each with an answer and a bridge back to the Big Idea.
3. *(10 min)* **Round 1:** deliver the 7-minute briefing to your pair (playing the committee), recorded. The "committee" asks two prepared questions from your matrix.
4. *(5 min)* Self-review the recording against the rubric (`rehearsal_score.py`); note the two highest-leverage fixes (usually: bury-the-ask and time).
5. *(5 min)* Structured peer critique: the committee scores the same rubric; critique the delivery, not the person; one fix per criticism.
6. *(10 min)* **Round 2:** re-deliver with fixes, recorded; committee asks one *new* (unprepared) question to test bridging.
7. *(5 min)* Score Round 2; compute the delta; save both recordings + scores as `lab6_solution`. Note the single behaviour that moved the most.

**Expected output**
```
Speaker notes: ask at 0:00 and 7:00, total 7:00 / 7:00.
Q&A matrix: 4 questions (1 hostile, 1 data-wrong), each bridged to the Big Idea.
Round 1: 50% — buried the ask, ran 40s over, read one chart aloud.
Round 2: 87% — led with the ask, on time, bridged an unprepared question. Delta +37 pts.
Biggest mover: opening with the BLUF (2 -> 5).
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Ran over the slot | Too much narration per slide | Time-box each scene; practise the "cut to the ask" for a halved slot |
| Ask landed late | Background-first habit | Say the recommendation in the first 30 seconds; say it again to close |
| Froze on a hostile question | No prepared bridge | Pre-build the Q&A matrix; acknowledge → answer briefly → bridge |
| Read the chart aloud | Treating the title as a script | Title = takeaway; you add the why/so-what and point at one mark |
| Recording feels awkward to watch | Normal; that discomfort is the signal | Watch once for content, once for delivery; fix the top two only |
| Defended a challenged number to the death | Number conflated with recommendation | Separate them; route detail to appendix; show the recommendation survives |

**Instructor notes.** The recording is non-negotiable and is the module's engine — obtain consent up front and reassure the room the videos are theirs. The reliable "aha" is the Round-1 → Round-2 delta: almost everyone jumps 20–40 points by simply leading with the ask and holding time, and *seeing* that on the rubric converts skeptics. Play the tough committee member yourself for one pair to model the hostile-question bridge. Fast finishers: deliver the Arabic version, or take a halved slot on the spot. This lab flows directly into capstone rehearsal — the reps here are the capstone's delivery.

## Mini Exercises

**Quiz (5 questions)**
1. When must the ask be stated? → in the first 30 seconds (BLUF) and again at the close.
2. Before asserting a chart's point, what must you do? → orient the audience to the axes in one sentence.
3. A committee member says "your data is wrong." First move? → separate the number from the recommendation; acknowledge and route to appendix; show the recommendation holds.
4. After any Q&A answer, where do you return? → the Big Idea (bridge back).
5. Why record rehearsals? → self-review of delivery (filler, pace, eye contact) is the most effective feedback; the round-to-round delta is the learning signal.

**Bridge drill.** The instructor fires off-topic and hostile questions rapid-fire; participants practise "acknowledge → brief answer → bridge to the Big Idea" in one breath each.

**Cold-open exercise.** Each participant delivers only their first 30 seconds (the BLUF) to the room; the room scores "did the ask land?" — repeat until it does.

**Discussion questions.**
- The chair halves your slot to three minutes on the spot. What survives, and in what order? (the ask, the one strongest evidence scene, the ask again)
- When is it right to concede a point in Q&A rather than defend it? (when conceding a detail leaves the recommendation intact; defending trivia burns credibility and time)

## Case Study — The Steering Committee Briefing That Won the Reallocation

**Scenario.** The Tayseer analytics lead has one seven-minute slot before a Steering Committee chaired by a Deputy Minister to secure the SAR 40 million reallocation. In the rehearsal, the lead opened with three minutes of program history, put the recommendation on the last slide, and — when a member challenged the adoption figure — spent two minutes defending the number and never returned to the ask. The committee, in the real session, would have run out of patience before the recommendation appeared.

**Business context.** This is the culminating decision the entire course's analysis exists to influence. Losing the room here wastes a quarter of work and the team's credibility; winning it funds three regions and cements analytics as a decision partner.

**Technical challenge.** Rebuild the *delivery* (not the deck) so the ask lands in thirty seconds, the seven scenes fit the slot, and the inevitable "your number is wrong" and "aren't those regions just small" challenges are handled without losing the thread — in a formal, bilingual, senior-government setting.

**Constraints.** Seven-minute slot (assume it may be halved); Deputy Minister-chaired, protocol-sensitive; bilingual; static slides with a Q&A appendix; the challenged number is legitimately different from finance's, and must be reconciled honestly.

**Solution approach (facilitate, don't lecture).** (1) Re-open with the BLUF; move history to a single situation slide. (2) Time-box the seven scenes; rehearse to a visible timer and practise the halved-slot cut. (3) Pre-build the Q&A matrix; for the number challenge, separate figure from recommendation, reconcile in the appendix, show the recommendation survives the lower estimate, and bridge back. (4) Rehearse recorded, twice, scoring the delta. (5) Respect protocol: address the chair, keep the bilingual discipline, close by restating the ask.

**Discussion questions.**
1. Why does opening with three minutes of history lose the room even when the history is accurate?
2. How should the lead have handled the challenged adoption number so it strengthened, rather than derailed, the briefing?
3. What changes when the slot is halved on the spot — what is the minimum viable briefing?
4. How do senior-audience protocol and bilingual delivery interact with the BLUF discipline in this room?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Ask stated in first 30 seconds | Opening | Yes | Recording review |
| Delivery within the slot | Time discipline | ≤ 7:00 | Timer |
| Q&A answers bridged to the Big Idea | Q&A | 100% | Rubric |
| Charts oriented before asserted | Chart delivery | 100% | Rubric |
| Round-1 → Round-2 rubric improvement | Iteration | ≥ +15 points | `rehearsal_score.py` |
| Hostile/off-topic question handled without losing thread | Composure | Yes | Committee note |

**Example benchmark table (filled during lab):**

| Criterion (0–5) | Round 1 | Round 2 |
|---|---|---|
| Opening / BLUF | 2 | 5 |
| One message per slide | 3 | 4 |
| Chart delivery | 2 | 4 |
| Q&A handling | 2 | 4 |
| Time discipline | 3 | 5 |
| Presence | 3 | 4 |
| **Total (%)** | **50%** | **87%** |

## Required Visuals and Training Assets

### Diagrams
1. **Attention-decay curve** — *Purpose:* justify front-loading. *Elements:* a decaying attention line over a 7-minute slot with "ask lands here (0:30)" marked near the peak and "old habit: ask at 7:00" marked in the trough. *Style:* annotated line, English + Arabic. *Designer description:* "A downward attention curve across seven minutes; a green flag at 0:30 labelled 'BLUF', a red flag at 7:00 labelled 'buried ask'."
2. **Spoken-briefing structure** — *Purpose:* the delivery template. *Elements:* top-line → three beats → options/recommendation → ask, with time boxes and 'say the ask twice' marked. *Style:* timeline strip.
3. **Q&A handling matrix** — *Purpose:* Q&A coaching. *Elements:* five question types × technique × bridge-back, with the "never bluff a number" rule stamped. *Style:* table poster.
4. **Rehearsal feedback loop** — *Purpose:* the lab method. *Elements:* record → self-review → critique → iterate, spiralling to a higher rubric score. *Style:* loop diagram.

### Images (screenshots)
1. **Speaker-notes output**: *why:* Lab 6 reference; *content:* timed notes with the ask at open and close.
2. **Q&A matrix output**: *why:* preparation exemplar; *content:* four questions with answers and bridges.
3. **Rubric score card (Round 1 vs 2)**: *why:* shows the delta that is the grade; *content:* the six-criterion before/after.
4. **Simulated committee room setup**: *why:* stage the lab realistically; *content:* presenter, screen, seated "committee," visible timer.

### Simulations
1. **Hostile-committee bot** — *Setup:* a prompt/checklist that generates realistic challenge questions (data-wrong, off-topic, leading) for the "committee" to fire. *Expected behaviour:* unprepared presenters lose the thread; prepared bridges hold it. *Learning objective:* Q&A is prepared, not improvised.
2. **The halved-slot drill** — *Setup:* mid-delivery, the timer is cut to three minutes. *Expected behaviour:* structured presenters cut to ask + one scene + ask; others rush and overrun. *Learning objective:* the BLUF is what makes a briefing survivable under time pressure.

### Interactive Activities
- **Cold-open round (10 min):** everyone delivers only their 30-second BLUF; the room scores "did the ask land?" and the weakest re-open live.
- **Bridge relay (10 min):** rapid-fire hostile/off-topic questions; participants practise acknowledge → answer → bridge in one breath.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tayseer_services.csv` | (golden thread) | CSV | ~28,000 rows | Underlies the briefing and Q&A appendix |
| M5 storyboard + scenes | Participant (from Lab 5) | py + png | few files | The deck being delivered |
| `qa_bank.md` | Course team | Markdown | 1 page | Bank of realistic committee questions for the "committee" to draw from |
| Recording-consent form | Course team | PDF | 1 page | Consent for rehearsal recording |

### Demo Requirements
- **Instructor demo:** deliver the 7-minute Tayseer briefing twice — once badly (buried ask, over time, defends a number to death), once well (BLUF, on time, bridges the hostile question) — so the room sees the same content win or lose on delivery alone.
- **Student demo:** two pairs present Round 2 to the whole room as a mock committee; the room scores the rubric and names the biggest mover.
- **Expected outputs:** two recorded rehearsal rounds with rubric scores and a positive delta, timed speaker notes, and a prepared Q&A matrix.


