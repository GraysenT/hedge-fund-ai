import pandas as pd
from pathlib import Path
from datetime import datetime

SIGNAL_LOG_DIR = Path("signal_logs")
SIGNAL_LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_signals(signals_df: pd.DataFrame):
    """
    Save all signals for the current day.
    Expects columns: date, strategy, ticker, signal, confidence, etc.
    """
    today = datetime.utcnow().strftime("%Y-%m-%d")
    filename = SIGNAL_LOG_DIR / f"signals_{today}.csv"
    signals_df.to_csv(filename, index=False)
    print(f"📝 Signals logged to {filename}")
    