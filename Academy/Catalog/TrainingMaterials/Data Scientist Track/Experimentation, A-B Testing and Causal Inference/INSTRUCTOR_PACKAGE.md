# Experimentation, A/B Testing and Causal Inference
## التجريب واختبارات A/B والاستدلال السببي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Experimentation, A/B Testing and Causal Inference |
| **Arabic Title** | التجريب واختبارات A/B والاستدلال السببي |
| **Code** | SDA-DSC-213 |
| **Track** | Data Scientist (عالم البيانات) |
| **Level** | Specialist (متخصص) |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | Data scientists supporting product, policy, and programme decisions |
| **Prerequisites** | SDA-DSC-111 |
| **Assessment** | Experiment design and analysis project |
| **Stackability** | Causal badge · Core of Analytics & Experimentation specialisation · Next: SDA-DSC-311 |
| **Tools & Platforms** | statsmodels · DoWhy/EconML · experiment simulators (numpy/scipy/pandas · Jupyter) |

## Course Description

A specialist module on answering "what actually works" with data. Participants design and analyse randomised experiments, compute power and sample sizes, and apply causal-inference methods — matching, difference-in-differences, and instrumental variables — when experiments are impossible. The module turns data scientists into trusted advisors on policy and product decisions, able to separate a real effect from a hopeful coincidence and to say precisely how sure they are.

The course is built around a single evolving artefact: **Injaz (إنجاز)**, a unified Saudi digital-government services platform where citizens renew licenses, issue certificates, and pay fees online. Across every module participants run experiments and causal analyses on the same platform — first a clean randomised test of a redesigned document-upload step, then, when randomisation is impossible, quasi-experimental evaluations of a region-by-region reminder-notification rollout and a self-selected digital-literacy programme. Every lab produces a component of an **experimentation toolkit** and a growing analysis notebook, so by Day 4 each participant owns a full experiment design, a powered analysis pipeline, and a causal-inference case study that culminates in the capstone decision memo — the same shape of evidence they will produce in SDA-DSC-311 (Decision Science) and defend in the Data Science capstone.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design randomised experiments with valid randomisation units and guardrail metrics
2. **LO2** — Compute statistical power, sample sizes, and minimum detectable effects
3. **LO3** — Analyze experiment results with correct variance estimation and multiple-testing control
4. **LO4** — Apply quasi-experimental methods including matching and difference-in-differences
5. **LO5** — Evaluate causal claims from observational data using DAG-based reasoning
6. **LO6** — Communicate experimental evidence and uncertainty to decision-makers

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Causal thinking and honest experiments | M1: Causal Thinking & Potential Outcomes · M2: Experiment Design & Randomisation | 55% | 45% | Selection-bias simulation + a fully specified, randomised Injaz experiment design doc |
| **Day 2** | Powering and analysing experiments | M3: Power Analysis & Sample Sizing · M4: Analysis Pitfalls (Peeking, Multiple Testing) | 45% | 55% | Sample-size calculator + a correct, corrected analysis of the uploader experiment |
| **Day 3** | When you cannot randomise | M5: Quasi-Experiments (Matching, DiD, IV) · M6: Causal Graphs & Confounding | 45% | 55% | DiD estimate of the reminder rollout + a DAG-justified observational analysis with refutation tests |
| **Day 4** | From evidence to decision | M7: Experimentation Case Study · Capstone | 30% | 70% | Capstone experiment-and-analysis package + decision memo + panel-style presentation |

## Hour-by-Hour Breakdown

### Day 1 — Causal Thinking and Honest Experiments

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **"What actually works?"** + course kickoff + Injaz golden thread | Distinguish correlation from causation; frame decisions as counterfactual questions; meet the platform and dataset | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Potential outcomes & the fundamental problem** (M1) | Potential outcomes notation, counterfactuals, ATE/ATT, why randomisation identifies causal effects, selection bias | Lecture + whiteboard derivation | 75/25 |
| 3 | **Lab 1 — Simulate potential outcomes and selection bias** | Build a simulator where ground-truth effect is known; show naive comparison is biased, randomisation is not | Guided lab (pairs) | 15/85 |
| 4 | **Experiment design & randomisation** (M2) | Randomisation unit, SUTVA/interference, metric & guardrail design, balance checks, assignment mechanics | Lecture + design walkthrough | 70/30 |
| 5 | **Lab 2 — Design the Injaz uploader experiment** | Choose unit, define OEC + guardrails, write the design doc, randomise and verify balance | Guided lab (pairs) | 15/85 |

### Day 2 — Powering and Analysing Experiments

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Power, MDE, and sample size** (M3) | Type I/II error, power, effect size, the four-way relationship, proportions vs means, variance reduction preview | Lecture + live power curves | 65/35 |
| 2 | **Lab 3 — Build the sample-size calculator** | Implement power/MDE/sample-size functions; produce the run-length plan for Injaz | Guided lab | 15/85 |
| 3 | **Analysis pitfalls: peeking & multiple testing** (M4) | Correct variance estimation, the delta method, CUPED, sequential testing, FDR/Bonferroni, Simpson's paradox | Lecture + simulation demo | 60/40 |
| 4 | **Lab 4 — Analyse the uploader experiment** | Two-proportion test, regression with covariates, CUPED, guardrail checks, multiple-comparison correction | Guided lab | 10/90 |
| 5 | **Reading results honestly** + mini-exercises + benchmarks | Confidence intervals vs p-values, practical vs statistical significance, decision framing | Discussion + worked cases | 40/60 |

### Day 3 — When You Cannot Randomise

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Quasi-experiments & matching** (M5) | Confounding in observational data, propensity scores, matching, weighting, overlap/common support | Lecture + estimator walkthrough | 65/35 |
| 2 | **Lab 5a — Match to evaluate the training programme** | Estimate propensity, match/weight, check balance, estimate ATT, sensitivity to unobserved confounding | Guided lab | 15/85 |
| 3 | **Difference-in-differences & instrumental variables** (M5) | Parallel-trends assumption, DiD estimator, event studies, IV and the reminder-rollout instrument | Lecture + panel-data demo | 60/40 |
| 4 | **Lab 5b — DiD on the regional reminder rollout** | Build the region×time panel, run TWFE DiD, plot event study, test parallel trends | Guided lab | 10/90 |
| 5 | **Causal graphs & confounding** (M6) + **Lab 6** | DAGs, d-separation, backdoor criterion, colliders, DoWhy identify→estimate→refute | Micro-lecture + lab | 30/70 |

### Day 4 — From Evidence to Decision

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Causal graphs deep-dive & refutation** (M6) | Frontdoor, instrument validity in a DAG, refutation tests, when identification fails | Lecture + DoWhy refuters | 50/50 |
| 2 | **Experimentation case study end-to-end** (M7) | Integrate design → power → analysis → causal robustness → decision on one Injaz question | Worked case + facilitation | 40/60 |
| 3 | **Capstone kickoff & build** | Scope the capstone brief; begin design + power + analysis + causal-check pipeline | Project work | 5/95 |
| 4 | **Capstone build + decision memo** | Complete analysis; write the decision memo with quantified uncertainty and a ship/hold recommendation | Project work | 0/100 |
| 5 | **Capstone presentations + assessment + wrap-up** | 6-minute decision briefings; rubric scoring; path to SDA-DSC-311 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module uses the **Injaz** platform and its three datasets (`injaz_sessions.csv`, `injaz_users.csv`, `injaz_regions_panel.csv`). Never introduce a throwaway example — always evolve the Injaz analysis notebook. This is what makes the Day 4 capstone achievable and coherent.
- **Simulation-first pedagogy:** causal inference is invisible in real data because the counterfactual is missing. Teach every method first on a **simulator where the true effect is known**, then apply it to Injaz where it is not. Participants only trust a method after they watch it recover a number they planted.
- **Pace control:** Labs 4 and 5b are the most overrun-prone. Publish checkpoint notebooks (`lab1-start`, `lab1-solution`, … `lab6-solution`) and a `causal_utils.py` starter so stragglers can fast-forward without falling behind on concepts.
- **Pairing:** rotate pairs each day; pair a strong-statistics participant with a strong-Python/pandas participant. The A/B-testing intuition and the panel-data wrangling are different skills — the transfer is the point.
- **Environment strategy:** primary = local Jupyter with `numpy`, `scipy`, `statsmodels`, `pandas`, `matplotlib`, `dowhy`, `econml`, `linearmodels`; fallback = Google Colab (a `requirements.txt` and `!pip install` cell are provided). Verify DoWhy/EconML import cleanly the week before — they have the heaviest dependency chain.
- **Language:** deliver in English or Arabic; keep all code, identifiers, and variable names in English (production and reproducibility convention). Statistical terms are introduced bilingually the first time (e.g., power / القوة الإحصائية).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 4's afternoon is deliberately light on new theory so build and presentation time is protected.
- **Assessment logistics:** the capstone is the catalog assessment ("Experiment design and analysis project"). Collect notebooks and decision memos at the end of Day 4 Hour 4; rubric scoring happens live during Hour 5 briefings. Emphasise from Day 1 that a correct "we cannot conclude" is worth full marks — honesty about uncertainty is the graded skill.

---

# Module 1 — Causal Thinking and Potential Outcomes

## الوحدة 1 — التفكير السببي والنواتج المحتملة

## Module Overview

**Purpose.** Every decision a data scientist supports — ship this feature, fund this programme, send this reminder — is a causal question in disguise: *what would happen if we did this, versus if we did not?* This module installs the mental operating system for the whole course: the potential-outcomes framework. Participants learn to state precisely what causal effect they mean, why the effect can never be observed for a single unit (the fundamental problem of causal inference), and why randomisation — not more data, not a fancier model — is what turns a correlation into a defensible causal claim.

**Business relevance.** Saudi government and enterprise leaders are increasingly asked to justify spend with evidence of impact, not activity metrics. A team that reports "completion rate rose 6% after we launched the new uploader" has said nothing about whether the uploader *caused* the rise — the season, a marketing push, or a policy change could be responsible. Data scientists who can separate the causal signal from the confounded noise become trusted advisors; those who cannot quietly mislead every decision they touch. This is the skill that distinguishes a specialist from an analyst.

**Industry use cases.**
- A digital-government platform must prove a redesigned flow *caused* higher service completion before rolling it nationwide, because a rollback after national launch is politically and operationally expensive.
- A telecom must decide whether a retention offer actually reduces churn or is merely given to customers who would have stayed anyway (selection bias).
- A public-health programme must estimate whether a subsidy changed behaviour among those who received it, knowing recipients differ systematically from non-recipients.

**Expected competencies.** After this module a participant can write a decision as a potential-outcomes contrast, name the estimand (ATE, ATT), explain the fundamental problem of causal inference, articulate why randomisation identifies the ATE, and demonstrate selection bias in a simulator where the ground truth is known.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Express a business decision as a potential-outcomes contrast and name the estimand | LO5, LO6 |
| 1.2 | Explain the fundamental problem of causal inference and the role of the counterfactual | LO5 |
| 1.3 | Decompose the naive difference into ATE plus selection bias | LO5 |
| 1.4 | Justify why randomisation makes treatment independent of potential outcomes | LO1, LO5 |
| 1.5 | Demonstrate selection bias and its removal in a simulation with known ground truth | LO5, LO6 |

## Technical Content

### 1. Correlation, causation, and the cost of confusing them

The oldest sentence in statistics — "correlation is not causation" — is repeated so often that it has stopped changing anyone's behaviour. This module replaces the slogan with machinery. The reason correlation misleads is **confounding**: a third factor that drives both the supposed cause and the effect. On the Injaz platform, users who opt into the new "guided uploader" during a soft launch are disproportionately younger, more digitally literate, and using newer devices — exactly the users who complete services at a high rate regardless of the uploader. Comparing opt-in users to everyone else measures *who chose the feature*, not *what the feature did*.

The practical stakes: a decision made on a confounded comparison is not merely imprecise, it can point the **wrong direction**. A programme that looks beneficial because healthy people enrol can be worthless or harmful. The course's job is to give participants a framework precise enough that these traps become visible before the analysis, not after the rollout.

**Instructor note.** Open with a two-minute audience poll: "Injaz completion rate is 8 points higher for users who received an SMS reminder. Should we send reminders to everyone?" Let the class argue. Someone will say "but maybe reminders go to people who already engage." That intuition *is* the potential-outcomes framework — the rest of the module is making it rigorous.

### 2. The potential-outcomes framework (Neyman–Rubin)

For each unit *i* and a binary treatment *T ∈ {0,1}*, define two **potential outcomes**:

- *Yᵢ(1)* — the outcome if unit *i* is treated
- *Yᵢ(0)* — the outcome if unit *i* is not treated

The **individual treatment effect** is *τᵢ = Yᵢ(1) − Yᵢ(0)*. This is the honest definition of "the effect of the treatment on this unit": the difference between two versions of the same world that differ only in the treatment.

The observed outcome links to the potential outcomes through the treatment actually received:

*Yᵢ = Tᵢ · Yᵢ(1) + (1 − Tᵢ) · Yᵢ(0)*

We define the estimands the course cares about:

- **ATE** (Average Treatment Effect): *E[Y(1) − Y(0)]* over the whole population — "if we gave the uploader to everyone versus no one."
- **ATT** (Average Treatment effect on the Treated): *E[Y(1) − Y(0) | T = 1]* — "the effect among the users who actually got it." ATT is usually the right estimand for evaluating a programme that was rolled out to a specific group.
- **CATE** (Conditional ATE): *E[Y(1) − Y(0) | X = x]* — the effect for a subgroup, the foundation of heterogeneous-effects analysis (Module 5's EconML).

Naming the estimand *before* touching data is a discipline that prevents most causal confusion. "The effect" is ambiguous; "the ATT on completion rate for users in the Riyadh region during Q2" is answerable.

### 3. The fundamental problem of causal inference

Here is the wall every method in this course exists to climb: **we can never observe both *Yᵢ(1)* and *Yᵢ(0)* for the same unit.** A user either got the new uploader or did not; the other outcome is a counterfactual that never happened. The individual effect *τᵢ* is therefore fundamentally unobservable. Causal inference is, in Holland's phrase, a **missing-data problem** — exactly half the potential outcomes are missing, and no cleverness recovers a specific missing value.

What we *can* estimate are **averages**. Even though no individual's *τᵢ* is observable, the *average* *E[Y(1) − Y(0)]* can be identified under the right conditions, because averages let treated units stand in for the counterfactuals of control units and vice versa. The entire discipline is the study of *when* that substitution is valid.

The naive estimator is the difference in observed group means:

*τ̂ₙₐᵢᵥₑ = E[Y | T = 1] − E[Y | T = 0]*

The central algebraic result of the module — derived on the whiteboard — decomposes it:

*E[Y | T=1] − E[Y | T=0] = ATT + (E[Y(0) | T=1] − E[Y(0) | T=0])*

The second term is **selection bias**: the difference in the *untreated* potential outcome between the groups. It asks: even with no treatment, would the treated group have differed anyway? For the Injaz opt-in uploader, yes — digitally literate early adopters complete more even without help — so the bias is positive and the naive estimate overstates the effect. Randomisation's whole job is to force that bias term to zero.

### 4. Why randomisation works

When treatment *T* is assigned by a coin flip, it is **statistically independent of the potential outcomes**: *(Y(0), Y(1)) ⊥ T*. This independence is not an assumption to be hoped for — it is *manufactured* by the design. Its consequences are decisive:

- *E[Y(0) | T=1] = E[Y(0) | T=0]* ⇒ the selection-bias term vanishes.
- The treated group's average untreated outcome equals the control group's observed average, so the control group is a valid counterfactual for the treated group.
- Therefore *τ̂ₙₐᵢᵥₑ* is an unbiased estimate of the ATE.

Randomisation also balances **unobserved** confounders in expectation — the ones you did not think to measure. This is its unique power and why the randomised controlled experiment (A/B test) is the gold standard: a matching model can only adjust for confounders you named and measured; randomisation handles the ones you never knew existed. Everything in Modules 5–6 is an attempt to approximate this power when a coin flip is impossible, and each approximation buys weaker guarantees.

**Key nuance for the class.** Randomisation guarantees balance *in expectation*, not in any single experiment. A specific 50/50 split can still be unlucky and imbalanced on age. This is why we (a) check balance (Module 2), (b) can adjust for covariates to reduce variance (Module 4), and (c) size experiments large enough that chance imbalance is small (Module 3).

### 5. Assumptions, best practices, common mistakes

**Assumptions to teach explicitly**
- **SUTVA** (Stable Unit Treatment Value Assumption): one unit's outcome does not depend on another unit's treatment (no interference), and there is only one version of the treatment. Violated when Injaz users share devices or when a "treated" region's residents talk to a "control" region's residents. Introduced here, deepened in Module 2.
- **Consistency:** the observed outcome under the received treatment equals that treatment's potential outcome.
- **Ignorability / unconfoundedness:** *(Y(0), Y(1)) ⊥ T | X* — treatment is as-good-as-random given covariates. *Guaranteed* by randomisation; *assumed and unverifiable* in observational studies (Modules 5–6).

**Common mistakes (each demonstrated in Lab 1)**
1. Reporting the naive difference on self-selected groups and calling it "the effect."
2. Controlling for a variable on the causal path (a mediator) or a collider, which *introduces* bias — the pre-emptive warning for Module 6.
3. Confusing ATE and ATT and then generalising a programme's effect on volunteers to the whole population.
4. Believing "we have millions of rows, so bias is not a problem" — bias does not shrink with sample size, only variance does. This is the single most expensive misconception in applied data science.
5. Interpreting a regression coefficient as causal without a design or an identification argument.

**Production considerations.** In an organisation, the potential-outcomes framing is also a *communication* tool: forcing a stakeholder to state the counterfactual ("compared to what?") exposes vague requests and aligns everyone on what "impact" means before a single query runs.

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides). A ministry launches a voluntary digital-skills workshop and reports that attendees complete online services at a 22-point higher rate than non-attendees — proof, the deck says, that the workshop works. A skeptical data scientist asks one question: who attends workshops? Motivated, already-engaged citizens. She reframes it in potential outcomes: the 22 points is *ATT + selection bias*, and the selection bias is almost certainly large and positive because attendees would have completed more *even without the workshop*. She proposes the fix the rest of this course teaches: a randomised invitation, or — since the workshops already happened — matching on pre-workshop engagement (Module 5). The re-analysis later shows the true effect is closer to 4 points: real, worth funding, but a fifth of the headline. The 18-point gap was selection bias, and a nationwide budget was nearly set by it.

## Code Examples

### A potential-outcomes simulator (ground truth known)

```python
# injaz_causal/potential_outcomes.py
"""A simulator where BOTH potential outcomes exist, so we can see the
counterfactual we could never observe in reality. This is the teaching
device for the whole course: plant a known effect, then check which
estimator recovers it.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(213)

def simulate_injaz_users(n: int = 20_000, true_effect: float = 0.05) -> pd.DataFrame:
    """Simulate users of the Injaz portal with a KNOWN causal effect of the
    new guided uploader on service-completion probability.

    digital_literacy is a confounder: it raises baseline completion AND
    makes a user more likely to opt into the new uploader.
    """
    literacy = rng.beta(2, 2, size=n)                 # 0..1 latent skill
    age = rng.integers(18, 70, size=n)

    # Baseline completion probability under CONTROL (no new uploader), Y(0)
    base = 0.35 + 0.40 * literacy - 0.002 * (age - 40)
    p0 = np.clip(base, 0.01, 0.99)
    # Under TREATMENT the uploader adds `true_effect` to the probability, Y(1)
    p1 = np.clip(p0 + true_effect, 0.01, 0.99)

    y0 = rng.binomial(1, p0)                           # potential outcome Y(0)
    y1 = rng.binomial(1, p1)                           # potential outcome Y(1)

    df = pd.DataFrame({"age": age, "digital_literacy": literacy,
                       "p0": p0, "p1": p1, "y0": y0, "y1": y1})
    # The individual effect — REAL here, UNOBSERVABLE in the wild
    df["tau_i"] = df["y1"] - df["y0"]
    return df

users = simulate_injaz_users()
true_ate = (users["p1"] - users["p0"]).mean()
print(f"True ATE (planted): {true_ate:.4f}")           # ~0.0500
```

