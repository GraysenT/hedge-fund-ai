import pandas as pd
from pathlib import Path

SIGNAL_DIR = Path("signal_logs")
PERF_DIR = Path("performance_logs")

def run_replay():
    signals = pd.concat([pd.read_csv(f) for f in SIGNAL_DIR.glob("signals_*.csv")])
    perf = pd.concat([pd.read_csv(f) for f in PERF_DIR.glob("performance_*.csv")])

    merged = signals.merge(perf, on=["date", "strategy"], how="inner")
    merged["cumulative_pnl"] = merged.groupby("strategy")["pnl"].cumsum()

    report = merged.groupby("strategy")[["pnl", "confidence", "cumulative_pnl"]].agg(["mean", "sum", "count"])
    report.to_csv("reports/replay_simulation_summary.csv")
    print("🎮 Simulation replay complete.")