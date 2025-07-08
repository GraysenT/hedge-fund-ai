import pandas as pd
from pathlib import Path

SIGNAL_DIR = Path("signal_logs")
PERF_DIR = Path("performance_logs")
CLASSIFIED_DIR = Path("classified_failures")
CLASSIFIED_DIR.mkdir(exist_ok=True, parents=True)

def classify_failures():
    # Load signals
    signal_files = sorted(SIGNAL_DIR.glob("signals_*.csv"))
    perf_files = sorted(PERF_DIR.glob("performance_*.csv"))

    if not signal_files or not perf_files:
        print("🚫 No signal or performance files found.")
        return

    signal_df = pd.concat([pd.read_csv(f) for f in signal_files], ignore_index=True)
    perf_df = pd.concat([pd.read_csv(f) for f in perf_files], ignore_index=True)

    signal_df["date"] = pd.to_datetime(signal_df["date"])
    perf_df["date"] = pd.to_datetime(perf_df["date"])

    merged = signal_df.merge(perf_df, on=["date", "strategy"])
    merged["failure"] = (merged["pnl"] < 0) & (merged["confidence"] >= 0.6)

    def root_cause(row):
        if not row["failure"]:
            return "Success"
        if row["confidence"] > 0.9 and row["pnl"] < -100:
            return "Overconfident Loss"
        elif abs(row["pnl"]) > 200 and row["confidence"] < 0.8:
            return "Volatility Mismatch"
        elif row.get("news_override", False):
            return "News Override Conflict"
        else:
            return "Unknown Failure"

    merged["failure_reason"] = merged.apply(root_cause, axis=1)

    merged.to_csv(CLASSIFIED_DIR / "classified_signal_failures.csv", index=False)
    print("✅ Saved classified signal failures.")

def load_failure_data():
    fpath = CLASSIFIED_DIR / "classified_signal_failures.csv"
    if fpath.exists():
        return pd.read_csv(fpath)
    return pd.DataFrame()
    