### Selection bias vs randomisation, side by side

```python
# injaz_causal/selection_vs_random.py
"""Show the decomposition from Section 3 numerically: a self-selected
rollout is biased; a randomised rollout is not. Same users, same true
effect — only the ASSIGNMENT mechanism differs.
"""
import numpy as np
from injaz_causal.potential_outcomes import simulate_injaz_users, rng

users = simulate_injaz_users()

# ---- Assignment 1: SELF-SELECTION (confounded) ----
# High-literacy users opt into the new uploader more often.
p_optin = 0.15 + 0.70 * users["digital_literacy"]
users["T_self"] = rng.binomial(1, p_optin)

# ---- Assignment 2: RANDOMISATION (a coin flip) ----
users["T_rand"] = rng.binomial(1, 0.5, size=len(users))

def observed_outcome(df, t_col):
    return np.where(df[t_col] == 1, df["y1"], df["y0"])

def naive_diff(df, t_col):
    y = observed_outcome(df, t_col)
    return y[df[t_col] == 1].mean() - y[df[t_col] == 0].mean()

true_ate = (users["p1"] - users["p0"]).mean()
print(f"True ATE            : {true_ate: .4f}")
print(f"Naive (self-select) : {naive_diff(users, 'T_self'): .4f}  <- biased high")
print(f"Naive (randomised)  : {naive_diff(users, 'T_rand'): .4f}  <- ~unbiased")
# Typical output:
# True ATE            :  0.0500
# Naive (self-select) :  0.1930  <- selection bias inflates it ~4x
# Naive (randomised)  :  0.0487  <- recovers the truth within noise
```

### Quantifying the selection-bias term

```python
# injaz_causal/bias_decomposition.py
"""Because the simulator exposes Y(0) for EVERYONE, we can compute the
selection-bias term directly:  E[Y(0)|T=1] - E[Y(0)|T=0]."""
from injaz_causal.selection_vs_random import users

for t_col, label in [("T_self", "self-selection"), ("T_rand", "randomised")]:
    y0_treated = users.loc[users[t_col] == 1, "y0"].mean()
    y0_control = users.loc[users[t_col] == 0, "y0"].mean()
    bias = y0_treated - y0_control
    att  = users.loc[users[t_col] == 1, "tau_i"].mean()
    print(f"{label:14s}: ATT={att:.4f}  selection_bias={bias:+.4f}  "
          f"naive≈ATT+bias={att+bias:.4f}")
# self-selection: ATT=0.0500  selection_bias=+0.1430  naive≈0.1930
# randomised    : ATT=0.0500  selection_bias=+0.0000  naive≈0.0500
```

## Hands-on Lab 1 — Simulate Potential Outcomes and Selection Bias

| | |
|---|---|
| **Objective** | Build an Injaz user simulator with known ground truth; demonstrate that a naive comparison of self-selected groups is biased while a randomised comparison recovers the true effect; quantify the selection-bias term |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, Jupyter, `numpy pandas matplotlib scipy`; notebook `lab1-start.ipynb` (`git checkout lab1-start`) |

**Instructions & tasks**

1. *(8 min)* Complete `simulate_injaz_users()` so that `digital_literacy` raises both baseline completion and opt-in probability. Confirm the planted ATE prints ≈ 0.05.
2. *(10 min)* Implement both assignment mechanisms (self-selection and randomisation) and the `naive_diff` estimator against the correctly-revealed observed outcome.
3. *(10 min)* Compute the naive difference under each mechanism; explain in a markdown cell why they differ although the true effect is identical.
4. *(10 min)* Compute the selection-bias term *E[Y(0)|T=1] − E[Y(0)|T=0]* directly (possible only because the simulator exposes both potential outcomes) and verify naive ≈ ATT + bias.
5. *(7 min)* Sweep sample size `n ∈ {1k, 10k, 100k, 1M}`; plot the naive self-selection estimate vs `n`. Show it converges to the *biased* value, not the truth — bias does not shrink with data.
6. *(5 min)* Write a three-sentence conclusion a non-technical manager could read.

**Expected output**
```
True ATE (planted): 0.0500
Naive (self-select): 0.1930   |  bias term: +0.1430
Naive (randomised) : 0.0487   |  bias term: +0.0000
As n -> 1,000,000 the self-selection estimate converges to 0.193, NOT 0.05.
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Naive randomised estimate far from 0.05 | `n` too small; unlucky split | Increase `n`; average over several seeds to show it centres on 0.05 |
| Self-selection estimate ≈ true ATE | Opt-in not actually correlated with literacy | Check `p_optin` uses `digital_literacy`; print the correlation |
| Probabilities outside [0,1] | Missing `np.clip` | Clip `p0`, `p1` before `binomial` |
| Bias term ≈ 0 under self-selection | Revealed the wrong potential outcome | `observed = where(T==1, y1, y0)`; verify indexing |

**Instructor notes.** The sample-size sweep in step 5 is the emotional core of the module — watch faces when the "big data" estimate confidently converges to the wrong answer. Fast finishers: add a covariate-adjusted estimate (regress `y` on `T` and `digital_literacy`) and show it partially removes the bias — a teaser for Modules 4 and 6.

## Mini Exercises

**Quiz (5 questions)**
1. What are the two potential outcomes for a unit under a binary treatment? → *Y(1)* and *Y(0)*, the outcomes with and without treatment.
2. State the fundamental problem of causal inference. → For any unit only one potential outcome is observed; the counterfactual is missing, so individual effects are unobservable.
3. Decompose the naive difference of means. → ATT + selection bias, where bias = *E[Y(0)|T=1] − E[Y(0)|T=0]*.
4. Why does randomisation eliminate selection bias? → It makes *T* independent of potential outcomes, so *E[Y(0)|T=1] = E[Y(0)|T=0]*.
5. True/False: with enough data, selection bias disappears. → **False**; more data shrinks variance, not bias.

**Debugging exercise.** Give a notebook that reveals the observed outcome as `where(T==1, y0, y1)` (swapped). The estimated effect has the wrong sign; participants must locate the inverted counterfactual.

**Estimand exercise.** For three Injaz decisions ("should we launch the uploader to all users", "did the workshop help attendees", "what is the effect for elderly users"), each pair writes the estimand (ATE / ATT / CATE) and the potential-outcomes contrast in one line.

**Discussion questions.**
- A stakeholder says "we have 4 million rows, the result must be reliable." What do you say? (large *n* controls variance, not confounding; a biased estimator stays biased)
- When is ATT the more relevant estimand than ATE? (evaluating a programme delivered to a specific self-selected or targeted group)

## Case Study — The Voluntary Workshop That "Worked"

**Scenario.** The Ministry of Human Resources ran a voluntary "Digital Services Skills" workshop across five cities. An internal deck reports attendees subsequently complete Injaz services at 71% versus 49% for non-attendees and recommends a SAR 40M nationwide rollout.

**Business context.** The number is real and the correlation is strong. The rollout decision hinges entirely on whether the 22-point gap is *caused* by the workshop.

**Technical challenge.** Attendance was self-selected. Frame the 22 points in potential-outcomes terms and identify every reason the naive comparison is untrustworthy.

**Constraints.** The workshops already happened (no re-randomising the past); only observational data on attendees and non-attendees exists; a decision is due in three weeks.

**Solution approach (facilitate, don't lecture).** (1) Write the estimand: ATT of the workshop on completion. (2) Decompose 22 points = ATT + selection bias; argue the bias sign is positive. (3) Enumerate confounders (baseline literacy, age, prior Injaz usage, region). (4) Recognise this is now an observational problem requiring matching or DiD (Module 5) — and pre-commit to *randomising the next cohort's invitations* so the next evaluation is clean.

**Discussion questions.**
1. What is the sign of the selection bias here, and why?
2. Which single design change would have made this analysis trivial?
3. If matching later shows a 4-point effect, is the workshop worth funding? What else do you need? (cost per completion, counterfactual value of a completion)
4. How would you present "the headline is 22 but the honest estimate is 4" to the deck's author without making an enemy?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Recovery of planted ATE (randomised) | Correctness | within ±0.005 of 0.05 at n=100k | simulator + naive estimator |
| Selection-bias term reproduced | Correctness | matches naive − ATT to 3 dp | direct computation on Y(0) |
| Estimand named before analysis | Rigor | 3/3 decisions correctly typed | estimand exercise |
| Bias-vs-n misconception corrected | Understanding | correct written explanation | conclusion cell + quiz Q5 |
| Time to explain counterfactual to a peer | Fluency | < 2 min, unaided | pair check |

**Example benchmark table (filled during lab):**

| Assignment mechanism | Estimate | Selection bias | Distance from true ATE (0.05) |
|---|---|---|---|
| Self-selection | 0.193 | +0.143 | 0.143 (biased) |
| Randomisation | 0.049 | +0.000 | 0.001 (unbiased) |

## Required Visuals and Training Assets

### Diagrams
1. **The two-worlds counterfactual** — *Purpose:* anchor image for the whole course. *Elements:* one user shown in two parallel worlds (treated / not treated), each with an outcome; a scissors icon cutting one world away labelled "never observed". *Style:* flat vector, two-panel split, English labels with Arabic subtitles (النواتج المحتملة).
2. **Naive difference decomposition** — *Purpose:* make selection bias visible. *Elements:* a bar for the naive difference split into an "ATT" segment and a "selection bias" segment. *Style:* stacked-bar explainer.
3. **Confounding triangle for Injaz** — *Purpose:* concretise the confounder. *Elements:* nodes digital_literacy → uploader-adoption and digital_literacy → completion, with the spurious uploader→completion path highlighted. *Style:* simple DAG (foreshadows Module 6).
4. **Bias-does-not-shrink-with-n** — *Purpose:* kill the big-data misconception. *Elements:* two convergence curves vs sample size — randomised converging to 0.05, self-selected converging to 0.19. *Style:* line chart with a labelled gap.

### Images (screenshots)
1. **Jupyter notebook — simulator output**: *why:* expected-output reference; *content:* the printed true-ATE and both naive estimates.
2. **Whiteboard photo — the decomposition derivation**: *why:* participants re-derive it; *content:* the algebra from *E[Y|T=1] − E[Y|T=0]* to ATT + bias.
3. **Plot — convergence vs n**: *why:* the module's punchline made visual; *content:* the two curves with the persistent gap annotated.

### Simulations
1. **Confounding strength dial** — *Setup:* a slider for the literacy→opt-in coefficient. *Expected behaviour:* as confounding rises, the naive self-selection estimate diverges further from 0.05 while the randomised estimate stays put. *Learning objective:* bias magnitude is set by confounding strength, not sample size.
2. **Unlucky randomisation** — *Setup:* fix `n = 500` and reseed. *Expected behaviour:* individual randomised estimates scatter around 0.05, occasionally far off. *Learning objective:* randomisation balances *in expectation*; small experiments still need power (Module 3) and balance checks (Module 2).

### Interactive Activities
- **"Compared to what?" round (10 min):** the instructor reads six real-sounding impact claims; the class shouts the missing counterfactual for each.
- **Estimand card sort (10 min):** 12 decision cards sorted onto ATE / ATT / CATE bins, then defended.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_users.csv` | Synthetic, course-generated (KSA age distribution, latent literacy, region) | CSV | 20,000 rows × 8 cols | Simulator seed + confounder illustration; reused across modules |
| `simulated_potential_outcomes.parquet` | Produced by the simulator with both Y(0), Y(1) | Parquet | 20,000 rows | Ground-truth checks unavailable in real data |

### Demo Requirements
- **Instructor demo:** live-code the swap from self-selection to randomisation and watch the estimate jump from 0.19 to 0.05 in under 6 minutes — the speed *is* the message.
- **Student demo:** one pair explains their convergence-vs-n plot and states the one-sentence implication for "big data" projects.
- **Expected outputs:** planted ATE recovered under randomisation; selection-bias term reproduced to 3 decimal places.

---

# Module 2 — Experiment Design and Randomisation

## الوحدة 2 — تصميم التجارب والعشوائية

## Module Overview

**Purpose.** Module 1 proved that randomisation is what buys a causal claim. This module turns that principle into an operational experiment. Participants learn to choose the randomisation unit, define the metric that decides the experiment (the Overall Evaluation Criterion) and the guardrails that protect against collateral damage, defend against interference and other SUTVA violations, execute the assignment reproducibly, and verify balance before trusting a single result. A powerful analysis cannot rescue a broken design; this is the module where experiments are won or lost.

**Business relevance.** In a national digital-services context, a badly designed experiment is worse than no experiment: it produces a confident number that is wrong, and organisations act on confident numbers. Choosing the wrong randomisation unit (randomising by page-view when users see many pages) silently violates independence and inflates false-positive rates; forgetting a guardrail means a feature that lifts completion while doubling support-ticket load ships unnoticed. Getting design right is what makes an experimentation programme trustworthy enough for ministries to rely on.

**Industry use cases.**
- A government portal randomises a redesigned upload step by *user* (not session) so a returning citizen always sees one consistent experience — required for both statistics and user trust.
- A ride-hailing marketplace cannot randomise by rider because drivers and riders interact; it randomises by *city* and time (switchback) to contain interference.
- A bank tests a new onboarding flow but sets a guardrail on fraud rate: any variant that lifts sign-ups while raising fraud is auto-rejected regardless of the primary metric.

**Expected competencies.** Participants can select and justify a randomisation unit, design an OEC with guardrail and diagnostic metrics, identify SUTVA/interference risks and mitigations, implement reproducible hash-based assignment, run and interpret a Sample-Ratio-Mismatch (SRM) check and covariate balance test, and write a one-page experiment design document.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Select a randomisation unit appropriate to the intervention and interference risk | LO1 |
| 2.2 | Design an OEC plus guardrail and diagnostic metrics for a decision | LO1, LO6 |
| 2.3 | Identify SUTVA/interference violations and choose a containment design | LO1 |
| 2.4 | Implement reproducible, deterministic random assignment | LO1 |
| 2.5 | Verify assignment integrity with SRM and covariate-balance checks | LO1, LO3 |

## Technical Content

### 1. The anatomy of an online experiment

An A/B test has a fixed skeleton, and naming its parts prevents sloppy design:

- **Unit of randomisation** — what gets independently coin-flipped (user, session, region, device).
- **Unit of analysis** — the level at which the metric is computed (often, but not always, the same as the randomisation unit; a mismatch requires the delta method in Module 4).
- **Treatment / control (variants)** — control is the current experience; treatments are the changes under test.
- **Overall Evaluation Criterion (OEC)** — the single metric that, if it moves favourably without tripping guardrails, means "ship."
- **Guardrail metrics** — things that must *not* get worse (latency, error rate, support tickets, complaints).
- **Exposure / trigger** — the point at which a unit actually experiences the difference. Analysing only *triggered* users sharpens power; forgetting triggering dilutes real effects.

For the Injaz golden thread: the flagship experiment tests a **guided document-uploader** against the current plain uploader. Randomisation unit = **user (national-ID hash)**; OEC = **service-completion rate**; guardrails = **median time-to-complete, support-ticket rate, upload-error rate**; trigger = **reaching the upload step**.

### 2. Choosing the randomisation unit

The choice is driven by three forces:

1. **Consistency of experience.** If a user must not flip between variants across visits, randomise by user, not session. Government services demand this — a citizen seeing two different upload flows in one week erodes trust and pollutes the data.
2. **Interference (SUTVA).** If units affect each other, randomise at a coarser level that contains the spillover. Marketplace supply/demand, social features, and shared devices all push the unit *up* (session → user → household → region).
3. **Statistical power.** Coarser units mean fewer independent observations and lower power. Randomising by region gives strong interference protection but perhaps only 13 units — far too few for a standard test, forcing switchback or synthetic-control designs.

The tension between (1)/(2) and (3) is the core design trade-off. Teach the rule: **randomise at the coarsest unit interference demands, and no coarser.** Over-coarsening throws away power for nothing.

### 3. Metric design: OEC, guardrails, and diagnostics

A good OEC is **sensitive** (moves when the feature works), **directional** (higher is unambiguously better), and **aligned with long-term value** (not a vanity metric a dark pattern could inflate). Completion rate qualifies; "clicks on the upload button" does not — a confusing button gets more clicks.

Metric taxonomy to teach:

| Type | Role | Injaz example |
|---|---|---|
| **OEC / primary** | Decides the experiment | Service-completion rate |
| **Guardrail** | Must not regress | Time-to-complete, support-ticket rate, error rate |
| **Diagnostic / secondary** | Explains *why* | Step-level drop-off, retries per upload |
| **Data-quality** | Validates the experiment itself | Sample-ratio, trigger rate, missing-data rate |

