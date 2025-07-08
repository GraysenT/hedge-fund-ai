import pandas as pd
from pathlib import Path
from datetime import datetime

TRADE_LOG = Path("execution_logs/stat_arb_trades.csv")
MEMORY_LOG = Path("memory/stat_arb_performance.csv")

def update_stat_arb_memory():
    if not TRADE_LOG.exists():
        print("🟡 No stat arb trades to process.")
        return

    df = pd.read_csv(TRADE_LOG)
    if df.empty:
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    # Basic performance label: assume profit if zscore reverted to 0 (placeholder)
    df["outcome"] = df["zscore"].apply(lambda z: "success" if abs(z) < 1.0 else "fail")

    memory_df = df.groupby(["pair", "outcome"]).size().unstack(fill_value=0)
    memory_df["success_rate"] = memory_df["success"] / (memory_df.sum(axis=1) + 1e-6)

    memory_df.to_csv(MEMORY_LOG)
    print(f"✅ Stat arb memory updated: {MEMORY_LOG}")
    