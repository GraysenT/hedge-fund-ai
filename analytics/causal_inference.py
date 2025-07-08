import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_causal_inference(csv_path):
    df = pd.read_csv(csv_path)
    target = "pnl"

    corr = df.corr()[target].drop(target)
    corr = corr.sort_values(ascending=False)

    print("🧠 Top causal candidates:")
    print(corr.head(10))

    plt.figure(figsize=(10, 5))
    sns.barplot(x=corr.values[:10], y=corr.index[:10])
    plt.title(f"Top Causal Feature Correlations to {target}")
    plt.xlabel("Correlation")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_causal_inference("logs/signal_feature_log.csv")