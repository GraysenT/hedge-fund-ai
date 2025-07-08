import pandas as pd
import random
import os
from datetime import datetime
import hashlib

def mutate_idea(row):
    # Slightly tweak confidence range or strategy
    base_conf = row["Confidence Range"]
    strategies = ["Fusion", "LSTM", "Macro", "Sentiment"]

    new_conf = base_conf
    if ">" in base_conf:
        val = float(base_conf.replace(">", "").strip())
        new_val = round(val + random.uniform(-0.1, 0.1), 2)
        new_conf = f"> {max(0.0, min(1.0, new_val))}"

    new_strategy = random.choice([s for s in strategies if s != row["Strategy"]])

    return pd.Series([new_strategy, new_conf])

def generate_id(asset, signal, confidence, strategy):
    string = f"{asset}_{signal}_{confidence}_{strategy}"
    return hashlib.md5(string.encode()).hexdigest()[:8]

def run():
    print("\n🔁 Recursive Simulation Engine Running...")

    promo_path = "logs/promoted_ideas.csv"
    hypo_path = "logs/generated_hypotheses.csv"

    if not os.path.exists(promo_path):
        print("❌ No promoted ideas available.")
        return

    df = pd.read_csv(promo_path)
    if df.empty:
        print("ℹ️ No promoted ideas to expand.")
        return

    # Pick top N promoted ideas
    top = df.sort_values("Simulated Return (%)", ascending=False).head(5).copy()

    # Mutate each one into a new idea
    mutated = []
    for _, row in top.iterrows():
        asset = row["Asset"]
        signal = row["Signal"]
        base_conf = row["Confidence Range"]
        strategy = row["Strategy"]

        new_strategy, new_conf = mutate_idea(row)
        new_id = generate_id(asset, signal, new_conf, new_strategy)

        mutated.append({
            "Asset": asset,
            "Signal": signal,
            "Confidence Range": new_conf,
            "Strategy": new_strategy,
            "Pattern Count": 1,
            "Success Rate": 0.0,
            "Hypothesis ID": new_id,
            "Generated From": row["Hypothesis ID"],
            "Generated At": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })

    hypo_df = pd.DataFrame(mutated)
    if os.path.exists(hypo_path):
        existing = pd.read_csv(hypo_path)
        hypo_df = pd.concat([existing, hypo_df]).drop_duplicates("Hypothesis ID")

    hypo_df.to_csv(hypo_path, index=False)
    print(f"✅ Recursive hypotheses generated: {len(mutated)} → saved to: {hypo_path}")

if __name__ == "__main__":
    run()
    