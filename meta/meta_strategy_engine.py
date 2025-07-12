import pandas as pd
from utils.paths import STRATEGY_STATUS_FILE

def blend_strategies(status_file=STRATEGY_STATUS_FILE):
    """
    Compute weighted score for each strategy based on live metrics:
    confidence, reward, alpha health, etc.
    """
    try:
        df = pd.read_json(status_file)
    except Exception as e:
        print(f"[MetaStrategyEngine] Failed to load strategy status: {e}")
        return {}

    if df.empty or "Strategy" not in df.columns:
        return {}

    df = df.set_index("Strategy")
    score = (
        0.4 * df["Confidence"].fillna(0) +
        0.3 * df["RewardScore"].fillna(0) +
        0.2 * df["AlphaHealth"].fillna(0) +
        0.1 * df["Deployability"].fillna(0)
    )

    return score.sort_values(ascending=False).to_dict()