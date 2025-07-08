import pandas as pd
from pathlib import Path
from datetime import datetime

PERF_DIR = Path("performance_logs")
PERF_DIR.mkdir(parents=True, exist_ok=True)

def log_daily_performance(date, pnl_dict, capital_dict, sharpe_dict=None):
    """
    Save daily performance metrics for each strategy.
    """
    data = []
    for strategy, pnl in pnl_dict.items():
        row = {
            "date": date,
            "strategy": strategy,
            "pnl": pnl,
            "capital_used": capital_dict.get(strategy, 0),
            "sharpe": sharpe_dict.get(strategy, None) if sharpe_dict else None
        }
        data.append(row)

    df = pd.DataFrame(data)
    filename = PERF_DIR / f"performance_{date}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved performance log: {filename}")

def load_all_performance():
    all_files = list(PERF_DIR.glob("performance_*.csv"))
    if not all_files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in all_files]
    return pd.concat(dfs, ignore_index=True)
    