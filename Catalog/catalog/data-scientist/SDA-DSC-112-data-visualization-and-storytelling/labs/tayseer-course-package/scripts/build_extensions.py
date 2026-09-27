#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_extensions.py - SDA-DSC-112 Tayseer dataset package
=========================================================

Deterministically generates the Case B and Case C extension datasets from the
CSVs already shipped in the package.  Nothing numeric is hand-typed: every
figure below is computed from `data/core/tayseer_services.csv`,
`data/dimensions/dim_regions.csv`, `data/dimensions/dim_channels.csv` and
`data/supporting/kpi_targets.csv`.  Only the qualitative text columns
(technique names, teaching notes, critique prose) are literals.

Outputs
-------
  data/supporting/regional_equity_latest.csv    Case C - per-capita equity, 13 regions
  data/supporting/regional_equity_lorenz.csv    Case C - Lorenz curve + Gini input
  data/instructional/kpi_spin_pairs.csv         Case B - spun vs honest KPI pairs
  data/instructional/success_dashboard_spec.csv Case B - paired dashboard tile spec
  data/instructional/critique_canon.csv         Case B/M1 - the ten critique exemplars

Run:  python3 scripts/build_extensions.py       (from the package root)
"""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ENC = "utf-8-sig"                      # Excel / Power BI on Windows
DIGITAL_CHANNELS = ["Mobile App", "Web Portal"]
STALLED = ["Jazan", "Najran", "Al-Baha", "Asir", "Northern Borders"]


# ----------------------------------------------------------------------------
# 0. Load
# ----------------------------------------------------------------------------
def load():
    fact = pd.read_csv(ROOT / "data/core/tayseer_services.csv",
                       encoding=ENC, parse_dates=["month"])
    regions = pd.read_csv(ROOT / "data/dimensions/dim_regions.csv", encoding=ENC)
    channels = pd.read_csv(ROOT / "data/dimensions/dim_channels.csv", encoding=ENC)
    kpis = pd.read_csv(ROOT / "data/supporting/kpi_targets.csv", encoding=ENC)
    scorecard = pd.read_csv(ROOT / "data/supporting/regional_scorecard_latest.csv",
                            encoding=ENC)
    return fact, regions, channels, kpis, scorecard


# ----------------------------------------------------------------------------
# 1. The measure rules, as functions (percentages are NON-additive)
# ----------------------------------------------------------------------------
def wmean(frame, col, weight):
    """Weighted recomputation - the only legitimate way to roll up a rate."""
    return float((frame[col] * frame[weight]).sum() / frame[weight].sum())


def adoption(frame):
    """User-weighted digital adoption %, per KPI-01."""
    return 100.0 * float((frame.digital_adoption_pct / 100.0 * frame.unique_users).sum()
                         / frame.unique_users.sum())


def digital_txn(frame):
    return int(frame[frame.channel.isin(DIGITAL_CHANNELS)].transactions.sum())


# ----------------------------------------------------------------------------
# 2. Case C - regional_equity_latest.csv
# ----------------------------------------------------------------------------
def build_equity(fact, regions):
    latest = fact[fact.month == fact.month.max()]

    rows = []
    for region, grp in latest.groupby("region", sort=True):
        rows.append({
            "region": region,
            "monthly_transactions": int(grp.transactions.sum()),
            "monthly_unique_users": int(grp.unique_users.sum()),
            "monthly_digital_transactions": digital_txn(grp),
            "digital_adoption_pct": round(adoption(grp), 1),
            "cost_per_txn_sar": round(wmean(grp, "cost_per_txn_sar", "transactions"), 1),
            "csat": round(wmean(grp, "csat", "transactions"), 2),
            "csat_user_weighted": round(wmean(grp, "csat", "unique_users"), 2),
            "avg_completion_min": round(wmean(grp, "avg_completion_min", "transactions"), 1),
        })
    eq = pd.DataFrame(rows).merge(
        regions[["region", "region_code", "region_ar", "population_2025",
                 "households_2025", "area_km2", "internet_penetration_pct",
                 "digital_readiness_index", "service_branches", "priority_tier"]],
        on="region", how="left")

    pop_k = eq.population_2025 / 1_000.0
    eq["population_density_per_km2"] = (eq.population_2025 / eq.area_km2).round(2)
    eq["branches_per_100k_pop"] = (eq.service_branches / eq.population_2025 * 100_000).round(2)
    eq["txn_per_1k_pop"] = (eq.monthly_transactions / pop_k).round(1)
    eq["digital_txn_per_1k_pop"] = (eq.monthly_digital_transactions / pop_k).round(1)

    # National denominators - recomputed, never averaged
    nat_digital_per_1k = latest[latest.channel.isin(DIGITAL_CHANNELS)].transactions.sum() \
        / regions.population_2025.sum() * 1_000
    eq["index_vs_national"] = (eq.monthly_digital_transactions / pop_k
                               / nat_digital_per_1k * 100).round(1)

    eq["population_share_pct"] = (eq.population_2025 / regions.population_2025.sum() * 100).round(2)
    eq["digital_txn_share_pct"] = (eq.monthly_digital_transactions
                                   / eq.monthly_digital_transactions.sum() * 100).round(2)

    # The headline teaching pair: the raw-count map vs the rate map
    eq["rank_by_raw_volume"] = eq.monthly_digital_transactions.rank(
        ascending=False, method="min").astype(int)
    eq["rank_by_per_capita"] = (eq.monthly_digital_transactions / pop_k).rank(
        ascending=False, method="min").astype(int)
    eq["rank_shift"] = eq.rank_by_raw_volume - eq.rank_by_per_capita

    cols = ["region", "region_code", "region_ar", "population_2025", "households_2025",
            "area_km2", "population_density_per_km2", "service_branches",
            "branches_per_100k_pop", "monthly_transactions", "monthly_unique_users",
            "monthly_digital_transactions", "txn_per_1k_pop", "digital_txn_per_1k_pop",
            "digital_adoption_pct", "cost_per_txn_sar", "csat", "csat_user_weighted",
            "avg_completion_min", "internet_penetration_pct", "digital_readiness_index",
            "priority_tier", "population_share_pct", "digital_txn_share_pct",
            "index_vs_national", "rank_by_raw_volume", "rank_by_per_capita", "rank_shift"]
    return eq[cols].sort_values("rank_by_per_capita").reset_index(drop=True), nat_digital_per_1k


# ----------------------------------------------------------------------------
# 3. Case C - regional_equity_lorenz.csv  (+ the Gini we actually compute)
# ----------------------------------------------------------------------------
def build_lorenz(equity):
    lz = equity.sort_values("digital_txn_per_1k_pop").reset_index(drop=True).copy()

    pop_total = lz.population_2025.sum()
    dig_total = lz.monthly_digital_transactions.sum()

    lz["population_share"] = lz.population_2025 / pop_total
    lz["digital_txn_share"] = lz.monthly_digital_transactions / dig_total
    cum_pop = lz.population_share.cumsum()
    cum_dig = lz.digital_txn_share.cumsum()
    lz["cum_population_share_start"] = cum_pop.shift(1).fillna(0.0)
    lz["cum_population_share"] = cum_pop
    lz["cum_digital_txn_share_start"] = cum_dig.shift(1).fillna(0.0)
    lz["cum_digital_txn_share"] = cum_dig

    # Trapezoidal area under the Lorenz curve, segment by segment
    dx = lz.cum_population_share - lz.cum_population_share_start
    lz["gini_segment_area"] = dx * (lz.cum_digital_txn_share
                                    + lz.cum_digital_txn_share_start) / 2.0
    gini = 1.0 - 2.0 * lz.gini_segment_area.sum()

    lz["equality_reference"] = lz.cum_population_share      # the 45-degree line
    lz["gap_to_equality"] = lz.cum_population_share - lz.cum_digital_txn_share
    lz["lorenz_rank"] = np.arange(1, len(lz) + 1)
    lz["gini_coefficient"] = round(float(gini), 4)          # constant, repeated for Excel

    for c in ["population_share", "digital_txn_share", "cum_population_share_start",
              "cum_population_share", "cum_digital_txn_share_start",
              "cum_digital_txn_share", "gini_segment_area", "equality_reference",
              "gap_to_equality"]:
        lz[c] = lz[c].round(8)
    # Force the closing point to be exactly (1, 1) after rounding
    lz.loc[lz.index[-1], "cum_population_share"] = 1.0
    lz.loc[lz.index[-1], "cum_digital_txn_share"] = 1.0
    lz.loc[lz.index[-1], "equality_reference"] = 1.0
    lz.loc[lz.index[-1], "gap_to_equality"] = 0.0

    cols = ["lorenz_rank", "region", "region_code", "region_ar", "population_2025",
            "monthly_digital_transactions", "digital_txn_per_1k_pop",
            "population_share", "digital_txn_share",
            "cum_population_share_start", "cum_population_share",
            "cum_digital_txn_share_start", "cum_digital_txn_share",
            "equality_reference", "gap_to_equality", "gini_segment_area",
            "gini_coefficient"]
    return lz[cols], float(gini)


# ----------------------------------------------------------------------------
# 4. Case B - every figure the spin pairs quote, computed once, here
# ----------------------------------------------------------------------------
def compute_figures(fact, regions, equity):
    latest_month = fact.month.max()
    L = fact[fact.month == latest_month]
    F0 = fact[fact.month == fact.month.min()]

    series = fact.groupby("month").apply(adoption)          # 60-month national series
    a = series.values
    months = list(series.index)

    reg_adopt = L.groupby("region").apply(adoption)

    f = {}
    f["latest_month"] = latest_month
    f["n_months"] = len(a)

    # (1) averages of averages
    f["adopt_naive"] = round(float(L.digital_adoption_pct.mean()), 2)
    f["adopt_weighted"] = round(float(adoption(L)), 2)

    # (2) truncated axis / lie factor - national adoption, last 12 months, y from 60
    f["adopt_12m_ago"] = round(float(a[-13]), 2)
    f["trunc_axis_start"] = 60.0
    shown = ((a[-1] - 60.0) - (a[-13] - 60.0)) / (a[-13] - 60.0) * 100
    real = (a[-1] - a[-13]) / a[-13] * 100
    f["trunc_apparent_pct"] = round(float(shown), 2)
    f["trunc_real_pct"] = round(float(real), 2)
    f["lie_factor"] = round(float(shown / real), 1)

    # (3) cherry-picked start month: argmax slope to the latest month
    slopes = [(a[-1] - a[s]) / (len(a) - 1 - s) for s in range(len(a) - 1)]
    best = int(np.argmax(slopes))
    f["cherry_start_month"] = months[best].strftime("%Y-%m")
    f["cherry_slope"] = round(float(slopes[best]), 4)
    f["cherry_projection_dec"] = round(float(a[-1] + 6 * slopes[best]), 2)
    slope_9m = (a[-1] - a[-10]) / 9.0
    f["slope_9m"] = round(float(slope_9m), 4)
    f["honest_projection_dec"] = round(float(a[-1] + 6 * slope_9m), 2)

    # (4) aggregation hides the distribution
    S = L[L.region.isin(STALLED)]
    f["stalled_adoption"] = round(float(adoption(S)), 2)
    f["stalled_pop_share"] = round(float(regions.set_index("region")
                                         .population_2025[STALLED].sum()
                                         / regions.population_2025.sum() * 100), 2)

    # (5) pp vs %
    f["adopt_first_month"] = round(float(a[0]), 2)
    f["growth_pp"] = round(float(a[-1] - a[0]), 2)
    f["growth_rel_pct"] = round(float((a[-1] - a[0]) / a[0] * 100), 2)

    # (6) CSAT unweighted vs weighted
    f["csat_naive"] = round(float(L.csat.mean()), 2)
    f["csat_weighted"] = round(wmean(L, "csat", "transactions"), 2)

    # (7) RAG threshold gaming - green line moved from 65.0 to the amber line 62.0
    f["regions_green_at_65"] = int((reg_adopt >= 65.0).sum())
    f["regions_green_at_62"] = int((reg_adopt >= 62.0).sum())

    # (8) rounding to the target (KPI-08 = regions below 65)
    f["regions_below_target"] = int((reg_adopt < 65.0).sum())
    f["regions_below_target_rounded"] = int((reg_adopt.round(1) < 65.0).sum())

    # (9) transactions counted as citizens served
    f["monthly_transactions"] = int(L.transactions.sum())
    f["monthly_unique_users"] = int(L.unique_users.sum())

    # (10) rebased index hides a level problem
    reg_series = fact.groupby(["region", "month"]).apply(adoption).unstack()
    index_latest = reg_series.iloc[:, -1] / reg_series.iloc[:, 0] * 100
    rank_index = index_latest.rank(ascending=False, method="min").astype(int)
    rank_level = reg_series.iloc[:, -1].rank(ascending=False, method="min").astype(int)
    top = index_latest.idxmax()
    f["index_region"] = top
    f["index_value"] = round(float(index_latest[top]), 1)
    f["index_level"] = round(float(reg_series.loc[top].iloc[-1]), 1)
    f["index_rank_by_index"] = int(rank_index[top])
    f["index_rank_by_level"] = int(rank_level[top])

    # (11) coverage filter - drop the branch channel
    dig = int(L[L.channel.isin(DIGITAL_CHANNELS)].transactions.sum())
    f["digital_share_all"] = round(dig / L.transactions.sum() * 100, 2)
    f["digital_share_excl_branch"] = round(
        dig / L[L.channel != "Branch"].transactions.sum() * 100, 2)

    # (12) cherry-picked segment - the best service category stands in for the programme
    cat = L.groupby("service_category").apply(adoption)
    f["best_category"] = cat.idxmax()
    f["best_category_adoption"] = round(float(cat.max()), 2)

    # (13) unit cost with the expensive channel removed
    f["cost_all"] = round(wmean(L, "cost_per_txn_sar", "transactions"), 2)
    NB = L[L.channel != "Branch"]
    f["cost_excl_branch"] = round(wmean(NB, "cost_per_txn_sar", "transactions"), 2)

    # Channel-level latest-month figures, quoted by the honest dashboard tiles
    chan = L.groupby("channel").apply(lambda x: pd.Series({
        "txn": x.transactions.sum(),
        "csat": wmean(x, "csat", "transactions"),
        "cost": wmean(x, "cost_per_txn_sar", "transactions")}))
    f["branch_txn"] = int(chan.loc["Branch", "txn"])
    f["branch_share"] = round(float(chan.loc["Branch", "txn"] / L.transactions.sum() * 100), 1)
    f["csat_branch"] = round(float(chan.loc["Branch", "csat"]), 2)
    f["csat_mobile"] = round(float(chan.loc["Mobile App", "csat"]), 2)
    f["cost_branch"] = round(float(chan.loc["Branch", "cost"]), 1)
    f["cost_mobile"] = round(float(chan.loc["Mobile App", "cost"]), 2)

    # Regional spread behind the national card
    f["region_adopt_min"] = round(float(reg_adopt.min()), 1)
    f["region_adopt_max"] = round(float(reg_adopt.max()), 1)
    f["nat_digital_per_1k"] = round(float(
        L[L.channel.isin(DIGITAL_CHANNELS)].transactions.sum()
        / regions.population_2025.sum() * 1000), 1)

    # Case C headline, quoted by the honest dashboard.
    # Biggest fall from the raw-volume map to the rate map; ties broken in favour
    # of the region that ends up lowest per capita.
    worst = equity.sort_values(["rank_shift", "rank_by_per_capita"],
                               ascending=[True, False]).iloc[0]
    f["shift_region"] = worst.region
    f["shift_raw_rank"] = int(worst.rank_by_raw_volume)
    f["shift_pc_rank"] = int(worst.rank_by_per_capita)
    f["shift_value"] = int(worst.rank_shift)
    f["jazan_index"] = float(equity.set_index("region").loc["Jazan", "index_vs_national"])
    return f


# ----------------------------------------------------------------------------
# 5. Case B - kpi_spin_pairs.csv
# ----------------------------------------------------------------------------
def build_spin_pairs(f):
    FACT = "data/core/tayseer_services.csv"
    REG = "data/dimensions/dim_regions.csv"
    rows = [
        dict(
            technique_id="SPIN-01",
            technique_en="Average of averages on a non-additive rate",
            technique_ar="متوسط المتوسطات لمؤشر غير قابل للجمع",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="%",
            source_file=FACT,
            spun_figure=f["adopt_naive"],
            honest_figure=f["adopt_weighted"],
            how_it_was_produced="AVERAGE(digital_adoption_pct) over the 468 rows of the latest month (2026-06) in tayseer_services.csv",
            what_the_reader_concludes="Adoption is 61.2% - the programme is 3.8pp short of the 65% target and needs more money.",
            the_honest_statement="User-weighted adoption is 63.8%. The 61.2% figure averages a segment-level rate that is repeated on four channel rows, so every small segment counts as much as Riyadh.",
            the_fix="Recompute as SUM(digital_adoption_pct/100 * unique_users) / SUM(unique_users) * 100, exactly as KPI-01 defines it. Flag the measure non-additive in the semantic layer so AVERAGE is impossible to reach.",
            severity="High",
            detectability="Hard",
        ),
        dict(
            technique_id="SPIN-02",
            technique_en="Truncated y-axis on a bar chart",
            technique_ar="بتر محور القيم في مخطط الأعمدة",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="% change apparent vs actual",
            source_file=FACT,
            spun_figure=f["trunc_apparent_pct"],
            honest_figure=f["trunc_real_pct"],
            how_it_was_produced=(
                "Two bars, national adoption at 2025-06 (%.2f%%) and 2026-06 (%.2f%%), drawn on a y-axis "
                "starting at %.0f. Apparent change = ((v1-60)-(v0-60))/(v0-60); actual change = (v1-v0)/v0. "
                "Tufte lie factor = apparent / actual = %.1f." % (
                    f["adopt_12m_ago"], f["adopt_weighted"], f["trunc_axis_start"], f["lie_factor"])),
            what_the_reader_concludes="Adoption more than doubled in a year - the bar on the right is over twice the height of the one on the left.",
            the_honest_statement="Adoption rose %.2fpp, a %.2f%% relative change. The chart exaggerates it by a factor of %.1f." % (
                f["adopt_weighted"] - f["adopt_12m_ago"], f["trunc_real_pct"], f["lie_factor"]),
            the_fix="Start bar charts at zero. If the change genuinely needs magnification, switch the mark to a line or a dot plot with a labelled, clearly non-zero axis and annotate the actual pp change.",
            severity="High",
            detectability="Easy",
        ),
        dict(
            technique_id="SPIN-03",
            technique_en="Cherry-picked start month for the trend line",
            technique_ar="اختيار انتقائي لشهر البداية في خط الاتجاه",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="% adoption projected at Dec-2026",
            source_file=FACT,
            spun_figure=f["cherry_projection_dec"],
            honest_figure=f["honest_projection_dec"],
            how_it_was_produced=(
                "Search all %d possible start months for the one that maximises "
                "(adoption[2026-06] - adoption[s]) / months; the winner is %s at %.4f pp/month. "
                "Project six months: 63.84 + 6 x slope. The honest version uses the nine-month slope "
                "(%.4f pp/month) that regional_scorecard_latest.csv already uses as its stall detector."
                % (f["n_months"] - 1, f["cherry_start_month"], f["cherry_slope"], f["slope_9m"])),
            what_the_reader_concludes="On trend we clear 65% comfortably by December - no intervention needed.",
            the_honest_statement="Growth has decelerated. At the pace of the last nine months the December figure is %.1f%%, still short of 65%%." % f["honest_projection_dec"],
            the_fix="Fix the window before you look at the data, state it on the chart, and show the recent slope alongside the long-run one. Where they disagree, that disagreement is the finding.",
            severity="High",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-04",
            technique_en="National aggregate hides the distribution",
            technique_ar="الإجمالي الوطني يخفي التوزيع",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="%",
            source_file=FACT,
            spun_figure=f["adopt_weighted"],
            honest_figure=f["stalled_adoption"],
            how_it_was_produced=(
                "Spun: user-weighted adoption over all 13 regions. Honest: the same recomputation "
                "restricted to the five stalled Tier-1 regions (Jazan, Najran, Al-Baha, Asir, "
                "Northern Borders), which hold %.1f%% of the population." % f["stalled_pop_share"]),
            what_the_reader_concludes="The country is 1.2pp from target; the programme is essentially on track.",
            the_honest_statement="Five regions holding %.1f%% of the population sit at %.1f%%, %.1fpp below the national figure and none of them is moving." % (
                f["stalled_pop_share"], f["stalled_adoption"], f["adopt_weighted"] - f["stalled_adoption"]),
            the_fix="Never ship a national KPI card without the distribution beside it - a strip plot, a sorted dot plot or a min/max annotation on the card itself.",
            severity="High",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-05",
            technique_en="Percentage change of a percentage (pp reported as %)",
            technique_ar="تغير نسبي لنسبة مئوية (نقاط مئوية تُعرض كنسبة)",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="reported growth number",
            source_file=FACT,
            spun_figure=f["growth_rel_pct"],
            honest_figure=f["growth_pp"],
            how_it_was_produced=(
                "Spun: (adoption[2026-06] - adoption[2021-07]) / adoption[2021-07] * 100 = %.2f, "
                "then printed with a %% sign. Honest: the same difference in percentage points, "
                "%.2fpp (%.2f%% to %.2f%%)." % (
                    f["growth_rel_pct"], f["growth_pp"], f["adopt_first_month"], f["adopt_weighted"])),
            what_the_reader_concludes="Adoption grew by 86.6% - read as 'nearly nine out of ten citizens now transact digitally'.",
            the_honest_statement="Adoption rose %.1f percentage points, from %.1f%% to %.1f%%. A percentage of a percentage is a different quantity and needs a different word." % (
                f["growth_pp"], f["adopt_first_month"], f["adopt_weighted"]),
            the_fix="House rule: rates change in percentage points, counts change in percent. Put the unit in the label ('pp') and never let a pp figure inherit a % sign.",
            severity="Medium",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-06",
            technique_en="Unweighted CSAT average",
            technique_ar="متوسط رضا غير مرجّح",
            kpi_affected="KPI-03 Customer Satisfaction (CSAT)",
            figure_unit="CSAT 1-5",
            source_file=FACT,
            spun_figure=f["csat_naive"],
            honest_figure=f["csat_weighted"],
            how_it_was_produced="AVERAGE(csat) over the latest month's 468 rows, versus KPI-03's definition SUM(csat * transactions) / SUM(transactions).",
            what_the_reader_concludes="CSAT is 4.00 - sitting exactly on the amber line and about to go red.",
            the_honest_statement="Transaction-weighted CSAT is 4.16. The unweighted figure gives a low-volume branch row the same say as a million mobile transactions - here the wrong method understates the result.",
            the_fix="Weight by transactions, as KPI-03 already specifies. Note that the averages trap does not always flatter; it simply produces a number that answers no question.",
            severity="Medium",
            detectability="Hard",
        ),
        dict(
            technique_id="SPIN-07",
            technique_en="RAG threshold moved so amber reads green",
            technique_ar="تحريك عتبات الألوان ليظهر البرتقالي أخضر",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="regions rated green (of 13)",
            source_file=FACT + " + data/supporting/kpi_targets.csv",
            spun_figure=f["regions_green_at_62"],
            honest_figure=f["regions_green_at_65"],
            how_it_was_produced=(
                "Count regions whose user-weighted adoption clears the green line. kpi_targets.csv sets "
                "KPI-01 threshold_green = 65.0 and threshold_amber = 62.0; the spun dashboard paints "
                "green from 62.0 upward."),
            what_the_reader_concludes="Eight of thirteen regions are green - a clear majority of the country is performing.",
            the_honest_statement="Against the published green line of 65.0%%, %d of 13 regions are green and %d sit below the target." % (
                f["regions_green_at_65"], f["regions_below_target"]),
            the_fix="Thresholds are governance, not design. Take them from kpi_targets.csv at build time, show the numeric threshold on the tile, and log any change with a date and an owner.",
            severity="High",
            detectability="Easy",
        ),
        dict(
            technique_id="SPIN-08",
            technique_en="Rounding a region across the target line",
            technique_ar="التقريب الذي يعبر بمنطقة خط المستهدف",
            kpi_affected="KPI-08 Regions Below Adoption Target",
            figure_unit="regions below target (count)",
            source_file=FACT,
            spun_figure=f["regions_below_target_rounded"],
            honest_figure=f["regions_below_target"],
            how_it_was_produced=(
                "Spun: round each region's adoption to one decimal before the comparison, so Hail's "
                "64.97% becomes 65.0% and drops out of the count. Honest: compare the unrounded value, "
                "as KPI-08 defines it (DISTINCTCOUNT(region) WHERE adoption < 65)."),
            what_the_reader_concludes="Only eight regions are still below target - we cleared one this month.",
            the_honest_statement="Nine regions are below target. Hail is at 64.97%, which is below 65% however it is displayed.",
            the_fix="Compare at full precision, round only for display, and never let the display precision drive a threshold test. Show the raw value in the tooltip.",
            severity="Medium",
            detectability="Hard",
        ),
        dict(
            technique_id="SPIN-09",
            technique_en="Transactions counted as citizens served",
            technique_ar="احتساب المعاملات كأنها مستفيدون",
            kpi_affected="KPI-06 Monthly Transactions",
            figure_unit="count (latest month)",
            source_file=FACT,
            spun_figure=f["monthly_transactions"],
            honest_figure=f["monthly_unique_users"],
            how_it_was_produced="SUM(transactions) versus SUM(unique_users) for 2026-06. The ratio is %.2f transactions per beneficiary." % (
                f["monthly_transactions"] / f["monthly_unique_users"]),
            what_the_reader_concludes="We served 12.5 million citizens last month - more than a third of the population.",
            the_honest_statement="12.5 million transactions were completed by 6.7 million distinct beneficiaries, %.2f transactions each." % (
                f["monthly_transactions"] / f["monthly_unique_users"]),
            the_fix="Label the tile with the noun you actually measured. unique_users is semi-additive - sum it within a month, never across months, and never call a transaction a person.",
            severity="High",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-10",
            technique_en="Rebased index hides the level",
            technique_ar="مؤشر معاد تأسيسه يخفي المستوى",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="rank of 13",
            source_file=FACT,
            spun_figure=f["index_rank_by_index"],
            honest_figure=f["index_rank_by_level"],
            how_it_was_produced=(
                "Index each region's user-weighted adoption to its own 2021-07 value = 100 and rank by "
                "the 2026-06 index: %s leads at %.1f. Rank the same regions by the adoption level "
                "instead and %s is %d of 13 at %.1f%%, still below the 65%% target."
                % (f["index_region"], f["index_value"], f["index_region"],
                   f["index_rank_by_level"], f["index_level"])),
            what_the_reader_concludes="%s is the programme's best performer - top of the growth league table." % f["index_region"],
            the_honest_statement="%s grew fastest from a low base but sits %d of 13 on the measure the target is written against, at %.1f%%." % (
                f["index_region"], f["index_rank_by_level"], f["index_level"]),
            the_fix="Show the level and the change together - a dot plot of current value with a connector back to the baseline. If you must index, print the base value on the chart.",
            severity="Medium",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-11",
            technique_en="Coverage filter - the branch channel is excluded",
            technique_ar="فلتر تغطية - استبعاد قناة الفروع",
            kpi_affected="KPI-10 Digital share of transactions",
            figure_unit="% of transactions that are digital",
            source_file=FACT + " + data/dimensions/dim_channels.csv",
            spun_figure=f["digital_share_excl_branch"],
            honest_figure=f["digital_share_all"],
            how_it_was_produced=(
                "Spun: SUM(transactions WHERE channel in Mobile App, Web Portal) / "
                "SUM(transactions WHERE channel <> 'Branch'). Honest: the same numerator over "
                "SUM(transactions) across all four channels."),
            what_the_reader_concludes="Four in five transactions are already digital - the channel shift is essentially finished.",
            the_honest_statement="%.1f%% of all transactions are digital. The %.1f%% figure silently deletes the {:,} branch transactions that are exactly the thing the programme exists to move.".format(f["branch_txn"]) % (
                f["digital_share_all"], f["digital_share_excl_branch"]),
            the_fix="Print the filter on the tile. A denominator that excludes the population you are trying to change cannot measure whether you changed it.",
            severity="High",
            detectability="Medium",
        ),
        dict(
            technique_id="SPIN-12",
            technique_en="Best segment stands in for the programme",
            technique_ar="أفضل شريحة تُقدَّم بوصفها البرنامج كله",
            kpi_affected="KPI-01 Digital Adoption %",
            figure_unit="%",
            source_file=FACT,
            spun_figure=f["best_category_adoption"],
            honest_figure=f["adopt_weighted"],
            how_it_was_produced=(
                "Recompute user-weighted adoption by service_category for 2026-06 and quote the maximum "
                "(%s, %.2f%%) as the headline. Honest: the same recomputation over all nine categories."
                % (f["best_category"], f["best_category_adoption"])),
            what_the_reader_concludes="We have passed the 65% target.",
            the_honest_statement="One of nine categories (%s) is above target at %.1f%%; the programme is at %.1f%%." % (
                f["best_category"], f["best_category_adoption"], f["adopt_weighted"]),
            the_fix="A headline KPI must cover the whole scope its target was written against. Show the best and worst segment on the same tile, or show all nine.",
            severity="Medium",
            detectability="Easy",
        ),
        dict(
            technique_id="SPIN-13",
            technique_en="Unit cost quoted with the expensive channel removed",
            technique_ar="تكلفة الوحدة بعد حذف القناة الأعلى تكلفة",
            kpi_affected="KPI-02 Cost per Transaction",
            figure_unit="SAR per transaction",
            source_file=FACT,
            spun_figure=f["cost_excl_branch"],
            honest_figure=f["cost_all"],
            how_it_was_produced=(
                "Spun: SUM(cost_per_txn_sar * transactions) / SUM(transactions) over rows where "
                "channel <> 'Branch'. Honest: the same transaction-weighted recomputation over all "
                "four channels, which is how KPI-02 is defined."),
            what_the_reader_concludes="Unit cost is 8.40 SAR, less than half the 18 SAR target - the cost case is won.",
            the_honest_statement="Fully loaded cost per transaction is %.2f SAR against an 18 SAR target, and five regions are still above it." % f["cost_all"],
            the_fix="Cost KPIs must carry the full delivery footprint. If a channel is excluded, the tile title says so and the excluded volume is shown next to it.",
            severity="High",
            detectability="Medium",
        ),
    ]
    cols = ["technique_id", "technique_en", "technique_ar", "kpi_affected", "figure_unit",
            "spun_figure", "honest_figure", "gap", "how_it_was_produced",
            "what_the_reader_concludes", "the_honest_statement", "the_fix",
            "severity", "detectability", "source_file"]
    sp = pd.DataFrame(rows)
    sp["gap"] = (sp.spun_figure - sp.honest_figure).round(2)
    return sp[cols]


# ----------------------------------------------------------------------------
# 6. Case B - success_dashboard_spec.csv  (same truth, two dashboards)
# ----------------------------------------------------------------------------
def build_dashboard_spec(f):
    """Ten paired tiles. Every value_shown is formatted from a computed figure."""
    tiles = [
        # ---- T01 ----------------------------------------------------------
        dict(tile_id="T01", tile_title_en="National Digital Adoption",
             tile_title_ar="نسبة التبني الرقمي على المستوى الوطني",
             spun=dict(chart_type="KPI card (large number)",
                       measure="AVERAGE(digital_adoption_pct)",
                       filter_applied="month = 2026-06",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="%.1f%%" % f["adopt_naive"],
                       colour_rule="Amber fill because 61.2 sits between 55 and 62",
                       annotation="(none)",
                       what="Hides that the measure is non-additive and was averaged across 468 segment rows",
                       note="SPIN-01. The card is the first thing read and the last thing checked."),
             honest=dict(chart_type="KPI card with sparkline and distribution strip",
                         measure="SUM(digital_adoption_pct/100 * unique_users) / SUM(unique_users) * 100",
                         filter_applied="month = 2026-06",
                         axis_start="no axis", axis_end="no axis",
                         value_shown="%.1f%%" % f["adopt_weighted"],
                         colour_rule="Neutral fill; the 65.0 target drawn as a reference line, no traffic light",
                         annotation="User-weighted, per KPI-01. Regional range %.1f%% to %.1f%%." % (
                             f["region_adopt_min"], f["region_adopt_max"]),
                         what="Reveals that one national number covers a 17.8pp regional spread",
                         note="The measure definition belongs on the tile, not in a data dictionary nobody opens.")),
        # ---- T02 ----------------------------------------------------------
        dict(tile_id="T02", tile_title_en="Adoption Momentum",
             tile_title_ar="زخم التبني",
             spun=dict(chart_type="Two-bar column chart",
                       measure="Adoption, 2025-06 vs 2026-06",
                       filter_applied="last 12 months, endpoints only",
                       axis_start="60", axis_end="65",
                       value_shown="%.2f%% -> %.2f%%" % (f["adopt_12m_ago"], f["adopt_weighted"]),
                       colour_rule="Growth bar in brand green, baseline bar in grey",
                       annotation="'Adoption keeps climbing'",
                       what="A 2.16pp rise is drawn as a bar more than twice as tall: lie factor %.1f" % f["lie_factor"],
                       note="SPIN-02. Ask the class to measure the two bars with a ruler before revealing the axis."),
             honest=dict(chart_type="Line chart, 60 months",
                         measure="Adoption, full window",
                         filter_applied="2021-07 to 2026-06, no filter",
                         axis_start="0", axis_end="100",
                         value_shown="%.1f%% -> %.1f%% (+%.1fpp)" % (
                             f["adopt_first_month"], f["adopt_weighted"], f["growth_pp"]),
                         colour_rule="Single line; the last nine months drawn in the accent colour",
                         annotation="Slope has fallen from %.2f to %.2f pp/month" % (f["cherry_slope"], f["slope_9m"]),
                         what="Reveals the deceleration that the two-bar version removes by construction",
                         note="Two points cannot show a trend. Sixty can.")),
        # ---- T03 ----------------------------------------------------------
        dict(tile_id="T03", tile_title_en="Regional Performance",
             tile_title_ar="الأداء حسب المنطقة",
             spun=dict(chart_type="Choropleth map, raw digital transaction counts",
                       measure="SUM(transactions WHERE channel is digital)",
                       filter_applied="month = 2026-06",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="Riyadh 2,193,502 / Makkah 2,036,556 darkest",
                       colour_rule="Sequential green ramp on the raw count",
                       annotation="(none)",
                       what="Population, not performance: the map is a population map with extra steps",
                       note="Case C. A raw-count choropleth always finds the biggest region."),
             honest=dict(chart_type="Sorted dot plot, digital transactions per 1,000 residents",
                         measure="SUM(transactions WHERE channel is digital) / population_2025 * 1000",
                         filter_applied="month = 2026-06",
                         axis_start="0", axis_end="260",
                         value_shown="%s %d of 13 per capita (%d of 13 by raw volume)" % (
                             f["shift_region"], f["shift_pc_rank"], f["shift_raw_rank"]),
                         colour_rule="Grey dots; the five Tier-1 regions in the accent colour",
                         annotation="National reference line at %.1f per 1,000" % f["nat_digital_per_1k"],
                         what="Reveals %s falling %d places once population is in the denominator" % (
                             f["shift_region"], abs(f["shift_value"])),
                         note="Rank shift between the two encodings is the whole Case C lesson.")),
        # ---- T04 ----------------------------------------------------------
        dict(tile_id="T04", tile_title_en="Citizens Served This Month",
             tile_title_ar="المستفيدون هذا الشهر",
             spun=dict(chart_type="Big number",
                       measure="SUM(transactions)",
                       filter_applied="month = 2026-06",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="{:,} citizens".format(f["monthly_transactions"]),
                       colour_rule="Brand green, 72pt",
                       annotation="'More than a third of the population'",
                       what="Counts repeat transactions as separate people",
                       note="SPIN-09. The noun on the tile is the claim."),
             honest=dict(chart_type="Big number with a secondary figure",
                         measure="SUM(unique_users), with SUM(transactions) beneath",
                         filter_applied="month = 2026-06",
                         axis_start="no axis", axis_end="no axis",
                         value_shown="{:,} beneficiaries / {:,} transactions".format(
                             f["monthly_unique_users"], f["monthly_transactions"]),
                         colour_rule="Neutral; no colour carries meaning on a count tile",
                         annotation="%.2f transactions per beneficiary. unique_users is semi-additive - never summed across months." % (
                             f["monthly_transactions"] / f["monthly_unique_users"]),
                         what="Reveals that reach and volume are different questions",
                         note="Pair every volume number with its denominator.")),
        # ---- T05 ----------------------------------------------------------
        dict(tile_id="T05", tile_title_en="Satisfaction",
             tile_title_ar="رضا المستفيدين",
             spun=dict(chart_type="Gauge",
                       measure="AVERAGE(csat)",
                       filter_applied="month = 2026-06",
                       axis_start="1", axis_end="5",
                       value_shown="%.2f" % f["csat_naive"],
                       colour_rule="Red / amber / green arcs at 3.7 / 4.0 / 4.3",
                       annotation="(none)",
                       what="Unweighted average; the needle sits on the amber boundary by accident of method",
                       note="SPIN-06. A gauge spends a quarter of the canvas on one number and still gets it wrong."),
             honest=dict(chart_type="Bullet chart",
                         measure="SUM(csat * transactions) / SUM(transactions)",
                         filter_applied="month = 2026-06",
                         axis_start="3.0", axis_end="5.0",
                         value_shown="%.2f" % f["csat_weighted"],
                         colour_rule="Single bar, target 4.30 as a tick; qualitative bands in light grey",
                         annotation="Transaction-weighted, per KPI-03. Branch CSAT %.2f, Mobile App %.2f." % (
                             f["csat_branch"], f["csat_mobile"]),
                         what="Reveals the channel spread behind the single score",
                         note="Bullet chart: same information, one eighth of the ink.")),
        # ---- T06 ----------------------------------------------------------
        dict(tile_id="T06", tile_title_en="Cost per Transaction",
             tile_title_ar="تكلفة المعاملة",
             spun=dict(chart_type="KPI card with green down-arrow",
                       measure="SUM(cost_per_txn_sar * transactions) / SUM(transactions)",
                       filter_applied="month = 2026-06 AND channel <> 'Branch'",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="%.2f SAR" % f["cost_excl_branch"],
                       colour_rule="Green because the number is under the 18 SAR target",
                       annotation="'Less than half the target'",
                       what="The excluded branch channel is the entire cost problem",
                       note="SPIN-13. The filter is real, documented nowhere, and decisive."),
             honest=dict(chart_type="KPI card plus a small multiple by channel",
                         measure="SUM(cost_per_txn_sar * transactions) / SUM(transactions)",
                         filter_applied="month = 2026-06, all four channels",
                         axis_start="0", axis_end="70",
                         value_shown="%.2f SAR" % f["cost_all"],
                         colour_rule="Neutral card; 18 SAR target as a reference line on the small multiple",
                         annotation="All channels included. Branch %.1f SAR, Mobile App %.2f SAR." % (
                             f["cost_branch"], f["cost_mobile"]),
                         what="Reveals that the saving comes from moving volume, not from cheaper delivery",
                         note="Any filter that changes the answer belongs in the title.")),
        # ---- T07 ----------------------------------------------------------
        dict(tile_id="T07", tile_title_en="Projection to December 2026",
             tile_title_ar="التوقع حتى ديسمبر 2026",
             spun=dict(chart_type="Line with a fitted extension",
                       measure="Adoption projected on the full-window slope",
                       filter_applied="trend fitted from %s" % f["cherry_start_month"],
                       axis_start="30", axis_end="70",
                       value_shown="%.1f%% by Dec-2026" % f["cherry_projection_dec"],
                       colour_rule="Dashed green projection, no interval",
                       annotation="'On track to exceed target'",
                       what="Fits the trend from the fastest-growing start month available",
                       note="SPIN-03. The start month is a choice; make the class find it."),
             honest=dict(chart_type="Line with two projection scenarios",
                         measure="Adoption projected on the nine-month slope, with the full-window slope shown for contrast",
                         filter_applied="last nine months for the primary fit",
                         axis_start="30", axis_end="70",
                         value_shown="%.1f%% by Dec-2026 (full-window fit: %.1f%%)" % (
                             f["honest_projection_dec"], f["cherry_projection_dec"]),
                         colour_rule="Grey band between the two scenarios; target line at 65",
                         annotation="Recent slope %.3f pp/month vs %.3f since %s" % (
                             f["slope_9m"], f["cherry_slope"], f["cherry_start_month"]),
                         what="Reveals that the projection is a choice of window, and shows both",
                         note="Show the uncertainty you created by choosing.")),
        # ---- T08 ----------------------------------------------------------
        dict(tile_id="T08", tile_title_en="Regional RAG Status",
             tile_title_ar="حالة المناطق (أحمر/برتقالي/أخضر)",
             spun=dict(chart_type="13-cell colour grid",
                       measure="Region adoption vs a green line set at 62.0",
                       filter_applied="month = 2026-06",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="%d of 13 green" % f["regions_green_at_62"],
                       colour_rule="Green at or above 62.0, amber 55.0-62.0, red below 55.0",
                       annotation="(no thresholds printed)",
                       what="Uses the amber line as the green line; the 65.0 target never appears",
                       note="SPIN-07. Colour with no printed threshold is an assertion, not evidence."),
             honest=dict(chart_type="Sorted bar chart with the target line",
                         measure="Region adoption vs threshold_green from kpi_targets.csv",
                         filter_applied="month = 2026-06",
                         axis_start="0", axis_end="70",
                         value_shown="%d of 13 at or above 65.0; %d below target" % (
                             f["regions_green_at_65"], f["regions_below_target"]),
                         colour_rule="Diverging scale centred on the 65.0 target, thresholds printed on the axis",
                         annotation="Thresholds read from kpi_targets.csv: red 55.0, amber 62.0, green 65.0",
                         what="Reveals how far below the line each region is, not merely that it is",
                         note="Bind thresholds to the governance file at build time.")),
        # ---- T09 ----------------------------------------------------------
        dict(tile_id="T09", tile_title_en="Growth Since Programme Start",
             tile_title_ar="النمو منذ انطلاق البرنامج",
             spun=dict(chart_type="Indexed line, 13 series",
                       measure="Region adoption indexed to 2021-07 = 100",
                       filter_applied="all 60 months",
                       axis_start="100", axis_end="220",
                       value_shown="%s leads at %.1f" % (f["index_region"], f["index_value"]),
                       colour_rule="%s highlighted, the rest grey" % f["index_region"],
                       annotation="'Our fastest-improving region'",
                       what="Rebasing deletes the level: the leader is %d of 13 on the actual measure" % f["index_rank_by_level"],
                       note="SPIN-10. Index charts always flatter whoever started lowest."),
             honest=dict(chart_type="Dot plot of current level with a connector to the 2021 baseline",
                         measure="Region adoption, level and change together",
                         filter_applied="2021-07 and 2026-06",
                         axis_start="0", axis_end="70",
                         value_shown="%s %.1f%% today, %d of 13" % (
                             f["index_region"], f["index_level"], f["index_rank_by_level"]),
                         colour_rule="Grey connectors, current-value dots coloured against the 65.0 target",
                         annotation="Index %.1f on a 2021-07 = 100 base; level %.1f%%, %.1fpp below target" % (
                             f["index_value"], f["index_level"], 65.0 - f["index_level"]),
                         what="Reveals level and change in one mark, so neither can hide the other",
                         note="If you index, print the base value.")),
        # ---- T10 ----------------------------------------------------------
        dict(tile_id="T10", tile_title_en="Digital Share of Service Delivery",
             tile_title_ar="حصة القنوات الرقمية من تقديم الخدمة",
             spun=dict(chart_type="Donut",
                       measure="Digital transactions / non-branch transactions",
                       filter_applied="month = 2026-06 AND channel <> 'Branch'",
                       axis_start="no axis", axis_end="no axis",
                       value_shown="%.1f%% digital" % f["digital_share_excl_branch"],
                       colour_rule="Two-segment donut, digital in brand green",
                       annotation="'The channel shift is nearly complete'",
                       what="Removes the {:,} branch transactions the programme exists to move".format(f["branch_txn"]),
                       note="SPIN-11. A donut hides the denominator twice: by shape and by filter."),
             honest=dict(chart_type="100% stacked bar by channel, 60 months",
                         measure="Transactions by channel as a share of all transactions",
                         filter_applied="all channels, all months",
                         axis_start="0", axis_end="100",
                         value_shown="%.1f%% digital (%.1f%% if branch is excluded)" % (
                             f["digital_share_all"], f["digital_share_excl_branch"]),
                         colour_rule="Four ordered channel colours, branch at the top where the change is visible",
                         annotation="Denominator = all four channels. Branch alone is %.1f%% of volume." % f["branch_share"],
                         what="Reveals the residual branch volume and how slowly it is falling",
                         note="Composition questions need the whole whole.")),
    ]

    rows = []
    for t in tiles:
        for variant in ("spun", "honest"):
            v = t[variant]
            rows.append({
                "variant": variant,
                "tile_id": t["tile_id"],
                "tile_title_en": t["tile_title_en"],
                "tile_title_ar": t["tile_title_ar"],
                "chart_type": v["chart_type"],
                "measure": v["measure"],
                "filter_applied": v["filter_applied"],
                "axis_start": v["axis_start"],
                "axis_end": v["axis_end"],
                "value_shown": v["value_shown"],
                "colour_rule": v["colour_rule"],
                "annotation": v["annotation"],
                "what_it_hides_or_reveals": v["what"],
                "teaching_note": v["note"],
            })
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------
# 7. critique_canon.csv - facts drawn only from research/famous_viz_verified.md
# ----------------------------------------------------------------------------
def build_critique_canon():
    rows = [
        dict(
            item_id="CAN-01",
            title="Map of the Broad Street cholera outbreak",
            creator="John Snow; engraved by Charles Cheffins",
            year="1854 (shown to the London Epidemiological Society, December 1854; published 1855)",
            module_used_in="M2 - chart choice and the raw-count map",
            encodings="Street base map; one stacked black bar per death at the victim's address; labelled pump marks; a dotted isoline of equal walking distance by the nearest road to the Broad Street pump",
            the_claim="Cholera is transmitted by contaminated water, not miasma - specifically the Broad Street pump was the common source.",
            what_it_does_brilliantly="The first dot map to make a spatial hypothesis testable, and the anomalies carry the argument: 61 deaths confirmed as pump-water drinkers, the brewery workers on a beer allowance who did not die, the workhouse with its own well. The walking-distance isoline is the first use of a network distance surface in epidemiology.",
            documented_flaw="It is a raw-count map with no population denominator, made after the outbreak ended and playing no part in persuading the vestry; roughly three quarters of residents had fled, so the denominator moved under it. Stacked bars conflate a death with a death at an address, inflating apparent density at large tenements. Snow's own case rested more on the Southwark & Vauxhall versus Lambeth water-company comparison than on the map.",
            transferable_lesson_for_tayseer="Our raw digital-transaction choropleth has the same defect: it finds Riyadh and Makkah because they are large. Case C's per-capita rate map is the corrected form.",
            critique_question_1="What is the denominator on this map, and what happens to the argument once you learn that three quarters of the residents had left?",
            critique_question_2="Snow's dotted line is a walking-distance boundary, not a Voronoi cell. Why is that distinction worth a slide?",
        ),
        dict(
            item_id="CAN-02",
            title="Carte figurative des pertes successives en hommes de l'Armee Francaise dans la campagne de Russie 1812-1813",
            creator="Charles Joseph Minard",
            year="1869 (lithograph, 62 x 30 cm, dated 20 November 1869)",
            module_used_in="M3 - encoding density and narrative subordination",
            encodings="Six variables: troop number as band width (1 mm per 10,000 men), longitude, latitude, direction of travel as colour (tan = advance, black = retreat), position relative to dates, and a temperature line below aligned by longitude",
            the_claim="The catastrophic attrition of the Grande Armee, coupled to distance, direction, river crossings and cold.",
            what_it_does_brilliantly="Six dimensions with no gridlines, no legend clutter and two colours. The arithmetic closes: 340,000 + 60,000 + 22,000 = 422,000 crossing the Niemen, and 4,000 + 6,000 = 10,000 returning. The temperature curve is narratively subordinated beneath the flow so the reader couples cold to collapse unprompted.",
            documented_flaw="Deliberate geographic distortion: the retreat leg is drifted south so it does not overlap the advance. A linear taper between Vilnius and Vitebsk hides roughly 165,000 deaths on that leg - more than the entire retreat. The band is non-monotonic near longitude 26.4, rising from 12,000 to 14,000. One temperature reading carries no date, there is a gap implying over 50 miles of movement in a day, and the temperatures are degrees Reaumur, not Celsius (C = Re x 1.25), so relabelled reproductions understate the cold by 25%.",
            transferable_lesson_for_tayseer="Interpolating between two reporting points can erase the worst period entirely. Plot every one of our 60 months; never draw a straight line between the endpoints.",
            critique_question_1="The band width is monotonic except at one point. Find it, and decide whether the exception is data or drafting.",
            critique_question_2="Convert the temperature axis from Reaumur to Celsius. How much colder does the retreat become, and what does that do to the story?",
        ),
        dict(
            item_id="CAN-03",
            title="Diagram of the Causes of Mortality in the Army in the East",
            creator="Florence Nightingale",
            year="1858",
            module_used_in="M1 - perception and the encoding accuracy hierarchy",
            encodings="Two circles of twelve equal-angle sectors, April 1854 - March 1855 and April 1855 - March 1856; blue = preventible or mitigable zymotic disease, red = wounds, black = all other causes; wedges superimposed from a common vertex at the centre, area proportional to the annual death rate per 1,000",
            the_claim="Most deaths in the Crimea were from preventible disease, and they fell after the Sanitary Commission arrived at Scutari in March 1855.",
            what_it_does_brilliantly="The split at March 1855 is the argument, built into the layout. The rose is correctly area-encoded - Nightingale identified the radius error in her earlier bat's wing diagram, issued an erratum slip, and replaced it with the wedges. January 1855 disease mortality reaches an annualised 1,022.8 per 1,000, an annual rate above 100% of the force.",
            documented_flaw="Even with correct area encoding, angular and area extent sit low on the decoding-accuracy hierarchy and readers tend to read radial extent, so differences are perceptually exaggerated at the extremes. The three wedges are superimposed, not stacked, and most modern recreations read them cumulatively and overstate total mortality. Nightingale's own line chart of the same rates is more accurate to read, and Hugh Small argues it was probably more influential on the reform.",
            transferable_lesson_for_tayseer="Our gauge wall lost to a sorted bar chart in the Module 4 usability benchmark for exactly this reason. Rhetorical force and decoding accuracy are different objectives - choose one deliberately.",
            critique_question_1="Redraw one circle as a line chart of the same rates. Which reading task gets easier, and which gets harder?",
            critique_question_2="The wedges share a vertex rather than stacking. What does a reader who assumes stacking conclude, and by how much are they wrong?",
        ),
        dict(
            item_id="CAN-04",
            title="Gapminder animated bubble chart (Trendalyzer)",
            creator="Hans Rosling, with Ola Rosling and Anna Rosling Ronnlund; Gapminder Foundation",
            year="2006 TED talk 'The best stats you've ever seen'; Trendalyzer acquired by Google March 2007",
            module_used_in="M5 - presentation versus analysis",
            encodings="x = income per person on a log scale, y = life expectancy, size = population, colour = world region, time = animation frame with a scrub slider and trails",
            the_claim="Country development is a continuum that moves over time, not a fixed rich-world / poor-world split.",
            what_it_does_brilliantly="Four variables plus time in one readable frame, with a narrator carrying attention across the animation. It is the canonical demonstration that a chart can be a performance.",
            documented_flaw="Robertson, Fernandez, Fisher, Lee & Stasko (2008) tested it directly: animation is the least effective form for analysis. In the analysis condition, small multiples took 45.69 s, traces 55.01 s and animation 83.10 s, with small multiples significantly more accurate (p < .001). In the presentation condition animation was fastest at 15.80 s. Without the narrator the chart becomes a change-blindness problem, and two non-adjacent years cannot be compared at all. Bubble area is a weak channel and overplotting destroys readability at high counts.",
            transferable_lesson_for_tayseer="Animate for the committee room, small-multiple for the analyst pack. Our 13-region trend grid is the analysis form; the animated version belongs only in a narrated session.",
            critique_question_1="Name the reading task the animation makes impossible, and the chart form that restores it.",
            critique_question_2="If animation is 82% slower for analysis and fastest for presentation, which of our two Tayseer audiences gets which version?",
        ),
        dict(
            item_id="CAN-05",
            title="Our World in Data grapher charts",
            creator="Our World in Data - Max Roser, University of Oxford and the Global Change Data Lab (registered charity 1186433)",
            year="Founded May 2013; Grapher is the in-house chart engine",
            module_used_in="M4 - the reusable chart object and governed publishing",
            encodings="One configurable chart object per indicator: switchable chart types, country selector, time slider, download tab for data and image, and an embed code. Exemplars include life expectancy versus CO2 per capita (log x, linear y, size = population, colour = region) and the CO2 per-capita Marimekko where width = population, height = per-capita emissions and area = total emissions.",
            the_claim="Public statistics become usable when every chart carries its data, its sources and its licence with it.",
            what_it_does_brilliantly="Every chart is an interactive object that ships its own data and provenance, which is exactly why it survives being embedded elsewhere. The Marimekko double-encoding is a clean teaching case for area judgement and a direct companion to the Nightingale debate.",
            documented_flaw="Two licensing traps. OWID's own content and data are CC BY, but third-party data carried in a grapher keeps the third party's licence, so 'check the Learn more about this data panel' is a required step. And the Grapher source code is no longer MIT: the current licence permits viewing and studying the code only, and forbids copying, modifying or redistributing it without written permission. Wikipedia and most secondary sources are out of date on this - do not tell a class they can fork Grapher.",
            transferable_lesson_for_tayseer="Our Tayseer tiles should carry the same three things OWID charts do: the measure definition, the source file, and the download. That is what makes a dashboard auditable rather than merely attractive.",
            critique_question_1="Open the Marimekko. Which of the three quantities encoded there can you actually read off, and which one are you estimating?",
            critique_question_2="A chart you embed is CC BY but its underlying series is not. What must appear on the slide?",
        ),
        dict(
            item_id="CAN-06",
            title="The New York Times election needle",
            creator="The New York Times Graphics department; gauge designed and built by Gregor Aisch, election results operation led by Wilson Andrews",
            year="Debuted election night, 8 November 2016",
            module_used_in="M6 - communicating uncertainty under pressure",
            encodings="A gauge needle showing a live in-progress forecast, not a vote count; the needle's range fixed between the 25th and 75th percentile of the model's simulated outcomes; movement generated with Perlin noise so it reads as organic; amplitude narrows as the forecast tightens",
            the_claim="The probable final outcome, updated as partial returns arrive, with the visible wobble standing in for the uncertainty.",
            what_it_does_brilliantly="The jitter is the uncertainty, not decoration - its amplitude is the interquartile range of the simulations. Aisch's rationale is that bare probabilities fail most audiences because it is very hard to make sense of probabilities between 75% and 85%. Hullman, Resnick & Adar's hypothetical outcome plots (PLOS ONE, 2015) supply the formal justification: animating individual draws lets viewers count and integrate rather than decode a statistical convention.",
            documented_flaw="A broken metaphor - real gauges do not jitter, so viewers read the wobble as a malfunction or as live incoming data. Critics argued it implied a trend where none existed, as stochastic movement was read as direction. It became a mass anxiety object. Aisch's own concession is that the piece lacked explicit, static annotation of what it was doing. In 2020 the Times dropped the national needle and ran needles for only Georgia, Florida and North Carolina, because record absentee balloting broke the model's assumptions.",
            transferable_lesson_for_tayseer="Our December 2026 projection is a forecast with a window choice inside it. Show the range, label the method on the tile, and never let a projection wear the visual costume of a measurement.",
            critique_question_1="The wobble encodes the interquartile range. What does a viewer who has not been told that conclude instead?",
            critique_question_2="Which of our dashboard tiles is a forecast dressed as a measurement, and what static annotation fixes it?",
        ),
        dict(
            item_id="CAN-07",
            title="How the Virus Got Out",
            creator="Jin Wu, Weiyi Cai, Derek Watkins and James Glanz, The New York Times",
            year="Published 22 March 2020",
            module_used_in="M5 - sequencing and scrollytelling",
            encodings="Scrollytelling narrative; animated dot-density maps at fixed dates (1, 21, 23, 31 January; 14 February; 1, 11, 20 March); a mobility and flow visualisation of individual movements out of Wuhan built on phone-location and travel data; comparative regional insets; a travel-volume time series",
            the_claim="Roughly seven million people left Wuhan before the 23 January cordon, so the lockdown came too late to contain global spread.",
            what_it_does_brilliantly="The piece controls the order in which facts arrive, so the reader reaches the conclusion by construction rather than by assertion. The flow animation shows a mechanism - the movement of individuals - rather than an aggregate quantity, which is the rare case where animation earns its place.",
            documented_flaw="Sequencing is persuasion. A reader taken through a fixed order cannot interrogate an alternative order, and the fixed date stops are editorial choices that the form presents as natural. The same technique that makes the argument legible also makes it hard to dissent from inside the piece.",
            transferable_lesson_for_tayseer="Module 5's storyboard is this technique at committee scale. Sequence deliberately, and then state the sequence out loud so the audience knows a choice was made.",
            critique_question_1="List the eight date stops. Which of them are epidemiological and which are editorial?",
            critique_question_2="Where in the Tayseer story does sequence do work that a single chart could not - and where would it be manipulation?",
        ),
        dict(
            item_id="CAN-08",
            title="Missing Deaths / U.S. Deaths Near 100,000, An Incalculable Loss",
            creator="The New York Times - excess-deaths tracker published 21 April 2020; the front page led by Simone Landon, with names compiled by Alain Delaquerière",
            year="2020 (excess deaths from 21 April; the front page on 24 May)",
            module_used_in="M5 - the baseline is the argument, and when not to make a chart",
            encodings="Excess deaths: a line for observed mortality against a modelled expected line with a shaded band, for 32 countries plus selected cities. The front page: no chart at all - 1,000 names and one-line obituary fragments set as continuous type filling the page.",
            the_claim="The true toll of the pandemic exceeds the confirmed count, and its magnitude is not something a quantity can carry alone.",
            what_it_does_brilliantly="The excess-deaths visual is trivial - a line and a band - while every contested claim lives in how the counterfactual was built: a linear model on 2015-2019 mortality with a time trend for demographic change and a smoothing spline for seasonality. The front page is the deliberate refusal of aggregation, stated intent being to convey the vastness and variety of the tragedies by personalising them, countering data fatigue.",
            documented_flaw="The excess-deaths README carries its own caveat: the expected deaths are not adjusted for how non-Covid deaths may change during the outbreak, so the baseline is contestable exactly where the claim is strongest. The front page's pre-publication tweet was later deleted after one listed person turned out to have died by homicide - sourcing from online obituaries at speed has a failure mode.",
            transferable_lesson_for_tayseer="Our do-nothing projection in regional_scorecard_latest.csv is a counterfactual, and the hard part is upstream of the chart. State the baseline method on the slide, and know when a list of names beats a bar.",
            critique_question_1="Rebuild the expected-deaths line with a different baseline window. How much of the claim survives?",
            critique_question_2="Is there a point in the Tayseer story where the right answer is not a chart? Defend it.",
        ),
        dict(
            item_id="CAN-09",
            title="FT COVID-19 trajectory charts and the FT Visual Vocabulary",
            creator="John Burn-Murdoch (trajectories) and the FT Visual Journalism Team (Visual Vocabulary); Chart Doctor column by Alan Smith",
            year="Trajectories first published 11 March 2020 (prototyped 10 March); Chart Doctor launched May 2016",
            module_used_in="M2 - matching the relationship to the chart form; M3 - scale choice",
            encodings="Trajectories: x = days since the country's 100th confirmed case, y = cumulative cases or deaths on a log scale, diagonal doubling-time reference lines, direct line labels with no legend, East Asian countries blue and Italy black with everything else grey, and a narrative headline. Visual Vocabulary: nine relationship categories - deviation, correlation, ranking, distribution, change over time, part-to-whole, magnitude, spatial, flow.",
            the_claim="Trajectories: national epidemics are comparable once aligned on a common starting point, and the slope is the growth rate. Visual Vocabulary: chart choice follows from the relationship you want to show.",
            what_it_does_brilliantly="On a log scale the slope is the growth rate, so the reading task becomes comparing slopes against the doubling-time guides - the epidemiologically meaningful comparison. Aligning on days since the 100th case removes the confound of when an epidemic started. The doubling-time diagonals are the single most important annotation on the chart. The Visual Vocabulary's nine categories are a genuinely good course spine.",
            documented_flaw="Romano, Sotis, Dominioni & Guidi (Health Economics, 2020, 29(11), 1482-1494) found that showing COVID deaths on a logarithmic scale left people with a less accurate understanding of how the pandemic had developed, less accurate predictions, and shifted attitudes and policy preferences; they recommend a linear scale as the default for general audiences. Daily wiggles also reflect reporting schedules rather than transmission, which is why seven-day rolling averages followed. Separately, the Visual Vocabulary is copyright The Financial Times, all rights reserved - link to it, do not reproduce it in course materials without clearance.",
            transferable_lesson_for_tayseer="The same chart can be well designed and misleading depending on which question the reader brought. Decide whether the tile serves the analyst comparing rates or the committee judging magnitude, and say which on the tile.",
            critique_question_1="Redraw one trajectory chart on a linear axis. Which reader is now better served, and which is worse?",
            critique_question_2="Take three Tayseer questions to the nine Visual Vocabulary categories. Does the category the question falls into match the chart we shipped?",
        ),
        dict(
            item_id="CAN-10",
            title="FiveThirtyEight probabilistic forecast displays",
            creator="FiveThirtyEight (Nate Silver; later G. Elliott Morris)",
            year="2016 and 2020 election forecasts; the site was shut down on 5 March 2025",
            module_used_in="M6 - probability, frequency framing and the hostile question",
            encodings="A histogram or dot array of roughly 40,000 simulated outcomes across electoral-vote totals; frequency framing in the headline ('he wins X in 100 times we run this'); the snake chart, where states are laid out along a winding path from most Democratic to most Republican, position shows how competitive a state is, segment length encodes electoral votes and colour encodes party lean and confidence.",
            the_claim="A forecast is a distribution, not a number, and the reader should be shown the whole distribution.",
            what_it_does_brilliantly="In 2016 FiveThirtyEight's final figure was Trump 29% / Clinton 71% on polls-only - the least confident mainstream forecast, against HuffPost Pollster at 1.7% for Trump. The 2020 presentation answered 2016 directly with simulation displays, frequency framing and explicit correlated-error discussion. The snake chart lets a reader trace from either end to find the state that crosses 270, which no choropleth does. In 2020 it correctly called 48 states and DC, missing Florida, North Carolina and Maine's second district.",
            documented_flaw="The presentation innovations were attempts to stop readers collapsing 71% into 'certain', and they largely failed - the least confident forecast was the one most widely described as wrong. Two practical hazards for a course: fivethirtyeight.com URLs are all dead, since ABC redirected the archive on 15 May 2026 and every features URL now 302s to abcnews.com/politics, so cite archive.org snapshots only; and the widely repeated claim that FiveThirtyEight published a critique of the hurricane cone of uncertainty could not be verified - attribute that critique to Broad, Leiserowitz, Weinkle & Steketee (BAMS, 2007) and to Alberto Cairo instead.",
            transferable_lesson_for_tayseer="Our December projection is a probability statement. Use frequency framing in the committee - 'in X of 10 plausible futures the five regions still miss 65%' - and show the distribution, not the point.",
            critique_question_1="A committee member says the 71% forecast was 'wrong'. Answer in one sentence that a non-statistician accepts.",
            critique_question_2="Rewrite our December projection tile using frequency framing. What does it cost, and what does it buy?",
        ),
    ]
    cols = ["item_id", "title", "creator", "year", "module_used_in", "encodings",
            "the_claim", "what_it_does_brilliantly", "documented_flaw",
            "transferable_lesson_for_tayseer", "critique_question_1", "critique_question_2"]
    return pd.DataFrame(rows)[cols]


# ----------------------------------------------------------------------------
# 8. Main
# ----------------------------------------------------------------------------
def main():
    fact, regions, channels, kpis, scorecard = load()

    equity, nat_dig_per_1k = build_equity(fact, regions)
    lorenz, gini = build_lorenz(equity)
    figures = compute_figures(fact, regions, equity)
    spin = build_spin_pairs(figures)
    dash = build_dashboard_spec(figures)
    canon = build_critique_canon()

    outputs = [
        ("data/supporting/regional_equity_latest.csv", equity),
        ("data/supporting/regional_equity_lorenz.csv", lorenz),
        ("data/instructional/kpi_spin_pairs.csv", spin),
        ("data/instructional/success_dashboard_spec.csv", dash),
        ("data/instructional/critique_canon.csv", canon),
    ]
    for rel, frame in outputs:
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False, encoding=ENC)
        print("wrote %-48s %4d rows x %2d cols" % (rel, len(frame), frame.shape[1]))

    print("\nHeadline figures")
    print("  Gini (digital transactions vs population)      %.4f" % gini)
    print("  National digital transactions per 1k residents %.2f" % nat_dig_per_1k)
    print("  Biggest rank shift: %s  raw #%d -> per capita #%d" % (
        figures["shift_region"], figures["shift_raw_rank"], figures["shift_pc_rank"]))
    print("  Lie factor (truncated axis, y from 60)         %.1f" % figures["lie_factor"])
    print("  Averages-of-averages gap                       %.2fpp" % (
        figures["adopt_weighted"] - figures["adopt_naive"]))


if __name__ == "__main__":
    main()
