import pandas as pd
import os

def run():
    print("\n⚖️ Portfolio Allocator AI Running...")

    # Use meta-blended weights if available, fallback to base
    meta_path = os.path.join("logs", "meta_blended_weights.csv")
    fallback_path = os.path.join("logs", "strategy_weights.csv")

    if os.path.exists(meta_path):
        print("📊 Using Meta Blended Weights")
        df = pd.read_csv(meta_path)
        df = df.rename(columns={"Meta Weight": "Weight"})
    else:
        print("📊 Using Fallback Base Allocator Weights")
        df = pd.read_csv(fallback_path)

    if "Strategy" not in df.columns or "Weight" not in df.columns:
        print("❌ Required columns missing.")
        return

    # Normalize and save
    df["Weight"] = df["Weight"] / df["Weight"].sum()
    print("📊 Strategy Scores and Weights:")
    print(df.set_index("Strategy")["Weight"].round(4))

    df.to_csv("logs/strategy_weights.csv", index=False)
    print("✅ Portfolio weights saved to logs/strategy_weights.csv")

if __name__ == "__main__":
    run()
