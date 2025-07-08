import json
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns

def show_research_dashboard():
    path = "memory/research_memory.json"
    if not os.path.exists(path):
        print("❌ No research memory found.")
        return

    with open(path, "r") as f:
        memory = json.load(f)

    df = pd.DataFrame(memory)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values("timestamp", ascending=False)

    print("📊 Top Research Ideas:")
    print(df[["timestamp", "idea", "score"]].head(5))

    plt.figure(figsize=(10, 5))
    sns.histplot(df["score"], bins=10, kde=True)
    plt.title("Research Hypothesis Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    show_research_dashboard()