import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_investor_dashboard():
    path = "reports/investor_report.json"
    if not os.path.exists(path):
        print("❌ No investor report found.")
        return

    with open(path, "r") as f:
        report = json.load(f)

    print("\n📈 Investor Report Summary")
    for k, v in report["summary"].items():
        print(f"{k}: {v}")

    df_alloc = pd.DataFrame(report["allocation"])
    df_strats = pd.DataFrame(report["top_strategies"])

    plt.figure(figsize=(10, 4))
    sns.barplot(data=df_strats, x="strategy", y="pnl_total", palette="crest")
    plt.title("Top Strategy PnL")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    sns.barplot(data=df_alloc, x="strategy", y="weight", palette="flare")
    plt.title("Capital Allocation")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_investor_dashboard()