import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

PERF_LOG = Path("performance_logs")

def load_strategy_returns():
    files = list(PERF_LOG.glob("performance_*.csv"))
    if not files:
        return pd.DataFrame()

    df = pd.concat([pd.read_csv(f) for f in files])
    df["date"] = pd.to_datetime(df["date"])
    pivot = df.pivot(index="date", columns="strategy", values="pnl").fillna(0)
    returns = pivot.pct_change().dropna()
    return returns

def mean_variance_optimizer(returns_df):
    if returns_df.empty:
        return {}

    mu = returns_df.mean()
    cov = returns_df.cov()
    inv_cov = np.linalg.pinv(cov.values)
    weights = inv_cov.dot(mu.values)
    weights = np.maximum(weights, 0)
    weights /= weights.sum() + 1e-6

    return dict(zip(returns_df.columns, weights.round(4)))

def save_optimal_weights(weight_dict):
    ts = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    path = Path("memory/optimized_weights.csv")
    pd.DataFrame(list(weight_dict.items()), columns=["strategy", "weight"]).to_csv(path, index=False)
    print(f"✅ Saved optimized weights to {path}")