import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

DEPLOY_PATH = "memory/deployability_scores.json"
CONF_RISK_PATH = "memory/confidence_vs_risk.json"

def show_deployment_dashboard():
    if not os.path.exists(DEPLOY_PATH):
        print("❌ No deployability scores found.")
        return

    with open(DEPLOY_PATH, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df = df.sort_values("deployability", ascending=False)

    print("🚦 Top Strategies by Deployability:")
    print(df[["idea", "deployability"]].head(5))

    plt.figure(figsize=(10, 5))
    sns.histplot(df["deployability"], bins=15, color='green')
    plt.title("Deployability Score Distribution")
    plt.xlabel("Deployability Score")
    plt.ylabel("Number of Strategies")
    plt.axvline(0.65, color="red", linestyle="--", label="Deploy Threshold")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    show_confidence_vs_risk_chart()

def show_confidence_vs_risk_chart():
    if not os.path.exists(CONF_RISK_PATH):
        print("⚠️ No confidence-risk data.")
        return

    with open(CONF_RISK_PATH, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="risk", y="confidence",
        size="signal_strength", sizes=(20, 200),
        hue="signal_strength", palette="coolwarm",
        data=df, alpha=0.8, edgecolor="black"
    )
    plt.title("Confidence vs Risk Map")
    plt.xlabel("Risk")
    plt.ylabel("Confidence")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_deployment_dashboard()