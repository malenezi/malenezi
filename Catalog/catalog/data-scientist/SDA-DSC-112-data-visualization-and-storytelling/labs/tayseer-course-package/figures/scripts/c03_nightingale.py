"""Nightingale 1858 — the rose, area-encoded and superimposed from a common vertex,
   beside her own 'Lines' diagram of the same rates."""
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from canon_style import *

ng = pd.read_csv("Nightingale.csv", parse_dates=["Date"])
p1 = ng[ng.Date < "1855-04-01"]     # Apr 1854 - Mar 1855, before the Sanitary Commission
p2 = ng[ng.Date >= "1855-04-01"]    # Apr 1855 - Mar 1856, after
BLUE_N, RED_N, BLACK_N = "#6E9BC5", "#C0504D", "#3B3B3B"

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.75], wspace=0.30)
ax1 = fig.add_subplot(gs[0], projection="polar")
ax2 = fig.add_subplot(gs[1], projection="polar")
axl = fig.add_subplot(gs[2])

RMAX = np.sqrt(ng[["Disease.rate", "Wounds.rate", "Other.rate"]].values.max())

def rose(ax, d, title):
    n = len(d); theta = np.linspace(0, 2*np.pi, n, endpoint=False); width = 2*np.pi/n
    # superimposed from the common centre, NOT stacked; radius = sqrt(rate) so AREA = rate
    for col, colour, z in (("Disease.rate", BLUE_N, 1), ("Other.rate", BLACK_N, 2), ("Wounds.rate", RED_N, 3)):
        ax.bar(theta, np.sqrt(d[col].values), width=width, bottom=0.0,
               color=colour, edgecolor="white", lw=0.5, align="edge", zorder=z, alpha=0.95)
    ax.set_theta_zero_location("N"); ax.set_theta_direction(1)
    ax.set_ylim(0, RMAX*1.02); ax.set_yticklabels([]); ax.set_yticks([])
    ax.set_xticks(theta + width/2)
    ax.set_xticklabels(list(d.Month), fontsize=6.0, color=GREY)
    ax.grid(color=LIGHT, lw=0.5); ax.spines["polar"].set_visible(False)
    ax.set_title(title, fontsize=9, color=NAVY, fontweight="bold", pad=12)

rose(ax1, p2, "Apr 1855 – Mar 1856\nafter the Sanitary Commission")
rose(ax2, p1, "Apr 1854 – Mar 1855\nbefore")

axl.plot(ng.Date, ng["Disease.rate"], color=BLUE_N, lw=2.2, label="Preventible disease")
axl.plot(ng.Date, ng["Wounds.rate"],  color=RED_N,  lw=1.6, label="Wounds")
axl.plot(ng.Date, ng["Other.rate"],   color=BLACK_N, lw=1.6, label="All other causes")
axl.axvline(pd.Timestamp("1855-03-15"), color=ORANGE, lw=1.4, ls="--")
axl.annotate("Sanitary Commission\narrives at Scutari, Mar 1855",
             xy=(pd.Timestamp("1855-03-15"), 520), xytext=(pd.Timestamp("1855-04-20"), 700),
             fontsize=8, color=ORANGE, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.0))
peak = ng.loc[ng["Disease.rate"].idxmax()]
axl.annotate("Jan 1855: 1,022.8 per 1,000 per year\n— an annual rate above the whole force",
             xy=(peak.Date, peak["Disease.rate"]), xytext=(pd.Timestamp("1854-04-20"), 1005),
             fontsize=8.5, color=NAVY, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=NAVY, lw=1.0))
axl.set_ylabel("Annual deaths per 1,000")
axl.legend(loc=(0.60, 0.42), fontsize=8)
despine(axl); axl.grid(axis="y", color=LIGHT, lw=0.6); axl.set_axisbelow(True)
axl.set_ylim(0, 1180)
head(axl, "the same numbers, read accurately", "…and her own 'Lines' diagram of the identical rates", ORANGE, dy=0.02)

fig.text(0.008, 0.965, "1858  ·  DIAGRAM OF THE CAUSES OF MORTALITY IN THE ARMY IN THE EAST",
         fontsize=7.5, color=TEAL, fontweight="bold")
fig.text(0.008, 0.905, "Nightingale's rose — and the chart that reads better",
         fontsize=11.5, color=NAVY, fontweight="bold")
footnote(fig, "Recreated from HistData::Nightingale (24 months; rate = 12 × 1000 × deaths ÷ army).  "
              "Drawn the way Nightingale drew it: wedges SUPERIMPOSED from the common centre — not stacked — with radius = √rate so that AREA is proportional to rate.  "
              "The area-vs-radius error belongs to her earlier 1858 'bat's wing'; she spotted it, issued an erratum and replaced it with this. "
              "The fair critique is that area sits low on the Cleveland–McGill ranking, so the rose exaggerates at the extremes — and Hugh Small argues the Lines diagram was probably the more influential of the two.")
fig.subplots_adjust(top=0.80, bottom=0.06, left=0.015, right=0.99)
save(fig, "canon_03_nightingale")
