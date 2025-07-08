import pandas as pd
import os

def run():
    print("\n🧠 Reinforcement Reward Agent (Volatility-Aware) Running...")

    path = os.path.join("logs", "backtest_results.csv")
    output_path = os.path.join("logs", "strategy_weights_reinforced.csv")

    if not os.path.exists(path):
        print("🚫 No backtest results found.")
        return

    df = pd.read_csv(path)
    df["Return (%)"] = pd.to_numeric(df["Return (%)"], errors="coerce")
    df.dropna(subset=["Return (%)"], inplace=True)

    if "Strategy" not in df.columns or "Correct" not in df.columns:
        print("❌ Required columns missing.")
        return

    grouped = df.groupby("Strategy")

    # Accuracy and avg return
    accuracy = grouped["Correct"].value_counts(normalize=True).unstack().fillna(0)["✅"]
    avg_return = grouped["Return (%)"].mean()

    # NEW: Volatility (std dev of return %)
    volatility = grouped["Return (%)"].std().fillna(0)

    # Reward shaping: penalize high volatility
    risk_penalty = 1 / (1 + volatility)
    reward_score = (accuracy * avg_return) * risk_penalty

    # === OPTIONAL BOOST FROM SELF-LABELED PATTERNS ===
    labels_path = "logs/self_labeled_patterns.csv"
    if os.path.exists(labels_path):
        labels = pd.read_csv(labels_path)
        labels_set = set(zip(labels["Signal"], labels["Strategy"]))

        print(f"🔍 Boosting reward for self-labeled successful patterns: {len(labels_set)} found")

        # Apply boost to reward score
        for idx in reward_score.index:
            for signal_type in ["Buy", "Sell", "Hold"]:  # loop over signal types
                if (signal_type, idx) in labels_set:
                    reward_score[idx] *= 1.2  # boost 20%
                    print(f"  ✅ Boosted: {signal_type} + {idx}")
                    break  # only boost once per strategy

    # === Research Feedback Integration ===
    feedback_path = "logs/research_feedback_scores.csv"
    if os.path.exists(feedback_path):
        feedback_df = pd.read_csv(feedback_path)
        feedback_map = dict(zip(feedback_df["Strategy"], feedback_df["Research Boost Score"]))

        print(f"🔁 Applying research feedback boosts to strategies:")
        for strat in reward_score.index:
            if strat in feedback_map:
                boost = feedback_map[strat]
                reward_score[strat] += boost
                print(f"  ✅ {strat} boosted by +{round(boost, 2)}")

    weights = reward_score / reward_score.sum()

    result = pd.DataFrame({
        "Strategy": reward_score.index,
        "Accuracy": accuracy,
        "Avg Return": avg_return,
        "Volatility": volatility,
        "Reward Score": reward_score,
        "Reinforced Weight": weights
    }).reset_index(drop=True)

    print("📈 Volatility-Aware Reinforced Strategy Weights:")
    print(result[["Strategy", "Reinforced Weight", "Volatility"]].round(4))

    result.to_csv(output_path, index=False)
    print(f"✅ Reinforced weights saved to: {output_path}")

if __name__ == "__main__":
    run()