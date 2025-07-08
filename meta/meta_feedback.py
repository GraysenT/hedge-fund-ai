import pandas as pd
import os

def run(min_samples=3):
    print("\n🧠 Meta-Feedback Engine Running...")

    memory_path = "logs/simulation_memory.csv"
    output_path = "logs/meta_feedback_scores.csv"

    if not os.path.exists(memory_path):
        print("❌ Memory log not found.")
        return

    df = pd.read_csv(memory_path)
    if "Strategy" not in df.columns or "Return (%)" not in df.columns:
        print("❌ Required columns missing from memory log.")
        return

    df["Success"] = (df["Correct"] == "✅") & (df["Return (%)"] > 0)
    grouped = df.groupby("Strategy")["Success"].agg(["count", "mean"]).reset_index()
    grouped.columns = ["Strategy", "Samples", "Meta Success Rate"]
    grouped = grouped[grouped["Samples"] >= min_samples]

    grouped["Meta Score"] = grouped["Meta Success Rate"] * grouped["Samples"]
    grouped = grouped.sort_values("Meta Score", ascending=False)

    print("📊 Meta Feedback Scores:")
    print(grouped.round(3))

    grouped.to_csv(output_path, index=False)
    print(f"✅ Scores saved to: {output_path}")

if __name__ == "__main__":
    run()
    