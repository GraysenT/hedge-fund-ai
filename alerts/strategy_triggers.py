import pandas as pd
from pathlib import Path

MUTED_PATH = Path("memory/muted_strategies.csv")
REWARDED_PATH = Path("memory/rewarded_strategies.csv")

def load_muted_strategies_df():
    if MUTED_PATH.exists():
        return pd.read_csv(MUTED_PATH)
    return pd.DataFrame(columns=["strategy", "timestamp", "reason"])

def load_rewarded_strategies_df():
    if REWARDED_PATH.exists():
        return pd.read_csv(REWARDED_PATH)
    return pd.DataFrame(columns=["strategy", "timestamp", "source"])