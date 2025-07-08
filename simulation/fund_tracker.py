import pandas as pd
from pathlib import Path
from datetime import datetime

PERF_LOG = Path("performance_logs")
FUND_LOG = Path("audit/fund_balance.csv")
FUND_LOG.parent.mkdir(parents=True, exist_ok=True)

def update_fund_balance(start_balance=1_000_000):
    files = list(PERF_LOG.glob("performance_*.csv"))
    df = pd.concat([pd.read_csv(f) for f in files])
    df["date"] = pd.to_datetime(df["date"])

    pnl_daily = df.groupby("date")["pnl"].sum().cumsum()
    balance = start_balance + pnl_daily

    log = pd.DataFrame({
        "date": pnl_daily.index,
        "balance": balance
    })

    log.to_csv(FUND_LOG, index=False)
    print(f"📘 Fund balance saved: {FUND_LOG}")