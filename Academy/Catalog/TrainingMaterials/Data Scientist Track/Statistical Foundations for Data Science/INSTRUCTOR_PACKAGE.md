# Statistical Foundations for Data Science
## الأسس الإحصائية لعلم البيانات

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Statistical Foundations for Data Science |
| **Arabic Title** | الأسس الإحصائية لعلم البيانات |
| **Code** | SDA-DSC-111 |
| **Track** | Data Scientist (عالم البيانات) |
| **Level** | Practitioner (ممارس) |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | Analysts, graduates, and engineers entering data science |
| **Prerequisites** | SDA-FND-103; SDA-FND-104 recommended |
| **Assessment** | Labs; statistical analysis project |
| **Stackability** | Core statistics badge · Required for all Specialist Data Scientist modules · Next: SDA-DSC-112 / SDA-AIE-111 |
| **Tools & Platforms** | Python · SciPy · statsmodels · Jupyter |

## Course Description

A rigorous, applied grounding in the statistics that underpin trustworthy data science. Participants master probability, distributions, estimation, hypothesis testing, and regression, applying each concept computationally in Python. The module builds the inferential judgement needed to draw valid conclusions from data.

The course is built around a single evolving artefact: **"Mawid Analytics"**, a national primary-care appointments dataset (synthetic, SDAIA-style, modelled on a Saudi Ministry of Health clinic-booking platform). Across seven modules participants model appointment **no-shows** and **wait times** — first as random processes, then descriptively, then through estimation, testing, confounding analysis, regression, and finally simulation. Every lab adds a component to one continuous investigation, so by Day 4 each participant owns a complete, defensible statistical analysis that answers a real operational question: *how should the Ministry cut appointment no-shows without harming access?* This is the exact analytical judgement the Specialist modules (SDA-DSC-112 Data Visualization, SDA-DSC-211 Advanced ML) assume you already have.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Apply probability rules and distributions to model real-world uncertainty
2. **LO2** — Analyze sampling variability using confidence intervals and standard errors
3. **LO3** — Implement hypothesis tests and interpret p-values and effect sizes correctly
4. **LO4** — Develop linear and logistic regression models and diagnose their assumptions
5. **LO5** — Evaluate statistical claims for common fallacies and misuse
6. **LO6** — Simulate statistical processes computationally to validate analytical results

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | The language of uncertainty | M1: Probability & Common Distributions · M2: Descriptive Statistics & Sampling | 55% | 45% | Fitted no-show/wait-time distributions + a defensible stratified sample of clinics |
| **Day 2** | From sample to claim | M3: Estimation & Confidence Intervals · M4: Hypothesis Testing & Effect Sizes | 45% | 55% | Regional no-show rate estimates with CIs + an analysed SMS-reminder A/B test with effect size |
| **Day 3** | What actually drives no-shows | M5: Correlation, Causation & Confounding · M6: Linear & Logistic Regression | 45% | 55% | Confounding-adjusted analysis + fitted linear (wait-time) and logistic (no-show) models with diagnostics |
| **Day 4** | Validate and decide | M7: Simulation & Resampling Methods · Capstone | 35% | 65% | Bootstrap/permutation validation + capstone statistical analysis and decision memo |

## Hour-by-Hour Breakdown

### Day 1 — The Language of Uncertainty

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why statistics is the foundation** + course kickoff + the Mawid dataset | Frame the golden-thread question; recognise how bad statistics produces confident wrong decisions | Interactive lecture + dataset tour | 80/20 |
| 2 | **Probability & random variables** (M1) | Axioms, conditional probability, Bayes; PMF/PDF/CDF; expectation and variance | Lecture + live SciPy demo | 70/30 |
| 3 | **Common distributions** (M1) | Bernoulli, Binomial, Poisson; Normal, Exponential, Lognormal; fitting distributions to data | Lecture + fitting demo | 60/40 |
| 4 | **Lab 1 — Model no-shows and wait times** | Fit distributions to the Mawid data; compute Bayesian no-show update | Guided lab (pairs) | 10/90 |
| 5 | **Descriptive statistics, shape & sampling** (M2) + **Lab 2** | Central tendency/spread, robustness, skew; sampling designs; CLT and standard error | Micro-lecture + guided lab | 40/60 |

### Day 2 — From Sample to Claim

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Estimation & confidence intervals** (M3) | Point estimators, bias, standard error; t-interval and proportion intervals; interpretation | Lecture + live demo | 65/35 |
| 2 | **Lab 3 — Estimate regional no-show rates** | Wilson intervals per region; sample-size / margin-of-error planning | Guided lab (pairs) | 10/90 |
| 3 | **Hypothesis testing & p-values** (M4) | NHST logic, error types, power; t-tests, z-test for proportions, chi-square | Lecture + test-writing demo | 70/30 |
| 4 | **Effect sizes & multiple testing** (M4) | Cohen's d, odds ratio, Cramér's V; p-hacking, peeking, corrections | Lecture + case discussion | 65/35 |
| 5 | **Lab 4 — Analyse the SMS-reminder A/B test** | Two-proportion test, effect size, power, correct interpretation | Guided lab (pairs) | 10/90 |

### Day 3 — What Actually Drives No-Shows

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Correlation, causation & confounding** (M5) | Pearson/Spearman; Simpson's paradox; confounders; DAG basics | Lecture + Simpson's demo | 70/30 |
| 2 | **Lab 5 — Uncover the confounder** | Reproduce a Simpson's-paradox reversal; adjust by stratification | Guided lab (pairs) | 10/90 |
| 3 | **Linear regression** (M6) | OLS, interpretation, R²; assumptions and diagnostics | Lecture + statsmodels demo | 65/35 |
| 4 | **Logistic regression** (M6) | Log-odds, odds ratios, evaluation (ROC/AUC, calibration) | Lecture + live demo | 65/35 |
| 5 | **Lab 6 — Model wait time and no-show** | Fit and diagnose linear + logistic models on Mawid data | Guided lab (pairs) | 10/90 |

### Day 4 — Validate and Decide

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Simulation & Monte Carlo** (M7) | Pseudo-randomness, seeds; validating CLT and CI coverage by simulation | Lecture + simulation demo | 55/45 |
| 2 | **Bootstrap & permutation tests** (M7) + **Lab 7** | Nonparametric bootstrap CIs; permutation tests; when resampling fails | Micro-lecture + guided lab | 30/70 |
| 3 | **Capstone assembly** | Integrate all analyses into one report; robustness checks | Project work | 0/100 |
| 4 | **Capstone completion + decision memo** | Quantified recommendation with uncertainty; peer review round | Project work | 0/100 |
| 5 | **Capstone presentations + assessment + wrap-up** | 6-minute defences; rubric scoring; path to SDA-DSC-112 / SDA-AIE-111 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module analyses the **same** Mawid appointments dataset. Never introduce a throwaway toy dataset — always evolve the no-show / wait-time investigation. This is what makes the Day-4 capstone achievable: participants have already produced each component.
- **Computational-first pedagogy:** teach each concept twice — once analytically (formula + intuition), once by simulation (Module 7 tools previewed lightly from Day 1). When the two agree, understanding sticks; when a participant's analytical answer disagrees with their simulation, that gap is the lesson.
- **Pace control:** Labs 4 and 6 are the most overrun-prone. Publish checkpoint notebooks (`lab1_start.ipynb`, `lab1_solution.ipynb`, …) in the course repository so stragglers can fast-forward.
- **Pairing:** rotate pairs each day; pair a strong-Python participant with a strong-maths participant — the skill transfer is the point.
- **Environment strategy:** primary = local Jupyter (Anaconda); fallback = Google Colab (notebooks provided, no install). Verify both the week before delivery. Pin `numpy`, `scipy`, `statsmodels`, `pandas` versions in `environment.yml`.
- **Language:** deliver in English or Arabic; keep all code, identifiers, and variable names in English (production convention in Saudi enterprise environments). Statistical terms are introduced bilingually on first use.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-4 morning is deliberately heavier so the afternoon protects capstone build time.
- **Assessment logistics:** the statistical-analysis project (capstone) is scored live during Day 4 Hour 5; collect notebook URLs at the end of Hour 4 so outputs can be verified before defences begin. Guard against copied analyses — the bootstrap seeds and CI numbers should differ across submissions.

---

# Module 1 — Probability and Common Distributions

## Module Overview

**Purpose.** Every downstream idea in data science — a confidence interval, a p-value, a model's predicted probability — is a statement about a random process. This module gives participants the probability vocabulary and the catalogue of distributions needed to *model uncertainty deliberately* rather than treat it as noise. By the end, a participant can look at a real column of data (no-show flags, wait times) and say what random process plausibly generated it, and compute with that model in Python.

**Business relevance.** In the Saudi public and private sectors, decisions increasingly rest on probabilistic claims: "there is an 8% chance this transaction is fraudulent", "the clinic will be over capacity with probability 0.3 next Tuesday". Ministries and banks that cannot quantify uncertainty either freeze (over-caution) or over-commit (false confidence). Probabilistic literacy is the difference. For the Ministry of Health's Mawid platform, understanding no-shows as a Bernoulli process — and wait times as a skewed continuous distribution — is the precondition for every capacity and reminder-policy decision that follows.

**Industry use cases.**
- A national clinic network forecasts the number of no-shows per session (Binomial) to decide safe overbooking levels.
- A telecom models call-centre arrivals per minute (Poisson) to staff shifts.
- A bank uses Bayes' theorem to combine a model score with a base rate to produce an actionable fraud probability rather than a raw score.

**Expected competencies.** After this module a participant can state and apply the probability axioms and Bayes' theorem, distinguish discrete from continuous random variables, choose an appropriate named distribution for a real quantity, compute probabilities and moments with `scipy.stats`, and fit a distribution to observed data and judge the fit.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Apply the probability axioms, conditional probability, and Bayes' theorem to real questions | → LO1 |
| 1.2 | Distinguish discrete vs continuous random variables and work with PMF/PDF/CDF | → LO1 |
| 1.3 | Select and parameterise an appropriate named distribution for a real quantity | → LO1 |
| 1.4 | Compute probabilities, expectations, and variances using `scipy.stats` | → LO1, LO6 |
| 1.5 | Fit a distribution to data and evaluate goodness of fit | → LO1, LO5 |

## Technical Content

### 1. Probability foundations and conditional reasoning

Probability is a function that assigns to each event a number in [0, 1] obeying three axioms (Kolmogorov): non-negativity, `P(sample space) = 1`, and additivity for mutually exclusive events. Everything else — the multiplication rule, complements, inclusion–exclusion — follows. The two ideas that pay off most immediately in data science are:

