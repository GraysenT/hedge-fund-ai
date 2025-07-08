import json
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_risk_dashboard():
    matrix_path = "memory/global_risk_matrix.json"
    if not os.path.exists(matrix_path):
        print("❌ No risk matrix found.")
        return

    with open(matrix_path, "r") as f:
        matrix = json.load(f)

    df = pd.DataFrame(matrix)

    print("🛡️ Risk Matrix Overview:")
    print(df[["strategy", "risk_score", "volatility", "drawdown_est", "red_flag"]].sort_values("risk_score", ascending=False))

    plt.figure(figsize=(10, 5))
    sns.heatmap(df.pivot(index="strategy", columns="red_flag", values="risk_score").fillna(0), annot=True, cmap="Reds")
    plt.title("Global Risk Matrix (Red = Red Flag Triggered)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_risk_dashboard()