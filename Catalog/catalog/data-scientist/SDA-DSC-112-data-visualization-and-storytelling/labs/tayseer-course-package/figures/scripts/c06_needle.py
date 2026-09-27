"""The New York Times election needle, 2016 — what the jitter actually encoded."""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
from canon_style import *

rng = np.random.default_rng(7)
sims = rng.normal(0.71, 0.135, 200000); sims = sims[(sims > 0.02) & (sims < 0.99)][:40000]
q25, q75 = np.quantile(sims, [0.25, 0.75]); med = np.median(sims)

def perlin(n, seed, octaves=4):
    r = np.random.default_rng(seed); t = np.linspace(0, 1, n); out = np.zeros(n)
    for o in range(octaves):
        f, a = 2 ** o, 0.5 ** o
        k = np.sort(r.random(f + 2)); v = r.random(f + 2) * 2 - 1
        out += a * np.interp(t, np.linspace(0, 1, len(k)), v)
    return out / np.abs(out).max()

fig = plt.figure(figsize=(W, H))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1], wspace=0.22)
gl = gs[0].subgridspec(1, 4, wspace=0.10)
axd = fig.add_subplot(gs[1])

# ---- LEFT: four sampled frames of the gauge -----------------------------
noise = perlin(4000, 11)
frames = [400, 1500, 2600, 3700]
for i, fr in enumerate(frames):
    ax = fig.add_subplot(gl[i]); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.10, 1.10); ax.set_ylim(-0.40, 1.14)
    ax.add_patch(Wedge((0, 0), 1.0, 90, 180, width=0.22, facecolor="#DCE3F0", lw=0))
    ax.add_patch(Wedge((0, 0), 1.0, 0, 90, width=0.22, facecolor="#F3D7C4", lw=0))
    # the needle sweeps only between the 25th and 75th percentile of the simulations
    p = q25 + (q75 - q25) * (noise[fr] * 0.5 + 0.5)
    ang = np.pi * (1 - p)
    ax.plot([0, 0.86 * np.cos(ang)], [0, 0.86 * np.sin(ang)], color=NAVY, lw=2.6,
            solid_capstyle="round", zorder=4)
    ax.add_patch(Circle((0, 0), 0.055, facecolor=NAVY, lw=0, zorder=5))
    ax.text(-1.02, -0.14, "TRUMP", fontsize=6.5, color="#C06A34", fontweight="bold")
    ax.text(1.02, -0.14, "CLINTON", fontsize=6.5, color=BLUE, fontweight="bold", ha="right")
    ax.text(0, 1.07, f"frame {i+1}", fontsize=7, color=GREY, ha="center")
    if i == 0:
        ax.text(0, -0.21, "The needle never left the interquartile range —\n"
                          "but every viewer read the wobble as news arriving.",
                fontsize=8, color=INK, ha="left", va="top", transform=ax.transAxes)

# ---- RIGHT: the distribution the needle was sampling --------------------
axd.hist(sims * 100, bins=70, color="#DCE3F0", lw=0)
axd.axvspan(q25 * 100, q75 * 100, color=TEAL, alpha=0.16, zorder=1)
axd.axvline(med * 100, color=NAVY, lw=2.0)
axd.annotate(f"Median forecast {med*100:.0f}%", xy=(med*100, 1290), xytext=(med*100-40, 1620),
             fontsize=8.5, color=NAVY, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=NAVY, lw=1.0))
axd.annotate(f"Needle range = 25th–75th percentile\n({q25*100:.0f}% to {q75*100:.0f}%), moved by Perlin noise\nso it looked organic, not mechanical",
             xy=(q75*100, 620), xytext=(3, 1130), fontsize=8.5, color=TEAL, fontweight="bold",
             arrowprops=dict(arrowstyle="-", color=TEAL, lw=1.1))
axd.set_xlabel("Simulated probability of a Clinton win (%)")
axd.set_ylabel("Simulations"); axd.set_xlim(0, 100); axd.set_ylim(0, 1850)
despine(axd); axd.grid(axis="y", color=LIGHT, lw=0.6); axd.set_axisbelow(True)
head(axd, "…and what it was sampling from", "The forecast distribution behind the gauge", ORANGE, dy=0.03)

fig.text(0.008, 0.965, "8 NOVEMBER 2016  ·  THE JITTER WAS THE UNCERTAINTY",
         fontsize=7.5, color=TEAL, fontweight="bold")
fig.text(0.008, 0.900, "What millions of people watched…", fontsize=11.5, color=NAVY, fontweight="bold")
footnote(fig, "A reconstruction of the MECHANIC, not of that night's numbers: the simulated distribution here is illustrative. "
              "The mechanic is as Gregor Aisch documented it — the needle's travel was bounded by the 25th and 75th percentile of the model's simulations, driven by Perlin noise, and the amplitude narrowed as the forecast tightened. "
              "It is a Hypothetical Outcome Plot in gauge clothing (Hullman, Resnick & Adar, PLOS ONE 2015). "
              "The failure was the metaphor: real gauges do not jitter, so viewers read the wobble as malfunction or as live returns — and the piece carried no static annotation saying what it was doing.")
fig.subplots_adjust(top=0.80, bottom=0.13, left=0.015, right=0.995)
save(fig, "canon_06_nyt_needle")
