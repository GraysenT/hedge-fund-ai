import pandas as pd
import os
import random
from datetime import datetime

def run(min_occurrences=2):
    print("\n🔬 Autonomous Research Agent Running...")

    memory_path = "logs/research_memory.csv"
    sim_output = "logs/research_simulations.csv"

    if not os.path.exists(memory_path):
        print("❌ Research memory not found.")
        return

    df = pd.read_csv(memory_path)
    if df.empty:
        print("ℹ️ No hypotheses to evaluate.")
        return

    # Filter: only simulate ideas with at least min_occurrences
    candidates = df[df["Occurrences"] >= min_occurrences].drop_duplicates("Hypothesis ID")
    if candidates.empty:
        print("ℹ️ No frequent ideas to simulate.")
        return

    results = []
    for _, row in candidates.iterrows():
        idea_id = row["Hypothesis ID"]
        strategy = row["Strategy"]
        signal = row["Signal"]
        asset = row["Asset"]
        confidence = row["Confidence Range"]
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Simulate result (placeholder random logic or external plug-in later)
        simulated_return = round(random.uniform(-2.5, 4.5), 2)
        passed = simulated_return > 0.5

        results.append({
            "Hypothesis ID": idea_id,
            "Strategy": strategy,
            "Signal": signal,
            "Asset": asset,
            "Confidence Range": confidence,
            "Simulated Return (%)": simulated_return,
            "Passed": passed,
            "Simulated At": timestamp
        })

    result_df = pd.DataFrame(results)

    # Append or create simulation log
    if os.path.exists(sim_output):
        existing = pd.read_csv(sim_output)
        result_df = pd.concat([existing, result_df]).drop_duplicates(subset=["Hypothesis ID", "Simulated At"])

    result_df.to_csv(sim_output, index=False)
    print(f"✅ Simulated {len(results)} hypotheses → Saved to: {sim_output}")

if __name__ == "__main__":
    run()
    