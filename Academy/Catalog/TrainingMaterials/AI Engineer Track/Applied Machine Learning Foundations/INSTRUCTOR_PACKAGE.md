# Applied Machine Learning Foundations
## أسس تعلم الآلة التطبيقي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Applied Machine Learning Foundations |
| **Module Code** | SDA-AIE-111 |
| **Arabic Title** | أسس تعلم الآلة التطبيقي |
| **Level** | Practitioner |
| **Duration** | 5 days × 5 learning hours = **25 hours** |
| **Audience** | Developers, engineers, analysts entering AI engineering; cross-listed to Data Scientist track |
| **Prerequisites** | SDA-FND-103; SDA-FND-104 recommended |
| **Assessment** | Daily labs (60%) + end-to-end ML project (40%) |
| **Stackability** | Core ML badge · Required for all Specialist AI Engineer modules and DSC-211 · Next: SDA-AIE-112 |
| **Tools & Platforms** | scikit-learn · pandas · Jupyter · XGBoost · Matplotlib |

## Course Description

A hands-on foundation in supervised and unsupervised learning that teaches the complete modelling workflow. Participants frame business problems as ML tasks, train and tune models with scikit-learn, and evaluate them with the right metrics. The module ends with an end-to-end modelling project on real data.

The course is built around a single evolving artefact: the **"Manafeth" customer-analytics workbench** — a modelling project for a fictional Saudi quick-commerce platform. Participants receive raw order and customer data on Day 1 and evolve one repository through the whole workflow: they frame the churn and basket-value problems, split the data correctly, build baselines, train regression and classification models, wrap everything in leakage-proof scikit-learn pipelines, evaluate with defensible metrics and cross-validation, upgrade to tree ensembles with XGBoost, segment customers with clustering and PCA, and tune the final model systematically. Every lab produces a component that the capstone reuses, so by Day 5 each participant has personally executed the end-to-end workflow once on Manafeth data — and then proves it a second time, unassisted, on real data.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Frame business problems as supervised or unsupervised learning tasks
2. **LO2** — Implement the end-to-end ML workflow from data splitting to model selection
3. **LO3** — Develop classification and regression models using scikit-learn pipelines
4. **LO4** — Apply feature engineering, scaling, and encoding techniques appropriately
5. **LO5** — Evaluate models using suitable metrics, cross-validation, and error analysis
6. **LO6** — Diagnose and mitigate overfitting, underfitting, and data leakage
7. **LO7** — Optimize model performance through systematic hyperparameter tuning

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | From business question to first model | M1: ML Problem Framing & Workflow Design · M2 (part 1): Regression | 50% | 50% | Framing canvas + stratified splits + beaten baseline + first regression model |
| **Day 2** | Models and pipelines that don't lie | M2 (part 2): Classification · M3: Feature Engineering & Preprocessing Pipelines | 45% | 55% | Churn classifiers + leakage-proof `ColumnTransformer` pipeline |
| **Day 3** | Trust, but verify | M4: Model Evaluation, Metrics & Cross-Validation · M5: Tree Ensembles | 45% | 55% | Evaluation harness with CV + error analysis + tuned-by-default ensemble beating linear models |
| **Day 4** | Structure without labels, performance by design | M6: Unsupervised Learning · M7: Hyperparameter Tuning & Model Selection · Capstone kickoff | 40% | 60% | Customer segments + PCA views + systematically tuned final model + capstone dataset selected |
| **Day 5** | The end-to-end project | Final Capstone Project | 5% | 95% | Complete modelling project on real data: notebook, model card, 5-minute demo |

## Hour-by-Hour Breakdown

### Day 1 — From Business Question to First Model

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why ML projects fail before training starts** + course kickoff | Recognise ML vs rules vs analytics; identify the workflow stages this course covers; meet the Manafeth golden thread | Interactive lecture + failure-story discussion | 80/20 |
| 2 | **Problem framing and workflow design** (M1) | Task taxonomy (regression/classification/clustering); framing canvas; splitting discipline; baselines as contract | Lecture + live framing of the Manafeth churn problem | 70/30 |
| 3 | **Lab 1 — Frame, split, baseline** | EDA on Manafeth data; framing canvas; stratified train/test split; dummy baselines committed to the scoreboard | Guided lab (pairs) | 10/90 |
| 4 | **Supervised learning I: regression** (M2) | Linear regression as loss minimisation; interpreting coefficients; residuals; under/overfitting first contact | Lecture + live model build | 70/30 |
| 5 | **Lab 2a — First regression model** | Predict basket value with `LinearRegression`; compare MAE against the dummy baseline; plot residuals | Guided lab (pairs) | 10/90 |

### Day 2 — Models and Pipelines That Don't Lie

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Supervised learning II: classification** (M2) | Logistic regression, decision trees, k-NN; decision boundaries; probability outputs vs labels; class imbalance first contact | Lecture + boundary visualisation demo | 70/30 |
| 2 | **Lab 2b — Churn classifiers + overfitting demo** | Train logistic regression and decision tree on churn; watch a depth-20 tree memorise the training set | Guided lab (pairs) | 10/90 |
| 3 | **Feature engineering and preprocessing pipelines** (M3) | Scaling, encoding, missing values, `ColumnTransformer`; why `Pipeline` is the anti-leakage weapon | Lecture + live pipeline assembly | 70/30 |
| 4 | **Lab 3 — Build the preprocessing pipeline** | Full `Pipeline` for Manafeth; leakage hunt on a sabotaged notebook; RFM + datetime features | Guided lab (pairs) | 10/90 |
| 5 | **Feature engineering workshop** (M3) | Domain features: Ramadan flag, order recency, city-tier encoding; group review of engineered features | Workshop + micro-lecture | 30/70 |

### Day 3 — Trust, But Verify

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Model evaluation and metrics** (M4) | Regression metrics (MAE/RMSE/R²); classification metrics (precision/recall/F1/ROC-AUC/PR-AUC); why accuracy lies at 14% churn | Lecture + metric-choice exercise | 70/30 |
| 2 | **Cross-validation, learning curves, error analysis** (M4) | k-fold and stratified CV; learning/validation curves; reading a confusion matrix like an analyst | Lecture + live CV run | 60/40 |
| 3 | **Lab 4 — Evaluation harness** | Cross-validated comparison of Day 2 models; threshold tuning on PR curve; slice-based error analysis | Guided lab (pairs) | 10/90 |
| 4 | **Tree ensembles: random forests and gradient boosting** (M5) | Bagging vs boosting intuition; random forests; gradient boosting; XGBoost in practice | Lecture + live ensemble build | 70/30 |
| 5 | **Lab 5 — Ensemble the churn model** | RandomForest + XGBoost vs linear baseline; permutation importance; overfitting check via validation curve | Guided lab (pairs) | 10/90 |

### Day 4 — Structure Without Labels, Performance by Design

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Unsupervised learning: clustering** (M6) | K-means mechanics; choosing k (elbow, silhouette); DBSCAN and hierarchical at a glance; clustering as business segmentation | Lecture + live clustering | 70/30 |
| 2 | **Dimensionality reduction: PCA** (M6) | Variance, components, explained-variance ratio; PCA for visualisation vs for features; scaling before PCA | Lecture + demo, lab begins | 40/60 |
| 3 | **Lab 6 — Segment the customers** | K-means segmentation with silhouette selection; PCA projection plot; name and profile the segments | Guided lab (pairs) | 10/90 |
| 4 | **Hyperparameter tuning and model selection** (M7) | Grid vs randomised search; CV inside search; the model-selection protocol; tuning budgets; leakage in tuning | Lecture + live search | 60/40 |
| 5 | **Lab 7 + capstone kickoff** | `RandomizedSearchCV` on the XGBoost churn model; freeze the final model; teams choose their capstone dataset | Lab + project briefing | 20/80 |

### Day 5 — The End-to-End Project

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Capstone work I — frame and split** | Framing canvas for the chosen real dataset; EDA; correct split committed before any modelling (Milestone C1) | Project work (teams of 2) | 0/100 |
| 2 | **Capstone work II — pipeline and baseline** | Preprocessing pipeline; dummy baseline; first honest model (Milestone C2) | Project work | 0/100 |
| 3 | **Capstone work III — evaluate, improve, tune** | Model comparison under CV; error analysis; systematic tuning of the best candidate (Milestone C3) | Project work | 0/100 |
| 4 | **Capstone finalisation** | Model card; notebook cleanup to tell the story; peer review against checklist (Milestone C4) | Project work + peer review | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric scoring; path to SDA-AIE-112/113 and the Specialist tier | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module works the same Manafeth dataset. Never introduce a throwaway toy dataset for a technique — always demonstrate on Manafeth, so that pipelines, splits, and baselines built in earlier labs keep paying off. The capstone is the one deliberate change of data, and that is the point: participants prove the *workflow* transfers, not the dataset.
- **Pace control:** Labs 3 and 7 are the most overrun-prone (pipeline debugging and search wall-clock time respectively). Publish checkpoint notebooks (`lab1_solution.ipynb` … `lab7_solution.ipynb`) in the course repository so stragglers can fast-forward; cap Lab 7 search budgets (`n_iter=30`) so runs finish inside the hour.
- **Pairing:** rotate pairs daily. Pair a strong-Python participant with a strong-domain participant; framing quality improves measurably when a domain thinker is in the pair.
- **Environment strategy:** primary = local Python 3.12 + venv/conda with JupyterLab; fallback = hosted JupyterHub or Google Colab (course notebooks run unchanged; datasets pulled from the shared drive). Verify both the week before delivery — XGBoost wheels occasionally lag new Python releases.
- **Language:** deliver in English or Arabic; keep all code, column names, and notebook headings in English (production convention in Saudi enterprise environments — mixed-language column names break downstream tooling).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day 5 is deliberately theory-free so teams can work in long uninterrupted blocks between prayers.
- **Assessment logistics:** daily labs are checked off at end of day via the scoreboard notebook (baseline and model scores per pair); capstone rubric scoring happens live during Day 5 Hour 5 demos. Collect capstone notebooks at the end of Hour 4 so instructors can skim them before demos begin.

---

# Module 1 — ML Problem Framing and Workflow Design

## Module Overview

**Purpose.** Most machine-learning failures are decided before a single model is trained: the wrong task type, a target that leaks the answer, a split that flatters the model, or a metric nobody in the business recognises. This module teaches participants to convert a business problem into a well-posed ML task, to design the workflow before touching an estimator, and to establish the two disciplines that protect everything downstream — split first, baseline always.

**Business relevance.** Saudi enterprises and government entities are moving from AI pilots to production programmes, and the scarce skill is not model training — scikit-learn makes that a few lines — but framing: knowing whether a problem is prediction or segmentation, whether the labels exist, whether the prediction is actionable, and what "good enough" means in riyals. A correctly framed project fails fast and cheap in week one or succeeds; a mis-framed project burns a quarter and erodes trust in the whole AI programme.

**Industry use cases.**
- A retail bank wants to "reduce card churn" — framing decides between churn classification (act per customer), survival analysis (when), or uplift modelling (who is *persuadable*), each with different data and different economics.
- A logistics operator wants "better delivery promises" — framed as a regression on delivery time with a business-set quantile, not a mean, because a late promise costs more than an early one.
- A ministry service centre wants to "understand complaint patterns" — no labels exist, so the honest framing is unsupervised clustering feeding a human taxonomy, not an imaginary classifier.

**Expected competencies.** After this module a participant can complete a framing canvas for a business problem, select the task type and justify it, define the prediction target and unit of analysis precisely, execute a defensible train/test split (stratified or temporal), and establish dummy baselines that every later model must beat.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Decide whether a business problem needs ML, rules, or analytics — and defend the decision | LO1 |
| 1.2 | Classify problems into regression, classification, or unsupervised tasks with correct target definitions | LO1 |
| 1.3 | Describe the end-to-end workflow stages and the order they must happen in | LO2 |
| 1.4 | Execute stratified and temporal train/test splits before any exploration of the test set | LO2, LO6 |
| 1.5 | Establish dummy baselines and use them as the acceptance bar for every subsequent model | LO2, LO5 |

## Technical Content

### 1. When ML is the wrong answer

Machine learning learns a function from examples. That sentence contains three preconditions worth teaching as a checklist: there must be **examples** (historical data with outcomes), a **pattern** (the outcome must be at least partly predictable from the inputs), and a **payoff** (a prediction someone will act on). If a deterministic rule already exists ("block transactions over the card limit"), write the rule. If the need is a one-off insight ("which city grew fastest last quarter?"), that is analytics, not ML. If the outcome is dominated by information you will never have, no model rescues it.

Frame this as the first gate of the workflow, and give the class the counter-examples: a "fraud model" that reimplemented three business rules with 40 hours of training compute; a "demand forecast" for a product with four historical data points; a churn model whose predictions nobody was staffed to act on. Every experienced practitioner in the room will have one of these stories — collect two or three before moving on.

### 2. The task taxonomy and the framing canvas

The practical taxonomy for this course:

| Task | Target | Output | Manafeth example |
|---|---|---|---|
| **Regression** | Continuous number | A quantity | Next-month basket value in SAR |
| **Binary classification** | Yes/no label | Probability + decision | Will this customer churn in 30 days? |
| **Multiclass classification** | One of k labels | Probability per class | Which delivery slot will they pick? |
| **Clustering** | None (unsupervised) | Group assignments | Customer behavioural segments |
| **Dimensionality reduction** | None | Compressed representation | 2-D map of 30 usage features |

The **framing canvas** (participants fill one in Lab 1 and again in the capstone) forces precision on six questions:

1. **Business question:** what decision will change because of this model?
2. **Unit of analysis:** one row = one *what*? (customer-month, order, sensor-hour) — the most common silent error in real projects.
3. **Target definition:** precisely, mechanically computable from data. "Churn = no completed order in the 30 days following the observation date." Vague targets produce unreproducible labels.
4. **Features available *at prediction time*:** the timestamp discipline — anything recorded after the prediction moment is leakage by construction.
5. **Metric and threshold of success:** chosen with the business, in business terms, *before* modelling ("catch ≥ 60% of churners while contacting ≤ 20% of the base").
6. **Baseline and current practice:** what does the business do today, and what does a naive model score? Both are acceptance bars.

### 3. The end-to-end workflow

The course's canonical workflow — the map on the wall for all five days:

```
business question → framing canvas → data audit & EDA
      → SPLIT (train / validation / test)          ← before any modelling decisions
      → baseline (dummy + simple heuristic)
      → iterate: [ features → model → cross-validated evaluation → error analysis ]
      → hyperparameter tuning of the best candidate
      → final evaluation on the untouched test set  ← once
      → model card + decision: ship / iterate / stop
```

Three rules give the workflow its integrity:

- **Split first.** The test set is quarantined the moment the target is defined. Every decision made after looking at test data — feature choices, model choices, thresholds — contaminates it. In scikit-learn terms: `train_test_split` happens in notebook cell 3, not cell 30.
- **The test set is spent once.** Validation (or cross-validation on the training set) absorbs all iteration; the test set answers only the final question "what should we expect in production?" A test set consulted ten times is a validation set with a misleading name.
- **Stratify or respect time.** For imbalanced targets, `stratify=y` preserves the class ratio in both halves. When the data has a time axis and the model will predict the future, split by time — random splits let the model train on tomorrow to predict yesterday, and the offline score becomes fiction.

### 4. Baselines: the cheapest insurance in ML

A baseline is a model so simple it cannot be wrong about its own honesty. The course mandates two per task:

- **Dummy baseline:** `DummyRegressor(strategy="mean")` / `DummyClassifier(strategy="most_frequent")` (and `strategy="stratified"` for probabilistic comparison). These define the floor: any model that fails to beat them clearly is worse than no model.
- **Heuristic baseline:** one line of domain logic — "predict churn if no order in 21 days", "predict basket value = customer's own 3-order average". These are what the business could deploy this afternoon for free; the model must beat *them*, not just the dummy, to justify its existence.

Baselines also calibrate expectations early: at Manafeth's 14% churn rate, the most-frequent classifier scores 86% accuracy while catching zero churners — the single most effective demonstration of why accuracy is the wrong metric here, three hours before Module 4 formalises it.

### 5. Common mistakes & production considerations

1. **Framing the proxy, not the problem.** Predicting "customer called support" because churn labels were hard to build — then acting on it as if it were churn.
2. **Unit-of-analysis drift.** Features built per-customer, labels per-order; the join silently duplicates rows and the model trains on the same customer 40 times, inflating every score.
3. **Target leakage at framing time.** Including `refund_issued` as a feature for churn — refunds happen mostly *after* the churn decision. The timestamp test catches it: "would this value exist at prediction time?"
4. **Test-set peeking.** Choosing features by their correlation with the target computed on all data; running EDA on the full dataset including test rows. Split first.
5. **Metric chosen after the model.** Teams pick the metric their model happens to win. Canvas question 5 exists to prevent exactly this.
6. **No stop condition.** Workflows without a pre-agreed success threshold iterate forever; "ship / iterate / stop" is a framing decision.

Production considerations: framed problems become contracts — the target definition and prediction-time feature list from the canvas are exactly what a deployment team (SDA-AIE-113, SDA-AIE-216) needs to reproduce; write them down as if they will be audited, because in regulated Saudi sectors (SAMA-supervised finance, health) they will be.

### 6. The Manafeth problem, framed live

Close the theory by framing the golden thread on the projector, with the class filling the canvas: Manafeth (منافذ), a quick-commerce grocery platform operating in Riyadh, Jeddah and Dammam, loses money acquiring customers who lapse after Ramadan. Business question: *which active customers should receive the retention voucher, given a budget covering 20% of the base?* Unit: customer at monthly snapshot date. Target: no completed order in the following 30 days. Features: order history, recency/frequency/monetary aggregates, city, device, payment method — all computable at snapshot time. Metric: recall at the top-20% of predicted risk (with PR-AUC for model comparison). Baselines: most-frequent dummy; the "21-day silence" heuristic the CRM team uses today. Secondary thread (regression): predict next-month basket value to size voucher amounts.

## Code Examples

### Data audit and framing-time EDA

```python
# notebooks/day1/lab1_framing.ipynb — Data audit (run BEFORE splitting decisions, on train only after split)
import pandas as pd

customers = pd.read_csv("data/manafeth_customers.csv", parse_dates=["signup_date", "snapshot_date"])
print(customers.shape)                        # (48_000, 19)

# The three questions every audit answers:
# 1) What is one row?  -> one customer at the 2025-11-01 snapshot
assert customers["customer_id"].is_unique, "unit-of-analysis violation: duplicate customers"

# 2) Is the target computable and how balanced is it?
print(customers["churned_30d"].value_counts(normalize=True))
# 0    0.86
# 1    0.14        <- remember this number; it explains Module 4

# 3) What can hurt us later?
print(customers.isna().mean().sort_values(ascending=False).head())
# avg_rating          0.31     <- missingness is informative: new customers have no ratings
# last_promo_used     0.22
```

### Split first — stratified, seeded, quarantined

```python
# notebooks/day1/lab1_framing.ipynb — The split happens BEFORE modelling decisions
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
TARGET = "churned_30d"
LEAKY = ["refund_issued", "support_ticket_after_snapshot"]   # exist only after prediction time

X = customers.drop(columns=[TARGET, "customer_id", *LEAKY])
y = customers[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    stratify=y,                 # preserve the 14% churn rate in both halves
    random_state=RANDOM_STATE,  # reproducibility is a course-wide rule
)
print(y_train.mean(), y_test.mean())   # 0.140, 0.140 — stratification verified

# Quarantine: X_test / y_test are not touched again until Day 4 Hour 5.
X_test.to_parquet("data/splits/test_features.parquet")
```

### Baselines as the acceptance bar

```python
# notebooks/day1/lab1_framing.ipynb — Every later model must beat BOTH of these
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.metrics import average_precision_score, mean_absolute_error

# Dummy floor for churn
dummy = DummyClassifier(strategy="stratified", random_state=RANDOM_STATE).fit(X_train, y_train)
print("dummy PR-AUC:", average_precision_score(y_train, dummy.predict_proba(X_train)[:, 1]))
# dummy PR-AUC: 0.14   (= the churn rate; that is what "no skill" looks like on PR-AUC)

# Heuristic bar: the CRM team's current rule, expressed as a model
def silence_heuristic(frame: pd.DataFrame) -> pd.Series:
    """Predict churn if no order in the last 21 days — deployable today for free."""
    return (frame["days_since_last_order"] > 21).astype(int)

# Dummy floor for basket-value regression
dummy_reg = DummyRegressor(strategy="mean").fit(X_train, y_train_basket)
print("dummy MAE:", mean_absolute_error(y_train_basket, dummy_reg.predict(X_train)))
# dummy MAE: 34.2 SAR — the number to beat, in units the business understands
```

### The framing canvas as a repository artefact

```markdown
<!-- project/FRAMING.md — committed before the first model; audited at capstone review -->
# Framing Canvas — Manafeth Churn
| Question | Answer |
|---|---|
| Business decision | Allocate retention vouchers to top-20% risk customers monthly |
| Unit of analysis | customer × monthly snapshot |
| Target | churned_30d = no completed order in (snapshot, snapshot+30d] |
| Prediction-time features | RFM aggregates, city, device, payment method, tenure (all ≤ snapshot) |
| Excluded as leakage | refund_issued, support_ticket_after_snapshot |
| Success metric | recall@top-20% ≥ 0.60; PR-AUC for comparison |
| Baselines | stratified dummy (PR-AUC 0.14); 21-day-silence heuristic (recall@20% 0.41) |
| Stop condition | if best model < heuristic + 5 pts after Day 3, revisit features not models |
```

## Hands-on Lab 1 — Frame, Split, Baseline

| | |
|---|---|
| **Objective** | Produce the framing canvas, a verified stratified split, and committed dummy + heuristic baselines for both Manafeth tasks (churn classification, basket-value regression) |
| **Duration** | 50 minutes (Day 1 Hour 3) |
| **Setup** | Course repo cloned; `pip install -r requirements.txt` done; JupyterLab open on `notebooks/day1/lab1_framing.ipynb` (skeleton with TODO cells) |

**Instructions & tasks**

1. *(10 min)* Data audit: shape, dtypes, uniqueness of `customer_id`, target balance, missingness table. Answer the three audit questions in a markdown cell.
2. *(10 min)* Complete `FRAMING.md` in pairs: target definition, unit, prediction-time feature list. Flag at least two leaky columns from the data dictionary (there are three planted).
3. *(10 min)* Execute the stratified split with `random_state=42`; verify the churn rate matches in both halves; save the test partition to `data/splits/` and add a "do not open" markdown cell.
4. *(10 min)* Fit `DummyClassifier` (stratified) and `DummyRegressor` (mean); implement the 21-day-silence heuristic; record PR-AUC, recall@top-20%, and MAE on the *training* set.
5. *(5 min)* Post baseline numbers to the class scoreboard notebook; compare with neighbouring pairs (numbers must match to two decimals — same seed, same data).
6. *(5 min)* Commit: `feat(lab1): framing canvas, quarantined split, baselines`.

