import pandas as pd
from pathlib import Path

ALPHA_PATH = Path("memory/deep_alpha_weights.csv")

def train_alpha_agent():
    """
    Train alpha score model using past performance.
    Saves average recent PnL per strategy.
    """
    from performance.performance_tracker import load_all_performance
    df = load_all_performance()
    if df.empty:
        return

    df["reward"] = df["pnl"]
    df["strategy_score"] = df.groupby("strategy")["reward"].rolling(5).mean().reset_index(level=0, drop=True)
    updated = df.groupby("strategy")["strategy_score"].mean().to_dict()

    pd.DataFrame(list(updated.items()), columns=["strategy", "alpha_score"]).to_csv(ALPHA_PATH, index=False)
    print(f"🧠 Alpha agent updated scores: {ALPHA_PATH}")

def load_alpha_scores():
    """
    Load the latest alpha scores per strategy.
    """
    if not ALPHA_PATH.exists():
        return {}
    df = pd.read_csv(ALPHA_PATH)
    return dict(zip(df["strategy"], df["alpha_score"]))