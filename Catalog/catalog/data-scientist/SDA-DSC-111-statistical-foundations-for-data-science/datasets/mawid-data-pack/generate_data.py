#!/usr/bin/env python3
"""
generate_data.py — Course data generator for SDA-DSC-111
Statistical Foundations for Data Science (SDAIA Academy)

Generates the "Mawid Analytics" golden-thread dataset and every auxiliary
file the course uses. Synthetic, SDAIA-style, modelled on a national
primary-care clinic-booking platform. NO real patient data.

Golden-thread checks (run verify_data.py after generation):
  * overall no-show rate            ~ 0.18
  * wait time: median ~18 min, right-skewed lognormal, mean ~21
  * Simpson reversal PRESENT: crude reminded rate HIGHER (targeted rollout),
    reminders HELP within every clinic_type and risk_band stratum
  * adjusted reminder odds ratio    ~ 0.68
  * randomized pilot (ab_pilot==1): control ~0.21 vs reminder ~0.15
  * Makkah (high) and Eastern Province (low) exclude the national Wilson CI;
    the smallest region's point estimate overlaps it (the "small-region trap")

Pinned against: numpy>=1.26, scipy>=1.11, pandas>=2.0
"""
import numpy as np
import pandas as pd
from pathlib import Path

import sys
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 42   # course seed: 42
rng = np.random.default_rng(SEED)
OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

N_TOTAL = 50_000
N_PILOT = 8_000           # randomized SMS pilot rows (~4,000/arm)

# ----------------------------------------------------------------------
# 1. Regions (13 administrative regions of Saudi Arabia)
#    ns_off: extra no-show logit AFTER compensating for urban/rural mix,
#    so only Makkah / Eastern are genuinely different by design.
# ----------------------------------------------------------------------
REGIONS = [
    # (en, ar, volume share, ns_off, wait_off, urban clinic prob)
    ("Riyadh",           "الرياض",          0.245,  0.00,  0.08, 0.85),
    ("Makkah",           "مكة المكرمة",     0.215,  0.20,  0.12, 0.80),
    ("Eastern Province", "المنطقة الشرقية", 0.150, -0.19, -0.08, 0.80),
    ("Asir",             "عسير",            0.080,  0.00,  0.02, 0.45),
    ("Madinah",          "المدينة المنورة", 0.062,  0.00, -0.02, 0.70),
    ("Jazan",            "جازان",           0.050,  0.00,  0.05, 0.35),
    ("Qassim",           "القصيم",          0.042,  0.00, -0.04, 0.55),
    ("Tabuk",            "تبوك",            0.032,  0.00,  0.00, 0.50),
    ("Hail",             "حائل",            0.024,  0.00, -0.03, 0.45),
    ("Najran",           "نجران",           0.020,  0.00, 0.04, 0.35),
    ("Al-Bahah",         "الباحة",          0.016,  0.00, -0.02, 0.30),
    ("Northern Borders", "الحدود الشمالية", 0.012,  0.00,  0.00, 0.35),
    ("Al-Jouf",          "الجوف",           0.0075, -0.20, -0.05, 0.35),
]
region_en = [r[0] for r in REGIONS]
shares = np.array([r[2] for r in REGIONS]); shares = shares / shares.sum()
URBAN_P  = {r[0]: r[5] for r in REGIONS}
RURAL_EFF = 0.85                                   # rural no-show logit effect
reg_ns_design = {r[0]: r[3] for r in REGIONS}
reg_wt_eff = {r[0]: r[4] for r in REGIONS}

# ----------------------------------------------------------------------
# 2. Clinics (~120), urban/rural, with random effects
# ----------------------------------------------------------------------
N_CLINICS = 120
clinic_counts = np.maximum(2, np.round(shares * N_CLINICS).astype(int))
while clinic_counts.sum() > N_CLINICS:
    clinic_counts[np.argmax(clinic_counts)] -= 1
while clinic_counts.sum() < N_CLINICS:
    clinic_counts[np.argmax(shares)] += 1

clinics, cid = [], 0
for (reg, cnt) in zip(region_en, clinic_counts):
    for _ in range(cnt):
        cid += 1
        ctype = "urban" if rng.random() < URBAN_P[reg] else "rural"
        clinics.append({
            "clinic_id": f"CL{cid:03d}", "region": reg, "clinic_type": ctype,
            "size_w": rng.lognormal(0.30 if ctype == "urban" else 0.0, 0.35),
            "re_noshow": rng.normal(0, 0.14),
            "re_wait":   rng.normal(0, 0.16),
            "avg_daily_slots": int(rng.integers(60, 220) if ctype == "urban"
                                   else rng.integers(25, 90)),
        })
clin = pd.DataFrame(clinics)

# ----------------------------------------------------------------------
# 3. Appointments: region volume follows `shares` exactly in expectation;
#    within a region, clinic volume follows clinic size.
# ----------------------------------------------------------------------
w = np.zeros(len(clin))
for i, reg in enumerate(region_en):
    m = (clin["region"] == reg).to_numpy()
    w[m] = shares[i] * clin.loc[m, "size_w"].to_numpy() / clin.loc[m, "size_w"].sum()