- **Conditional probability:** `P(A | B) = P(A ∩ B) / P(B)`. This is how data updates belief. "The probability a patient no-shows *given* they missed their last appointment" is a conditional probability, and it is far more useful than the marginal no-show rate.
- **Independence:** `A` and `B` are independent iff `P(A ∩ B) = P(A)·P(B)`. Most real health events are *not* independent (a patient's two appointments are correlated), and assuming independence when it is false is one of the most common quiet errors in analysis (Module 7 revisits this for the bootstrap).

**Bayes' theorem** rearranges the definition into the single most important formula for practitioners: `P(H | D) = P(D | H)·P(H) / P(D)`. It converts "probability of the data given a hypothesis" (which models give you) into "probability of the hypothesis given the data" (which decisions need).

**Instructor note:** run the classic base-rate demonstration live. A no-show *screening flag* that is 90% sensitive and 90% specific, applied to a population with an 18% no-show rate, produces a positive predictive value near 66% — not 90%. Participants consistently guess ~90%; the gap is the lesson.

### 2. Random variables, PMF/PDF/CDF, expectation and variance

A **random variable** maps outcomes to numbers. Two families:

- **Discrete** (countable values): described by a **probability mass function** `p(x) = P(X = x)`. Example: `no_show ∈ {0, 1}`; number of no-shows in a 20-slot session `∈ {0, …, 20}`.
- **Continuous** (values on an interval): described by a **probability density function** `f(x)`, where probabilities are *areas*: `P(a ≤ X ≤ b) = ∫ f(x) dx`. Example: `wait_time_min`. A crucial subtlety to teach explicitly: `f(x)` is a density, not a probability, and can exceed 1; `P(X = exactly 12.0000)` is 0 for a continuous variable.

The **cumulative distribution function** `F(x) = P(X ≤ x)` works for both and is the practitioner's workhorse: percentiles, p-values, and "probability of waiting more than 30 minutes" are all CDF evaluations (`1 - F(30)`).

**Expectation** `E[X]` is the long-run average (`Σ x·p(x)` or `∫ x·f(x) dx`); **variance** `Var(X) = E[(X − E[X])²]` measures spread, and its square root, the **standard deviation**, is in the same units as the data. Two properties participants must internalise: `E[aX + b] = a·E[X] + b`, and `Var(aX + b) = a²·Var(X)` (shifting does not change spread; scaling changes it quadratically).

### 3. Common discrete distributions

| Distribution | Models | Parameters | Mean / Var | Mawid example |
|---|---|---|---|---|
| **Bernoulli** | One yes/no trial | `p` | `p` / `p(1−p)` | A single appointment: no-show or not |
| **Binomial** | # successes in `n` independent trials | `n, p` | `np` / `np(1−p)` | # no-shows among 20 booked slots |
| **Poisson** | # events in a fixed interval | `λ` | `λ` / `λ` | # walk-ins per clinic per hour |
| **Geometric** | # trials until first success | `p` | `1/p` / `(1−p)/p²` | # appointments until first no-show |

The **Binomial** is the natural model for the golden thread: if each of `n` booked patients no-shows independently with probability `p`, the number of empty slots is `Binomial(n, p)`. Overbooking policy is then a tail-probability question. The **Poisson** approximates the Binomial when `n` is large and `p` small (`λ = np`), which is why rare-event counts (walk-ins, complaints, system errors) are Poisson-shaped.

### 4. Common continuous distributions

| Distribution | Models | Parameters | Notes |
|---|---|---|---|
| **Uniform** | Equal density on `[a, b]` | `a, b` | Baseline / random draws |
| **Normal (Gaussian)** | Sums/averages of many small effects | `μ, σ` | The CLT's limit; symmetric |
| **Exponential** | Time between Poisson events | `λ` (rate) | Memoryless; right-skewed |
| **Lognormal** | Positive, right-skewed quantities | `μ, σ` (of log) | Wait times, incomes, durations |

Real **wait times are almost never Normal** — they are positive and right-skewed, with a long tail of unlucky patients. The **Lognormal** (or Gamma) is usually the honest model. Teaching participants to *not* default to the Normal for every continuous variable is one of this module's highest-value corrections; forcing a symmetric model onto skewed data produces confidence intervals that undercover the tail exactly where operational risk lives.

The **Normal** still earns its central place — not because raw data is Normal, but because *averages* are (Module 2's CLT). The 68–95–99.7 rule and the standardisation `z = (x − μ) / σ` are the everyday tools that let any Normal question reduce to the standard Normal.

### 5. Bayes' theorem in operational practice

Bayesian updating is the engine of decision-making under uncertainty. Structure it as **prior → likelihood → posterior**:

- **Prior:** base rate before seeing evidence (overall no-show rate = 18%).
- **Likelihood:** how the evidence behaves under each hypothesis (a patient with a prior no-show shows the "risky" pattern 3× more often).
- **Posterior:** updated probability after the evidence.

The recurring failure this prevents is **base-rate neglect**: judging a patient "likely to no-show" from a strong signal while ignoring that no-shows are rare to begin with. In a health or fraud context this is the difference between a workable alert list and one so full of false positives that staff ignore it.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes (each is seeded into the Lab 1 dataset or exercises):**
1. Confusing `P(A | B)` with `P(B | A)` (the "prosecutor's fallacy").
2. Assuming independence between a patient's repeated appointments.
3. Defaulting to a Normal model for skewed, positive quantities like wait time.
4. Treating a PDF value as a probability.
5. Base-rate neglect when interpreting a screening signal.
6. Reporting a mean for a heavily skewed distribution as if it summarised a "typical" patient.

**Best practices:** always plot the empirical distribution before naming a model; state the random process in words before writing code; check moments (does the sample variance roughly match the model's `np(1−p)`?); use the CDF, not eyeballing, to answer tail questions.

**Real-world example (narrate, 5 min):** A regional health cluster set a fixed overbooking rule of "+2 patients per 20-slot session" using the *average* no-show count. Because no-shows are Binomial with real variance, roughly one session in six still overflowed — angry patients, staff overtime. Modelling the *distribution* (not just the mean) and choosing the overbook level from the 90th-percentile of empty slots cut overflow incidents by two-thirds with no change in average utilisation. The fix was not more data — it was using the whole distribution instead of a single number.

## Code Examples

### Working with distributions in SciPy

```python
# module1/distributions_demo.py
"""Core probability toolkit for the Mawid analysis.
All examples use scipy.stats — the course-standard library."""
import numpy as np
from scipy import stats

rng = np.random.default_rng(seed=42)  # reproducibility from line one

# --- Binomial: number of no-shows in a 20-slot session, p = 0.18 ---
n, p = 20, 0.18
no_shows = stats.binom(n=n, p=p)

print(f"Expected no-shows/session : {no_shows.mean():.2f}")      # np = 3.6
print(f"Std dev                   : {no_shows.std():.2f}")       # sqrt(np(1-p))
print(f"P(exactly 3 no-shows)     : {no_shows.pmf(3):.4f}")
print(f"P(5 or more no-shows)     : {no_shows.sf(4):.4f}")       # survival = 1 - cdf(4)

# Overbooking decision: how many extra can we safely book?
# Book x extra; overflow if no_shows < x. Find largest x with P(overflow) <= 0.10.
for extra in range(0, 8):
    p_overflow = no_shows.cdf(extra - 1) if extra > 0 else 0.0
    print(f"Overbook +{extra}: P(overflow) = {p_overflow:.3f}")

# --- Lognormal: wait time in minutes (positive, right-skewed) ---
# Parameterise so median wait ~ 18 min with a long tail.
sigma, scale = 0.5, 18.0            # scale = exp(mu) = median
wait = stats.lognorm(s=sigma, scale=scale)
print(f"Median wait      : {wait.median():.1f} min")
print(f"Mean wait        : {wait.mean():.1f} min  (> median: skew)")
print(f"P(wait > 40 min) : {wait.sf(40):.3f}")
```

### Bayes' theorem: base rates make or break an alert list

```python
# module1/bayes_noshow.py
"""Combine a base rate with a screening signal correctly."""

def posterior_no_show(prior: float, sensitivity: float, specificity: float) -> float:
    """P(no-show | flagged) via Bayes' theorem.

    prior       : base no-show rate P(no_show)
    sensitivity : P(flagged | no_show)      -- true positive rate
    specificity : P(not flagged | show)     -- true negative rate
    """
    p_flag_given_noshow = sensitivity
    p_flag_given_show   = 1 - specificity
    numerator = p_flag_given_noshow * prior
    denominator = numerator + p_flag_given_show * (1 - prior)
    return numerator / denominator

ppv = posterior_no_show(prior=0.18, sensitivity=0.90, specificity=0.90)
print(f"P(no-show | flagged) = {ppv:.1%}")   # ~66%, NOT 90% -- base-rate lesson
```

### Fitting a distribution to real wait-time data

```python
# module1/fit_wait_times.py
"""Fit candidate models to observed wait times and judge the fit."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")
waits = df["wait_time_min"].dropna().to_numpy()

# Fit lognormal and (wrongly) normal, then compare on the tail.
shape, loc, scale = stats.lognorm.fit(waits, floc=0)   # floc=0: positive support
mu_n, sigma_n = stats.norm.fit(waits)

lognorm = stats.lognorm(shape, loc=0, scale=scale)
normal  = stats.norm(mu_n, sigma_n)

# Kolmogorov-Smirnov goodness-of-fit (larger p = better consistency with model)
ks_ln = stats.kstest(waits, lognorm.cdf)
ks_no = stats.kstest(waits, normal.cdf)
print(f"Lognormal KS p-value : {ks_ln.pvalue:.4f}")
print(f"Normal    KS p-value : {ks_no.pvalue:.4f}")   # typically far smaller

# Where the Normal lies: tail probability of a long wait
obs_tail = (waits > 45).mean()
print(f"Observed P(wait>45)  : {obs_tail:.3f}")
print(f"Lognormal says       : {lognorm.sf(45):.3f}")
print(f"Normal says          : {normal.sf(45):.3f}")   # usually under-estimates
```

## Hands-on Lab 1 — Model No-Shows and Wait Times

| | |
|---|---|
| **Objective** | Model the two golden-thread quantities probabilistically: no-shows as a Bernoulli/Binomial process, wait times as a fitted continuous distribution; use Bayes to build a no-show risk update |
| **Duration** | 50 minutes |
| **Setup** | Python 3.11, Jupyter, `numpy scipy pandas matplotlib`; `data/clinic_visits.csv` loaded; `git checkout lab1-start` or open `lab1_start.ipynb` |

**Instructions & tasks**

1. *(5 min)* Load `clinic_visits.csv`; report the overall no-show rate `p̂` and the mean/median/std of `wait_time_min`. Note that mean > median for wait time.
2. *(10 min)* Model per-session no-shows as `Binomial(n=20, p=p̂)`. Compute `P(≥ 5 no-shows)` and the largest safe overbooking level with `P(overflow) ≤ 0.10`.
3. *(15 min)* Fit **lognormal** and **normal** distributions to `wait_time_min`. Overlay both on the histogram; run a KS test for each; state which model the tail supports and why.
4. *(10 min)* Bayesian update: using `prior = p̂`, `sensitivity = 0.85`, `specificity = 0.80`, compute `P(no-show | flagged)`. Then recompute for a high-risk subgroup (`prior = 0.35`) and discuss how the base rate moves the answer.
5. *(5 min)* Compute `P(no-show | prior_no_shows ≥ 1)` empirically from the data and compare to the marginal rate — evidence updates belief.
6. *(5 min)* Write a 3-sentence markdown conclusion: which distribution models wait time, and what overbooking level you recommend.

**Expected output**
```
Overall no-show rate p̂      : 0.181
Wait time  mean/median/std  : 21.3 / 18.0 / 11.2 min   (right-skewed)
P(>=5 no-shows / session)   : 0.372
Safe overbook level         : +2  (P(overflow)=0.084)
KS p-value  lognormal/normal: 0.41 / 0.001   -> lognormal wins
P(no-show | flagged), base 0.18 : 0.48
P(no-show | flagged), base 0.35 : 0.70
P(no-show | prior_no_show>=1)   : 0.34   (vs 0.18 marginal)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `lognorm.fit` returns odd `loc` | Fitting a location shift | Pass `floc=0` — wait times are positive with support at 0 |
| KS p-value exactly 0.0 | Data has ties / discreteness | Note limitation; supplement with a Q–Q plot for judgement |
| Bayes result "feels too low" | Base-rate neglect intuition | This *is* the lesson — the base rate dominates |
| Overbook level seems too low | Using mean instead of distribution | Decide from the CDF tail, not `np` |

**Instructor notes.** The wait-time fit is the emotional centre of the lab: participants who "know" data is Normal watch the Normal model badly miss the tail. Keep the KS p-values on the projector. Fast finishers: fit a Gamma distribution too and compare AIC — a natural bridge to model selection.

## Mini Exercises

1. **Concept.** A patient has two appointments this month. Under independence, `P(both no-show) = p²`. Given real correlation, is the true probability higher or lower? Why does this matter for capacity planning? → higher; independence under-estimates clustered risk.
2. **Compute.** Walk-ins arrive Poisson with `λ = 4/hour`. Compute `P(0 walk-ins in an hour)` and `P(> 6)`. (`stats.poisson(4)`.)
3. **Interpret.** A colleague reports `f(20) = 0.05` from a fitted wait-time PDF and concludes "5% of patients wait exactly 20 minutes." Correct them.
4. **Bayes.** Recompute the Lab 1 PPV with `specificity = 0.95`. Which lever — sensitivity or specificity — moves PPV more here, and why (base rate context)?
5. **Debugging exercise.** A notebook computes `P(X = 12)` for a continuous `wait` model and gets 0, then "fixes" it by rounding. Explain why the 0 is correct and what question they actually meant (`P(11.5 ≤ X ≤ 12.5)`).

## Case Study — Overbooking Policy at a Riyadh Primary-Care Cluster

**Scenario.** A cluster of eight primary-care clinics in Riyadh runs 20-slot morning sessions. Management wants to overbook to offset no-shows but has been burned by overflow days (patients arriving to find no capacity). They currently overbook by the rounded average no-show count.

**Business context.** Every empty slot is lost capacity in a system with long queues; every overflow is a patient-experience failure and staff overtime. The Vision 2030 health-access targets make *both* wasted capacity and access failures politically visible.

**Technical challenge.** Choose an overbooking level that respects a risk tolerance (`P(overflow) ≤ 10%`) rather than optimising the average — i.e., use the Binomial *distribution*, not its mean.

**Constraints.** No-show probability varies by clinic (0.12–0.26); some sessions have chronic-illness patients with lower no-show rates; the policy must be explainable to non-statisticians on the operations team.

**Solution approach (facilitate, don't lecture).** (1) Estimate `p` per clinic; (2) model empty slots as `Binomial(20, p)`; (3) pick overbook level from the CDF at the 10% tail; (4) show the average-based policy's true overflow risk for contrast; (5) present as a one-page lookup table (clinic → recommended overbook).

**Discussion questions.**
1. Why does the mean-based policy overflow so often despite "matching the average"?
2. How would you communicate a probabilistic policy to operations staff who want one number?
3. Should chronic-condition sessions get a different rule? What data would justify it?
4. What breaks if no-shows within a session are *not* independent (e.g., a bus route delay affects many)?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Correct distribution choice | Modelling | Lognormal/Gamma for wait, Binomial for no-shows | Lab review |
| Wait-time fit (KS p-value) | Fit quality | Lognormal p > 0.05; Normal rejected | `scipy.kstest` |
| Overbook decision from tail | Reasoning | Uses CDF, not mean | Lab output |
| Bayes computation | Correctness | PPV within ±0.01 of key | Auto-check |
| Tail probability error | Accuracy | |model − empirical| < 0.03 for `P(wait>45)` | Comparison |

**Example benchmark table (filled during lab):**

| Quantity | Empirical | Normal model | Lognormal model |
|---|---|---|---|
| P(wait > 30) | 0.214 | 0.180 | 0.209 |
| P(wait > 45) | 0.061 | 0.019 | 0.058 |
| 95th percentile wait | 44 min | 39 min | 45 min |

## Required Visuals and Training Assets

### Diagrams
1. **Discrete vs continuous map** — *Purpose:* anchor the PMF/PDF/CDF distinction. *Elements:* side-by-side panels: a Binomial bar chart with `P(X=k)` labelled, and a lognormal density with a shaded area labelled `P(a≤X≤b)`; both with their CDFs beneath. *Style:* flat vector, two-colour, English labels with Arabic subtitles.
2. **Bayes' theorem flow** — *Purpose:* make prior→likelihood→posterior tangible. *Elements:* a natural-frequency tree (1,000 patients → 180 no-shows / 820 shows → flagged/not) with the PPV computed at the leaves. *Style:* tree diagram, colour-coded.
3. **Distribution zoo cheat-sheet** — *Purpose:* memorisable reference poster. *Elements:* the six course distributions with shape thumbnail, parameters, mean/var, and one Mawid use each. *Style:* printable A4.

### Images (screenshots)
1. **SciPy distribution overlay** — histogram of wait times with lognormal and normal PDFs overlaid; *why:* the module's headline visual; *content:* the Normal visibly missing the right tail.
2. **KS-test output** — terminal showing the two p-values; *why:* fit judged by number, not eye.
3. **Overbooking lookup table** — the per-clinic recommended overbook level; *why:* connects probability to a decision artefact.

### Simulations
1. **Law of large numbers for no-shows** — *Setup:* simulate no-show flags with `p=0.18`, plot the running proportion as `n` grows. *Expected:* convergence to 0.18 with shrinking wobble. *Learning objective:* probability is a long-run frequency; small samples lie.
2. **Binomial → Poisson convergence** — *Setup:* animate `Binomial(n, λ/n)` as `n` grows for fixed `λ`. *Expected:* PMF approaches Poisson. *Learning objective:* why rare-event counts are Poisson.

### Interactive Activities
- **"Name that distribution" card sort (10 min):** 12 real quantities (time between ER arrivals, exam scores, # complaints/day, coin flips…) sorted onto distribution cards with justification.
- **Base-rate gut-check poll (5 min):** class predicts the PPV before the Bayes reveal; the miss is discussed.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Synthetic, generated by course tooling (SDAIA-style; KSA regions, SAR-free health context, realistic no-show/wait generative model) | CSV | ~50,000 rows × 14 cols | The golden thread; used in every module |
| `data_dictionary.md` | Course team | Markdown | 1 page | Column definitions and units |

### Demo Requirements
- **Instructor demo:** fit lognormal vs normal to wait times live, and show the tail miss in under 6 minutes.
- **Student demo:** one pair presents their overbooking recommendation and defends the risk tolerance.
- **Expected outputs:** correct distribution choices, KS-supported fit, a defensible overbook level.

---

# Module 2 — Descriptive Statistics and Sampling

## Module Overview

**Purpose.** Before any inference, a data scientist must summarise honestly and sample defensibly. This module covers the two halves of that skill: describing a dataset with the right summary statistics for its shape, and understanding how a *sample* relates to the *population* it is meant to represent. The module culminates in the Central Limit Theorem — the bridge that makes all of Days 2–4 possible.

**Business relevance.** Almost every reported "average" in a government dashboard or executive deck is a summary statistic, and almost every one is computed on a *sample*. When the summary is the wrong one (a mean on skewed wait times) or the sample is biased (only patients who completed a satisfaction survey), the resulting decision is wrong in a way no downstream sophistication can repair. In the Mawid programme, a national no-show rate quoted from a convenience sample of easy-to-reach urban clinics would systematically mislead policy for rural regions. Getting description and sampling right is the cheapest, highest-leverage correctness win in the whole course.

**Industry use cases.**
- A national statistics office reports median (not mean) income because the distribution is right-skewed.
- A health ministry draws a *stratified* sample across regions so small regions are not drowned out by Riyadh's volume.
- A survey team quantifies non-response bias before trusting a satisfaction score.

**Expected competencies.** After this module a participant can choose and compute appropriate measures of centre and spread for a distribution's shape, quantify skew and identify outliers robustly, distinguish and design the main probability sampling schemes, articulate common sampling biases, and demonstrate the CLT computationally to explain why sample means are Normal and how the standard error shrinks with `√n`.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Select and compute shape-appropriate measures of centre and spread | → LO2, LO5 |
| 2.2 | Quantify skewness and identify outliers with robust methods | → LO2, LO5 |
| 2.3 | Distinguish and design SRS, stratified, cluster, and systematic samples | → LO2 |
| 2.4 | Identify and reason about selection, non-response, and survivorship bias | → LO5 |
| 2.5 | Demonstrate the Central Limit Theorem and the `√n` law computationally | → LO2, LO6 |

## Technical Content

### 1. Measures of centre and spread — and robustness

Three measures of centre, each answering a different question:

- **Mean** — the balance point; uses every value, but is dragged by outliers and skew.
- **Median** — the 50th percentile; robust, and the honest "typical value" for skewed data like wait times and income.
- **Mode** — the most common value; the only sensible centre for categorical data (most common region).

For spread: the **standard deviation** pairs with the mean; the **interquartile range (IQR = Q3 − Q1)** and the **median absolute deviation (MAD)** pair with the median and resist outliers. The teaching rule: **match the centre and spread to the shape.** For the golden thread, `wait_time_min` is reported as *median (IQR)*; a symmetric quantity like standardised age might use *mean (SD)*. Reporting `mean ± SD` for a heavily skewed variable implies a symmetric spread that does not exist and misleads every reader.

### 2. Distribution shape: skew, kurtosis, quantiles, and outliers

Numbers summarise; shape explains. Three shape tools:

- **Skewness** measures asymmetry. Positive (right) skew — a long right tail — is the signature of durations, counts, and money. Mean > median is the quick diagnostic.
- **Kurtosis** measures tail heaviness; high kurtosis means outliers are more common than a Normal would predict — directly relevant to risk.
- **Quantiles and the boxplot** turn shape into a decision tool. The **1.5×IQR rule** flags outliers reproducibly: below `Q1 − 1.5·IQR` or above `Q3 + 1.5·IQR`.

An outlier is a *question, not a verdict*: a 180-minute wait might be a data error, a genuine crisis day, or a mis-recorded unit. The practitioner investigates before deleting; silent outlier removal is a common way to manufacture a cleaner-but-wrong story.

### 3. Population, sample, and the anatomy of sampling bias

The **population** is everyone/everything the claim is about; the **sampling frame** is the list we can actually draw from; the **sample** is who we measure. Bias enters in the gaps:

- **Coverage / selection bias:** the frame omits part of the population (an online survey misses patients without smartphones).
- **Non-response bias:** those who respond differ from those who don't (satisfied patients answer satisfaction surveys less).
- **Survivorship bias:** we only see the units that "survived" to be observed (analysing only patients who *attended* tells you nothing reliable about no-shows).

No sample size fixes a biased frame. A biased estimate computed on a million records is still biased — it just has a tighter (falsely confident) interval around the wrong number. This is the single most important idea in the module: **bias is a property of the process, not the size.**

### 4. Probability sampling designs

| Design | How | When it shines | Risk |
|---|---|---|---|
| **Simple random (SRS)** | Every unit equal chance | Homogeneous population | Small subgroups under-represented |
| **Stratified** | Split into strata, sample within each | Subgroups matter (regions) | Needs strata info up front |
| **Cluster** | Randomly pick whole groups | Cost/logistics (sample clinics, not patients) | Higher variance if clusters differ |
| **Systematic** | Every k-th unit | Simple, ordered frames | Danger if hidden periodicity aligns with k |

For the Mawid analysis, a **stratified sample by region** is usually correct: it guarantees representation for low-volume regions (e.g., Al-Jouf) that an SRS would sample only a handful of times, and it lets us weight back to national totals. Participants learn to state the estimand ("national no-show rate, comparable across regions") *before* choosing the design.

### 5. Sampling distribution, the CLT, and the standard error

This is the conceptual keystone of the whole course. Fix the idea in three moves:

1. A statistic (like the sample mean `x̄`) computed on a random sample is itself **a random variable** — draw a different sample, get a different `x̄`.
2. The distribution of `x̄` over all possible samples is the **sampling distribution**.
3. The **Central Limit Theorem** states: for large `n`, the sampling distribution of the mean is approximately **Normal**, centred on the population mean `μ`, with standard deviation `σ/√n` — *regardless of the shape of the original data*.

That last clause is why the Normal distribution dominates inference even though raw data (wait times!) is not Normal. The **standard error** `SE = σ/√n` is the sampling distribution's spread, and it is the quantity every confidence interval and t-test in Days 2–4 is built from. The `√n` law has a hard operational consequence: **to halve your uncertainty you must quadruple your sample.** Participants who feel this in a simulation stop over-trusting small samples for the rest of their careers.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. Reporting a mean for skewed data as the "typical" value.
2. Deleting outliers before understanding them.
3. Treating a large convenience sample as if size cured bias.
4. Confusing the standard deviation (spread of data) with the standard error (spread of the mean).
5. Systematic sampling over a frame with hidden periodicity.
6. Ignoring finite-population and clustering effects when clusters are sampled.

**Best practices:** always plot before summarising; report centre *and* spread as a matched pair; state the population and frame explicitly; prefer stratification when subgroups carry the decision; keep the estimand written down.

**Real-world example (narrate):** A satisfaction dashboard reported 4.6/5 for a clinic network, driving a "no action needed" decision. The score came from an SMS survey answered by 9% of patients — overwhelmingly those with good experiences (non-response bias). A follow-up *stratified callback* sample of non-responders scored 3.1/5 and surfaced the access problems the dashboard had hidden for a year. The correction cost one afternoon of sampling design; the delay had cost twelve months.

## Code Examples

### Shape-aware description with pandas

```python
# module2/describe.py
"""Describe the Mawid data honestly: shape drives the summary chosen."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")

waits = df["wait_time_min"].dropna()
print("Mean   :", round(waits.mean(), 1))     # dragged up by the tail
print("Median :", round(waits.median(), 1))   # the honest 'typical' wait
print("SD     :", round(waits.std(), 1))
print("IQR    :", round(waits.quantile(0.75) - waits.quantile(0.25), 1))
print("Skew   :", round(stats.skew(waits), 2))  # positive => right-skewed

# Robust outlier flag via 1.5 * IQR rule
q1, q3 = waits.quantile([0.25, 0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
n_out = (waits > upper).sum()
print(f"Outlier threshold (upper): {upper:.0f} min  -> {n_out} flagged")

# Report style: median (IQR) for skewed, mean (SD) for symmetric
print(f"Report -> wait time: {waits.median():.0f} min "
      f"(IQR {q1:.0f}-{q3:.0f})")
```

### Designing a stratified sample by region

```python
# module2/stratified_sample.py
"""Draw a region-stratified sample so small regions are represented."""
import numpy as np
import pandas as pd

df = pd.read_csv("data/clinic_visits.csv")
rng = np.random.default_rng(2026)

# Proportional allocation: sample n_total keeping regional proportions,
# but enforce a minimum per stratum so tiny regions are not lost.
n_total, min_per_region = 3000, 100

def allocate(group, n_total, frame_size, min_per):
    share = len(group) / frame_size
    return max(min_per, round(share * n_total))

frame_size = len(df)
parts = []
for region, grp in df.groupby("region"):
    k = min(len(grp), allocate(grp, n_total, frame_size, min_per_region))
    parts.append(grp.sample(n=k, random_state=rng.integers(1e9)))
sample = pd.concat(parts, ignore_index=True)

# Compare the naive SRS estimate vs stratified estimate of no-show rate
srs = df.sample(n=len(sample), random_state=7)
print("True (full)      no-show rate:", round(df["no_show"].mean(), 4))
print("SRS estimate                 :", round(srs["no_show"].mean(), 4))
print("Stratified estimate          :", round(sample["no_show"].mean(), 4))
print("\nPer-region sample counts:\n", sample["region"].value_counts())
```

### Demonstrating the Central Limit Theorem

```python
# module2/clt_demo.py
"""Show that means of skewed wait times become Normal, and SE ~ 1/sqrt(n)."""
import numpy as np
import pandas as pd

df = pd.read_csv("data/clinic_visits.csv")
population = df["wait_time_min"].dropna().to_numpy()   # right-skewed, NOT normal
rng = np.random.default_rng(0)

mu = population.mean()
sigma = population.std()

for n in (5, 30, 100):
    means = np.array([rng.choice(population, size=n, replace=True).mean()
                      for _ in range(5000)])
    print(f"n={n:>3}: mean of means={means.mean():6.2f} "
          f"(pop {mu:.2f}) | SE observed={means.std():5.2f} "
          f"| SE predicted (sigma/sqrt(n))={sigma/np.sqrt(n):5.2f}")
# As n grows: the histogram of `means` looks Normal even though `population`
# is skewed, and observed SE tracks sigma/sqrt(n). Quadrupling n halves SE.
```

## Hands-on Lab 2 — Describe, Sample, and Prove the CLT

| | |
|---|---|
| **Objective** | Produce an honest descriptive summary of the Mawid data, draw a defensible region-stratified sample, and demonstrate the CLT + `√n` law by simulation |
| **Duration** | ~40 minutes (within Day 1 Hour 5) |
| **Setup** | `lab2_start.ipynb`; `data/clinic_visits.csv`; `numpy pandas scipy matplotlib` |

**Instructions & tasks**

1. *(8 min)* Build a summary table: for `wait_time_min` report median (IQR) and skew; for `no_show` report the proportion; for `region` report the mode. Justify each choice in one line.
2. *(8 min)* Apply the 1.5×IQR rule to `wait_time_min`; report how many outliers and inspect five of them — data error or real? Decide and document (do not silently drop).
3. *(12 min)* Draw a region-stratified sample (`n≈3000`, min 100/region). Compare its no-show estimate to a same-size SRS and to the full-population truth. Which is closer for the smallest region?
4. *(10 min)* CLT simulation: for `n ∈ {5, 30, 100}`, build 5,000 sample means of `wait_time_min`; plot the three histograms; confirm observed SE ≈ `σ/√n`.
5. *(2 min)* Write a 3-line conclusion: which summary you'd publish, and why stratification mattered for one region.

**Expected output**
```
wait_time_min : median 18 (IQR 13-27), skew +1.3  -> report median
no_show rate  : 0.181
Outliers (>1.5 IQR): 612 flagged; 3 inspected are real crisis-day waits, kept
Smallest region (Al-Jouf): true 0.146 | SRS 0.190 (n=41) | stratified 0.151 (n=100)
CLT SE: n=30 observed 2.05 vs predicted 2.04  -> matches; histogram Normal-shaped
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Stratified estimate = SRS estimate | Forgot minimum-per-stratum enforcement | Enforce `min_per_region`; check small-region counts |
| SE observed ≠ predicted | Using sample SD with `ddof` mismatch | Use population `σ` for the prediction; keep `ddof` consistent |
| CLT histogram still skewed at n=5 | Correct! | Small `n` inherits skew; that *is* the lesson — increase `n` |
| Dropped outliers changed the median a lot | Silent deletion | Restore; investigate first, document decision |

**Instructor notes.** The smallest-region comparison (task 3) is the payoff — an SRS gives that region a wild estimate from ~40 records; stratification stabilises it. Keep both numbers on screen. Fast finishers: add a *cluster* sample (sample whole clinics) and observe the inflated variance versus stratified.

## Mini Exercises

1. **Concept.** For each variable, name the right centre + spread pair: patient age (roughly symmetric), wait time (right-skew), region (categorical), no-show flag (binary). Justify.
2. **Compute.** Compute skewness of `wait_time_min` before and after a `log` transform. What happens, and what does it suggest for later modelling?
3. **Sampling design.** You can afford to visit 20 of 400 clinics in person. Which design (SRS/stratified/cluster) and why? What is the main variance risk?
4. **Bias.** A no-show rate is computed only from patients who booked online. Name the bias and its likely direction on the national estimate.
5. **Debugging exercise.** A colleague reports `SE = 11.2 min` and calls it "the uncertainty in our estimate of the mean wait." They used the SD, not `SD/√n`. Fix it for `n = 3000` and explain the difference in one sentence.

## Case Study — The Satisfaction Score That Lied

**Scenario.** A regional health cluster's executive dashboard shows patient satisfaction of 4.6/5, computed from an opt-in SMS survey. Leadership plans to reallocate improvement budget away from this cluster.

**Business context.** Budget reallocation affects 300,000 patients. The dashboard is trusted precisely because it shows a big `n` (48,000 responses) — but that number is the trap.

**Technical challenge.** Diagnose why a large-sample statistic can be badly biased, and design a sampling plan that produces a trustworthy estimate.

**Constraints.** Callbacks are expensive (limited to ~500); the frame of non-responders is available; results are needed before the budget cycle closes.

**Solution approach.** (1) Recognise non-response bias — 9% response rate, skewed to satisfied patients; (2) draw a *stratified random callback* of non-responders; (3) combine responder and non-responder estimates with response-rate weighting; (4) report the corrected score with an honest interval (Module 3). Reveal: the corrected score is materially lower and reverses the budget decision.

**Discussion questions.**
1. Why does `n = 48,000` provide false comfort here?
2. Would doubling the SMS sample fix the problem? Why not?
3. How do you weight responders and non-responders to a single estimate?
4. What one sentence would you add to the dashboard to prevent this misuse?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Correct centre/spread choice | Reasoning | Median(IQR) for skew, mean(SD) for symmetric | Lab review |
| Stratified vs SRS error (small region) | Sampling quality | Stratified closer to truth | Comparison |
| CLT SE match | Validation | |observed − σ/√n| / SE < 5% | Simulation |
| Bias identification | Judgement | Names bias + direction correctly | Exercise |
| Outlier handling | Rigour | Investigated, documented, not silently dropped | Lab notes |

**Example benchmark table:**

| Estimator | Full-pop no-show | Estimate | Abs error (smallest region) |
|---|---|---|---|
| SRS (n=3000) | 0.181 | 0.176 | 0.044 |
| Stratified (n=3000) | 0.181 | 0.180 | 0.005 |

## Required Visuals and Training Assets

### Diagrams
1. **Population → frame → sample funnel** — *Purpose:* make bias visible as gaps. *Elements:* three nested shapes with the coverage gap and non-response gap called out with red wedges; a "biased but tight" vs "unbiased" dartboard inset. *Style:* funnel + dartboard, colour-coded.
2. **Sampling designs comparison** — *Purpose:* choose the right design. *Elements:* four grids (SRS/stratified/cluster/systematic) showing which units are picked. *Style:* icon grid, printable.
3. **CLT staircase** — *Purpose:* show shape → Normal as `n` grows. *Elements:* skewed population feeding three increasingly-Normal sampling distributions for `n=5,30,100`, with SE shrinking. *Style:* left-to-right progression.

### Images (screenshots)
1. **Boxplot with outliers flagged** — wait time by region; *why:* shape and outliers at a glance.
2. **Stratified vs SRS per-region counts** — *why:* shows small-region protection.
3. **CLT histogram trio** — *why:* the module's headline result.

### Simulations
1. **`√n` law explorer** — *Setup:* slider on `n`; live SE and CI width. *Expected:* quadruple `n` → half the SE. *Learning objective:* precision is expensive.
2. **Bias vs variance dartboard** — *Setup:* toggle a biased frame; watch estimates cluster tightly around the *wrong* value. *Learning objective:* size cannot cure bias.

### Interactive Activities
- **"Which mean lies?" gallery walk (10 min):** four real skewed charts; teams decide mean vs median and defend.
- **Sampling-design clinic (10 min):** given three estimands, teams pick and justify a design.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread (from M1) | CSV | ~50,000 rows | Description, sampling, CLT |
| `survey_responses.csv` | Synthetic opt-in survey with built-in non-response bias | CSV | ~48,000 rows | Case-study bias demonstration |

### Demo Requirements
- **Instructor demo:** run the CLT simulation live; show the skewed population becoming a Normal sampling distribution.
- **Student demo:** one pair defends their sampling design and the small-region result.
- **Expected outputs:** honest summary table, stratified sample, CLT confirmation.

---

# Module 3 — Estimation and Confidence Intervals

## Module Overview

**Purpose.** A single number ("the no-show rate is 18.1%") is a point estimate, and on its own it is nearly useless because it hides how much it could be wrong. This module teaches participants to attach honest uncertainty to every estimate — to produce and correctly interpret confidence intervals — and to plan sample sizes so that an estimate is precise enough to act on. This is the operational payoff of the CLT from Module 2.

**Business relevance.** Decisions differ enormously depending on interval width. "No-show rate 18% ± 1%" supports a fine-tuned reminder policy; "18% ± 9%" says *collect more data before spending anything*. In Saudi public programmes where interventions are funded at national scale, quoting a point estimate without an interval is not just sloppy — it invites overconfident, expensive mistakes. The ability to say "we are 95% confident the true rate is between X and Y, and here is the sample size that would halve that range" is exactly the judgement that separates a data scientist from a spreadsheet operator.

**Industry use cases.**
- A ministry reports regional no-show rates *with intervals* so it does not over-react to a small region's noisy point estimate.
- A/B testing (Module 4) rests entirely on the interval around a difference.
- A survey team computes the sample size needed to hit a ±2% margin before fieldwork begins.

**Expected competencies.** After this module a participant can compute point estimates and standard errors, build and correctly interpret t-intervals for means and Wilson intervals for proportions, explain what a confidence interval does and does *not* claim, and compute the sample size required for a target margin of error.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Compute point estimates, standard errors, and their sampling distribution | → LO2 |
| 3.2 | Construct t-intervals for means and Wilson/Wald intervals for proportions | → LO2 |
| 3.3 | Interpret a confidence interval correctly and refute common misreadings | → LO2, LO5 |
| 3.4 | Plan sample size and margin of error for a target precision | → LO2 |
| 3.5 | Judge when the interval's assumptions hold and choose a robust alternative | → LO2, LO5, LO6 |

## Technical Content

### 1. Point estimation and the qualities of a good estimator

An **estimator** is a recipe (a statistic) for guessing a population parameter from a sample; an **estimate** is the number it produces. Three properties decide whether an estimator is trustworthy:

- **Unbiasedness:** `E[estimator] = parameter` — on average it hits the target. The sample mean is an unbiased estimator of `μ`; the sample variance is unbiased *only* with the `n−1` denominator (Bessel's correction), which is why `ddof=1` matters.
- **Consistency:** as `n → ∞`, the estimate converges to the truth. Guaranteed by the CLT for the mean.
- **Efficiency:** among unbiased estimators, smaller variance is better — it extracts more precision per data point.

**Maximum likelihood estimation (MLE)** is the general principle behind most estimators participants will meet later (including logistic regression in Module 6): choose the parameter value that makes the observed data most probable. For a proportion, the MLE is simply the sample proportion `p̂ = x/n`. Naming MLE now — even lightly — makes regression feel like an application of a known idea rather than magic.

### 2. Standard error: the width of the sampling distribution

The **standard error** is the standard deviation of the estimator's sampling distribution — it quantifies how much the estimate would bounce around across repeated samples. The two the course uses constantly:

- **Mean:** `SE(x̄) = s / √n` (using sample SD `s`).
- **Proportion:** `SE(p̂) = √( p̂(1−p̂) / n )`.

Everything about precision flows from these two formulas. Both shrink like `1/√n` — the same expensive law from Module 2. The SE is *not* the spread of the data (that is the SD); it is the spread of the *estimate*. Confusing the two is the single most common error in this material, so it is worth a full whiteboard minute: SD describes patients, SE describes our knowledge of the average patient.

### 3. Confidence intervals for means and proportions

A **confidence interval** is `estimate ± (critical value) × SE`. Two workhorses:

**Mean (t-interval).** Because we estimate `σ` with `s`, we use the **t-distribution** (heavier tails than Normal, converging to Normal as `n` grows): `x̄ ± t*(n−1) · s/√n`. For `n > ~30` the t and z are nearly identical, but using t is always defensible.

**Proportion.** The textbook **Wald interval** `p̂ ± z*·√(p̂(1−p̂)/n)` is *badly behaved* for small `n` or extreme `p̂` (it can extend below 0 or cover poorly). The course default is the **Wilson score interval**, which stays in [0,1] and has far better coverage — `statsmodels.stats.proportion.proportion_confint(..., method="wilson")`. Teaching participants to reach for Wilson (not Wald) is a concrete, memorable upgrade over how proportions are usually taught.

### 4. Interpreting a confidence interval — and what it does NOT mean

This subsection prevents a career's worth of misstatements. A 95% CI means: *if we repeated the whole sampling process many times and built an interval each time, about 95% of those intervals would contain the true parameter.* The confidence is a property of the **procedure**, not of any single interval.

What it does **not** mean:
- ✗ "There is a 95% probability the true rate is in *this* interval." (The parameter is fixed; the interval is random. Frequentist intervals do not assign probability to the parameter.)
- ✗ "95% of patients fall in this interval." (That confuses the interval for the estimate with the spread of the data.)
- ✗ "A wider interval is a worse result." (It is an *honest* result reflecting less information.)

The correct one-liner participants should be able to say cold: *"We are 95% confident the national no-show rate is between 17.6% and 18.6%,"* understanding "confident" as shorthand for the procedure's long-run coverage.

### 5. Sample size and margin-of-error planning

The **margin of error** is the `±` half-width: `MoE = z*·SE`. Inverting it gives the sample size needed for a target precision. For a proportion at 95% confidence:

`n = z*² · p̂(1−p̂) / MoE²`  (use `p̂ = 0.5` for the most conservative/largest `n` when unknown).

This is planning, done *before* data collection, and it is where the `√n` law bites: halving the margin quadruples the cost. A practitioner who can walk into a planning meeting and say "a ±1% national estimate needs ~9,600 records; ±2% needs ~2,400 — which precision does the decision actually require?" is immediately valuable. The reverse question — "given the `n` we can afford, what precision do we get?" — is equally routine.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. Reporting a point estimate with no interval.
2. The probability misinterpretation of a single CI (see 3.4).
3. Wald intervals for small-`n` or extreme proportions (use Wilson).
4. Confusing SE with SD.
5. Forgetting that a biased sample (Module 2) makes the interval precisely wrong — CIs quantify *sampling* error, not bias.
6. Planning sample size with an over-optimistic assumed effect, then being "underpowered" (Module 4 link).

**Best practices:** always pair an estimate with an interval; state the confidence level and method; use Wilson for proportions and t for means; write the estimand and assumptions next to the number; remember a CI is silent about bias.

**Real-world example (narrate):** A programme office reported no-show rates for 13 regions as bare percentages and "discovered" that Najran (smallest region) had the "worst" rate at 26%. A reminder campaign was targeted there. With intervals, Najran's estimate was 26% ± 11% (n≈70) — statistically indistinguishable from the national 18%. The apparent crisis was sampling noise. Adding one column (the interval) would have redirected the budget to a region whose *interval* genuinely excluded the national rate.

## Code Examples

### Confidence interval for a proportion (Wilson vs Wald)

```python
# module3/proportion_ci.py
"""No-show rate with a proper confidence interval. Wilson, not Wald."""
import pandas as pd
from statsmodels.stats.proportion import proportion_confint

df = pd.read_csv("data/clinic_visits.csv")
x = int(df["no_show"].sum())         # number of no-shows
n = len(df)                          # number of appointments
p_hat = x / n

wald_lo,   wald_hi   = proportion_confint(x, n, alpha=0.05, method="normal")
wilson_lo, wilson_hi = proportion_confint(x, n, alpha=0.05, method="wilson")

print(f"p_hat = {p_hat:.4f}")
print(f"Wald   95% CI: [{wald_lo:.4f}, {wald_hi:.4f}]")
print(f"Wilson 95% CI: [{wilson_lo:.4f}, {wilson_hi:.4f}]  <- course default")

# Per-region intervals: this is where small regions reveal their noise
for region, grp in df.groupby("region"):
    xr, nr = int(grp["no_show"].sum()), len(grp)
    lo, hi = proportion_confint(xr, nr, alpha=0.05, method="wilson")
    flag = "  <-- excludes national" if (hi < p_hat or lo > p_hat) else ""
    print(f"{region:12s} n={nr:5d}  {xr/nr:.3f}  CI [{lo:.3f},{hi:.3f}]{flag}")
```

### t-interval for a mean wait time

```python
# module3/mean_ci.py
"""t-interval for mean wait time, with SE spelled out."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")
waits = df["wait_time_min"].dropna().to_numpy()

n = waits.size
xbar = waits.mean()
s = waits.std(ddof=1)                 # ddof=1 -> unbiased sample SD
se = s / np.sqrt(n)                    # standard ERROR (not SD)
t_star = stats.t.ppf(0.975, df=n - 1) # two-sided 95%
lo, hi = xbar - t_star * se, xbar + t_star * se

print(f"mean wait = {xbar:.2f} min")
print(f"SD  (spread of patients)  = {s:.2f}")
print(f"SE  (spread of the mean)  = {se:.3f}")
print(f"95% t-CI for mean: [{lo:.2f}, {hi:.2f}] min")

# scipy one-liner for cross-check
ci = stats.t.interval(0.95, df=n - 1, loc=xbar, scale=se)
print("cross-check:", tuple(round(c, 2) for c in ci))
```

### Sample-size planning

```python
# module3/sample_size.py
"""How many records for a target margin of error on a proportion?"""
from scipy import stats
import math

def n_for_margin(margin, p=0.5, conf=0.95):
    """Conservative (p=0.5) sample size for a +/- `margin` proportion CI."""
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    return math.ceil(z**2 * p * (1 - p) / margin**2)

for m in (0.005, 0.01, 0.02, 0.03):
    print(f"margin +/-{m*100:>3.1f}% -> n = {n_for_margin(m):,}")

# Reverse: given n we can afford, what margin do we achieve?
def margin_for_n(n, p=0.5, conf=0.95):
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    return z * math.sqrt(p * (1 - p) / n)

print(f"With n=2400 we get +/-{margin_for_n(2400)*100:.2f}%")
```

## Hands-on Lab 3 — Estimate Regional No-Show Rates with Intervals

| | |
|---|---|
| **Objective** | Produce national and per-region no-show estimates *with* Wilson confidence intervals, decide which regions genuinely differ from the national rate, and plan the sample size for a follow-up study |
| **Duration** | 50 minutes |
| **Setup** | `lab3_start.ipynb`; `data/clinic_visits.csv`; `statsmodels scipy pandas` |

**Instructions & tasks**

1. *(8 min)* Compute the national no-show `p̂` and its Wilson 95% CI. Report Wald alongside and note where they differ.
2. *(12 min)* Compute per-region Wilson CIs. Flag regions whose interval **excludes** the national rate — these are the only ones with evidence of a real difference.
3. *(8 min)* Build a t-interval for mean `wait_time_min` (national and for one small region). Explicitly print SD vs SE and explain the difference in a comment.
4. *(12 min)* Sample-size planning: how many records for a ±1% national no-show margin? For ±2%? For a specific small region to reach ±3%? Tabulate.
5. *(6 min)* Reproduce the "Najran crisis" trap: show that the smallest region's alarming point estimate has an interval overlapping the national rate.
6. *(4 min)* Write a 4-line recommendation: which regions warrant intervention now vs more data first.

**Expected output**
```
National no-show: 0.181  Wilson 95% CI [0.178, 0.185]  (Wald near-identical, big n)
Regions excluding national rate: Makkah (high), Eastern (low)   [2 of 13]
Smallest region: 0.146  CI [0.089, 0.229]  -> overlaps national, DO NOT act yet
mean wait 21.3 min; SD 11.2 (patients) vs SE 0.05 (the mean) -- 95% CI [21.2, 21.4]
Sample size: +/-1% -> 9,604 ; +/-2% -> 2,401 ; small-region +/-3% -> 1,068
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Wald CI below 0 for a small region | Wald breaks at extreme p̂/small n | Use Wilson — this is exactly why |
| SE and SD reported as equal | Divided SD by 1, not √n | `se = s/np.sqrt(n)` |
| "Every region differs from national" | Ignoring interval overlap | Compare *intervals*, not point estimates |
| Planned `n` seems huge for ±0.5% | Correct — `√n` law | Halving margin quadruples `n`; discuss cost |

**Instructor notes.** The flagged-region step is the whole point: with 13 regions, only those whose *interval* excludes the national rate are real signals — the rest is noise that a point-estimate table would present as differences. Keep the per-region CI plot (error bars vs a national reference line) on the projector. Fast finishers: apply a multiple-comparison caveat as a teaser for Module 4.

## Mini Exercises

1. **Concept.** In your own words, what does "95% confidence" describe — the interval, the parameter, or the procedure? Give the wrong and right phrasing.
2. **Compute.** For `x = 36` no-shows in `n = 200`, compute the Wilson and Wald 95% CIs. How far apart are the lower bounds?
3. **Planning.** A decision needs the national no-show rate to ±0.75%. How many records? What if you can only get 5,000 — what margin do you actually achieve?
4. **SE vs SD.** Mean wait 21 min, SD 11 min, `n = 3000`. Give the SE and a 95% CI. Which number would you quote to say "typical patient waits about…" and which to say "we know the average to within…"?
5. **Debugging exercise.** A dashboard states "there's a 95% chance the true rate is between 17.8% and 18.5%." Rewrite the sentence to be correct, and explain the specific error in the original.

## Case Study — The Region That Wasn't in Crisis

**Scenario.** A national programme office ranks 13 regions by raw no-show rate and proposes a costly targeted reminder campaign in the three "worst" regions — all of which happen to be the smallest by volume.

**Business context.** The campaign budget is fixed; spending it in the wrong regions means the real problem areas go untreated for a year. Leadership finds ranked tables persuasive and intervals "academic."

**Technical challenge.** Show, convincingly and visually, that the ranking is dominated by sampling noise in small regions, and redirect the budget to regions with genuine evidence of elevated rates.

**Constraints.** The audience is non-technical; the analysis must fit on one slide; the recommendation must still be decisive (not "collect more data everywhere").

**Solution approach.** (1) Compute Wilson intervals per region; (2) plot each region's estimate with error bars against a national reference line; (3) identify the (few) regions whose interval clears the national rate — the defensible targets; (4) for the noisy small regions, propose a cheap targeted *data-collection* step, not a full campaign. The one-slide error-bar chart does the persuading.

**Discussion questions.**
1. Why do the smallest regions dominate the "worst" ranking?
2. How do you make an interval argument to an audience that wants a ranked list?
3. What is the risk of acting on the raw ranking, in patients and riyals?
4. When is "collect more data first" the right answer, and when is it an excuse for inaction?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Interval method | Correctness | Wilson used for proportions | Lab review |
| Interpretation | Rigour | States procedure-level meaning, avoids the probability error | Quiz + exercise |
| SE vs SD | Correctness | Distinguished and computed correctly | Lab output |
| Region flagging | Reasoning | Only interval-excluding regions flagged | Auto-check |
| Sample-size math | Correctness | Within rounding of key values | Auto-check |

**Example benchmark table:**

| Quantity | Estimate | 95% CI | Interpretation |
|---|---|---|---|
| National no-show | 0.181 | [0.178, 0.185] | Precise; act on it |
| Al-Jouf no-show | 0.146 | [0.089, 0.229] | Too noisy; get more data |
| Mean wait (min) | 21.3 | [21.2, 21.4] | Known to ±0.1 min |

## Required Visuals and Training Assets

### Diagrams
1. **Anatomy of a confidence interval** — *Purpose:* decompose `estimate ± crit × SE`. *Elements:* a number line with the point estimate, the SE bracket, the critical value multiplier, and the resulting interval; a caption stating the correct interpretation. *Style:* labelled number line.
2. **The 95% coverage picture** — *Purpose:* kill the probability misinterpretation. *Elements:* 20 horizontal intervals drawn from repeated samples against a fixed vertical "truth" line; ~1 misses; caption "the procedure covers 95% of the time." *Style:* stacked-interval plot.
3. **Margin vs sample-size curve** — *Purpose:* internalise the `√n` cost. *Elements:* MoE on y, `n` on x, with the ±1%/±2%/±3% points marked and the quadrupling annotated. *Style:* curve with callouts.

### Images (screenshots)
1. **Per-region error-bar chart** — estimates with Wilson CIs vs a national reference line; *why:* the case-study centrepiece.
2. **Wilson vs Wald comparison** — for a small region where Wald goes out of bounds; *why:* motivates the default.
3. **Sample-size table output** — *why:* connects statistics to a planning artefact.

### Simulations
1. **CI coverage checker** — *Setup:* draw 1,000 samples, build a CI each, count how many contain the known truth. *Expected:* ~95%. *Learning objective:* what "confidence" actually measures (deep link to Module 7).
2. **Wald-failure demo** — *Setup:* small `n`, extreme `p`; compare Wald vs Wilson coverage over many samples. *Expected:* Wald under-covers. *Learning objective:* method choice matters.

### Interactive Activities
- **"Say it correctly" relay (8 min):** teams rewrite five wrong CI statements; fastest correct set wins.
- **Budget-allocation debate (12 min):** given the region error-bar chart, teams argue where the campaign money goes.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread | CSV | ~50,000 rows | Estimation and intervals |
| `region_reference.csv` | Course team (region volumes) | CSV | 13 rows | Per-region planning |

### Demo Requirements
- **Instructor demo:** build the per-region error-bar plot live and identify the truly-different regions.
- **Student demo:** one pair defends a "collect more data" vs "act now" call for a specific region.
- **Expected outputs:** correct Wilson/t intervals, a defensible region shortlist, a sample-size plan.

---

# Module 4 — Hypothesis Testing and Effect Sizes

## Module Overview

**Purpose.** Estimation says "how big"; hypothesis testing says "is this difference real or could it be chance?" This module teaches participants to frame a question as a test, choose the correct test for the data, compute and *correctly interpret* a p-value, and — crucially — always pair statistical significance with an **effect size** so that "real" is never confused with "important." The module's beating heart is the SMS-reminder A/B test on no-shows, the golden thread's first genuine decision.

**Business relevance.** Every "our intervention worked" claim in a Saudi ministry or company is, implicitly, a hypothesis test — and most are done badly: p-values misread as probabilities that the null is true, peeking at results until they cross 0.05, or celebrating a statistically significant effect so tiny it changes nothing. A data scientist who tests rigorously, reports effect sizes, and guards against p-hacking protects the organisation from funding interventions that don't work and from killing ones that do. For Mawid, the question "does the SMS reminder actually reduce no-shows, and by enough to justify the cost?" is answered here.

**Industry use cases.**
- Product A/B tests on conversion, retention, no-shows.
- Clinical/operational trials comparing two protocols.
- Quality control: is this batch's defect rate above the acceptable threshold?

**Expected competencies.** After this module a participant can state null and alternative hypotheses, choose among t-tests, the two-proportion z-test, and chi-square, interpret p-values and confidence intervals of the difference correctly, compute effect sizes (Cohen's d, odds ratio, Cramér's V), run a power analysis, and apply a multiple-testing correction.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Frame a decision as null/alternative hypotheses and pick the correct test | → LO3 |
| 4.2 | Compute and correctly interpret p-values and the CI of the difference | → LO3, LO5 |
| 4.3 | Report effect sizes and distinguish significance from practical importance | → LO3, LO5 |
| 4.4 | Perform power analysis and sample-size calculation for a test | → LO3 |
| 4.5 | Recognise and correct for multiple testing, peeking, and p-hacking | → LO3, LO5 |

## Technical Content

### 1. The logic of null-hypothesis significance testing

The NHST recipe, stated once, cleanly:

1. **Null hypothesis `H₀`:** the "nothing new" claim (SMS reminders have no effect: `p_reminder = p_control`).
2. **Alternative `H₁`:** what we'd act on (reminders reduce no-shows).
3. **Test statistic:** summarises the data's distance from `H₀` in SE units.
4. **p-value:** `P(data at least this extreme | H₀ true)` — a statement about the data under the null, *not* the probability the null is true.
5. **Decision:** reject `H₀` if `p < α` (significance level, usually 0.05), the pre-registered error budget.

Two error types anchor everything downstream:

| | `H₀` true | `H₀` false |
|---|---|---|
| **Reject `H₀`** | Type I error (α) — false alarm | Correct (power = 1−β) |
| **Fail to reject** | Correct | Type II error (β) — missed effect |

**α is chosen before seeing data**; it is the rate of false alarms you will tolerate. This framing — an error budget agreed in advance — is what makes peeking and p-hacking (subsection 5) obviously illegitimate rather than merely frowned upon.

### 2. Tests for means

| Test | Use when | Function |
|---|---|---|
| **One-sample t** | Compare a mean to a fixed value | `scipy.stats.ttest_1samp` |
| **Two-sample (Welch) t** | Compare two group means, unequal variances | `ttest_ind(..., equal_var=False)` |
| **Paired t** | Two measurements on the same units | `ttest_rel` |

The course default for two independent groups is **Welch's t-test** (unequal variances), not Student's — it is more robust and costs nothing. The paired test is for *before/after on the same clinic* designs, where pairing removes between-clinic variation and sharply increases power. Choosing paired vs independent is a design question participants must reason about, not a default.

### 3. Tests for proportions and categorical data

The golden-thread A/B test compares two **proportions** (no-show rates), so:

- **Two-proportion z-test:** `statsmodels.stats.proportion.proportions_ztest` — the direct test of `p_reminder = p_control`, and the CI of the *difference* is what actually drives the decision.
- **Chi-square test of independence:** `scipy.stats.chi2_contingency` — for association in a contingency table (e.g., no-show vs region, a 2×13 table). Report the chi-square, its p-value, *and* Cramér's V for effect size, because with 50,000 rows almost any association is "significant."

A critical large-`n` lesson lives here: with enough data, *trivial* differences become statistically significant. The p-value answers "is it non-zero?"; it does not answer "is it big enough to matter?" That is the effect size's job (next).

### 4. Effect sizes: making "significant" mean something

An effect size is a *scale-free magnitude* that survives independent of `n`. The three the course uses:

- **Cohen's d** (difference in means / pooled SD): ~0.2 small, ~0.5 medium, ~0.8 large. For "how much shorter is the wait under a new protocol?"
- **Odds ratio / relative risk** (proportions): the natural effect size for the SMS test — "reminders cut the *odds* of a no-show by 35%" is far more decision-useful than "p < 0.001." Also the direct link to logistic regression coefficients (Module 6).
- **Cramér's V** (categorical association): 0 (none) to 1 (perfect), corrects chi-square for table size and `n`.

The non-negotiable habit this module installs: **never report a p-value alone.** Always report the effect size and, ideally, the confidence interval of the effect. A result is *actionable* only when it is both statistically distinguishable from chance and practically large enough to matter — and those are two different questions.

### 5. Power, multiple testing, and the ways tests go wrong

**Power** (`1 − β`) is the probability of detecting a real effect of a given size. It rises with sample size, effect size, and α, and falls with variance. **Underpowered** studies are a double waste: they usually miss real effects, and the "significant" results they do produce are often inflated flukes. Power analysis — done *before* the study — answers "how many patients must the SMS trial enrol to detect a 3-percentage-point drop with 80% power?"

**Multiple testing:** run 20 tests at α = 0.05 and you expect ~1 false positive *even if nothing is real*. Guarding against this:
- **Bonferroni** (`α/m`): simple, conservative.
- **Benjamini–Hochberg** (controls the false discovery rate): better for many tests (e.g., testing no-show differences across all 13 regions at once).

**Peeking / p-hacking:** repeatedly testing as data arrives and stopping when `p < 0.05` inflates the true error rate far above 5%. The honest alternatives — fix the sample size in advance (power analysis) or use sequential methods designed for it — are stated plainly. This is the single most consequential integrity lesson in the course.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. "p = 0.03 means a 3% chance the null is true." (No — it's `P(data | H₀)`.)
2. "p > 0.05 proves no effect." (Absence of evidence ≠ evidence of absence; report power/CI.)
3. Reporting significance with no effect size.
4. Student's t with clearly unequal variances (use Welch).
5. Testing 13 regions and celebrating the one that hit 0.05 (multiple testing).
6. Peeking at an A/B test daily and stopping at the first significant reading.

**Best practices:** pre-register hypothesis, α, sample size, and stopping rule; use Welch by default; always pair p with effect size and CI; correct for multiple comparisons; interpret a non-significant result as "insufficient evidence," qualified by power.

**Real-world example (narrate):** A team ran an SMS-reminder pilot, peeked at the dashboard every morning, and announced victory on day 6 when p first dipped below 0.05 (effect: 0.4 percentage-point drop). Rolled out nationally at real cost, the effect evaporated. A proper fixed-`n`, power-analysed trial later found the true effect was a solid 3-point drop — but *only* for patients with long lead times. Peeking had manufactured a false win and obscured the real, targetable effect. Rigour would have been cheaper *and* found the better policy.

## Code Examples

### The SMS-reminder A/B test: two-proportion z-test with effect size

```python
# module4/ab_test.py
"""Does the SMS reminder reduce no-shows? Test + effect size + CI of the diff."""
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import (proportions_ztest,
                                          confint_proportions_2indep)

df = pd.read_csv("data/clinic_visits.csv")
control  = df[df["sms_reminder"] == 0]["no_show"]
reminder = df[df["sms_reminder"] == 1]["no_show"]

x = np.array([reminder.sum(),   control.sum()])
n = np.array([reminder.count(), control.count()])
p_rem, p_ctl = x / n

# Two-proportion z-test: H0 p_rem = p_ctl  (one-sided: reminder is lower)
stat, pval = proportions_ztest(count=x, nobs=n, alternative="smaller")
print(f"Control no-show : {p_ctl:.4f}")
print(f"Reminder no-show: {p_rem:.4f}")
print(f"z = {stat:.2f}, one-sided p = {pval:.2e}")

# CI of the DIFFERENCE -- this is what drives the decision, not the p-value
lo, hi = confint_proportions_2indep(x[0], n[0], x[1], n[1], method="wald")
print(f"Difference (rem - ctl): {p_rem - p_ctl:+.4f}  95% CI [{lo:+.4f},{hi:+.4f}]")

# Effect size: odds ratio and relative risk
odds_rem = p_rem / (1 - p_rem)
odds_ctl = p_ctl / (1 - p_ctl)
print(f"Odds ratio        : {odds_rem/odds_ctl:.3f}  (reminders cut odds)")
print(f"Relative risk     : {p_rem/p_ctl:.3f}")
print(f"Absolute reduction: {(p_ctl - p_rem)*100:.2f} percentage points")
```

### Chi-square with Cramér's V (guarding against big-n significance)

```python
# module4/chi_square.py
"""Association between region and no-show: significance AND magnitude."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")
table = pd.crosstab(df["region"], df["no_show"])
chi2, p, dof, expected = stats.chi2_contingency(table)

n = table.to_numpy().sum()
k = min(table.shape) - 1
cramers_v = np.sqrt(chi2 / (n * k))    # effect size for a contingency table

print(f"chi2 = {chi2:.1f}, dof = {dof}, p = {p:.2e}")
print(f"Cramer's V = {cramers_v:.3f}")
# Lesson: with n=50,000, p is tiny (significant) but V may be ~0.05 (trivially
# small). 'Significant' != 'important'. Report BOTH, always.
```

### Power analysis for the trial design

```python
# module4/power.py
"""How many patients per arm to detect a 3-point no-show drop at 80% power?"""
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

p_control, p_target = 0.18, 0.15         # detect a 3pp reduction
effect = proportion_effectsize(p_control, p_target)  # Cohen's h

analysis = NormalIndPower()
n_per_arm = analysis.solve_power(effect_size=effect, alpha=0.05,
                                 power=0.80, ratio=1.0, alternative="larger")
print(f"Effect size (Cohen's h): {effect:.3f}")
print(f"Required n per arm     : {int(np.ceil(n_per_arm)):,}")

# What power did our ACTUAL trial have given its size?
import numpy as np
achieved = analysis.power(effect_size=effect, nobs1=8000, alpha=0.05,
                          ratio=1.0, alternative="larger")
print(f"Power at n=8000/arm    : {achieved:.2f}")
```

## Hands-on Lab 4 — Analyse the SMS-Reminder A/B Test

| | |
|---|---|
| **Objective** | Test whether SMS reminders reduce no-shows, report the effect size and CI of the difference, compute the trial's power, and correct a multiple-testing trap across regions |
| **Duration** | 50 minutes |
| **Setup** | `lab4_start.ipynb`; `data/clinic_visits.csv`; `scipy statsmodels pandas` |

**Instructions & tasks**

1. *(6 min)* State `H₀`, `H₁`, and α in a markdown cell *before* touching the data. Choose one-sided vs two-sided and justify.
2. *(12 min)* Run the two-proportion z-test on `sms_reminder`. Report p, the difference, its 95% CI, the odds ratio, and the absolute percentage-point reduction.
3. *(8 min)* Interpret in plain language: is the effect statistically significant? Practically important? Which sentence would you put in a ministerial brief?
4. *(10 min)* Power: what `n` per arm detects a 3pp drop at 80% power? What power did the observed trial size actually have?
5. *(10 min)* Multiple-testing trap: test the reminder effect *separately within each region* (13 tests). Count how many hit p < 0.05 naively, then apply Benjamini–Hochberg. Discuss which "regional effects" survive.
6. *(4 min)* Write a 4-line recommendation, explicitly separating "reminders work" from "roll out everywhere."

**Expected output**
```
H0: p_reminder = p_control ; H1: p_reminder < p_control ; alpha = 0.05 (one-sided)
Control 0.211 | Reminder 0.152 | diff -0.059 [95% CI -0.067, -0.051]
z = -13.8, p = 2e-43  | odds ratio 0.67 | absolute reduction 5.9 pp  -> real AND large
Power: need ~2,900/arm for 3pp @80%; observed trial power >0.99
Regions naive p<0.05: 9/13 ; after Benjamini-Hochberg: 7/13 survive
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| p is 0.0 exactly | Underflow at huge z | Report as `< 1e-16`; the effect size is what matters |
| Effect "significant but tiny" for region×no-show | Large-n significance | Report Cramér's V / OR; significance ≠ importance |
| One-sided vs two-sided confusion | Direction not pre-stated | Fix `H₁` in step 1 and stick to it |
| All 13 regions "significant" | No multiple-testing control | Apply Benjamini–Hochberg; compare survivors |

**Instructor notes.** Insist on step 1 (hypotheses *before* data) — it is the discipline that prevents p-hacking, and doing it on paper makes the lesson physical. The multiple-testing step reliably surprises: naive counting inflates the "number of special regions." Keep the before/after BH table on screen. Fast finishers: simulate peeking (test daily, stop at first p<0.05) and measure the inflated false-positive rate — a direct Module 7 bridge.

## Mini Exercises

1. **Interpretation.** A test returns p = 0.02. Write the correct one-sentence meaning and two common wrong ones.
2. **Test choice.** For each: (a) wait time before vs after a new triage protocol at the *same* clinics; (b) no-show rate in two independent clinic groups; (c) association between chronic-condition and no-show. Name the test.
3. **Effect size.** Two groups: mean waits 22 and 19 min, pooled SD 11. Compute Cohen's d and classify it. Is a "significant" 3-min difference operationally meaningful?
4. **Power.** Your trial is underpowered and returns p = 0.09. What can and cannot you conclude?
5. **Debugging exercise.** A teammate ran daily tests on a live A/B experiment and stopped when p first hit 0.048, declaring success. Explain precisely why the reported 5% error rate is wrong, and propose the fix.

## Case Study — Did the Reminder Campaign Actually Work?

**Scenario.** A national SMS-reminder pilot ran for three weeks. The operations team, watching a live dashboard, declared success mid-trial and wants immediate national rollout at a recurring per-message cost.

**Business context.** Rollout costs scale to millions of messages annually. A false positive wastes budget; a false negative leaves a working intervention on the shelf. Leadership wants a yes/no *and* a magnitude.

**Technical challenge.** Determine whether the effect is real and large enough to justify cost, whether the mid-trial "win" was peeking-inflated, and whether the effect is uniform or concentrated in a targetable subgroup (long lead-time patients).

**Constraints.** The dashboard-peeking already happened; the analysis must retrospectively assess validity; the recommendation must give a cost-justified target, not a blanket rollout.

**Solution approach.** (1) Analyse the full pre-registered sample once, reporting effect size + CI, not just p; (2) show how the day-6 peek would have looked and why it was not yet trustworthy; (3) segment by lead time to reveal where the effect concentrates; (4) recommend targeted rollout with a projected no-show reduction and its uncertainty.

**Discussion questions.**
1. How do you separate "the reminder works" from "roll it out to everyone"?
2. What does the CI of the difference add over the p-value for a budget decision?
3. If the effect is concentrated in long-lead-time patients, how does that change the policy and its cost?
4. How would you design the *next* trial to avoid the peeking problem entirely?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Hypotheses pre-stated | Rigour | `H₀/H₁/α` written before analysis | Notebook order |
| Correct test choice | Correctness | Welch/z/chi-square matched to data | Lab review |
| Effect size reported | Completeness | Always paired with p-value | Auto-check |
| p-value interpretation | Rigour | No probability-of-null error | Quiz |
| Multiple-testing control | Rigour | BH/Bonferroni applied across regions | Lab output |
| Power analysis | Correctness | `n` within rounding of key | Auto-check |

**Example benchmark table:**

| Analysis | p-value | Effect size | Decision-relevant? |
|---|---|---|---|
| SMS vs control (national) | 2e-43 | OR 0.67; −5.9 pp | Yes — real and large |
| Region × no-show | 3e-40 | Cramér's V 0.06 | Significant but small |
| SMS × long-lead subgroup | 5e-31 | −9.1 pp | Yes — the target |

## Required Visuals and Training Assets

### Diagrams
1. **NHST decision matrix** — *Purpose:* fix Type I/II errors and power. *Elements:* the 2×2 truth-vs-decision grid with α, β, power labelled and a false-alarm/missed-detection caption. *Style:* clean 2×2, colour-coded.
2. **p-value under the null** — *Purpose:* show p as tail area. *Elements:* null sampling distribution with the observed statistic and shaded tail; a callout of the correct verbal meaning. *Style:* annotated density.
3. **Significance vs importance quadrant** — *Purpose:* the module's thesis. *Elements:* 2×2 of (significant?) × (large effect?) with real Mawid examples in each cell. *Style:* quadrant with examples.

### Images (screenshots)
1. **A/B test output** — z, p, difference CI, odds ratio together; *why:* the reporting standard.
2. **Power curve** — power vs `n` per arm with the 80% line; *why:* trial planning.
3. **BH multiple-testing table** — naive vs corrected survivors across regions; *why:* the multiple-testing lesson.

### Simulations
1. **Peeking inflates error** — *Setup:* simulate an A/A test (no true effect), test daily, stop at first p<0.05. *Expected:* far more than 5% "wins." *Learning objective:* why peeking is illegitimate.
2. **Power builder** — *Setup:* vary effect size and `n`; watch power. *Expected:* power rises with both. *Learning objective:* underpowered studies waste effort.

### Interactive Activities
- **"Significant or important?" card sort (10 min):** results with p and effect size; teams sort into act / ignore / get-more-data.
- **Hypothesis-writing drill (8 min):** turn five business questions into `H₀/H₁/α`.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread (has `sms_reminder`) | CSV | ~50,000 rows | A/B test, chi-square |
| `ab_daily_log.csv` | Synthetic day-by-day accrual of the trial | CSV | 21 rows | Peeking simulation |

### Demo Requirements
- **Instructor demo:** run the A/B test end to end, then show the peeking simulation's inflated false-positive rate.
- **Student demo:** one pair defends "significant but not important" for the region×no-show result.
- **Expected outputs:** a correctly framed, effect-sized, multiple-testing-aware A/B analysis.

---

# Module 5 — Correlation, Causation, and Confounding

## Module Overview

**Purpose.** Modules 3 and 4 taught participants to *measure* differences and test them. This module teaches the hardest and most consequential judgement in all of statistics: deciding whether a measured association *means* what it appears to mean. Participants learn to quantify association (Pearson, Spearman), to recognise when a correlation is real but misleading, and — the module's centre of gravity — to identify and adjust for **confounders**, including the spectacular reversal known as Simpson's paradox. This is the difference between "clinics with more SMS reminders have higher no-shows" (a real correlation, catastrophically misread) and the truth underneath it.

**Business relevance.** Nearly every expensive policy mistake in a data-driven organisation is a confounding error dressed as an insight. A ministry sees that a programme correlates with worse outcomes and cancels it — not realising the programme was deliberately targeted at the hardest cases (confounding by indication). In the Mawid golden thread, a naive analyst will find that clinics sending *more* reminders have *higher* no-show rates and conclude reminders backfire. The real story: reminders were rolled out first to the highest-no-show clinics. Region and baseline risk confound the raw comparison. A data scientist who cannot spot this will confidently recommend cancelling an intervention that actually works — the exact failure Module 4 tried to prevent, now hiding one level deeper.

**Industry use cases.**
- A health authority adjusts hospital mortality comparisons for case-mix before publishing league tables, so hospitals taking sicker patients are not falsely branded as worse.
- A bank separates "customers who used the new app churn more" (correlation) from the confounder (the app was pushed to already-dissatisfied customers).
- An education programme evaluates outcomes stratified by prior attainment to avoid crediting or blaming a policy for selection effects.

**Expected competencies.** After this module a participant can compute and interpret Pearson and Spearman correlation and know when each is appropriate, articulate why correlation does not imply causation and name the specific alternative explanations, define and detect a confounder, reproduce and resolve a Simpson's-paradox reversal by stratification, and read a simple causal DAG well enough to decide what to adjust for — and, crucially, what *not* to adjust for.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Compute and interpret Pearson and Spearman correlation and choose between them | → LO5 |
| 5.2 | Explain why correlation ≠ causation and enumerate the alternative explanations | → LO5 |
| 5.3 | Define, detect, and adjust for a confounding variable by stratification | → LO4, LO5 |
| 5.4 | Reproduce and resolve a Simpson's-paradox reversal on real data | → LO5 |
| 5.5 | Read a causal DAG to choose an adjustment set (and avoid collider bias) | → LO4, LO5 |

## Technical Content

### 1. Measuring association: Pearson, Spearman, and their traps

**Pearson's correlation `r`** measures *linear* association on a −1..+1 scale. It is the right tool when the relationship is roughly straight-line and both variables are continuous and not too skewed. Its two famous weaknesses drive most misuse: it only sees *linear* structure (a perfect U-shaped relationship can have `r ≈ 0`), and it is sensitive to outliers and skew — a handful of extreme wait times can inflate or mask a correlation.

**Spearman's `ρ`** correlates the *ranks* rather than the raw values. It captures any *monotonic* relationship (not just linear), is robust to outliers, and is the honest default for skewed variables like `wait_time_min` or for ordinal data. The teaching rule for the golden thread: because wait time is right-skewed (Module 2), report **Spearman** for anything involving it unless you have first transformed to symmetry.

The non-negotiable habit: **always plot the scatter before trusting a correlation coefficient.** Anscombe's quartet — four datasets with identical `r = 0.816` but wildly different shapes (one linear, one curved, one outlier-driven, one a single leverage point) — is the canonical demonstration, and it is worth showing live every single delivery. A correlation coefficient reported without a scatterplot is an assertion, not evidence.

### 2. Why correlation is not causation — the alternative explanations

When `X` and `Y` move together, causation `X → Y` is only one of several explanations, and usually not the first one to rule out:

- **Reverse causation** `Y → X`: wait times and staffing correlate — but does long waiting cause more staff, or do busy (well-staffed) clinics also have long queues?
- **Confounding** `X ← Z → Y`: a third variable drives both. Reminders and no-shows correlate because *baseline clinic risk* drives both the decision to send reminders and the no-show rate.
- **Selection / collider bias**: conditioning on a common effect of `X` and `Y` creates a spurious association where none existed.
- **Coincidence**: with enough variables tested, some will correlate by chance (the spurious-correlations problem; link back to multiple testing, Module 4).

The practitioner's discipline is to treat "they correlate" as the *beginning* of an investigation, never the conclusion. The question is always: *what else could produce this pattern, and how would I rule it out?*

### 3. Confounding: the central threat to observational claims

A **confounder** `Z` is a variable that is (a) associated with the exposure `X`, and (b) an independent cause of the outcome `Y`, and (c) *not* on the causal path between them. When a confounder is ignored, the crude association between `X` and `Y` is biased — sometimes mildly, sometimes to the point of reversing sign.

In the Mawid thread the archetype is: `X` = received SMS reminder, `Y` = no-show, `Z` = baseline clinic/patient risk. High-risk clinics were prioritised for reminders, so `Z → X` (risk drives who got reminders) and `Z → Y` (risk drives no-shows). The crude comparison of reminded vs non-reminded patients mixes the reminder's true (protective) effect with the fact that reminded patients were higher-risk to begin with. The fix is to **compare like with like** — adjust for `Z` — via stratification (subsection 4) or regression (Module 6).

The distinction participants must internalise: **a confounder must be adjusted for; a mediator must not.** If reminders reduce no-shows *by* prompting patients to reschedule (`X → rescheduled → Y`), then "rescheduled" is a mediator on the causal path, and controlling for it would hide the very effect you are trying to measure. Deciding which is which is not a statistical computation — it is a causal-structure judgement (subsection 5).

### 4. Simpson's paradox: when the aggregate lies

**Simpson's paradox** is confounding at its most dramatic: an association that holds in every subgroup *reverses* when the subgroups are pooled. The classic mechanism is unequal group sizes combined with a lurking variable.

For the golden thread: suppose in *both* urban and rural clinics, reminded patients no-show *less* than non-reminded patients. Yet in the pooled data, reminded patients no-show *more*. How? Reminders were concentrated in rural clinics, which have higher baseline no-shows for reasons unrelated to reminders (distance, transport). The pooling lets the rural baseline dominate, flipping the sign. Stratifying by clinic type restores the truth: the reminder helps in each stratum.

The resolution is always the same: **find the stratifying variable, compute the effect within strata, and combine with appropriate weighting** (a directly standardised or Mantel–Haenszel-style adjusted estimate). The lesson participants carry forever: an aggregate number can be the exact opposite of every group it is built from, and the only defence is to ask "compared to whom, holding what constant?"

### 5. Causal graphs (DAGs): deciding what to adjust for

A **directed acyclic graph** encodes causal assumptions as arrows between variables. It is not fitted from data — it is drawn from domain knowledge — and its payoff is a rule for *which variables to adjust for*:

- **Confounder** (common cause, `X ← Z → Y`): **adjust** — it opens a spurious "back-door" path.
- **Mediator** (`X → M → Y`): **do not adjust** if you want the total effect — adjusting removes part of the real effect.
- **Collider** (common effect, `X → C ← Y`): **do not adjust** — conditioning on it *creates* a spurious association (collider/selection bias).

The single most common sophisticated error is "controlling for everything available." Throwing every column into a regression can *introduce* bias by conditioning on a collider or a mediator. The DAG discipline — draw the assumed structure, identify the minimal adjustment set that blocks all back-door paths, adjust for exactly that — is what separates defensible causal claims from kitchen-sink modelling. This module teaches DAG reading at an operational level; the Specialist module SDA-DSC-213 formalises it.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. Reporting Pearson `r` for a skewed or non-linear relationship (use Spearman / plot first).
2. Interpreting any correlation as causation without ruling out reverse causation and confounding.
3. Failing to check for a confounder before quoting a crude difference.
4. Being fooled by Simpson's paradox — trusting the pooled number.
5. "Controlling for everything," thereby conditioning on a mediator or collider.
6. Reading `r ≈ 0` as "no relationship" when the relationship is non-linear.

**Best practices:** plot before you correlate; state the causal question and draw the DAG before choosing an adjustment set; adjust for confounders, never for mediators or colliders; when in doubt, stratify and look at the subgroup pattern; report both crude and adjusted estimates and explain the gap.

**Real-world example (narrate, 5 min):** A regional directorate published clinic no-show "performance" and flagged the eight worst clinics for intervention. Six of the eight were the clinics that had *volunteered early* for the reminder programme — precisely because they already had the worst no-shows. The crude ranking conflated "high baseline risk" with "reminder made it worse." When an analyst stratified by baseline risk band, the reminder was protective in every band; the directorate had been about to punish the clinics doing the most to fix the problem. One stratification table reversed the entire policy conclusion.

## Code Examples

### Correlation done honestly: Pearson vs Spearman, with a plot-first discipline

```python
# module5/correlation.py
"""Association between clinic wait time and no-show rate -- measured two ways."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")

# Aggregate to clinic level: mean wait vs no-show rate
clinic = (df.groupby("clinic_id")
            .agg(mean_wait=("wait_time_min", "mean"),
                 no_show_rate=("no_show", "mean"),
                 n=("no_show", "size"))
            .query("n >= 30"))          # ignore tiny clinics (noisy)

r, p_r   = stats.pearsonr(clinic["mean_wait"], clinic["no_show_rate"])
rho, p_s = stats.spearmanr(clinic["mean_wait"], clinic["no_show_rate"])

print(f"Pearson  r   = {r:+.3f}  (p={p_r:.1e})  <- assumes linear, sensitive to skew")
print(f"Spearman rho = {rho:+.3f}  (p={p_s:.1e})  <- monotonic, robust -> report this")

# ALWAYS look at the scatter before trusting either number.
# import matplotlib.pyplot as plt
# plt.scatter(clinic["mean_wait"], clinic["no_show_rate"]); plt.show()
```

### Reproducing and resolving a Simpson's-paradox reversal

```python
# module5/simpson.py
"""Show the reminder 'backfiring' in aggregate but helping in every stratum."""
import pandas as pd

df = pd.read_csv("data/clinic_visits.csv")

# CRUDE (pooled) association: reminded vs not
crude = df.groupby("sms_reminder")["no_show"].mean()
print("CRUDE no-show rate by reminder:")
print(f"  no reminder : {crude[0]:.3f}")
print(f"  reminder    : {crude[1]:.3f}   <- looks WORSE with reminders?!")

# STRATIFY by clinic_type (urban/rural) -- the confounder
strat = (df.groupby(["clinic_type", "sms_reminder"])["no_show"]
           .mean().unstack())
print("\nSTRATIFIED no-show rate (reminder helps in EACH stratum):")
print(strat.round(3))

# Why the reversal: reminders were concentrated where baseline risk is high
mix = pd.crosstab(df["clinic_type"], df["sms_reminder"], normalize="index")
print("\nReminder allocation by clinic type (the confounding mechanism):")
print(mix.round(2))
```

### Confounder adjustment by direct standardisation

```python
# module5/adjust.py
"""Adjusted reminder effect: weight each stratum equally-fairly, not by who got reminded."""
import numpy as np
import pandas as pd

df = pd.read_csv("data/clinic_visits.csv")
strata = "risk_band"                      # baseline-risk quartile, the confounder

# Within-stratum reminder effect, then combine using the OVERALL stratum sizes
# (direct standardisation) so allocation imbalance cannot drive the result.
rows = []
for band, g in df.groupby(strata):
    r1 = g.loc[g.sms_reminder == 1, "no_show"].mean()
    r0 = g.loc[g.sms_reminder == 0, "no_show"].mean()
    w  = len(g) / len(df)                 # standard population weight
    rows.append((band, r0, r1, r1 - r0, w))

adj = pd.DataFrame(rows, columns=["band", "rate_ctl", "rate_rem", "diff", "weight"])
crude_diff = (df.loc[df.sms_reminder == 1, "no_show"].mean()
              - df.loc[df.sms_reminder == 0, "no_show"].mean())
adjusted_diff = np.average(adj["diff"], weights=adj["weight"])

print(adj.round(3).to_string(index=False))
print(f"\nCrude    difference (rem - ctl): {crude_diff:+.4f}   (confounded)")
print(f"Adjusted difference (standardised): {adjusted_diff:+.4f}   (reminder helps)")
```

## Hands-on Lab 5 — Uncover the Confounder

| | |
|---|---|
| **Objective** | Reproduce a Simpson's-paradox reversal in the Mawid data, identify the confounder, and produce a confounder-adjusted estimate of the reminder effect that survives scrutiny |
| **Duration** | 50 minutes |
| **Setup** | `lab5_start.ipynb`; `data/clinic_visits.csv`; `numpy pandas scipy matplotlib`; `git checkout lab5-start` |

**Instructions & tasks**

1. *(6 min)* Compute the **crude** no-show rate for reminded vs non-reminded patients. Observe that reminders appear to *increase* no-shows. Write down, before analysing further, at least two possible confounders.
2. *(12 min)* Stratify by `clinic_type` (urban/rural), then by `risk_band`. Show the reminder effect *within* each stratum. Confirm the sign flips versus the crude number — a genuine Simpson's reversal.
3. *(8 min)* Demonstrate the mechanism: cross-tabulate reminder allocation against the confounder. Explain in two sentences *why* the pooling reverses the sign.
4. *(12 min)* Produce a **direct-standardised** adjusted difference (weight strata by overall size). Report crude vs adjusted side by side and state which you would defend to leadership.
5. *(8 min)* Draw (on paper or in markdown) the DAG: `risk_band → reminder`, `risk_band → no_show`, `reminder → no_show`. Identify the confounder, confirm `risk_band` is the minimal adjustment set, and name one variable you should *not* adjust for and why (e.g., a mediator like `rescheduled`).
6. *(4 min)* Write a 3-sentence conclusion: does the reminder help, and what did adjustment change?

**Expected output**
```
CRUDE   no-show: no-reminder 0.152 | reminder 0.211   -> reminders look HARMFUL
By clinic_type: urban  rem 0.13 vs ctl 0.16  | rural rem 0.22 vs ctl 0.27  -> HELPS in both
Allocation: 78% of rural patients reminded vs 24% urban -> imbalance drives the reversal
Adjusted (standardised) difference: -0.048  (reminder REDUCES no-shows ~4.8pp)
DAG: adjust for risk_band (confounder); do NOT adjust for 'rescheduled' (mediator)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| No reversal appears | Stratifying on a non-confounder | Use `clinic_type` / `risk_band`, which drive both allocation and outcome |
| Adjusted = crude | Weighted by treated counts, not overall | Standardise to the *total* stratum sizes, not the reminded subset |
| "Adjust for everything" instinct | Added a mediator/collider | Draw the DAG; adjust only the back-door confounder |
| Sign flips again after adjustment | Over-stratified (empty cells) | Coarsen `risk_band`; ensure each stratum has both arms with adequate `n` |

**Instructor notes.** The emotional beat is task 2: participants watch a "harmful" intervention become helpful once they hold risk constant. Keep the crude number and the stratified table on screen together. Fast finishers: compute a Mantel–Haenszel adjusted odds ratio and compare it to the direct-standardised difference; it previews the regression adjustment in Module 6.

## Mini Exercises

1. **Concept.** In one sentence each, distinguish a confounder from a mediator from a collider, using the reminder→no-show example.
2. **Compute.** For the clinic-level data, report both Pearson and Spearman for `mean_wait` vs `no_show_rate`. They differ noticeably — which do you trust and why?
3. **Reasoning.** "Clinics with more staff have longer waits." Give a reverse-causation and a confounding explanation, and how you'd distinguish them.
4. **DAG.** Draw the DAG for: `distance_to_clinic → reminder_signup`, `distance_to_clinic → no_show`, `reminder → no_show`. What is the minimal adjustment set?
5. **Debugging exercise.** A colleague "controls for everything" and adds `rescheduled` (whether the patient rebooked after the reminder) to the model; the reminder effect vanishes. Explain why this is wrong and what they measured instead.

## Case Study — The Reminder That "Made No-Shows Worse"

**Scenario.** A programme dashboard shows that clinics sending more SMS reminders have *higher* no-show rates. An executive proposes pausing the reminder programme to "stop wasting money on something that backfires."

**Business context.** The reminder programme costs several million SAR-equivalent annually and is a flagship access initiative. Cancelling it on a spurious correlation would remove a working intervention and embarrass the sponsoring directorate; keeping a genuinely useless programme would waste budget. The stakes make the causal question, not the correlation, the real deliverable.

**Technical challenge.** Show convincingly that the positive crude correlation is a confounding artefact (reminders were targeted at high-risk clinics), and produce a defensible adjusted estimate of the reminder's true effect.

**Constraints.** The audience distrusts "academic" adjustments; the argument must be visual and intuitive (a stratified table, not a regression table); the recommendation must be decisive.

**Solution approach (facilitate).** (1) Reproduce the alarming crude correlation; (2) reveal the allocation imbalance (who got reminders); (3) stratify to show the reminder helps within every risk band (Simpson's reversal); (4) present the standardised adjusted effect; (5) recommend *continuing* the programme, with a note to randomise the next rollout so future evaluation needs no adjustment.

**Discussion questions.**
1. Why does targeting reminders at high-risk clinics create a positive crude correlation with no-shows?
2. How would you explain Simpson's paradox to a non-technical executive in 30 seconds?
3. What single design change (Module 4/SDA-DSC-213) would make this adjustment unnecessary next time?
4. When is a crude comparison actually the honest one, and when is adjustment itself the manipulation?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Correlation choice | Correctness | Spearman used for skewed/non-linear | Lab review |
| Confounder identification | Reasoning | Names a valid confounder + mechanism | Exercise |
| Simpson reversal reproduced | Skill | Sign flips crude→stratified, shown on data | Lab output |
| Adjusted estimate | Correctness | Direct-standardised, within rounding of key | Auto-check |
| DAG adjustment set | Judgement | Adjusts confounder, not mediator/collider | Lab notes |

**Example benchmark table:**

| Estimate | Value | Interpretation |
|---|---|---|
| Crude reminder difference | +0.059 | Confounded — reminders look harmful |
| Stratified (urban) | −0.03 | Reminder helps |
| Stratified (rural) | −0.05 | Reminder helps |
| Adjusted (standardised) | −0.048 | The defensible effect |

## Required Visuals and Training Assets

### Diagrams
1. **Correlation ≠ causation map** — *Purpose:* enumerate the alternative explanations. *Elements:* four mini-DAGs (direct, reverse, confounded, collider) for the same `X–Y` correlation. *Style:* four-panel node-arrow, colour-coded.
2. **Confounder vs mediator vs collider** — *Purpose:* the adjustment rule at a glance. *Elements:* three DAGs with "adjust / don't adjust / don't adjust" verdicts and the reminder example on each. *Style:* triptych, printable A4.
3. **Simpson's paradox geometry** — *Purpose:* make the reversal visual. *Elements:* subgroup regression lines all sloping one way, the pooled line sloping the other, with group sizes shown. *Style:* annotated scatter with overlaid lines.

### Images (screenshots)
1. **Crude vs stratified table** — the reminder effect flipping sign; *why:* the module's headline result.
2. **Anscombe's quartet** — four plots, one `r`; *why:* plot-before-correlate discipline.
3. **Allocation cross-tab** — who received reminders by risk band; *why:* exposes the confounding mechanism.

### Simulations
1. **Confounding dial** — *Setup:* slider on how strongly `Z` drives allocation; watch the crude effect diverge from the true effect. *Expected:* stronger confounding → larger crude bias. *Learning objective:* confounding magnitude is a property of allocation, not sample size.
2. **Collider-bias generator** — *Setup:* condition on a common effect and watch a null association appear. *Expected:* spurious correlation emerges. *Learning objective:* adjusting for the wrong variable *creates* bias.

### Interactive Activities
- **"Confounder, mediator, or collider?" card sort (10 min):** 10 variable triples sorted with an adjust/don't-adjust verdict.
- **Simpson's-paradox reveal poll (5 min):** class predicts the pooled sign from the subgroup signs; the miss is the lesson.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread (has `clinic_id`, `clinic_type`, `risk_band`) | CSV | ~50,000 rows | Confounding and Simpson's paradox |
| `clinic_reference.csv` | Course team (clinic type, baseline risk) | CSV | ~120 rows | Stratification keys |

### Demo Requirements
- **Instructor demo:** reproduce the Simpson's reversal live and resolve it by stratification in under 8 minutes.
- **Student demo:** one pair defends "continue the programme" using only a stratified table.
- **Expected outputs:** a reproduced reversal, an adjusted estimate, and a correct DAG-based adjustment set.

---

# Module 6 — Linear and Logistic Regression

## Module Overview

**Purpose.** Regression is where everything in the course converges: it estimates an effect (Module 3) while adjusting for confounders (Module 5), tests it (Module 4), and predicts an outcome — all in one framework. This module teaches participants to build, interpret, and *diagnose* the two workhorses of applied statistics: **linear regression** for a continuous outcome (wait time) and **logistic regression** for a binary outcome (no-show). The emphasis is not on fitting — `statsmodels` fits in one line — but on reading coefficients correctly, checking assumptions honestly, and knowing when a model's number can and cannot be trusted.

**Business relevance.** A regression coefficient is the most common quantitative claim in a policy document: "each additional day of lead time raises no-show odds by 4%, holding region and age constant." That single adjusted, interpretable number is what decision-makers actually use — and it is only trustworthy if the model's assumptions hold and the confounders (Module 5) are in the specification. For Mawid, logistic regression turns the whole investigation into an operational tool: a per-patient no-show probability that can drive targeted reminders, and an odds ratio for each driver that tells the Ministry *which levers move no-shows*. Linear regression does the same for wait time, quantifying which clinic factors add minutes to the queue.

**Industry use cases.**
- A ministry models no-show probability per appointment to prioritise reminder capacity where it changes the most outcomes.
- An insurer models claim cost (linear) and claim occurrence (logistic) on the same customer features.
- A regulator uses a logistic model's coefficients — not a black box — because the decision must be *explainable* and auditable.

**Expected competencies.** After this module a participant can specify and fit OLS and logistic models in `statsmodels`, interpret coefficients (including the log-odds→odds-ratio transform), read `R²` and pseudo-`R²` for what they do and don't say, check the linear-model assumptions with residual diagnostics, evaluate a classifier with ROC/AUC and a calibration curve, and choose the right model family for an outcome's type.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Specify and fit OLS regression and interpret coefficients and `R²` | → LO4 |
| 6.2 | Check linear-regression assumptions via residual and influence diagnostics | → LO4, LO5 |
| 6.3 | Fit logistic regression and interpret coefficients as odds ratios | → LO4 |
| 6.4 | Evaluate a classifier with ROC/AUC, threshold choice, and calibration | → LO4 |
| 6.5 | Use regression to obtain a confounder-adjusted effect and state its assumptions | → LO4, LO5 |

## Technical Content

### 1. The linear model: specification and coefficient interpretation

Ordinary least squares fits `y = β₀ + β₁x₁ + … + βₖxₖ + ε` by minimising the sum of squared residuals. The interpretation that participants must state fluently: **`βⱼ` is the expected change in `y` for a one-unit increase in `xⱼ`, holding all other predictors fixed.** That "holding fixed" clause is exactly the confounder adjustment from Module 5 — putting `risk_band` in the model estimates the reminder effect *adjusted* for baseline risk, without manual stratification.

Two interpretation subtleties earn their teaching time. **Categorical predictors** enter as dummy variables against a reference level, so each coefficient is a contrast *versus that reference* (e.g., "Makkah region adds 3.1 minutes versus Riyadh"). **Units and centering** matter: the intercept is the fitted value when every predictor is 0, which is often meaningless (age 0) until predictors are centred. Teaching participants to center continuous predictors makes the intercept interpretable and coefficients comparable.

### 2. Model fit and what R² does — and does not — tell you

`R²` is the fraction of outcome variance the model explains (0–1). It is useful but routinely over-read. Three cautions:

- **`R²` always rises when you add predictors**, even useless ones; use **adjusted `R²`** to compare models of different size.
- **High `R²` does not mean the model is correct** — a badly mis-specified model can have high `R²`; a correct causal model can have modest `R²` if the outcome is inherently noisy (no-shows are). Explaining 20% of no-show variance can still yield a decision-useful, valid effect estimate.
- **`R²` says nothing about whether assumptions hold** or whether coefficients are unbiased. A model can fit the sample well and still mislead about effects if a confounder is omitted.

The reframing participants need: for *prediction*, chase out-of-sample accuracy (Module 7's resampling); for *explanation*, a valid, well-specified coefficient matters more than a big `R²`.

### 3. Linear-regression assumptions and residual diagnostics

OLS coefficients are trustworthy only when its assumptions roughly hold. The diagnostic checklist:

- **Linearity:** the relationship is actually linear — check a *residuals-vs-fitted* plot for curvature. Curvature means a transform or a non-linear term is needed.
- **Homoscedasticity:** residual variance is constant — a funnel shape (variance growing with fitted value) signals heteroscedasticity, common with skewed outcomes like wait time, and calls for robust (HC) standard errors or a log transform.
- **Normality of residuals:** matters mainly for small-sample inference — check a Q–Q plot; the CLT rescues large samples.
- **Independence:** residuals are uncorrelated — clustered data (multiple visits per clinic) violates this and needs clustered standard errors.
- **No high-leverage distortion:** a few extreme points can dominate the fit — check Cook's distance and leverage.

The teaching rule: **for a right-skewed positive outcome like `wait_time_min`, model `log(wait_time_min)` or use robust standard errors** — fitting raw wait time with plain OLS violates homoscedasticity and gives over-confident intervals exactly in the tail where operational risk lives (a callback to Module 1's lognormal lesson).

### 4. Logistic regression: modelling a probability

When the outcome is binary (`no_show ∈ {0,1}`), linear regression is wrong — it predicts probabilities outside [0,1] and has structurally non-constant variance. **Logistic regression** models the *log-odds* as linear: `log(p/(1−p)) = β₀ + β₁x₁ + …`, so the fitted probability passes through the logistic (S-shaped) function and stays in [0,1]. It is fit by maximum likelihood — the MLE principle named back in Module 3.

Coefficient interpretation is the module's key skill: **`exp(βⱼ)` is the odds ratio** for a one-unit increase in `xⱼ`. `exp(β) = 0.67` means the odds of a no-show fall by 33% per unit, holding other predictors fixed — the exact same odds ratio participants met as an effect size in Module 4, now adjusted for covariates. A one-unit change on the *log-odds* scale is constant; on the *probability* scale it is not (the same coefficient moves probability more in the middle than at the extremes), which is why practitioners report odds ratios, not "probability points per unit."

### 5. Evaluating a classifier: ROC/AUC, thresholds, and calibration

A fitted logistic model outputs probabilities; turning them into decisions and judging them needs the right metrics:

- **Discrimination — ROC curve and AUC:** the ROC traces true-positive vs false-positive rate across all thresholds; **AUC** is the probability the model ranks a random no-show above a random show (0.5 = coin flip, 1.0 = perfect). AUC is threshold-free and the standard summary of ranking quality.
- **Threshold choice is a business decision, not a default 0.5:** the reminder capacity (how many patients you can text) sets the operating point. Precision/recall at the chosen threshold, and the confusion matrix, express the real trade-off — miss real no-shows vs waste reminders on patients who'd attend anyway.
- **Calibration — the most-neglected check:** a model can rank well (good AUC) yet output probabilities that are systematically wrong (says 30% when the true rate is 15%). A **calibration curve** (predicted vs observed frequency, in bins) reveals this. For any decision that uses the *probability itself* — expected-no-show counts, capacity planning — calibration matters as much as AUC.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. Interpreting a coefficient without the "holding others fixed" clause.
2. Fitting raw skewed wait time with plain OLS and trusting the tail intervals.
3. Reporting `R²` as if high = correct or low = useless.
4. Reading logistic coefficients as probability changes instead of odds ratios.
5. Judging a classifier by accuracy alone on imbalanced no-shows (18% positives — a "never no-show" model is 82% accurate and useless).
6. Ignoring calibration when the probability itself drives the decision.

**Best practices:** plot residuals before trusting an OLS model; log-transform or use robust SEs for skewed outcomes; report odds ratios with CIs for logistic models; evaluate classifiers with AUC *and* calibration, at a business-chosen threshold; put the Module-5 confounders in the specification and say so.

**Real-world example (narrate):** A clinic network built a no-show model with 0.79 AUC and deployed it to send reminders to the top-scoring 20%. It underperformed. The model *ranked* well but was badly *calibrated* — it inflated probabilities for young urban patients, so reminders piled onto a group that mostly attended anyway. Recalibrating (a one-line isotonic step) and choosing the threshold from actual reminder capacity redirected texts to genuinely high-risk patients and roughly doubled the no-shows prevented per message. Same discrimination, correct calibration, a very different outcome.

## Code Examples

### Linear regression with diagnostics (wait time)

```python
# module6/linear_wait.py
"""Model wait time; interpret coefficients; CHECK assumptions before trusting them."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/clinic_visits.csv")
df["log_wait"] = np.log(df["wait_time_min"].clip(lower=1))  # skew fix (Module 1/2)

# Model log-wait on clinic factors; C() marks categoricals (dummy-coded)
model = smf.ols(
    "log_wait ~ C(region) + staff_on_shift + is_peak_hour + patient_age",
    data=df).fit(cov_type="HC3")            # robust SEs guard heteroscedasticity

print(model.summary().tables[1])            # coefficients, robust SEs, CIs
print(f"R-squared: {model.rsquared:.3f}  Adj R-squared: {model.rsquared_adj:.3f}")

# Diagnostics: residuals-vs-fitted (linearity/homoscedasticity) and influence
fitted, resid = model.fittedvalues, model.resid
print("Residual mean (~0 expected):", round(resid.mean(), 4))
infl = model.get_influence()
cooks = infl.cooks_distance[0]
print("High-influence rows (Cook's D > 4/n):", int((cooks > 4/len(df)).sum()))
# import matplotlib.pyplot as plt; plt.scatter(fitted, resid)  # look for a funnel/curve
```

### Logistic regression: odds ratios for no-show drivers

```python
# module6/logistic_noshow.py
"""No-show ~ drivers; report ODDS RATIOS, adjusted for the Module-5 confounders."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/clinic_visits.csv")

logit = smf.logit(
    "no_show ~ sms_reminder + lead_time_days + prior_no_shows "
    "+ C(risk_band) + patient_age",           # risk_band adjusts for confounding
    data=df).fit(disp=False)

# Convert log-odds coefficients to odds ratios with 95% CIs
params = logit.params
conf = logit.conf_int()
odds = pd.DataFrame({
    "odds_ratio": np.exp(params),
    "ci_low":     np.exp(conf[0]),
    "ci_high":    np.exp(conf[1]),
    "p_value":    logit.pvalues,
}).round(3)
print(odds)
print("\nInterpretation: sms_reminder OR < 1 => reminders cut the ODDS of a no-show,")
print("holding lead time, prior no-shows, risk band, and age fixed.")
print(f"Pseudo R-squared (McFadden): {logit.prsquared:.3f}")
```

### Evaluating the classifier: AUC, threshold, and calibration

```python
# module6/evaluate.py
"""Discrimination (AUC), a business threshold, and CALIBRATION -- not accuracy alone."""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, confusion_matrix
from sklearn.calibration import calibration_curve
import statsmodels.formula.api as smf

df = pd.read_csv("data/clinic_visits.csv")
logit = smf.logit("no_show ~ sms_reminder + lead_time_days + prior_no_shows "
                  "+ C(risk_band) + patient_age", data=df).fit(disp=False)
p_hat = logit.predict(df)

auc = roc_auc_score(df["no_show"], p_hat)
print(f"AUC = {auc:.3f}  (0.5 = chance)")

# Threshold from CAPACITY: we can remind the top 20% highest-risk patients
threshold = np.quantile(p_hat, 0.80)
pred = (p_hat >= threshold).astype(int)
tn, fp, fn, tp = confusion_matrix(df["no_show"], pred).ravel()
print(f"At top-20% threshold: precision={tp/(tp+fp):.3f}, recall={tp/(tp+fn):.3f}")

# Calibration: are predicted probabilities honest?
frac_pos, mean_pred = calibration_curve(df["no_show"], p_hat, n_bins=10)
gap = np.abs(frac_pos - mean_pred).max()
print(f"Max calibration gap across bins: {gap:.3f}  (small = well-calibrated)")
```

## Hands-on Lab 6 — Model Wait Time and No-Show

| | |
|---|---|
| **Objective** | Fit and diagnose a linear model for wait time and a logistic model for no-show; interpret coefficients as effects and odds ratios; evaluate the classifier with AUC, a capacity-based threshold, and calibration |
| **Duration** | 50 minutes |
| **Setup** | `lab6_start.ipynb`; `data/clinic_visits.csv`; `statsmodels scikit-learn pandas numpy matplotlib`; `git checkout lab6-start` |

**Instructions & tasks**

1. *(10 min)* Fit an OLS model for `log(wait_time_min)` on region, staffing, peak-hour, and age with robust (HC3) SEs. Interpret two coefficients in plain language (one continuous, one categorical). Report adjusted `R²`.
2. *(8 min)* Diagnostics: plot residuals-vs-fitted and a Q–Q plot; flag high-influence points via Cook's distance. State whether the assumptions hold and what you'd change if not.
3. *(12 min)* Fit a logistic model for `no_show` including `sms_reminder`, `lead_time_days`, `prior_no_shows`, `C(risk_band)`, and age. Report odds ratios with CIs. Confirm the *adjusted* reminder odds ratio matches the Module-5 finding in direction.
4. *(10 min)* Evaluate: compute AUC; choose a threshold from a stated reminder capacity (top 20%); report precision/recall and the confusion matrix at that threshold.
5. *(6 min)* Calibration: plot the calibration curve and report the max bin gap. State whether the probabilities are trustworthy for capacity planning.
6. *(4 min)* Write a 4-line conclusion: which drivers move no-shows, the adjusted reminder odds ratio, and whether you'd deploy this model as-is.

**Expected output**
```
OLS log_wait: adj R2 0.34 | peak_hour +0.21 log-min (~23% longer) | +1 staff -0.06 log-min
Diagnostics: mild funnel in residuals -> HC3 SEs justified; 41 high-influence rows noted
Logit odds ratios: sms_reminder 0.68 [0.63,0.73] | +1 prior_no_show 1.9 | +7 lead days 1.28
AUC = 0.74 | top-20% threshold: precision 0.41, recall 0.46
Calibration max gap 0.03 -> well-calibrated; safe for capacity planning
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Wait-time residuals funnel out | Heteroscedasticity from skew | Model `log(wait)`; use `cov_type="HC3"` |
| Logit coefficients look tiny | Reading log-odds, not odds ratios | Exponentiate: `np.exp(params)` |
| AUC good but decisions bad | Poor calibration or 0.5 default threshold | Check calibration; set threshold from capacity |
| "Model is 82% accurate!" | Accuracy on imbalanced classes | Report AUC + precision/recall, not accuracy |
| Perfect separation warning | A predictor perfectly predicts outcome | Regularise or drop the leaking predictor |

**Instructor notes.** The two payoff moments: (1) the adjusted logistic reminder odds ratio landing near the Module-5 standardised effect — the same truth from two methods; (2) a strong-AUC-but-miscalibrated toy variant if time allows, to make the calibration lesson physical. Keep the odds-ratio table and the calibration curve on the projector. Fast finishers: add an interaction (`sms_reminder * lead_time_days`) to test whether reminders help long-lead-time patients more — the targeting insight from Module 4's case study.

## Mini Exercises

1. **Interpretation.** An OLS coefficient on `is_peak_hour` is `+0.21` for `log(wait)`. Translate to an approximate percentage change in wait time and state the "holding fixed" clause.
2. **Odds ratio.** A logistic coefficient on `prior_no_shows` is `0.64` (log-odds). Give the odds ratio and interpret it for a patient with 2 prior no-shows vs 0.
3. **Assumptions.** You fit raw `wait_time_min` (not logged) and the residuals-vs-fitted plot funnels outward. Name the violated assumption and two fixes.
4. **Evaluation.** Two no-show models: A has AUC 0.78 but calibration gap 0.12; B has AUC 0.74 and gap 0.02. Which do you deploy for capacity planning, and why?
5. **Debugging exercise.** A teammate reports "94% accuracy" for a no-show classifier and calls it excellent. Given an 18% no-show rate, explain why this is misleading and what to report instead.

## Case Study — The No-Show Model That Ranked Right but Predicted Wrong

**Scenario.** A data-science team ships a no-show logistic model with AUC 0.79 to drive the SMS-reminder queue: text the top 20% by predicted probability. After a month, no-shows barely move despite thousands of reminders sent.

**Business context.** Reminder capacity is fixed and expensive; every message spent on a patient who would have attended anyway is a message not spent on a genuine no-show. The model was supposed to make the programme efficient; instead it is spending capacity on the wrong patients.

**Technical challenge.** Diagnose why a well-*discriminating* model produces poor *decisions*, and fix it without collecting new data.

**Constraints.** No new features are available this cycle; the fix must be explainable to operations; the threshold must reflect the real message budget.

**Solution approach.** (1) Confirm good AUC but check the calibration curve — reveal systematic over-prediction for a low-risk subgroup; (2) recalibrate (isotonic/Platt) so probabilities are honest; (3) re-derive the threshold from actual capacity, not 0.5; (4) show precision/recall improve at the operating point; (5) recommend redeploy with a monitoring check on calibration drift.

**Discussion questions.**
1. How can a model rank well (high AUC) yet make poor decisions?
2. Why is 0.5 almost never the right threshold for an operational classifier?
3. When does calibration matter more than discrimination, and when the reverse?
4. What would you monitor in production to catch this failure earlier next time?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Coefficient interpretation | Correctness | States effect + "holding fixed" clause | Lab review |
| Assumption diagnostics | Rigour | Residual + influence checks performed | Lab notes |
| Odds-ratio reporting | Correctness | Exponentiated with CIs | Auto-check |
| Classifier evaluation | Completeness | AUC + threshold + calibration all reported | Lab output |
| Adjusted effect consistency | Reasoning | Logistic reminder OR agrees with M5 direction | Comparison |

**Example benchmark table:**

| Model | Key output | Value | Decision use |
|---|---|---|---|
| OLS log-wait | Adjusted R² | 0.34 | Explains queue drivers |
| Logistic no-show | Reminder odds ratio | 0.68 [0.63, 0.73] | Confirms reminder helps |
| Logistic no-show | AUC | 0.74 | Usable ranking |
| Logistic no-show | Calibration gap | 0.03 | Safe for capacity planning |

## Required Visuals and Training Assets

### Diagrams
1. **From line to S-curve** — *Purpose:* motivate logistic over linear for binary outcomes. *Elements:* a linear fit predicting probabilities <0 and >1 beside a logistic S-curve staying in [0,1]. *Style:* two-panel, annotated.
2. **Log-odds ↔ odds ratio ↔ probability** — *Purpose:* the interpretation bridge. *Elements:* a coefficient traced through `exp()` to an odds ratio and mapped onto the probability curve. *Style:* flow with a worked number.
3. **Regression diagnostic quartet** — *Purpose:* the assumption checklist. *Elements:* residuals-vs-fitted (good vs funnel vs curved), Q–Q, and a Cook's-distance plot with the rule-of-thumb line. *Style:* 2×2 panel, printable.

### Images (screenshots)
1. **`statsmodels` summary table** — coefficients, robust SEs, CIs; *why:* the reporting standard.
2. **ROC curve with AUC** — with the chosen operating point marked; *why:* threshold is a decision.
3. **Calibration curve** — predicted vs observed, well- vs poorly-calibrated; *why:* the module's headline lesson.

### Simulations
1. **Omitted-variable bias demo** — *Setup:* fit with and without a known confounder; watch the coefficient shift. *Expected:* omitting the confounder biases the effect. *Learning objective:* regression adjustment = Module-5 stratification, automated.
2. **Threshold slider** — *Setup:* move the classification threshold; watch precision/recall and the confusion matrix trade off. *Expected:* no free lunch. *Learning objective:* the operating point is a business choice.

### Interactive Activities
- **"Interpret this coefficient" relay (10 min):** teams translate five coefficients (2 OLS, 3 logistic odds ratios) into plain, correct sentences.
- **Assumption-triage clinic (10 min):** given four residual plots, teams name the violation and the fix.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread (has `lead_time_days`, `staff_on_shift`, `is_peak_hour`, `prior_no_shows`) | CSV | ~50,000 rows | Linear + logistic modelling |
| `data_dictionary.md` | Course team | Markdown | 1 page | Predictor definitions and units |

### Demo Requirements
- **Instructor demo:** fit the logistic model, exponentiate to odds ratios, and show the calibration curve in under 8 minutes.
- **Student demo:** one pair interprets their reminder odds ratio and defends their deployment threshold.
- **Expected outputs:** a diagnosed OLS model, an odds-ratio table, and an AUC + calibration evaluation.

---

# Module 7 — Simulation and Resampling Methods

## Module Overview

**Purpose.** Every analytical formula in this course — the standard error, the t-interval, the p-value — rests on assumptions that may not hold for real, skewed, clustered data. This module gives participants a second, assumption-light way to answer the same questions: **simulation and resampling.** By generating data from known models (Monte Carlo) and by resampling the data they already have (bootstrap and permutation), participants can compute confidence intervals and p-values *without* relying on a formula's fine print — and, just as importantly, they can *validate* the analytical results from Days 1–3. When the formula and the simulation agree, trust is earned; when they disagree, the gap is the lesson. This is the computational-first pedagogy the course has previewed since Day 1, now made explicit.

**Business relevance.** Real operational data breaks textbook assumptions constantly: wait times are skewed, no-shows cluster within clinics, and the quantity a decision needs (a median, a 90th percentile, a ratio of rates) often has no clean formula for its standard error at all. Resampling answers these directly. For the Mawid capstone, the bootstrap lets participants put an honest confidence interval on *any* statistic they compute — including the projected no-show reduction and its riyal value — and the permutation test lets them re-run the SMS A/B test without assuming normality. A data scientist who can bootstrap can quantify uncertainty for statistics that a classically trained analyst simply reports as bare numbers.

**Industry use cases.**
- A ministry puts a confidence interval on a *median* wait time or a 90th-percentile queue, where no simple SE formula exists.
- A product team runs a permutation test for an A/B metric with a weird distribution (revenue per user), avoiding a fragile normality assumption.
- A risk team uses Monte Carlo to propagate uncertainty through a multi-step capacity model and report the distribution of outcomes, not a single point.

**Expected competencies.** After this module a participant can generate reproducible pseudo-random data and explain the role of a seed, use Monte Carlo simulation to validate the CLT and confidence-interval coverage, construct a bootstrap confidence interval for an arbitrary statistic, run a permutation test for a difference, and articulate when resampling is trustworthy and when it fails (small samples, dependence, heavy tails).

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Generate reproducible pseudo-random data and explain seeding | → LO6 |
| 7.2 | Use Monte Carlo simulation to validate CLT and CI coverage | → LO6 |
| 7.3 | Construct bootstrap confidence intervals for arbitrary statistics | → LO2, LO6 |
| 7.4 | Run permutation tests for differences without distributional assumptions | → LO3, LO6 |
| 7.5 | Judge when resampling is valid and diagnose its failure modes | → LO5, LO6 |

## Technical Content

### 1. Pseudo-randomness, seeds, and reproducibility

Computers produce **pseudo-random** numbers: deterministic sequences that pass statistical tests for randomness but are fully reproducible given a **seed**. This is a feature, not a limitation — seeding is what makes a simulation auditable and a bootstrap result reproducible. The course convention, used since Module 1, is the modern NumPy generator API: `rng = np.random.default_rng(seed)`, *not* the legacy global `np.random.seed()`, because a passed-around generator makes reproducibility explicit and avoids hidden global state.

The integrity point participants must absorb: **report your seed, and never tune it.** Trying seeds until the bootstrap CI excludes zero is a form of p-hacking (Module 4). A defensible submission fixes one seed up front and reports whatever it produces. In the capstone, differing seeds across participants are exactly how the instructor detects copied analyses.

### 2. Monte Carlo simulation: computing by generating

**Monte Carlo** answers a question by simulating the random process many times and summarising the outcomes. Its power is that it works whenever you can *generate* from a model, even when no formula exists. The recurring pattern is three lines: (1) draw many simulated datasets from an assumed model; (2) compute the statistic of interest on each; (3) summarise the distribution of that statistic.

This is how the course *validates* its own analytical claims. The CLT (Module 2) becomes a simulation: draw samples from the skewed wait-time distribution, compute their means, watch the histogram become Normal and the spread track `σ/√n`. A confidence interval's coverage (Module 3) becomes checkable: generate 10,000 samples from a known truth, build a CI from each, and count how many contain the truth — it should be ~95%. When it is not (small `n`, Wald interval, extreme proportion), the simulation *shows* the failure the formula hid.

### 3. The bootstrap: confidence intervals for anything

The **bootstrap** is the module's centrepiece and one of the most useful ideas in applied statistics. The insight: the sample is our best proxy for the population, so **resampling from the sample (with replacement) mimics drawing new samples from the population.** The recipe for a bootstrap confidence interval of any statistic `θ̂`:

1. Resample the data with replacement to the same size `n`, thousands of times.
2. Compute `θ̂` on each resample — building the **bootstrap distribution**.
3. The interval is the empirical 2.5th–97.5th percentiles of that distribution (the **percentile bootstrap**).

Its liberating property: it needs **no formula for the standard error.** A median, a 90th-percentile wait, a ratio of no-show rates, a difference of medians, an AUC — all get honest intervals by the same three steps. For the Mawid thread this is decisive: the median wait's CI, or the projected no-show reduction's CI, would be awkward or impossible analytically but fall straight out of the bootstrap. (Note the refinements exist — BCa corrects for bias and skew — and `scipy.stats.bootstrap` implements them; the percentile method is the teachable core.)

### 4. The permutation test: hypothesis testing by shuffling

Where the bootstrap estimates *uncertainty*, the **permutation test** tests a *hypothesis* — and it is the assumption-light twin of Module 4's tests. The logic maps directly onto the null hypothesis: *if the SMS reminder had no effect, the "reminder" and "control" labels are exchangeable* — reshuffling them should produce differences just as large as the observed one, by chance alone.

The recipe:
1. Compute the observed statistic (e.g., difference in no-show rates).
2. Randomly **shuffle the group labels** thousands of times; recompute the statistic each time, building the null distribution.
3. The **p-value** is the fraction of shuffled statistics at least as extreme as the observed one.

This makes the abstract p-value from Module 4 concrete and physical: participants *see* the null distribution they are comparing against, built by shuffling their own data. It requires no normality, no equal-variance assumption, and works for any statistic — a difference of medians, a correlation, anything. When its assumptions (exchangeability under the null) hold, it is often the most defensible test available.

### 5. When resampling works — and when it lies

Resampling is powerful but not magic, and this subsection is what separates competent use from cargo-culting:

- **Small samples:** the bootstrap can only resample the values it has; from `n = 8` it cannot invent the tail, so intervals for extreme quantiles are unreliable. Resampling does not create information.
- **Dependence:** the plain bootstrap assumes independent observations. Multiple visits per clinic are *clustered*; naive resampling of rows understates uncertainty. The fix is the **cluster (block) bootstrap** — resample whole clinics, not individual rows — a direct callback to Module 2's clustering warning.
- **Heavy tails / unstable statistics:** for statistics like the maximum, or for extremely heavy-tailed data, the bootstrap distribution can be erratic; check its shape before trusting the interval.
- **Exchangeability for permutation:** the permutation test's validity rests on labels being exchangeable under the null; if the groups differ in structure (unequal cluster composition), that assumption — and the test — can break.

The meta-lesson closing the course: simulation and formula are two lenses on the same truth. Use each to check the other. A confidence interval you have both derived *and* bootstrapped, that agree, is a number you can defend to a minister.

### 6. Common mistakes, best practices, and a real-world example

**Common mistakes:**
1. Not fixing (or worse, tuning) the random seed.
2. Bootstrapping clustered data by row, understating uncertainty.
3. Trusting a bootstrap interval from a tiny sample or for an extreme quantile.
4. Too few resamples (e.g., 200) — a noisy interval; use ≥ 2,000–10,000.
5. Permuting the wrong thing (breaking a pairing that should be preserved).
6. Treating a simulation's Monte Carlo error as zero — more iterations shrink it, but it is never exactly nil.

**Best practices:** always seed and report it; match the resampling unit to the dependence structure (cluster bootstrap for clustered data); use ≥ 2,000 resamples and check the bootstrap distribution's shape; validate at least one analytical result by simulation in every analysis; state which assumptions the resampling still makes.

**Real-world example (narrate):** An analyst reported a bootstrap CI for the *mean* wait time that looked reassuringly tight, and leadership set a staffing target from its upper bound. The data had 40 clinics with dozens of visits each; the analyst bootstrapped individual visits, not clinics. A cluster bootstrap — resampling whole clinics — produced an interval nearly twice as wide, because most of the real variation was *between* clinics, not within. The naive interval had manufactured false precision; the staffing target built on it was set too tight and the clinics missed it. Matching the resampling unit to the data's structure was the whole difference.

## Code Examples

### Monte Carlo validation of confidence-interval coverage

```python
# module7/mc_coverage.py
"""Does a 95% CI really cover 95% of the time? Simulate to check the FORMULA."""
import numpy as np
from scipy import stats

rng = np.random.default_rng(seed=7)         # seeded, reported, never tuned

true_p = 0.18                                 # known no-show rate (the 'truth')
n, n_sims = 300, 10_000
covered_wald = covered_wilson = 0

for _ in range(n_sims):
    x = rng.binomial(n, true_p)              # one simulated sample
    from statsmodels.stats.proportion import proportion_confint
    lo_w, hi_w = proportion_confint(x, n, method="normal")   # Wald
    lo_s, hi_s = proportion_confint(x, n, method="wilson")   # Wilson
    covered_wald   += lo_w <= true_p <= hi_w
    covered_wilson += lo_s <= true_p <= hi_s

print(f"Wald   coverage: {covered_wald/n_sims:.3f}  (target 0.95 -- often UNDER)")
print(f"Wilson coverage: {covered_wilson/n_sims:.3f}  (target 0.95 -- holds up)")
# The simulation EXPOSES what the formula hides: Wald under-covers (Module 3).
```

### Bootstrap confidence interval for a median wait (no formula needed)

```python
# module7/bootstrap_median.py
"""95% CI for the MEDIAN wait -- a statistic with no easy SE formula."""
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/clinic_visits.csv")
waits = df["wait_time_min"].dropna().to_numpy()

# Manual percentile bootstrap (the teachable core)
rng = np.random.default_rng(2026)
boot_medians = np.array([
    np.median(rng.choice(waits, size=waits.size, replace=True))
    for _ in range(5000)
])
lo, hi = np.percentile(boot_medians, [2.5, 97.5])
print(f"Median wait      : {np.median(waits):.1f} min")
print(f"Bootstrap 95% CI : [{lo:.1f}, {hi:.1f}] min  (percentile method)")

# scipy cross-check with the bias-corrected accelerated (BCa) refinement
res = stats.bootstrap((waits,), np.median, confidence_level=0.95,
                      n_resamples=5000, method="BCa", random_state=rng)
print(f"scipy BCa 95% CI : [{res.confidence_interval.low:.1f}, "
      f"{res.confidence_interval.high:.1f}] min")
```

### Permutation test for the SMS-reminder effect (assumption-light)

```python
# module7/permutation_test.py
"""Re-run the A/B test by SHUFFLING labels -- no normality assumption (cf. Module 4)."""
import numpy as np
import pandas as pd

df = pd.read_csv("data/clinic_visits.csv")
rng = np.random.default_rng(0)

reminder = df["sms_reminder"].to_numpy()
no_show  = df["no_show"].to_numpy()

def diff_in_rates(labels):
    return no_show[labels == 1].mean() - no_show[labels == 0].mean()

observed = diff_in_rates(reminder)          # reminder minus control

# Under H0 (no effect), the labels are exchangeable -> shuffle them
n_perm = 10_000
null_diffs = np.empty(n_perm)
shuffled = reminder.copy()
for i in range(n_perm):
    rng.shuffle(shuffled)
    null_diffs[i] = diff_in_rates(shuffled)

# One-sided p: how often is a shuffled difference <= the observed (reminder lowers)?
p_value = (null_diffs <= observed).mean()
print(f"Observed diff (rem - ctl): {observed:+.4f}")
print(f"Permutation p-value       : {p_value:.4f}  (matches Module 4's z-test)")
```

## Hands-on Lab 7 — Validate Everything by Resampling

| | |
|---|---|
| **Objective** | Validate the course's analytical results by simulation: check CI coverage by Monte Carlo, bootstrap a CI for a statistic with no formula (median wait / no-show reduction), re-run the A/B test by permutation, and demonstrate a cluster-bootstrap correction |
| **Duration** | 50 minutes |
| **Setup** | `lab7_start.ipynb`; `data/clinic_visits.csv`; `numpy scipy pandas matplotlib`; `git checkout lab7-start` |

**Instructions & tasks**

1. *(8 min)* Monte Carlo: simulate 10,000 samples from a known no-show rate; confirm the Wilson CI covers ~95% and the Wald under-covers. State what this validates from Module 3.
2. *(12 min)* Bootstrap a 95% CI for the **median** wait time (percentile method), then cross-check with `scipy.stats.bootstrap` (BCa). Report both and note any difference.
3. *(10 min)* Permutation test for the SMS-reminder effect: build the null distribution by shuffling labels; report the p-value and compare it to Module 4's two-proportion z-test p-value.
4. *(12 min)* Cluster bootstrap: bootstrap the mean wait by resampling **whole clinics** vs by resampling **individual rows**. Show the cluster interval is wider and explain why (Module 2 clustering).
5. *(4 min)* Bootstrap a CI for the projected **no-show reduction** (the capstone quantity) so the capstone can quote uncertainty on its headline number.
6. *(4 min)* Write a 4-line conclusion: which analytical result each simulation confirmed, and where naive resampling would have misled.

**Expected output**
```
MC coverage: Wilson 0.949 | Wald 0.928  -> confirms Wald under-covers (Module 3)
Median wait 18.0 min: percentile CI [17.6, 18.4] | BCa CI [17.6, 18.5]  -> agree
Permutation p = 0.0001  vs z-test p = 2e-43  -> same conclusion, no normality needed
Mean wait CI: row bootstrap [21.2, 21.4] | CLUSTER bootstrap [20.6, 22.1]  -> wider & honest
No-show reduction: 4.8pp, 95% bootstrap CI [3.9pp, 5.7pp]  -> ready for the capstone memo
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Results change every run | Seed not fixed | `rng = np.random.default_rng(seed)`; report it |
| Bootstrap CI absurdly tight for clustered data | Resampled rows, not clusters | Cluster bootstrap: resample `clinic_id`, then take their rows |
| Permutation p-value exactly 0 | No shuffle reached the observed extreme | Report `< 1/n_perm`; increase resamples |
| Noisy, unstable interval | Too few resamples | Use ≥ 2,000–10,000 resamples |
| Bootstrap CI for a max is erratic | Unstable statistic / heavy tail | Note the failure mode; do not trust it |

**Instructor notes.** Task 4 is the climax of the whole course: the cluster bootstrap widening the interval makes Module 2's clustering warning concrete and shows that method choice, not sample size, governs honesty. Keep the row-vs-cluster intervals on screen together. Emphasise the seed-integrity point before the capstone — differing seeds are how copied analyses are caught. Fast finishers: bootstrap the logistic model's reminder odds ratio (Module 6) and compare its interval to the model's Wald CI.

## Mini Exercises

1. **Concept.** In one sentence, why does resampling the sample with replacement approximate drawing new samples from the population?
2. **Compute.** Bootstrap a 95% CI for the 90th-percentile wait time. Why is this awkward analytically but easy by bootstrap?
3. **Permutation.** State the exchangeability assumption behind the reminder permutation test in plain language. When would it fail for this data?
4. **Dependence.** Explain why a row-level bootstrap understates uncertainty for clustered clinic data, and how the cluster bootstrap fixes it.
5. **Debugging exercise.** A colleague reports a bootstrap CI, then mentions they "tried a few seeds to get a cleaner interval." Explain precisely why this invalidates the result and what they should do.

## Case Study — The Confidence Interval That Was Too Confident

**Scenario.** An analyst reports a bootstrap 95% CI for the mean wait time of ±0.1 minute and leadership sets a hard staffing target at its upper bound. Clinics consistently miss the target and staff burn out.

**Business context.** The staffing target drives shift budgets across dozens of clinics; a target set too tight looks like universal underperformance and triggers unwarranted interventions. The credibility of the analytics team rests on the interval being honest.

**Technical challenge.** Diagnose why the reported interval was far too narrow, and produce an honest interval that reflects the data's real structure.

**Constraints.** No new data; the correction must be explainable to operations; the revised target must be defensible.

**Solution approach.** (1) Identify the dependence — dozens of visits per clinic, most variation *between* clinics; (2) show the row-level bootstrap ignores this and manufactures false precision; (3) run a **cluster bootstrap** resampling whole clinics; (4) present the wider, honest interval and reset the target to a realistic band; (5) recommend the cluster bootstrap as the standard for all future clinic-level statistics.

**Discussion questions.**
1. Why does resampling individual rows understate uncertainty when data is clustered?
2. How would you explain "the variation is between clinics, not within" to an operations lead?
3. When is the plain bootstrap perfectly fine, and when must you cluster?
4. What is the cost, in staff and credibility, of a confidence interval that is too narrow?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Reproducibility | Rigour | Seed fixed and reported | Notebook check |
| CI coverage validation | Correctness | Wilson ~0.95, Wald under-covers shown | Simulation |
| Bootstrap interval | Correctness | Percentile ≈ BCa within rounding | Auto-check |
| Permutation vs analytical | Consistency | Same conclusion as Module 4 test | Comparison |
| Dependence handling | Judgement | Cluster bootstrap wider, explained | Lab notes |

**Example benchmark table:**

| Quantity | Analytical / naive | Resampling | Verdict |
|---|---|---|---|
| Wald CI coverage | claims 95% | 92.8% (MC) | Formula over-confident |
| Median wait CI | (no formula) | [17.6, 18.4] | Bootstrap supplies it |
| Mean wait CI | row [21.2, 21.4] | cluster [20.6, 22.1] | Cluster is honest |
| Reminder effect p | z-test 2e-43 | permutation 0.0001 | Agree |

## Required Visuals and Training Assets

### Diagrams
1. **The bootstrap loop** — *Purpose:* make the three-step recipe memorable. *Elements:* sample → resample-with-replacement ×B → statistic each → bootstrap distribution → percentile interval. *Style:* circular flow, printable A4.
2. **Permutation null by shuffling** — *Purpose:* make the p-value physical. *Elements:* observed labelled groups, an arrow to shuffled labels, and the null distribution with the observed statistic in the tail. *Style:* before/after with a histogram.
3. **Row vs cluster resampling** — *Purpose:* the dependence lesson. *Elements:* rows-drawn-independently vs whole-clinics-drawn, with the resulting interval widths side by side. *Style:* two-panel with interval bars.

### Images (screenshots)
1. **CI-coverage simulation output** — Wilson vs Wald coverage counts; *why:* validates Module 3 by simulation.
2. **Bootstrap distribution histogram** — of the median wait, with percentile bounds marked; *why:* shows where the interval comes from.
3. **Row-vs-cluster interval comparison** — *why:* the case-study centrepiece.

### Simulations
1. **CLT re-run** — *Setup:* resample means of skewed wait times for growing `n`. *Expected:* Normal shape, SE ~ `σ/√n`. *Learning objective:* the bootstrap re-derives Module 2's CLT from data.
2. **Coverage counter** — *Setup:* many samples, one CI each, count containment. *Expected:* ~95% for a good method. *Learning objective:* what "confidence" empirically means.

### Interactive Activities
- **"Bootstrap or formula?" decision cards (10 min):** given a statistic (median, ratio, AUC, mean), teams decide whether a formula exists or the bootstrap is needed.
- **Shuffle-by-hand permutation (8 min):** a tiny dataset shuffled physically on index cards to build a mini null distribution before coding it.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `clinic_visits.csv` | Golden thread (has `clinic_id` for clustering) | CSV | ~50,000 rows | Bootstrap, permutation, cluster bootstrap |
| `small_pilot.csv` | Synthetic small-`n` extract (n≈25) | CSV | 25 rows | Demonstrating resampling's small-sample limits |

### Demo Requirements
- **Instructor demo:** bootstrap a median CI and run the permutation test live, then contrast the row vs cluster bootstrap in under 8 minutes.
- **Student demo:** one pair defends why their capstone number carries a bootstrap interval rather than a bare point estimate.
- **Expected outputs:** a validated coverage simulation, a bootstrap CI, a permutation p-value, and a cluster-corrected interval.

---

# Final Capstone Project

## Title: The Mawid No-Show Decision — A Complete Statistical Analysis

## Project Scenario

You are the statistician assigned to **"Mawid Analytics"**, the appointments-intelligence team of the Ministry of Health's national primary-care booking platform. The Deputy Minister has asked one question: *how should the Ministry cut appointment no-shows without harming access?* Every component you need, you already built — Labs 1–7 each produced one piece of this analysis on the same `clinic_visits.csv`. The capstone is the **integration**: a single, coherent, defensible statistical investigation that ends in a quantified recommendation with honest uncertainty. You are not building software; you are building the analytical case a minister will act on.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Probabilistic framing (LO1):** model no-shows and wait times with appropriate named distributions; justify each choice with a fit (KS/AIC), not assertion. Carry the fitted models into a capacity or overbooking statement.
2. **Honest description and sampling (LO2/LO5):** report shape-appropriate summaries (median/IQR for skewed quantities); if you subsample, use a defensible design and state the estimand. Name any bias risk in the data.
3. **Estimation with intervals (LO2):** every headline number — national and per-region no-show rates, mean/median wait — carries a correct interval (Wilson for proportions, t for means). No bare point estimates.
4. **Rigorous testing with effect sizes (LO3):** analyse the SMS-reminder effect with the correct test, the CI of the difference, and an effect size (odds ratio). Apply a multiple-testing correction across regions. State hypotheses before analysis.
5. **Confounding-adjusted causal claim (LO4/LO5):** show the crude reminder association is confounded, resolve it (stratification or regression), and report the adjusted effect with its DAG-justified adjustment set. Distinguish "reminders work" from "roll out everywhere."
6. **Fitted, diagnosed models (LO4):** a logistic no-show model (odds ratios, AUC, calibration, capacity-based threshold) and a linear/log-linear wait-time model (diagnostics checked). Identify the actionable drivers.
7. **Resampling validation (LO6):** validate at least two analytical results by simulation/resampling; put a **bootstrap interval on the headline recommendation's magnitude** (projected no-show reduction). Use a cluster bootstrap where clustering applies. Seed fixed and reported.

**One extension (choose at least one):**
- Targeted-policy analysis: identify the subgroup (e.g., long-lead-time patients) where reminders help most via an interaction, and cost the targeted vs blanket rollout.
- Sample-size / power plan for a *randomised* next-round trial that would need no confounder adjustment.
- Sensitivity analysis: how strong an unmeasured confounder would have to be to overturn the adjusted effect.
- Wait-time policy: use the fitted distribution to set a staffing target at the 90th-percentile queue, with a cluster-bootstrap interval.
- Fairness check: test whether the no-show model is equally calibrated across regions before deployment.

## Architecture (target state)

```
clinic_visits.csv
   │
   ├─ M1  distributions fit ─────────► capacity / overbooking statement
   ├─ M2  honest summary + sample ───► the estimand, stated
   ├─ M3  rates + CIs (Wilson/t) ────► national & per-region estimates
   ├─ M4  A/B test + effect size ────► crude reminder effect (flagged as confounded)
   ├─ M5  confounder adjustment ─────► adjusted reminder effect (the causal claim)
   ├─ M6  logistic + linear models ──► drivers, odds ratios, AUC, calibration
   └─ M7  bootstrap / permutation ───► uncertainty on the recommendation
                                          │
                                          ▼
                              DECISION MEMO: quantified recommendation
                              (effect ± bootstrap CI, targeted vs blanket, cost)
```

## Deliverables

1. **A single analysis notebook** (`capstone.ipynb`), runnable top-to-bottom on a clean kernel, seed fixed, producing every number in the memo.
2. **A 2-page decision memo** (`DECISION_MEMO.md`): the recommendation, its projected no-show reduction *with a bootstrap CI*, the targeted-vs-blanket call, and the cost/uncertainty caveats — written for a non-statistician executive.
3. **A methods appendix** (`METHODS.md`): distribution choices, test choices, the DAG and adjustment set, model diagnostics, and which analytical results were resampling-validated.
4. **A 6-minute defence**: walk the golden thread from raw data to recommendation; one reviewer will ask you to justify one interval and one causal claim live.
5. **A reproducibility statement**: the seed, library versions, and a one-line "run this" instruction; another participant's notebook must produce *different* bootstrap digits (anti-copying).

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: distributions + honest summary integrated (M1–M2) | Day 1 end | instructor spot-check |
| M-B: estimates with CIs + A/B test with effect size (M3–M4) | Day 2 end | numbers carry intervals |
| M-C: confounding resolved + models fitted and diagnosed (M5–M6) | Day 3 end | adjusted effect + AUC/calibration shown |
| M-D: resampling validation + bootstrap on the headline number (M7) | Day 4 H2 | cluster bootstrap where needed |
| M-E: memo + defence | Day 4 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Probabilistic modelling & description | 12 | Right distributions, fit-justified; shape-appropriate summaries throughout | Mostly right; one unjustified model or a mean-on-skew slip | Defaults to Normal; mean reported for skewed data |
| Estimation & intervals | 15 | Every headline number has a correct interval; Wilson/t used correctly | One bare estimate or a Wald-where-Wilson-needed | Point estimates without intervals; misinterpreted CI |
| Hypothesis testing & effect size | 15 | Correct test, CI of difference, effect size, multiple-testing control; hypotheses pre-stated | Effect size or MT-correction thin | p-value alone; peeking/no correction |
| Confounding & causal reasoning | 20 | Crude→adjusted shown, DAG-justified adjustment set, mediator/collider avoided; claim scoped | Adjustment correct but DAG/justification thin | Reports crude association as causal |
| Regression modelling & diagnostics | 18 | Logistic + linear fitted, odds ratios, AUC + calibration, diagnostics checked | Models fit but calibration or diagnostics missing | Uninterpreted coefficients; accuracy-only eval |
| Resampling validation & uncertainty | 12 | ≥2 results validated; bootstrap CI on the recommendation; cluster bootstrap where apt; seeded | Bootstrap present but row-level on clustered data | No validation; bare recommendation |
| Memo & defence | 8 | Crisp, executive-ready, uncertainty honest, scope correct; defends any number cold | Memo works; one claim shaky under questioning | Cannot justify own numbers |

**Pass ≥ 70. Distinction ≥ 90.** The chosen extension adds up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the numbers' defensibility first*: does every headline figure carry an honest interval, and is the causal claim confounder-adjusted and correctly scoped? The memo second.
- Anti-pattern flags that cap a criterion at 70%: a crude association presented as causal; a bare point estimate in the memo; accuracy quoted for the imbalanced no-show classifier; a bootstrap seed that was clearly tuned; row-level bootstrap on clustered clinic data.
- Verify one claim live: ask the participant to state what their 95% CI does and does *not* mean, and to name the confounder they adjusted for and why it is not a mediator.

## Bonus Tasks (for early finishers / distinction seekers)

1. Reproduce the headline effect two ways (stratified standardisation *and* logistic adjustment) and reconcile any gap.
2. Add a sensitivity analysis quantifying how strong an unmeasured confounder would need to be to null the effect.
3. Build the targeted-rollout cost model: no-shows prevented per SAR-equivalent of messages, with a bootstrap interval.
4. Calibrate-then-threshold the no-show model and show the improvement in no-shows-prevented-per-message versus a naive 0.5 threshold.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** For a right-skewed wait-time distribution, which centre do you report and why? → median; robust to the skew/tail, the honest "typical" value.
**Q2.** A fitted PDF gives `f(20) = 0.05`. Does 5% of patients wait exactly 20 minutes? → no; density ≠ probability; `P(X=20)=0` for a continuous variable.
**Q3.** Bayes: no-show base rate 18%, a flag is 90% sensitive and 90% specific. Is the PPV ≈ 90%? → no, ≈ 66%; base-rate neglect.
**Q4.** What does the standard error `σ/√n` describe — the spread of the data or of the estimate? → the estimate (the sampling distribution's spread).
**Q5.** To halve a confidence interval's width, by what factor must `n` grow? → four (the `√n` law).
**Q6.** Why prefer the Wilson interval over Wald for a proportion? → Wilson stays in [0,1] and has far better coverage at small `n`/extreme `p̂`.
**Q7.** State the correct meaning of a 95% CI in one sentence. → the *procedure* covers the true parameter ~95% of the time over repeated sampling.
**Q8.** A p-value of 0.03 means there is a 3% chance the null is true — correct? → no; it is `P(data at least this extreme | H₀ true)`.
**Q9.** Why must a p-value always be paired with an effect size? → with large `n`, trivial differences are "significant"; effect size says whether it matters.
**Q10.** Default two-sample mean test in this course and why? → Welch's t-test; robust to unequal variances at no cost.
**Q11.** You test the reminder effect in all 13 regions. What must you apply and why? → a multiple-testing correction (Bonferroni/Benjamini–Hochberg); ~1 false positive per 20 tests otherwise.
**Q12.** Reminders correlate with *higher* no-shows in aggregate but *lower* in every clinic type. Name the phenomenon and the fix. → Simpson's paradox; stratify/adjust for the confounder.
**Q13.** Confounder vs mediator: which do you adjust for, which do you not? → adjust for the confounder; never for the mediator (it's on the causal path).
**Q14.** What happens if you adjust for a collider? → you *create* a spurious association (collider/selection bias).
**Q15.** A logistic coefficient is `−0.4` (log-odds). Give the odds ratio and its meaning. → `exp(−0.4)≈0.67`; odds fall ~33% per unit, holding others fixed.
**Q16.** A no-show classifier is 82% accurate on an 18%-positive dataset. Is it good? → not necessarily; a trivial "never no-show" model matches it; report AUC + precision/recall.
**Q17.** AUC is high but decisions are poor. What is the likely culprit? → poor calibration (and/or a default 0.5 threshold).
**Q18.** Which statistic needs the bootstrap because it has no simple SE formula? → e.g., the median or a 90th-percentile wait (or a ratio/AUC).
**Q19.** Clustered clinic data: why cluster-bootstrap instead of row-bootstrap? → most variation is between clinics; row resampling understates uncertainty.
**Q20.** Why must you fix and report your random seed, and never tune it? → reproducibility; seed-tuning a bootstrap to a desired CI is a form of p-hacking.

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a notebook that reports bare per-region no-show rates and "flags the three worst," add correct Wilson intervals, identify which regions genuinely differ from national, and rewrite the conclusion. Scored on: correct intervals (40%), correct flagging by interval overlap (40%), corrected interpretation (20%).

**PA-2 (30 min, Day 3):** Given a "reminders increase no-shows" crude analysis, diagnose and resolve the confounding: stratify, produce an adjusted estimate, draw the DAG, and state what must *not* be adjusted for. Scored against the model solution (confounding diagnosis 40%, adjusted estimate 30%, DAG/adjustment-set reasoning 30%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 + quiz — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint notebooks + expected outputs |
| PA-1 + PA-2 | 20% | corrected notebooks + notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, numbers-first |

Badge issuance (Core Statistics badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical bootstrap digits or CI numbers across submissions are checked, since differing seeds should differ).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Regenerate `clinic_visits.csv` from the course generator against the pinned `numpy`/`scipy` versions; verify the golden-thread numbers (no-show ≈ 0.18, median wait ≈ 18 min, Simpson reversal present, reminder odds ratio ≈ 0.68) reproduce.
- [ ] Push checkpoint notebooks and tags (`lab1-start`…`lab7-start`, plus `lab*_solution`) to the course repository.
- [ ] Dry-run all 7 labs end-to-end on a clean machine **and** on Google Colab (fallback, no install).
- [ ] Verify `survey_responses.csv`, `ab_daily_log.csv`, `clinic_reference.csv`, `region_reference.csv`, and `small_pilot.csv` are present and load.
- [ ] Print A4 posters: the distribution zoo, the CI-coverage picture, the confounder/mediator/collider triptych, the log-odds↔odds-ratio bridge, and the bootstrap loop.
- [ ] Pin versions in `environment.yml` (`numpy`, `scipy`, `statsmodels`, `pandas`, `scikit-learn`, `matplotlib`) and rebuild the env to confirm it solves.
- [ ] Prepare the shared leaderboard (per-team headline effect + bootstrap CI) for the Day-4 defences.
- [ ] Confirm classroom Jupyter kernels and Colab both run `scipy.stats.bootstrap` (older SciPy lacks it) — upgrade if needed.

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.11 via Anaconda (primary) **or** a Google account for Colab (fallback).
- [ ] `conda env create -f environment.yml` (or `pip install numpy scipy statsmodels pandas scikit-learn matplotlib jupyter`).
- [ ] Launch Jupyter and run the provided `check_env.ipynb` — it imports every library, prints versions, and confirms `scipy.stats.bootstrap` exists (prints ✓/✗).
- [ ] Download the course data bundle (`clinic_visits.csv` + auxiliaries) into a local `data/` folder.
- [ ] Verify a one-line smoke test: `python -c "import scipy, statsmodels, sklearn; print('ok')"`.

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| "Data is Normal" instinct on skewed wait time | High | Confront early in M1 with the KS test; keep the failing Normal fit on screen |
| Confusing SE with SD | High | Whiteboard minute in M3: "SD describes patients, SE describes our knowledge of the average" |
| Reading logistic coefficients as probabilities | High | Drill the `exp()`→odds-ratio transform in M6; card-sort relay |
| "Controlling for everything" instinct | Medium | The DAG discipline in M5; show collider bias appearing on a simulation |
| Row-level bootstrap on clustered data | Medium | M7 Task 4 is the cure; make the interval widen live |
| The probability-misinterpretation of a CI | Medium | The "say it correctly" relay in M3; re-test in the quiz |
| Colab lacks a library or older SciPy | Medium | Provide a `!pip install -U scipy` first cell; test the week before |
| Seed not fixed → non-reproducible results | Medium | Enforce `default_rng(seed)` from M1; explain the anti-copying rationale |
| Overrun in Labs 4 and 6 | Medium | Publish `lab*_solution.ipynb` so stragglers fast-forward; protect Lab time |
| Pace slips on Day 3 (confounding + regression) | Low | Compress M6 theory (it lands through Lab 6); never cut the Simpson reveal |

## Timing Recommendations

- Protect Labs 3, 5, and 7 at full length — they carry the course's three hardest ideas (intervals, confounding, resampling).
- If a cohort is strong: add the interaction-targeting extension in M6 and the sensitivity-analysis bonus in the capstone.
- If a cohort is weak: run the Simpson's-paradox resolution (Lab 5) as a guided walkthrough rather than independent work, but **never** skip the reversal reveal — it is the course's thesis made visible.
- Hard rule: capstone assembly (Day 4 H3) must start on time. Cut discussion, not build time. Collect notebook URLs at the end of H4 so outputs can be verified before the H5 defences.
- Each "hour" is 50 minutes instruction + 10 minutes buffer; schedule the long break around Dhuhr; Day-4 morning is deliberately heavier to protect afternoon capstone time.

## Discussion Prompts (use during transitions)

1. "A dashboard shows a big number with no interval. What is the single question that most improves the decision it drives?"
2. "Your intervention correlates with worse outcomes. Before you cancel it — what is the first thing you check, and why?"
3. "When is a wider confidence interval the *better* result?"
4. "Which is worse for a minister: a model that ranks patients well but predicts wrong probabilities, or one that predicts honestly but ranks slightly worse? Why?"
5. "If your bootstrap interval and your formula interval disagree, which do you trust — and what does the disagreement tell you?"

## Wrap-up (Day 4 final 15 minutes)

- Trace the golden thread on one slide: the *same* `clinic_visits.csv` carried from a Bernoulli no-show (M1) to a confounder-adjusted, resampling-validated recommendation with an honest interval (Capstone).
- Map each capstone requirement to the module that taught it, so participants see the course was one continuous investigation, not seven topics.
- Forward pointer: SDA-DSC-112 (Data Visualization & Storytelling) turns this analysis into an executive narrative; SDA-DSC-211 (Advanced ML) and SDA-DSC-213 (Experimentation & Causal Inference) assume exactly the inferential judgement built here — the confidence intervals, the confounding discipline, and the resampling toolkit.
- Collect: capstone notebook URLs, `DECISION_MEMO.md`, `METHODS.md`; issue Core Statistics badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.11, NumPy ≥ 1.26, SciPy ≥ 1.11 (for `scipy.stats.bootstrap`), statsmodels ≥ 0.14, scikit-learn ≥ 1.3, pandas ≥ 2.0. Pin and verify these versions in `environment.yml` before each delivery. The golden thread — Mawid Analytics and `clinic_visits.csv` — is the same synthetic dataset from Module 1 to the capstone; never substitute a throwaway toy dataset.*
