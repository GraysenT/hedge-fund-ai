import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from simulation.stress_presets import get_stress_factor

PERF_LOG = Path("performance_logs")
OUTPUT = Path("reports/stress_test_results.csv")

def simulate_stress(preset="Mild_Correction"):
    print(f"📉 Running stress test using preset: {preset}")
    factor_drop = get_stress_factor(preset)

    # Load all performance logs
    files = list(PERF_LOG.glob("performance_*.csv"))
    if not files:
        print("🛑 No performance logs found.")
        return

    df = pd.concat([pd.read_csv(f) for f in files])
    df["date"] = pd.to_datetime(df["date"])

    # Simulate drawdown by reducing PnL
    df["stressed_pnl"] = df["pnl"] - abs(df["pnl"]) * factor_drop
    df["stressed_balance"] = df.groupby("strategy")["stressed_pnl"].cumsum()

    # Summarize
    summary = df.groupby("strategy")[["pnl", "stressed_pnl"]].sum()
    summary["drawdown"] = (summary["pnl"] - summary["stressed_pnl"]) / summary["pnl"].replace(0, 1e-6)
    summary["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    summary["preset"] = preset

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT)

    print(f"✅ Stress test complete: saved to {OUTPUT}")