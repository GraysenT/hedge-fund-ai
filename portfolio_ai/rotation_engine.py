import pandas as pd
import os

def run(window=3):
    print("\n🔁 Portfolio Rotation Engine Running...")

    path = "logs/portfolio_memory.csv"
    output = "logs/rotated_weights.csv"

    if not os.path.exists(path):
        print("❌ portfolio_memory.csv not found.")
        return

    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    recent = df.sort_values("Date", ascending=True).groupby("Strategy").tail(window)

    # Compute recent performance trend (change in weight)
    delta = recent.groupby("Strategy")["Weight"].apply(lambda x: x.iloc[-1] - x.iloc[0])
    delta = delta.fillna(0)

    # Normalize deltas to create new rotation weights
    total_delta = delta.sum()
    if total_delta == 0:
        print("⚠️ No weight change detected across strategies.")
        return

    weights = delta / total_delta
    weights = weights.clip(lower=0)  # eliminate negatives
    final_weights = weights / weights.sum()

    rotated = pd.DataFrame({
        "Strategy": final_weights.index,
        "Weight": final_weights.values,
        "Recent Δ": delta.values
    }).round(4)

    rotated.to_csv(output, index=False)
    print("📦 Rotation completed. New weights:")
    print(rotated)
    print(f"✅ Saved to {output}")

if __name__ == "__main__":
    run()