**Expected output**
```
Split verified: train churn 14.0% | test churn 14.0%  (n=38,400 / 9,600)
Dummy (stratified):     PR-AUC 0.141   recall@20% 0.20
Heuristic (21-day):     PR-AUC n/a     recall@20% 0.41
DummyRegressor (mean):  MAE 34.2 SAR
Leaky columns found: refund_issued, support_ticket_after_snapshot, next_month_orders
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Churn rates differ across pairs | Split before dropping duplicate rows, or missing `random_state` | Re-run audit cell; assert uniqueness before splitting; seed everything |
| `next_month_orders` not flagged as leaky | Name sounds like a feature | Apply the timestamp test: computable at snapshot time? No → leakage |
| Heuristic recall@20% ≈ 0.20 | Thresholded at 50% of base instead of top-20% | Rank by days-since-order and take the top quintile |
| Memory error loading CSV | 32-bit Python or Excel-opened CSV re-saved | Use provided parquet mirror `manafeth_customers.parquet` |

**Instructor notes.** The planted leaky column `next_month_orders` is the heart of this lab — roughly half the room misses it because it "looks like" a feature. When revealed, connect it forward: Module 3 shows leakage *inside* preprocessing, Module 7 shows leakage *inside* tuning. The scoreboard moment matters socially: identical baselines across pairs establishes that the workflow is deterministic and shared; divergent numbers always mean a workflow bug, and finding it publicly is the lesson.

## Mini Exercises

**Quiz (5 questions)**
1. A hospital wants to predict which appointments will be no-shows. Task type, unit of analysis, target? → binary classification; one row = one appointment; no-show flag at appointment time.
2. Why must the split precede EDA-driven feature selection? → otherwise feature choices encode test-set information; offline scores inflate.
3. When is a temporal split mandatory? → whenever the model will predict forward in time and the data has temporal structure.
4. `DummyClassifier(strategy="most_frequent")` scores 86% accuracy on Manafeth. What does that number mean? → nothing about skill; it restates the class balance — the floor, not an achievement.
5. Name the two acceptance bars every course model must beat. → dummy baseline and the domain heuristic.

**Debugging exercise.** Provide a notebook where `train_test_split` is called *after* a cell that fills missing `avg_rating` with the *global* mean. Participants must explain why the test set is already contaminated and reorder the workflow.

**Code-review exercise.** Review a framing canvas for "predict which SMEs will default": unit is "loan", target is "default ever", features include "months_of_arrears". Three findings expected (unit should be loan×time, target needs a horizon, arrears is leakage-prone).

**Discussion questions.**
- Manafeth's CRM team's heuristic catches 41% of churners for free. What uplift justifies the cost of building, deploying, and maintaining a model? Put a number on it.
- Your sponsor asks for "at least 95% accuracy" on churn. Renegotiate the metric in one paragraph of business language.

## Case Study — Framing Emergency-Department Demand at a Riyadh Hospital Cluster

**Scenario.** A three-hospital cluster in Riyadh suffers recurring emergency-department overcrowding. The transformation office requests "an AI model to solve ED overcrowding" with historical admissions data (4 years, per-visit records) and staffing rosters available.

**Business context.** Overcrowding drives ambulance diversions and breaches Ministry of Health wait-time targets. The levers actually available: flex-staffing 6 hours ahead, opening an overflow ward 24 hours ahead, and diverting non-urgent cases to a sister clinic in real time.

**Technical challenge.** "Solve overcrowding" is not a task. The class must decompose it into candidate framings and select by actionability: (a) regression forecasting hourly arrivals 6–24 h ahead (feeds both staffing levers); (b) per-patient triage classification at arrival (feeds diversion); (c) clustering of arrival patterns (insight, weak lever). Each framing implies different units, targets, splits (temporal, always), and metrics (quantile loss for staffing — understaffing costs more than overstaffing; recall on urgent cases for triage — with per-class costs).

**Constraints.** Ramadan and Hajj seasonality dominate arrival patterns; the model must be explainable to clinical governance; per-patient framing raises PDPL considerations that arrival-level forecasting avoids entirely — a genuine reason to prefer the aggregate framing.

**Solution approach (facilitate, don't lecture).** Have groups fill one canvas per framing, then vote with the levers in hand. The intended landing: hourly-arrivals regression with a temporal split (train ≤ 2024, test 2025), pinball loss at the 80th percentile, baseline = same-hour-last-week. Triage classification is a valid second project with its own governance track — not a reason to delay the first.

**Discussion questions.**
1. Which framing delivers value with the *least* personal data? Why does that matter under PDPL beyond compliance?
2. The same-hour-last-week baseline scores well except during Ramadan. Does that argue for a bigger model or a Ramadan feature — and how would you know?
3. Leadership wants one "overcrowding score" dashboard. What is lost when three framings are collapsed into one number?
4. Write the stop condition for the arrivals model.

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Framing canvas completeness | Process quality | 6/6 fields precise and mechanically checkable | canvas checklist review |
| Leaky columns identified | Data discipline | 3/3 planted columns flagged | lab check |
| Split reproducibility | Workflow integrity | identical class ratios across all pairs (2 d.p.) | scoreboard comparison |
| Baseline coverage | Workflow integrity | dummy + heuristic recorded for both tasks | scoreboard |
| Time from data to committed baseline | Fluency | ≤ 40 min | lab timing |
| Test-set quarantine | Workflow integrity | 0 reads of test partition before Day 4 H5 | notebook audit (grep) |

**Example benchmark table (filled during lab):**

| Artefact | Value | Beats? |
|---|---|---|
| Dummy classifier (stratified) | PR-AUC 0.141 · recall@20% 0.20 | — (floor) |
| 21-day-silence heuristic | recall@20% 0.41 | dummy ✔ |
| Dummy regressor (mean) | MAE 34.2 SAR | — (floor) |
| 3-order-average heuristic | MAE 26.8 SAR | dummy ✔ |

## Required Visuals and Training Assets

### Diagrams
1. **The end-to-end workflow map** — *Purpose:* anchor image for the whole course; reappears in every module with the current stage highlighted. *Elements:* the pipeline from business question → canvas → audit → split → baseline → iterate loop → tuning → final test → model card; a padlock icon on the test set; the iterate loop drawn as a cycle with an exit condition. *Style:* horizontal flow, flat vector, course palette, English labels with Arabic subtitles. *Designer note:* the padlock must be visually loud — it is referenced verbally ~20 times across the week.
2. **Task-taxonomy decision tree** — *Elements:* "Do you have labels?" → supervised/unsupervised; "Is the target a number or a category?" → regression/classification; leaf nodes carry one Manafeth example each. *Style:* compact flowchart, printable A4.
3. **Leakage timeline** — *Elements:* a horizontal timeline with the snapshot moment marked; features drawn as dots before it (legal) and after it (red, forbidden); `refund_issued` placed after. *Style:* single-axis timeline, before/after shading.
4. **Split geometries** — *Elements:* three panels: random split, stratified split (class ratio bars equal), temporal split (train past / test future); a red "don't" panel showing random split on time-series. *Style:* four-panel grid.

### Images (screenshots)
1. **JupyterLab screenshot — lab notebook with audit cells run**: *why:* participants mirror the expected state; *content:* shape output, churn balance, missingness table visible.
2. **Terminal/notebook screenshot — verified split output**: *why:* expected-output reference; *content:* the `0.140 / 0.140` stratification check.
3. **Scoreboard notebook screenshot**: *why:* shows the shared-baseline convention; *content:* four pairs' identical baseline rows.
4. **FRAMING.md rendered on GitHub**: *why:* framing as a reviewable artefact; *content:* the canvas table with a review comment thread on the target definition.

### Simulations
1. **The contaminated-split notebook** — *Setup:* provided notebook imputes with the global mean before splitting. *Expected behaviour:* participants detect that test-set statistics influenced training data and reorder cells. *Learning objective:* leakage is a workflow-order property, not a modelling property.
2. **The proxy-target trap** — *Setup:* an alternative target `contacted_support` is offered with 3× more positives ("easier to model!"). *Expected behaviour:* groups articulate why a better-behaved proxy can still answer the wrong question. *Learning objective:* framing precision beats statistical convenience.

### Interactive Activities
- **Framing speed-round (15 min):** six one-line business problems on cards (bank churn, road-accident hotspots, Umrah visa demand, warehouse picking errors, ad click-through, water-pipe failures); pairs assign task type, unit, target in 90 seconds each; class debates the two hardest.
- **"Leak or feature?" card sort (10 min):** 12 column-name cards from the Manafeth dictionary sorted against the timestamp test on a floor-size leakage timeline.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `manafeth_customers.csv` | Synthetic, generated by course tooling (SAR amounts, KSA cities, Ramadan seasonality, 3 planted leaky columns) | CSV + parquet mirror | 48,000 rows × 19 cols | Golden-thread churn task, all modules |
| `manafeth_orders.csv` | Synthetic, order-level companion | CSV + parquet | 610,000 rows × 11 cols | Feature engineering (M3), basket-value regression |
| `data_dictionary.md` | Course repo | Markdown | 1 page | Leakage exercise; canvas completion |

### Demo Requirements
- **Instructor demo:** frame the Manafeth problem live on the projector, filling the canvas with class input, then run split + baselines end-to-end in under 10 minutes — rehearse it; the speed *is* the message ("the disciplined path is also the fast path").
- **Student demo:** two pairs present their leaky-column findings and defend one borderline call.
- **Expected outputs:** every pair has committed FRAMING.md, a verified split, and scoreboard baselines before Hour 4.

---

# Module 2 — Supervised Learning: Regression and Classification

## Module Overview

**Purpose.** This module builds the core supervised-learning toolkit: linear regression and its regularised variants for quantities, logistic regression, decision trees, and k-nearest neighbours for categories. The goal is not a zoo of algorithms but a working mental model of each — what it optimises, where its decision boundary comes from, how it fails — so that participants can choose, train, and *distrust* models intelligently. Overfitting and underfitting are introduced here as visible, reproducible phenomena, not abstractions.

**Business relevance.** Linear and logistic regression remain the most deployed models in Saudi enterprise ML — not despite their simplicity but because of it: they are auditable (SAMA model-governance reviews routinely favour them as challengers or champions), fast to retrain, and hard to break silently. An engineer who can extract 90% of the achievable signal with an interpretable model in a day is more valuable than one who reaches for gradient boosting before establishing what "achievable" means.

**Industry use cases.**
- A Saudi finance company scores personal-loan applications with regularised logistic regression because every coefficient must be explainable to credit risk and, on appeal, to the customer.
- A facilities operator predicts district-cooling energy load with ridge regression on weather and calendar features — the coefficients themselves became the executive briefing.
- Manafeth's own thread: logistic regression gives the churn team its first honest lift over the 21-day heuristic, and its coefficients tell the CRM team *why* customers lapse.

**Expected competencies.** Participants can fit and interpret linear/ridge/lasso regression, read residual plots, fit logistic regression and interpret coefficients as log-odds, train decision trees and control their complexity, explain k-NN and its scaling sensitivity, and demonstrate overfitting/underfitting empirically with train-vs-validation curves.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Fit and interpret linear regression; diagnose fit quality from residuals | LO3, LO5 |
| 2.2 | Apply ridge and lasso regularisation and explain the bias–variance trade they make | LO3, LO6 |
| 2.3 | Fit logistic regression; interpret coefficients and predicted probabilities correctly | LO3 |
| 2.4 | Train decision trees and k-NN; control capacity via depth and k | LO3, LO6 |
| 2.5 | Produce train-vs-validation evidence of overfitting and underfitting on demand | LO6, LO2 |

## Technical Content

### 1. Linear regression as loss minimisation

Teach linear regression as the template for *all* supervised learning: a family of functions (`ŷ = Xw + b`), a loss measuring wrongness (mean squared error), and an algorithm finding the weights that minimise it (closed form or gradient descent — show the gradient-descent view because every later model in the track, through deep learning in SDA-AIE-112, is this same picture with a different function family).

Practical reading skills matter more than derivations at Practitioner level:

- **Coefficients are marginal effects in the feature's units** — "each additional order per month adds 11.3 SAR to predicted basket value, holding the rest fixed" — and the *holding fixed* clause breaks down under correlated features (multicollinearity makes individual coefficients unstable while predictions stay fine; teach the distinction, it defuses many stakeholder arguments).
- **Residual plots are the model's confession.** Random cloud = healthy; funnel shape = variance grows with the prediction (consider log-transforming the SAR target); curvature = missing non-linearity (polynomial features or a tree-based model); distinct bands = a categorical effect not yet in the model.
- **R² is relative to the mean baseline** — literally "fraction of variance explained versus DummyRegressor" — which is why the Module 1 baseline discipline makes R² intuitive rather than mystical.

### 2. Regularisation: the first overfitting control

With polynomial features, a linear model can memorise noise. Ridge (L2) and lasso (L1) add a penalty on weight size to the loss:

- **Ridge** shrinks all weights smoothly; the go-to when many features carry a little signal each.
- **Lasso** drives some weights exactly to zero — embedded feature selection; the go-to when you suspect most features are irrelevant and want the model to say so.
- The strength `alpha` is the first *hyperparameter* participants meet: a knob set by validation performance, not by fitting. Plant the flag here — Module 7 is entirely about turning this knob systematically.
- Both are scale-sensitive: penalising weights only makes sense when features share a scale — the first concrete argument for the scaling discipline of Module 3.

### 3. Logistic regression: probabilities, not just labels

Logistic regression is linear regression pushed through a sigmoid so the output lives in (0, 1) and trains against log-loss. Three teaching points carry the practical weight:

- **The output is a probability, and the probability is the product.** Manafeth doesn't need a churn *label*; it needs a *ranking* to fill a top-20% voucher budget. `predict_proba` is the deliverable; `predict`'s default 0.5 threshold is a placeholder that Module 4 replaces with a business threshold.
- **Coefficients are log-odds effects:** `exp(coef)` is an odds multiplier ("each additional support ticket multiplies churn odds by 1.6"). This is the sentence stakeholders remember.
- **`class_weight="balanced"`** re-weights the loss when positives are rare — the first of three imbalance tools in the course (with threshold tuning in M4 and `scale_pos_weight` in M5).

### 4. Decision trees and k-NN: two opposite mental models

- **Decision trees** partition feature space with axis-aligned questions, chosen greedily to reduce impurity (Gini/entropy). Strengths: no scaling needed, handles mixed types and non-linearity, and the top of a small tree is a readable business policy. Weakness: unconstrained trees memorise — a `max_depth=None` tree on Manafeth reaches train PR-AUC 1.00 and validation 0.61, the course's cleanest overfitting exhibit. Capacity knobs: `max_depth`, `min_samples_leaf`.
- **k-NN** predicts from the labels of the k closest training points — no training phase, all cost at prediction time. It exists in this course chiefly as a *teaching instrument*: k=1 overfits perfectly (train accuracy 100% by construction), large k underfits toward the majority class, and its total dependence on distance makes it the second concrete argument for feature scaling. Say explicitly: rarely the production choice on tabular data, always the cleanest illustration of the capacity dial.

### 5. Overfitting, underfitting, and the capacity dial

The unifying picture, drawn once and reused all week: model capacity on the x-axis (polynomial degree, tree depth, 1/k, 1/alpha), error on the y-axis; training error falls monotonically, validation error is U-shaped. **Underfitting** = both errors high (model too simple / features too weak); **overfitting** = training low, validation high (model learned noise). Every mitigation in the course is a move on this picture: more data flattens the right side, regularisation and capacity limits move you left, better features lift the whole achievable region. Participants generate this plot themselves in Lab 2b (tree depth 1→20) — it is the module's laboratory result, not a slide.

### 6. Common mistakes & production considerations

1. **Interpreting coefficients on unscaled features as importance ranking** — a coefficient's size reflects the feature's units; compare only after scaling (or use permutation importance, M5).
2. **Trusting `predict` when the product needs `predict_proba`** — the silent 0.5 threshold ships a business decision nobody made.
3. **Fitting k-NN or regularised models on unscaled features** — distances and penalties both become arbitrary; the model "works" and is quietly wrong.
4. **Reading train accuracy as performance** — the depth-20 tree exhibit exists to make this mistake unrepeatable.
5. **One-hot-encoding high-cardinality IDs into linear models** — 40,000 customer-ID columns = memorisation by another name.
6. **Deleting the simple model once the complex one wins** — production teams keep the linear model as the challenger/fallback; it is also the debugging oracle when the ensemble misbehaves.

Production considerations: linear/logistic models retrain in seconds and serialise in kilobytes — operationally golden; coefficient snapshots across retrains are a cheap drift detector (a coefficient that flips sign is an incident); regulated deployments often pair a complex champion with an interpretable challenger, and this module builds the challenger.

## Code Examples

### Regression: baseline → linear → regularised

```python
# notebooks/day1/lab2a_regression.ipynb — Basket-value regression, honest from the start
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42

# Numeric-only first pass (categoricals join in Module 3 via ColumnTransformer)
num_cols = ["orders_per_month", "avg_basket_sar", "days_since_last_order",
            "tenure_months", "distinct_categories", "promo_usage_rate"]

X_tr, X_val, y_tr, y_val = train_test_split(
    X_train[num_cols], y_train_basket, test_size=0.25, random_state=RANDOM_STATE)

lin = LinearRegression().fit(X_tr, y_tr)
print("linear  MAE:", round(mean_absolute_error(y_val, lin.predict(X_val)), 1))   # 22.4 SAR
print("R^2:", round(r2_score(y_val, lin.predict(X_val)), 3))                       # 0.58
# vs dummy MAE 34.2 SAR (Lab 1) — the model earns its keep; now we ask HOW it fails.

# Coefficients in business units — only meaningful with the units attached
for name, coef in sorted(zip(num_cols, lin.coef_), key=lambda t: -abs(t[1])):
    print(f"{name:26s} {coef:+8.2f} SAR")
```

```python
# notebooks/day1/lab2a_regression.ipynb — Residual plot: the model's confession
import matplotlib.pyplot as plt

pred = lin.predict(X_val)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(pred, y_val - pred, s=6, alpha=0.4)
ax.axhline(0, color="red", lw=1)
ax.set_xlabel("Predicted basket value (SAR)")
ax.set_ylabel("Residual (actual - predicted)")
ax.set_title("Funnel shape = errors grow with basket size -> try log target")
plt.tight_layout()
# Follow-up cell fits on np.log1p(y) and shows the funnel flattening.
```

### Classification: logistic regression with probabilities as the product

```python
# notebooks/day2/lab2b_classification.ipynb — Churn: rank customers, don't just label them
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import average_precision_score

scaler = StandardScaler().fit(X_tr)                 # M3 replaces this with a Pipeline —
X_tr_s, X_val_s = scaler.transform(X_tr), scaler.transform(X_val)   # note the fit-on-train-only discipline

clf = LogisticRegression(class_weight="balanced", max_iter=1000,
                         random_state=RANDOM_STATE).fit(X_tr_s, y_tr)

proba = clf.predict_proba(X_val_s)[:, 1]            # the deliverable: a risk score per customer
print("PR-AUC:", round(average_precision_score(y_val, proba), 3))    # 0.44 vs dummy 0.14

# recall@top-20%: the metric from the framing canvas
budget = int(0.20 * len(y_val))
top = np.argsort(-proba)[:budget]
print("recall@20%:", round(y_val.iloc[top].sum() / y_val.sum(), 3))  # 0.57 vs heuristic 0.41

# Odds-ratio reading for the CRM team
odds = np.exp(clf.coef_[0])
for name, o in sorted(zip(num_cols, odds), key=lambda t: -abs(np.log(t[1]))):
    print(f"{name:26s} odds x{o:.2f}")
```

### The overfitting exhibit: tree depth sweep

```python
# notebooks/day2/lab2b_classification.ipynb — Generate the course's key plot yourself
from sklearn.tree import DecisionTreeClassifier

depths = range(1, 21)
train_scores, val_scores = [], []
for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, class_weight="balanced",
                                  random_state=RANDOM_STATE).fit(X_tr, y_tr)
    train_scores.append(average_precision_score(y_tr, tree.predict_proba(X_tr)[:, 1]))
    val_scores.append(average_precision_score(y_val, tree.predict_proba(X_val)[:, 1]))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(depths, train_scores, marker="o", label="train PR-AUC")
ax.plot(depths, val_scores, marker="s", label="validation PR-AUC")
ax.axvline(depths[int(np.argmax(val_scores))], ls="--", color="grey",
           label=f"best depth = {depths[int(np.argmax(val_scores))]}")
ax.set_xlabel("max_depth (model capacity)")
ax.legend(); ax.set_title("Training score rises forever; validation tells the truth")
# Expected: train -> 1.00 by depth ~16; validation peaks ~depth 6 at ~0.46 then decays.
```

## Hands-on Lab 2 — First Honest Models (Parts A and B)

| | |
|---|---|
| **Objective** | Beat both Lab 1 baselines with interpretable models: linear/ridge regression for basket value, logistic regression + capacity-controlled tree for churn; produce the overfitting plot from your own runs |
| **Duration** | 2 × 50 min (Day 1 H5 + Day 2 H2) |
| **Setup** | Lab 1 artefacts committed; `notebooks/day1/lab2a_regression.ipynb` and `notebooks/day2/lab2b_classification.ipynb` skeletons |

**Part A tasks (50 min — regression)**
1. Fit `LinearRegression` on the numeric features; record MAE/R² vs the dummy on the scoreboard (10 min).
2. Plot residuals vs predictions; diagnose the funnel; refit on `log1p(target)` and compare MAE in SAR after back-transform (15 min).
3. Fit `Ridge` and `Lasso` over `alpha ∈ {0.01, 0.1, 1, 10, 100}` on scaled features; plot validation MAE vs alpha; note which lasso coefficients hit zero and sanity-check them against domain sense (15 min).
4. Write a three-sentence markdown summary: best model, MAE in SAR, one surprising coefficient (10 min).

**Part B tasks (50 min — classification)**
1. Fit `LogisticRegression(class_weight="balanced")` on scaled features; record PR-AUC and recall@top-20%; compare against the 21-day heuristic (15 min).
2. Produce the odds-ratio table; write the one sentence the CRM team would quote (5 min).
3. Run the depth-1→20 tree sweep; produce the overfitting plot; mark best depth (15 min).
4. Fit k-NN with k ∈ {1, 5, 25, 101} on scaled and *unscaled* features; observe the scaling collapse (10 min).
5. Commit: `feat(lab2): linear+logistic beat baselines; overfitting exhibit` (5 min).

**Expected outputs**
```
Regression:  linear MAE 22.4 SAR | log-target 21.1 SAR | ridge(alpha=10) 20.8 SAR   [dummy 34.2]
Churn:       logreg PR-AUC 0.44, recall@20% 0.57        [dummy 0.14 / heuristic 0.41]
Tree sweep:  train PR-AUC -> 1.00 by depth 16; validation peak 0.46 @ depth 6
k-NN:        k=1 train acc 1.00/val PR-AUC 0.31; unscaled k=25 PR-AUC 0.19 (distance dominated by tenure_months)
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `ConvergenceWarning` on logistic regression | Unscaled features | Scale first (or raise `max_iter`) — and connect to why M3 pipelines exist |
| Lasso zeroes *all* coefficients | `alpha` too large on scaled target | Sweep alpha logarithmically; inspect the path |
| Validation curve is noisy / peak moves between runs | Small validation slice, no seed | Fix `random_state`; foreshadow CV (M4) as the real fix |
| recall@20% ≈ 0.20 despite good PR-AUC | Ranked by `predict` labels, not probabilities | Rank by `predict_proba[:, 1]` |
| MAE improves but predictions negative | Log-transform back-transformed incorrectly | Use `np.expm1(pred)`; assert non-negativity |

