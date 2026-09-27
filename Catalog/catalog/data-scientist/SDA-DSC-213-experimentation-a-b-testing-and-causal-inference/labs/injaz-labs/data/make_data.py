"""
make_data.py — Injaz (إنجاز) synthetic dataset generator
SDA-DSC-213 · Experimentation, A/B Testing and Causal Inference · SDAIA Academy

Generates every dataset used by Labs 1-7 and the capstone, with GROUND TRUTH
PLANTED so instructors can verify that each method recovers a number that was
deliberately put there. Nothing here is real citizen data.

Run:    python make_data.py            (writes into ./ next to this file)
        python make_data.py --outdir /path/to/data

Reproducibility: every dataset is drawn from a named, seeded Generator, so a
re-run reproduces the files byte-for-byte on the same numpy version.

--------------------------------------------------------------------------
PLANTED GROUND TRUTH (the instructor's answer key)
--------------------------------------------------------------------------
  Guided uploader, randomised A/B      true lift  = +2.20 pp on completion
  Guided uploader, self-selected       true ATE   = +5.00 pp, naive ~ +19.3 pp
  Training programme (observational)   true ATT   = +6.00 pp
  Regional reminder rollout (DiD)      true ATT   = +3.00 pp
  Online filing (IV, distance)         true LATE  = +8.00 pp  (OLS biased ~ +14 pp)
  AI autofill, capstone A/B            true lift  = +1.40 pp  (deliberately close
                                       to the 1.0 pp ship threshold)
--------------------------------------------------------------------------
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------
# Constants — the Injaz world
# ----------------------------------------------------------------------------

MASTER_SEED = 20260213  # course code SDA-DSC-213

REGIONS = [
    "Riyadh", "Makkah", "Eastern Province", "Madinah", "Asir", "Tabuk",
    "Qassim", "Hail", "Jazan", "Najran", "Al Bahah", "Al Jouf",
    "Northern Borders",
]
# Rough population weights (illustrative, not official statistics).
REGION_WEIGHTS = np.array(
    [0.26, 0.25, 0.15, 0.07, 0.07, 0.03, 0.05, 0.02, 0.05, 0.02, 0.01, 0.01, 0.01]
)
REGION_WEIGHTS = REGION_WEIGHTS / REGION_WEIGHTS.sum()

SERVICES = [
    "license_renewal", "certificate_issue", "fee_payment",
    "address_update", "permit_request",
]
SERVICE_WEIGHTS = np.array([0.32, 0.22, 0.24, 0.12, 0.10])

DEVICES = ["android", "ios", "desktop"]
DEVICE_WEIGHTS = np.array([0.52, 0.34, 0.14])

# Planted truths
TRUE_ATE_UPLOADER_SIM = 0.050     # Module 1 simulator
TARGET_NAIVE_SELFSELECT = 0.193   # Module 1 documented naive estimate
TRUE_LIFT_UPLOADER_AB = 0.022     # Module 4 experiment
TRUE_ATT_TRAINING = 0.060         # Module 5 matching
TRUE_ATT_REMINDER = 0.030         # Module 5 DiD
TRUE_LATE_ONLINE_FILING = 0.080   # Module 5 IV
TRUE_LIFT_AUTOFILL = 0.014        # Capstone A/B

BASE_COMPLETION = 0.55            # platform baseline used throughout


def rng(name: str) -> np.random.Generator:
    """A named generator: independent per dataset, identical across runs.

    NOTE: this deliberately does NOT use Python's built-in hash(). String
    hashing is salted per interpreter process (PYTHONHASHSEED), so a seed
    derived from hash() silently produces different data on every run --
    which would make the course's central reproducibility claim false.
    blake2b is stable across processes, machines and Python versions.
    """
    digest = hashlib.blake2b(f"{MASTER_SEED}:{name}".encode(), digest_size=8).digest()
    return np.random.default_rng(int.from_bytes(digest, "big") % (2**32))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# ----------------------------------------------------------------------------
# Shared latent user population
# ----------------------------------------------------------------------------

def draw_users(n: int, name: str) -> pd.DataFrame:
    """The latent population every dataset is carved out of.

    digital_literacy is the master confounder: it drives who adopts a new
    feature AND who completes a service. It is *observable* in this course
    (as `digital_literacy_score`, a noisy proxy) so participants can adjust
    for it -- and the simulator can show what happens when they do not.
    """
    g = rng(name)

    region = g.choice(REGIONS, size=n, p=REGION_WEIGHTS)

    # KSA-like adult age distribution: young-skewed, 18-75
    age = np.clip(g.gamma(shape=3.6, scale=4.6, size=n) + 18, 18, 75).round().astype(int)

    urbanicity = np.where(
        np.isin(region, ["Riyadh", "Makkah", "Eastern Province"]), 0.12, -0.06
    )

    # Latent digital literacy in [0,1]: younger + urban => higher
    lit_lin = 1.15 - 0.030 * (age - 18) + urbanicity + g.normal(0, 0.42, n)
    digital_literacy = np.clip(sigmoid(lit_lin * 1.35), 0.02, 0.98)

    # Observable noisy proxy (this is what an analyst actually has)
    digital_literacy_score = np.clip(
        digital_literacy + g.normal(0, 0.07, n), 0.0, 1.0
    ).round(4)

    device_age_years = np.clip(
        6.5 - 5.0 * digital_literacy + g.normal(0, 1.1, n), 0.2, 11.0
    ).round(2)

    device = np.where(
        g.random(n) < 0.14, "desktop",
        np.where(g.random(n) < 0.40 + 0.25 * digital_literacy, "ios", "android"),
    )

    # Distance to nearest in-person service centre (km) -- the IV.
    # Depends on region remoteness only; independent of literacy by construction.
    remote = np.isin(region, ["Najran", "Al Jouf", "Northern Borders", "Al Bahah", "Hail"])
    distance_km = np.clip(
        g.lognormal(mean=np.where(remote, 3.35, 2.25), sigma=0.62, size=n), 0.4, 260.0
    ).round(2)

    prior_sessions = g.poisson(2.2 + 3.4 * digital_literacy, n)

    # --- the latent "completion propensity index" -------------------------
    # z is a standardised blend of digital literacy and a persistent, unmodelled
    # user effect (habit, motivation, service mix). It drives BOTH the
    # pre-period completion rate and the post-period outcome, which is what
    # makes prior_completion_rate a genuinely useful CUPED covariate.
    lit_std = (digital_literacy - digital_literacy.mean()) / digital_literacy.std()
    user_effect = g.normal(0, 1.0, n)
    z = 0.75 * lit_std + 0.66 * user_effect          # Var(z) ~= 1

    # Pre-period completion rate -- the CUPED covariate (corr with the
    # post-period binary outcome ~ 0.38 => ~14% variance reduction).
    prior_completion_rate = np.clip(
        BASE_COMPLETION + 0.20 * z + g.normal(0, 0.06, n), 0.0, 1.0
    ).round(4)

    signup_cohort = g.choice(
        ["2024H1", "2024H2", "2025H1", "2025H2", "2026H1"], size=n,
        p=[0.14, 0.18, 0.22, 0.24, 0.22],
    )

    return pd.DataFrame({
        "user_id": np.arange(1, n + 1),
        "region": region,
        "age": age,
        "device": device,
        "device_age_years": device_age_years,
        "distance_km": distance_km,
        "prior_sessions": prior_sessions,
        "prior_completion_rate": prior_completion_rate,
        "digital_literacy_score": digital_literacy_score,
        "signup_cohort": signup_cohort,
        "_latent_literacy": digital_literacy,   # dropped before writing
        "_user_effect": user_effect,            # dropped before writing
        "_z": z,                                # dropped before writing
    })


def baseline_p(df: pd.DataFrame) -> np.ndarray:
    """P(complete | no treatment). Mean ~= 0.55, sd ~= 0.20 across users.

    The spread is deliberate: a population where everyone completes at exactly
    0.55 makes CUPED and stratification look useless, which is not the lesson.
    """
    z = df["_z"].to_numpy()
    return np.clip(BASE_COMPLETION + 0.20 * z, 0.06, 0.96)


# ----------------------------------------------------------------------------
# 1. Module 1 -- potential outcomes / selection bias simulator
# ----------------------------------------------------------------------------

def make_potential_outcomes(outdir: Path) -> dict:
    """20,000 users with BOTH Y(0) and Y(1) recorded -- impossible in real life,
    which is exactly why the course starts here.

    Two calibrations run automatically so the printed numbers match the
    instructor package:
      * beta_lit  is bisected so the naive self-selected estimate lands on the
        documented +19.3pp while the planted ATE stays at +5.0pp;
      * the randomisation seed is searched so the randomised estimate lands
        within a fifth of a standard error of the truth -- otherwise a single
        unlucky draw undercuts the module's punchline in front of the class.
    """
    users = draw_users(20_000, "potential_outcomes")
    n = len(users)
    lit = users["_latent_literacy"].to_numpy()
    lit_c = lit - lit.mean()
    ue = users["_user_effect"].to_numpy()

    # Fixed, plausible self-selection: literacy raises the odds of opting in.
    K_SELECT = 8.0
    p_select = sigmoid(K_SELECT * lit_c)
    g_sel = np.random.default_rng(4242)
    t_self = (g_sel.random(n) < p_select).astype(int)

    u = np.random.default_rng(97531).random(n)   # coupled potential outcomes

    def build_with(u_vec, beta_lit: float):
        # Headroom matters: p0 is capped at 0.93 so that p0 + 0.05 never hits
        # the 0.99 ceiling. Without it the realised ATE lands near +4.8 pp
        # instead of the +5.0 pp that is supposed to have been planted, and
        # the whole module's punchline is a fifth of a point off.
        p0 = np.clip(BASE_COMPLETION + beta_lit * lit_c + 0.09 * ue, 0.03, 0.93)
        p1 = np.clip(p0 + TRUE_ATE_UPLOADER_SIM, 0.03, 0.98)
        return (u_vec < p0).astype(int), (u_vec < p1).astype(int)

    def build(beta_lit: float):
        return build_with(u, beta_lit)

    def naive_self(beta_lit: float) -> float:
        y0, y1 = build(beta_lit)
        y = np.where(t_self == 1, y1, y0)
        return y[t_self == 1].mean() - y[t_self == 0].mean()

    lo, hi = 0.05, 4.0
    for _ in range(70):
        mid = (lo + hi) / 2
        if naive_self(mid) < TARGET_NAIVE_SELFSELECT:
            lo = mid
        else:
            hi = mid
    beta_star = (lo + hi) / 2

    # The REALISED ATE is mean(1[p0 <= u < p1]); at n = 20,000 its sampling sd
    # is about 0.15 pp, so an arbitrary draw lands near +4.8 pp and the module
    # spends the morning explaining why "+5.0" is not +5.0. Pick the coupling
    # draw whose realised ATE is the planted one, then re-calibrate beta on it.
    best_u = None
    for seed in range(600):
        uu = np.random.default_rng(10_000 + seed).random(n)
        y0_, y1_ = build_with(uu, beta_star)
        d = abs((y1_ - y0_).mean() - TRUE_ATE_UPLOADER_SIM)
        if best_u is None or d < best_u[0]:
            best_u = (d, uu)
    u = best_u[1]

    lo, hi = 0.05, 4.0
    for _ in range(70):
        mid = (lo + hi) / 2
        if naive_self(mid) < TARGET_NAIVE_SELFSELECT:
            lo = mid
        else:
            hi = mid
    beta_star = (lo + hi) / 2
    y0, y1 = build(beta_star)

    # --- seed search for a representative randomised draw -----------------
    target = float((y1 - y0).mean())
    best = None
    for seed in range(500):
        gg = np.random.default_rng(seed)
        t = (gg.random(n) < 0.5).astype(int)
        y = np.where(t == 1, y1, y0)
        est = y[t == 1].mean() - y[t == 0].mean()
        smd_lit = abs(lit[t == 1].mean() - lit[t == 0].mean()) / lit.std()
        # want an accurate AND well-balanced draw: this is the "textbook" run
        score = abs(est - target) + 0.5 * smd_lit
        if best is None or score < best[0]:
            best = (score, seed, t, est)
    _, rand_seed, t_rand, est_rand = best

    df = users.drop(columns=["_latent_literacy", "_user_effect", "_z"]).copy()
    df["latent_literacy"] = lit.round(4)      # exposed ONLY in this teaching file
    df["y0"] = y0
    df["y1"] = y1
    df["tau_individual"] = y1 - y0
    df["treated_self_selected"] = t_self
    df["treated_randomised"] = t_rand
    df["y_observed_self_selected"] = np.where(t_self == 1, y1, y0)
    df["y_observed_randomised"] = np.where(t_rand == 1, y1, y0)
    df["p_select"] = p_select.round(4)

    df.to_parquet(outdir / "simulated_potential_outcomes.parquet", index=False)

    return {
        "true_ATE": round(target, 4),
        "naive_self_selected": round(float(naive_self(beta_star)), 4),
        "naive_randomised": round(float(est_rand), 4),
        "selection_bias_term": round(
            float(y0[t_self == 1].mean() - y0[t_self == 0].mean()), 4),
        "beta_literacy_calibrated": round(float(beta_star), 4),
        "randomisation_seed": int(rand_seed),
        "treated_share_self_selected": round(float(t_self.mean()), 4),
    }


# ----------------------------------------------------------------------------
# 2. Module 2 -- 200k user pool for assignment / SRM / balance
# ----------------------------------------------------------------------------

def make_user_pool(outdir: Path) -> dict:
    users = draw_users(200_000, "user_pool")
    g = rng("pool_extra")

    users["os_family"] = np.where(
        users["device"] == "desktop", "web",
        np.where(users["device"] == "ios", "ios", "android"),
    )
    users["is_eligible"] = (
        (users["prior_sessions"] >= 1) & (g.random(len(users)) < 0.92)
    ).astype(int)
    users["preferred_language"] = np.where(g.random(len(users)) < 0.86, "ar", "en")

    out = users.drop(columns=["_latent_literacy", "_user_effect", "_z"])
    out = out[[
        "user_id", "region", "age", "device", "os_family", "device_age_years",
        "distance_km", "prior_sessions", "prior_completion_rate",
        "digital_literacy_score", "signup_cohort", "preferred_language",
        "is_eligible",
    ]]
    out.to_csv(outdir / "injaz_users_pool.csv", index=False)
    return {"rows": int(len(out)), "eligible": int(out["is_eligible"].sum())}


# ----------------------------------------------------------------------------
# 3. Modules 1/5/6 -- the 20k analysis cohort (matching, IV, DAG)
# ----------------------------------------------------------------------------

def make_user_cohort(outdir: Path) -> dict:
    """Carries three observational stories:
       (a) enrolled_training  -> self-selected programme, true ATT = +6.0pp
       (b) online_filing      -> endogenous channel, true LATE = +8.0pp,
                                 instrumented by distance_km
       (c) support_calls      -> a MEDIATOR of the uploader effect (the
                                 'control that erases the effect' trap)
    """
    users = draw_users(20_000, "cohort")
    g = rng("cohort_outcomes")
    n = len(users)
    # IMPORTANT: this cohort is built so that ignorability HOLDS given the
    # covariates a participant can actually see. Enrolment and the outcome are
    # both driven by the OBSERVED digital_literacy_score, not by the latent
    # trait behind it. If the confounder were only visible through a noisy
    # proxy, matching would carry residual bias and the lab would teach
    # "matching does not work" instead of "matching works when its assumption
    # holds" -- which is the wrong lesson for Module 5. Unobserved confounding
    # is introduced deliberately and separately, in the instrumental-variables
    # story below.
    lit = users["digital_literacy_score"].to_numpy()
    lit_c = lit - lit.mean()
    ue = users["_user_effect"].to_numpy()
    z_obs = 0.75 * (lit_c / lit.std()) + 0.66 * ue

    # --- (a) digital-literacy training programme: strong self-selection
    p_enrol = sigmoid(-0.55 + 3.6 * lit_c + 0.45 * (users["prior_sessions"] > 3)
                      - 0.010 * (users["age"] - 40))
    enrolled = (g.random(n) < p_enrol).astype(int)

    # --- (b) online filing: chosen partly because the office is far away (the IV)
    log_dist_c = np.log(users["distance_km"].to_numpy()) - np.log(users["distance_km"]).mean()
    unobserved_motivation = g.normal(0, 1.0, n)      # confounds filing AND completion
    p_online = sigmoid(-0.30 + 1.05 * log_dist_c + 1.9 * lit_c
                       + 0.75 * unobserved_motivation)
    online_filing = (g.random(n) < p_online).astype(int)

    # --- outcome model ---------------------------------------------------
    # Deliberately centred low with a modest spread: a linear-probability DGP
    # whose components run into the 0/1 ceiling would ATTENUATE the planted
    # effects, and every estimator would then look biased when in fact the
    # data-generating process was.
    p0 = np.clip(0.40 + 0.11 * z_obs, 0.02, 0.98)
    p_complete = (
        p0
        + TRUE_ATT_TRAINING * enrolled
        + TRUE_LATE_ONLINE_FILING * online_filing
        + 0.040 * unobserved_motivation           # the unobserved confounder
    )
    p_complete = np.clip(p_complete, 0.01, 0.99)
    completed = (g.random(n) < p_complete).astype(int)

    # --- (c) support calls: caused by BOTH low literacy and by struggling.
    # It is downstream of service difficulty -> a mediator/collider trap.
    support_calls = g.poisson(
        np.clip(0.85 - 0.75 * lit + 0.55 * (1 - completed), 0.02, 4.0)
    )

    df = users.drop(columns=["_latent_literacy", "_user_effect", "_z"]).copy()
    df["log_distance_km"] = np.log(df["distance_km"]).round(4)
    df["enrolled_training"] = enrolled
    df["online_filing"] = online_filing
    df["support_calls"] = support_calls
    df["completed"] = completed

    df.to_csv(outdir / "injaz_users.csv", index=False)

    # Diagnostics for the answer key
    import statsmodels.api as sm
    # Use the SAME specification the labs use (instrument log_distance_km,
    # controls digital_literacy_score + age) so the answer key and the
    # notebooks report one number rather than two defensible ones.
    age_c = users["age"].to_numpy() - users["age"].mean()
    exog = np.column_stack([lit_c, age_c])
    X = sm.add_constant(np.column_stack([online_filing, exog]))
    ols = sm.OLS(completed, X).fit(cov_type="HC3")
    first = sm.OLS(online_filing,
                   sm.add_constant(np.column_stack([log_dist_c, exog]))
                   ).fit(cov_type="HC3")
    # 2SLS check for the answer key
    dhat = first.fittedvalues
    ss = sm.OLS(completed, sm.add_constant(np.column_stack([dhat, lit_c]))).fit()

    return {
        "rows": n,
        "true_ATT_training": TRUE_ATT_TRAINING,
        "naive_diff_training": float(
            completed[enrolled == 1].mean() - completed[enrolled == 0].mean()),
        "true_LATE_online_filing": TRUE_LATE_ONLINE_FILING,
        "ols_online_filing_biased": float(np.asarray(ols.params)[1]),
        "first_stage_F_log_distance": float(np.asarray(first.tvalues)[1] ** 2),
        "iv_2sls_recovered": float(np.asarray(ss.params)[1]),
        "enrolment_rate": float(enrolled.mean()),
        "online_filing_rate": float(online_filing.mean()),
        "completion_rate": float(completed.mean()),
    }


# ----------------------------------------------------------------------------
# 4. Modules 2/4 -- the guided-uploader randomised experiment
# ----------------------------------------------------------------------------

def _build_ab(name: str, n: int, true_lift: float, feature: str,
              trigger_rate: float, guardrail_effects: dict) -> pd.DataFrame:
    users = draw_users(n, name)
    g = rng(name + "_ab")
    p0 = baseline_p(users)

    triggered = (g.random(n) < trigger_rate).astype(int)
    u_out = g.random(n)

    # A single unlucky draw would make the planted effect unrecoverable and
    # teach the wrong lesson, so we search assignment seeds for a draw that is
    # both accurate (realised lift close to the planted lift) and balanced.
    best = None
    for seed in range(400):
        gg = np.random.default_rng(seed)
        tr = (gg.random(n) < 0.5).astype(int)
        exp_ = tr * triggered
        pp = np.clip(p0 + true_lift * exp_, 0.02, 0.98)
        cc = (u_out < pp).astype(int)
        m = triggered == 1
        est = cc[m & (tr == 1)].mean() - cc[m & (tr == 0)].mean()
        smd = abs(p0[tr == 1].mean() - p0[tr == 0].mean()) / p0.std()
        # Users who never reached the changed step CANNOT have been affected,
        # so their arm difference is a built-in A/A test. If chance leaves a
        # real gap there, the "analysing all assigned users dilutes the effect"
        # trap stops firing -- the diluted estimate accidentally matches the
        # true one and the lab teaches nothing. Require that stratum to be null.
        nm = ~m
        aa = abs(cc[nm & (tr == 1)].mean() - cc[nm & (tr == 0)].mean())
        score = (abs(est - true_lift) / max(true_lift, 1e-9)
                 + 2.0 * smd + 3.0 * aa / max(true_lift, 1e-9))
        if best is None or score < best[0]:
            best = (score, tr)
    treated = best[1]
    variant = np.where(treated == 1, "treatment", "control")
    exposed = treated * triggered
    p = np.clip(p0 + true_lift * exposed, 0.02, 0.98)
    completed = (u_out < p).astype(int)

    # --- guardrails -------------------------------------------------------
    lit = users["_latent_literacy"].to_numpy()
    support_contact = (g.random(n) < np.clip(
        0.062 - 0.030 * lit + guardrail_effects["support_contact"] * exposed, 0.001, 0.5)
    ).astype(int)

    duration = np.clip(
        g.lognormal(mean=5.15 - 0.30 * lit, sigma=0.52, size=n)
        * (1 + guardrail_effects["duration_pct"] * exposed),
        8, 3000,
    ).round(1)

    error_flag = (g.random(n) < np.clip(
        0.041 - 0.018 * lit + guardrail_effects["error_rate"] * exposed, 0.001, 0.5)
    ).astype(int)

    drop_off = ((completed == 0) & (g.random(n) < 0.72)).astype(int)

    df = users.drop(columns=["_latent_literacy", "_user_effect", "_z"]).copy()
    df["feature"] = feature
    df["variant"] = variant
    df["triggered"] = triggered
    df["exposed"] = exposed
    df["completed"] = completed
    df["support_contact"] = support_contact
    df["session_duration_sec"] = duration
    df["error_flag"] = error_flag
    df["drop_off"] = drop_off
    df["age_band"] = pd.cut(df["age"], [17, 29, 44, 59, 100],
                            labels=["18-29", "30-44", "45-59", "60+"]).astype(str)
    return df


def make_uploader_experiment(outdir: Path) -> dict:
    df = _build_ab(
        "uploader", 80_000, TRUE_LIFT_UPLOADER_AB, "guided_uploader",
        trigger_rate=0.62,
        guardrail_effects={"support_contact": -0.004, "duration_pct": 0.015,
                           "error_rate": 0.0006},
    )
    cols = ["user_id", "region", "age", "age_band", "device", "device_age_years",
            "prior_sessions", "prior_completion_rate", "digital_literacy_score",
            "signup_cohort", "feature", "variant", "triggered", "exposed",
            "completed", "support_contact", "session_duration_sec",
            "error_flag", "drop_off"]
    df[cols].to_csv(outdir / "injaz_experiment_results.csv", index=False)

    # --- a deliberately BROKEN copy for the SRM injector demo -------------
    g = rng("srm_break")
    keep = ~((df["variant"] == "treatment") & (g.random(len(df)) < 0.031))
    df.loc[keep, cols].to_csv(outdir / "injaz_experiment_results_srm_broken.csv",
                              index=False)

    trig = df[df["triggered"] == 1]
    obs = (trig.loc[trig.variant == "treatment", "completed"].mean()
           - trig.loc[trig.variant == "control", "completed"].mean())
    return {
        "rows": int(len(df)),
        "true_lift_on_exposed": TRUE_LIFT_UPLOADER_AB,
        "observed_lift_triggered": float(obs),
        "trigger_rate": float(df["triggered"].mean()),
        "allocation_treatment": float((df["variant"] == "treatment").mean()),
        "srm_broken_allocation": float((df.loc[keep, "variant"] == "treatment").mean()),
    }


def make_autofill_experiment(outdir: Path) -> dict:
    """The capstone experiment. Effect is REAL but sits close to the 1.0pp
    practical-significance threshold, so the honest verdict is nuanced."""
    df = _build_ab(
        "autofill", 70_000, TRUE_LIFT_AUTOFILL, "ai_autofill",
        trigger_rate=0.71,
        guardrail_effects={"support_contact": 0.0035, "duration_pct": -0.06,
                           "error_rate": 0.0011},
    )
    cols = ["user_id", "region", "age", "age_band", "device", "device_age_years",
            "prior_sessions", "prior_completion_rate", "digital_literacy_score",
            "signup_cohort", "feature", "variant", "triggered", "exposed",
            "completed", "support_contact", "session_duration_sec",
            "error_flag", "drop_off"]
    df[cols].to_csv(outdir / "injaz_autofill_ab.csv", index=False)

    trig = df[df["triggered"] == 1]
    obs = (trig.loc[trig.variant == "treatment", "completed"].mean()
           - trig.loc[trig.variant == "control", "completed"].mean())
    return {
        "rows": int(len(df)),
        "true_lift_on_exposed": TRUE_LIFT_AUTOFILL,
        "observed_lift_triggered": float(obs),
        "ship_threshold_pp": 1.0,
        "note": "CI is expected to straddle the 1.0pp threshold -> teach 'hold/extend'",
    }


# ----------------------------------------------------------------------------
# 5. Module 3 -- pre-period + traffic forecast
# ----------------------------------------------------------------------------

def make_pre_period(outdir: Path) -> dict:
    exp = pd.read_csv(outdir / "injaz_experiment_results.csv",
                      usecols=["user_id", "prior_completion_rate", "prior_sessions",
                               "digital_literacy_score", "completed"])
    g = rng("pre_period")
    sub = exp.sample(50_000, random_state=7).copy()
    sub["pre_sessions"] = sub["prior_sessions"]
    sub["pre_completion_rate"] = sub["prior_completion_rate"]
    sub["pre_avg_duration_sec"] = np.clip(
        g.lognormal(5.1 - 0.6 * sub["digital_literacy_score"], 0.45, len(sub)), 10, 2500
    ).round(1)
    out = sub[["user_id", "pre_sessions", "pre_completion_rate", "pre_avg_duration_sec"]]
    out.to_csv(outdir / "injaz_pre_period.csv", index=False)
    corr = float(np.corrcoef(sub["pre_completion_rate"], sub["completed"])[0, 1])
    return {"rows": int(len(out)), "corr_pre_vs_outcome": corr,
            "expected_cuped_variance_reduction_pct": round(100 * corr ** 2, 1)}


def make_traffic_forecast(outdir: Path) -> dict:
    g = rng("traffic")
    dates = pd.date_range("2026-10-01", periods=90, freq="D")
    dow = dates.dayofweek.to_numpy()          # Mon=0 ... Sun=6
    # KSA working week: Sun-Thu busy, Fri-Sat quiet
    weekday_mult = np.where(np.isin(dow, [4, 5]), 0.58, 1.0)
    trend = 1 + 0.0016 * np.arange(90)
    eligible = (14_200 * weekday_mult * trend * g.normal(1, 0.045, 90)).round().astype(int)
    trigger = np.clip(g.normal(0.62, 0.018, 90), 0.5, 0.75).round(4)
    df = pd.DataFrame({
        "date": dates.strftime("%Y-%m-%d"),
        "day_of_week": dates.day_name(),
        "eligible_users": eligible,
        "trigger_rate": trigger,
        "is_weekend": np.isin(dow, [4, 5]).astype(int),
    })
    df.to_csv(outdir / "injaz_traffic_forecast.csv", index=False)
    return {"rows": 90, "mean_daily_eligible": int(eligible.mean()),
            "mean_daily_triggered": int((eligible * trigger).mean())}


# ----------------------------------------------------------------------------
# 6. Modules 2/4 -- session-level data (unit of analysis / clustering)
# ----------------------------------------------------------------------------

def make_sessions(outdir: Path) -> dict:
    exp = pd.read_csv(outdir / "injaz_experiment_results.csv")
    g = rng("sessions")
    n_sess = g.poisson(np.clip(1.4 + 2.6 * exp["digital_literacy_score"], 0.5, 12)) + 1
    idx = np.repeat(exp.index.to_numpy(), n_sess)
    s = exp.loc[idx, ["user_id", "region", "device", "variant", "triggered",
                      "digital_literacy_score", "completed"]].reset_index(drop=True)
    m = len(s)
    s["session_id"] = np.arange(1, m + 1)
    s["service_type"] = g.choice(SERVICES, m, p=SERVICE_WEIGHTS)
    start = pd.Timestamp("2026-10-01") + pd.to_timedelta(
        g.integers(0, 90 * 24 * 60, m), unit="m")
    s["session_start"] = start.strftime("%Y-%m-%d %H:%M")
    # Session outcome is correlated WITHIN user -- that is the whole point.
    user_prop = np.clip(0.28 + 0.62 * s["completed"] + g.normal(0, 0.07, m), 0.02, 0.98)
    s["session_completed"] = (g.random(m) < user_prop).astype(int)
    # `triggered` = the session reached the document-upload step. It is a
    # property of the SESSION, not of the arm, so it occurs in both arms --
    # this is the column you filter on for a like-for-like comparison.
    # `exposed` = reached the step AND was in the treatment arm.
    reached = ((s["triggered"] == 1) & (g.random(m) < 0.8)).astype(int)
    s["triggered_uploader"] = reached
    s["exposed_uploader"] = (reached * (s["variant"] == "treatment")).astype(int)
    s["duration_sec"] = np.clip(
        g.lognormal(5.0 - 0.35 * s["digital_literacy_score"], 0.55, m), 5, 3600).round(1)
    out = s[["session_id", "user_id", "session_start", "region", "device",
             "service_type", "variant", "triggered_uploader", "exposed_uploader",
             "session_completed", "duration_sec"]]
    out.to_csv(outdir / "injaz_sessions.csv.gz", index=False,
               compression={"method": "gzip", "mtime": 0})
    return {"rows": int(m), "users": int(out.user_id.nunique()),
            "mean_sessions_per_user": round(m / out.user_id.nunique(), 2)}


# ----------------------------------------------------------------------------
# 7. Module 5 -- regional reminder rollout panel (DiD / event study)
# ----------------------------------------------------------------------------

def _panel(pretrend: bool, name: str) -> pd.DataFrame:
    g = rng(name)
    months = pd.date_range("2025-01-01", periods=24, freq="MS")
    # Staggered activation. 4 regions never treated (clean controls).
    activation = {
        "Riyadh": 10, "Makkah": 10, "Eastern Province": 13, "Qassim": 13,
        "Madinah": 16, "Asir": 16, "Tabuk": 19, "Hail": 19, "Jazan": 19,
        "Najran": None, "Al Bahah": None, "Al Jouf": None, "Northern Borders": None,
    }
    region_fe = {r: v for r, v in zip(REGIONS, g.normal(0, 0.045, len(REGIONS)))}
    rows = []
    for r in REGIONS:
        act = activation[r]
        treated_ever = int(act is not None)
        for t, m in enumerate(months, start=1):
            time_fe = 0.004 * t + 0.012 * np.sin(2 * np.pi * t / 12)
            post = int(act is not None and t >= act)
            eff = TRUE_ATT_REMINDER * post
            # ramp-in: effect reaches full size after 2 months
            if post and act is not None and t < act + 2:
                eff *= 0.6
            drift = 0.0
            if pretrend and treated_ever:
                drift = 0.0022 * (t - 12)      # violates parallel trends
            base = BASE_COMPLETION + region_fe[r] + time_fe + drift + eff
            n_users = int(g.normal(6000 * (REGION_WEIGHTS[REGIONS.index(r)] * 13), 260))
            n_users = max(n_users, 900)
            rate = float(np.clip(base + g.normal(0, 0.0055), 0.05, 0.95))
            rows.append({
                "region": r,
                "month": m.strftime("%Y-%m"),
                "period": t,
                "activation_month": act if act is not None else "",
                "treated_ever": treated_ever,
                "post": post,
                "treated_post": int(post),
                "months_since_activation": (t - act) if act is not None else "",
                "eligible_users": n_users,
                "reminders_sent": int(n_users * 0.86) if post else 0,
                "completion_rate": round(rate, 5),
                "completions": int(round(rate * n_users)),
            })
    return pd.DataFrame(rows)


def make_regions_panel(outdir: Path) -> dict:
    clean = _panel(False, "panel_clean")
    clean.to_csv(outdir / "injaz_regions_panel.csv", index=False)
    broken = _panel(True, "panel_pretrend")
    broken.to_csv(outdir / "injaz_regions_panel_pretrend.csv", index=False)

    import statsmodels.formula.api as smf
    fit = smf.ols("completion_rate ~ treated_post + C(region) + C(period)",
                  data=clean).fit()
    return {
        "rows": int(len(clean)),
        "regions": len(REGIONS),
        "months": 24,
        "never_treated_regions": 4,
        "true_ATT": TRUE_ATT_REMINDER,
        "twfe_estimate_clean": float(fit.params["treated_post"]),
        "pretrend_file": "injaz_regions_panel_pretrend.csv (parallel trends violated)",
    }


# ----------------------------------------------------------------------------
# 8. Module 6 -- collider simulator
# ----------------------------------------------------------------------------

def make_collider_sim(outdir: Path) -> dict:
    g = rng("collider")
    n = 50_000
    # Two INDEPENDENT causes
    literacy = np.clip(g.normal(0.55, 0.17, n), 0.02, 0.98)
    simplicity = np.clip(g.normal(0.50, 0.19, n), 0.02, 0.98)  # how easy the service is
    # A sharp collider: completion is close to a threshold on literacy+simplicity,
    # so conditioning on it induces a strong, obviously spurious negative link.
    p = sigmoid(7.0 * (literacy + simplicity - 1.06))
    completed = (g.random(n) < p).astype(int)   # the COLLIDER
    df = pd.DataFrame({
        "user_id": np.arange(1, n + 1),
        "digital_literacy": literacy.round(4),
        "service_simplicity": simplicity.round(4),
        "completed": completed,
    })
    df.to_parquet(outdir / "collider_sim.parquet", index=False)
    r_all = float(np.corrcoef(literacy, simplicity)[0, 1])
    m = completed == 1
    r_cond = float(np.corrcoef(literacy[m], simplicity[m])[0, 1])
    return {"rows": n, "corr_unconditional": round(r_all, 4),
            "corr_conditional_on_collider": round(r_cond, 4)}


# ----------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=str(Path(__file__).parent))
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    truth: dict = {}
    print("Generating Injaz datasets ...")
    truth["module1_potential_outcomes"] = make_potential_outcomes(outdir)
    print("  simulated_potential_outcomes.parquet")
    truth["module2_user_pool"] = make_user_pool(outdir)
    print("  injaz_users_pool.csv")
    truth["module5_user_cohort"] = make_user_cohort(outdir)
    print("  injaz_users.csv")
    truth["module4_uploader_experiment"] = make_uploader_experiment(outdir)
    print("  injaz_experiment_results.csv (+ srm_broken)")
    truth["capstone_autofill"] = make_autofill_experiment(outdir)
    print("  injaz_autofill_ab.csv")
    truth["module3_pre_period"] = make_pre_period(outdir)
    print("  injaz_pre_period.csv")
    truth["module3_traffic"] = make_traffic_forecast(outdir)
    print("  injaz_traffic_forecast.csv")
    truth["module2_sessions"] = make_sessions(outdir)
    print("  injaz_sessions.csv.gz")
    truth["module5_regions_panel"] = make_regions_panel(outdir)
    print("  injaz_regions_panel.csv (+ pretrend)")
    truth["module6_collider"] = make_collider_sim(outdir)
    print("  collider_sim.parquet")

    with open(outdir / "GROUND_TRUTH.json", "w") as f:
        json.dump(truth, f, indent=2)
    print("\nGROUND_TRUTH.json written. Key numbers:")
    print(json.dumps(truth, indent=2))


if __name__ == "__main__":
    main()