Two hazards: **metric proliferation** (20 primary metrics guarantee a false positive — Module 4's multiple-testing problem) and **surrogate risk** (optimising a short-term proxy that diverges from the true goal). One OEC, a short guardrail list, and clearly-labelled diagnostics is the professional standard.

### 4. SUTVA, interference, and containment designs

SUTVA fails in two ways relevant to Injaz-scale systems:

- **Interference / spillover:** one unit's treatment changes another's outcome. Shared household devices, call-centre agents who learn the new flow and coach control users, or capacity effects (a faster flow frees agents, helping everyone) all break independence.
- **Multiple treatment versions:** "the uploader" is actually three slightly different builds across OS versions — a hidden violation of the single-version assumption.

Containment designs:

- **Cluster randomisation:** randomise groups (households, regions, branches); analyse with cluster-robust variance.
- **Switchback / time-split:** alternate treatment and control across time windows for the whole system — standard for marketplaces and pricing.
- **Two-sided / ego-cluster designs:** for network/social spillover.

Teach the diagnostic instinct: *before* designing, ask "can one user's treatment leak to another?" If yes, the naive user-level A/B test overstates precision and possibly the effect.

### 5. Assignment mechanics and reproducibility

Assignment must be **deterministic, uniform, and independent across experiments**. The professional pattern is **hashing**, not a per-request random draw:

- Hash `experiment_salt + unit_id` → map to `[0,1)` → bucket. Deterministic means a user lands in the same bucket on every request without storing state, and re-runs of the analysis reproduce exactly.
- A distinct **salt per experiment** guarantees that bucketing is independent across concurrent experiments, so overlapping tests do not confound each other.
- **Sample-Ratio Mismatch (SRM):** if you intend 50/50 but observe 50.9/49.1 on 200k users, a chi-square test will flag it — SRM almost always signals a bug (a redirect that drops one arm, a logging race) and **invalidates the experiment** until explained. Never analyse an SRM-failing test.

### 6. Common mistakes & production considerations

1. Randomising by session when users return — breaks independence and consistency.
2. No guardrails — shipping an OEC win that quietly degrades latency or support load.
3. Analysing everyone instead of *triggered* users — dilutes the effect toward zero.
4. Peeking at balance and re-randomising until "balanced" — this is p-hacking the design; randomise once, check, and adjust in analysis, do not re-roll.
5. Ignoring SRM because "it's close" — a 0.5% imbalance on millions of users is highly significant and diagnostic of a real defect.
6. Concurrent experiments sharing a salt — bucket correlation confounds both.
7. Pre-exposure contamination — users who saw the treatment in a leak stay in treatment; define exposure precisely.

**Production considerations.** Real experimentation platforms (the "experiment simulators" in the catalog tooling) log assignment at exposure, enforce mutually-exclusive layers for conflicting experiments, and run automated SRM/guardrail alerts. The design document — unit, OEC, guardrails, MDE, run length, stopping rule — is written and reviewed *before* launch and frozen; changing metrics after seeing data is the cardinal sin.

## Code Examples

### Deterministic hash-based assignment

```python
# injaz_experiment/assignment.py
"""Deterministic bucketing: the same unit always maps to the same arm,
with no stored state, and independent buckets across experiments via salt.
"""
import hashlib
import pandas as pd

def assign_variant(unit_id: str, experiment_salt: str,
                   split: tuple[float, ...] = (0.5, 0.5),
                   arms: tuple[str, ...] = ("control", "treatment")) -> str:
    """Map unit_id to an arm deterministically.

    - hashing (not random draw) => reproducible & stateless
    - experiment_salt => independent bucketing across concurrent tests
    """
    assert abs(sum(split) - 1.0) < 1e-9, "split must sum to 1"
    digest = hashlib.sha256(f"{experiment_salt}:{unit_id}".encode()).hexdigest()
    # take 8 hex chars -> integer -> uniform in [0, 1)
    u = int(digest[:8], 16) / 0xFFFFFFFF
    cum = 0.0
    for arm, frac in zip(arms, split):
        cum += frac
        if u < cum:
            return arm
    return arms[-1]

def assign_frame(users: pd.DataFrame, id_col: str, salt: str) -> pd.DataFrame:
    users = users.copy()
    users["variant"] = users[id_col].astype(str).map(
        lambda uid: assign_variant(uid, salt))
    return users
```

### Sample-Ratio-Mismatch check

```python
# injaz_experiment/srm.py
"""Never analyse an experiment that fails SRM. A significant deviation
from the intended split signals a data/plumbing bug, not a real effect."""
from scipy.stats import chisquare

def srm_check(counts: dict[str, int], expected_split: dict[str, float],
              alpha: float = 0.001) -> dict:
    arms = list(counts)
    observed = [counts[a] for a in arms]
    total = sum(observed)
    expected = [expected_split[a] * total for a in arms]
    stat, p = chisquare(f_obs=observed, f_exp=expected)
    return {"chi2": round(stat, 3), "p_value": p,
            "srm_detected": p < alpha,
            "verdict": "INVALID - investigate plumbing" if p < alpha
                       else "ratios OK"}

print(srm_check({"control": 100_142, "treatment": 99_858},
                {"control": 0.5, "treatment": 0.5}))     # ratios OK
print(srm_check({"control": 102_500, "treatment": 97_500},
                {"control": 0.5, "treatment": 0.5}))     # SRM detected
```

### Covariate balance check

```python
# injaz_experiment/balance.py
"""After a single randomisation, verify (don't re-roll) balance on
pre-treatment covariates. Standardised mean difference (SMD) < 0.1 is the
common 'balanced' rule of thumb."""
import numpy as np
import pandas as pd

def standardised_mean_diff(df: pd.DataFrame, covariate: str,
                           variant_col: str = "variant") -> float:
    t = df.loc[df[variant_col] == "treatment", covariate]
    c = df.loc[df[variant_col] == "control", covariate]
    pooled_sd = np.sqrt((t.var(ddof=1) + c.var(ddof=1)) / 2)
    return (t.mean() - c.mean()) / pooled_sd if pooled_sd > 0 else 0.0

def balance_table(df: pd.DataFrame, covariates: list[str]) -> pd.DataFrame:
    rows = [{"covariate": cov,
             "smd": round(standardised_mean_diff(df, cov), 4),
             "balanced": abs(standardised_mean_diff(df, cov)) < 0.1}
            for cov in covariates]
    return pd.DataFrame(rows)
```

## Hands-on Lab 2 — Design and Randomise the Injaz Uploader Experiment

| | |
|---|---|
| **Objective** | Produce a complete experiment design doc for the guided-uploader test, randomise 200k users deterministically, and prove the assignment is valid (no SRM, balanced covariates) |
| **Duration** | 50 minutes |
| **Setup** | `lab2-start.ipynb`; `injaz_users.csv` (extended to 200k with region, device, prior_completions); `injaz_experiment/` starter package |

**Instructions & tasks**

1. *(10 min)* Fill the **design doc** template: hypothesis, randomisation unit (+ justification vs session), OEC, three guardrails, trigger definition, unit of analysis. Defend the user-level choice in two sentences.
2. *(8 min)* Implement `assign_variant` (hash-based) and assign the 200k users with `salt="injaz-uploader-2026q2"`.
3. *(7 min)* Run the SRM check; confirm it passes. Then deliberately break it (drop 3% of treatment rows) and confirm it fails — understand what a real bug looks like.
4. *(10 min)* Build the balance table over `age`, `digital_literacy`, `prior_completions`, `region` (one-hot). Confirm all SMD < 0.1.
5. *(8 min)* Interference audit: list two plausible SUTVA violations for this experiment and the design change each would require.
6. *(7 min)* Write the frozen "analysis plan" stub (metric, test, correction) to hand to Module 4 — pre-registration in miniature.

**Expected output**
```
SRM check (intended 50/50): p=0.71  -> ratios OK
Balance table: max |SMD| = 0.017 (all < 0.1)  -> balanced
Design doc: unit=user(nid_hash), OEC=completion_rate,
            guardrails=[time_to_complete, support_tickets, upload_errors]
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| SRM fails on clean data | Non-deterministic assignment (per-row random) | Use the hash; the same id must always map to the same arm |
| One covariate imbalanced | Genuine chance imbalance | Do NOT re-randomise; note it, plan covariate adjustment (Module 4) |
| Buckets not ~50/50 | Salt varies per call / id not stringified | Fix a single salt; cast id to `str` |
| "region" balance undefined | Categorical passed raw | One-hot encode before SMD |

**Instructor notes.** The re-randomisation temptation in step 4 is the teachable trap — someone will want to re-roll the imbalanced covariate. Stop the room and explain why that biases the design; the correct response is adjust-in-analysis, never re-roll. Fast finishers: implement a `trigger` filter and show how analysing only triggered users changes the effective sample size.

## Mini Exercises

**Quiz (5 questions)**
1. When should you randomise by user rather than session? → when users return and must see a consistent experience, or when sessions are not independent.
2. What is an OEC and how many should an experiment have? → the single decision metric; exactly one primary.
3. What does an SRM indicate and what should you do? → a likely plumbing bug; do not analyse until explained.
4. Name a SUTVA-violating scenario and its containment design. → shared devices / spillover → cluster or switchback randomisation.
5. Why hash instead of drawing a random number per request? → deterministic, stateless, reproducible; independent across experiments via salt.

**Debugging exercise.** Provide an assignment that re-seeds `np.random` inside a loop, so the same user gets different arms across calls; participants diagnose the non-determinism and the resulting SRM.

**Design critique.** Give three flawed one-line designs (session-level for a returning-user feature; 12 primary metrics; region-level with n=13 and a standard z-test). Each pair names the flaw and the fix.

**Discussion questions.**
- Your PM wants five "primary" metrics so "we learn more." What is the statistical cost and your counter-proposal?
- A marketplace-style feature can't be user-randomised safely. Walk through choosing between cluster and switchback designs.

## Case Study — The Marketplace Feature That Couldn't Be A/B Tested

**Scenario.** Injaz adds a "priority appointment" marketplace where a limited pool of in-person slots is allocated across citizens. A user-level A/B test of a new allocation algorithm shows treatment users book 15% faster.

**Business context.** The slot pool is fixed. If treatment users grab slots faster, they do so *at the expense of* control users in the same pool — classic interference. The 15% is partly cannibalisation, not net improvement.

**Technical challenge.** Design an evaluation that measures the true system-level effect without the two arms competing for the same finite resource.

**Constraints.** Only 13 administrative regions; slot pools are regional; a decision is needed for the next quarter's capacity plan.

**Solution approach (facilitate, don't lecture).** (1) Diagnose the interference: shared finite inventory means SUTVA fails at user level. (2) Move the unit up: region-level or switchback (alternate algorithm by week within region). (3) Confront the small-N problem: 13 regions → use switchback across many weeks for power, cluster-robust or randomisation-inference variance. (4) Define the true OEC as *system* fill rate and citizen wait time, not individual speed.

**Discussion questions.**
1. Why is the user-level 15% an overestimate of the system effect?
2. What are the power consequences of moving to region-level, and how does switchback recover some power?
3. What guardrail protects against a "faster for some, much slower for others" outcome? (wait-time distribution, not just the mean)
4. How would you explain to leadership that the honest, harder design gives a smaller but *real* number?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Randomisation determinism | Correctness | identical arm on 3 re-runs, 100% of users | re-run assignment |
| SRM false-alarm rate on clean data | Correctness | p > 0.01 on valid 50/50 | SRM check |
| SRM detection on injected bug | Correctness | flagged at 3% arm loss | injected-defect test |
| Max covariate SMD | Balance | < 0.1 on all covariates | balance table |
| Design-doc completeness | Rigor | all 6 fields present + justified | doc rubric |
| Interference risks identified | Reasoning | ≥ 2 with mitigations | audit exercise |

**Example benchmark table (filled during lab):**

| Check | Result | Verdict |
|---|---|---|
| SRM (intended 50/50) | p = 0.71 | ratios OK |
| Injected 3% arm loss | p = 3e-9 | SRM detected — invalid |
| Balance (max SMD) | 0.017 | balanced |

## Required Visuals and Training Assets

### Diagrams
1. **Experiment anatomy** — *Purpose:* shared vocabulary. *Elements:* labelled boxes for unit-of-randomisation, unit-of-analysis, OEC, guardrails, trigger, arms; arrows from user pool to arms to metric. *Style:* flat schematic, bilingual labels.
2. **Randomisation-unit decision tree** — *Purpose:* operationalise the choice. *Elements:* branches on "users return?", "units interfere?", "enough units for power?" leading to session/user/cluster/switchback. *Style:* decision flowchart.
3. **Interference / spillover illustration** — *Purpose:* make SUTVA concrete. *Elements:* two users on a shared household device, treatment leaking to control; a finite slot pool being cannibalised. *Style:* two-panel scenario art.
4. **SRM diagnostic** — *Purpose:* show what a broken experiment looks like. *Elements:* observed vs expected bar pairs, chi-square callout, red "INVALID" stamp. *Style:* before/after bars.

### Images (screenshots)
1. **Design-doc template filled**: *why:* the deliverable exemplar; *content:* the six fields completed for the uploader test.
2. **Balance table output**: *why:* expected reference; *content:* SMD column all green (< 0.1).
3. **SRM pass vs fail**: *why:* the go/no-go gate; *content:* two chi-square outputs side by side.

### Simulations
1. **Interference dial** — *Setup:* a spillover-strength parameter leaking treatment to control. *Expected behaviour:* as spillover rises, the naive user-level estimate diverges from the true system effect. *Learning objective:* interference biases estimates; containment design is not optional.
2. **SRM injector** — *Setup:* a toggle that drops a configurable fraction of one arm. *Expected behaviour:* SRM p-value collapses past a threshold. *Learning objective:* even small ratio drift is detectable and disqualifying.

### Interactive Activities
- **Pick-the-unit workshop (15 min):** six feature briefs; teams choose and defend a randomisation unit each.
- **Guardrail brainstorm (10 min):** for the uploader, teams propose guardrails, then debate which are true guardrails vs vanity secondaries.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_users.csv` (extended) | Course-generated | CSV | 200,000 rows × 11 cols | Assignment, SRM, balance |
| `injaz_sessions.csv` | Course-generated | CSV | ~600k rows | Trigger/exposure and unit-of-analysis illustration |

### Demo Requirements
- **Instructor demo:** hash-assign 200k users, pass SRM, then inject a 3% arm loss live and watch SRM flip to INVALID.
- **Student demo:** one pair presents its design doc and defends the randomisation unit against a planted "why not session?" challenge.
- **Expected outputs:** deterministic assignment, SRM pass on clean data, all covariate SMD < 0.1, a complete frozen design doc.

---

# Module 3 — Power Analysis and Sample Sizing

## الوحدة 3 — تحليل القوة الإحصائية وتحديد حجم العينة

## Module Overview

**Purpose.** An experiment that is too small cannot detect the effect it was built to find — it is expensive theatre that ends in an inconclusive shrug misread as "no effect." This module teaches participants to compute, *before launch*, how many units are needed to detect an effect worth caring about, and conversely what effect a fixed sample can detect. They master the four-way relationship between significance level, power, effect size, and sample size, and turn it into a concrete run-length plan for the Injaz experiment.

**Business relevance.** Power analysis is where statistics meets the calendar and the budget. "How long must we run?" is the first question every product and policy owner asks, and an experimentation lead who cannot answer it credibly loses the room. Under-powered experiments waste traffic and, worse, produce a stream of false negatives that teach the organisation that "experiments never find anything" — killing the experimentation culture SDAIA is trying to build. Over-powered experiments burn weeks detecting effects far smaller than anyone would act on.

**Industry use cases.**
- A government portal with modest daily traffic must know whether a 1-point completion lift is even detectable this quarter, or whether only a 3-point lift can be found in a reasonable window.
- An e-commerce team sizes a checkout experiment to detect a 0.5% conversion lift because that is the smallest change that pays for the engineering.
- A team uses variance reduction (CUPED) to cut required sample size by 40%, turning a 6-week test into a 4-week test — a direct schedule win.

**Expected competencies.** Participants can define and compute statistical power, minimum detectable effect (MDE), and required sample size for means and proportions; explain the four-way trade-off; convert sample size into run length given traffic; account for multiple arms and variance reduction; and produce a defensible pre-launch sizing plan.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Define Type I/II error, significance, and power precisely | LO2 |
| 3.2 | Compute required sample size for proportion and mean outcomes | LO2 |
| 3.3 | Compute the MDE for a fixed sample and traffic budget | LO2 |
| 3.4 | Convert sample size into a run-length plan accounting for arms | LO2, LO6 |
| 3.5 | Estimate the sample-size reduction from variance reduction (CUPED) | LO2, LO3 |

## Technical Content

### 1. The four quantities and their trade-off

Every power calculation ties four numbers together; fix any three and the fourth is determined:

- **α (significance level):** the false-positive rate — probability of declaring an effect when none exists (Type I error). Convention 0.05; tightened when many tests run (Module 4).
- **Power (1 − β):** the true-positive rate — probability of detecting an effect that truly exists. Convention 0.80; 0.90 for high-stakes decisions. β is the false-negative (Type II) rate.
- **Effect size / MDE:** the smallest effect worth detecting, in the metric's units (e.g., a 2-percentage-point lift in completion rate). This is a *business* decision, not a statistical one.
- **Sample size (n):** units per arm.

The intuition to install: **smaller effects, higher power, and tighter α all cost more sample.** Halving the MDE roughly *quadruples* the required sample (n scales with 1/MDE²). This quadratic is the single most important fact in the module — it explains why detecting tiny effects is so expensive and why picking an honest MDE matters more than any other design choice.

### 2. Type I, Type II, and the meaning of power

Draw the 2×2 truth table (effect exists? × we detected it?) and place α and β on it. Key clarifications the class always needs:

- **Power is a property of a *design against a specific effect size*,** not of a dataset. "Is this experiment powered?" is meaningless without "…to detect what effect?"
- A non-significant result from an under-powered test means "we couldn't see it," **not** "there is no effect." Absence of evidence ≠ evidence of absence. This is the most consequential misreading in applied experimentation and the reason the run-length plan is written in advance.
- Post-hoc "observed power" computed from the realised effect is statistically meaningless — teach participants never to compute it. Power is a pre-experiment quantity.

### 3. Sample size for proportions and means

For a two-sided test comparing two groups, the sample size per arm follows the standard normal-approximation formula. For **proportions** (like completion rate):

*n = (z_{1−α/2} + z_{1−β})² · [p₁(1−p₁) + p₂(1−p₂)] / (p₂ − p₁)²*

where *p₁* is the baseline rate, *p₂ = p₁ + MDE*, and the *z* values are standard-normal quantiles (≈1.96 for α=0.05 two-sided, ≈0.84 for 80% power). For **means**, replace the proportion variances with *2σ²* and the effect with the mean difference:

*n = 2σ² (z_{1−α/2} + z_{1−β})² / Δ²*

Teach both the closed form (for intuition and quick estimates) and the `statsmodels` implementation (for exactness, including small-sample and unequal-allocation cases). The closed form reveals the levers; the library removes arithmetic risk. Always cross-check one against the other in the lab.

### 4. From sample size to run length

Sample size is per arm; the calendar plan needs more:

- **Total units = n × (number of arms).** A 4-arm test needs four times the traffic of the per-arm figure — teams routinely forget this and under-run.
- **Run length = total units / (daily eligible traffic × trigger rate).** Only *triggered* users count; if half of visitors never reach the upload step, effective traffic halves.
- **Minimum duration floor:** run at least one to two full weeks regardless of what n suggests, to average over weekly seasonality (weekday/weekend, payday cycles, Ramadan effects). A test that hits n in three days on a Monday–Wednesday burst is confounded by day-of-week.
- **Novelty and primacy effects:** early days may show inflated or depressed effects as users react to change; the duration floor mitigates this too.

### 5. Variance reduction and MDE budgeting

Because n scales with variance, *reducing variance* is equivalent to buying sample size for free. The headline technique is **CUPED** (Controlled-experiment Using Pre-Existing Data): regress the outcome on a pre-experiment covariate (e.g., the user's pre-period completion rate) and analyse the residual. Because the covariate is measured *before* treatment it cannot be affected by it, so the adjustment is unbiased — and it can cut variance 30–50% when the covariate is predictive, shrinking required sample proportionally.

Teach MDE as a **budget conversation**: given the traffic available this quarter, what is the smallest effect we can detect at 80% power? If that MDE (say 2.5 points) is larger than any effect leadership would act on, the honest answer is "this experiment is not worth running as designed" — and CUPED, a longer window, or a bigger expected effect are the only fixes. Delivering that answer *before* launch is a senior skill.

### 6. Common mistakes & production considerations

1. Sizing to detect the *expected* effect instead of the *minimum worthwhile* effect — then being under-powered if reality is smaller.
2. Forgetting to multiply per-arm n by the number of arms.
3. Ignoring the trigger rate and over-counting available traffic.
4. Running until significant instead of to a pre-computed n (the peeking problem — Module 4).
5. Using observed post-hoc power to excuse a null result.
6. Sizing on a vanity metric with tiny variance while the real OEC needs far more sample.
7. Ignoring cluster/switchback designs' effective sample size — the design's variance inflation (design effect) must enter the calculation.

**Production considerations.** Mature platforms compute power at design time from historical metric variance, auto-estimate run length from live traffic forecasts, and refuse to launch experiments that cannot reach their MDE in the requested window. The sizing plan is part of the frozen design doc from Module 2.

## Code Examples

### Sample size and power from first principles + statsmodels cross-check

```python
# injaz_power/sizing.py
"""Power/sizing for a two-proportion completion-rate test.
Closed-form for intuition, statsmodels for exactness — cross-check both."""
import numpy as np
from scipy.stats import norm
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

def sample_size_proportions(p1: float, mde: float, alpha: float = 0.05,
                            power: float = 0.80) -> int:
    """Per-arm sample size to detect an absolute lift `mde` over baseline p1."""
    p2 = p1 + mde
    z_a = norm.ppf(1 - alpha / 2)         # two-sided
    z_b = norm.ppf(power)
    num = (z_a + z_b) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2))
    return int(np.ceil(num / (p2 - p1) ** 2))

# Injaz: baseline completion 0.55, want to detect a +2pp lift
n_closed = sample_size_proportions(0.55, 0.02)

# Cross-check with statsmodels (uses Cohen's h effect size)
h = proportion_effectsize(0.57, 0.55)
n_sm = NormalIndPower().solve_power(effect_size=h, alpha=0.05,
                                    power=0.80, alternative="two-sided")
print(f"Closed-form per arm : {n_closed:,}")
print(f"statsmodels per arm : {int(np.ceil(n_sm)):,}")   # agree within rounding
```

### MDE for a fixed sample, and the run-length plan

```python
# injaz_power/mde_and_runlength.py
"""Invert the relationship: given available traffic, what is the smallest
effect we can detect? Then turn total sample into calendar days."""
import numpy as np
from scipy.stats import norm

def mde_proportions(p1: float, n_per_arm: int, alpha: float = 0.05,
                    power: float = 0.80) -> float:
    """Approximate absolute MDE for a two-proportion test at fixed n."""
    z_a, z_b = norm.ppf(1 - alpha / 2), norm.ppf(power)
    se = np.sqrt(2 * p1 * (1 - p1) / n_per_arm)   # variance approx near p1
    return (z_a + z_b) * se

def run_length_days(n_per_arm: int, n_arms: int, daily_eligible: int,
                    trigger_rate: float, min_days: int = 14) -> int:
    total = n_per_arm * n_arms
    daily_triggered = daily_eligible * trigger_rate
    days = int(np.ceil(total / daily_triggered))
    return max(days, min_days)      # enforce the seasonality floor

p1 = 0.55
print(f"MDE at n=40k/arm : {mde_proportions(p1, 40_000):.4f}")   # ~0.0099
plan = run_length_days(n_per_arm=40_000, n_arms=2,
                       daily_eligible=12_000, trigger_rate=0.6)
print(f"Run length       : {plan} days")
```

### CUPED variance reduction and its sample-size payoff

```python
# injaz_power/cuped.py
"""CUPED: use a PRE-experiment covariate to shrink variance -> smaller n.
The covariate must be pre-treatment so it cannot be affected by the test."""
import numpy as np
import pandas as pd

def cuped_adjust(df: pd.DataFrame, metric: str, pre_metric: str) -> pd.Series:
    theta = df[pre_metric].cov(df[metric]) / df[pre_metric].var()
    return df[metric] - theta * (df[pre_metric] - df[pre_metric].mean())

def variance_reduction(df: pd.DataFrame, metric: str, pre_metric: str) -> float:
    adj = cuped_adjust(df, metric, pre_metric)
    return 1 - adj.var() / df[metric].var()      # fraction of variance removed

# Predictive pre-period covariate -> big reduction -> proportional n savings
rng = np.random.default_rng(3)
n = 50_000
pre = rng.normal(0.55, 0.15, n)
metric = 0.8 * pre + rng.normal(0, 0.08, n)      # correlated with pre-period
df = pd.DataFrame({"completion": metric, "pre_completion": pre})
vr = variance_reduction(df, "completion", "pre_completion")
print(f"Variance reduced by {vr:.1%}  -> required n multiplied by {1-vr:.2f}")
```

## Hands-on Lab 3 — Build the Sample-Size Calculator and Run-Length Plan

| | |
|---|---|
| **Objective** | Implement a reusable power/MDE/sizing toolkit and produce the Injaz uploader experiment's run-length plan, including a CUPED-adjusted plan |
| **Duration** | 50 minutes |
| **Setup** | `lab3-start.ipynb`; `injaz_power/` starter; historical `injaz_pre_period.csv` (per-user pre-period completion) |

**Instructions & tasks**

1. *(8 min)* Implement `sample_size_proportions` and cross-check against `statsmodels` for baseline 0.55 and MDE 0.02; the two must agree within rounding.
2. *(8 min)* Plot required per-arm n vs MDE for MDE ∈ [0.005, 0.05]; annotate the quadratic blow-up as MDE shrinks.
3. *(8 min)* Compute the MDE achievable at the platform's real traffic (12,000 eligible/day, 0.6 trigger, 4-week window); state whether a 2-point lift is detectable.
4. *(8 min)* Produce the run-length plan for 2 arms; then redo for 3 arms and note the traffic multiplier.
5. *(10 min)* Estimate CUPED variance reduction from `injaz_pre_period.csv`; recompute required n and the shortened run length.
6. *(8 min)* Write the one-paragraph sizing recommendation for the design doc: chosen MDE, n/arm, arms, run length, with and without CUPED.

**Expected output**
```
n per arm (p1=0.55, MDE=0.02, 80% power): 9,873   [statsmodels agrees]
MDE detectable in 4 weeks at live traffic: 0.0091  -> a 2pp lift IS detectable
Run length (2 arms): 14 days (floor)   (3 arms): 21 days
CUPED variance reduction: 42%  ->  n per arm falls to 5,726, run length 14 days
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Closed-form and statsmodels disagree a lot | Mixing absolute lift with Cohen's h | Feed statsmodels `proportion_effectsize(p2, p1)` |
| Run length looks impossibly short | Forgot trigger rate / arm multiplier | Multiply n by arms; apply trigger rate to traffic |
| CUPED reduction ≈ 0 | Pre-covariate not predictive | Check correlation; CUPED helps only with a correlated covariate |
| Negative or absurd n | MDE larger than plausible range | Validate `p2 = p1 + mde` stays in (0,1) |

**Instructor notes.** Step 2's plot is the keeper — pin it to the wall for the rest of the course; every "can we detect a smaller effect?" question gets answered by pointing at the quadratic curve. Fast finishers: add unequal allocation (e.g., 90/10) and show how it inflates required total sample.

## Mini Exercises

**Quiz (5 questions)**
1. Define statistical power. → probability of detecting a true effect of a given size; 1 − β.
2. If you halve the MDE, how does required n change? → roughly ×4 (n ∝ 1/MDE²).
3. Why is a non-significant result not proof of no effect? → the test may be under-powered; absence of evidence ≠ evidence of absence.
4. Why multiply per-arm n by the number of arms? → each arm needs the computed sample; total traffic scales with arms.
5. Why is CUPED's covariate required to be pre-treatment? → so it is unaffected by the treatment, keeping the adjustment unbiased.

**Debugging exercise.** A notebook sizes a 4-arm test but reports the 2-arm total; participants find the missing arm multiplier and the resulting under-run.

**Estimation exercise.** Given baseline 0.30 and a required MDE of 0.03 at 90% power, hand-estimate n with the closed form, then verify in code.

**Discussion questions.**
- Leadership wants to detect a 0.3-point lift on modest traffic in two weeks. Walk them through why that is infeasible and the three levers available.
- When is 90% power worth the extra sample over 80%? (irreversible or high-stakes decisions)

## Case Study — The Experiment That Ran Forever

**Scenario.** An Injaz team launched a homepage-copy experiment "to see if it helps" with no pre-computed sample size, checking results daily and planning to stop "when it's significant." Six weeks in, the p-value has crossed and re-crossed 0.05 four times and the team is exhausted and confused.

**Business context.** The true effect, it later emerges, is about 0.4 points — real but far below the ~2-point MDE the traffic could support in six weeks. The team was chasing an effect they were never powered to resolve.

**Technical challenge.** Retrofit a proper design: what MDE was ever detectable, what run length would a 0.4-point effect require, and why did daily peeking make everything worse (Module 4 preview)?

**Constraints.** Fixed modest traffic; leadership now skeptical of experimentation entirely.

**Solution approach (facilitate, don't lecture).** (1) Compute the detectable MDE for six weeks of this traffic — show 0.4 points was hopeless. (2) Compute the run length a 0.4-point effect would actually need (months) and conclude it is not worth chasing. (3) Diagnose the peeking: repeated looks inflate false positives, explaining the flickering significance. (4) Rebuild trust: pre-register MDE and run length; only run experiments whose worthwhile effect is detectable in budget.

**Discussion questions.**
1. What is the difference between "no effect" and "no *detectable* effect here"?
2. How did daily peeking manufacture the flickering significance?
3. What should the team have computed before launch, and what decision would it have driven?
4. How do you rebuild leadership's trust in experimentation after this?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Closed-form vs statsmodels n | Correctness | agree within 1% | cross-check |
| MDE ↔ n quadratic reproduced | Understanding | correct curve + annotation | sizing plot |
| Run-length plan correctness | Correctness | includes arms × trigger × floor | plan output |
| CUPED variance-reduction estimate | Correctness | matches within 2% of resample | resampling check |
| Feasibility call before launch | Judgement | correct go/no-go on a 2pp lift | recommendation cell |

**Example benchmark table (filled during lab):**

| Scenario | n/arm | Run length | Note |
|---|---|---|---|
| MDE 0.02, 2 arms, no CUPED | 9,873 | 14 days (floor) | detectable |
| MDE 0.01, 2 arms, no CUPED | 39,000 | 22 days | 4× the sample |
| MDE 0.02, 2 arms, CUPED 42% | 5,726 | 14 days (floor) | free time saving |

## Required Visuals and Training Assets

### Diagrams
1. **The four-way trade-off** — *Purpose:* anchor for the module. *Elements:* a dial/quadrant linking α, power, MDE, n, with arrows showing how tightening one demands more of another. *Style:* interlocking-gears metaphor, bilingual labels.
2. **Type I / Type II truth table** — *Purpose:* fix the vocabulary. *Elements:* 2×2 (effect exists? × detected?) with α, β, power placed in cells; two overlapping sampling distributions beneath. *Style:* classic power-curve figure.
3. **MDE-vs-n quadratic** — *Purpose:* the module's punchline. *Elements:* the sharply rising curve as MDE shrinks, with the 2× and 4× cost points marked. *Style:* annotated line chart.
4. **Run-length pipeline** — *Purpose:* connect stats to the calendar. *Elements:* n/arm → ×arms → ÷(traffic×trigger) → max(·, floor). *Style:* left-to-right flow.

### Images (screenshots)
1. **Sizing calculator output**: *why:* expected reference; *content:* closed-form and statsmodels agreeing.
2. **MDE-vs-n plot**: *why:* wall poster; *content:* quadratic with cost callouts.
3. **CUPED before/after variance**: *why:* motivates variance reduction; *content:* two histograms and the % reduction.

### Simulations
1. **Power curve explorer** — *Setup:* sliders for effect size and n. *Expected behaviour:* the detection-probability curve rises with both; a marker shows realised power. *Learning objective:* power is a design property against a specific effect.
2. **Underpowered null generator** — *Setup:* repeatedly run a true-effect experiment at low n. *Expected behaviour:* a majority of runs return non-significant despite the real effect. *Learning objective:* false negatives are the cost of under-powering.

### Interactive Activities
- **MDE-budget negotiation (15 min):** teams role-play data scientist vs product owner to agree an honest MDE against a fixed traffic budget.
- **Size-it race (10 min):** six scenario cards; teams compute n and run length, fastest correct wins.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_pre_period.csv` | Course-generated pre-experiment window | CSV | 50,000 rows | CUPED covariate + variance-reduction estimate |
| `injaz_traffic_forecast.csv` | Course-generated daily eligible traffic | CSV | 90 rows | Run-length planning |

### Demo Requirements
- **Instructor demo:** compute n for a 2-point lift, then live-halve the MDE and watch n quadruple; add CUPED and watch the run length drop.
- **Student demo:** one pair presents the go/no-go feasibility call for a sub-1-point lift on live traffic.
- **Expected outputs:** agreeing closed-form/statsmodels sizes, a defensible run-length plan, a quantified CUPED saving.

---

# Module 4 — Analysis Pitfalls: Peeking and Multiple Testing

## الوحدة 4 — مزالق التحليل: المراقبة المتكررة والاختبارات المتعددة

## Module Overview

**Purpose.** A correctly designed, well-powered experiment can still be ruined at the analysis stage. This module inventories the ways honest-looking analyses manufacture false positives — peeking and optional stopping, testing dozens of metrics and segments, mismatched units of analysis, and Simpson's paradox — and equips participants with the corrections: sequential-testing methods, multiple-comparison control, the delta method for ratio metrics, and covariate-adjusted variance estimation. The theme is discipline: the number you report must survive the ways experiments lie.

**Business relevance.** These pitfalls are not academic. Peeking is the default behaviour of every dashboard-watching stakeholder; segment-hunting ("it worked for users in Riyadh on Android!") is how noise gets promoted to strategy. In a government setting, a false-positive rollout wastes public money and, once discovered, damages the credibility of the whole data-science function. A specialist who can say "that segment result won't replicate, here's why" and "we can't stop early without inflating our error rate" protects the organisation from acting on artefacts.

**Industry use cases.**
- A team watching a live dashboard wants to stop the moment p < 0.05; without a sequential method, their true false-positive rate is closer to 25% than 5%.
- An analyst reports the one significant metric out of 30 without correction; it fails to replicate and erodes trust.
- A ratio metric (revenue per user, uploads per session) is analysed with a naive per-user test, understating variance because the analysis unit differs from the randomisation unit — fixed with the delta method.

**Expected competencies.** Participants can estimate treatment effects with correct (robust, clustered, or delta-method) variance; apply Bonferroni and Benjamini–Hochberg corrections; explain and mitigate the peeking problem with sequential or fixed-horizon discipline; detect and interpret Simpson's paradox; and distinguish statistical from practical significance in a decision.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Estimate effects and correct standard errors (robust/clustered/delta) | LO3 |
| 4.2 | Explain how peeking inflates Type I error and apply a valid stopping rule | LO3 |
| 4.3 | Apply Bonferroni and Benjamini–Hochberg multiple-testing corrections | LO3 |
| 4.4 | Detect Simpson's paradox and analyse at the correct level | LO3, LO5 |
| 4.5 | Distinguish statistical from practical significance for a decision | LO3, LO6 |

## Technical Content

### 1. The peeking problem (optional stopping)

A fixed-horizon test controls α only if you look **once**, at the pre-computed sample size. Every additional peek is another chance for noise to cross the threshold, so the *cumulative* false-positive rate compounds. Checking daily for two weeks and stopping at the first p < 0.05 pushes the true Type I rate from 5% toward 20–30%. The p-value from such a procedure is not a valid p-value — it answers a question ("was it ever significant?") different from the one reported ("is it significant?").

Three valid responses:

- **Fixed-horizon discipline:** compute n (Module 3), run to it, analyse once. Simple and correct; hard to enforce against anxious stakeholders.
- **Group-sequential methods** (O'Brien–Fleming, Pocock): pre-plan a small number of interim looks with spending-function-adjusted thresholds that keep overall α at 0.05.
- **Always-valid inference / sequential tests** (mixture sequential probability ratio tests, always-valid confidence sequences): give p-values and intervals valid *at every moment*, so continuous monitoring is legitimate. This is what modern experimentation platforms use.

Teach the instinct: **if you want to watch continuously, you must use a method built for continuous watching.** You cannot use fixed-horizon math and peek.

### 2. Correct variance estimation

The effect estimate is usually easy; the standard error is where analyses go wrong.

- **Regression for experiments:** analysing an A/B test as an OLS regression of outcome on the treatment indicator gives the same point estimate as a difference in means, but lets you add pre-treatment covariates (CUPED-style) to cut variance and use **heteroskedasticity-robust (HC) standard errors** by default.
- **Clustered standard errors:** when the randomisation unit is a cluster (region, household) but rows are sessions, ignoring clustering *understates* the SE and inflates false positives. Cluster-robust variance is mandatory for cluster/switchback designs (Module 2).
- **The unit-of-analysis trap:** randomising by user but computing a session-level metric means observations within a user are correlated; a naive test treats them as independent and lies about precision. Fix with clustering or by aggregating to the user.

### 3. The delta method for ratio metrics

Many OECs are **ratios where the denominator is itself random**: uploads per session, revenue per user, completion *rate* computed as completions/sessions when the unit is the user. The variance of a ratio is not the variance of the numerator; the **delta method** gives the correct asymptotic variance of *E[X]/E[Y]* by linearising around the means. Teaching this explicitly prevents a common, invisible error where ratio metrics get t-tested as if they were simple means, producing confidence intervals that are too narrow.

### 4. Multiple testing

If you run 20 independent tests at α=0.05 under the null, the chance of at least one false positive is *1 − 0.95²⁰ ≈ 64%*. Every extra metric, arm, and segment is another test. Two correction families:

- **Family-wise error rate (FWER)** control — **Bonferroni** (test each at α/m) and Holm (a uniformly more powerful step-down variant). Controls the probability of *any* false positive; conservative, appropriate when a single false positive is costly (e.g., a guardrail breach).
- **False discovery rate (FDR)** control — **Benjamini–Hochberg** — controls the *expected proportion* of false positives among discoveries; more powerful, appropriate for exploratory secondary/diagnostic metrics where some false positives are tolerable.

Rule of thumb to teach: **one pre-registered OEC needs no correction; the guardrail family uses FWER; the exploratory metric/segment sweep uses FDR** — and any "significant" segment from an unplanned sweep is a hypothesis to test next time, not a finding to ship.

### 5. Simpson's paradox and segmentation traps

Simpson's paradox: an effect that holds in every subgroup can reverse in the aggregate (or vice versa) when subgroup sizes and baseline rates differ. On Injaz it appears when treatment allocation correlates with a segment that has a very different baseline — e.g., treatment happened to reach more low-baseline regions, dragging its pooled rate down even though it helped within each region. In a *randomised* experiment large-sample balance makes this rare but not impossible (especially with SRM or post-randomisation filtering); in *observational* data it is endemic (Module 6). The defence: analyse at the randomisation level, pre-specify segments, and be suspicious of any aggregate that disagrees with consistent subgroup stories.

### 6. Common mistakes & production considerations

1. Stopping at the first significant peek with fixed-horizon math.
2. Reporting the best of many metrics/segments without correction, then over-generalising.
3. t-testing a ratio metric as a mean (missing the delta method).
4. Ignoring clustering when the analysis unit is finer than the randomisation unit.
5. Confusing statistical significance (p < 0.05) with practical significance (effect large enough to act on) — a tiny, useless effect can be highly significant at large n.
6. Post-hoc segment mining presented as if pre-planned (HARKing).
7. Dropping "outliers" or filtering post-randomisation in ways correlated with treatment — reintroduces bias and can trigger Simpson reversals.

**Production considerations.** Trustworthy platforms enforce a pre-registered analysis plan, apply always-valid inference for the live dashboard, auto-correct secondary metrics, flag SRM before results are shown, and report effect sizes with confidence intervals rather than bare p-values. The analysis plan frozen in Module 2 is what makes all of this auditable.

## Code Examples

### Peeking simulation — inflated false positives

```python
# injaz_analysis/peeking.py
"""Under the NULL (no real effect), stopping at the first significant peek
inflates the false-positive rate far above alpha. Prove it by simulation."""
import numpy as np
from scipy.stats import ttest_ind

rng = np.random.default_rng(4)

def false_positive_rate(n_looks: int, per_look: int = 500,
                        n_sims: int = 2000, alpha: float = 0.05) -> float:
    false_positives = 0
    for _ in range(n_sims):
        a, b = np.empty(0), np.empty(0)
        flagged = False
        for _ in range(n_looks):                       # peek repeatedly
            a = np.concatenate([a, rng.normal(0, 1, per_look)])
            b = np.concatenate([b, rng.normal(0, 1, per_look)])  # SAME dist
            if ttest_ind(a, b).pvalue < alpha:
                flagged = True
                break                                  # stop at first sig
        false_positives += flagged
    return false_positives / n_sims

for looks in (1, 5, 10, 20):
    print(f"{looks:2d} looks -> false-positive rate {false_positive_rate(looks):.1%}")
# 1 look -> ~5%   5 looks -> ~14%   10 looks -> ~19%   20 looks -> ~25%
```

### Effect estimation with robust and clustered SEs

```python
# injaz_analysis/estimate.py
"""Regression-based analysis of the uploader A/B test:
same point estimate as diff-in-means, but supports covariate adjustment
and robust/clustered standard errors."""
import statsmodels.formula.api as smf

def analyse_experiment(df):
    # HC3 robust SEs; 'variant' is 'treatment'/'control', completed is 0/1
    m_robust = smf.ols("completed ~ C(variant)", data=df).fit(cov_type="HC3")

    # CUPED-style covariate adjustment cuts variance (pre-treatment covariate)
    m_adj = smf.ols("completed ~ C(variant) + pre_completion_rate",
                    data=df).fit(cov_type="HC3")

    # Clustered SEs when analysis unit (session) is finer than randomisation (user)
    m_cluster = smf.ols("completed ~ C(variant)", data=df).fit(
        cov_type="cluster", cov_kwds={"groups": df["user_id"]})
    return m_robust, m_adj, m_cluster

# Report: coefficient on C(variant)[T.treatment] = lift; its CI decides ship/hold
```

### Delta method for a ratio metric

```python
# injaz_analysis/delta_method.py
"""Correct variance for a ratio metric (uploads per session) whose
denominator is random. A naive per-value t-test understates variance."""
import numpy as np

def ratio_delta(num: np.ndarray, den: np.ndarray) -> tuple[float, float]:
    """Return (ratio estimate, delta-method standard error)."""
    n = len(num)
    mx, my = num.mean(), den.mean()
    vx, vy = num.var(ddof=1), den.var(ddof=1)
    cov = np.cov(num, den, ddof=1)[0, 1]
    ratio = mx / my
    # Var(X/Y) ≈ (1/my^2)[ Var(X) - 2*(mx/my)*Cov + (mx/my)^2 Var(Y) ] / n
    var = (vx - 2 * (mx / my) * cov + (mx / my) ** 2 * vy) / (my ** 2 * n)
    return ratio, np.sqrt(var)
```

### Multiple-testing correction

```python
# injaz_analysis/multiple_testing.py
"""Bonferroni (FWER) for guardrails; Benjamini-Hochberg (FDR) for the
exploratory metric sweep. Never ship a raw-significant segment from a sweep."""
from statsmodels.stats.multitest import multipletests

def correct(pvalues: list[float], method: str = "fdr_bh"):
    reject, p_adj, _, _ = multipletests(pvalues, alpha=0.05, method=method)
    return list(zip(pvalues, [round(p, 4) for p in p_adj], reject))

secondary_ps = [0.001, 0.011, 0.020, 0.033, 0.041, 0.049, 0.20, 0.55]
print("Bonferroni :", correct(secondary_ps, "bonferroni"))
print("BH (FDR)   :", correct(secondary_ps, "fdr_bh"))
```

## Hands-on Lab 4 — Analyse the Uploader Experiment Correctly

| | |
|---|---|
| **Objective** | Take the Module 2 randomised uploader data to a defensible decision: correct point estimate and CI, CUPED-adjusted, guardrails checked with FWER control, and a peeking demonstration |
| **Duration** | 50 minutes |
| **Setup** | `lab4-start.ipynb`; `injaz_experiment_results.csv` (user_id, variant, completed, pre_completion_rate, time_to_complete, support_ticket, region) |

**Instructions & tasks**

1. *(8 min)* Estimate the completion-rate lift with a two-proportion test and with OLS + HC3; confirm identical point estimates and report the 95% CI.
2. *(8 min)* Add `pre_completion_rate` (CUPED-style); report the narrower CI and the effective variance reduction.
3. *(8 min)* Run the three guardrails (time-to-complete, support-ticket rate, upload-error rate) and apply Bonferroni across the guardrail family; state whether any regresses.
4. *(8 min)* Run a segment sweep across region and device (≈12 tests); apply Benjamini–Hochberg; identify which "significant" raw results survive and explain why the survivors are still only hypotheses.
5. *(10 min)* Reproduce the peeking simulation; report the false-positive rate at 1/5/10/20 looks and write the one-sentence rule it justifies.
6. *(8 min)* Write the decision paragraph: lift, CI, guardrail verdict, and an explicit statistical-vs-practical-significance statement (is the lift big enough to ship?).

**Expected output**
```
Completion lift: +0.021 (95% CI [0.008, 0.034]), p=0.0016  [two-prop == OLS]
CUPED-adjusted : +0.021 (95% CI [0.012, 0.030])  variance reduced 39%
Guardrails (Bonferroni m=3): time_to_complete OK, support_tickets OK, errors OK
Segment sweep (BH): 1 of 12 raw-significant survives -> flag as next-test hypothesis
Peeking: 1 look 5% ... 20 looks 25% -> "watch continuously => sequential method only"
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| OLS ≠ two-proportion estimate | Wrong reference level / weighting | Use `C(variant)` with control as reference; check coding of `completed` |
| CI wider after CUPED | Non-predictive covariate or leakage | Ensure covariate is pre-treatment and correlated |
| Every segment "significant" | No correction applied | Apply BH/Bonferroni; discuss the 64% family error |
| Guardrail flips significance across runs | Peeking / re-filtering | Analyse once at frozen n; no post-randomisation filtering |

**Instructor notes.** The highest-value moment is step 4: let a pair excitedly announce "it works great for Android users in Riyadh!" then apply BH and watch it evaporate. Fast finishers: implement an always-valid confidence sequence and show it stays valid under continuous peeking where the fixed-horizon CI does not.

## Mini Exercises

**Quiz (5 questions)**
1. Why does peeking inflate the false-positive rate? → each look is another chance to cross the threshold; errors compound above α.
2. When are clustered standard errors required? → when the analysis unit is finer than the (cluster) randomisation unit.
3. Bonferroni vs Benjamini–Hochberg — which controls what? → FWER (any false positive) vs FDR (expected proportion of false discoveries).
4. Why can a ratio metric not be t-tested as a mean? → its denominator is random; use the delta method for correct variance.
5. Statistical vs practical significance? → p < 0.05 says "detectable"; practical asks "large enough to act on" — large n can make trivial effects significant.

**Debugging exercise.** A notebook analyses a user-randomised test at the session level with a plain t-test; participants add clustering and watch the CI widen to the honest width.

**Correction exercise.** Given eight secondary p-values, apply Bonferroni and BH by hand and in code; explain which discoveries each method keeps and why.

**Discussion questions.**
- A stakeholder screenshots a p=0.03 on day 3 and wants to ship. What do you say, and what would let you legitimately act early?
- When is FDR the right choice over FWER, and vice versa, for the Injaz metric families?

## Case Study — The Segment That Vanished

**Scenario.** An Injaz analyst reports that a new reminder banner "significantly increased completion among first-time users on iOS in the Eastern Province" (p=0.02) and recommends targeting that segment. The banner's overall effect was flat.

**Business context.** The claim came from an unplanned sweep of 40 segment × metric combinations. Leadership is ready to build a targeting system around it.

**Technical challenge.** Show why this finding is almost certainly noise, quantify the expected number of false positives from 40 tests, and propose the correct way to treat segment discoveries.

**Constraints.** The sweep already happened; the overall OEC was flat; the analyst is confident and senior.

**Solution approach (facilitate, don't lecture).** (1) Compute the family error: 40 tests at 0.05 → ~87% chance of at least one false positive. (2) Apply BH to the 40 p-values; show the segment does not survive. (3) Reframe: an unplanned segment result is a *hypothesis*, testable only by a fresh, pre-registered experiment in that segment. (4) Distinguish this from a legitimate pre-registered heterogeneity analysis.

**Discussion questions.**
1. How many false positives do you expect from 40 tests at α=0.05 under the null?
2. Why is a fresh pre-registered test the only way to promote a swept segment to a finding?
3. How do you deliver this to a confident senior colleague without a turf war?
4. What platform control would have prevented the premature recommendation?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Point-estimate agreement (two-prop vs OLS) | Correctness | identical to 4 dp | side-by-side |
| Clustered/robust SE applied correctly | Correctness | CI widens to honest width | clustered vs naive |
| Peeking FPR reproduced | Understanding | ~25% at 20 looks | simulation |
| Correct correction family chosen | Judgement | FWER guardrails, FDR sweep | rubric |
| Decision paragraph quality | Communication | states CI + practical significance | memo review |

**Example benchmark table (filled during lab):**

| Analysis | Estimate | 95% CI | Verdict |
|---|---|---|---|
| Naive two-proportion | +0.021 | [0.008, 0.034] | significant |
| CUPED-adjusted (HC3) | +0.021 | [0.012, 0.030] | significant, tighter |
| Session-level, no clustering | +0.021 | [0.014, 0.028] | falsely narrow — wrong |
| Session-level, clustered | +0.021 | [0.007, 0.035] | honest width |

## Required Visuals and Training Assets

### Diagrams
1. **Peeking inflates error** — *Purpose:* the module's headline. *Elements:* a rising staircase of cumulative false-positive rate vs number of looks, from 5% to 25%. *Style:* annotated step chart.
2. **Correction-family decision** — *Purpose:* choose FWER vs FDR. *Elements:* branch on "single OEC? / guardrail family? / exploratory sweep?" → none/Bonferroni/BH. *Style:* decision flow.
3. **Unit-of-analysis mismatch** — *Purpose:* motivate clustering. *Elements:* a user with many correlated sessions counted as independent, with a "too-narrow CI" callout. *Style:* nested-boxes schematic.
4. **Simpson's paradox** — *Purpose:* make reversal visceral. *Elements:* subgroup lines all sloping up, pooled line sloping down, with segment sizes shown. *Style:* classic paradox plot.

### Images (screenshots)
1. **OLS-with-robust-SE output**: *why:* the canonical analysis; *content:* the treatment coefficient, CI, HC3 note.
2. **BH correction table**: *why:* shows discoveries surviving; *content:* raw vs adjusted p-values, reject flags.
3. **Peeking FPR table**: *why:* the punchline; *content:* 1/5/10/20 looks with rising FPR.

### Simulations
1. **Optional-stopping sandbox** — *Setup:* toggle fixed-horizon vs sequential thresholds while peeking. *Expected behaviour:* fixed-horizon peeking exceeds 5% error; the sequential method holds 5%. *Learning objective:* continuous monitoring requires always-valid inference.
2. **Simpson generator** — *Setup:* skew treatment allocation across segments with different baselines. *Expected behaviour:* aggregate effect reverses subgroup effects. *Learning objective:* analyse at the right level; beware post-randomisation imbalance.

### Interactive Activities
- **Stop-or-go role-play (15 min):** a live "dashboard" ticks; teams must decide when it is legitimate to stop and justify the method.
- **Correction relay (10 min):** teams correct a set of p-values with the right family and defend the choice.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_experiment_results.csv` | Course-generated randomised outcomes | CSV | 80,000 rows | Full analysis, guardrails, segments |
| `injaz_sessions.csv` | Course-generated session-level | CSV | ~600k rows | Unit-of-analysis / clustering demo |

### Demo Requirements
- **Instructor demo:** run the peeking simulation live to ~25% FPR, then analyse the uploader once, correctly, to a shippable CI.
- **Student demo:** one pair presents the segment-sweep correction and explains why a survivor is still just a hypothesis.
- **Expected outputs:** matching estimates across methods, honest (clustered/robust) CIs, correct correction families, a decision paragraph separating statistical and practical significance.

---

# Module 5 — Quasi-Experiments: Matching, Difference-in-Differences, and Instrumental Variables

## الوحدة 5 — التجارب شبه المضبوطة: المطابقة والفروق في الفروق والمتغيرات الأداتية

## Module Overview

**Purpose.** Randomisation is the gold standard, but the real world frequently forbids it: a policy is rolled out to everyone, a programme is opened to volunteers, a reminder campaign launches region by region for operational reasons. This module gives participants the three workhorse quasi-experimental methods — matching/weighting on observed confounders, difference-in-differences (DiD) using a policy rollout as a natural experiment, and instrumental variables (IV) to exploit as-good-as-random variation — together with the assumptions each requires and the sensitivity checks that keep them honest. This is the module that lets a data scientist say something causal when an A/B test is off the table.

**Business relevance.** Most consequential decisions in government cannot be A/B tested: you cannot randomise which citizens receive a national subsidy or which regions get a new service first. Quasi-experimental evaluation is therefore the difference between "we spent SAR 200M and have no idea if it worked" and "the reminder programme raised completion by 3.2 points, and here is the evidence and its caveats." These methods are the core of programme evaluation and the reason the module earns the "Causal badge" anchoring the Analytics & Experimentation specialisation.

**Industry use cases.**
- A government evaluates a region-by-region SMS reminder rollout with DiD, using not-yet-treated regions as controls.
- A workforce agency estimates the effect of a voluntary training programme with propensity-score matching on pre-programme characteristics (the Module 1 case study, now solved).
- An economist uses distance-to-service-centre as an instrument for in-person versus online filing to estimate the effect of channel on completion, breaking the self-selection of channel.

**Expected competencies.** Participants can estimate propensity scores, match or weight to balance observed confounders and estimate the ATT with sensitivity analysis; build a panel and estimate a DiD/event-study model while testing parallel trends; identify a valid instrument, state its assumptions, and estimate a 2SLS/LATE effect; and correctly state what each method does and does not identify.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Estimate propensity scores and use matching/weighting to estimate the ATT | LO4 |
| 5.2 | Assess covariate overlap/common support and post-matching balance | LO4 |
| 5.3 | Estimate a difference-in-differences effect and test parallel trends | LO4, LO5 |
| 5.4 | Identify a valid instrument and estimate a LATE via 2SLS | LO4, LO5 |
| 5.5 | Run sensitivity analyses for unobserved confounding | LO4, LO5, LO6 |

## Technical Content

### 1. The observational challenge and the identification mindset

When treatment is not randomised, the selection-bias term from Module 1 is back and non-zero. Quasi-experimental methods do not make bias vanish by magic; each **assumes** a specific structure that, if true, lets a valid comparison be constructed, and each is only as credible as that assumption. The professional habit to install: **state the identifying assumption first, in words, then estimate.** "Under the assumption that, conditional on age/region/prior-usage, programme uptake is as-good-as-random, the matched ATT is X." The assumption is the argument; the estimate is arithmetic.

### 2. Propensity scores, matching, and weighting

The **propensity score** *e(X) = P(T=1 | X)* is the probability of treatment given observed covariates. Rosenbaum and Rubin's result: if treatment is ignorable given *X*, it is also ignorable given the single scalar *e(X)* — so conditioning on the propensity score suffices to remove *observed* confounding. Estimation strategies:

- **Matching:** pair each treated unit with control unit(s) of similar propensity (nearest-neighbour, caliper); estimate the ATT as the mean within-pair outcome difference.
- **Inverse-probability weighting (IPW):** weight units by *1/e(X)* (treated) and *1/(1−e(X))* (control) to build a pseudo-population where treatment is independent of *X*.
- **Doubly-robust estimators** (AIPW): combine an outcome model and a propensity model; consistent if *either* is correct — the recommended default, available in EconML/DoWhy.

Two non-negotiable checks: **overlap / common support** (treated and control propensity distributions must overlap — no comparison exists in regions of no overlap) and **post-matching balance** (SMDs must shrink below 0.1, as in Module 2). Matching that does not achieve balance has not done its job.

**Critical caveat:** matching only adjusts for confounders you **observed**. It offers zero protection against unobserved confounding — unlike randomisation. Hence the mandatory sensitivity analysis in Section 5.

### 3. Difference-in-differences

DiD exploits a treatment that turns on for some units at a known time. It compares the **change** in the treated group's outcome (before → after) to the **change** in a control group's outcome over the same period, differencing out (a) fixed differences between groups and (b) common time trends:

*DiD = (Ȳ_treat,post − Ȳ_treat,pre) − (Ȳ_control,post − Ȳ_control,pre)*

Equivalently, a two-way fixed-effects (TWFE) regression with unit and time fixed effects and a treatment×post interaction whose coefficient is the DiD estimate. The **identifying assumption is parallel trends**: absent treatment, treated and control groups would have moved in parallel. It is not directly testable (the counterfactual is missing) but is *supported* by showing parallel **pre-trends** in an event-study plot. For the Injaz reminder rollout, regions activated in later waves serve as controls for earlier waves.

Teach the modern caveat: **staggered rollouts break naive TWFE.** When units are treated at different times, the TWFE estimator uses already-treated units as controls and can be badly biased (even wrong-signed) under heterogeneous effects. Name the fix — modern staggered-DiD estimators (Callaway–Sant'Anna, Sun–Abraham) — and use a clean two-period or not-yet-treated comparison in the lab to stay valid.

### 4. Instrumental variables

When an unobserved confounder contaminates treatment, an **instrument** *Z* can rescue identification if it satisfies three conditions:

1. **Relevance:** *Z* actually affects treatment *T* (testable — check the first-stage F-statistic; weak instruments, F < 10, are dangerous).
2. **Exclusion:** *Z* affects the outcome *only through* *T*, never directly.
3. **Independence / exogeneity:** *Z* is as-good-as-random with respect to the confounders.

Two-stage least squares (2SLS) then estimates the effect. The estimand is the **LATE** (Local Average Treatment Effect) — the effect *for compliers*, the units whose treatment status is moved by the instrument, not the whole population. This subtlety matters for interpretation and is a frequent exam point. Exclusion and independence are **assumptions, not testable**; the credibility of an IV analysis rests entirely on the argument for them. For Injaz, distance to the nearest in-person service centre can instrument for online-versus-in-person filing: it strongly affects channel choice (relevance) and plausibly affects completion only through channel (exclusion) — a claim to defend, not assume.

### 5. Sensitivity analysis and refutation

Because observational identification rests on untestable assumptions, credibility comes from **stress-testing**:

- **Rosenbaum bounds / sensitivity to hidden bias:** how strong would an unobserved confounder have to be to overturn the matched result? A result that flips under a weak confounder is fragile.
- **Placebo / negative-control outcomes:** apply the method to an outcome the treatment cannot affect; a non-zero "effect" reveals residual bias.
- **Placebo timing (DiD):** pretend treatment happened a year earlier; a significant pre-treatment "effect" falsifies parallel trends.
- **DoWhy refuters** (Module 6): random common cause, data subset, placebo treatment — automated robustness checks.

Teach the ethic: **an observational estimate without a sensitivity analysis is an opinion.** The sensitivity analysis is what makes it evidence.

### 6. Common mistakes & production considerations

1. Matching without checking overlap — extrapolating into regions with no comparable controls.
2. Declaring matching successful without a post-matching balance table.
3. Treating a matched/IV estimate as bias-free when only *observed* confounding is addressed.
4. Naive TWFE on a staggered rollout (the negative-weights trap).
5. Asserting parallel trends without an event-study pre-trend check.
6. Using a weak instrument (low first-stage F) and reporting a precise-looking but unreliable 2SLS estimate.
7. Interpreting LATE as ATE — generalising a compliers' effect to everyone.
8. Controlling for a post-treatment variable or a collider (Module 6), reintroducing bias.

**Production considerations.** Programme evaluations feed real budget decisions, so the analysis plan, assumption arguments, and sensitivity results are documented for audit. DoWhy's identify→estimate→refute workflow (Module 6) provides exactly this structure and is the recommended backbone for observational work in the capstone.

## Code Examples

### Propensity-score matching for the training programme (DoWhy/EconML-style + manual)

```python
# injaz_causal/matching.py
"""Estimate the ATT of the voluntary digital-literacy programme on
completion, adjusting for OBSERVED confounders via propensity matching."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

def estimate_propensity(df, covariates, treat="enrolled"):
    X, y = df[covariates].values, df[treat].values
    model = LogisticRegression(max_iter=1000).fit(X, y)
    return model.predict_proba(X)[:, 1]

def nn_match_att(df, outcome="completed", treat="enrolled", caliper=0.05):
    treated = df[df[treat] == 1]
    control = df[df[treat] == 0]
    nn = NearestNeighbors(n_neighbors=1).fit(control[["pscore"]].values)
    dist, idx = nn.kneighbors(treated[["pscore"]].values)
    keep = dist.ravel() <= caliper                      # enforce common support
    matched_control = control.iloc[idx.ravel()[keep]]
    att = (treated[outcome].values[keep] - matched_control[outcome].values).mean()
    return att, keep.mean()

cov = ["age", "digital_literacy", "prior_completions", "region_code"]
df = pd.read_csv("data/injaz_users.csv")
df["pscore"] = estimate_propensity(df, cov)
att, matched_frac = nn_match_att(df)
print(f"Matched ATT on completion: {att:+.4f}  (matched {matched_frac:.0%})")
```

### DoWhy identify → estimate → refute (the recommended backbone)

```python
# injaz_causal/dowhy_matching.py
"""DoWhy makes the assumptions explicit: build a causal model, IDENTIFY the
estimand from the graph, ESTIMATE it, then REFUTE it with robustness checks."""
from dowhy import CausalModel

model = CausalModel(
    data=df,
    treatment="enrolled",
    outcome="completed",
    common_causes=["age", "digital_literacy", "prior_completions", "region_code"],
)
estimand = model.identify_effect()
estimate = model.estimate_effect(
    estimand, method_name="backdoor.propensity_score_weighting")
print("ATT (IPW):", round(estimate.value, 4))

# Refutation: a valid estimate should be robust to these
for refuter in ["random_common_cause", "placebo_treatment_refuter",
                "data_subset_refuter"]:
    r = model.refute_estimate(estimand, estimate, method_name=refuter)
    print(refuter, "->", r)
```

### Difference-in-differences on the reminder rollout

```python
# injaz_causal/did.py
"""Two-way fixed-effects DiD on the region x month panel. Use a clean
not-yet-treated comparison to avoid staggered-TWFE bias."""
import statsmodels.formula.api as smf
import pandas as pd

panel = pd.read_csv("data/injaz_regions_panel.csv")   # region, month, completion_rate, treated_post
# treated_post = 1 for treated regions in months on/after their activation
did = smf.ols("completion_rate ~ treated_post + C(region) + C(month)",
              data=panel).fit(cov_type="cluster",
                              cov_kwds={"groups": panel["region"]})
print(f"DiD effect (reminder rollout): {did.params['treated_post']:+.4f}")
print(did.conf_int().loc["treated_post"].round(4).to_dict())
```

### Event study (parallel-trends check)

```python
# injaz_causal/event_study.py
"""Plot effects by months-relative-to-activation. Flat, ~zero pre-period
coefficients support parallel trends; a pre-trend falsifies DiD."""
import statsmodels.formula.api as smf

# 'rel' = months since activation (negative = pre); omit rel=-1 as baseline
es = smf.ols("completion_rate ~ C(rel, Treatment(reference=-1)) "
             "+ C(region) + C(month)", data=panel).fit(
             cov_type="cluster", cov_kwds={"groups": panel["region"]})
# extract C(rel)[...] coefficients and plot with CIs vs relative time
```

### Instrumental variables (2SLS)

```python
# injaz_causal/iv.py
"""Distance to the nearest service centre instruments for online-vs-in-person
filing. Check first-stage strength; interpret the estimate as a LATE."""
from linearmodels.iv import IV2SLS
import pandas as pd

d = pd.read_csv("data/injaz_users.csv")
# outcome=completed, endog=online_filing, instrument=distance_km, exog=controls
iv = IV2SLS.from_formula(
    "completed ~ 1 + age + prior_completions + [online_filing ~ distance_km]",
    data=d).fit(cov_type="robust")
print(iv.summary)
print("First-stage F (weak-instrument check):",
      iv.first_stage.diagnostics.loc["online_filing", "f.stat"])
```

## Hands-on Lab 5 — Quasi-Experimental Evaluation of Two Injaz Programmes

| | |
|---|---|
| **Objective** | Estimate the ATT of the voluntary training programme by matching (Lab 5a) and the effect of the regional reminder rollout by DiD (Lab 5b), with balance, parallel-trends, and sensitivity checks |
| **Duration** | 2 × 50 min (Day 3 H2 + H4) |
| **Setup** | `lab5-start.ipynb`; `injaz_users.csv`, `injaz_regions_panel.csv`; `dowhy`, `econml`, `linearmodels` installed |

**Part A — Matching (50 min)**
1. *(8 min)* Estimate propensity for programme enrolment on age, literacy, prior completions, region; plot treated/control propensity overlap and identify the common-support region.
2. *(10 min)* Nearest-neighbour match with a caliper; produce the post-matching balance table (all SMD < 0.1).
3. *(10 min)* Estimate the matched ATT; cross-check with DoWhy IPW; compare to the naive difference from the Module 1 case study.
4. *(12 min)* Run DoWhy refuters (random common cause, placebo treatment) and a sensitivity statement on unobserved confounding.
5. *(10 min)* Write the finding: "naive 22 points → matched ~X points," with the caveat about unobserved confounders.

**Part B — DiD (50 min)**
1. *(10 min)* Build/inspect the region×month panel; mark `treated_post` using activation waves.
2. *(12 min)* Estimate the TWFE DiD with region-clustered SEs; report the effect and CI.
3. *(12 min)* Estimate and plot the event study; assess whether pre-period coefficients are flat (parallel trends).
4. *(8 min)* Run a placebo-timing test (shift activation 6 months earlier); confirm the placebo effect is null.
5. *(8 min)* Write the finding with its identifying assumption and one threat to validity.

**Expected outputs**
```
Overlap: common support holds for pscore in [0.08, 0.92]; 6% of treated dropped
Matched ATT: +0.041 (naive was +0.22) -> selection bias explained most of the gap
DoWhy refuters: placebo effect ~0.00, random-common-cause stable -> robust
DiD reminder effect: +0.032 (95% CI [0.018, 0.046]), region-clustered
Event study: pre-period coeffs ~0 (parallel trends supported); placebo timing null
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Balance still poor after matching | Poor propensity model / no overlap | Add covariates or trim to common support; consider IPW |
| Matched ATT ≈ naive | Confounders omitted from pscore | Include the confounders that drive selection |
| DiD effect implausibly large | Staggered-TWFE negative weights | Use a not-yet-treated / two-period comparison |
| Non-flat pre-trends | Parallel trends violated | DiD not identified here; report the failure honestly |
| IV estimate wildly imprecise | Weak instrument (F < 10) | Report weakness; do not over-interpret 2SLS |

**Instructor notes.** Part A closes the loop on the Module 1 workshop case study — the same 22-point headline now resolves to a defensible ~4 points; make that connection explicit. Part B's event-study plot is the deliverable most likely to appear in the capstone; ensure every pair produces one. Fast finishers: estimate heterogeneous effects (CATE) with EconML's causal forest on the reminder data.

## Mini Exercises

**Quiz (5 questions)**
1. What does a propensity score reduce the conditioning set to? → a single scalar *e(X)*; conditioning on it removes observed confounding.
2. State the DiD identifying assumption. → parallel trends: absent treatment, groups would have moved in parallel.
3. Name the three IV conditions. → relevance, exclusion, independence/exogeneity.
4. What does IV/2SLS identify, and for whom? → the LATE — the effect for compliers.
5. Why is a sensitivity analysis mandatory for matching? → matching handles only observed confounders; sensitivity bounds the risk from unobserved ones.

**Debugging exercise.** A DiD notebook includes a post-treatment control that absorbs the effect; participants identify the bad control and remove it.

**Assumption-articulation exercise.** For each of three Injaz observational questions, write the identifying assumption in one sentence before any estimation.

**Discussion questions.**
- Your matched ATT is robust to refuters but a reviewer says "you didn't measure motivation." How do you respond with a Rosenbaum-bounds argument?
- When would you prefer IV over matching for a channel-choice question, and what makes distance a defensible instrument?

## Case Study — Did the Regional Reminder Programme Work?

**Scenario.** Injaz rolled out an SMS/push reminder programme to boost service completion, activating regions in three waves over six months for operational (not experimental) reasons. Leadership wants a credible national-impact estimate before extending it.

**Business context.** No randomisation was possible; a SAR 90M annual extension hinges on the estimate. A naive before/after comparison shows +6 points, but a national digital-adoption trend was rising anyway.

**Technical challenge.** Separate the reminder effect from the secular adoption trend using the staggered rollout as a natural experiment.

**Constraints.** Only 13 regions; staggered activation; a strong background trend; a decision due in a month.

**Solution approach (facilitate, don't lecture).** (1) Build the region×month panel. (2) Use not-yet-treated regions as controls to avoid staggered-TWFE bias. (3) Estimate DiD; the +6 naive shrinks to ~+3.2 once the common trend is differenced out. (4) Validate with an event study (flat pre-trends) and a placebo-timing test. (5) State the parallel-trends assumption and its one credible threat (a region-specific campaign coinciding with activation).

**Discussion questions.**
1. Why is the naive before/after +6 an overestimate here?
2. How does using not-yet-treated regions as controls protect the estimate?
3. What would a non-flat pre-trend tell you, and would you still report a number?
4. How do you communicate "+3.2 points, assuming parallel trends" to decision-makers honestly?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Post-matching balance | Correctness | all SMD < 0.1 | balance table |
| Common support enforced | Rigor | out-of-support units trimmed | overlap plot |
| Matched ATT vs naive gap explained | Understanding | selection bias quantified | comparison |
| DiD effect + parallel-trends check | Correctness | flat pre-trends, clustered CI | event study |
| Refutation/sensitivity run | Rigor | ≥ 2 refuters + a sensitivity statement | DoWhy output |
| First-stage strength (IV) | Correctness | F reported, weakness flagged | 2SLS diagnostics |

**Example benchmark table (filled during lab):**

| Method | Estimate | Assumption | Robustness |
|---|---|---|---|
| Naive difference | +0.220 | none (invalid) | — |
| Propensity matching (ATT) | +0.041 | ignorability on observed X | refuters pass |
| DiD (reminder) | +0.032 | parallel trends | pre-trends flat, placebo null |
| IV / 2SLS (channel) | +0.058 (LATE) | relevance+exclusion+exogeneity | first-stage F = 34 |

## Required Visuals and Training Assets

### Diagrams
1. **Ladder of evidence** — *Purpose:* place methods by credibility. *Elements:* rungs from naive comparison → matching → DiD → IV → RCT, with the assumption each buys. *Style:* vertical ladder, bilingual.
2. **Propensity overlap / common support** — *Purpose:* the go/no-go for matching. *Elements:* treated vs control propensity densities with the overlap region shaded and non-overlap trimmed. *Style:* overlapping density plot.
3. **DiD two-lines figure** — *Purpose:* the core intuition. *Elements:* treated and control outcome lines pre/post, the counterfactual dashed line, the DiD gap arrow. *Style:* classic DiD schematic.
4. **IV as a valve** — *Purpose:* explain exclusion. *Elements:* instrument → treatment → outcome, with a blocked direct instrument→outcome arrow and a confounder the instrument bypasses. *Style:* small DAG.

### Images (screenshots)
1. **Post-matching balance table**: *why:* proves matching worked; *content:* SMD before/after all below 0.1.
2. **Event-study plot**: *why:* the DiD credibility exhibit; *content:* flat pre-period, jump at activation, CIs.
3. **DoWhy refutation output**: *why:* robustness evidence; *content:* placebo ~0, stable under random common cause.

### Simulations
1. **Unobserved-confounder injector** — *Setup:* add a hidden confounder of known strength to the matching data. *Expected behaviour:* matched ATT shifts; Rosenbaum bounds show how strong the confounder must be to flip the sign. *Learning objective:* matching's blind spot is unobserved confounding.
2. **Parallel-trends breaker** — *Setup:* give treated regions a divergent pre-trend. *Expected behaviour:* the event study shows a pre-trend and DiD is biased. *Learning objective:* DiD is only as good as parallel trends.

### Interactive Activities
- **Assumption courtroom (15 min):** one team estimates, another cross-examines the identifying assumption; the class rules credible/not.
- **Instrument brainstorm (10 min):** teams propose instruments for three Injaz decisions and test each against the three conditions.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_users.csv` | Course-generated with enrolment + distance | CSV | 20,000 rows | Matching, IV |
| `injaz_regions_panel.csv` | Course-generated region×month panel with staggered activation | CSV | 13 regions × 24 months | DiD, event study |

### Demo Requirements
- **Instructor demo:** collapse the Module 1 case-study's 22-point headline to a matched ~4 points live, then run DoWhy refuters.
- **Student demo:** one pair presents its event-study plot and defends the parallel-trends assumption against a challenge.
- **Expected outputs:** balanced matches on common support, a robust matched ATT, a DiD estimate with a supportive event study, and an IV estimate with a reported first-stage F.

---

# Module 6 — Causal Graphs and Confounding

## الوحدة 6 — الرسوم البيانية السببية والمُربِكات

## Module Overview

**Purpose.** Every method in Modules 5 chose *what to adjust for* — but on what basis? This module supplies the missing theory: causal graphs (directed acyclic graphs, DAGs) that encode assumptions about how variables cause one another, and the rules (d-separation, the backdoor and frontdoor criteria) that mechanically determine which variables to control for, which to leave alone, and when an effect is identifiable at all. The module's most important and counter-intuitive lesson is that **controlling for the wrong variable creates bias** — colliders and mediators are traps that a graph makes visible and that regression-by-reflex hides.

**Business relevance.** "Just throw everything into the regression" is the most common and most dangerous analytical instinct in industry. It silently opens collider paths and blocks mediation, producing confidently wrong numbers that drive real decisions. A data scientist who can draw the DAG, defend the adjustment set, and refuse to control for a collider is worth a team of people running kitchen-sink regressions. In government evaluation, where a wrong number can misdirect national policy, the discipline of graph-based identification is a governance asset, not an academic nicety.

**Industry use cases.**
- An analyst almost "controls for" the number of support calls when estimating the uploader's effect — a mediator on the causal path — which would erase the very effect being measured.
- A study of a hiring programme conditions on being hired (a collider), manufacturing a spurious negative correlation between two independent traits.
- A team uses a DAG to prove that, given the measured covariates, the reminder effect is identifiable by the backdoor criterion — and to show which single unmeasured variable would break it.

**Expected competencies.** Participants can build a DAG for a decision, read confounders, mediators, and colliders off it, apply the backdoor criterion to choose a valid adjustment set, recognise when identification fails, and run the full DoWhy identify→estimate→refute workflow with a defensible graph.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Build a DAG encoding causal assumptions for a decision | LO5 |
| 6.2 | Classify variables as confounders, mediators, or colliders | LO5 |
| 6.3 | Apply the backdoor criterion to select a valid adjustment set | LO5 |
| 6.4 | Explain why conditioning on a collider or mediator induces bias | LO5 |
| 6.5 | Run identify→estimate→refute in DoWhy on a defended graph | LO5, LO6 |

## Technical Content

### 1. Why graphs: assumptions you can see and argue

A DAG is a picture of causal assumptions: nodes are variables, arrows are direct causal effects, and the *absence* of an arrow is itself a strong claim ("X does not directly cause Y"). The power of the DAG is that it makes assumptions **explicit, communicable, and falsifiable in part** — a stakeholder can look at your graph and say "but marketing also drives both," adding an arrow that changes the whole analysis. Compare this to a regression specification, where the same assumptions are buried in the choice of which columns were included. Graphs move the causal argument out of the code and onto the whiteboard where it can be debated by domain experts.

### 2. The three elementary structures

Every path in a DAG is built from three junctions, and their behaviour under conditioning is the crux of the module:

| Structure | Shape | Path is open... | Conditioning on the middle node... |
|---|---|---|---|
| **Chain (mediator)** | X → M → Y | when M is *not* conditioned | **blocks** the path (removes the mediated effect) |
| **Fork (confounder)** | X ← C → Y | when C is *not* conditioned | **blocks** the spurious association (this is what you want) |
| **Collider** | X → K ← Y | **only when K is conditioned** | **opens** a spurious path (this is the trap) |

Two rules to memorise: **control confounders (forks); never control colliders or mediators** (unless you specifically want the direct effect, in which case a mediator is blocked deliberately and carefully). The collider rule is the counter-intuitive one — conditioning on a common *effect* of two variables makes them spuriously dependent, the mechanism behind selection bias, Berkson's paradox, and "controlling for too much."

### 3. d-separation and the backdoor criterion

**d-separation** is the graphical test for whether two variables are independent given a conditioning set: a path is blocked if it contains an uncontrolled fork/chain or a collider (whose descendants are also uncontrolled). Two variables are d-separated (independent) if *every* path between them is blocked.

The **backdoor criterion** operationalises confounding control: to identify the causal effect of *T* on *Y*, choose an adjustment set *S* that (a) blocks every "backdoor" path from *T* to *Y* (paths starting with an arrow *into* T), and (b) contains no descendant of *T* (no mediators/colliders on the causal path). Adjusting for such an *S* yields an unbiased effect. This is the theory that justified the covariate choices in Module 5's matching — the propensity model should include exactly a valid backdoor set, no more, no less. When a valid backdoor set exists among *measured* variables, the effect is identifiable; when the only sets that would close the backdoors include unmeasured variables, it is not (and you need IV, frontdoor, or an experiment).

### 4. The frontdoor criterion and other identification routes

When an unmeasured confounder blocks the backdoor, the effect can sometimes still be identified via the **frontdoor criterion**: if a fully-mediating variable *M* sits on the path *T → M → Y*, *M* is unaffected by the confounder, and no unblocked backdoor from *M* to *Y* exists, then chaining *T→M* and *M→Y* recovers the effect. It is rare in practice but conceptually vital: it shows identification is a property of the *graph*, not of which method you like. Mention instrumental variables (Module 5) as another graph-justified route — an instrument is a node with an arrow into *T*, no arrow into *Y* except through *T*, and no shared confounder with *Y*. The DAG unifies all of Module 5 under one framework.

### 5. When identification fails (and honesty about it)

Sometimes no measured adjustment set identifies the effect — the graph simply does not permit it with the data at hand. The professional response is not to run a regression anyway and hope; it is to **say so**, and to specify what would be needed (a measured confounder, an instrument, an experiment). Teach participants to produce, for any observational question, one of three verdicts: *identifiable by backdoor set S*, *identifiable by another route (frontdoor/IV)*, or *not identifiable with current data — here is what's missing*. This honesty is exactly the "communicate uncertainty to decision-makers" outcome (LO6) and is what separates a trusted advisor from a p-value vendor.

### 6. Common mistakes & production considerations

1. Kitchen-sink regression — adding every available variable, opening collider paths and blocking mediators.
2. Controlling for a mediator and reporting the shrunken direct effect as "the effect."
3. Conditioning on a collider (often via sample selection — analysing only "completed" sessions), inducing bias.
4. Drawing a DAG to rationalise a chosen adjustment set rather than to derive it (the graph must precede the model).
5. Treating an unfalsifiable DAG as fact — the graph encodes assumptions and must be defended and stress-tested.
6. Ignoring selection into the sample as a form of collider conditioning.
7. Believing more controls always reduce bias — they can increase it.

**Production considerations.** DoWhy institutionalises the correct workflow: declare the graph, **identify** the estimand from it (which surfaces the required adjustment set), **estimate**, then **refute**. This makes the causal assumptions a reviewable artefact — the graph and refutation report ship with the analysis. In the capstone, every observational claim is expected to carry its DAG and identification verdict.

## Code Examples

### Building and querying a DAG for the uploader question

```python
# injaz_causal/dag.py
"""Encode the causal assumptions as a DAG and let the graph tell us what to
control for — instead of guessing. digital_literacy confounds; support_calls
is a MEDIATOR (do not control); device is a confounder we can measure."""
import networkx as nx

edges = [
    ("digital_literacy", "uploader_adoption"),  # confounder -> treatment
    ("digital_literacy", "completed"),          # confounder -> outcome
    ("device_age", "uploader_adoption"),
    ("device_age", "completed"),
    ("uploader_adoption", "support_calls"),     # treatment -> mediator
    ("support_calls", "completed"),             # mediator -> outcome
    ("uploader_adoption", "completed"),         # direct causal effect (target)
]
G = nx.DiGraph(edges)

def backdoor_paths(G, t, y):
    """Naive listing: paths from T to Y that start with an arrow INTO T."""
    UG = G.to_undirected()
    paths = [p for p in nx.all_simple_paths(UG, t, y)
             if len(p) > 1 and G.has_edge(p[1], t)]   # first hop points into T
    return paths

print("Backdoor paths (must be blocked):", backdoor_paths(G, "uploader_adoption",
                                                          "completed"))
# -> paths through digital_literacy and device_age  => adjust for BOTH
# NOTE: support_calls is a MEDIATOR (descendant of T) -> never in the adj. set
```

### The collider trap, demonstrated

```python
# injaz_causal/collider.py
"""Two INDEPENDENT causes of a collider become spuriously correlated once you
condition on the collider. This is why 'controlling for everything' backfires."""
import numpy as np
rng = np.random.default_rng(6)

n = 50_000
skill = rng.normal(0, 1, n)           # independent trait A
effort = rng.normal(0, 1, n)          # independent trait B  (corr with skill ~0)
completed = ((skill + effort + rng.normal(0, 0.5, n)) > 1.0)  # collider K

print("Corr(skill, effort) unconditional :",
      round(np.corrcoef(skill, effort)[0, 1], 3))          # ~0.00
print("Corr(skill, effort | completed=1) :",
      round(np.corrcoef(skill[completed], effort[completed])[0, 1], 3))  # negative!
# Conditioning on the collider 'completed' manufactures a spurious negative corr.
```

### Full DoWhy workflow with the defended graph

```python
# injaz_causal/dowhy_dag.py
"""identify -> estimate -> refute, driven by an explicit graph. DoWhy reads
the DAG, refuses the mediator, and returns the backdoor-adjusted effect."""
from dowhy import CausalModel

gml = """graph [directed 1
  node [id "digital_literacy" label "digital_literacy"]
  node [id "device_age" label "device_age"]
  node [id "uploader_adoption" label "uploader_adoption"]
  node [id "support_calls" label "support_calls"]
  node [id "completed" label "completed"]
  edge [source "digital_literacy" target "uploader_adoption"]
  edge [source "digital_literacy" target "completed"]
  edge [source "device_age" target "uploader_adoption"]
  edge [source "device_age" target "completed"]
  edge [source "uploader_adoption" target "support_calls"]
  edge [source "support_calls" target "completed"]
  edge [source "uploader_adoption" target "completed"] ]"""

model = CausalModel(data=df, treatment="uploader_adoption",
                    outcome="completed", graph=gml)
estimand = model.identify_effect()          # surfaces the backdoor adjustment set
print(estimand)                             # note: support_calls NOT included
estimate = model.estimate_effect(estimand,
              method_name="backdoor.linear_regression")
refute = model.refute_estimate(estimand, estimate,
              method_name="placebo_treatment_refuter")
print("Effect:", round(estimate.value, 4), "| placebo:", refute)
```

## Hands-on Lab 6 — DAGs, Colliders, and Defensible Identification

| | |
|---|---|
| **Objective** | Build and defend a DAG for an Injaz observational question, derive the adjustment set with the backdoor criterion, demonstrate the collider trap, and run the DoWhy identify→estimate→refute workflow |
| **Duration** | 50 minutes |
| **Setup** | `lab6-start.ipynb`; `networkx`, `dowhy` installed; `injaz_users.csv` with `support_calls`, `device_age` |

**Instructions & tasks**

1. *(8 min)* Draw the DAG for "effect of uploader adoption on completion," including `digital_literacy`, `device_age`, and the mediator `support_calls`; justify each arrow in one line.
2. *(8 min)* By hand, list the backdoor paths and derive the valid adjustment set; state explicitly why `support_calls` is excluded.
3. *(10 min)* Reproduce the collider simulation; show two independent traits become correlated after conditioning on a common effect; write the one-sentence lesson.
4. *(10 min)* Run the DoWhy workflow with your graph; confirm the identified estimand adjusts for the confounders and not the mediator; report the effect.
5. *(8 min)* Deliberately add `support_calls` to the adjustment set and show the effect estimate shrinks — the mediator trap, made real.
6. *(6 min)* Write the identification verdict: identifiable by backdoor set {digital_literacy, device_age}, plus the one unmeasured variable that would break it.

**Expected output**
```
Backdoor set: {digital_literacy, device_age}  (support_calls excluded: mediator)
Collider demo: corr 0.00 unconditional -> -0.31 conditional on completed
DoWhy effect (correct adj set): +0.020
Effect controlling for mediator (WRONG): +0.006  <- mediated effect erased
Verdict: identifiable via backdoor; an unmeasured 'prior_trust' would break it
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| DoWhy adjusts for the mediator | Mediator drawn as a confounder | Fix the arrow direction: T → M, not M → T |
| Collider corr stays ~0 | Not conditioning on the collider | Subset on `completed == 1` before computing corr |
| Effect unchanged with/without mediator | Weak mediation in the data | Check the T→M and M→Y edge strengths |
| Estimand "not identifiable" | Backdoor open via an unmeasured node | Report honestly; state what to measure |

**Instructor notes.** Step 5 is the emotional payoff — watching the effect they measured all week evaporate when they "helpfully" add a control drives the lesson home permanently. Fast finishers: draw the DAG for the Module 5 IV analysis and show why distance qualifies as an instrument graphically.

## Mini Exercises

**Quiz (5 questions)**
1. What does an *absent* arrow in a DAG assert? → that there is no direct causal effect between those variables.
2. What happens when you condition on a collider? → a spurious association opens between its causes (bias).
3. State the backdoor criterion in one sentence. → adjust for a set that blocks all backdoor paths and contains no descendant of the treatment.
4. Why should you not control for a mediator when estimating a total effect? → it blocks part of the causal path, shrinking the effect.
5. What are the three identification verdicts a professional gives? → identifiable by backdoor set S; identifiable by another route (frontdoor/IV); not identifiable with current data.

**Debugging exercise.** Given a "kitchen-sink" regression that controls for a collider and a mediator, participants use the DAG to remove both and recover the correct effect.

**DAG-drawing exercise.** For an Injaz observational question, each pair draws a DAG and derives the adjustment set, then swaps with another pair to critique the assumptions.

**Discussion questions.**
- A colleague says "more controls always reduce bias." Refute with a collider example.
- When is deliberately controlling for a mediator the *right* thing to do? (estimating a direct/controlled effect, done carefully)

## Case Study — The Control That Erased the Effect

**Scenario.** An Injaz analyst estimating the uploader's effect on completion "improved" the model by controlling for the number of support calls, since "support calls obviously matter for completion." The measured effect dropped from +2 points to near zero, and the team nearly killed the feature.

**Business context.** Support calls are a *consequence* of using the (initially confusing) uploader and a channel through which some users still complete — a mediator on the causal path. Controlling for it removed the part of the effect that flows through support and understated the true impact.

**Technical challenge.** Diagnose the mediator error with a DAG, recover the correct total effect, and articulate when (if ever) controlling for support calls is legitimate.

**Constraints.** The team trusts "more controls = more rigour"; a ship/kill decision is imminent.

**Solution approach (facilitate, don't lecture).** (1) Draw the DAG: uploader → support_calls → completed, plus the direct uploader → completed. (2) Show support_calls is a descendant of treatment — excluded by the backdoor criterion. (3) Re-estimate without it; recover +2 points. (4) Explain that controlling for it answers a *different* question (the direct effect not via support), which is not what "does the feature help?" means.

**Discussion questions.**
1. Why did adding a "sensible" control erase the effect?
2. What question does the mediator-controlled estimate actually answer?
3. How would you explain total vs direct effect to a product owner in one minute?
4. What review step would have caught this before the near-kill decision?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Correct adjustment set derived | Correctness | matches backdoor set; mediator excluded | hand derivation + DoWhy |
| Collider bias reproduced | Understanding | spurious corr appears on conditioning | simulation |
| Mediator trap demonstrated | Understanding | effect shrinks when mediator added | before/after estimate |
| Identification verdict stated | Judgement | one of the three verdicts, justified | verdict cell |
| DoWhy workflow completed | Rigor | identify→estimate→refute with graph | notebook output |

**Example benchmark table (filled during lab):**

| Adjustment set | Effect estimate | Correct? |
|---|---|---|
| {} (no controls) | +0.045 | biased (confounded) |
| {digital_literacy, device_age} | +0.020 | correct (backdoor set) |
| {digital_literacy, device_age, support_calls} | +0.006 | wrong (mediator controlled) |
| {digital_literacy, device_age, completed_flag} | biased | wrong (collider/selection) |

## Required Visuals and Training Assets

### Diagrams
1. **The three junctions** — *Purpose:* the module's core reference. *Elements:* chain, fork, collider side by side with the "open/blocked under conditioning" rule under each. *Style:* three-panel DAG card, bilingual.
2. **Backdoor criterion on the Injaz DAG** — *Purpose:* derive the adjustment set visually. *Elements:* the uploader DAG with backdoor paths highlighted and the valid adjustment set circled; the mediator crossed out. *Style:* annotated DAG.
3. **Collider / selection bias** — *Purpose:* make the trap intuitive. *Elements:* two independent causes → a collider, with a "condition here → spurious link" callout; a sample-selection version. *Style:* before/after correlation scatter.
4. **Identification verdict flow** — *Purpose:* the professional decision. *Elements:* branch to backdoor-set / frontdoor-IV / not-identifiable-here. *Style:* decision flow.

### Images (screenshots)
1. **DoWhy identified estimand**: *why:* shows the derived adjustment set; *content:* the estimand text excluding the mediator.
2. **Collider scatter**: *why:* the counter-intuitive result; *content:* zero unconditional correlation, negative conditional correlation.
3. **Mediator before/after**: *why:* the case-study exhibit; *content:* effect +0.020 vs +0.006 with the mediator controlled.

### Simulations
1. **Adjustment-set explorer** — *Setup:* toggle variables in/out of the control set. *Expected behaviour:* the estimate is correct only for valid backdoor sets; adding colliders/mediators biases it. *Learning objective:* more controls is not more rigour.
2. **Selection-as-collider** — *Setup:* analyse only a selected subsample (e.g., completed sessions). *Expected behaviour:* a spurious association appears. *Learning objective:* sample selection is collider conditioning.

### Interactive Activities
- **Draw-the-DAG relay (15 min):** teams build DAGs for four Injaz questions and derive adjustment sets; peers critique the assumptions.
- **Spot-the-collider (10 min):** a set of variable triples; teams label each fork/chain/collider and state the control rule.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_users.csv` (with support_calls, device_age) | Course-generated | CSV | 20,000 rows | Backdoor derivation, mediator trap |
| `collider_sim.parquet` | Simulator with two independent traits + collider | Parquet | 50,000 rows | Collider demonstration |

### Demo Requirements
- **Instructor demo:** derive the adjustment set from the DAG, then show live how adding the mediator erases the effect.
- **Student demo:** one pair presents its DAG, adjustment set, and identification verdict for an observational question.
- **Expected outputs:** a defended DAG, the correct backdoor adjustment set, a reproduced collider bias, and a clear identification verdict.

---

# Module 7 — Experimentation Case Study

## الوحدة 7 — دراسة حالة تطبيقية في التجريب

## Module Overview

**Purpose.** The previous six modules taught individual instruments; this module teaches the *judgement* to conduct a full experimentation engagement end to end, choosing the right method for a messy real question and carrying it from design through decision. Using one integrative Injaz question, participants move through method selection, design, powering, analysis, causal robustness, and — the part that actually changes the world — communicating the result and its uncertainty to a decision-maker. It is the bridge from technique to trusted advice and the direct rehearsal for the capstone.

**Business relevance.** Real decisions rarely arrive labelled "use DiD." They arrive as "should we roll the AI-assisted form-autofill out nationally, and did last quarter's reminder pilot justify its cost?" — a blend of a feature to be A/B tested and a pilot to be evaluated observationally, on a deadline, for an audience that thinks in riyals and risk, not p-values. The specialist's value is choosing well, executing correctly, and translating the evidence into a defensible recommendation. This module is where all six skills become one professional capability.

**Industry use cases.**
- A product team must decide, in one engagement, whether to ship a new feature (randomised test) and how to interpret a past pilot that was never randomised (quasi-experiment) — and reconcile the two.
- An evaluation unit must present a nationwide programme's impact to leadership with an honest confidence interval and a clear ship/scale/hold recommendation.
- A data scientist must decline to give a causal number when the design does not support one, and say precisely what would.

**Expected competencies.** Participants can select the appropriate method for a given question and data situation, sequence a full analysis (design → power → analyse → validate → communicate), quantify and honestly convey uncertainty, and produce a decision memo that a non-technical leader can act on.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Select the appropriate experimental or quasi-experimental method for a question | LO1, LO4, LO5 |
| 7.2 | Sequence a full engagement from design to decision | LO1–LO5 |
| 7.3 | Quantify and communicate uncertainty to non-technical stakeholders | LO3, LO6 |
| 7.4 | Produce a decision memo with a defensible recommendation | LO6 |
| 7.5 | Recognise and state the limits of what the evidence can support | LO5, LO6 |

## Technical Content

### 1. Method selection: matching the tool to the question

The first and most consequential decision is *which method*, and it follows the data situation, not preference. Teach the selection flow explicitly:

- **Can we randomise going forward?** → run an A/B test (Modules 2–4). Always the first choice.
- **Did a treatment turn on at a known time for some units?** → difference-in-differences (Module 5).
- **Is there an as-good-as-random source of variation in an otherwise-confounded treatment?** → instrumental variables (Module 5).
- **Only cross-sectional observational data with measured confounders?** → matching/weighting on a defended backdoor set (Modules 5–6), with sensitivity analysis.
- **No measured way to close the backdoors?** → declare the effect not identifiable and specify what is missing (Module 6).

The integrative Injaz question has two limbs — a *future* feature (autofill) that can be A/B tested and a *past* pilot (reminders) that cannot — so it exercises the whole flow in one engagement.

### 2. Sequencing a full engagement

A professional engagement runs in a fixed order, and skipping steps is where credibility leaks:

1. **Frame** — write the decision and the estimand ("compared to what, for whom?").
2. **Design** — choose method, unit, OEC, guardrails; write and freeze the analysis plan.
3. **Power** — size the experiment or assess whether the observational data can detect a worthwhile effect.
4. **Analyse** — estimate with correct variance and corrections.
5. **Validate** — SRM/balance for experiments; parallel-trends/refutation/sensitivity for quasi-experiments.
6. **Decide & communicate** — translate to a recommendation with quantified uncertainty.

The discipline is that steps 1–3 happen *before* seeing outcomes; steps 4–5 follow the frozen plan; step 6 is where the value is realised.

### 3. Reconciling experimental and observational evidence

When a question has both an A/B result and a quasi-experimental one, they must be reconciled, not cherry-picked. Teach triangulation: agreement across methods with different assumptions strengthens a claim; disagreement is a finding in itself, usually pointing to a violated assumption (interference in the test, a broken parallel-trend in the DiD). The honest analyst reports both and explains the gap rather than presenting the more convenient number.

### 4. Quantifying and communicating uncertainty

Decision-makers do not act on p-values; they act on ranges and risks. Best practices:

- Lead with the **effect size and its confidence interval** in business units ("+3.2 points, likely between +1.8 and +4.6"), not the p-value.
- State **practical significance** explicitly against the decision threshold set in design.
- Convey **assumptions as risks** ("this holds if the not-yet-treated regions are a fair comparison; the main threat is a coinciding regional campaign").
- Give a **clear recommendation** (ship / scale / hold / redesign) with the reasoning, and say what evidence would change it.
- Use **one decisive visual** (the CI plot or event study), not a wall of tables.

### 5. When the answer is "we cannot conclude"

A central professional skill — and one the assessment explicitly rewards — is delivering a well-founded null or non-identifiability verdict. "The pilot's effect is not distinguishable from zero at the sample we have" and "this effect is not identifiable from the current data; a randomised invitation next quarter would settle it" are *successful* outcomes when they are correct. Teach participants to frame these constructively: what was ruled out, what remains open, and the concrete next step. A confident wrong answer is a failure; an honest "not yet" is a service.

### 6. Common mistakes & production considerations

1. Choosing a method by familiarity rather than by the data situation.
2. Running the steps out of order (peeking before the plan is frozen; drawing the DAG to justify a chosen model).
3. Cherry-picking the more favourable of an experimental and observational estimate.
4. Reporting p-values to leadership instead of effect sizes and intervals.
5. Overstating certainty by hiding the identifying assumptions.
6. Presenting "no significant effect" as "proven no effect."
7. Ending at the analysis instead of the decision — the memo is the deliverable, not the notebook.

**Production considerations.** In an experimentation programme, this engagement pattern becomes a repeatable template: a design doc, a frozen analysis plan, an analysis notebook, a validation report, and a one-page decision memo, all versioned together. That template is exactly what the capstone asks each participant to produce, and what SDA-DSC-311 (Decision Science) consumes as its input.

## Code Examples

### End-to-end engagement scaffold

```python
# injaz_case/engagement.py
"""A reusable engagement scaffold that sequences design -> power -> analyse
-> validate -> decide. Each Injaz question fills in the same skeleton."""
from dataclasses import dataclass, field

@dataclass
class Engagement:
    question: str
    estimand: str                       # ATE / ATT / LATE + population
    method: str                         # ab_test / did / iv / matching
    oec: str
    guardrails: list[str]
    mde: float
    analysis_plan_frozen: bool = False
    result: dict = field(default_factory=dict)

    def freeze_plan(self):
        assert self.method and self.oec and self.mde, "design incomplete"
        self.analysis_plan_frozen = True

    def record(self, effect, ci, validation, recommendation):
        assert self.analysis_plan_frozen, "analyse only after freezing the plan"
        self.result = {"effect": effect, "ci": ci,
                       "validation": validation,
                       "recommendation": recommendation}

autofill = Engagement(
    question="Does AI autofill raise completion for Injaz form submissions?",
    estimand="ATE on completion (all triggered users)",
    method="ab_test", oec="completion_rate",
    guardrails=["time_to_complete", "error_rate", "support_tickets"],
    mde=0.015)
autofill.freeze_plan()
```

### The decisive visual: effect with confidence interval

```python
# injaz_case/decision_plot.py
"""One decisive chart for the memo: effect sizes with CIs across methods,
plus the practical-significance threshold line."""
import matplotlib.pyplot as plt

def decision_plot(results: dict, threshold: float):
    """results: {label: (effect, lo, hi)}"""
    fig, ax = plt.subplots(figsize=(7, 3))
    for i, (label, (eff, lo, hi)) in enumerate(results.items()):
        ax.errorbar(eff, i, xerr=[[eff - lo], [hi - eff]], fmt="o", capsize=4)
        ax.annotate(f"{eff:+.3f}", (eff, i), textcoords="offset points",
                    xytext=(0, 8))
    ax.axvline(0, color="grey", lw=1)
    ax.axvline(threshold, color="green", ls="--", lw=1,
               label=f"ship threshold {threshold:+.3f}")
    ax.set_yticks(range(len(results)))
    ax.set_yticklabels(list(results))
    ax.set_xlabel("Effect on completion rate (with 95% CI)")
    ax.legend()
    return fig

decision_plot({"A/B autofill": (0.021, 0.008, 0.034),
               "DiD reminders": (0.032, 0.018, 0.046),
               "Matching training": (0.041, 0.010, 0.072)}, threshold=0.015)
```

### A structured decision-memo generator

```python
# injaz_case/memo.py
"""Turn an Engagement result into a one-page decision memo skeleton so the
deliverable is the DECISION, not the notebook."""
def render_memo(e) -> str:
    r = e.result
    eff, (lo, hi) = r["effect"], r["ci"]
    verdict = "SHIP" if lo > e.mde else ("HOLD" if hi < e.mde else "INCONCLUSIVE")
    return f"""# Decision Memo — {e.question}
Estimand: {e.estimand}   |   Method: {e.method}
Effect: {eff:+.3f} on {e.oec} (95% CI [{lo:+.3f}, {hi:+.3f}])
Practical threshold (MDE): {e.mde:+.3f}  ->  Recommendation: {verdict}
Validation: {r['validation']}
Rationale: {r['recommendation']}
What would change this: a larger sample / a cleaner control / a randomised pilot.
"""
```

## Hands-on Lab 7 — Full Engagement: The Autofill Decision

| | |
|---|---|
| **Objective** | Run one integrative Injaz engagement end to end — A/B test the AI autofill feature and reconcile it with the observational reminder evidence — and produce a decision memo |
| **Duration** | 50 minutes (feeds directly into the capstone) |
| **Setup** | `lab7-start.ipynb`; all prior Injaz datasets; the `injaz_case/` scaffold |

**Instructions & tasks**

1. *(8 min)* Frame the autofill decision: write the estimand, choose the method, define OEC + guardrails + MDE, and freeze the analysis plan.
2. *(10 min)* Analyse the autofill A/B data (CUPED-adjusted, robust SEs, guardrails with correction); report effect + CI.
3. *(8 min)* Pull in the reminder DiD estimate from Module 5; build the combined decision plot with the ship threshold.
4. *(8 min)* Validate: SRM/balance for the A/B, and restate the DiD's parallel-trends caveat; note any disagreement to reconcile.
5. *(10 min)* Generate the decision memo; write the ship/hold recommendation and the single sentence of "what would change this."
6. *(6 min)* Peer review: exchange memos; each reviewer checks that uncertainty and assumptions are stated, not hidden.

**Expected output**
```
Autofill A/B: +0.021 (95% CI [0.012, 0.030]) CUPED-adjusted; guardrails clean
Ship threshold (MDE): +0.015  ->  CI lower bound 0.012 < threshold -> HOLD/monitor
Reminder DiD (context): +0.032 (95% CI [0.018, 0.046]), parallel trends supported
Memo verdict: HOLD autofill for a longer run to clear the threshold; SCALE reminders
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Memo recommends SHIP on a CI crossing the threshold | Ignoring practical significance | Compare CI to the MDE threshold, not just to zero |
| A/B and DiD disagree, both reported as fact | No reconciliation | Explain the gap via a violated assumption; do not cherry-pick |
| Memo full of p-values | Wrong audience framing | Lead with effect + CI in business units |
| "No effect" stated as proven | Underpowered null misread | Report as "not distinguishable from zero at this sample" |

**Instructor notes.** The graded skill here is judgement, not code — spend the debrief on *why* each pair chose HOLD vs SHIP, and reward memos that state uncertainty crisply. This lab is deliberately a dress rehearsal for the capstone; participants should reuse their scaffold and memo template.

## Mini Exercises

**Quiz (5 questions)**
1. First question to ask when choosing a method? → can we randomise going forward?
2. Which steps must precede seeing outcomes? → framing, design, powering, and freezing the analysis plan.
3. How should an effect be reported to leadership? → effect size with a confidence interval in business units, plus practical-significance verdict.
4. What do you do when experimental and observational estimates disagree? → reconcile via the likely violated assumption; report both, do not cherry-pick.
5. Is "we cannot conclude" ever a correct deliverable? → yes, when justified, with what was ruled out and the next step.

**Debugging exercise.** A memo claims SHIP because "p < 0.05," though the CI lower bound is below the ship threshold; participants rewrite the recommendation correctly.

**Method-selection drill.** Six one-line Injaz questions; teams assign the correct method and justify in one sentence.

**Discussion questions.**
- When is a correct "hold and keep running" more valuable than a fast "ship"?
- How do you present a non-identifiable result so leadership still trusts the analysis?

## Case Study — The Board Wants One Number

**Scenario.** The Injaz steering board asks for "the number" — a single figure for the impact of last year's combined digital-experience investments (autofill A/B, reminder rollout, training programme) — to justify next year's budget.

**Business context.** The three interventions used three different designs with three different estimands and assumptions; collapsing them into one figure would be misleading, but the board wants simplicity.

**Technical challenge.** Present a coherent, honest impact story across methods without fabricating a false-precision single number.

**Constraints.** A non-technical board; a 10-minute slot; a real budget decision.

**Solution approach (facilitate, don't lecture).** (1) Present each effect with its CI and assumption on one decision plot. (2) Explain what can and cannot be summed (different populations/estimands). (3) Offer a defensible aggregate where legitimate (e.g., total additional completions attributable, with a range) rather than a single point. (4) Give a clear recommendation per intervention (scale reminders, hold autofill, expand training) with the evidence strength for each.

**Discussion questions.**
1. Why can the three estimates not simply be added into one effect?
2. What is a legitimate way to give the board a single actionable figure? (attributable completions with a range)
3. How do you honour "keep it simple" without sacrificing honesty?
4. Which intervention has the strongest causal evidence, and how do you convey that ranking?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Correct method selection | Judgement | 6/6 on the selection drill | drill |
| Engagement sequenced correctly | Process | plan frozen before analysis | scaffold state |
| Uncertainty communicated | Communication | effect + CI + practical verdict present | memo review |
| Reconciliation of methods | Reasoning | gap explained, not cherry-picked | memo + debrief |
| Honest limits stated | Integrity | "what would change this" present | memo |

**Example benchmark table (filled during lab):**

| Intervention | Method | Effect (95% CI) | Recommendation |
|---|---|---|---|
| Autofill | A/B test | +0.021 [0.012, 0.030] | Hold / keep running to clear threshold |
| Reminders | DiD | +0.032 [0.018, 0.046] | Scale |
| Training | Matching | +0.041 [0.010, 0.072] | Expand, monitor unobserved-confounding risk |

## Required Visuals and Training Assets

### Diagrams
1. **Method-selection flowchart** — *Purpose:* the module's spine. *Elements:* branches on randomise-forward? / staggered turn-on? / valid instrument? / measured confounders? → A/B, DiD, IV, matching, or not-identifiable. *Style:* full-page decision flow, bilingual.
2. **Engagement pipeline** — *Purpose:* enforce the order. *Elements:* frame → design → power → analyse → validate → decide, with "freeze plan" gate before analyse. *Style:* left-to-right pipeline with a lock icon.
3. **Triangulation** — *Purpose:* reconcile methods. *Elements:* three estimates from different assumptions converging (or not) on a range. *Style:* forest-plot-style convergence.
4. **Uncertainty-to-decision** — *Purpose:* the communication payoff. *Elements:* a CI plotted against a ship-threshold line, mapping regions to ship/hold/redesign. *Style:* annotated interval chart.

### Images (screenshots)
1. **Decision plot**: *why:* the memo's centrepiece; *content:* three effects with CIs and the threshold line.
2. **Decision memo**: *why:* the deliverable exemplar; *content:* the rendered one-page memo.
3. **Frozen analysis plan**: *why:* process evidence; *content:* the plan object marked frozen before results.

### Simulations
1. **Method-mismatch cost** — *Setup:* apply the wrong method to a question (e.g., naive A/B on an interfering feature). *Expected behaviour:* the estimate is biased vs the correct method. *Learning objective:* method selection is a causal decision.
2. **Disagreement diagnoser** — *Setup:* inject an assumption violation so A/B and DiD diverge. *Expected behaviour:* the divergence traces to the violated assumption. *Learning objective:* disagreement is information.

### Interactive Activities
- **Board-briefing role-play (20 min):** each team presents its decision memo to a "board" (peers + instructor) who probe the uncertainty and assumptions.
- **Method-selection speed round (10 min):** rapid-fire questions; teams call the method and justify.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `injaz_autofill_ab.csv` | Course-generated randomised autofill outcomes | CSV | 70,000 rows | Integrative A/B analysis |
| all prior Injaz datasets | Course-generated | CSV/Parquet | — | Reconciliation across methods |

### Demo Requirements
- **Instructor demo:** run the autofill engagement end to end and render the decision memo in under 10 minutes.
- **Student demo:** each team delivers a 3-minute board briefing of its memo; the class probes one assumption.
- **Expected outputs:** a frozen plan, a correct A/B analysis, a reconciled multi-method decision plot, and a one-page decision memo with honest uncertainty.

---

# Final Capstone Project

## Title: The Injaz Experimentation and Impact Evaluation Package

## Project Scenario

You are the experimentation lead assigned to **Injaz (إنجاز)**, the Saudi unified digital-government services platform. Leadership faces two linked decisions before the next budget cycle: (1) whether to nationally launch a new **AI-assisted document-and-form autofill** feature intended to raise service-completion rate, and (2) whether to **scale the regional reminder-notification programme** that was piloted region-by-region last year without randomisation. Your mandate: design and analyse a clean experiment for the feature, produce a credible causal evaluation of the pilot where randomisation was impossible, and deliver a decision memo leadership can act on. Everything you built in Labs 1–7 is a component; the capstone is the integration plus your own rigour and communication.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Design (LO1):** a frozen design doc for the autofill A/B test — randomisation unit + justification, OEC, ≥ 3 guardrails, trigger definition, unit of analysis, and a written analysis plan produced *before* analysis.
2. **Power (LO2):** a sizing analysis — required per-arm sample and run-length plan for the chosen MDE, including the arm multiplier and trigger rate, and a CUPED-adjusted alternative with its quantified saving.
3. **Experiment integrity (LO1/LO3):** deterministic hash assignment, a passing SRM check, and a covariate-balance table (all SMD < 0.1) — an experiment that fails these must be reported as invalid.
4. **Analysis (LO3):** the autofill effect with correct (robust or clustered) variance, CUPED adjustment, guardrails checked with the correct multiple-testing family, and a clear statistical-vs-practical-significance verdict against the design threshold.
5. **Causal evaluation (LO4/LO5):** a quasi-experimental evaluation of the reminder pilot (DiD with an event-study parallel-trends check *or* matching with sensitivity analysis), including the DAG/identifying assumption and ≥ 2 refutation/validation checks.
6. **Communication (LO6):** a one-page decision memo with effect sizes and confidence intervals in business units, a ship/scale/hold recommendation per intervention, the key assumptions stated as risks, and an explicit "what would change this."
7. **Reproducibility & rigour (LO3):** a clean, runnable notebook/repo; a fixed random seed; the frozen analysis plan versioned before results; no peeking-driven stopping; honest treatment of any null or non-identifiable result.

**One extension (choose at least one):**
- Heterogeneous treatment effects (CATE) on the autofill test with EconML (causal forest), with an honest note on multiple-testing across subgroups.
- Always-valid / sequential-inference analysis of the autofill test enabling legitimate continuous monitoring.
- Staggered-DiD estimator (Callaway–Sant'Anna or Sun–Abraham) on the full multi-wave reminder rollout, compared against naive TWFE.
- Instrumental-variables estimate of the effect of filing channel on completion, with a defended instrument and first-stage F.
- A power/variance-reduction study quantifying how much CUPED and stratification would shorten future Injaz experiments.

## Architecture (target state)

```
Frame ──> Design doc (frozen plan) ──> Power/sizing ──> [A/B: assign → SRM → balance → analyse]
                                                     └─> [Pilot: DAG → identify → estimate → refute]
   A/B effect (CUPED, robust CI) ─┐
   Pilot effect (DiD/matching CI) ┼──> reconcile ──> Decision plot (vs threshold) ──> Decision memo
   guardrails + validation ───────┘                                                    (ship/scale/hold)
Reproducible notebook: fixed seed · frozen plan versioned before results · honest nulls
```

## Deliverables

1. A runnable analysis notebook (or repo) covering design, power, A/B analysis, and causal evaluation, with a fixed seed and a clean top-to-bottom run.
2. The frozen **design doc + analysis plan** (timestamped/committed *before* the results section).
3. Experiment-integrity evidence: SRM result and covariate-balance table.
4. Causal-evaluation section: DAG, identifying assumption, estimate with CI, and refutation/validation output.
5. A one-page **decision memo** with the decision plot, per-intervention recommendations, quantified uncertainty, and "what would change this."
6. A 6-minute presentation: the two decisions, the evidence and its limits, and the recommendation.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: framed question + frozen design doc + sizing | Day 4 H3 start | instructor spot-check of the plan |
| M-B: A/B analysed (SRM, balance, effect, guardrails) | Day 4 H3 end | integrity checks pass |
| M-C: pilot evaluated (DiD/matching + validation) | Day 4 H4 mid | refutation/validation present |
| M-D: decision memo + extension | Day 4 H4 end | full self-audit checklist |
| M-E: presentation + submission | Day 4 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Experiment design & analysis plan | 15 | Unit justified, OEC + guardrails sound, plan frozen before results | Minor gaps (thin guardrails, late freeze) | No plan / metrics chosen after seeing data |
| Power & sample sizing | 15 | Correct sizing incl. arms, trigger, floor; CUPED saving quantified | Mostly correct; one factor omitted | Wrong or missing sizing; under-run unrecognised |
| Experiment integrity | 10 | SRM + balance correct; invalid experiments flagged | Checks present but partial | No SRM/balance; invalid test analysed anyway |
| A/B analysis correctness | 20 | Robust/clustered variance, CUPED, correct correction family, practical-vs-statistical verdict | 1–2 issues (naive SE or missing correction) | Naive t-test, no correction, p-value worship |
| Causal evaluation | 20 | DAG + assumption stated; DiD/matching valid; ≥ 2 refutations; sensitivity honest | Method sound; validation thin | No identification argument; unvalidated claim |
| Decision communication | 15 | One-page memo: effects+CIs in business units, clear recommendation, risks + "what would change this" | Memo works; uncertainty understated | p-values to leadership; overstated certainty |
| Reproducibility & integrity | 5 | Clean seeded run; honest nulls; no peeking | Minor reproducibility gaps | Non-runnable; peeking-driven stop |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80. A correct, well-justified null or non-identifiability verdict earns full marks on the relevant criteria.

## Assessment Criteria Notes for Instructors

- Grade the *reasoning and honesty first*, the point estimate second — a defensible "hold, keep running" or "not identifiable, here's what's needed" is a top-band answer.
- Anti-pattern flags that cap a criterion at 70%: metrics chosen after seeing data; peeking-driven stopping; controlling for a mediator/collider; presenting an observational estimate with no assumption or refutation; reporting bare p-values to leadership.
- Verify one claim live: ask the participant to state the identifying assumption of their causal estimate and the single unmeasured variable that would break it.

## Bonus Tasks (for early finishers / distinction seekers)

1. Reproduce the peeking hazard on their own A/B data and contrast a sequential method that would have been valid.
2. Add a Rosenbaum-bounds sensitivity analysis quantifying how strong hidden bias must be to overturn the pilot conclusion.
3. Build a reusable `causal_utils.py` (assignment, SRM, balance, sizing, DiD, refutation) and document it as a mini-package.
4. Produce a second decision plot showing how the recommendation changes under the most pessimistic credible assumptions.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** State the fundamental problem of causal inference. → only one potential outcome per unit is observed; individual effects are unobservable.
**Q2.** Decompose the naive difference of means. → ATT + selection bias (E[Y(0)|T=1] − E[Y(0)|T=0]).
**Q3.** Why does more data not fix selection bias? → large n reduces variance, not bias; a biased estimator stays biased.
**Q4.** ATE vs ATT — when is ATT the right estimand? → when evaluating a treatment delivered to a specific/self-selected group.
**Q5.** When should you randomise by user rather than session? → returning users needing a consistent experience or non-independent sessions.
**Q6.** What does an SRM indicate and what must you do? → a likely plumbing bug; do not analyse until explained.
**Q7.** If you halve the MDE, how does required n change? → roughly ×4 (n ∝ 1/MDE²).
**Q8.** Why is a non-significant result not proof of no effect? → the test may be under-powered; absence of evidence ≠ evidence of absence.
**Q9.** Why must CUPED's covariate be pre-treatment? → so treatment cannot affect it, keeping the adjustment unbiased.
**Q10.** How does peeking inflate the false-positive rate? → each look is another chance to cross α; errors compound.
**Q11.** Bonferroni vs Benjamini–Hochberg — what does each control? → FWER (any false positive) vs FDR (expected proportion of false discoveries).
**Q12.** Why can a ratio metric not be t-tested as a mean? → its denominator is random; use the delta method.
**Q13.** When are clustered standard errors required? → when the analysis unit is finer than a cluster randomisation unit.
**Q14.** State the DiD identifying assumption and how it is supported. → parallel trends; supported by flat pre-trends in an event study.
**Q15.** Name the three IV conditions. → relevance, exclusion, independence/exogeneity.
**Q16.** What does IV identify and for whom? → the LATE — the effect for compliers.
**Q17.** What happens when you condition on a collider? → a spurious association opens between its causes (bias).
**Q18.** State the backdoor criterion. → adjust for a set blocking all backdoor paths and containing no descendant of the treatment.
**Q19.** Why should you not control for a mediator when estimating a total effect? → it blocks part of the causal path, shrinking the effect.
**Q20.** How should an effect be reported to leadership? → effect size with a confidence interval in business units, plus a practical-significance verdict.

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a broken experiment (SRM failure + a session-level analysis of a user-randomised test), diagnose both defects and produce a corrected, correctly-powered analysis. Scored on diagnosis (40%), corrected analysis (40%), verification evidence (20%).

**PA-2 (30 min, Day 3):** Given an observational dataset and a proposed kitchen-sink regression, draw the DAG, identify the mediator and collider being wrongly controlled, and produce the correctly-identified estimate with a refutation. Scored against the model solution (identification correctness 50%, refutation 30%, written verdict 20%).

**PA-3:** Capstone (rubric above) — 40% of the course grade. Labs completion + PA-1/PA-2 + quiz — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint notebooks + expected outputs |
| PA-1 + PA-2 | 20% | corrected analyses + written diagnoses |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | frozen plan, analysis, memo — reasoning-first |

Badge issuance (Causal badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical simulated seeds/results across submissions are checked). A correct null or non-identifiability verdict, well justified, never counts against the participant.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Clone the course repo; push checkpoint notebooks (`lab1-start` … `lab7-start`, `lab1-solution` … `lab7-solution`) and all `sim-*` branches
- [ ] Regenerate the synthetic Injaz datasets (`injaz_users.csv`, `injaz_sessions.csv`, `injaz_experiment_results.csv`, `injaz_regions_panel.csv`, `injaz_autofill_ab.csv`) with fixed seeds; verify every solution notebook runs top-to-bottom
- [ ] Confirm `dowhy`, `econml`, and `linearmodels` import cleanly in the primary environment **and** on the Colab fallback (heaviest dependency chain — test early)
- [ ] Dry-run all 7 labs end-to-end on a clean machine; time Labs 4 and 5b specifically (overrun-prone)
- [ ] Print A4 posters: two-worlds counterfactual, MDE-vs-n quadratic, the three DAG junctions, method-selection flowchart
- [ ] Load the simulators (confounding dial, peeking sandbox, collider generator, parallel-trends breaker) and verify sliders work
- [ ] Prepare the shared leaderboard (recovered ATE accuracy, sizing plans, DiD estimates)
- [ ] Confirm the classroom can pip-install the stack (or pre-mirror wheels for DoWhy/EconML in restricted environments)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + Jupyter (or VS Code + Python extension)
- [ ] `pip install numpy scipy pandas matplotlib statsmodels scikit-learn`
- [ ] `pip install dowhy econml linearmodels networkx` (the causal stack — install early; it is the heaviest)
- [ ] Clone the course repo; run the provided `check_env.py` (validates all imports and prints ✓/✗)
- [ ] Colab fallback: open the provided notebook and run the top `!pip install` cell once
- [ ] A basic refresher on hypothesis testing and confidence intervals from SDA-DSC-111 (linked pre-read)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| DoWhy/EconML install failures | High | Pre-mirrored wheels; Colab fallback; pin versions in `requirements.txt` |
| Confusing ATE and ATT in write-ups | High | Return to the estimand card sort; require naming the estimand before every analysis |
| "Big data fixes bias" misconception | High | Re-run the Module 1 convergence-vs-n plot on their own data |
| Re-randomising to fix an imbalanced covariate | Medium | Stop the room; reinforce adjust-in-analysis, never re-roll |
| Peeking / stopping at first significance | Medium | The peeking simulation; enforce the frozen plan |
| Controlling for mediators/colliders reflexively | Medium | The Module 6 mediator-trap exercise; DAG-before-model rule |
| Naive TWFE on staggered rollout | Medium | Provide the clean not-yet-treated comparison; mention modern estimators |
| Reporting p-values to "leadership" in the memo | Medium | Memo rubric requires effect + CI in business units |
| Weak-instrument over-interpretation | Low | Require first-stage F; flag F < 10 as unreliable |

## Timing Recommendations

- Protect Labs 4 (analysis) and 5b (DiD) at full length; compress Module 7 theory (it lands through Lab 7) if behind.
- If a cohort is strong: bring the staggered-DiD estimator and EconML CATE into main scope on Day 3–4.
- If a cohort is weak: reduce Lab 5 to Part A (matching) as a guided demo and keep Part B (DiD) hands-on; never cut the parallel-trends/event-study observation — it is the module's credibility lesson.
- Hard rule: capstone framing (Day 4 H3) must start on time; cut discussion, not build time.
- Simulation-first is non-negotiable — always plant a known effect and recover it before touching Injaz data.

## Discussion Prompts (use during transitions)

1. "Injaz completion is up 6 points since launch. What would convince you the feature *caused* it — and what would convince you it didn't?"
2. "Your model is right, but the workshop attendees would have completed more anyway. Which number does the ministry's budget actually depend on?"
3. "You have four million rows. Which of your problems does that solve, and which does it not touch at all?"
4. "A colleague adds a 'sensible' control and the effect vanishes. Bug or feature — and how do you tell?"
5. "The board wants one number. What is the most honest single number you can give — and what must come with it?"

## Wrap-up (Day 4 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it (one slide): design→M2, power→M3, analysis→M4, causal evaluation→M5/M6, communication→M7.
- Reinforce the through-line: randomisation is the gold standard; every observational method is an assumption-laden attempt to approximate it, and honesty about those assumptions is the graded skill.
- Forward pointer: SDA-DSC-311 (Decision Science and Optimization Modeling) consumes exactly these causal estimates as inputs to prescriptive decisions; the decision memo produced today is the interface.
- Collect: analysis notebooks, frozen design docs, decision memos; issue Causal-badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12 with numpy, scipy, pandas, statsmodels, scikit-learn, DoWhy, EconML, linearmodels, and networkx. Every causal method is taught simulation-first on the Injaz golden thread — plant a known effect, recover it, then apply it where the truth is unknown. Verify pinned package versions in the course lock file before each delivery.*