**Instructor notes.** The depth-sweep plot is the module's money shot — have every pair post theirs to the shared board; identical shapes with identical seeds reinforce the deterministic-workflow message. Let one pair discover the k-NN unscaled collapse naturally, then diagnose it on the projector with a two-column distance calculation: `tenure_months` (0–120) crushes `promo_usage_rate` (0–1). That 3-minute arithmetic sells Module 3's scaling content better than any slide. Fast finishers: `PolynomialFeatures(degree=2)` + ridge on regression — a preview of feature engineering paying off.

## Mini Exercises

**Quiz.** (1) Ridge vs lasso in one sentence each, and when do you want lasso's behaviour? (2) `exp(coef) = 1.6` on `support_tickets` — say it in business language. (3) Why does k=1 always score perfectly on training data? (4) Train PR-AUC 0.98, validation 0.55 — name the condition and two mitigations. (5) Why must features be scaled before k-NN and regularised regression but not before decision trees?
**Debugging exercise.** Branch notebook `sim-scale-leak`: `StandardScaler` fit on train+validation concatenated. Scores barely move — participants must explain why this is *still* wrong (workflow contamination compounds; with smaller data or stronger shift it inflates), fix it, and state the rule: fit transforms on training data only.
**Code-review exercise.** Review a notebook that (a) reports train accuracy as "model accuracy", (b) one-hot encodes `customer_id`, (c) picks the classification threshold by eyeballing validation accuracy. Three findings with fixes.
**Discussion.** The logistic model catches 57% of churners at the 20% budget; the depth-6 tree catches 55% but its top three splits are a readable policy. Which ships first, and what would change your answer?

## Case Study — Used-Car Price Prediction at a Saudi Auto Marketplace

**Scenario.** "Markabat", a Riyadh-based online used-car marketplace, prices trade-in offers manually through three senior buyers. Offers take 4 hours, buyers disagree by up to 18%, and weekend listing surges go unpriced. The data: 90,000 historical listings with sale prices, make/model/year/mileage/city/condition photos-count, and time-on-platform.

**Business context.** A trade-in offer accepted within minutes converts 3× better. But an offer 10% above market loses money on every car, and an offer 10% below drives sellers to competitors — asymmetric costs on an illiquid inventory.

**Technical challenge.** Frame and build the first pricing model: regression on sale price (log-transformed — car prices span 8k to 900k SAR), temporal split (market prices drift; a random split would leak future market levels), MAE reported in SAR *and* in percentage terms per price band. Ridge on engineered features (age, km/year, make-model frequency encoding) is the deliberate first model: every coefficient will be challenged by the senior buyers, and surviving that review is the adoption gate.

**Constraints.** The buyers must be able to override with a logged reason (human-in-the-loop by design); rare models (< 30 sales) need a fallback rule, not a hallucinated prediction; price predictions for cars older than the training range must refuse rather than extrapolate.

**Solution approach.** Baseline = same-model-median price (beats dummy by miles; the model must beat *it*); log-target ridge with residual analysis *per make* exposes where the linear model underserves (luxury segment curvature → the M5 handoff argument); prediction intervals via residual quantiles give buyers a range, not a point — which is what they actually asked for when interviewed.

**Discussion questions.** (1) Why is the temporal split non-negotiable here, and what exact failure would a random split hide? (2) The model is 2% better on MAE but the buyers trust their medians — design the two-week shadow trial that settles it. (3) Which is the right error currency for the CFO: SAR, %, or margin-weighted? (4) Where does this framing put the refuse-to-predict boundary, and what does the API return there (connects to SDA-AIE-113)?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Regression MAE vs dummy | Model quality | ≥ 35% improvement (≤ 22.5 SAR vs 34.2) | scoreboard |
| Churn PR-AUC vs dummy | Model quality | ≥ 3× dummy (≥ 0.42) | scoreboard |
| recall@top-20% vs heuristic | Business metric | ≥ heuristic + 10 pts (≥ 0.51) | scoreboard |
| Overfitting exhibit produced | Diagnostic skill | plot with train/val divergence + marked peak | lab check |
| Coefficient interpretation | Communication | 1 correct business sentence per model | markdown cell review |
| Train-metric reporting errors | Discipline | 0 (all scoreboard entries are validation metrics) | scoreboard audit |

**Example benchmark table:**

| Model | Task | Validation score | Beats baseline? |
|---|---|---|---|
| LinearRegression | basket MAE | 22.4 SAR | ✔ (34.2) |
| Ridge(alpha=10), log target | basket MAE | 20.8 SAR | ✔ |
| LogisticRegression (balanced) | churn PR-AUC / recall@20% | 0.44 / 0.57 | ✔ (0.14 / 0.41) |
| DecisionTree(depth=6) | churn PR-AUC | 0.46 | ✔ |
| DecisionTree(depth=None) | churn PR-AUC | 0.61 val, **1.00 train** | overfit exhibit |

## Required Visuals and Training Assets

### Diagrams
1. **The capacity dial (bias–variance U-curve)** — *Purpose:* the module's unifying image, reused in M5 and M7. *Elements:* capacity axis annotated with tree depth / polynomial degree / 1/k / 1/alpha; train curve descending, validation U-curve; under/overfit zones shaded; "more data", "regularisation", "better features" arrows showing their effects. *Style:* single chart, flat vector, course palette. *Designer note:* leave a blank margin — instructors annotate live.
2. **Decision-boundary triptych** — *Elements:* the same 2-D slice of Manafeth data under logistic regression (straight boundary), depth-3 tree (axis-aligned boxes), k-NN k=5 (organic islands). *Style:* three panels, identical axes, matched colours.
3. **Sigmoid bridge** — *Elements:* linear score axis → sigmoid → probability axis, with one customer's features flowing through to `p=0.72` and the odds-ratio reading called out. *Style:* left-to-right flow.
4. **Residual-pattern field guide** — *Elements:* four mini residual plots (healthy cloud, funnel, curvature, bands) each with its diagnosis and fix. *Style:* 2×2 quadrant card, printable.

### Images
1. **Notebook screenshot — coefficient table with SAR units**: *why:* interpretation convention; *content:* sorted coefficients with sign colouring.
2. **The depth-sweep plot from the reference solution**: *why:* expected-shape reference for Lab 2b; *content:* train→1.0, validation peak at depth 6.
3. **Residual funnel before/after log transform**: *why:* diagnose-then-fix pattern; *content:* two panels, same axes.
4. **Scoreboard after Day 2**: *why:* progress narrative; *content:* baseline rows now dominated by model rows across all pairs.

### Simulations
1. **The unscaled k-NN collapse** — *Setup:* Lab 2b step 4 as written. *Expected:* PR-AUC drops toward dummy when `tenure_months` dominates distances. *Learning objective:* scale sensitivity is a property of the algorithm class, not a style preference.
2. **Coefficient instability under collinearity** — *Setup:* provided notebook adds `orders_per_quarter = 3×orders_per_month + noise`; coefficients on both swing wildly between CV folds while MAE holds. *Expected:* participants distinguish "prediction is fine" from "interpretation is broken". *Learning objective:* multicollinearity's real cost.
3. **The memorising tree** — *Setup:* `max_depth=None` on the full feature set including a re-planted `customer_id_hash`. *Expected:* perfect training score; validation collapse; feature importance exposes the ID. *Learning objective:* IDs are leakage vectors for high-capacity models.

### Interactive Activities
- **Model-choice speed debate (10 min):** four scenarios (credit appeal process, hourly load forecast, in-app instant ranking, exec one-pager); pairs assign linear/logistic/tree/k-NN with one-line justifications.
- **Human gradient descent (10 min, energiser):** the class minimises a projected 2-D loss surface by shouting weight updates; the instructor plots each step — makes "learning = loss minimisation" kinaesthetic before SDA-AIE-112 needs it.

### Datasets
Same golden-thread artefacts as Module 1 (`manafeth_customers`, `manafeth_orders`); plus `markabat_listings_sample.csv` (2,000 rows, synthetic) for the case-study residual demo. No new primary datasets — the thread holds.

### Demo Requirements
- **Instructor demo:** live build of logistic churn model from split to recall@20% in 8 minutes, narrating each decision against the workflow map; then the depth-sweep run live (it takes ~20 s — let the room watch the divergence appear).
- **Student demo:** two pairs present their overfitting plots and defend their chosen depth.
- **Expected outputs:** every pair's scoreboard shows both baselines beaten by end of Day 2 Hour 2; the overfitting plot is committed — it reappears as evidence in the capstone rubric.

---

# Module 3 — Feature Engineering and Preprocessing Pipelines

## Module Overview

**Purpose.** Models are only as good as the matrix they see. This module teaches the transformations that turn raw enterprise data into model-ready features — imputation, scaling, encoding, datetime and aggregate features — and, more importantly, the *packaging discipline* that keeps those transformations honest: every transformation lives inside a scikit-learn `Pipeline` with a `ColumnTransformer`, fit on training data only, applied identically everywhere. The pipeline is simultaneously the anti-leakage weapon and the deployable artefact.

**Business relevance.** In practice, feature work moves metrics more than model choice: on tabular enterprise problems, a well-engineered feature routinely outperforms a model upgrade. Equally, preprocessing is where production ML dies quietly — a scaler fit on the full dataset, an encoder that crashes on an unseen city, an imputation computed after the split. Saudi enterprises deploying under governance (SAMA, NDMO data controls) increasingly ask teams to *show* that preprocessing cannot leak — a fitted `Pipeline` object is precisely that evidence.

**Industry use cases.**
- A Saudi bank's credit model encodes 200+ merchant categories with target encoding inside a CV-safe pipeline — done naively, target encoding is the single most common leakage source in industry.
- Manafeth's thread: RFM aggregates from the orders table, a Ramadan-proximity flag, and city-tier encoding lift churn PR-AUC more than any Day 3 model change will.
- A utilities company imputes smart-meter gaps differently for missing-at-random (sensor dropout) vs structural (new installation) reasons — the missingness *indicator* itself becomes a predictive feature.

**Expected competencies.** Participants can build a `ColumnTransformer` covering numeric/categorical/datetime columns, choose imputation and encoding strategies per column with reasons, engineer aggregate features from a transactional table without temporal leakage, and explain why the fitted pipeline object is the unit that ships.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Select and apply imputation strategies, including missingness indicators | LO4 |
| 3.2 | Apply scaling and encoding correctly per feature type and model class | LO4, LO3 |
| 3.3 | Compose preprocessing + model into a single `Pipeline`/`ColumnTransformer` | LO3, LO2 |
| 3.4 | Engineer datetime and aggregate (RFM) features under the prediction-time rule | LO4, LO1 |
| 3.5 | Detect and eliminate preprocessing leakage in a given notebook | LO6 |

## Technical Content

### 1. Missing values: impute with a reason

Imputation choices are modelling decisions, not cleanup chores:

- **Numeric:** median (robust default), mean (only for symmetric distributions), or model-based (`KNNImputer` — rarely worth it at this level). Constant `0` only when zero is meaningful ("no promo used").
- **Categorical:** explicit `"missing"` category usually beats mode imputation — absence is information.
- **The indicator trick:** `SimpleImputer(add_indicator=True)` appends a was-missing flag. On Manafeth, `avg_rating` is missing for 31% of customers — overwhelmingly *new* customers, who churn differently. The indicator carries the signal the imputed value erases.
- **The order rule:** imputation statistics are *learned parameters*. Median computed on the full dataset = test-set information in the training matrix. Inside a `Pipeline`, this mistake becomes unwritable — the strongest argument for the packaging discipline.
- Know the difference between missing-at-random and structural missingness; the fix differs (impute vs redesign the feature), and misdiagnosis is common in enterprise data where "missing" often means "not applicable".

### 2. Scaling: who needs it and why

| Model family | Needs scaling? | Why |
|---|---|---|
| Linear/logistic + regularisation | **Yes** | Penalty compares weight sizes across features |
| k-NN, SVM, k-means, PCA | **Yes** | Distance/variance computations mix units |
| Decision trees, random forests, gradient boosting | **No** | Splits are order-based; monotone transforms are invisible |

Tools: `StandardScaler` (default), `MinMaxScaler` (bounded inputs, e.g., for neural nets in SDA-AIE-112), `RobustScaler` (heavy outliers — Manafeth basket values have a long tail of bulk orders). Two rules: fit on train only (the Module 2 lesson, now automated), and *never scale the target silently* — if you transform `y`, own the back-transform in the metric.

### 3. Encoding categoricals: the cardinality ladder

- **One-hot (`OneHotEncoder(handle_unknown="ignore")`)** — the default for low cardinality (Manafeth: `city` (3), `device` (2), `payment_method` (4)). `handle_unknown="ignore"` is non-negotiable in production: the first unseen category otherwise crashes the service — the classic "works until the Taif launch" incident.
- **Ordinal (`OrdinalEncoder`)** — only when order is real (`city_tier` 1<2<3). Arbitrary ordinal encoding into linear models invents relationships; into trees it merely costs a little split efficiency.
- **Frequency / target encoding** — the high-cardinality tools (hundreds of merchant categories, thousands of SKUs). Target encoding replaces a category with the target mean *for that category* — powerful and dangerous: computed naively it leaks the label into the features. It must be fit inside CV (each fold's encoding learned from that fold's training part only); at Practitioner level, teach frequency encoding as the safe default and target encoding as "know the hazard, use library implementations, verify with the leakage test".
- **The ID rule (from M2):** identifiers are never features. High-cardinality encodings of quasi-IDs (exact GPS points, full postcodes) are IDs wearing a costume.

### 4. Datetime and aggregate features: where the lift lives

Datetimes are unusable raw and gold once decomposed: hour, day-of-week, month, `is_weekend` (Fri/Sat in KSA — a locale bug in every imported code sample; make the room find it), days-since-event, and cyclical encodings (`sin/cos` of hour) when models must know 23:00 borders 00:00. Domain calendars matter more than any of these in the Saudi market: Ramadan proximity, Eid windows, school terms, salary days (27th) — Manafeth order volume doubles in Ramadan evenings, and a `days_to_ramadan` feature captures what no generic component can.

Aggregates from the orders table are the module's heavy lift: RFM (recency, frequency, monetary) per customer — `days_since_last_order`, `orders_90d`, `avg_basket_90d`, `basket_trend` (last-30d vs prior-60d ratio). The temporal discipline from Module 1 applies *inside* the groupby: aggregates use only orders **before the snapshot date**. An aggregate over all orders is leakage by construction — it summarises the future. This is the course's second planted-leak hunt (Lab 3), and the most production-realistic one.

### 5. Pipelines and ColumnTransformer: the packaging discipline

`Pipeline` chains steps so that `fit` learns all parameters from training data and `transform` replays them identically; `ColumnTransformer` routes column groups to their own preprocessing. Consequences worth stating as doctrine:

1. **Leakage-proof by construction:** cross-validation of a `Pipeline` refits preprocessing inside every fold — the *only* mechanically safe way to combine CV with learned transforms (Module 4 depends on this; Module 7 tunes preprocessing and model jointly because of it).
2. **One artefact:** the fitted pipeline serialises as a single object; the serving side (SDA-AIE-113) calls `pipeline.predict(raw_row)` and cannot skew preprocessing against training — the training/serving-skew defence at the object level.
3. **Reviewable:** `set_config(display="diagram")` renders the pipeline as an HTML diagram in the notebook — the preprocessing *is* the documentation.

### 6. Common mistakes & production considerations

1. Fitting any transformer before the split, or on train+validation concatenated (the M2 simulation, now formalised as banned).
2. `handle_unknown` left at default → first unseen category is a production crash.
3. Target encoding computed on the full training set, evaluated with CV → optimistic scores that evaporate in production; the most expensive leak in industry tabular ML.
4. Aggregates computed over all time → future information in every row; offline metrics become fiction.
5. Dropping rows with any missing value → silently biases the population (new customers vanish from Manafeth training data — precisely the churn-prone segment).
6. Pipeline-less notebooks where preprocessing exists as 14 scattered cells → unreproducible, unreviewable, undeployable.

Production considerations: the fitted pipeline is versioned *with* the model (they are one artefact); feature lists in `FRAMING.md` are contracts — adding a feature is a reviewed change; expensive aggregates get precomputed in feature pipelines/stores at scale (pointer to SDA-DSC-214), but the prediction-time rule travels unchanged.

## Code Examples

### The course preprocessing pipeline

```python
# src/manafeth/features.py — single source of preprocessing truth, imported by every later notebook
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUM_COLS = ["orders_per_month", "avg_basket_sar", "days_since_last_order",
            "tenure_months", "distinct_categories", "promo_usage_rate",
            "avg_rating", "orders_90d", "basket_trend", "days_to_ramadan"]
CAT_COLS = ["city", "device", "payment_method"]

def build_preprocessor() -> ColumnTransformer:
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median", add_indicator=True)),  # indicator: missingness is signal
        ("scale", StandardScaler()),
    ])
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),  # Taif launch survives
    ])
    return ColumnTransformer([
        ("num", numeric, NUM_COLS),
        ("cat", categorical, CAT_COLS),
    ], remainder="drop", verbose_feature_names_out=True)  # drop: unlisted columns NEVER leak in silently
```

```python
# notebooks/day2/lab3_pipelines.ipynb — Preprocessing + model as ONE object
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import set_config

from manafeth.features import build_preprocessor

set_config(display="diagram")            # the pipeline renders itself — preprocessing as documentation

churn_model = Pipeline([
    ("prep", build_preprocessor()),
    ("clf", LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)),
])
churn_model.fit(X_train, y_train)        # ALL preprocessing parameters learned here, from train only
proba = churn_model.predict_proba(X_valid)[:, 1]    # raw dataframe in, risk score out — nothing to skew
```

### Temporal-safe RFM aggregates from the orders table

```python
# src/manafeth/features.py — aggregates obey the prediction-time rule INSIDE the groupby
import pandas as pd

def rfm_features(orders: pd.DataFrame, snapshot: pd.Timestamp) -> pd.DataFrame:
    """RFM aggregates using only orders BEFORE the snapshot.

    An aggregate over all orders summarises the future = leakage by construction.
    """
    past = orders[orders["order_ts"] < snapshot]                    # the load-bearing line
    g = past.groupby("customer_id")
    feats = pd.DataFrame({
        "days_since_last_order": (snapshot - g["order_ts"].max()).dt.days,
        "orders_90d": g["order_ts"].apply(
            lambda s: (s >= snapshot - pd.Timedelta(days=90)).sum()),
        "avg_basket_90d": g.apply(
            lambda d: d.loc[d["order_ts"] >= snapshot - pd.Timedelta(days=90),
                            "basket_sar"].mean()),
    })
    last30 = past[past["order_ts"] >= snapshot - pd.Timedelta(days=30)]
    prior60 = past[(past["order_ts"] < snapshot - pd.Timedelta(days=30))
                   & (past["order_ts"] >= snapshot - pd.Timedelta(days=90))]
    feats["basket_trend"] = (last30.groupby("customer_id")["basket_sar"].mean()
                             / prior60.groupby("customer_id")["basket_sar"].mean()).fillna(1.0)
    return feats.reset_index()
```

### KSA calendar features

```python
# src/manafeth/features.py — the features generic tutorials never have
RAMADAN_START = {2025: pd.Timestamp("2025-03-01"), 2026: pd.Timestamp("2026-02-18")}

def calendar_features(df: pd.DataFrame, ts_col: str = "snapshot_date") -> pd.DataFrame:
    out = df.copy()
    ts = out[ts_col]
    out["is_weekend"] = ts.dt.dayofweek.isin([4, 5]).astype(int)   # Fri/Sat in KSA — NOT Sat/Sun
    out["days_to_ramadan"] = ts.apply(
        lambda d: min((start - d).days % 365 for start in RAMADAN_START.values()))
    out["near_salary_day"] = ts.dt.day.isin([26, 27, 28, 29]).astype(int)
    return out
```

### The leakage test — proving a pipeline is honest

```python
# notebooks/day2/lab3_pipelines.ipynb — If shuffled labels score above chance, something leaks
import numpy as np
from sklearn.model_selection import cross_val_score

rng = np.random.default_rng(42)
y_shuffled = pd.Series(rng.permutation(y_train.values), index=y_train.index)

score = cross_val_score(churn_model, X_train, y_shuffled, cv=5,
                        scoring="average_precision").mean()
print("PR-AUC on shuffled labels:", round(score, 3))
# ≈ 0.14 (chance) -> pipeline is honest. Materially above 0.14 -> a feature or a step leaks the label.
```

## Hands-on Lab 3 — Build the Pipeline, Hunt the Leaks

| | |
|---|---|
| **Objective** | Deliver `build_preprocessor()` + the full churn pipeline; engineer RFM and calendar features that lift PR-AUC; find all three leaks in the sabotaged notebook; pass the shuffled-label test |
| **Duration** | 50 min (Day 2 H4) + workshop hour (Day 2 H5) |
| **Setup** | Lab 2 artefacts; `notebooks/day2/lab3_pipelines.ipynb` skeleton + `notebooks/day2/sabotaged_features.ipynb` |

**Tasks**
1. *(10 min)* Implement `build_preprocessor()` per the template; fit the logistic pipeline; confirm the score matches Lab 2b within noise (the pipeline changes packaging, not math).
2. *(15 min)* Implement `rfm_features()` with the snapshot filter; join onto the training frame; refit; record the PR-AUC lift on the scoreboard.
3. *(10 min)* Add `calendar_features()`; verify the KSA weekend definition with a spot check on a known Friday; refit and record.
4. *(10 min)* Leakage hunt in `sabotaged_features.ipynb` — three planted leaks: scaler fit before split; RFM computed without the snapshot filter; target encoding of `city` using full-train target means evaluated under CV. Document each with the one-line fix.
5. *(5 min)* Run the shuffled-label test on your final pipeline; commit `feat(lab3): leakage-proof pipeline + RFM/calendar features` with the test output in the message.

**Workshop hour (Day 2 H5):** pairs propose one new domain feature each (from the orders table only), implement it inside the pipeline, and post before/after PR-AUC; the class votes on the most valuable feature per compute cost.

