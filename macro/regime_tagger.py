import pandas as pd
from pathlib import Path

def tag_regimes(perf_df: pd.DataFrame):
    """
    Tags each row of a performance DataFrame with a simple regime label.
    Extendable to macro/econ indicators.
    """
    perf_df["regime"] = "neutral"
    perf_df.loc[perf_df["pnl"] > 100, "regime"] = "bull"
    perf_df.loc[perf_df["pnl"] < -100, "regime"] = "bear"
    return perf_df