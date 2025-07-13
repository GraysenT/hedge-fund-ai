import matplotlib.pyplot as plt
import pandas as pd

def plot_rewards(csv_path="logs/performance_log.csv"):
    df = pd.read_csv(csv_path)
    grouped = df.groupby("strategy").mean()

    grouped["pnl"].plot(kind="bar", title="Avg PnL by Strategy", ylabel="PnL")
    plt.show()

    grouped["sharpe"].plot(kind="bar", title="Avg Sharpe by Strategy", ylabel="Sharpe Ratio")
    plt.show()