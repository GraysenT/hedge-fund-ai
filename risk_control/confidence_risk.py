import pandas as pd
import os
from datetime import datetime

def run():
    print("\n📊 Confidence vs. Risk Analysis Running...")

    final_signal_path = "logs/final_signals.csv"
    reinforcement_path = "logs/strategy_weights_reinforced.csv"
    output_path = "logs/confidence_risk_scores.csv"

    if not os.path.exists(final_signal_path) or not os.path.exists(reinforcement_path):
        print("❌ Required data not found.")
        return

    signals = pd.read_csv(final_signal_path)
    weights = pd.read_csv(reinforcement_path)

    if signals.empty or weights.empty:
        print("ℹ️ No signals or weights to analyze.")
        return

    # Merge confidence + weight
    merged = signals.merge(weights, on="Strategy", how="left")

    grouped = merged.groupby("Strategy").agg({
        "Confidence": "mean",
        "Reinforced Weight": "mean"
    }).rename(columns={"Confidence": "Avg Confidence", "Reinforced Weight": "Weight"})

    # Simulate volatility as 1 - confidence for now
    grouped["Estimated Risk"] = 1 - grouped["Avg Confidence"]
    grouped["Confidence/Risk Ratio"] = grouped["Avg Confidence"] / grouped["Estimated Risk"]

    grouped = grouped.reset_index()
    grouped["Scored At"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    grouped.to_csv(output_path, index=False)

    print(f"✅ Confidence vs. Risk scores saved to: {output_path}")
    print(grouped)

if __name__ == "__main__":
    run()
