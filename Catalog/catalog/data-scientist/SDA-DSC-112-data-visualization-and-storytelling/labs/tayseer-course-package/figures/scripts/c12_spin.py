"""Case B — the same truth, two dashboards. Every figure here is reproducible from the shipped CSVs."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sys; sys.path.insert(0,'/home/claude/work/canon')
from canon_style import *
P="/home/claude/work/pkg/"
df = pd.read_csv(P+"data/core/tayseer_services.csv", encoding="utf-8-sig", parse_dates=["month"])
sc = pd.read_csv(P+"data/supporting/regional_scorecard_latest.csv", encoding="utf-8-sig")

def nat(frame):
    return frame.groupby("month").apply(
        lambda x: 100*(x.digital_adoption_pct/100*x.unique_users).sum()/x.unique_users.sum(),
        include_groups=False)
series = nat(df); L = df[df.month == df.month.max()]
weighted, naive = series.iloc[-1], L.digital_adoption_pct.mean()

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.30], wspace=0.34)
axs = fig.add_subplot(gs[0]); axh = fig.add_subplot(gs[1]); axr = fig.add_subplot(gs[2])

# --- the spun tile ---------------------------------------------------------
last13 = series.iloc[-13:]
axs.bar(range(13), last13.values, color=GREEN, width=0.72)
axs.set_ylim(60, 64.6)                       # <- the lie
axs.set_xticks([0, 6, 12]); axs.set_xticklabels(["Jul", "Jan", "Jun"])
axs.set_yticks([60, 62, 64])
axs.set_ylabel("Digital adoption (%)")
despine(axs); axs.grid(axis="y", color=LIGHT, lw=0.6); axs.set_axisbelow(True)
axs.text(0.5, 1.01, "ON TRACK  ·  ADOPTION UP", transform=axs.transAxes, ha="center",
         fontsize=9.5, color=GREEN, fontweight="bold")
axs.text(0.03, 0.90, f"Headline shown: {naive:.1f}%\nAxis starts at 60", transform=axs.transAxes,
         fontsize=8, color=RED, fontweight="bold", va="top", linespacing=1.5)
head(axs, "the success dashboard", "What the committee was shown", RED, dy=0.055)

# --- the honest tile -------------------------------------------------------
axh.bar(range(13), last13.values, color=BLUE, width=0.72)
axh.set_ylim(0, 70); axh.axhline(65, color=ORANGE, lw=1.4, ls="--")
axh.text(12.4, 65.6, "target 65", fontsize=7.5, color=ORANGE, fontweight="bold", ha="right")
axh.set_xticks([0, 6, 12]); axh.set_xticklabels(["Jul", "Jan", "Jun"])
axh.set_ylabel("Digital adoption (%)")
despine(axh); axh.grid(axis="y", color=LIGHT, lw=0.6); axh.set_axisbelow(True)
axh.text(0.5, 1.01, "+1.5 pp IN 12 MONTHS  ·  1.2 pp SHORT", transform=axh.transAxes,
         ha="center", fontsize=9.5, color=NAVY, fontweight="bold")
axh.text(0.04, 0.56, f"Headline shown: {weighted:.1f}%\n(user-weighted,\naxis from zero)", transform=axh.transAxes,
         fontsize=8, color="white", fontweight="bold", va="top", linespacing=1.5)
head(axh, "the same data, the same month", "What the data actually says", dy=0.055)

# --- the distribution the national number hides ---------------------------
d = sc.sort_values("digital_adoption_pct")
cols = [ORANGE if t.startswith("Tier 1") else "#C3CBDB" for t in d.priority_tier]
axr.barh(range(len(d)), d.digital_adoption_pct, color=cols, height=0.72)
axr.set_yticks(range(len(d))); axr.set_yticklabels(d.region, fontsize=7.6)
axr.axvline(65, color=ORANGE, lw=1.4, ls="--")
axr.axvline(weighted, color=NAVY, lw=1.4)
axr.text(weighted-0.8, 13.1, f"national\n{weighted:.1f}%", fontsize=7.4, color=NAVY,
         fontweight="bold", ha="right", va="top", linespacing=1.4)
axr.text(65.8, 13.1, "target\n65", fontsize=7.4, color=ORANGE, fontweight="bold", va="top", linespacing=1.4)
axr.set_xlim(0, 82); axr.set_xlabel("Digital adoption (%), latest month")
despine(axr, keep=("bottom",)); axr.tick_params(axis="y", length=0)
axr.grid(axis="x", color=LIGHT, lw=0.6); axr.set_axisbelow(True)
below = int((d.digital_adoption_pct < 65).sum())
axr.text(0.02, 0.06, f"{below} of 13 regions sit below the target.\nNo single national number can say that.",
         transform=axr.transAxes, fontsize=8, color=INK, ha="left", va="bottom", linespacing=1.5)
head(axr, "why one number is never the answer", "The distribution behind the headline", ORANGE, dy=0.055)

footnote(fig, f"All three panels use the same month of tayseer_services.csv. The spun headline {naive:.2f}% is AVERAGE(digital_adoption_pct) — "
              f"the averages-of-averages bug; the honest {weighted:.2f}% recomputes from components weighted by unique_users. "
              "The left panel's zero-suppressed axis is not a style preference: a bar encodes length from zero, so truncating it changes the quantity the mark represents. "
              "Thirteen such techniques, each with the exact operation that produces it and the figure it yields, ship in kpi_spin_pairs.csv; the tile-by-tile pair is in success_dashboard_spec.csv.")
fig.subplots_adjust(top=0.78, bottom=0.14, left=0.055, right=0.99)
save(fig, "case_b_spin_vs_honest")