w = w / w.sum()
idx = rng.choice(len(clin), size=N_TOTAL, p=w)
df = clin.iloc[idx][["clinic_id", "region", "clinic_type",
                     "re_noshow", "re_wait"]].reset_index(drop=True)
df.insert(0, "appointment_id", [f"AP{i:06d}" for i in range(1, N_TOTAL + 1)])
rural = (df["clinic_type"] == "rural").to_numpy().astype(int)

# Patient / visit covariates
df["patient_age"] = np.clip(rng.normal(41, 14, N_TOTAL).round(), 15, 90).astype(int)
df["lead_time_days"] = np.clip(np.round(rng.lognormal(np.log(6.0), 0.80, N_TOTAL)),
                               0, 60).astype(int)
df["prior_no_shows"] = rng.poisson(0.35, N_TOTAL).clip(0, 6)
df["staff_on_shift"] = np.clip(rng.poisson(6 - 1.5 * rural, N_TOTAL), 2, 12)
df["is_peak_hour"] = rng.binomial(1, 0.35, N_TOTAL)

# ----------------------------------------------------------------------
# 4. risk_band — baseline SEGMENT risk (clinic type, region, clinic effect).
#    This is the Module-5 confounder: it drove the reminder rollout AND it
#    drives no-shows. (prior_no_shows / lead time are patient-level drivers
#    kept OUT of the band so their regression effects stay interpretable.)
# ----------------------------------------------------------------------
# Empirical composition compensation: each region's offset is corrected for
# its ACTUAL patient-level rural share and clinic-effect draw, so a region's
# design rate is not pushed around by clinic-size luck. Only Makkah (high),
# Eastern Province (low) and Al-Jouf (low, tiny n) differ by design.
re_ns = df["re_noshow"].to_numpy()
re_ns = re_ns - df.groupby("region")["re_noshow"].transform("mean").to_numpy()
rural_share_reg = df.groupby("region")["clinic_type"]     .transform(lambda s: (s == "rural").mean()).to_numpy()
rural_share_all = float((df["clinic_type"] == "rural").mean())
region_ns = (df["region"].map(reg_ns_design).to_numpy()
             - RURAL_EFF * (rural_share_reg - rural_share_all))
segment = RURAL_EFF * rural + region_ns + re_ns
# outcome-side risk: steep urban/rural contrast, gentler within-type gradient
seg_out = 1.18 * rural + 0.58 * (region_ns + re_ns)
df["risk_band"] = pd.qcut(segment + rng.normal(0, 0.18, N_TOTAL), 4,
                          labels=["Q1", "Q2", "Q3", "Q4"]).astype(str)
band_num = df["risk_band"].str[1].astype(int).to_numpy()

# ----------------------------------------------------------------------
# 5. SMS reminder assignment
#    (a) randomized pilot rows: fair coin (the clean A/B test)
#    (b) all other rows: OBSERVATIONAL rollout targeted at high-risk
#        segments -> the crude comparison reverses (Simpson's paradox)
# ----------------------------------------------------------------------
pw = np.array([0.45, 0.80, 1.00, 0.95])[band_num - 1]
pilot_idx = rng.choice(N_TOTAL, size=N_PILOT, replace=False, p=pw / pw.sum())
df["ab_pilot"] = 0
df.loc[pilot_idx, "ab_pilot"] = 1

# observational rollout: allocation driven by the risk BAND (targeting policy)
alloc_logit = -3.10 + 1.30 * (band_num - 1) + 1.50 * rural
sms_obs = rng.binomial(1, 1 / (1 + np.exp(-alloc_logit)))
sms_pilot = rng.binomial(1, 0.5, N_TOTAL)
df["sms_reminder"] = np.where(df["ab_pilot"] == 1, sms_pilot, sms_obs)

# Mediator: reminded patients sometimes proactively reschedule
df["rescheduled"] = rng.binomial(1, np.where(df["sms_reminder"] == 1, 0.15, 0.02))

# ----------------------------------------------------------------------
# 6. Outcome: no_show — logistic model.
#    Total reminder effect ~ OR 0.68 (direct + via rescheduling).
# ----------------------------------------------------------------------
from scipy.optimize import brentq
base_lin = (seg_out                               # baseline-risk confounder
            + 0.62 * df["prior_no_shows"].clip(0, 3)
            + 0.034 * (df["lead_time_days"] - 6)
            - 0.013 * (df["patient_age"] - 41)
            - 0.335 * df["sms_reminder"]          # direct protective effect
            - 0.700 * df["rescheduled"])          # mediated protective effect

# Calibrate each region's mean rate to its DESIGN target on the probability
# scale (handles logistic curvature and uneven reminder coverage):
#   Makkah high, Eastern Province low, Al-Jouf low-ish; everyone else national.
TARGET = {r: 0.181 for r in region_en}
TARGET.update({"Makkah": 0.205, "Eastern Province": 0.158, "Al-Jouf": 0.152})
logit = lambda p: np.log(p / (1 - p))
adj = {r: 0.0 for r in region_en}
for _ in range(5):
    lin = base_lin + df["region"].map(adj).to_numpy()
    b0 = brentq(lambda b: (1 / (1 + np.exp(-(b + lin)))).mean() - 0.181, -8, 4)
    p = 1 / (1 + np.exp(-(b0 + lin)))
    for r in region_en:
        m = float(p[(df["region"] == r).to_numpy()].mean())
        adj[r] += float(logit(TARGET[r]) - logit(m))
