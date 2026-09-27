"""1854 Broad Street — Snow's dot map recreated from HistData (Dodson/Tobler digitisation),
   paired with Snow's own daily table, which is the critique quantified."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from canon_style import *

streets = pd.read_csv("Snow.streets.csv")
deaths  = pd.read_csv("Snow.deaths.csv")
pumps   = pd.read_csv("Snow.pumps.csv")
dates   = pd.read_csv("Snow.dates.csv", parse_dates=["date"])

fig, (axm, axd) = plt.subplots(1, 2, figsize=(W, H), gridspec_kw={"width_ratios":[1.0,1.45]})

# ---- LEFT: the map -------------------------------------------------------
for _, seg in streets.groupby("street"):
    axm.plot(seg.x, seg.y, color="#B9C2D4", lw=0.9, solid_capstyle="round", zorder=1)
axm.scatter(deaths.x, deaths.y, s=7, color=NAVY, marker="s", lw=0, zorder=3)
other = pumps[pumps.pump != 7]
axm.scatter(other.x, other.y, s=52, facecolor="white", edgecolor=GREY, lw=1.2, zorder=4)
bs = pumps[pumps.pump == 7]
axm.scatter(bs.x, bs.y, s=150, facecolor=ORANGE, edgecolor="white", lw=1.6, zorder=5)
axm.annotate("Broad Street\npump", xy=(bs.x.iloc[0], bs.y.iloc[0]), xytext=(4.4, 12.6),
             fontsize=9, fontweight="bold", color=ORANGE, ha="left", va="center",
             arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.1,
                             connectionstyle="angle3,angleA=0,angleB=70"))
axm.text(4.4, 19.4, "578 deaths,\none mark each,\nstacked at the\nvictim's address",
         fontsize=8, color=INK, ha="left", va="top")
axm.text(4.4, 6.4, "12 other\npublic pumps", fontsize=8, color=GREY, va="top")
fit_equal(axm, (6.5, 20.2), (3.5, 20.5), 4.0/3.35)
axm.set_xticks([]); axm.set_yticks([]); despine(axm, keep=())
head(axm, "1  ·  the map everyone knows", "Snow, Soho, 1854 — deaths cluster on one pump")

# ---- RIGHT: the table nobody shows --------------------------------------
d = dates.dropna(subset=["date"])
axd.bar(d.date, d.attacks, width=0.85, color=LIGHT, label="Attacks")
axd.plot(d.date, d.deaths, color=NAVY, lw=1.8, label="Deaths")
peak = d.loc[d.attacks.idxmax()]
removal = pd.Timestamp("1854-09-08")
axd.axvline(removal, color=ORANGE, lw=1.4, ls="--")
axd.annotate("Handle removed, 8 Sept\nattacks already down\n143 → 12 per day",
             xy=(removal, 118), xytext=(removal + pd.Timedelta(days=2.5), 120),
             fontsize=8.5, color=ORANGE, fontweight="bold", va="top",
             arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.0))
axd.annotate(f"Peak {int(peak.attacks)} attacks\n1 September",
             xy=(peak.date, peak.attacks), xytext=(peak.date - pd.Timedelta(days=11), 132),
             fontsize=8.5, color=NAVY, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=NAVY, lw=1.0))
axd.set_ylim(0, 150); axd.set_ylabel("Cases per day")
axd.legend(loc="upper right", fontsize=8)
despine(axd)
axd.grid(axis="y", color=LIGHT, lw=0.6); axd.set_axisbelow(True)
import matplotlib.dates as mdates
axd.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
head(axd, "2  ·  the data that complicates it", "Snow's own daily table, 19 Aug – 30 Sept 1854", ORANGE)

footnote(fig,
    "Recreated from HistData (Snow.deaths / Snow.streets / Snow.pumps / Snow.dates — Dodson & Tobler digitisation of Snow's 1855 map; coordinates in 100 m units).  "
    "616 deaths in total.  The map was drawn AFTER the outbreak and shown in Dec 1854; it persuaded nobody at the time — and it carries no population denominator, "
    "while three quarters of residents had fled.")
fig.tight_layout(w_pad=2.6, rect=(0,0,1,0.88))
save(fig, "canon_01_snow")
