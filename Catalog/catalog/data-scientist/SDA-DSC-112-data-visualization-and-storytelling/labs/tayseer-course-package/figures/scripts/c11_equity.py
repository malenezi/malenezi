"""Case C — regional service inequality: the same regions, ranked two ways."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sys; sys.path.insert(0,'/home/claude/work/canon')
from canon_style import *
P="/home/claude/work/pkg/"
eq = pd.read_csv(P+"data/supporting/regional_equity_latest.csv", encoding="utf-8-sig")
lz = pd.read_csv(P+"data/supporting/regional_equity_lorenz.csv", encoding="utf-8-sig")

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 1.15, 1.0], wspace=0.55)
ax1 = fig.add_subplot(gs[0]); ax2 = fig.add_subplot(gs[1]); ax3 = fig.add_subplot(gs[2])
T1 = eq.priority_tier.str.startswith("Tier 1")

def hbar(ax, col, title, kick, kcol, fmt):
    d = eq.sort_values(col)
    cols = [ORANGE if t else "#C3CBDB" for t in T1.loc[d.index]]
    ax.barh(range(len(d)), d[col], color=cols, height=0.72)
    ax.set_yticks(range(len(d))); ax.set_yticklabels(d.region, fontsize=7.6)
    for i, v in enumerate(d[col]):
        ax.text(v*1.015, i, fmt.format(v), va="center", fontsize=7, color=GREY)
    ax.set_xlim(0, d[col].max()*1.30)
    despine(ax, keep=("bottom",)); ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=LIGHT, lw=0.6); ax.set_axisbelow(True)
    head(ax, kick, title, kcol, dy=0.02)
    return d

hbar(ax1, "monthly_digital_transactions", "Ranked by volume", "the map a raw-count choropleth draws", GREY, "{:,.0f}")
ax1.set_xticks([0, 1e6, 2e6, 3e6]); ax1.set_xticklabels(["0", "1m", "2m", "3m"])
hbar(ax2, "digital_txn_per_1k_pop", "Ranked per 1,000 residents", "the same month, divided by population", ORANGE, "{:.0f}")

nat = eq.monthly_digital_transactions.sum()/eq.population_2025.sum()*1000
ax2.axvline(nat, color=NAVY, lw=1.3, ls="--")
ax2.text(nat, len(eq)-0.2, f" national {nat:.0f}", fontsize=7.2, color=NAVY, fontweight="bold", va="top")

# Lorenz
ax3.plot([0,1],[0,1], color=LIGHT, lw=1.4, ls="--")
x = np.concatenate([[0], lz.cum_population_share.values])
y = np.concatenate([[0], lz.cum_digital_txn_share.values])
ax3.plot(x, y, color=TEAL, lw=2.2)
ax3.fill_between(x, y, x, color=TEAL, alpha=0.12)
gini = 1 - np.sum((x[1:]-x[:-1])*(y[1:]+y[:-1]))
ax3.set_xlabel("Cumulative share of population"); ax3.set_ylabel("Cumulative share of digital transactions")
ax3.set_xlim(0,1); ax3.set_ylim(0,1); ax3.set_aspect("equal")
despine(ax3); ax3.grid(color=LIGHT, lw=0.6); ax3.set_axisbelow(True)
ax3.text(0.05, 0.90, f"Gini = {gini:.3f}", fontsize=10, color=NAVY, fontweight="bold", transform=ax3.transAxes)
ax3.text(0.04, 0.76, "Volume is spread almost evenly,\nso the Lorenz curve hugs the\ndiagonal. The inequality in this\nprogramme is in the LEVEL of\nadoption, not the share of\ntransactions — which is why this\nis the wrong chart for the ask.",
         fontsize=7.2, color=INK, transform=ax3.transAxes, va="top", linespacing=1.5,
         bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=2))
head(ax3, "and the chart that answers a different question", "Lorenz curve", PURPLE, dy=0.02)

dn = eq.loc[(eq.rank_by_per_capita - eq.rank_by_raw_volume).idxmax()]
up = eq.loc[(eq.rank_by_raw_volume - eq.rank_by_per_capita).idxmax()]
footnote(fig, f"Computed from tayseer_services.csv and dim_regions.csv for the latest month; orange marks the five Tier-1 regions. "
              f"The ranking inverts: {dn.region} is #{int(dn.rank_by_raw_volume)} of 13 by raw digital volume and #{int(dn.rank_by_per_capita)} per capita, "
              f"while {up.region} moves from #{int(up.rank_by_raw_volume)} to #{int(up.rank_by_per_capita)}. "
              "The raw-count chart is not wrong — it answers 'where is the work?'. It is simply not the chart for 'who is underserved?'. "
              "Normalise before you rank, and put the denominator in the subtitle.")
fig.subplots_adjust(top=0.80, bottom=0.15, left=0.085, right=0.99)
save(fig, "case_c_equity")