df["no_show"] = rng.binomial(1, p)

# ----------------------------------------------------------------------
# 7. Outcome: wait_time_min — lognormal; no-shows never waited (NaN)
# ----------------------------------------------------------------------
region_wt = df["region"].map(reg_wt_eff).to_numpy()
log_wait = (np.log(15.1)
            + 0.22 * df["is_peak_hour"]
            - 0.085 * (df["staff_on_shift"] - 6)
            + 0.10 * rural
            + 1.3 * region_wt + 1.1 * df["re_wait"].to_numpy()
            + rng.normal(0, 0.44, N_TOTAL))
df["wait_time_min"] = np.round(np.exp(log_wait)).clip(1, 240)
df.loc[df["no_show"] == 1, "wait_time_min"] = np.nan

df = df.drop(columns=["re_noshow", "re_wait"])
COLS = ["appointment_id", "region", "clinic_id", "clinic_type", "risk_band",
        "patient_age", "lead_time_days", "prior_no_shows", "sms_reminder",
        "ab_pilot", "rescheduled", "staff_on_shift", "is_peak_hour",
        "wait_time_min", "no_show"]
df = df[COLS]
df.to_csv(OUT / "clinic_visits.csv", index=False)

# ----------------------------------------------------------------------
# 8. ab_daily_log.csv — 21-day accrual of the randomized pilot
# ----------------------------------------------------------------------
pilot = df[df["ab_pilot"] == 1].copy()
pilot["trial_day"] = rng.integers(1, 22, len(pilot))
log = (pilot.groupby(["trial_day", "sms_reminder"])
       .agg(n=("no_show", "size"), no_shows=("no_show", "sum")).unstack())
ab_log = pd.DataFrame({
    "trial_day": log.index,
    "n_control":        log[("n", 0)].astype(int),
    "noshows_control":  log[("no_shows", 0)].astype(int),
    "n_reminder":       log[("n", 1)].astype(int),
    "noshows_reminder": log[("no_shows", 1)].astype(int),
}).reset_index(drop=True)
ab_log.to_csv(OUT / "ab_daily_log.csv", index=False)

# ----------------------------------------------------------------------
# 9. survey_responses.csv — opt-in SMS survey with non-response bias
#    47,500 SMS opt-in responses (satisfied patients over-respond,
#    mean ~4.6) + 500 stratified callbacks of non-responders (mean ~3.1).
# ----------------------------------------------------------------------
def scores(n, probs): return rng.choice([1, 2, 3, 4, 5], size=n, p=probs)
n_opt, n_cb = 47_500, 500
survey = pd.DataFrame({
    "survey_id": [f"SV{i:05d}" for i in range(1, n_opt + n_cb + 1)],
    "region": np.concatenate([rng.choice(region_en, n_opt, p=shares),
                              rng.choice(region_en, n_cb)]),
    "channel": ["sms_optin"] * n_opt + ["callback_nonresponder"] * n_cb,
    "satisfaction": np.concatenate([
        scores(n_opt, [0.008, 0.018, 0.055, 0.215, 0.704]),   # mean ~4.59
        scores(n_cb,  [0.115, 0.215, 0.285, 0.235, 0.150]),   # mean ~3.1
    ]),
})
survey.to_csv(OUT / "survey_responses.csv", index=False)

# ----------------------------------------------------------------------
# 10. clinic_reference.csv / region_reference.csv / small_pilot.csv
# ----------------------------------------------------------------------
emp = (df.groupby("clinic_id")
       .agg(n_appointments=("no_show", "size"),
            baseline_noshow_rate=("no_show", "mean")).round(3))
clin[["clinic_id", "region", "clinic_type", "avg_daily_slots"]] \
    .merge(emp, on="clinic_id", how="left") \
    .to_csv(OUT / "clinic_reference.csv", index=False)

pd.DataFrame({
    "region": region_en,
    "region_ar": [r[1] for r in REGIONS],
    "volume_share": shares.round(4),
    "n_rows_in_dataset": df["region"].value_counts().reindex(region_en).values,
    "n_clinics": clinic_counts,
}).to_csv(OUT / "region_reference.csv", index=False)

small_src = df[(df["clinic_type"] == "rural") & df["wait_time_min"].notna()]
small_src.sample(25, random_state=7)[
    ["appointment_id", "clinic_id", "sms_reminder", "wait_time_min", "no_show"]] \
    .to_csv(OUT / "small_pilot.csv", index=False)

print("Files written to", OUT)
print(df.shape, "| no-show:", round(df.no_show.mean(), 4),
      "| wait med/mean/sd:", df.wait_time_min.median(),
      round(df.wait_time_min.mean(), 1), round(df.wait_time_min.std(), 1))