**Expected outputs**
```
Pipeline (numeric+cat, no new features):  PR-AUC 0.45   (Lab 2b parity ✔)
+ RFM aggregates:                          PR-AUC 0.52   (+0.07 — features beat models)
+ calendar features:                       PR-AUC 0.54
Leak hunt: 3/3 found (scaler-order, unfiltered RFM, naive target encoding)
Shuffled-label test: PR-AUC 0.14 ✔ honest
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| `ValueError: could not convert string` at fit | Categorical column routed to numeric branch | Check `NUM_COLS`/`CAT_COLS` against `df.dtypes` |
| Score explodes to 0.97 after adding aggregates | Snapshot filter missing → future orders in features | Restore `order_ts < snapshot`; re-run shuffled-label test |
| Unseen city crashes `transform` | `handle_unknown` not set | `OneHotEncoder(handle_unknown="ignore")` |
| `basket_trend` full of `inf` | Division by zero prior-60d mean | `fillna(1.0)` + `replace([inf], 1.0)`; discuss cold-start customers |
| Pipeline score ≠ Lab 2b score | Different feature list, or scaler previously fit on val too | Diff `NUM_COLS`; the pipeline number is the *correct* one |

**Instructor notes.** The moment PR-AUC jumps to 0.97 for pairs that forget the snapshot filter is the best teaching gift of the week — do not pre-warn; let it happen, then ask the room "who believes this number?" before showing the filter. The shuffled-label test then becomes a tool they trust because it caught *their* bug. Keep the workshop-hour vote honest by requiring before/after numbers from the same seed.

## Mini Exercises

**Quiz.** (1) Why does `add_indicator=True` help on `avg_rating`? (2) Which model families need scaling and which don't — and why? (3) What exactly does `handle_unknown="ignore"` prevent in production? (4) Why must target encoding be fit inside each CV fold? (5) State the prediction-time rule for aggregate features in one sentence.
**Debugging exercise.** A pipeline scores PR-AUC 0.54 in the notebook but 0.31 when a colleague applies the *saved preprocessing steps by hand* to new data. Cause: they re-fit the scaler on the new data instead of using the fitted pipeline. Lesson: ship the object, not the recipe.
**Code-review exercise.** Review a PR adding features: `OrdinalEncoder` on `payment_method` feeding logistic regression, `dropna()` on the whole frame, an aggregate `total_lifetime_orders` without a time filter. Three findings with severity ranking.
**Discussion.** The workshop's winning feature costs a 610k-row groupby per scoring run. Who pays that cost at serving time, and what would you tell the SDA-AIE-113 team?

## Case Study — SME Loan Features and the Leak That Approved Itself

**Scenario.** A Saudi fintech lending to SMEs built a default-risk model with impressive offline PR-AUC (0.81). Three months after launch, realised default rates among approved loans ran far above prediction. The audit found the culprit feature: `months_since_last_arrears`, computed from the *current* collections table — for loans that later defaulted, the collections process itself had updated the field. The feature encoded the outcome.

**Business context.** Under SAMA-style model governance the lender must now evidence, for every feature, *when* its value becomes known relative to the decision moment. The remediation is not deleting one column — it is rebuilding the feature layer with a prediction-time contract.

**Technical challenge.** Reconstruct the feature set as-of the application date: every feature computed from tables filtered to `event_ts < application_ts` (exactly Lab 3's snapshot discipline, at production scale); rebuild training data by replaying historical snapshots; re-estimate honest performance (PR-AUC falls to 0.66 — the true number the business must plan around).

**Constraints.** Historical tables were overwritten in place (no event log) for two source systems — those features must be dropped or rebuilt from backups; the model must stay in production during remediation with a widened manual-review band; the regulator receives the before/after evidence pack.

**Solution approach.** Feature-by-feature timestamp audit (the framing-canvas question 4, industrialised); as-of joins against event-sourced tables; the shuffled-label test added to the retraining pipeline as a permanent gate; the 0.81→0.66 delta communicated as "we removed fiction, not performance". Connect forward: event-sourced feature stores (SDA-DSC-214) exist because of exactly this failure class.

**Discussion questions.** (1) Why did the leak survive code review but not the production ledger? (2) Which of this module's three tools (pipeline packaging, snapshot filtering, shuffled-label test) would have caught it earliest, and at what cost? (3) Draft the two-sentence explanation of the PR-AUC drop for the credit committee. (4) The team proposes keeping the leaky model "because it's more accurate" — dismantle that sentence.

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| PR-AUC lift from engineered features | Model quality | ≥ +0.07 over Lab 2b pipeline | scoreboard |
| Leak hunt | Data discipline | 3/3 planted leaks found and fixed | lab check |
| Shuffled-label test | Workflow integrity | PR-AUC within ±0.02 of class rate | notebook output |
| Unseen-category robustness | Production readiness | `transform` on a "Taif" row succeeds | provided assert cell |
| Preprocessing packaging | Production readiness | 0 transforms outside the Pipeline in final notebook | notebook audit |
| Pipeline fit/transform wall-clock | Performance | ≤ 30 s full training frame on lab laptop | `%%time` |

**Example benchmark table:**

| Pipeline variant | PR-AUC | recall@20% | Honest? (shuffled test) |
|---|---|---|---|
| Lab 2b features, packaged | 0.45 | 0.58 | ✔ 0.14 |
| + RFM (snapshot-filtered) | 0.52 | 0.63 | ✔ 0.14 |
| + calendar | 0.54 | 0.65 | ✔ 0.14 |
| + RFM (unfiltered — the bug) | 0.97 | 0.94 | ✘ 0.41 — fiction |

## Required Visuals and Training Assets

### Diagrams
1. **Pipeline anatomy** — *Purpose:* the module's anchor. *Elements:* raw dataframe → `ColumnTransformer` splitting into numeric branch (impute+indicator → scale) and categorical branch (impute → one-hot) → concatenated matrix → estimator; `fit` arrows annotated "learns on train only", `transform` arrows "replays everywhere". *Style:* left-to-right plumbing diagram matching sklearn's HTML rendering so the notebook diagram feels familiar. *Designer note:* colour the learned-parameter boxes distinctly — "these are what leak when misused."
2. **The cardinality ladder** — *Elements:* encoding choices stacked by cardinality (one-hot → ordinal-if-ordered → frequency → target-with-CV) with hazard icons increasing upward. *Style:* ladder/stairs, printable.
3. **Snapshot-filtered aggregation** — *Elements:* one customer's order timeline; snapshot line; orders before it flowing into RFM boxes, orders after it greyed out with a red X. *Style:* timeline with aggregation funnels; pairs with M1's leakage timeline.
4. **Ship-the-object** — *Elements:* two panels: "recipe" (14 notebook cells re-applied by hand, skew icon) vs "object" (one fitted pipeline serialised, identical at train and serve). *Style:* before/after split.

### Images
1. **sklearn HTML pipeline diagram screenshot** — *why:* expected notebook state; *content:* the full churn pipeline rendered via `set_config(display="diagram")`.
2. **Scoreboard after feature lifts** — *why:* "features beat models" made visible; *content:* +0.07 RFM jump highlighted.
3. **The 0.97 leak screenshot** — *why:* what fiction looks like; *content:* unfiltered-RFM run next to the shuffled-label test failing at 0.41.
4. **Missingness heatmap (matplotlib)** — *why:* audit habit; *content:* `avg_rating` block structure aligned with low tenure.

### Simulations
1. **The unfiltered aggregate** — *Setup:* Lab 3 task 2 without pre-warning. *Expected:* PR-AUC 0.97; shuffled-label test exposes it. *Learning objective:* too-good-to-be-true has a test.
2. **The Taif launch** — *Setup:* scoring file with an unseen city under a default `OneHotEncoder`. *Expected:* crash; fix with `handle_unknown="ignore"`; discuss monitoring unseen-category rates in production. *Learning objective:* encoders are production interfaces.
3. **Naive target encoding** — *Setup:* provided notebook target-encodes `city` on full training data, CV score jumps +0.04, holdout shows nothing. *Expected:* participants explain the fold-leak mechanism. *Learning objective:* the most expensive leak in industry, experienced safely.

### Interactive Activities
- **Feature bazaar (workshop hour):** pairs pitch one engineered feature with before/after evidence; class allocates a fictional 100-SAR compute budget across pitches.
- **"Impute or indicate?" card round (10 min):** eight missingness scenarios (sensor dropout, not-applicable, survey refusal, new customer…) sorted to strategies with reasons.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `manafeth_orders.csv` | Golden thread (from M1) | CSV/parquet | 610,000 × 11 | RFM aggregation source |
| `sabotaged_features.ipynb` | Course repo (3 planted leaks) | notebook | — | Leak hunt |
| `scoring_taif.csv` | Course repo | CSV | 200 rows | Unseen-category simulation |

### Demo Requirements
- **Instructor demo:** assemble the full pipeline live from an empty cell, ending with the HTML diagram; then break it live (unfiltered RFM) and let the shuffled-label test catch it on the projector.
- **Student demo:** workshop-hour feature pitches (all pairs, 90 seconds each).
- **Expected outputs:** every pair enters Day 3 with a leakage-proof pipeline at PR-AUC ≥ 0.52 — it is the substrate Module 4 evaluates and Module 5 upgrades.

---

# Module 4 — Model Evaluation, Metrics, and Cross-Validation

## Module Overview

**Purpose.** Evaluation is where ML earns or forfeits trust. This module gives participants the full evaluation toolkit — regression and classification metrics, cross-validation, learning and validation curves, calibration awareness, and structured error analysis — and the judgement to match metric to business decision. The through-line: a single score is never the deliverable; the deliverable is an evaluation *argument* a sceptic can audit.

**Business relevance.** Enterprises do not lose money to low accuracy; they lose it to the wrong metric optimised confidently. A 99%-accurate fraud model that catches no fraud, a demand forecast rewarded for average error while stockouts happen in the tail, a churn model evaluated on a random split of time-ordered data — all are metric failures, not model failures. In regulated Saudi sectors, model validation is a formal function (SAMA model risk management); the skills in this module are exactly what an internal validator asks for.

**Industry use cases.**
- Manafeth's thread: PR-AUC and recall@top-20% replace accuracy because the voucher budget, not the class ratio, defines success; threshold tuning converts a score into a defensible operating point.
- A Saudi bank's credit model reports AUC to analysts but *approval rate at fixed bad-rate* to the business — the same model, two audiences, two metrics, one truth.
- A grid operator evaluates load forecasts with pinball (quantile) loss because under-forecasting at peak costs blackout risk while over-forecasting costs fuel — asymmetric, like most real losses.

**Expected competencies.** Participants can choose and compute appropriate metrics for regression and classification (including imbalanced problems), run stratified k-fold cross-validation on full pipelines, read confusion matrices, ROC and PR curves, tune decision thresholds against business constraints, generate learning/validation curves, and run slice-based error analysis that produces feature ideas rather than just numbers.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Select metrics that match the business decision, for regression and classification | LO5, LO1 |
| 4.2 | Explain why accuracy misleads under imbalance; use PR-AUC, ROC-AUC, F1 appropriately | LO5 |
| 4.3 | Run stratified k-fold CV on pipelines and interpret fold variance | LO5, LO2 |
| 4.4 | Tune the decision threshold against an explicit business constraint | LO5 |
| 4.5 | Diagnose over/underfitting with learning and validation curves; run slice-based error analysis | LO6, LO5 |

## Technical Content

### 1. Regression metrics: the error currency

- **MAE** — mean absolute error, in target units; robust, and the one to put in front of the business ("on average we miss basket value by 19 SAR").
- **RMSE** — squares errors first, so large misses dominate; choose it when big errors are disproportionately costly. MAE and RMSE diverging is itself diagnostic: a long error tail exists — go look at it.
- **MAPE** — percentage error; intuitive but explodes near zero targets and punishes over-forecasting asymmetrically; use with guardrails.
- **R²** — variance explained vs the mean baseline; good for comparing across targets, useless as a business number.
- **Quantile (pinball) loss** — when the costs are asymmetric (the ED staffing case from M1); at Practitioner level, know it exists and when to ask for it.

Rule: report one primary metric chosen *at framing time*, in business units, plus whichever secondary metrics illuminate the failure mode.

### 2. Classification metrics: the confusion matrix is the source of truth

Everything derives from the four cells. Teach the derivations against Manafeth numbers (validation: 9,600 customers, 1,344 churners):

- **Accuracy** = right / all — degenerate at 86/14 imbalance (the dummy scores 86%).
- **Precision** = of those we flagged, how many churned — the cost side (wasted vouchers).
- **Recall** = of those who churned, how many we flagged — the benefit side (churners saved).
- **F1** — harmonic mean; a compromise, useful when no explicit budget exists; never a substitute for knowing the budget.
- **ROC-AUC** — ranking quality across all thresholds; robust to imbalance in interpretation but can look flattering when negatives dominate.
- **PR-AUC (average precision)** — precision/recall trade across thresholds; the honest curve when positives are rare, because its baseline *is* the positive rate (0.14), not 0.5.
- **recall@k / precision@k** — metrics for budgeted actions ("top-20% get vouchers") — usually the *actual* business metric hiding under a requested "accuracy".

**Thresholds are business decisions.** A probability model plus a threshold is a policy. Sweep the threshold, plot precision and recall against it, and let the voucher budget choose the operating point — in Lab 4 participants discover the 0.5 default is nowhere near optimal for Manafeth. Mention calibration in one breath: if probabilities feed expected-value arithmetic (voucher cost × churn probability), check the calibration curve; tree ensembles in M5 are often over-confident.

### 3. Cross-validation: the honest average

A single train/validation split is one noisy draw; k-fold CV averages k draws and — run on a `Pipeline` — refits preprocessing per fold, keeping M3's guarantees:

- **`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`** is the course default for classification; plain `KFold` for regression.
- **Report mean ± std.** Fold variance is information: 0.53 ± 0.01 and 0.53 ± 0.08 are different claims; a model choice inside one std of another is not a choice yet.
- **Grouped data needs `GroupKFold`** — when multiple rows share a customer, random folds put the same customer on both sides and scores inflate (unit-of-analysis, third appearance).
- **Temporal data needs `TimeSeriesSplit`** — folds respect time order; connect back to M1's split geometries.
- **CV estimates the *procedure*, not the artefact:** the final model refits on all training data; CV told you what to expect of that procedure on unseen data. The untouched test set (opened once, Day 4 H5) confirms it.

### 4. Learning curves and validation curves: diagnosis before treatment

- **Learning curve** (score vs training-set size): both curves converged and low → underfitting; more data won't help — better features or capacity will. Large persistent gap → overfitting; more data or regularisation will. This single plot answers the most expensive question in applied ML — "should we collect more data?" — before anyone spends a riyal on it.
- **Validation curve** (score vs one hyperparameter): the M2 depth sweep, generalised into a named tool via `validation_curve`; it is also the conceptual bridge into M7 — tuning is validation curves in many dimensions, automated.

### 5. Error analysis: where the next point of PR-AUC lives

Metrics say *how much* the model is wrong; error analysis says *where* and suggests *why*:

- **Slice the errors:** compute recall per city, per tenure band, per device. Manafeth's model, at this point in the week, is measurably worse on new (< 3 months) customers — thin RFM history; the finding writes the next feature (acquisition-channel data) rather than the next model.
- **Read the worst cases:** the 20 highest-confidence mistakes in each direction, as rows, with a human's eyes. False positives cluster in Ramadan-only shoppers ("seasonal, not churned") — a segment definition error found only by looking.
- **Slice metrics are fairness metrics.** Per-city recall differing by 15 points is an equity question about who receives retention benefits — surface this plainly; it returns with teeth in governance modules.

### 6. Common mistakes & production considerations

1. Reporting accuracy on imbalanced problems — the dummy already "achieves" the class ratio.
2. Selecting models on test-set scores — the test set becomes a validation set and its final number becomes fiction; the quarantine exists for this.
3. Tuning the threshold on the test set — thresholds are learned parameters; tune on validation folds.
4. Comparing models across different splits or seeds — all scoreboard comparisons share `random_state=42` and the same folds for a reason.
5. Ignoring fold variance — "0.54 beats 0.53" with ±0.03 stds is noise wearing a medal.
6. Metric monoculture — one number hides the tail; MAE+RMSE together, or PR-AUC + recall@k together, tell fuller truths.

Production considerations: the offline metric is a *proxy* — the voucher campaign's true metric is incremental retention, measurable only in production (A/B evaluation, SDA-DSC-213 territory); evaluation reports are governance artefacts — versioned with the model, reproducible from seed; per-slice metrics become monitoring dimensions after deployment (SDA-AIE-216).

## Code Examples

### The evaluation harness

```python
# src/manafeth/evaluation.py — one function, every model, same folds: comparisons stay legal
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate

CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
SCORING = {"pr_auc": "average_precision", "roc_auc": "roc_auc", "recall": "recall"}

def evaluate(pipeline, X, y, name: str) -> pd.Series:
    """Cross-validate a FULL pipeline (preprocessing refits per fold — M3's guarantee)."""
    res = cross_validate(pipeline, X, y, cv=CV, scoring=SCORING, n_jobs=-1)
    row = {f"{m}_mean": res[f"test_{m}"].mean() for m in SCORING}
    row |= {f"{m}_std": res[f"test_{m}"].std() for m in SCORING}
    return pd.Series(row, name=name).round(3)

# notebooks/day3/lab4_evaluation.ipynb
results = pd.DataFrame([
    evaluate(dummy_pipeline,    X_train, y_train, "dummy"),
    evaluate(logreg_pipeline,   X_train, y_train, "logreg+features"),
    evaluate(tree_pipeline,     X_train, y_train, "tree(depth=6)"),
])
print(results[["pr_auc_mean", "pr_auc_std"]])
#                   pr_auc_mean  pr_auc_std
# dummy                   0.141       0.004
# logreg+features         0.531       0.011      <- ±1 std: the honest claim
# tree(depth=6)           0.512       0.019
```

### Threshold tuning against the voucher budget

```python
# notebooks/day3/lab4_evaluation.ipynb — A threshold is a policy; choose it with the business constraint
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import cross_val_predict

proba = cross_val_predict(logreg_pipeline, X_train, y_train, cv=CV,
                          method="predict_proba")[:, 1]     # out-of-fold: every score is honest

prec, rec, thr = precision_recall_curve(y_train, proba)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(thr, prec[:-1], label="precision")
ax.plot(thr, rec[:-1], label="recall")
ax.axvline(0.5, ls=":", color="grey", label="default 0.5 (nobody chose this)")

# The ACTUAL constraint: contact 20% of the base
budget_thr = np.quantile(proba, 0.80)
ax.axvline(budget_thr, ls="--", color="red", label=f"top-20% budget -> thr={budget_thr:.2f}")
ax.set_xlabel("decision threshold"); ax.legend()

flagged = proba >= budget_thr
print(f"At budget threshold: precision {y_train[flagged].mean():.2f}, "
      f"recall {y_train[flagged].sum() / y_train.sum():.2f}")
# At budget threshold: precision 0.46, recall 0.66  -> the sentence for the CRM meeting
```

### Learning curve — should we buy more data?

```python
# notebooks/day3/lab4_evaluation.ipynb
from sklearn.model_selection import learning_curve

sizes, tr, val = learning_curve(logreg_pipeline, X_train, y_train, cv=CV,
                                scoring="average_precision",
                                train_sizes=np.linspace(0.1, 1.0, 6), n_jobs=-1)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(sizes, tr.mean(axis=1), marker="o", label="train")
ax.plot(sizes, val.mean(axis=1), marker="s", label="validation")
ax.fill_between(sizes, val.mean(1) - val.std(1), val.mean(1) + val.std(1), alpha=0.2)
ax.set_xlabel("training examples"); ax.set_ylabel("PR-AUC"); ax.legend()
ax.set_title("Converged and flat -> more rows won't help; better features will (M3 was the right investment)")
```

### Slice-based error analysis

```python
# notebooks/day3/lab4_evaluation.ipynb — where does the model fail, and on whom?
analysis = X_train.assign(y=y_train.values, proba=proba,
                          flagged=(proba >= budget_thr))

def slice_recall(df, col):
    g = df[df["y"] == 1].groupby(col)
    return (g["flagged"].mean().rename("recall")
            .to_frame().join(g.size().rename("churners")))

print(slice_recall(analysis, "city"))
#          recall  churners
# Dammam    0.68       241
# Jeddah    0.67       498
# Riyadh    0.64       605
print(slice_recall(analysis, pd.cut(analysis["tenure_months"], [0, 3, 12, 120],
                                    labels=["new", "growing", "established"])))
#              recall  churners
# new           0.49       402   <- the finding: thin history, weak features
# growing       0.71       513
# established   0.74       429

worst_fp = analysis[analysis["y"] == 0].nlargest(20, "proba")
# Read these 20 rows aloud in class: Ramadan-only shoppers scored as churners.
```

## Hands-on Lab 4 — The Evaluation Harness

| | |
|---|---|
| **Objective** | Deliver `evaluate()` and a cross-validated comparison of all models so far; tune the threshold to the voucher budget; produce a learning curve verdict and two error-analysis findings with proposed fixes |
| **Duration** | 50 minutes (Day 3 Hour 3) |
| **Setup** | Lab 3 pipeline committed; `notebooks/day3/lab4_evaluation.ipynb` skeleton |

**Tasks**
1. *(10 min)* Implement `evaluate()` with shared folds; run it on dummy, logistic, and tree pipelines; format the mean ± std table.
2. *(10 min)* Out-of-fold probabilities via `cross_val_predict`; plot the precision/recall vs threshold curves; mark the budget threshold; record precision/recall at budget on the scoreboard.
3. *(10 min)* Generate the learning curve; write the one-sentence verdict ("more data would / would not help because…").
4. *(15 min)* Slice recall by city, tenure band, and device; extract the 20 worst false positives and 20 worst false negatives; write two findings, each with a proposed feature or segment fix.
5. *(5 min)* Commit `feat(lab4): CV harness, budget threshold, error-analysis findings`.

**Expected outputs**
```
CV table: logreg 0.531 ± 0.011 | tree(6) 0.512 ± 0.019 | dummy 0.141 ± 0.004
Budget threshold 0.31 -> precision 0.46, recall 0.66 (vs 0.72/0.34 at default 0.5)
Learning curve: converged by ~25k rows -> verdict: invest in features, not rows
Findings: (1) new-customer recall 0.49 -> propose acquisition-channel feature
          (2) Ramadan-only shoppers dominate top FPs -> propose seasonal-shopper flag
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| CV runs > 5 min | Pipeline refit cost × folds, single-core | `n_jobs=-1`; confirm no notebook-global heavy work inside the pipeline |
| Fold scores wildly unequal | Forgot stratification, or grouped rows split across folds | Use the shared `CV` object; check for duplicate customers |
| Threshold curve looks like a staircase | Plotted `predict` labels not probabilities | Use `predict_proba` out-of-fold |
| recall@budget worse than Lab 3's single-split value | Single split was a lucky draw | That is the lesson — CV is the honest number; update the scoreboard convention |
| `cross_val_predict` scores differ from `cross_validate` | They answer different questions (pooled vs per-fold) | Explain, don't "fix"; use each for its purpose |

**Instructor notes.** The threshold exercise carries the business payload of the day: participants discover that the "default" 0.5 threshold left 32 points of recall on the table under the actual budget. Insist findings in task 4 come with *proposed fixes* — error analysis that ends at numbers is spectating. The new-customer finding is planted (thin RFM history) so every pair can succeed; the Ramadan false-positive cluster rewards the pairs who read rows instead of aggregates.

## Mini Exercises

**Quiz.** (1) Why is PR-AUC preferred over ROC-AUC at 14% positives? (2) What does 0.53 ± 0.08 permit you to claim against 0.51 ± 0.02? (3) Who should set the classification threshold, and with what input? (4) Learning curve converged-and-flat: what do you buy next — data, features, or capacity? (5) When is `GroupKFold` mandatory?
**Debugging exercise.** A colleague reports PR-AUC 0.61 for the same pipeline. Diff their notebook: they tuned the threshold *and* selected features against the test set. Quantify the damage by re-running honestly; state which number goes in the report.
**Code-review exercise.** Review an evaluation section: accuracy on the imbalanced task, model comparison across different seeds, "final AUC" computed on the test set in cell 12 of 40. Three findings, plus the corrected protocol in five lines.
**Discussion.** Manafeth's CFO asks: "Is 0.66 recall good?" — construct the answer that converts recall into vouchers, saved customers, and SAR, and note what extra number you need (customer lifetime value).

