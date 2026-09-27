"""NYT excess deaths — the visual is trivial; the argument is the baseline."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from canon_style import *

d = pd.read_csv("nytimes_covid-19-data_master_excess-deaths_deaths.csv")
d = d[(d.country == "United States") & (d.placename.isna()) & (d.frequency == "weekly")].copy()
d["start_date"] = pd.to_datetime(d.start_date)
d = d[d.start_date <= "2020-07-25"].sort_values("start_date")

fig, (axa, axb) = plt.subplots(1, 2, figsize=(W, H), gridspec_kw={"width_ratios":[1.35,1], "wspace":0.24})

x = d.start_date
axa.plot(x, d.expected_deaths, color=GREY, lw=1.5, ls="--", label="Expected — the baseline model")
axa.plot(x, d.deaths, color=NAVY, lw=1.9, label="Deaths actually recorded, all causes")
axa.fill_between(x, d.expected_deaths, d.deaths, where=d.deaths > d.expected_deaths,
                 color=ORANGE, alpha=0.35, lw=0, label="Excess")
m = d[d.start_date >= "2020-03-01"]
tot = int((m.deaths - m.expected_deaths).clip(lower=0).sum())
axa.annotate(f"{tot:,} deaths above the baseline since March —\nthe toll that confirmed counts were missing",
             xy=(pd.Timestamp("2020-04-11"), 72000), xytext=(pd.Timestamp("2020-04-25"), 77500),
             fontsize=8.5, color=ORANGE, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.1))
axa.set_ylabel("Deaths per week, all causes, United States")
axa.set_ylim(50000, 82000)
axa.legend(fontsize=8, loc="upper left")
despine(axa); axa.grid(axis="y", color=LIGHT, lw=0.6); axa.set_axisbelow(True)
import matplotlib.dates as mdates
axa.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
head(axa, "a line, a dashed line, a shaded band", "The chart itself is trivial to draw", dy=0.03)

# ---- panel B: the same picture, five defensible baselines ---------------
shifts = [-0.05, -0.02, 0.0, 0.02, 0.05]
totals = [int(((m.deaths - m.expected_deaths * (1 + s)).clip(lower=0)).sum()) for s in shifts]
cols = [MUTED, "#B7C0D3", ORANGE, "#B7C0D3", MUTED]
bars = axb.bar([f"{s:+.0%}" if s else "as\npublished" for s in shifts], totals, color=cols, width=0.62)
for b, t in zip(bars, totals):
    axb.text(b.get_x()+b.get_width()/2, t + 3000, f"{t/1000:.0f}k", ha="center",
             fontsize=8.5, color=NAVY, fontweight="bold")
axb.set_xlabel("Shift applied to the expected-deaths baseline")
axb.set_ylabel("Excess deaths, March – July 2020")
axb.set_ylim(0, max(totals)*1.20)
axb.set_yticks([0, 100000, 200000, 300000]); axb.set_yticklabels(["0", "100k", "200k", "300k"])
despine(axb); axb.grid(axis="y", color=LIGHT, lw=0.6); axb.set_axisbelow(True)
spread = (max(totals)-min(totals))/1000
axb.text(0.5, -0.30, f"A ±5% move in a baseline nobody sees swings the headline by {spread:.0f},000 deaths.\n"
                     "NYT's own caveat: the expected count is NOT adjusted for how\nnon-Covid deaths may themselves have changed during the outbreak.",
         transform=axb.transAxes, fontsize=8, color=INK, ha="center", va="top", linespacing=1.5)
head(axb, "the hard part is upstream of the chart", "The counterfactual you chose to draw", ORANGE, dy=0.03)

footnote(fig, "Built from the New York Times excess-deaths dataset (github.com/nytimes/covid-19-data/excess-deaths, CC BY-NC 4.0; the series is archived — collection stopped 24 March 2023). "
              "NYT's method: a linear model fitted to roughly 2015–2019 mortality, with a linear time trend for demographic change plus a smoothing spline for seasonality. "
              "Teaching point: a reader who accepts the picture has already accepted the baseline — and the baseline is an argument, not a measurement.")
fig.subplots_adjust(top=0.82, bottom=0.26, left=0.05, right=0.995)
save(fig, "canon_07_excess_deaths")
