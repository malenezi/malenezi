"""'An Incalculable Loss', NYT front page, 24 May 2020 — the case for NOT making a chart."""
import numpy as np, matplotlib.pyplot as plt
from canon_style import *

fig, (axa, axb) = plt.subplots(1, 2, figsize=(W, H), gridspec_kw={"wspace": 0.14})

# ---- A: 100,000 marks ----------------------------------------------------
rng = np.random.default_rng(5)
cols, rows = 500, 200
xs, ys = np.meshgrid(np.arange(cols), np.arange(rows))
axa.scatter(xs.ravel(), ys.ravel(), s=0.35, c="#AEB8D0", lw=0, marker="s")
axa.set_xlim(-6, cols+5); axa.set_ylim(-8, rows+6); axa.invert_yaxis()
axa.set_xticks([]); axa.set_yticks([]); despine(axa, keep=())
axa.text(0.5, -0.06, "100,000 marks. One per death. You feel nothing.",
         transform=axa.transAxes, fontsize=9, color=GREY, ha="center")
head(axa, "the aggregate", "What a chart of 100,000 deaths looks like", GREY, dy=0.06)

# ---- B: what the Times printed instead ----------------------------------
axb.set_xlim(0, 1); axb.set_ylim(0, 1); axb.axis("off")
axb.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96, facecolor="#FCFCFA",
                            edgecolor="#CBD2E0", lw=1.0))
axb.text(0.5, 0.935, "U.S. DEATHS NEAR 100,000, AN INCALCULABLE LOSS",
         fontsize=10.5, color="#222222", fontweight="bold", ha="center", family="Liberation Serif")
axb.text(0.5, 0.885, "They Were Not Simply Names on a List. They Were Us.",
         fontsize=8, color="#555555", ha="center", style="italic", family="Liberation Serif")
axb.plot([0.06, 0.94], [0.862, 0.862], color="#999999", lw=0.7)
lines = [
    "one of the world's great harmonica players  ·  loved the sound of a train whistle  ·",
    "taught generations of schoolchildren to read  ·  a retired police sergeant who cooked",
    "for the whole street  ·  she could recite every capital city  ·  never missed a Friday",
    "prayer  ·  he built the family house with his own hands  ·  a nurse of thirty-one years  ·",
    "always the first to arrive and the last to leave  ·  a grandmother of nineteen  ·  he",
    "grew tomatoes on a balcony  ·  she sang in the choir for four decades  ·  a bus driver",
    "who knew every passenger by name  ·  loved crosswords and bad puns  ·  she walked",
    "her neighbour's dog every morning for eleven years  ·  a father who never raised his",
    "voice  ·  the best baker on the block  ·  he wrote letters, not emails  ·  she kept every",
    "school report her children ever brought home  ·  a mechanic who fixed anything  ·",
]
for i, ln in enumerate(lines):
    axb.text(0.065, 0.805 - i*0.052, ln, fontsize=6.4, color="#333333",
             family="Liberation Serif", va="top")
axb.text(0.5, 0.235, "…and 99,980 more", fontsize=8, color="#666666",
         ha="center", family="Liberation Serif", style="italic")
axb.text(0.5, 0.13, "One thousand names filled the entire front page.\nNo chart. No axis. No aggregation.",
         fontsize=8.5, color=INK, ha="center", linespacing=1.6)
head(axb, "the refusal to aggregate", "What the Times printed instead, 24 May 2020", ORANGE, dy=0.06)

footnote(fig, "Right panel is an ILLUSTRATIVE MOCK-UP in the spirit of the original front page — the phrases are invented, not the Times' text, and no real person is represented. "
              "The original (led by Simone Landon, names compiled by Alain Delaquérière) set 1,000 names and one-line obituary fragments as continuous type across the whole front page, to 'convey the vastness and variety of the tragedies by personalizing them, countering data fatigue'. "
              "Pair it with the excess-deaths line chart: the same event, one rendered as a quantity and one as a thousand people. Knowing which job you are doing is the whole skill.")
fig.subplots_adjust(top=0.80, bottom=0.10, left=0.02, right=0.98)
save(fig, "canon_10_incalculable_loss")