## Case Study — Credit-Default Metrics Under Model Governance at a Saudi Finance Company

**Scenario.** A consumer-finance company (SAMA-supervised) replaces a legacy scorecard with an ML default-risk model. Data science reports ROC-AUC 0.84 vs the scorecard's 0.79 and requests approval. The model validation unit rejects the submission — not the model, the *evaluation*.

**Business context.** The lending decision operates at a fixed risk appetite: approve as many customers as possible subject to portfolio bad-rate ≤ 3%. Validation requires: performance at the operating point (approval rate at 3% bad-rate), stability across time (quarterly OOT — out-of-time — samples, not random CV), slice performance by segment (salary bands, regions, new-to-credit customers), and calibration evidence (predicted PDs feed provisioning arithmetic under IFRS 9).

**Technical challenge.** Rebuild the evaluation: temporal validation replacing random CV (default patterns drift with the economy); the headline becomes "approval rate 61% → 68% at fixed 3% bad-rate" — the number the business actually buys; calibration curve + Brier score for the provisioning use; slice table exposing that the model underperforms the scorecard on new-to-credit applicants (thin files — the same finding pattern as Manafeth's new customers, in higher-stakes clothing).

**Constraints.** The new-to-credit slice cannot simply be excluded (financial-inclusion mandate); champion/challenger deployment requires the scorecard kept warm; every evaluation artefact must be reproducible by validators from seed and data snapshot.

**Solution approach.** Hybrid policy: ML champion for thick-file applicants, scorecard for thin files, with an explicit routing rule — a *model-selection* decision made by error analysis, not leaderboard position. Quarterly OOT evaluation is codified as the retraining gate. The validators' checklist maps one-to-one onto this module's toolkit: operating-point metric, temporal splits, slices, calibration, reproducibility.

**Discussion questions.** (1) Why does random CV overstate performance in a drifting economy, and what does `TimeSeriesSplit` change? (2) AUC rose but thin-file performance fell — was the old evaluation *wrong* or *incomplete*? (3) Defend the hybrid routing rule against "just use the better model everywhere". (4) Which parts of this validation protocol should Manafeth adopt despite having no regulator? 

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| CV harness adoption | Workflow integrity | all scoreboard entries carry mean ± std on shared folds | scoreboard audit |
| Budget-threshold operating point | Business metric | recall ≥ 0.64 at 20% contact rate (logreg+features) | harness output |
| Learning-curve verdict | Diagnostic skill | correct data-vs-features call with evidence | markdown review |
| Error-analysis findings | Diagnostic skill | ≥ 2 findings, each with a proposed fix | lab check |
| Test-set quarantine | Workflow integrity | still 0 reads | notebook audit |
| Harness runtime | Performance | 5-fold × 3 models ≤ 3 min on lab laptop | `%%time` |

**Example benchmark table:**

| Model (pipeline) | PR-AUC (CV) | recall@20% (OOF) | Verdict |
|---|---|---|---|
| dummy | 0.141 ± 0.004 | 0.20 | floor |
| logreg + M3 features | 0.531 ± 0.011 | 0.66 | champion so far |
| tree(depth=6) + M3 features | 0.512 ± 0.019 | 0.63 | within noise of logreg — not a choice yet |
| 21-day heuristic | — | 0.41 | retired with honours |

## Required Visuals and Training Assets

### Diagrams
1. **Metric-choice decision tree** — *Purpose:* the module's take-home card. *Elements:* branches from "regression or classification?" through "symmetric costs?", "rare positives?", "fixed action budget?" to recommended metrics, each leaf carrying one course example. *Style:* compact flowchart, printable A4, course palette.
2. **Confusion-matrix anatomy** — *Elements:* the 2×2 with Manafeth counts, arrows deriving precision/recall/accuracy from cells, voucher-cost and lost-customer-cost icons on the two error cells. *Style:* annotated matrix poster.
3. **k-fold CV on a pipeline** — *Elements:* five folds as bars; per fold: preprocessing refit icon + train/validate segments; scores flowing into mean ± std; a red "don't" inset showing preprocessing fit once outside the loop. *Style:* horizontal fold strips; explicitly reuses M3's pipeline drawing.
4. **Learning-curve verdict guide** — *Elements:* three mini learning curves (converged-flat, gap-persistent, still-rising) with their verdicts (features / regularise-or-data / more data). *Style:* triptych card, pairs with M2's residual field guide.

### Images
1. **CV results table screenshot** — *why:* expected format; *content:* mean ± std columns, models as rows.
2. **Threshold curves with budget line** — *why:* the day's key artefact; *content:* precision/recall curves, grey 0.5 line, red budget line.
3. **Slice-recall bar chart (matplotlib)** — *why:* error analysis made visual; *content:* tenure bands with the new-customer dip highlighted.
4. **Worst-20 false positives dataframe view** — *why:* teach reading rows; *content:* Ramadan-only shopper pattern visible in order-recency columns.

### Simulations
1. **The lucky split** — *Setup:* provided seed makes a single split flatter the tree model above logreg; CV reverses the ranking. *Expected:* participants articulate why the CV verdict wins. *Learning objective:* single splits are one noisy draw.
2. **Test-set shopping** — *Setup:* a notebook "improves" PR-AUC from 0.53 to 0.58 through five successive test-set consultations. *Expected:* participants replicate honestly and watch the gain evaporate; count the consultations. *Learning objective:* the quarantine is arithmetic, not etiquette.
3. **Threshold drift** — *Setup:* apply the tuned threshold to a shifted-month sample where score distribution moved. *Expected:* contact rate silently rises from 20% to 31%. *Learning objective:* thresholds are coupled to score distributions — monitor both (SDA-AIE-216 preview).

### Interactive Activities
- **Metric courtroom (15 min):** prosecution and defence argue "accuracy misled the business" on three mini-cases (fraud, demand forecast, churn); the class jury issues metric verdicts.
- **Error-analysis gallery walk (10 min):** pairs post their two findings; the room dot-votes the finding most likely to move next week's PR-AUC.

### Datasets
Golden-thread artefacts only; plus `shifted_month.parquet` (Manafeth scored one month later, for the threshold-drift simulation). No new primary datasets.

### Demo Requirements
- **Instructor demo:** run the harness live on three pipelines, then tune the threshold on the projector, ending with the CRM-meeting sentence ("at 20% budget we save two-thirds of leaving customers").
- **Student demo:** two pairs present one error-analysis finding each, with the fix they propose; class challenges the evidence.
- **Expected outputs:** every pair enters Module 5 with a CV harness, an operating point, and two feature ideas — Module 5's ensembles are judged by this same harness, no new rules.

---

# Module 5 — Tree Ensembles: Random Forests and Gradient Boosting

## Module Overview

**Purpose.** Single decision trees are readable but unstable; ensembles turn many weak trees into the strongest general-purpose learners available for tabular data. This module teaches the two ensemble families — bagging (random forests) and boosting (gradient boosting, delivered through scikit-learn and XGBoost) — with enough mechanism to tune them intelligently, plus the model-inspection tools (permutation importance, partial dependence) that keep powerful models explainable.

**Business relevance.** On enterprise tabular problems — credit, churn, demand, maintenance — gradient boosting remains the production benchmark to beat, frequently outperforming deep learning at a fraction of the cost and operational complexity. A Practitioner who can take a well-framed problem with honest features and reliably extract ensemble-level performance is immediately useful; the same person knowing when the *linear challenger is close enough to win on auditability* is more useful still.

**Industry use cases.**
- Manafeth's thread: XGBoost lifts churn PR-AUC from 0.53 to 0.60 on the same features and the same harness — the fair comparison Modules 3–4 made possible.
- A Jubail petrochemical plant predicts compressor failures from sensor aggregates with gradient boosting; permutation importance focuses maintenance engineers on three actionable signals.
- A Saudi insurer's motor-claims severity model uses random forests for their variance-reduction stability across quarterly retrains — rank stability matters more than the last point of accuracy.

**Expected competencies.** Participants can explain bagging vs boosting, train and regularise random forests and gradient-boosted trees, use early stopping, handle class imbalance with `scale_pos_weight`, compute and correctly interpret permutation importance, and defend an evidence-based champion/challenger choice.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain how bagging reduces variance and boosting reduces bias | LO3, LO6 |
| 5.2 | Train and regularise RandomForest and gradient-boosting models within pipelines | LO3, LO7 |
| 5.3 | Apply early stopping and imbalance handling in XGBoost | LO3, LO7 |
| 5.4 | Interpret ensembles with permutation importance and partial dependence | LO5 |
| 5.5 | Select a champion model with CV evidence and articulate the interpretability trade | LO2, LO5 |

## Technical Content

### 1. Why many weak trees beat one strong tree

The single deep tree from Module 2 had low bias and catastrophic variance — retrain on a different sample and the tree changes shape entirely. Ensembles attack this from two directions:

- **Bagging (random forests):** train many deep trees on bootstrap resamples, each split considering only a random feature subset (`max_features`), and average their votes. Averaging nearly-independent high-variance estimators slashes variance while keeping bias low. The de-correlation from feature subsampling is the trick — without it, every tree grabs `days_since_last_order` first and the average averages nothing.
- **Boosting (gradient boosting):** train *shallow* trees sequentially, each one fit to the errors (gradients of the loss) of the ensemble so far, added with a small `learning_rate`. Where bagging averages independent opinions, boosting compounds corrections — it reduces bias, which is why it usually wins on tabular data, and why it overfits more willingly and demands more careful tuning.

One sentence each, repeated until it sticks: *forests average away variance; boosting stacks away bias.*

### 2. Random forests in practice

- Defaults are strong: `n_estimators=300`, trees full-depth, `max_features="sqrt"`. More trees never hurt accuracy (only compute); the curve just flattens — show this, it demystifies the knob.
- Regularisation knobs when needed: `min_samples_leaf` (the big one), `max_depth`.
- **OOB score** (`oob_score=True`): each tree is validated on the rows its bootstrap missed — a free, honest validation signal; a nice cross-check on the harness, never a replacement for it.
- Failure modes: forests cannot extrapolate beyond the training range of a feature (all trees predict constants outside it — the Markabat old-car problem from M2 returns); and they are memory-hungrier at serving time than a boosted model of equal skill.

### 3. Gradient boosting and XGBoost

The knobs, organised by what they control:

| Knob | Controls | Course guidance |
|---|---|---|
| `n_estimators` + `learning_rate` | How long / how fast | Low rate (0.05) + early stopping to find `n_estimators` |
| `max_depth` | Interaction depth per tree | 3–6 for most tabular problems |
| `subsample`, `colsample_bytree` | Stochasticity (variance control) | 0.8 / 0.8 solid defaults |
| `reg_alpha`, `reg_lambda` | Leaf-weight penalties | The last knobs to touch |
| `scale_pos_weight` | Class imbalance | ≈ neg/pos ratio (≈ 6 for Manafeth) |

- **Early stopping is the load-bearing practice:** hold out an eval set, stop when validation loss stalls (`early_stopping_rounds=50`); it converts the most dangerous knob (`n_estimators`) into an observed quantity. Note the subtlety honestly: the eval set now influences training, so keep it separate from the folds that produce reported scores.
- **`HistGradientBoostingClassifier`** is scikit-learn's fast native equivalent (LightGBM-style histograms, native NaN handling) — the course shows it as the pure-sklearn option; XGBoost is taught as the listed industry tool.
- Trees don't need feature scaling (M3's table) — but keep the pipeline anyway: encoding, imputation, and the leakage guarantees still apply; only the scaler becomes optional.

### 4. Opening the box: importance and dependence

- **Impurity-based feature importance (the default `feature_importances_`) is biased** toward high-cardinality and continuous features — teach the flaw before the tool, or the tool teaches the flaw.
- **Permutation importance** (`sklearn.inspection.permutation_importance`): shuffle one column on *validation* data, measure the score drop — model-agnostic, honest, and interpretable as "what the model actually leans on". Correlated features share importance; note it.
- **Partial dependence plots** show the average predicted response as one feature varies — the tool that turns "the model likes recency" into a curve the CRM team can act on ("risk accelerates sharply after 18 quiet days" — which incidentally validates their old 21-day heuristic and buys goodwill).
- Importance ≠ causality. `promo_usage_rate` predicting retention does not mean vouchers cause it — selection effects abound. Say this twice; SDA-DSC-213 exists because of it.

### 5. Champion, challenger, and the interpretability trade

The Day 3 closing ritual: the harness table with dummy → heuristic → logreg → tree → forest → XGBoost on identical folds. XGBoost wins PR-AUC by ~7 points over logistic; logistic retrains in seconds, explains itself, and already beat the business heuristic soundly. The decision framework: performance delta × business value of the delta vs operational and governance cost of complexity. For Manafeth's voucher budget, 7 PR-AUC points ≈ hundreds of additional saved customers per month — the ensemble earns its complexity; the logistic model stays warm as challenger and sanity oracle. Both sentences go in the model card.

### 6. Common mistakes & production considerations

1. Tuning `n_estimators` by grid instead of early stopping — slow and worse.
2. Reporting scores from the early-stopping eval set — it participated in training; report from untouched folds.
3. Trusting impurity importances — the planted `customer_id_hash` (M2 simulation) tops that list; permutation importance buries it.
4. Chasing +0.003 PR-AUC with 4-hour searches while the M4 error-analysis findings (new-customer features) sit unimplemented — features beat knobs, still.
5. Treating ensemble probability outputs as calibrated — boosted scores are often mis-calibrated; check the calibration curve before expected-value arithmetic (M4 callback).
6. Deploying a forest where the serving budget was 5 ms and 50 MB — ensembles have operational weight; know it before the champion is crowned.

Production considerations: version the tuned configuration with the model artefact; retrain cadence matters more for boosted models (they fit the current distribution tightly — drift bites faster); XGBoost model files serialise compactly (`save_model`) and load in the SDA-AIE-113 serving pattern unchanged; keep the challenger deployed for shadow comparison (SDA-AIE-216 formalises this).

## Code Examples

### Random forest with OOB cross-check

```python
# notebooks/day3/lab5_ensembles.ipynb — Forest: strong defaults, honest OOB
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from manafeth.features import build_preprocessor
from manafeth.evaluation import evaluate

forest = Pipeline([
    ("prep", build_preprocessor()),
    ("clf", RandomForestClassifier(
        n_estimators=300, max_features="sqrt", min_samples_leaf=5,
        class_weight="balanced", oob_score=True, n_jobs=-1, random_state=42)),
])
print(evaluate(forest, X_train, y_train, "random_forest"))
# pr_auc_mean 0.571  pr_auc_std 0.012
forest.fit(X_train, y_train)
print("OOB accuracy cross-check:", round(forest["clf"].oob_score_, 3))
```

### XGBoost with early stopping and imbalance handling

```python
# notebooks/day3/lab5_ensembles.ipynb — Boosting: low learning rate, let early stopping choose length
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# Early-stopping eval set: carved from TRAIN, kept apart from reported-score folds
X_fit, X_es, y_fit, y_es = train_test_split(X_train, y_train, test_size=0.15,
                                            stratify=y_train, random_state=42)
prep = build_preprocessor().fit(X_fit)          # transform explicitly for the eval_set API

xgb = XGBClassifier(
    n_estimators=2000,                # ceiling — early stopping finds the real number
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8, colsample_bytree=0.8,
    scale_pos_weight=(y_fit == 0).sum() / (y_fit == 1).sum(),   # ~6.1 for Manafeth
    eval_metric="aucpr",
    early_stopping_rounds=50,
    random_state=42,
)
xgb.fit(prep.transform(X_fit), y_fit,
        eval_set=[(prep.transform(X_es), y_es)], verbose=100)
print("best_iteration:", xgb.best_iteration)     # ~380 — n_estimators, observed not guessed

# Reported score still comes from the shared harness (pipeline form, fixed n_estimators):
xgb_pipe = Pipeline([("prep", build_preprocessor()),
                     ("clf", XGBClassifier(n_estimators=xgb.best_iteration,
                                           learning_rate=0.05, max_depth=4,
                                           subsample=0.8, colsample_bytree=0.8,
                                           scale_pos_weight=6.1, eval_metric="aucpr",
                                           random_state=42))])
print(evaluate(xgb_pipe, X_train, y_train, "xgboost"))
# pr_auc_mean 0.598  pr_auc_std 0.010     <- the same harness, so the comparison is legal
```

### Permutation importance and partial dependence

```python
# notebooks/day3/lab5_ensembles.ipynb — What does the champion actually lean on?
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance, PartialDependenceDisplay

xgb_pipe.fit(X_fit, y_fit)
imp = permutation_importance(xgb_pipe, X_es, y_es, scoring="average_precision",
                             n_repeats=10, random_state=42, n_jobs=-1)
order = imp.importances_mean.argsort()[::-1][:8]
fig, ax = plt.subplots(figsize=(7, 4))
ax.boxplot(imp.importances[order].T, tick_labels=X_es.columns[order], vert=False)
ax.set_xlabel("PR-AUC drop when shuffled (validation)")
ax.set_title("Permutation importance: honest, model-agnostic, leakage-revealing")

# Partial dependence: the curve the CRM team can act on
PartialDependenceDisplay.from_estimator(
    xgb_pipe, X_es, ["days_since_last_order", "basket_trend"], kind="average")
# Reading: churn risk accelerates sharply after ~18 quiet days —
# the old 21-day heuristic was nearly right; the model refines it per-customer.
```

## Hands-on Lab 5 — Ensemble the Churn Model

| | |
|---|---|
| **Objective** | Beat the logistic champion with forest and XGBoost under the shared harness; produce permutation importance and one partial-dependence reading; update the champion/challenger table with an argued recommendation |
| **Duration** | 50 minutes (Day 3 Hour 5) |
| **Setup** | Lab 4 harness committed; `pip install xgboost` verified (pre-checked in environment setup); `notebooks/day3/lab5_ensembles.ipynb` skeleton |

**Tasks**
1. *(10 min)* Random forest pipeline per template; harness it; note OOB cross-check; scoreboard.
2. *(15 min)* XGBoost with early stopping: carve the eval set, find `best_iteration`, harness the fixed-length pipeline; scoreboard.
3. *(5 min)* Plot `n_estimators` vs validation PR-AUC for the forest (100/300/1000) — observe the flattening, not a peak.
4. *(10 min)* Permutation importance (top 8) on validation; compare with impurity importances; note one disagreement and explain it.
5. *(5 min)* One partial-dependence plot; write the one-sentence CRM reading.
6. *(5 min)* Update `CHAMPION.md`: harness table (all models, same folds), recommendation, and the challenger-retention sentence. Commit `feat(lab5): ensembles under shared harness; champion argued`.

