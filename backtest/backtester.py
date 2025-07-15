import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

SIGNAL_DIR = Path("signal_logs")
PERF_LOG = Path("performance_logs")

def load_signals():
    files = list(SIGNAL_DIR.glob("signals_*.csv"))
    if not files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def load_performance():
    files = list(PERF_LOG.glob("performance_*.csv"))
    if not files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def run_backtest():
    print("🧪 Running historical signal backtest...")

    signals = load_signals()
    perf = load_performance()

    if signals.empty or perf.empty:
        print("🚫 No data available.")
        return None

    signals["date"] = pd.to_datetime(signals["date"])
    perf["date"] = pd.to_datetime(perf["date"])

    merged = signals.merge(perf, on=["date", "strategy"], how="inner")

    results = merged.groupby("strategy")["pnl"].agg(["mean", "std", "count", "sum"]).reset_index()
    results["sharpe"] = results["mean"] / results["std"].replace(0, 1e-6)
    results["avg_pnl"] = results["sum"] / results["count"]
    results["roi_estimate"] = results["sum"] / merged["capital_used"].sum()

    today = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    output = Path(f"reports/backtest_summary_{today}.csv")
    output.parent.mkdir(exist_ok=True, parents=True)
    results.to_csv(output, index=False)

    print(f"✅ Backtest complete: {output}")
    return results
    