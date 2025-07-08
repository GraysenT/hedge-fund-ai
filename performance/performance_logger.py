import pandas as pd
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("performance_logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_strategy_performance(perf_dict):
    """
    Accepts a dictionary of {strategy: {"pnl": float, "capital_used": float}}
    and logs it to a daily file.
    """
    today = datetime.utcnow().strftime("%Y-%m-%d")
    path = LOG_DIR / f"performance_{today}.csv"

    rows = []
    for strategy, stats in perf_dict.items():
        rows.append({
            "date": today,
            "strategy": strategy,
            "pnl": stats.get("pnl", 0),
            "capital_used": stats.get("capital_used", 0)
        })

    df = pd.DataFrame(rows)
    if path.exists():
        df.to_csv(path, mode="a", index=False, header=False)
    else:
        df.to_csv(path, index=False)

    print(f"✅ Logged {len(rows)} performance rows to {path}")