**Expected outputs**
```
random_forest:  PR-AUC 0.571 ± 0.012   recall@20% 0.70
xgboost:        PR-AUC 0.598 ± 0.010   recall@20% 0.73   best_iteration ≈ 380
logreg:         PR-AUC 0.531 ± 0.011   (challenger, retained)
Permutation top-3: days_since_last_order, basket_trend, orders_90d
Impurity list disagrees: avg_basket_sar inflated (continuous-feature bias)
PDP reading: risk accelerates after ~18 quiet days -> refines the 21-day heuristic
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| XGBoost ignores `early_stopping_rounds` | Older/newer API variant | Course pins xgboost ≥ 2.0; parameter goes in the constructor |
| PR-AUC 0.97 returns | The unfiltered-RFM bug resurrected via a stale cell | Restart kernel, run top-to-bottom; the shuffled-label test is one cell away |
| Forest slower than XGBoost | Full-depth trees × 300 on one core | `n_jobs=-1`; discuss train-vs-serve cost asymmetry |
| Importances differ run-to-run | Permutation repeats too low / no seed | `n_repeats=10, random_state=42`; read the boxplot spread as the uncertainty |
| Early-stopped model scores worse in harness | Eval-set luck; harness folds are the arbiter | Trust the harness; this is why reported scores never come from the eval set |

**Instructor notes.** Keep the harness sacred: every number on the Day 3 closing table comes from `evaluate()` on shared folds, or it does not go on the table — enforcing this once, publicly, teaches more about evaluation discipline than Module 4's hour did. The impurity-vs-permutation disagreement is planted (continuous-feature bias on `avg_basket_sar`); ask pairs to explain it before you do. Fast finishers: `HistGradientBoostingClassifier` head-to-head with XGBoost — near-parity at less install friction is itself a finding.

## Mini Exercises

**Quiz.** (1) Forests average away ___; boosting stacks away ___. (2) Why does feature subsampling make bagging work? (3) What does early stopping convert `n_estimators` into? (4) Why must reported scores avoid the early-stopping eval set? (5) Your top impurity importance is a 40k-cardinality hash — what do you suspect and which tool confirms it?
**Debugging exercise.** Branch `sim-depth12`: XGBoost with `max_depth=12`, no subsampling — train PR-AUC 0.99, harness 0.55. Participants must name the failure from the M2 capacity picture and fix it two ways (depth down; subsample + regularisation).
**Code-review exercise.** Review a PR: forest without `class_weight` on the 14% problem, scores reported from the eval set, impurity importances in the exec summary, `n_estimators=50` "for speed" with no curve shown. Four findings.
**Discussion.** The insurer (use case 3) chose forests over boosting for rank stability across retrains. Construct the argument, then the counter-argument for Manafeth.

## Case Study — Predictive Maintenance at a Jubail Petrochemical Plant

**Scenario.** A rotating-equipment reliability team at a Jubail complex wants 72-hour advance warning of compressor trips. Data: 2 years of sensor telemetry (vibration, temperature, pressure — aggregated per hour), maintenance logs, and 41 historical trip events across 28 compressors.

**Business context.** An unplanned trip costs multiples of a planned intervention; but a false alarm that idles a healthy train costs real production too. The maintenance planner needs a *ranked daily watchlist*, not an alarm bell — precision@top-3 per day is the operating metric.

**Technical challenge.** Severe imbalance (41 positives), grouped structure (the same compressor contributes many rows — `GroupKFold` by machine, or trips leak across folds), temporal integrity (features from trailing windows only), and small-n honesty: with 41 events, CV variance is enormous and must be reported, not hidden. Gradient boosting on trailing-window aggregates (rolling means, deltas, exceedance counts) with `scale_pos_weight`, early stopping, and permutation importance to hand engineers three physical signals they can verify against domain knowledge — vibration-trend and temperature-delta rank top, which matches bearing-failure physics and builds the trust that determines adoption.

**Constraints.** Model must run on the historian server (no GPU — fine, XGBoost is CPU-happy); every alert reviewed by an engineer (human-in-the-loop mandated); n=41 means no test-set luxury — nested CV or leave-one-machine-out is the honest protocol; safety instrumented systems remain untouched — this is advisory analytics, stated explicitly in the model card.

**Solution approach.** Frame as classification on machine-day units ("trip within 72h"); `GroupKFold` by compressor; boosted model beats the vibration-threshold heuristic (precision@3 0.44 vs 0.19) with wide, honestly-reported intervals; the deployment is a morning watchlist email — the least-ML-looking, most-adopted artefact in the plant.

**Discussion questions.** (1) Why is `GroupKFold` by machine non-negotiable here — what exactly leaks otherwise? (2) With 41 events, what claims are and are not supportable? Draft the honesty paragraph of the model card. (3) The heuristic the model replaced was an engineer's threshold — how do you retire it without retiring the engineer's trust? (4) Which M5 tool did the most work in this story: the ensemble, early stopping, or permutation importance?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Champion PR-AUC (CV) | Model quality | ≥ 0.59 (XGBoost on M3 features) | shared harness |
| recall@20% at budget threshold | Business metric | ≥ 0.72 | harness + OOF threshold |
| Early stopping used | Practice adoption | `best_iteration` reported, not guessed | notebook check |
| Importance tooling | Interpretation | permutation importance + 1 PDP reading | lab check |
| Champion table completeness | Decision quality | all 6 models, same folds, ± std | CHAMPION.md review |
| Full-harness runtime | Performance | ≤ 6 min for both ensembles, 5 folds | `%%time` |

**Example benchmark table (the Day 3 closing table):**

| Model | PR-AUC (CV) | recall@20% | Retrain cost | Verdict |
|---|---|---|---|---|
| dummy | 0.141 ± 0.004 | 0.20 | — | floor |
| 21-day heuristic | — | 0.41 | — | retired |
| logreg + features | 0.531 ± 0.011 | 0.66 | seconds | challenger |
| tree(depth=6) | 0.512 ± 0.019 | 0.63 | seconds | dropped |
| random forest | 0.571 ± 0.012 | 0.70 | ~1 min | contender |
| **XGBoost (es@380)** | **0.598 ± 0.010** | **0.73** | ~2 min | **champion** |

## Required Visuals and Training Assets

### Diagrams
1. **Bagging vs boosting, side by side** — *Purpose:* the module's anchor. *Elements:* left panel — parallel trees on bootstrap samples with a feature-subset dice icon, votes averaged; right panel — sequential shallow trees each fed the previous ensemble's residuals, small-step additions; captions "averages away variance" / "stacks away bias". *Style:* mirrored panels, course palette. *Designer note:* trees drawn deep on the left, shallow on the right — the depth asymmetry is content.
2. **The knob map (XGBoost)** — *Elements:* knobs grouped by function (length/rate, capacity, stochasticity, penalties, imbalance) with course-default values and "touch order" numbering. *Style:* control-panel motif, printable.
3. **Early-stopping curve** — *Elements:* train and eval loss vs boosting rounds; stall point marked; the 50-round patience window shaded; `best_iteration` arrow. *Style:* single chart matching the verbose=100 output participants see.
4. **Impurity vs permutation importance** — *Elements:* the same model's two rankings side by side with the inflated continuous feature and the buried hash highlighted. *Style:* slope chart between two ranked lists.

### Images
1. **XGBoost training log screenshot** — *why:* expected output; *content:* aucpr per 100 rounds, early-stop message at ~430, best_iteration 380.
2. **Permutation-importance boxplot** — *why:* reference for Lab 5 task 4; *content:* top-8 features with spread.
3. **PDP screenshot** — *why:* the CRM-readable curve; *content:* days_since_last_order with the 18-day acceleration visible.
4. **Day 3 closing champion table** — *why:* the module's deliverable format; *content:* the six-model table above, rendered.

### Simulations
1. **The resurrected leak** — *Setup:* a stale-kernel cell re-introduces unfiltered RFM into the ensemble run. *Expected:* 0.97 again; the shuffled-label test kills it in one cell. *Learning objective:* leak checks are re-run per model, not per week.
2. **Overfit boosting** — *Setup:* branch `sim-depth12`. *Expected:* train/harness gap; fixed two ways. *Learning objective:* the capacity dial applies to ensembles; boosting just hides the dial better.
3. **Extrapolation cliff** — *Setup:* score synthetic customers with `tenure_months=240` (beyond training range) under forest vs linear model. *Expected:* forest predicts a constant; linear extrapolates (dangerously but visibly). *Learning objective:* trees cannot extrapolate — know your feature ranges (ties to Markabat's refuse-to-predict boundary).

### Interactive Activities
- **Ensemble relay (10 min):** the room *is* a boosting run — each row of participants corrects the residual errors of the previous row's guesses on a projected scatter; the instructor plots the compounding fit.
- **Champion tribunal (15 min):** three groups argue for logistic / forest / XGBoost as Manafeth's production champion using only the closing table plus operational facts; the class votes; the winning argument goes into CHAMPION.md verbatim.

### Datasets
Golden-thread artefacts unchanged — deliberately: the module's claim is that the *same* features and harness make model upgrades a fair fight. Plus `jubail_sensors_sample.parquet` (5,000 rows, synthetic) for the case-study walkthrough.

### Demo Requirements
- **Instructor demo:** live XGBoost run with `verbose=100` streaming — narrate the eval curve stalling and the early stop firing; then permutation importance exposing the planted hash feature in 90 seconds.
- **Student demo:** champion-tribunal spokespeople (3 × 2 minutes).
- **Expected outputs:** every pair's CHAMPION.md names a champion with harness evidence and retains the challenger — Module 7 tunes exactly this champion; the capstone rubric asks for exactly this table.

---

# Module 6 — Unsupervised Learning: Clustering and Dimensionality Reduction

## Module Overview

**Purpose.** Not every business question comes with labels. This module teaches the two workhorse unsupervised techniques — clustering (k-means as the core method, DBSCAN and hierarchical clustering as contrast) and dimensionality reduction (PCA as the core, t-SNE/UMAP as visualisation-only companions) — together with the harder skill they demand: evaluating results when no ground truth exists. The framing discipline from Module 1 returns with force, because unsupervised work is where vague objectives go to produce impressive-looking nothing.

**Business relevance.** Segmentation drives marketing budgets, store layouts, tariff design, and service tiers across the Saudi market; anomaly detection guards payments and industrial equipment; PCA underlies compression, visualisation, and noise reduction across analytics stacks. Unsupervised results are also uniquely easy to oversell — colourful cluster plots command belief they haven't earned — so the module trains sceptical evaluation as hard as it trains the algorithms.

**Industry use cases.**
- Manafeth's thread: behavioural segmentation of the customer base — the segments become a *feature* for the churn model and a *language* for the CRM team ("Ramadan-seasonal bulk shoppers" enters the company vocabulary).
- A Jeddah municipality clusters 311-style service requests by pattern (location × category × time) to redesign crew scheduling — no labels existed until clustering proposed them.
- A payments processor uses distance-to-normal-behaviour (a clustering by-product) as one input to fraud review queues.

**Expected competencies.** Participants can prepare features for distance-based methods, run k-means with a defensible choice of k (elbow + silhouette + business readability), profile and *name* clusters, apply DBSCAN where density beats centroids, run PCA with a correct read of explained variance, and state clearly what t-SNE/UMAP plots do and do not show.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Frame a business question as clustering or dimensionality reduction, with success criteria | LO1 |
| 6.2 | Apply k-means correctly: scaling, initialisation, choosing k with silhouette and business sense | LO3, LO4 |
| 6.3 | Contrast k-means, DBSCAN, and hierarchical clustering; pick per data shape | LO3 |
| 6.4 | Apply PCA for compression and visualisation; interpret explained variance and loadings | LO4 |
| 6.5 | Evaluate unsupervised results without labels; profile and communicate segments | LO5, LO2 |

## Technical Content

### 1. Framing without labels

The framing canvas survives with two fields rewritten: the *target* becomes the intended **use** of the structure (segments feeding CRM playbooks; components feeding a model; anomalies feeding a review queue), and the *metric* becomes a **usefulness test** (can marketing name and act on each segment? does the compressed representation preserve model performance?). Without these two answers, clustering produces what one practitioner memorably called "a pie chart with delusions". State the honest defaults: clustering for *discovery and operations*, not truth; PCA for *compression and viewing*, not meaning.

### 2. K-means: mechanism and craft

K-means alternates assign-to-nearest-centroid / recompute-centroids until stable, minimising within-cluster variance (inertia). The craft around the loop matters more than the loop:

- **Scale first, always** — k-means is pure distance; the M2 k-NN lesson applies verbatim. Log-transform heavy-tailed monetary features first or the bulk-order tail owns a centroid by itself.
- **`n_init` and seeding:** k-means converges to local optima; `n_init="auto"` (multiple restarts, keep best inertia) plus `random_state=42` for reproducibility.
- **Choosing k:** the elbow plot (inertia vs k) is suggestive, rarely decisive; **silhouette score** (cohesion vs separation, −1…1) gives a quantitative vote; the deciding vote is **business readability** — five nameable segments beat seven where two are "miscellaneous". Teach all three; forbid using the elbow alone.
- **Profile before you present:** per-cluster means of the *original* (unscaled) features, cluster sizes, and a two-word name per cluster. A segment nobody can name is a segment nobody will use.
- Assumptions worth stating: k-means favours convex, similar-sized blobs; it *will* partition even structureless noise into k confident-looking pieces — the null test in Lab 6 makes this visceral.

### 3. When centroids fail: DBSCAN and hierarchical

- **DBSCAN** grows clusters from density (`eps`, `min_samples`); finds arbitrary shapes and — its production superpower — outputs *noise points* rather than forcing every row into a cluster. Natural fit for anomaly-flavoured questions (the payments use case); sensitive to `eps` and struggles when densities vary.
- **Agglomerative (hierarchical)** merges nearest clusters bottom-up; the dendrogram *is* the deliverable when stakeholders want taxonomy ("segments and sub-segments") — cut height chooses granularity after the fact.
- Selection heuristic for the course: blobs of similar scale → k-means; unknown shapes / want outliers → DBSCAN; want a hierarchy to discuss → agglomerative. All three inherit the scaling requirement.

### 4. PCA: variance as a budget

PCA rotates the feature space onto orthogonal directions of maximal variance; keeping the top components compresses with least (linear) information loss:

- **Explained-variance ratio is the budget sheet:** "PC1+PC2 carry 58% of variance" quantifies what a 2-D view shows and hides. The cumulative curve chooses dimensionality for compression (e.g., 95% at 11 of 24 components).
- **Scale first** — PCA maximises variance, and unscaled variance is just units (tenure_months would own PC1 for no reason beyond its range).
- **Loadings give the components meaning:** PC1 loading positively on frequency/monetary features is an "engagement intensity" axis; PC2 contrasting Ramadan-window activity against steady ordering is a "seasonality" axis. Name components the way you name clusters — carefully and provisionally.
- **Two distinct uses, one method:** *visualisation* (2 components, human eyes — how Lab 6 draws its segment map) and *feature transformation* (components feeding a model — with `PCA` as a Pipeline step so the rotation is learned on training folds only; the M3 discipline never sleeps).
- **t-SNE/UMAP in one honest paragraph:** superb at revealing local structure for *viewing*; distances and densities between far-apart groups are not faithful; never cluster on t-SNE output, never feed it to models — plot, enjoy, verify elsewhere.

### 5. Evaluating without ground truth

The evaluation stack for unsupervised work, weakest to strongest:

1. **Internal indices** (silhouette, inertia curves) — necessary hygiene, insufficient alone.
2. **Stability** — re-run under resampling/seeds; segments that dissolve under bootstrap were noise wearing colours (`adjusted_rand_score` between runs quantifies it).
3. **External usefulness** — the strongest test and the course requirement: do the segments predict something they weren't built from? Manafeth's segments are validated by their churn-rate spread (4% to 31% across segments) and by the +0.01 PR-AUC they add as a churn-model feature. Structure that helps prediction is structure that exists.

### 6. Common mistakes & production considerations

1. Clustering unscaled or un-transformed monetary features — one centroid per whale, noise elsewhere.
2. Choosing k by elbow alone — the elbow is often a shrug; silhouette + readability must concur.
3. Presenting t-SNE proximity as similarity evidence — the most confidently misread plot in analytics.
4. Forgetting that k-means *always* returns k clusters — run the null test before believing structure.
5. PCA on mixed raw scales, or interpreting components as causal factors rather than variance directions.
6. Segment drift unmonitored — customer behaviour shifts (Ramadan, promotions); segments must be re-fit and re-validated on a cadence, with stability tracked between refits.

Production considerations: fitted k-means/PCA objects are transformers — they serialise inside the same Pipeline artefact and assign segments at serving time consistently; segment definitions are business contracts (CRM playbooks reference them by name), so re-fits that reshuffle segments need a migration story; anomaly-queue thresholds from distance-to-centroid need the same drift monitoring as classification thresholds (M4 simulation echo).

## Code Examples

### K-means with the full choosing-k protocol

```python
# notebooks/day4/lab6_unsupervised.ipynb — Segmentation: scale, restart, choose k three ways
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, FunctionTransformer

SEG_COLS = ["orders_per_month", "avg_basket_sar", "days_since_last_order",
            "tenure_months", "distinct_categories", "promo_usage_rate",
            "ramadan_order_share", "weekend_order_share"]

seg_prep = Pipeline([
    ("log_money", FunctionTransformer(                     # tame the bulk-order tail FIRST
        lambda X: np.column_stack([np.log1p(X[:, 1]), np.delete(X, 1, axis=1)]))),
    ("scale", StandardScaler()),
])
Z = seg_prep.fit_transform(X_train[SEG_COLS].to_numpy())

inertias, silhouettes = {}, {}
for k in range(2, 11):
    km = KMeans(n_clusters=k, n_init="auto", random_state=42).fit(Z)
    inertias[k] = km.inertia_
    silhouettes[k] = silhouette_score(Z, km.labels_, sample_size=10_000, random_state=42)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(list(inertias), list(inertias.values()), marker="o"); axes[0].set_title("Elbow (suggestive)")
axes[1].plot(list(silhouettes), list(silhouettes.values()), marker="s"); axes[1].set_title("Silhouette (a vote)")
# Elbow mumbles 4-6; silhouette peaks at 5 (0.31). Business readability casts the deciding vote in profiling.
```

### Profiling and naming — the deliverable

```python
# notebooks/day4/lab6_unsupervised.ipynb — A segment nobody can name is a segment nobody will use
km = KMeans(n_clusters=5, n_init="auto", random_state=42).fit(Z)
seg = X_train[SEG_COLS].assign(segment=km.labels_, churned=y_train.values)

profile = seg.groupby("segment").agg(
    size=("segment", "size"),
    orders_pm=("orders_per_month", "mean"),
    basket=("avg_basket_sar", "mean"),
    recency=("days_since_last_order", "mean"),
    ramadan_share=("ramadan_order_share", "mean"),
    churn_rate=("churned", "mean"),
).round(2)
print(profile.sort_values("churn_rate"))
#          size  orders_pm  basket  recency  ramadan_share  churn_rate
# 2       9,870       7.9    96.4      3.1          0.18         0.04   <- "Daily essentials loyalists"
# 0      11,214       3.2   142.7      8.9          0.21         0.09   <- "Weekly family shoppers"
# 4       6,041       2.1   388.2     11.5          0.24         0.11   <- "Bulk-order households"
# 1       7,432       1.4    88.3     19.7          0.63         0.24   <- "Ramadan-seasonal shoppers"
# 3       3,843       0.9    61.0     34.2          0.29         0.31   <- "Drifting newcomers"
# The churn-rate spread (4% -> 31%) is the external-usefulness evidence: this structure is real.
```

### PCA: budget sheet, map, and loadings

```python
# notebooks/day4/lab6_unsupervised.ipynb — Compress, view, interpret — in that order
from sklearn.decomposition import PCA

pca = PCA(random_state=42).fit(Z)
cum = np.cumsum(pca.explained_variance_ratio_)
print("PC1+PC2 carry:", round(cum[1], 2))        # 0.58 — what the 2-D map shows (and hides)
print("components for 95%:", int(np.searchsorted(cum, 0.95) + 1))   # 6 of 8

coords = pca.transform(Z)[:, :2]
fig, ax = plt.subplots(figsize=(7, 5))
sc = ax.scatter(coords[:, 0], coords[:, 1], c=km.labels_, s=4, alpha=0.4, cmap="tab10")
ax.set_xlabel("PC1 — engagement intensity (58% with PC2)")
ax.set_ylabel("PC2 — seasonality axis")
ax.set_title("Segment map: k-means labels on PCA plane (view, not proof)")

loadings = pd.DataFrame(pca.components_[:2].T, index=SEG_COLS, columns=["PC1", "PC2"])
print(loadings.round(2).sort_values("PC1"))
# PC1 loads + on orders_pm, distinct_categories, - on recency  -> engagement axis
# PC2 loads + on ramadan_order_share                            -> seasonality axis
```

### The null test — would we have "found" structure in noise?

```python
# notebooks/day4/lab6_unsupervised.ipynb — K-means always returns k clusters; make sure yours mean something
rng = np.random.default_rng(42)
noise = rng.standard_normal(Z.shape)             # pure structureless noise, same shape

km_noise = KMeans(n_clusters=5, n_init="auto", random_state=42).fit(noise)
print("silhouette (real data):", round(silhouette_score(Z, km.labels_, sample_size=10_000, random_state=42), 3))
print("silhouette (noise):    ", round(silhouette_score(noise, km_noise.labels_, sample_size=10_000, random_state=42), 3))
# real 0.31 vs noise 0.09 -> our structure clears the null. Report both numbers; the gap IS the claim.
```

## Hands-on Lab 6 — Segment the Customers

| | |
|---|---|
| **Objective** | Deliver a named, profiled, null-tested 5-segment customer model with a PCA segment map; validate segments externally by churn-rate spread; add `segment` as a churn-model feature and measure the effect |
| **Duration** | 50 minutes (Day 4 Hour 3; Hour 2's demo seeds the PCA portion) |
| **Setup** | Lab 5 artefacts; `notebooks/day4/lab6_unsupervised.ipynb` skeleton |

**Tasks**
1. *(10 min)* Build `seg_prep` (log-money + scale); run the k=2..10 sweep; produce elbow + silhouette panels; record your k vote before profiling.
2. *(10 min)* Fit final k-means; produce the profile table; name every segment in ≤ 3 words; flag any unnameable segment (that is a finding, not a failure — revisit k).
3. *(10 min)* PCA: cumulative-variance printout, 2-D segment map, top loadings; write one-line readings of PC1 and PC2.
4. *(5 min)* Run the null test; report the real-vs-noise silhouette gap.
5. *(10 min)* External usefulness: churn-rate-by-segment table; then add `segment` as a categorical feature to the champion pipeline and re-run the M4 harness — record the delta.
6. *(5 min)* Commit `feat(lab6): named segments, null-tested, churn-validated`.

**Expected outputs**
```
k sweep: silhouette peak 0.31 @ k=5 (elbow ambiguous 4–6)
Profile: 5 nameable segments, sizes 3.8k–11.2k
Null test: silhouette 0.31 (real) vs 0.09 (noise) ✔
External: churn 4% -> 31% across segments; +segment feature: PR-AUC 0.598 -> 0.607
PCA: PC1+PC2 = 58%; PC1 engagement, PC2 seasonality
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| One cluster of 60 customers, one of 30k | Monetary tail unscaled/unlogged | Confirm `log_money` step ran before scaling |
| Silhouette computation takes minutes | Full-n pairwise distances | `sample_size=10_000, random_state=42` |
| Segments reshuffle every run | No seed / single init | `random_state=42, n_init="auto"` |
| Segment feature adds nothing to churn model | Segments built FROM the same features | Expected and worth saying aloud — the +0.009 comes from the interaction structure; discuss |
| PCA map shows smeared continuum, no islands | Reality: behaviour is continuous | Correct reading — clusters are a useful quantisation, not natural kinds; this sentence goes in the profile doc |

**Instructor notes.** The null test is the module's conscience — run it even if time is short; the 0.31-vs-0.09 gap gives participants a defensible sentence for stakeholders. Expect (and welcome) the "smeared continuum" observation on the PCA map: the honest statement that Manafeth's segments are useful quantisations of continuous behaviour, not discovered species, is exactly the epistemic posture this module exists to teach. The naming exercise gets 10 protected minutes: names are how segments survive contact with the business.

## Mini Exercises

**Quiz.** (1) Why must features be scaled before k-means and PCA? (2) Three inputs to choosing k — and which one decides? (3) What does DBSCAN give you that k-means structurally cannot? (4) "PC1+PC2 = 58%" — what exactly does the segment map hide? (5) Name the three levels of unsupervised evaluation, weakest to strongest.
**Debugging exercise.** A colleague's segmentation puts 92% of customers in one cluster. Diagnose from their notebook: raw SAR features, no log, k chosen by elbow on inertia of unscaled data. Fix and quantify the change in silhouette and profile readability.
**Code-review exercise.** Review a segmentation deck: clusters computed on t-SNE coordinates, segment names invented before profiling, no stability or null check, k=12 with five segments labelled "misc". Four findings, ranked by damage.
**Discussion.** The CRM team wants to keep last year's segment names after a re-fit reshuffles boundaries. What do you owe them — stable names, stable definitions, or a migration map — and what does each cost?

## Case Study — Clustering Municipal Service Requests in Jeddah

**Scenario.** A Jeddah municipality receives ~30,000 monthly service requests (road damage, waste, lighting, flooding, encroachment) through the unified portal. Crews are dispatched from fixed depots on fixed schedules designed years ago. The operations director asks: "What patterns are we not seeing?"

**Business context.** No labels exist — nobody has ever categorised requests beyond the citizen-chosen category, which is noisy (flooding logged as "road damage", etc.). The goal is operational: redesign crew schedules and depot allocation for the actual demand structure.

**Technical challenge.** Feature construction is the real work: requests become vectors of location (district), category, hour-of-day, day-of-week, and seasonal markers. K-means on scaled features proposes 7 patterns; the profiling step reveals three that reshape operations — a post-rain flooding+road cluster concentrated in specific low-lying districts (predictable from weather, crew pre-positioning possible), a Friday-evening waste surge around corniche districts (schedule mismatch: crews stand down exactly when demand peaks), and a Ramadan-night lighting/noise cluster (seasonal shift-plan case). DBSCAN on the location dimensions separately flags outlier request bursts — an early-warning by-product the emergency room adopts.

**Constraints.** District-level aggregation only (PDPL: no household-level profiling); results must survive a re-run on the following quarter (stability gate) before schedules change; the deliverable is an operations memo in plain Arabic, not a notebook — cluster names carry the entire communication burden.

