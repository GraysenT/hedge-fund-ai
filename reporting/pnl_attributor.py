import pandas as pd
from pathlib import Path

PERF_LOG = Path("performance_logs")

def generate_attribution_report():
    files = list(PERF_LOG.glob("performance_*.csv"))
    df = pd.concat([pd.read_csv(f) for f in files])

    df["date"] = pd.to_datetime(df["date"])

    grouped = df.groupby(["strategy", "ticker"]).agg({
        "pnl": "sum",
        "capital_used": "sum"
    }).reset_index()

    grouped["roi"] = grouped["pnl"] / grouped["capital_used"].replace(0, 1e-6)
    grouped.to_csv("reports/pnl_attribution.csv", index=False)
    print("✅ PnL attribution report saved.")