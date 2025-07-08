import pandas as pd
from pathlib import Path
from datetime import datetime

SIGNALS = Path("signal_logs")
PERF = Path("performance_logs")
AUDIT_LOG = Path("memory/strategy_audit.csv")

def audit_strategies():
    print("📋 Auditing strategy consistency...")

    s_df = pd.concat([pd.read_csv(f) for f in SIGNALS.glob("signals_*.csv")])
    p_df = pd.concat([pd.read_csv(f) for f in PERF.glob("performance_*.csv")])

    s_df["date"] = pd.to_datetime(s_df["date"])
    p_df["date"] = pd.to_datetime(p_df["date"])
    merged = s_df.merge(p_df, on=["date", "strategy"])

    results = merged.groupby("strategy").agg({
        "confidence": "mean",
        "pnl": ["mean", "std", "count"]
    }).reset_index()
    results.columns = ["strategy", "conf", "avg_pnl", "vol", "count"]
    results["sharpe"] = results["avg_pnl"] / results["vol"].replace(0, 1e-6)

    results.to_csv(AUDIT_LOG, index=False)
    print("✅ Audit saved:", AUDIT_LOG)