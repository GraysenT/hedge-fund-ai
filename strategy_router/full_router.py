import pandas as pd
from reinforcement.self_label_agent import reinforce
from reinforcement.deep_alpha_agent import load_alpha_scores

def route_signals(signals_df: pd.DataFrame) -> pd.DataFrame:
    """
    Main routing logic for signals:
    - Applies reinforcement learning weights
    - Adjusts by alpha scores
    - Normalizes confidence
    """
    if signals_df.empty:
        return signals_df

    signals_df = signals_df.copy()

    # Initialize with equal weights per strategy
    base_weights = {s: 1.0 for s in signals_df["strategy"].unique()}

    # Apply reinforcement weight adjustment
    reinforced = reinforce(base_weights)

    # Apply alpha scores if available
    alpha_scores = load_alpha_scores()
    for strat in reinforced:
        if strat in alpha_scores:
            reinforced[strat] *= 1 + min(alpha_scores[strat], 1.0)

    # Normalize weights
    total = sum(reinforced.values())
    if total > 0:
        reinforced = {k: v / total for k, v in reinforced.items()}

    # Apply weights to signals
    signals_df["weight"] = signals_df["strategy"].map(reinforced)
    signals_df["weighted_confidence"] = signals_df["confidence"] * signals_df["weight"]
    signals_df["final_score"] = signals_df["weighted_confidence"]

    # Optional sorting
    signals_df = signals_df.sort_values(by="final_score", ascending=False)

    return signals_df