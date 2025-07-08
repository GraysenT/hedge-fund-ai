import pandas as pd
import os


def run():
    print("\n📉 Performance Decay Engine Running...")

    memory_path = os.path.join("logs", "portfolio_memory.csv")
    decay_output = os.path.join("logs", "strategy_weights_decayed.csv")

    if not os.path.exists(memory_path):
        print("🚫 No portfolio memory log found.")
        return

    df = pd.read_csv(memory_path)

    if "Date" not in df.columns or "Strategy" not in df.columns or "Weight" not in df.columns:
        print("❌ Missing required columns in portfolio memory.")
        return

    # Most recent weights
    latest_date = df["Date"].max()
    recent_df = df[df["Date"] == latest_date].copy()

    # Compute decay from historical average
    avg_weights = df.groupby("Strategy")["Weight"].mean()
    recent_df["Decay Score"] = recent_df.apply(
        lambda row: row["Weight"] / avg_weights[row["Strategy"]], axis=1)

    # Apply decay: if score is < 0.85, reduce weight 10%
    def decay_weight(row):
        if row["Decay Score"] < 0.85:
            return round(max(0.0, row["Weight"] * 0.9), 4)
        return row["Weight"]

    recent_df["Adjusted Weight"] = recent_df.apply(decay_weight, axis=1)

    # Normalize
    total = recent_df["Adjusted Weight"].sum()
    recent_df["Final Weight"] = recent_df["Adjusted Weight"] / total

    print("📊 Adjusted Weights with Decay Applied:")
    print(recent_df[["Strategy", "Weight",
          "Decay Score", "Final Weight"]].round(4))

    recent_df[["Strategy", "Final Weight"]].to_csv(decay_output, index=False)
    print(f"✅ Decayed weights saved to: {decay_output}")


if __name__ == "__main__":
    run()
