import pandas as pd
import os
from datetime import datetime

def run(return_threshold=1.0):
    print("\n🟢 Idea Promotion Engine Running...")

    sim_path = "logs/research_simulations.csv"
    promo_path = "logs/promoted_ideas.csv"

    if not os.path.exists(sim_path):
        print("❌ No simulation results found.")
        return

    df = pd.read_csv(sim_path)
    if df.empty:
        print("ℹ️ No simulations available.")
        return

    # Filter for successful ideas
    eligible = df[(df["Passed"] == True) & (df["Simulated Return (%)"] >= return_threshold)]
    if eligible.empty:
        print("ℹ️ No promotable ideas found.")
        return

    print("📈 Eligible for Promotion:")
    print(eligible[["Hypothesis ID", "Strategy", "Signal", "Asset", "Simulated Return (%)"]])

    # Promote all or top N
    promoted = eligible.copy()
    promoted["Promoted At"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Append if file exists
    if os.path.exists(promo_path):
        existing = pd.read_csv(promo_path)
        combined = pd.concat([existing, promoted]).drop_duplicates(subset=["Hypothesis ID"])
    else:
        combined = promoted

    combined.to_csv(promo_path, index=False)
    print(f"✅ Promoted {len(promoted)} ideas → Saved to: {promo_path}")

if __name__ == "__main__":
    run()
    