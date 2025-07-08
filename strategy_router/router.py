import pandas as pd
import os

def run():
    print("\n📦 Strategy Router Running...")

    meta_path = "logs/meta_blended_weights.csv"
    fallback_path = "logs/strategy_weights.csv"
    health_path = "logs/alpha_defense_report.csv"
    output_path = "logs/strategy_routing.csv"

    # === Load weights ===
    if os.path.exists(meta_path):
        print("📊 Using Meta-Blended Weights")
        df = pd.read_csv(meta_path)
        df = df.rename(columns={"Meta Weight": "Weight"})
    else:
        print("📊 Using Fallback Weights")
        df = pd.read_csv(fallback_path)

    if "Strategy" not in df.columns or "Weight" not in df.columns:
        print("❌ Invalid weight format.")
        return

    # === Alpha Health Filter ===
    if os.path.exists(health_path):
        health_df = pd.read_csv(health_path)
        decaying = health_df[health_df["Status"] == "❌ Decaying"]["Strategy"].tolist()

        if decaying:
            print(f"🚫 Auto-muted decaying strategies: {decaying}")
            df = df[~df["Strategy"].isin(decaying)]
    else:
        print("⚠️ No alpha health report found — skipping integrity filter.")

    # === Save routing ===
    df = df[["Strategy", "Weight"]].round(4)
    df.to_csv(output_path, index=False)

    print("✅ Active Strategies:")
    for s in df["Strategy"]:
        print(f" → {s}")
    
    muted = set(df["Strategy"].tolist())
    if os.path.exists(fallback_path):
        all_strats = pd.read_csv(fallback_path)["Strategy"].unique().tolist()
        muted_set = sorted(set(all_strats) - muted)
        if muted_set:
            print("🔕 Muted Strategies:")
            for s in muted_set:
                print(f" - {s}")

    print(f"📘 Routing decisions saved to {output_path}")

if __name__ == "__main__":
    run()
    