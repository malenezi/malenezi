"""Explanation for a control room that distrusts black boxes."""
from __future__ import annotations
import numpy as np, pandas as pd


def importance_by_family(imp: pd.DataFrame) -> pd.DataFrame:
    """Roll feature gains up into the families taught in Module 4."""
    def fam(f):
        if "_lag" in f and f.startswith("demand"): return "lag"
        if "_r" in f and f.startswith("demand"):  return "rolling"
        if f.startswith(("d_", "w_", "y_")):      return "fourier"
        if f in ("cdd", "hdd", "temp_c", "temp_lag24"): return "weather"
        return "calendar"
    out = imp.copy()
    out["family"] = out["feature"].map(fam)
    return (out.groupby("family")["gain"].sum()
              .pipe(lambda s: (s / s.sum() * 100).round(1))
              .sort_values(ascending=False).rename("share_%").reset_index())
