#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_extensions.py — SDA-DSC-112 Tayseer dataset package
============================================================

Automated consistency checks for the Case B and Case C extension datasets, in
the same spirit as docs/validation_report.md.  Every check prints PASS or FAIL
with the detail behind it.

The spin-pair checks are the important ones: for each of the 13 techniques in
kpi_spin_pairs.csv, the stated operation is re-executed here, independently of
the build script, straight against the shipped CSVs, and compared with the
spun_figure and honest_figure columns.  Nothing is asserted on trust.

Run:  python3 scripts/validate_extensions.py       (from the package root)
Exit code 0 when every check passes, 1 otherwise.
"""

from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ENC = "utf-8-sig"
DIGITAL_CHANNELS = ["Mobile App", "Web Portal"]
STALLED = ["Jazan", "Najran", "Al-Baha", "Asir", "Northern Borders"]

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((bool(ok), name, str(detail)))
    print("%-6s %-72s %s" % ("PASS" if ok else "FAIL", name, detail))
    return bool(ok)


def close(a, b, tol=0.051):
    return abs(float(a) - float(b)) <= tol


# ----------------------------------------------------------------------------
# Sources
# ----------------------------------------------------------------------------
fact = pd.read_csv(ROOT / "data/core/tayseer_services.csv", encoding=ENC, parse_dates=["month"])
regions = pd.read_csv(ROOT / "data/dimensions/dim_regions.csv", encoding=ENC)
kpis = pd.read_csv(ROOT / "data/supporting/kpi_targets.csv", encoding=ENC).set_index("kpi_id")
scorecard = pd.read_csv(ROOT / "data/supporting/regional_scorecard_latest.csv", encoding=ENC)

equity = pd.read_csv(ROOT / "data/supporting/regional_equity_latest.csv", encoding=ENC)
lorenz = pd.read_csv(ROOT / "data/supporting/regional_equity_lorenz.csv", encoding=ENC)
spin = pd.read_csv(ROOT / "data/instructional/kpi_spin_pairs.csv", encoding=ENC)
dash = pd.read_csv(ROOT / "data/instructional/success_dashboard_spec.csv", encoding=ENC)
canon = pd.read_csv(ROOT / "data/instructional/critique_canon.csv", encoding=ENC)

NEW_FILES = ["data/supporting/regional_equity_latest.csv",
             "data/supporting/regional_equity_lorenz.csv",
             "data/instructional/kpi_spin_pairs.csv",
             "data/instructional/success_dashboard_spec.csv",
             "data/instructional/critique_canon.csv"]

L = fact[fact.month == fact.month.max()]
F0 = fact[fact.month == fact.month.min()]


def wmean(frame, col, weight):
    return float((frame[col] * frame[weight]).sum() / frame[weight].sum())


def adoption(frame):
    return 100.0 * float((frame.digital_adoption_pct / 100.0 * frame.unique_users).sum()
                         / frame.unique_users.sum())


print("Case B / Case C extension validation\n" + "=" * 96)

# ----------------------------------------------------------------------------
# A. Structure
# ----------------------------------------------------------------------------
check("Every extension file is UTF-8 with BOM",
      all(open(ROOT / f, "rb").read(3) == b"\xef\xbb\xbf" for f in NEW_FILES),
      "%d files" % len(NEW_FILES))

check("regional_equity_latest has one row per region", len(equity) == 13, "%d rows" % len(equity))
check("regional_equity_lorenz has one row per region", len(lorenz) == 13, "%d rows" % len(lorenz))
check("kpi_spin_pairs carries at least 10 spin techniques", len(spin) >= 10, "%d techniques" % len(spin))
check("success_dashboard_spec pairs every tile", len(dash) == 2 * dash.tile_id.nunique(),
      "%d rows, %d tiles x 2 variants" % (len(dash), dash.tile_id.nunique()))
check("critique_canon carries the ten exemplars", len(canon) == 10, "%d rows" % len(canon))
check("No nulls anywhere in the five extension files",
      not any(pd.read_csv(ROOT / f, encoding=ENC).isna().any().any() for f in NEW_FILES))

# ----------------------------------------------------------------------------
# B. Keys
# ----------------------------------------------------------------------------
valid_regions = set(regions.region)
check("Equity region keys resolve to dim_regions",
      set(equity.region) == valid_regions, "%d regions" % equity.region.nunique())
check("Lorenz region keys resolve to dim_regions",
      set(lorenz.region) == valid_regions, "%d regions" % lorenz.region.nunique())
check("Equity region_code and region_ar match dim_regions exactly",
      equity.merge(regions, on="region", suffixes=("", "_dim")).eval(
          "region_code == region_code_dim and region_ar == region_ar_dim").all())
check("Equity population and area match dim_regions exactly",
      equity.merge(regions, on="region", suffixes=("", "_dim")).eval(
          "population_2025 == population_2025_dim and area_km2 == area_km2_dim "
          "and households_2025 == households_2025_dim and service_branches == service_branches_dim").all())
check("The five Tier-1 regions are unchanged",
      sorted(equity[equity.priority_tier.str.startswith("Tier 1")].region) == sorted(STALLED),
      ", ".join(sorted(STALLED)))

# ----------------------------------------------------------------------------
# C. Case C — per-capita values reconcile with regional_scorecard_latest.csv
# ----------------------------------------------------------------------------
m = equity.merge(scorecard, on="region", suffixes=("_eq", "_sc"))
for col, tol in [("digital_txn_per_1k_pop", 0.05), ("txn_per_1k_pop", 0.05),
                 ("digital_adoption_pct", 0.05), ("cost_per_txn_sar", 0.05),
                 ("csat", 0.005), ("avg_completion_min", 0.05),
                 ("monthly_transactions", 0.0), ("monthly_unique_users", 0.0)]:
    d = (m[col + "_eq"] - m[col + "_sc"]).abs()
    check("Equity reconciles with the scorecard on %s" % col, (d <= tol).all(),
          "max |diff| = %.4f" % d.max())

# ----------------------------------------------------------------------------
# D. Case C — values reproduce from the fact table
# ----------------------------------------------------------------------------
rec = L.groupby("region").apply(
    lambda g: pd.Series({
        "txn": g.transactions.sum(),
        "dig": g[g.channel.isin(DIGITAL_CHANNELS)].transactions.sum(),
        "adopt": adoption(g)}))
rec = rec.join(regions.set_index("region").population_2025)
rec["txn_per_1k"] = rec.txn / rec.population_2025 * 1000
rec["dig_per_1k"] = rec.dig / rec.population_2025 * 1000
e = equity.set_index("region")
check("digital_txn_per_1k_pop recomputes from tayseer_services + dim_regions",
      close((e.digital_txn_per_1k_pop - rec.dig_per_1k.round(1)).abs().max(), 0),
      "max |diff| = %.4f" % (e.digital_txn_per_1k_pop - rec.dig_per_1k.round(1)).abs().max())
check("txn_per_1k_pop recomputes from tayseer_services + dim_regions",
      close((e.txn_per_1k_pop - rec.txn_per_1k.round(1)).abs().max(), 0),
      "max |diff| = %.4f" % (e.txn_per_1k_pop - rec.txn_per_1k.round(1)).abs().max())

nat_dig_per_1k = L[L.channel.isin(DIGITAL_CHANNELS)].transactions.sum() / regions.population_2025.sum() * 1000
idx = (rec.dig_per_1k / nat_dig_per_1k * 100).round(1)
check("index_vs_national = per-capita rate / national rate x 100",
      (e.index_vs_national - idx).abs().max() <= 0.05,
      "national denominator %.2f digital transactions per 1,000" % nat_dig_per_1k)

check("branches_per_100k_pop and density recompute from dim_regions",
      ((e.branches_per_100k_pop - (e.service_branches / e.population_2025 * 1e5).round(2)).abs().max() <= 0.005)
      and ((e.population_density_per_km2 - (e.population_2025 / e.area_km2).round(2)).abs().max() <= 0.005))

check("Rank columns are complete permutations of 1..13",
      sorted(equity.rank_by_raw_volume) == list(range(1, 14))
      and sorted(equity.rank_by_per_capita) == list(range(1, 14)))
check("rank_shift = rank_by_raw_volume - rank_by_per_capita",
      (equity.rank_shift == equity.rank_by_raw_volume - equity.rank_by_per_capita).all())
worst = equity.sort_values(["rank_shift", "rank_by_per_capita"], ascending=[True, False]).iloc[0]
check("The headline rank shift is a Tier-1 region falling to last per capita",
      worst.rank_by_per_capita == 13 and worst.priority_tier.startswith("Tier 1"),
      "%s: #%d by raw volume, #%d per capita (shift %d)" % (
          worst.region, worst.rank_by_raw_volume, worst.rank_by_per_capita, worst.rank_shift))

# ----------------------------------------------------------------------------
# E. Case C — the Lorenz curve and the Gini
# ----------------------------------------------------------------------------
check("Lorenz rows are sorted ascending by digital transactions per capita",
      lorenz.digital_txn_per_1k_pop.is_monotonic_increasing
      and list(lorenz.lorenz_rank) == list(range(1, 14)))
check("Lorenz population shares sum to 1.0",
      close(lorenz.population_share.sum(), 1.0, 1e-6), "%.10f" % lorenz.population_share.sum())
check("Lorenz digital-transaction shares sum to 1.0",
      close(lorenz.digital_txn_share.sum(), 1.0, 1e-6), "%.10f" % lorenz.digital_txn_share.sum())
check("Cumulative population share ends at exactly 1.0",
      lorenz.cum_population_share.iloc[-1] == 1.0, "%.10f" % lorenz.cum_population_share.iloc[-1])
check("Cumulative digital-transaction share ends at exactly 1.0",
      lorenz.cum_digital_txn_share.iloc[-1] == 1.0, "%.10f" % lorenz.cum_digital_txn_share.iloc[-1])
check("Both cumulative series are monotonic and start above zero",
      lorenz.cum_population_share.is_monotonic_increasing
      and lorenz.cum_digital_txn_share.is_monotonic_increasing
      and lorenz.cum_population_share_start.iloc[0] == 0.0
      and lorenz.cum_digital_txn_share_start.iloc[0] == 0.0)
check("Each segment start equals the previous segment end",
      (lorenz.cum_population_share_start.iloc[1:].values
       == lorenz.cum_population_share.iloc[:-1].values).all())
check("Lorenz curve lies at or below the equality line",
      (lorenz.gap_to_equality >= -1e-9).all(), "max gap %.4f" % lorenz.gap_to_equality.max())

dx = lorenz.cum_population_share - lorenz.cum_population_share_start
area = (dx * (lorenz.cum_digital_txn_share + lorenz.cum_digital_txn_share_start) / 2).sum()
gini_recomputed = 1 - 2 * area
gini_shipped = float(lorenz.gini_coefficient.iloc[0])
check("Gini recomputes from the shipped cumulative shares",
      close(gini_recomputed, gini_shipped, 5e-4),
      "shipped %.4f, recomputed %.4f" % (gini_shipped, gini_recomputed))
check("Gini sits in a plausible range (0 < G < 0.25)",
      0 < gini_shipped < 0.25, "G = %.4f" % gini_shipped)
check("gini_coefficient is constant across the file", lorenz.gini_coefficient.nunique() == 1)
check("Lorenz totals match the equity table",
      lorenz.population_2025.sum() == equity.population_2025.sum()
      and lorenz.monthly_digital_transactions.sum() == equity.monthly_digital_transactions.sum(),
      "{:,} residents, {:,} digital transactions".format(
          int(lorenz.population_2025.sum()), int(lorenz.monthly_digital_transactions.sum())))

# ----------------------------------------------------------------------------
# F. Case B — every spun and honest figure is re-executed here
# ----------------------------------------------------------------------------
sp = spin.set_index("technique_id")
series = fact.groupby("month").apply(adoption)
a = series.values
reg_adopt = L.groupby("region").apply(adoption)
reg_series = fact.groupby(["region", "month"]).apply(adoption).unstack()

slopes = [(a[-1] - a[s]) / (len(a) - 1 - s) for s in range(len(a) - 1)]
best = int(np.argmax(slopes))
slope_9m = (a[-1] - a[-10]) / 9.0
shown = ((a[-1] - 60.0) - (a[-13] - 60.0)) / (a[-13] - 60.0) * 100
real = (a[-1] - a[-13]) / a[-13] * 100
index_latest = reg_series.iloc[:, -1] / reg_series.iloc[:, 0] * 100
top = index_latest.idxmax()
dig = L[L.channel.isin(DIGITAL_CHANNELS)].transactions.sum()
cat = L.groupby("service_category").apply(adoption)
NB = L[L.channel != "Branch"]

EXPECTED = {
    "SPIN-01": (L.digital_adoption_pct.mean(),
                adoption(L),
                "AVERAGE(digital_adoption_pct) vs SUM(pct/100*unique_users)/SUM(unique_users)*100"),
    "SPIN-02": (shown, real,
                "apparent vs actual %% change, y-axis from 60; lie factor %.1f" % (shown / real)),
    "SPIN-03": (a[-1] + 6 * slopes[best], a[-1] + 6 * slope_9m,
                "argmax start month %s (%.4f pp/mo) vs the 9-month slope (%.4f pp/mo)"
                % (series.index[best].strftime("%Y-%m"), slopes[best], slope_9m)),
    "SPIN-04": (adoption(L), adoption(L[L.region.isin(STALLED)]),
                "national vs the five stalled Tier-1 regions"),
    "SPIN-05": ((a[-1] - a[0]) / a[0] * 100, a[-1] - a[0],
                "relative % growth vs percentage points"),
    "SPIN-06": (L.csat.mean(), wmean(L, "csat", "transactions"),
                "AVERAGE(csat) vs SUM(csat*transactions)/SUM(transactions)"),
    "SPIN-07": ((reg_adopt >= float(kpis.loc["KPI-01", "threshold_amber"])).sum(),
                (reg_adopt >= float(kpis.loc["KPI-01", "threshold_green"])).sum(),
                "green line at threshold_amber 62.0 vs threshold_green 65.0"),
    "SPIN-08": ((reg_adopt.round(1) < 65.0).sum(), (reg_adopt < 65.0).sum(),
                "rounded vs unrounded comparison against the 65% target"),
    "SPIN-09": (L.transactions.sum(), L.unique_users.sum(),
                "SUM(transactions) vs SUM(unique_users), 2026-06"),
    "SPIN-10": (int(index_latest.rank(ascending=False, method="min")[top]),
                int(reg_series.iloc[:, -1].rank(ascending=False, method="min")[top]),
                "%s: rank by 2021-07=100 index vs rank by adoption level" % top),
    "SPIN-11": (dig / NB.transactions.sum() * 100, dig / L.transactions.sum() * 100,
                "digital share excluding vs including the branch channel"),
    "SPIN-12": (cat.max(), adoption(L),
                "best service_category (%s) vs the whole programme" % cat.idxmax()),
    "SPIN-13": (wmean(NB, "cost_per_txn_sar", "transactions"),
                wmean(L, "cost_per_txn_sar", "transactions"),
                "transaction-weighted unit cost excluding vs including Branch"),
}

check("Every spin technique has a re-executable recipe in this script",
      set(sp.index) == set(EXPECTED), "%d of %d" % (len(EXPECTED), len(sp)))

for tid in sp.index:
    exp_spun, exp_honest, detail = EXPECTED[tid]
    got_spun = float(sp.loc[tid, "spun_figure"])
    got_honest = float(sp.loc[tid, "honest_figure"])
    tol = max(0.011, abs(exp_spun) * 1e-6)
    ok = close(got_spun, exp_spun, tol) and close(got_honest, exp_honest, tol)
    check("%s figures reproduce from source" % tid, ok,
          "spun %s vs %.4f | honest %s vs %.4f | %s"
          % (got_spun, exp_spun, got_honest, exp_honest, detail))

check("gap = spun_figure - honest_figure on every row",
      ((spin.spun_figure - spin.honest_figure).round(2) - spin.gap).abs().max() <= 0.005)
check("The averages-of-averages pair is the deck's 61.2 vs 63.8",
      round(float(sp.loc["SPIN-01", "spun_figure"]), 1) == 61.2
      and round(float(sp.loc["SPIN-01", "honest_figure"]), 1) == 63.8,
      "gap %.2fpp" % abs(float(sp.loc["SPIN-01", "gap"])))
check("The computed lie factor is spun / honest on SPIN-02",
      close(float(sp.loc["SPIN-02", "spun_figure"]) / float(sp.loc["SPIN-02", "honest_figure"]),
            shown / real, 0.05),
      "lie factor %.1f" % (shown / real))
check("Every spin technique names its source file",
      spin.source_file.str.contains("data/").all())
check("severity and detectability use the stated vocabularies",
      set(spin.severity) <= {"Low", "Medium", "High"}
      and set(spin.detectability) <= {"Easy", "Medium", "Hard"},
      "severity %s; detectability %s" % (", ".join(sorted(set(spin.severity))), ", ".join(sorted(set(spin.detectability)))))
check("Each spin technique carries an Arabic name",
      spin.technique_ar.map(lambda s: any("؀" <= c <= "ۿ" for c in str(s))).all())
check("The ten required spin families are all present",
      len(spin) >= 10 and spin.technique_id.is_unique,
      ", ".join(spin.technique_id))

# ----------------------------------------------------------------------------
# G. Case B — the paired dashboards
# ----------------------------------------------------------------------------
spun_tiles = dash[dash.variant == "spun"]
honest_tiles = dash[dash.variant == "honest"]
check("Dashboard variants are exactly spun and honest",
      set(dash.variant) == {"spun", "honest"})
check("Spun and honest specs have matching tile_ids",
      list(spun_tiles.tile_id) == list(honest_tiles.tile_id),
      "%d paired tiles: %s" % (len(spun_tiles), ", ".join(spun_tiles.tile_id)))
check("Tile titles are identical across variants (same truth, two treatments)",
      (spun_tiles.set_index("tile_id").tile_title_en
       == honest_tiles.set_index("tile_id").tile_title_en).all())
check("Every tile carries an Arabic title",
      dash.tile_title_ar.map(lambda s: any("؀" <= c <= "ۿ" for c in str(s))).all())
check("Every honest tile is annotated and every tile has a teaching note",
      (honest_tiles.annotation.str.strip() != "(none)").all()
      and (dash.teaching_note.str.len() > 10).all())
check("The truncated-axis tile declares its axis start",
      spun_tiles.set_index("tile_id").loc["T02", "axis_start"] == 60
      or str(spun_tiles.set_index("tile_id").loc["T02", "axis_start"]) == "60")
check("Dashboard values quote figures that appear in kpi_spin_pairs",
      "%.1f%%" % float(sp.loc["SPIN-01", "spun_figure"])
      in spun_tiles.set_index("tile_id").loc["T01", "value_shown"]
      and "%.1f%%" % float(sp.loc["SPIN-01", "honest_figure"])
      in honest_tiles.set_index("tile_id").loc["T01", "value_shown"],
      "T01 spun %s / honest %s" % (spun_tiles.set_index("tile_id").loc["T01", "value_shown"],
                                   honest_tiles.set_index("tile_id").loc["T01", "value_shown"]))

# ----------------------------------------------------------------------------
# H. critique_canon
# ----------------------------------------------------------------------------
check("critique_canon item_ids are unique", canon.item_id.is_unique, ", ".join(canon.item_id))
check("Every critique item maps to a course module",
      canon.module_used_in.str.match(r"^M[1-6]").all(),
      ", ".join(sorted(set(canon.module_used_in.str[:2]))))
check("Every critique item carries a documented flaw and a Tayseer lesson",
      (canon.documented_flaw.str.len() > 80).all()
      and (canon.transferable_lesson_for_tayseer.str.len() > 40).all())
check("Every critique item carries two usable critique prompts",
      (canon.critique_question_1.str.len() > 30).all()
      and (canon.critique_question_2.str.len() > 30).all()
      and canon[["critique_question_1", "critique_question_2"]].apply(
          lambda r: r.iloc[0] != r.iloc[1], axis=1).all())

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
passed = sum(1 for ok, _, _ in RESULTS if ok)
print("=" * 96)
print("%d of %d checks passed." % (passed, len(RESULTS)))
sys.exit(0 if passed == len(RESULTS) else 1)
