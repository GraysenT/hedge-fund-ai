import pandas as pd
from pathlib import Path

def calculate_risk_budget(weights: dict, perf_df: pd.DataFrame):
    vol = perf_df.groupby("strategy")["pnl"].std().to_dict()
    adjusted = {}

    for strat, weight in weights.items():
        risk = vol.get(strat, 1e-6)
        adjusted[strat] = weight / (risk + 1e-6)

    total = sum(adjusted.values())
    return {k: round(v / total, 4) for k, v in adjusted.items()}