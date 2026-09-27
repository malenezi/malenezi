"""The reserve brief: the forecast, in the language of the decision."""
from __future__ import annotations
import pandas as pd

TEMPLATE = """RESERVE BRIEF — Tayyar day-ahead load forecast
Issued {issued} for the 24 hours beginning {start} (Central Operating Area)

  Expected peak demand      {peak:,.0f} MW at {peak_hour}
  90% upper bound (p95)     {p95:,.0f} MW
  Recommended spinning reserve  {reserve:,.0f} MW
      = p95 peak minus expected peak, i.e. the demand we would need to cover
        if tomorrow lands at the top of the interval.

  Confidence: over the last {n_origins} backtested days this interval contained
  the actual demand {coverage:.0%} of the time (target 90%).

  Where this forecast is weakest: {weakness}
  Fallback if it fails: {fallback}
"""


def reserve_brief(fc: pd.DataFrame, coverage: float, n_origins: int,
                  weakness: str, fallback: str, issued=None) -> str:
    peak_i = fc["q50"].idxmax()
    return TEMPLATE.format(
        issued=issued or pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
        start=fc.index[0], peak=fc.loc[peak_i, "q50"],
        peak_hour=str(peak_i), p95=fc["q95"].max(),
        reserve=fc["q95"].max() - fc.loc[peak_i, "q50"],
        n_origins=n_origins, coverage=coverage,
        weakness=weakness, fallback=fallback)
