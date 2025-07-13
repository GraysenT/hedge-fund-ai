import matplotlib.pyplot as plt

def plot_performance(stats):
    strategies = list(stats.keys())
    pnl = [stats[s]["pnl"] for s in strategies]

    plt.figure(figsize=(10, 5))
    plt.bar(strategies, pnl)
    plt.title("Strategy PnL Comparison")
    plt.ylabel("PnL ($)")
    plt.xlabel("Strategy")
    plt.grid(True)
    plt.show()