**Solution approach.** Full course protocol: scale → sweep k with silhouette → profile → *name* → null test → external validation (do clusters predict resolution-time overruns they weren't built from? yes, ×2.3 spread) → stability check across quarters (`adjusted_rand_score` 0.81). Two schedule changes ship; complaint resolution times drop measurably; the "pattern" language enters the operations vocabulary — the model's real legacy.

**Discussion questions.** (1) The citizen-chosen category is noisy — does clustering fix labels, replace them, or neither? (2) Which of the three levels of evaluation did the resolution-time check represent, and why is it the strongest? (3) Design the stability gate: what ARI threshold, over what period, blocks a schedule change? (4) Where is the PDPL line between useful spatial clustering and profiling — and who decides?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Silhouette at chosen k | Structure quality | ≥ 0.25, reported *with* the noise-null value | lab output |
| Null-test gap | Honesty | real ≥ 2.5 × noise silhouette | lab output |
| Segment nameability | Usefulness | 5/5 segments named ≤ 3 words | profile review |
| External validation | Usefulness | churn-rate spread ≥ 4× between extreme segments | profile table |
| Segment feature effect | Integration | churn PR-AUC delta reported (any sign) | shared harness |
| Reproducibility | Workflow integrity | identical segments across pairs (seeded) | scoreboard |

**Example benchmark table:**

| Artefact | Value | Evidence type |
|---|---|---|
| Silhouette @ k=5 | 0.31 (noise null: 0.09) | internal + null |
| Churn spread across segments | 4% → 31% | external usefulness |
| Segment feature in champion | PR-AUC 0.598 → 0.607 | external usefulness |
| Re-run stability (seed 43 vs 42) | ARI 0.86 | stability |
| PC1+PC2 explained variance | 58% | budget sheet |

## Required Visuals and Training Assets

### Diagrams
1. **K-means iteration strip** — *Purpose:* demystify the algorithm. *Elements:* four frames (random centroids → assignment → centroid move → convergence) on a 2-D slice of Manafeth data; inertia value ticking down per frame. *Style:* film-strip sequence, course palette.
2. **Method-choice map** — *Elements:* three data shapes (round blobs, crescents/varying shapes with noise, nested taxonomy) mapped to k-means / DBSCAN / hierarchical, with one Saudi use case per branch. *Style:* decision flowchart with data-shape thumbnails.
3. **PCA rotation** — *Elements:* 2-D correlated cloud with original axes, then principal axes overlaid, then projection onto PC1 with the variance budget annotated; loadings table inset. *Style:* three-step build, designed for progressive slide reveal.
4. **The evaluation ladder** — *Elements:* three rungs (internal indices → stability → external usefulness) with Manafeth's evidence at each rung; a crossed-out "it looks meaningful" at the bottom. *Style:* ladder motif, printable; pairs with M4's metric-choice card.

### Images
1. **Elbow + silhouette twin panels** — *why:* expected shapes; *content:* ambiguous elbow, silhouette peak at 5.
2. **Profile table with names** — *why:* the deliverable format; *content:* the five named segments with churn-rate column highlighted.
3. **PCA segment map** — *why:* reference plot; *content:* five colours on the PC1/PC2 plane with axis readings in the labels.
4. **Null-test output cell** — *why:* the honesty artefact; *content:* 0.31 vs 0.09 side by side.

### Simulations
1. **Clustering pure noise** — *Setup:* the null-test cell, run first *without* revealing the data is noise; ask the room to name the clusters. *Expected:* confident wrong names, then the reveal. *Learning objective:* k-means always delivers k clusters; scepticism is a protocol, not a mood.
2. **The whale cluster** — *Setup:* skip the log transform. *Expected:* one micro-cluster of bulk buyers, one blob of everyone; silhouette collapses. *Learning objective:* distance methods inherit every scaling sin.
3. **t-SNE overreach** — *Setup:* provided t-SNE plot with two islands whose *between-island* distance reverses under a different perplexity. *Expected:* participants catch the unstable global geometry. *Learning objective:* t-SNE is a viewing instrument, not a measuring one.

### Interactive Activities
- **Human k-means (10 min, energiser):** participants as data points on a floor grid, three volunteers as centroids; two assign/update rounds to convergence — the algorithm learned kinaesthetically.
- **Segment-naming workshop (10 min):** pairs swap profile tables and name each other's segments blind; mismatched names expose under-separated clusters better than any index.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Golden-thread customer frame + `ramadan_order_share`, `weekend_order_share` (from M3 features) | Course repo | parquet | 38,400 × 8 seg features | Segmentation |
| `jeddah_requests_sample.csv` | Synthetic, district-aggregated | CSV | 12,000 rows | Case-study walkthrough |
| Noise-null generator cell | Course repo | notebook cell | — | Null test |

### Demo Requirements
- **Instructor demo:** run the noise-null *first* (unrevealed) and harvest confident cluster names from the room before the reveal — the module's most memorable three minutes; then the real segmentation start-to-profile in ten.
- **Student demo:** two pairs present one named segment each with its churn evidence; the class challenges one name.
- **Expected outputs:** every pair has a named, null-tested segmentation and has measured its effect on the champion model — the capstone's optional unsupervised component follows exactly this protocol.

---

# Module 7 — Hyperparameter Tuning and Model Selection

## Module Overview

**Purpose.** Every model so far carried knobs set by rule of thumb. This module makes the knob-turning systematic: search spaces, `GridSearchCV` and `RandomizedSearchCV` over full pipelines, tuning under a compute budget, the selection protocol that keeps comparisons honest (including where nested CV fits), and the final act of the workflow — refit on all training data, open the untouched test set once, and write the model card. It is the capstone's dress rehearsal: after this module, participants have executed the complete workflow end to end.

**Business relevance.** Tuning is where teams burn compute and integrity in equal measure: grid searches that cost a GPU-week to gain nothing, and — worse — scores inflated by tuning on the data that reports them. A Practitioner who tunes on a budget and reports honestly ships faster and survives model-validation review; the discipline transfers directly to the expensive world of LLM-era hyperparameters where a single sweep can cost real money.

**Industry use cases.**
- Manafeth's thread: a 30-draw randomised search lifts the XGBoost champion from PR-AUC 0.598 to 0.612 — a real gain, honestly measured, at 12 minutes of laptop compute.
- A Makkah hospitality group tunes seasonal demand models under a strict overnight compute window — randomised search with log-uniform ranges finds 95% of the achievable gain at 8% of the grid's cost.
- A bank's model-validation unit rejects any score produced by the same folds that selected the hyperparameters — nested evaluation or a held-out test set is the admissibility bar.

**Expected competencies.** Participants can define sensible search spaces and distributions, run randomised and grid search over pipelines (tuning preprocessing and model jointly), read search results beyond the single best row, explain selection bias and when nested CV is warranted, execute the final refit-and-test protocol, and write a model card that a reviewer can audit.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Design search spaces with appropriate scales and priorities per model family | LO7 |
| 7.2 | Run GridSearchCV and RandomizedSearchCV over full pipelines within a budget | LO7, LO3 |
| 7.3 | Avoid tuning leakage: separate selection data from reporting data | LO6, LO7 |
| 7.4 | Execute the final protocol: refit, single test-set evaluation, model card | LO2, LO5 |
| 7.5 | Decide when tuning is the right investment versus features or data | LO7, LO2 |

## Technical Content

### 1. What tuning actually is

Hyperparameters are the settings the fit cannot learn: they shape the hypothesis space (depth, regularisation) or the optimisation (learning rate). Tuning is an outer optimisation loop around cross-validated fits — the M2 validation curve generalised to many dimensions and automated. Two truths frame everything: the response surface is *shallow near the optimum* (many good configurations exist — perfection is not the goal), and the gains are *bounded by the features* (tuning polishes; it does not transmute — the M4 learning-curve verdict decides whether to be here at all).

### 2. Grid, random, and the budget argument

- **`GridSearchCV`** exhausts a small discrete space; right when knobs are few and cheap (alpha for ridge: one knob, log-spaced — grid is perfect).
- **`RandomizedSearchCV`** samples configurations from distributions; the course default for ensembles. The classic argument: with many knobs, only a few matter (per problem, unknown in advance); random search probes each dimension at `n_iter` distinct values while a grid wastes its budget on redundant combinations of the unimportant ones.
- **Distributions carry judgement:** learning rate and regularisation are log-uniform (`loguniform(0.01, 0.3)`) — the difference between 0.01 and 0.03 matters like 0.1 vs 0.3, not like 0.27 vs 0.29; depth and leaf counts are small integer ranges; subsampling uniform on [0.6, 1.0].
- **Budgeting:** total fits = `n_iter × folds`. 30 draws × 5 folds × ~25 s/fit ≈ 1 hour of core-time — `n_jobs=-1` makes it 12 minutes on lab laptops. Set the budget first, then shape the space to spend it well. Successive-halving (`HalvingRandomSearchCV`) is named as the next tool up when budgets bite harder.
- Early stopping (M5) composes awkwardly with plain `cross_val_score` inside search; the course pattern tunes `n_estimators` as a bounded draw instead, and notes the production alternative (search wrappers with per-fold eval sets).

### 3. Tuning leakage and the selection protocol

The subtle sin: scores used to *select* a configuration are optimistically biased *as estimates* of that configuration — the winner among 30 draws partly won by luck on those folds. The protocol that keeps everyone honest:

1. **Tune on the training data with CV** (`RandomizedSearchCV` does this internally — every fold refits the whole pipeline, preprocessing included; M3's guarantee is what makes this legal).
2. **Select** `best_params_` — and *look at the neighbourhood*, not just the winner: if the top ten configurations score within a hair, the surface is flat and the choice is robust; if the winner stands alone, suspect luck.
3. **Report from data the search never touched.** For the course: the untouched test set, opened once. When no test set can be spared, **nested CV** (an outer loop around the whole search) estimates the *procedure's* performance — explain it conceptually, demonstrate the inner/outer picture, and state the Practitioner guidance: with 38k rows, a proper test set is simpler and sufficient; nested CV earns its cost on small data (the Jubail case's n=41 world).
4. **Refit on all training data** with the chosen configuration (`refit=True` does exactly this) — the artefact that ships trains on everything available.

### 4. The final act: test set and model card

Day 4 Hour 5 closes the loop opened in Lab 1: unquarantine the test set, evaluate the refit champion **once**, and compare against the CV estimate — agreement within a std is the expected, quietly triumphant result; a large gap is a red flag pointing at leakage or distribution shift, and it must be investigated, not renarrated. Then the **model card** — one page: intended use and decision (from the framing canvas), data lineage and snapshot, features with prediction-time attestation, the champion table (CV) plus the single test number, the operating threshold and its budget rationale, slices where performance is weaker (M4's findings), limitations and refusal boundaries, retraining cadence and owner. The card is the interface between this course and SDA-AIE-113/216 — the artefact a deployment engineer and a validator both read first.

### 5. When *not* to tune

The decision framework, stated as a checklist run *before* any search: (a) learning curve converged? if still rising, data beats knobs; (b) error analysis mined? unimplemented feature findings beat knobs (Manafeth's new-customer feature is worth more than the 0.014 the search will find); (c) baseline honest and beaten? tuning a leaky pipeline optimises fiction; (d) budget justified? a +0.01 PR-AUC that saves 40 customers/month justifies 12 minutes — the same gain on a 100-customer base justifies nothing. Tuning is the *last* lever the workflow pulls, which is exactly why this module is the last before the capstone.

### 6. Common mistakes & production considerations

1. Grid-searching six knobs at three values each (729 fits) when 30 random draws cover the space better.
2. Linear-scale sampling of learning rate or alpha — half the budget lands in a corner of the space that behaves identically.
3. Reporting `best_score_` as the expected production performance — it selected the winner; it flatters the winner.
4. Tuning the pipeline's model but hand-tuning preprocessing outside the search — joint search or documented freeze, never invisible knobs.
5. Re-tuning on the test set after a disappointing test number — the quarantine's final exam; failing it converts the test set into training data permanently.
6. Tuning before the leakage tests — the search will happily amplify a leak into a "great" configuration.

Production considerations: log every search (space, seed, all results — not just the winner) so the tuning is reproducible and auditable; retraining pipelines re-run the *search* on cadence, not just the fit, because optimal configurations drift with data; hyperparameters are configuration artefacts versioned with the model (the SDA-AIE-113 config-management pattern receives them); compute governance — searches carry cost tags in enterprise MLOps platforms (SDA-AIE-216).

## Code Examples

### Randomised search over the full pipeline

```python
# notebooks/day4/lab7_tuning.ipynb — Tune the CHAMPION, jointly with its preprocessing
from scipy.stats import loguniform, randint, uniform
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from manafeth.features import build_preprocessor

pipe = Pipeline([
    ("prep", build_preprocessor()),
    ("clf", XGBClassifier(eval_metric="aucpr", random_state=42, n_jobs=-1)),
])

space = {
    # log-uniform where ratios matter, integers where structure does
    "clf__learning_rate":    loguniform(0.01, 0.3),
    "clf__n_estimators":     randint(200, 1200),
    "clf__max_depth":        randint(3, 8),
    "clf__min_child_weight": randint(1, 8),
    "clf__subsample":        uniform(0.6, 0.4),          # [0.6, 1.0]
    "clf__colsample_bytree": uniform(0.6, 0.4),
    "clf__reg_lambda":       loguniform(0.1, 10),
    "clf__scale_pos_weight": uniform(4, 5),              # around the 6.1 imbalance ratio
    # preprocessing is searchable too — one honest example:
    "prep__num__impute__strategy": ["median", "mean"],
}

search = RandomizedSearchCV(
    pipe, space,
    n_iter=30,                                           # the budget, decided BEFORE running
    cv=StratifiedKFold(5, shuffle=True, random_state=42),
    scoring="average_precision",
    n_jobs=-1, random_state=42, refit=True, verbose=1,
)
search.fit(X_train, y_train)                             # 150 fits ≈ 12 min on lab laptops
print("best CV PR-AUC:", round(search.best_score_, 3))   # 0.612 — a SELECTION score, not a promise
print(search.best_params_)
```

### Reading the search beyond the winner

```python
# notebooks/day4/lab7_tuning.ipynb — Is the winner robust or lucky? Look at the neighbourhood.
import pandas as pd

res = (pd.DataFrame(search.cv_results_)
         .sort_values("rank_test_score")
         [["mean_test_score", "std_test_score", "param_clf__learning_rate",
           "param_clf__max_depth", "param_clf__n_estimators"]]
         .head(10).round(4))
print(res)
# Top-10 within 0.006 of each other -> flat optimum: the choice is robust, stop searching.

# Which knobs mattered? Correlate each sampled knob with the score:
full = pd.DataFrame(search.cv_results_)
for p in ["param_clf__learning_rate", "param_clf__max_depth", "param_clf__subsample"]:
    corr = full[p].astype(float).corr(full["mean_test_score"], method="spearman")
    print(f"{p:32s} spearman {corr:+.2f}")
# learning_rate dominates (-0.61 beyond 0.15); depth mild; subsample ~flat -> next search narrows rate only.
```

### The final protocol: refit, single test evaluation, agreement check

```python
# notebooks/day4/lab7_tuning.ipynb — Day 4 H5: the quarantine ends. Once.
from sklearn.metrics import average_precision_score
import numpy as np

final_model = search.best_estimator_                     # refit=True: already trained on ALL training data

X_test = pd.read_parquet("data/splits/test_features.parquet")   # first read since Day 1
y_test = pd.read_parquet("data/splits/test_target.parquet")["churned_30d"]

test_proba = final_model.predict_proba(X_test)[:, 1]
test_pr_auc = average_precision_score(y_test, test_proba)
print(f"CV estimate 0.612 ± 0.010  |  test (once): {test_pr_auc:.3f}")
# test: 0.607 -> within one std of the CV estimate. The workflow kept its promise.

# Operating point at the voucher budget, on test:
thr = np.quantile(test_proba, 0.80)
flagged = test_proba >= thr
print(f"recall@20%: {y_test[flagged].sum() / y_test.sum():.2f}  "
      f"precision: {y_test[flagged].mean():.2f}")        # 0.74 / 0.51 -> the model-card numbers
```

### The model card

```markdown
<!-- project/MODEL_CARD.md — one page; the interface to SDA-AIE-113 / 216 and to any reviewer -->
# Model Card — Manafeth Churn Champion (xgb-churn-v1)
**Intended use:** rank active customers monthly; top-20% by risk receive retention vouchers. Not for credit or pricing decisions.
**Data:** manafeth_customers/orders snapshot 2025-11-01; 38,400 train / 9,600 test (stratified, seed 42); churn = no completed order in 30 days post-snapshot.
**Features:** 13 + segment (M6); all attested computable at snapshot time (FRAMING.md); leakage checks: shuffled-label PR-AUC 0.14 ✔.
**Performance:** CV PR-AUC 0.612 ± 0.010; test (single evaluation) 0.607; recall@20% 0.74, precision 0.51. Challenger (logistic) 0.531 — retained.
**Known weaknesses:** new customers (<3 months) recall 0.54 vs 0.76 established; Ramadan-seasonal shoppers over-flagged (M4 findings; feature work queued).
**Operating point:** threshold = 80th score percentile, re-derived per scoring run (threshold-drift guard, M4).
**Retraining:** monthly, full search quarterly; owner: CRM analytics; escalation: score-distribution shift > 5 pts contact rate.
```

## Hands-on Lab 7 — Tune the Champion, Close the Loop

| | |
|---|---|
| **Objective** | Run a budgeted randomised search over the full champion pipeline; read the results beyond the winner; execute the final refit + single test-set evaluation; deliver the model card |
| **Duration** | 50 minutes (Day 4 Hour 5, shared with capstone kickoff — search runs while teams read capstone briefs) |
| **Setup** | Lab 6 artefacts; `notebooks/day4/lab7_tuning.ipynb` skeleton; test partition untouched since Day 1 |

**Tasks**
1. *(5 min)* Pre-tuning checklist as a markdown cell: learning-curve verdict, error-analysis debts, leakage tests green, budget statement (30 × 5 fits).
2. *(15 min)* Launch the randomised search (it runs ~12 min — start it, then draft the model card skeleton while it runs; this is deliberate time design).
3. *(10 min)* Read the results: top-10 table, flatness verdict, knob-importance correlations, one sentence on what the *next* search would narrow.
4. *(10 min)* The final act: confirm `refit`, open the test set, single evaluation, agreement check against CV, operating point at budget.
5. *(10 min)* Complete MODEL_CARD.md; commit `feat(lab7): tuned champion, test evaluation, model card` — the golden thread is complete.

**Expected outputs**
```
Search: 30 draws × 5 folds, 12m20s; best CV PR-AUC 0.612 ± 0.010 (was 0.598)
Top-10 spread: 0.006 -> flat optimum, choice robust
Knob verdict: learning_rate dominates; subsample flat
Test (once): PR-AUC 0.607 — within 1 std of CV ✔ | recall@20% 0.74, precision 0.51
MODEL_CARD.md complete: 8/8 sections
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Search estimated > 30 min | Laptop cores / n_iter too high | `n_iter=20` is acceptable; note the budget change in the checklist cell |
| `Invalid parameter clf__...` | Pipeline step names differ | `pipe.get_params().keys()` is the source of truth |
| Test score far below CV (gap > 3 std) | Leak amplified by tuning, or stale test file | Stop; re-run shuffled-label test; verify test partition hash; investigate before renarrating |
| Someone re-tunes after seeing the test number | The final-exam failure | The instructor moment of the day: the test set is now spent; the honest path is new data or accepting the number |
| `best_score_` reported in the model card as expected performance | Selection-score confusion | Card takes the *test* number; `best_score_` is labelled as selection score |

**Instructor notes.** Design the hour so the 12-minute search runs while capstone briefs are read — dead compute time becomes project time. The agreement check (CV 0.612 vs test 0.607) is the emotional payoff of the entire week: the quarantine held, the estimate was honest, the workflow kept its promise — say exactly that sentence. If any pair's gap exceeds three stds, treat it as a live investigation with the room watching; it is almost always the stale-kernel unfiltered-RFM ghost, and catching it publicly on Day 4 is a gift.

## Mini Exercises

**Quiz.** (1) Why does random search beat grid at equal budget in high dimensions? (2) Why log-uniform for learning rate? (3) `best_score_` = 0.612 — what may you claim, and what may you not? (4) When does nested CV earn its cost? (5) You saw the test number and want one more tweak — what did the tweak just cost you?
**Debugging exercise.** A search reports best CV 0.71 (!). The space included `prep__num__impute__add_indicator=[True, False]` *and* a stale feature list with `next_month_orders` re-included. Participants must find which change produced fiction and which was legitimate.
**Code-review exercise.** Review a tuning notebook: 729-cell grid on six knobs, linear-scale alpha, `best_score_` quoted to the business, no seed on the search. Four findings, plus the 10-line honest rewrite.
**Discussion.** Manafeth's search bought +0.014 PR-AUC for 12 minutes; the M4 new-customer feature is estimated at +0.02 for two days of pipeline work. Sequence the roadmap and defend it to a manager who says "just tune it harder."

## Case Study — Tuning Under a Compute Window at a Makkah Hospitality Group

**Scenario.** A hospitality group operating 11 Makkah properties forecasts nightly demand per property to drive pricing and staffing. Models retrain weekly; the analytics team gets a 4-hour overnight window on a shared on-prem server (no cloud burst — data residency policy). The previous contractor left a 4,096-combination grid search that never finished inside the window, so staff had been silently truncating it — deploying whatever configuration the alphabet reached first.

**Business context.** Umrah seasonality, Ramadan, and Hajj create demand regimes an untuned model misprices in both directions; but an unfinished, order-dependent search is worse — configurations shipped by accident, undocumented and unreproducible.

**Technical challenge.** Redesign tuning to *finish, honestly, inside the window*: one gradient-boosted model per property cluster (not per property — a pooling decision made by error analysis), randomised search with log-uniform rate and integer depth, `n_iter` sized from measured fit cost to fill 3 of the 4 hours with 25% headroom, seeds fixed, every result logged. Nested evaluation is skipped in favour of a rolling out-of-time test month — the temporally honest choice for forecasting (M4's OOT lesson recurring).

**Constraints.** Shared server: searches must be `nice`-d and killable; the pricing team needs the new configuration by 06:00 or yesterday's stays; audit requires reproducing any historical week's model from logs alone; Hajj-week data is embargoed from general training (governance rule) and evaluated as its own slice.

**Solution approach.** Budget-first design: measured fit cost (38 s) × 5 folds × `n_iter` ≤ 180 min → `n_iter=56`; flat-optimum verification each week (top-10 spread logged; a widening spread is the retune-harder signal); knob-importance tracking across weeks shows the space itself can shrink — after six weeks, three knobs are frozen and the window shortens to 90 minutes. Result: reproducible weekly configurations, a documented +9% revenue-weighted forecast improvement over the truncated-grid era, and an auditable trail.

**Discussion questions.** (1) The truncated grid sometimes shipped *good* configurations — why is it still indefensible? (2) Defend the property-cluster pooling decision: what evidence from M4's toolkit supports or refutes it? (3) Design the weekly one-page tuning log an auditor and a pricing manager can both read. (4) When the top-10 spread widens one week, what are the three candidate causes and their checks?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Tuned champion CV PR-AUC | Model quality | ≥ 0.61 (+0.01 over untuned) | search output |
| Search budget adherence | Process discipline | stated before running; actual within 25% | checklist cell + `%%time` |
| CV-vs-test agreement | Workflow integrity | gap ≤ 1 CV std | final-protocol cell |
| Test-set evaluations | Workflow integrity | exactly 1, ever | notebook audit |
| Model card completeness | Communication | 8/8 sections, reviewer-auditable | card checklist |
| Search reproducibility | Auditability | identical `best_params_` across pairs (seeded) | scoreboard |

**Example benchmark table (the course's final scoreboard):**

| Stage | PR-AUC | recall@20% | Evidence |
|---|---|---|---|
| Dummy (Day 1) | 0.141 | 0.20 | floor |
| Heuristic (Day 1) | — | 0.41 | business bar |
| Logistic + features (Day 2–3) | 0.531 CV | 0.66 | challenger |
| XGBoost champion (Day 3) | 0.598 CV | 0.73 | harness |
| + segments (Day 4) | 0.607 CV | 0.73 | harness |
| **Tuned champion (Day 4)** | **0.612 CV / 0.607 test** | **0.74 test** | **single test evaluation** |

## Required Visuals and Training Assets

### Diagrams
1. **Grid vs random budget coverage** — *Purpose:* the module's anchor argument. *Elements:* two panels of a 2-D space where only one dimension matters; 9 grid points probing 3 distinct values of it vs 9 random points probing 9; the marginal histograms along each axis making the coverage difference undeniable. *Style:* twin scatter panels with marginal strips.
2. **The selection protocol pipeline** — *Elements:* training data → CV search (folds × draws grid) → best config → refit on all training → single arrow to the padlocked test set → model card; a red loop-back arrow from test to search struck out. *Style:* extends the M1 workflow map — same padlock, final position.
3. **Nested CV, unfolded** — *Elements:* outer folds each containing a complete inner search; captions "inner selects, outer estimates"; a "when: small data / strict governance" badge. *Style:* nested boxes, deliberately schematic.
4. **The last-lever checklist** — *Elements:* the four pre-tuning questions (curve? features? leaks? budget?) as gates before a "search" button. *Style:* gate flowchart, printable; pairs with M4's verdict guide.

### Images
1. **Search progress + result screenshot** — *why:* expected output; *content:* verbose fit log, 12m20s wall clock, best score line.
2. **Top-10 results table** — *why:* the flatness read; *content:* 0.006 spread highlighted.
3. **CV-vs-test agreement cell** — *why:* the week's payoff artefact; *content:* `0.612 ± 0.010 | test: 0.607`.
4. **Completed model card render** — *why:* the deliverable format; *content:* the one-pager as it appears on the repo.

### Simulations
1. **The lucky winner** — *Setup:* `n_iter=200` on a deliberately tiny 2k-row subsample. *Expected:* best CV score visibly exceeds its own test check; the top-10 spread is wide. *Learning objective:* selection bias grows with draws and shrinks with data — see it once at small scale.
2. **The spent test set** — *Setup:* scripted sequence of five "one more tweak" test evaluations, each nudging choices. *Expected:* apparent test PR-AUC climbs 0.607 → 0.625 while a *second* held-out sample shows 0.605 flat. *Learning objective:* the quarantine is arithmetic — its violation has a measurable price.
3. **The amplified leak** — *Setup:* the debugging exercise's stale feature list inside a search. *Expected:* search converges hard onto configurations that exploit the leak. *Learning objective:* tuning optimises whatever you gave it, fiction included.

### Interactive Activities
- **Budget auction (10 min):** teams get 150 fictional fit-credits and bid them across knobs/draws/folds for a stated problem; designs are compared against the flat-optimum reveal.
- **Model-card review circle (15 min):** pairs swap cards and review as the SDA-AIE-113 receiving engineer — "could I deploy from this page alone?"; unanswerable questions are card defects, logged and fixed.

### Datasets
Golden-thread artefacts, final form: the tuned pipeline consumes exactly the M3 feature module and M6 segment feature — by design, the search's legality rests on that packaging. Plus `makkah_demand_sample.parquet` (synthetic, 8,000 rows) for the case-study walkthrough.

### Demo Requirements
- **Instructor demo:** launch the search live and *leave it running on the projector* while introducing the capstone — the progress bar as ambient proof that budgets are real; return to read the results and execute the test-set opening ceremonially (the room should feel the once-ness).
- **Student demo:** one pair presents their knob-importance verdict and next-search proposal.
- **Expected outputs:** every pair ends Day 4 with a tuned, test-evaluated champion and a complete model card — the Manafeth thread is closed, and the capstone repeats the entire arc on real data, unassisted.

---

# Final Capstone Project

## Title: End-to-End Modelling Project on Real Data

## Project Scenario

For four days you executed the machine-learning workflow on Manafeth with an instructor at your shoulder and a golden thread beneath your feet. The capstone removes both. In teams of two, you select a **real public dataset** from the vetted menu (chosen at Day 4 Hour 5 kickoff), frame a business problem it can honestly answer, and execute the complete workflow — framing canvas to model card — in one day, unassisted. Nothing new is taught on Day 5; everything you need was built in Labs 1–7 and lives in your own repository. The capstone's claim is the course's claim: the *workflow* transfers, not the dataset.

**Vetted dataset menu (each hides at least one deliberate trap — part of the assessment):**

| Dataset | Task | The trap the rubric watches for |
|---|---|---|
| Telco customer churn | Binary classification, imbalanced | `TotalCharges` near-duplicates tenure×monthly — collinearity & interpretation |
| Hotel booking cancellations | Binary classification | `reservation_status` leaks the label outright; deposit-type is a near-leak |
| Bike-sharing hourly demand | Regression, temporal | Random split is fiction; temporal split + calendar features mandatory |
| Bank marketing (term deposits) | Binary classification, imbalanced | `duration` is only known after the call — the canonical leakage column |
| Used-car listings prices | Regression, long tail | Log target; rare models need a refuse-to-predict boundary (Markabat, M2) |
| Online retail transactions | Regression via RFM aggregation | Unit-of-analysis: transactions must become customer-snapshots without future rows |

Teams may propose their own dataset; instructor approval required (checks: ≥ 5,000 rows, a defensible target, no personal data requiring PDPL review, downloadable to the shared drive by Day 4 evening).

## Requirements

**Mandatory (maps to grading rubric):**

1. **Framing canvas (LO1):** completed `FRAMING.md` — business decision, unit of analysis, mechanically computable target, prediction-time feature attestation, success metric with threshold, baselines, stop condition — committed *before* any modelling code runs.
2. **Split discipline (LO2, LO6):** stratified or temporal split with the choice justified in one sentence; test partition quarantined with exactly one evaluation at the end; the split cell precedes all EDA-driven decisions.
3. **Baselines (LO2, LO5):** dummy baseline plus one domain heuristic, both recorded before the first model; every reported model beats both or the notebook says why it was kept anyway.
4. **Leakage-proof pipeline (LO3, LO4):** all preprocessing inside a `Pipeline`/`ColumnTransformer` fit on training data only; imputation, scaling, and encoding choices justified per column group; at least two engineered features beyond the raw columns; the shuffled-label test run and reported.
5. **Honest evaluation (LO5):** cross-validated comparison of ≥ 3 model families (one interpretable challenger mandatory) on shared folds with mean ± std; metric chosen at framing time in business terms; threshold or operating point derived from a stated constraint, not the 0.5 default.
6. **Error analysis (LO5, LO6):** ≥ 2 slice- or row-level findings, each with a proposed fix; the dataset's planted trap found and neutralised (or an argued explanation of why it does not apply).
7. **Systematic tuning + final protocol (LO7, LO2):** budgeted `RandomizedSearchCV` (or grid where the space is genuinely small) over the full pipeline; budget stated before running; top-10 flatness read; refit and **single** test-set evaluation with a CV-agreement check.
8. **Model card:** one page in the Lab 7 format — intended use, data lineage, feature attestation, champion table, test number, operating point, known weaknesses, retraining cadence.

**One extension (choose at least one):**
- Unsupervised component: segment the population per the M6 protocol (null test included) and measure the segment feature's effect on the supervised model
- Calibration analysis: calibration curve + Brier score; recalibrate if warranted and show the before/after
- Learning-curve verdict used to argue a data-versus-features investment recommendation to a fictional sponsor
- `GroupKFold` or `TimeSeriesSplit` evaluation where the data's structure demands it, with the inflation quantified against naive CV
- A second dataset from the menu, framing only (canvas + split + baselines) — breadth for early finishers

## Architecture (target state)

```
capstone-repo/
├── FRAMING.md            ← committed first; audited against the notebook history
├── notebooks/
│   └── capstone.ipynb    ← the story: audit → split → baseline → iterate → tune → test (once)
├── src/features.py       ← preprocessing + engineered features (importable, pipeline-packaged)
├── data/
│   ├── raw/              ← untouched download
│   └── splits/           ← quarantined test partition (one read, Hour 4)
├── MODEL_CARD.md         ← the deliverable a reviewer reads first
└── SCOREBOARD.md         ← dummy → heuristic → challenger → champion → tuned, same folds

Workflow:  frame → SPLIT 🔒 → baselines → [features → model → CV → error analysis]* → tune → test (once) → card
```

## Deliverables

1. Repository (or shared folder) with the structure above and a runnable top-to-bottom notebook (`Restart & Run All` succeeds on the lab environment)
2. `FRAMING.md` with commit timestamp preceding all modelling commits
3. `MODEL_CARD.md` complete (8/8 sections) with the single test evaluation and CV-agreement statement
4. `SCOREBOARD.md`: all models on shared folds, mean ± std, baselines included
5. 5-minute demo: the business question, one framing decision defended, the champion table, the trap found, the test-vs-CV agreement moment

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| C1: Framed and split | End Day 5 H1 | `FRAMING.md` committed; split cell verified; quarantine declared |
| C2: Pipeline and baselines | End Day 5 H2 | dummy + heuristic on scoreboard; shuffled-label test green |
| C3: Evaluated, improved, tuned | End Day 5 H3 | ≥ 3 models on shared folds; 2 findings; search complete within budget |
| C4: Finalised | End Day 5 H4 | single test evaluation done; model card complete; peer review checklist signed |
| C5: Demo | Day 5 H5 | rubric scoring live |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Problem framing & data discipline | 15 | Canvas precise and mechanically checkable; split choice justified; quarantine airtight | Canvas complete but one vague field; split correct, justification thin | Target underspecified; EDA before split; test set consulted early |
| Pipeline & feature engineering | 15 | All preprocessing pipeline-packaged; ≥ 2 engineered features with measured lift; choices justified | Pipeline correct; features present but lift unmeasured or marginal | Transforms outside the pipeline; fit-on-all-data; no engineered features |
| Baselines & model comparison | 15 | Dummy + heuristic + interpretable challenger + champion, same folds, ± std | All present; folds shared but variance unreported | No heuristic; comparisons across different splits; champion unopposed |
| Evaluation & error analysis | 20 | Metric matches the framed decision; operating point from a stated constraint; 2+ findings with fixes; the trap found | Metric right; findings present but fixes vague; trap found late or partially | Accuracy on imbalanced data; default threshold unexamined; trap shipped |
| Tuning & final protocol | 15 | Budget stated first; flatness read; single test evaluation; CV-agreement check articulated | Search sound; results read only at the winner; test protocol correct | `best_score_` reported as performance; test set opened more than once |
| Model card & notebook narrative | 12 | Card auditable by a stranger; notebook reads as an argument, not a scratchpad | Card complete but one section thin; notebook runs but rambles | Card missing sections; notebook fails Restart & Run All |
| Demo | 8 | Crisp, evidence-first, questions handled; the agreement moment landed | Demo works; storyline present but leans on the instructor's prompts | Cannot explain own framing or numbers |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope scores ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository evidence first*, demo second: commit order proves the split-before-EDA claim; the notebook's cell history exposes test-set peeking better than any interview.
- Anti-pattern flags that cap a criterion at 70%: a test-set score that appears anywhere before Hour 4; a shuffled-label test that was run but not shown; scoreboard entries on mismatched folds; a "found" trap with no evidence of when it was found.
- Verify one claim live per team during the demo: ask them to re-run the shuffled-label cell, or to state what their CV std permits them to claim about their champion versus their challenger.
- The trap is diagnostic, not punitive: a team that finds `duration` in bank marketing and *quantifies* the inflation it caused (before/after PR-AUC) has demonstrated LO6 more convincingly than a team whose dataset hid it from them — score the demonstration, not the luck of the menu.
- Teams that finish C3 early should be steered to extensions, not to more tuning — the M7 last-lever checklist applies to them too.

## Bonus Tasks (for early finishers / distinction seekers)

1. Nested CV on the final champion; compare the nested estimate against the single test number and explain the difference in two sentences
2. A `predict_with_refusal()` wrapper that returns "out of training range" for extrapolation-zone rows (the Markabat boundary, implemented), with a test
3. Threshold-drift guard: re-derive the operating threshold on a resampled month and report the contact-rate movement (M4 simulation, reproduced on capstone data)
4. Champion/challenger memo: one page arguing which model ships, in language the fictional sponsor's CFO can act on

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** A ministry wants to "understand complaint patterns" but no labels exist. What is the honest task framing? → unsupervised clustering feeding a human taxonomy — not an imaginary classifier.
**Q2.** State the timestamp test for leakage in one sentence. → would this feature's value exist at prediction time? If not, it is leakage by construction.
**Q3.** Why must `train_test_split` happen before EDA-driven feature selection? → otherwise feature choices encode test-set information and offline scores inflate.
**Q4.** Name the two acceptance bars every course model must beat. → the dummy baseline and the domain heuristic.
**Q5.** `DummyClassifier(strategy="most_frequent")` scores 86% accuracy on a 14%-positive problem. What does that number mean? → nothing about skill; it restates the class balance — the floor, not an achievement.
**Q6.** Ridge vs lasso in one sentence each. → ridge shrinks all weights smoothly (many weak signals); lasso drives some weights to exactly zero (embedded feature selection).
**Q7.** `exp(coef) = 1.6` on `support_tickets` in a logistic model — say it in business language. → each additional support ticket multiplies the odds of churn by 1.6.
**Q8.** Which model families require feature scaling and why, in one line? → distance- and penalty-based models (k-NN, SVM, k-means, PCA, regularised linear); trees don't — splits are order-based.
**Q9.** What does `handle_unknown="ignore"` prevent in production? → a crash on the first unseen category (the "Taif launch" incident).
**Q10.** Why must target encoding be fit inside each CV fold? → fit on the full training set it leaks the label into the features; fold scores become optimistic fiction.
**Q11.** State the prediction-time rule for aggregate features. → aggregates use only events strictly before the snapshot date; an all-time aggregate summarises the future.
**Q12.** What does the shuffled-label test detect, and what result means "honest"? → any path from label to features/pipeline; score ≈ the positive class rate means honest.
**Q13.** Why is PR-AUC preferred over ROC-AUC at 14% positives? → its baseline is the positive rate, so it doesn't flatter models when negatives dominate; it tracks the precision/recall trade the business feels.
**Q14.** Who sets the classification threshold and with what input? → the business, via an explicit constraint (budget, cost ratio) — never the 0.5 default by omission.
**Q15.** CV results 0.53 ± 0.08 vs 0.51 ± 0.02 — what may you claim? → nothing yet; the difference is inside one standard deviation — not a model choice.
**Q16.** Forests average away ___; boosting stacks away ___. → variance; bias.
**Q17.** What does early stopping convert `n_estimators` into, and where must reported scores come from? → an observed quantity; from folds the early-stopping eval set never touched.
**Q18.** Give the three levels of unsupervised evaluation, weakest to strongest. → internal indices (silhouette) → stability (ARI across runs) → external usefulness (predicts something it wasn't built from).
**Q19.** Why does random search beat grid search at equal budget when many knobs don't matter? → random probes n_iter distinct values per dimension; grid wastes budget on redundant combinations of unimportant knobs.
**Q20.** You evaluated on the test set, then made "one more tweak" and re-evaluated. What did the tweak cost? → the test set — it is now a validation set; its number is no longer an unbiased estimate of production performance.

## Practical Assessments

Both practical assessments are scored inside the daily-labs component; they reuse course artefacts, so no separate environment is needed.

**PA-1 — The Sabotaged Notebook (30 min, Day 3 Hour 3, embedded in Lab 4):** Each pair receives a variant of the Manafeth workflow with three planted violations drawn from a pool (scaler fit before split; unfiltered aggregate; threshold tuned on test; comparison across mismatched folds; train metrics on the scoreboard). Deliverable: each violation named, its inflation quantified by honest re-run, and the corrected number stated. Scored: diagnosis (40%), quantified damage (40%), corrected protocol (20%).

**PA-2 — The Evaluation Triage (30 min, Day 4 Hour 4, embedded in Lab 7 prep):** Given a one-page "model approval request" (metric table, split description, tuning summary — containing two admissibility flaws such as `best_score_` reported as expected performance, or random CV on temporal data), write the validator's response: what is admissible, what must be redone, and the exact protocol for the redo. Scored against a model answer: triage correctness (50%), protocol precision (30%), business-language clarity (20%).

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| **Daily labs** (catalog component — 60%) | | |
| — Lab completion & checkpoints (Labs 1–7) | 40% | scoreboard entries + committed expected outputs per lab |
| — PA-1 + PA-2 | 12% | artefacts + written responses |
| — Quiz (10-question selection) | 8% | closed book, 15 min, Day 5 Hour 5 pre-demo |
| **End-to-end ML project** (catalog component — 40%) | 40% | capstone rubric, repository-first |

**Core ML badge** issuance requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical "engineered features" or identical capstone framing across teams on the same dataset are checked; shared seeds make legitimate identical *baselines* expected — the check targets authored content). The badge is required for all Specialist AI Engineer modules and DSC-211; the natural next module is SDA-AIE-112.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Regenerate the Manafeth synthetic datasets (`manafeth_customers`, `manafeth_orders`) with the course tooling at seed 42; verify the three planted leaky columns, the 14.0% churn rate, and the Ramadan seasonality against the expected-output blocks in Labs 1–7
- [ ] Run all seven checkpoint solution notebooks (`lab1_solution.ipynb` … `lab7_solution.ipynb`) top-to-bottom on a clean environment; confirm every expected-output number matches (drift here means a library version moved — fix the pin, not the course)
- [ ] Time the Lab 7 reference search on the actual classroom hardware; if > 15 min, reduce the published `n_iter` and update the budget line in the lab
- [ ] Download and mirror the six capstone menu datasets to the shared drive (classroom networks and public dataset hosts do not mix on demo day); verify each trap is present in the mirrored version
- [ ] Prepare the sabotaged notebooks (`sabotaged_features.ipynb`, PA-1 variants) and all `sim-*` branches; verify the 0.97 unfiltered-RFM number reproduces
- [ ] Set up the class scoreboard notebook on the shared drive; pre-fill the dummy rows so Day 1 pairs have a format to match
- [ ] Print A4 posters: the workflow map (padlock loud), the capacity dial, the metric-choice decision tree, the evaluation ladder, the last-lever checklist
- [ ] Verify the fallback environment (JupyterHub or Colab): course notebooks run unchanged, datasets reachable, XGBoost importable
- [ ] Check the delivery dates against the Ramadan/Eid calendar — both the schedule (breaks, energy) and the `RAMADAN_START` constants in `calendar_features()` (update the year map if the course tooling hasn't)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 (64-bit) with venv or conda; git installed and configured
- [ ] `pip install -r requirements.txt` from the course repo — pins scikit-learn ≥ 1.5, pandas ≥ 2.2, xgboost ≥ 2.0, matplotlib, jupyterlab, pyarrow, scipy
- [ ] Launch JupyterLab; run the provided `check_env.ipynb` (imports, versions, a 10-second XGBoost fit, parquet read) — it prints ✓/✗ per item
- [ ] Pull the course datasets from the shared drive link; verify `manafeth_customers.parquet` opens (48,000 × 19)
- [ ] Laptop spec note: 8 GB RAM minimum; participants below it should say so now — pairing assignments will put them on the stronger machine for Labs 5 and 7
- [ ] Fallback: a Google account for Colab, in case local setup fails on the day

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| XGBoost wheel fails to install (Windows / new Python) | High | Pre-checked in `check_env.ipynb`; fallback conda install or `HistGradientBoostingClassifier` for the day, fix at break |
| Stale-kernel resurrects the unfiltered-RFM leak (0.97 returns) | High | Course mantra: Restart & Run All before believing any number; the shuffled-label test is one cell away |
| Parquet read fails (`pyarrow` missing) | Medium | It's in requirements; the CSV mirrors exist for true emergencies |
| Divergent scoreboard numbers across pairs | Medium | Always a workflow bug (seed, split order, feature list diff) — debug publicly, it is the lesson |
| CV or search runs exceed the hour on weak laptops | Medium | `n_jobs=-1` first; then reduce folds to 3 or `n_iter` to 20 with the budget change noted in the checklist cell |
| Participants peek at the test set "just to check" | Medium | The quarantine is assessed (notebook audit); make the Day 4 H5 opening ceremonial so the once-ness lands |
| Excel-opened CSVs re-saved with mangled encodings/dtypes | Medium | Use the parquet mirrors; never open course CSVs in Excel |
| Strong participants race ahead and tune everything | Low | Route them to error-analysis findings and extensions — enforce the M7 last-lever checklist socially |
| Fear of the math among domain-background participants | Low | The course's mechanism-over-derivation stance is deliberate; pair them with strong-Python partners — their framing instincts are the pair's asset |

## Timing Recommendations

- Protect Lab 3 (pipeline debugging) and Lab 7 (search wall-clock) at full length; they are the overrun-prone hours. Compress M6 theory if behind — clustering lands through the lab and the noise-null demo, not the slides.
- The Day 2 Hour 5 feature workshop is the first buffer to spend if Day 2 slips; fold its vote into the first ten minutes of Day 3.
- If a cohort is strong: pull calibration and `HistGradientBoosting` head-to-head into main scope on Day 3; offer the second-dataset extension at capstone kickoff.
- If a cohort is weak: make Lab 6 task 5 (segment feature into the champion) a guided demo; never cut the null test or the Day 4 H5 test-set opening — they are the course's thesis made visible.
- Hard rule: capstone milestones C1–C4 gate on the clock, not on polish. A team still "improving features" at Hour 3 ships a worse project than a team that froze and evaluated honestly — say this at kickoff and enforce it at C3.

## Discussion Prompts (use during transitions)

1. "What is the most expensive model your organisation ever built that answered the wrong question?"
2. "Your baseline catches 41% for free. Finish this sentence to your CFO: 'the model is worth building because…'"
3. "Which number do you trust more: 0.61 on a single split, or 0.53 ± 0.01 under CV — and what did the difference cost whoever shipped the first one?"
4. "The test set is opened once. What does your team's current 'test set' actually measure, honestly?"
5. "Tuning bought us +0.014 in 12 minutes; a new feature is worth +0.02 in two days. Who in your organisation decides that sequencing today — and should they?"

## Wrap-up (final day, last 15 minutes)

- Map the week onto the workflow poster one last time: every capstone requirement traces to the module that taught it — the padlock closes the loop it opened on Day 1.
- The scoreboard retrospective: dummy 0.141 → heuristic 0.41 → logistic 0.66 → tuned champion 0.74 recall@20%, and what each jump cost — framing, features, ensembles, tuning, in that order of value.
- Forward pointers: SDA-AIE-112 (deep learning — the same loss-minimisation picture with a different function family, as promised in M2); SDA-AIE-113 consumes exactly the pipeline + model card artefacts built here; DSC-211 cross-lists this module for the Data Scientist track; the Core ML badge unlocks all Specialist AI Engineer modules.
- Collect: capstone repositories, model cards, scoreboards; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, scikit-learn ≥ 1.5, XGBoost ≥ 2.0, pandas ≥ 2.2. Verify pinned versions in the course requirements file before each delivery, and re-run the seven solution notebooks after any dependency change.*
