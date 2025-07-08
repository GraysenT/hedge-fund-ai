import os
import pandas as pd
import json

BACKTEST_RESULTS_DIR = "backtesting/results"
STRATEGY_MEMORY_PATH = "strategy_memory/latest_weights.json"

# Thresholds for logic
SHARPE_REINFORCE_THRESHOLD = 1.5
SHARPE_DECAY_THRESHOLD = 0.3
REINFORCE_BONUS = 0.2
DECAY_FACTOR = 0.5


def load_latest_performance():
    files = [f for f in os.listdir(BACKTEST_RESULTS_DIR) if f.startswith("backtest_perf")]
    if not files:
        raise FileNotFoundError("No backtest performance files found.")
    latest_file = sorted(files)[-1]
    path = os.path.join(BACKTEST_RESULTS_DIR, latest_file)
    return pd.read_csv(path)


def generate_weight_adjustments():
    df = load_latest_performance()
    adjustments = {}

    for _, row in df.iterrows():
        strategy = row['asset']
        sharpe = row.get('sharpe_ratio', 0)

        if sharpe >= SHARPE_REINFORCE_THRESHOLD:
            adjustments[strategy] = 1.0 + REINFORCE_BONUS  # boost
        elif sharpe < SHARPE_DECAY_THRESHOLD:
            adjustments[strategy] = DECAY_FACTOR  # decay
        else:
            adjustments[strategy] = 1.0  # neutral

    return adjustments


def save_adjusted_weights(adjustments):
    os.makedirs("strategy_memory", exist_ok=True)
    with open(STRATEGY_MEMORY_PATH, 'w') as f:
        json.dump(adjustments, f, indent=2)
    print(f"✅ Adjusted weights saved to {STRATEGY_MEMORY_PATH}")


if __name__ == '__main__':
    weights = generate_weight_adjustments()
    print("\n📊 Strategy Reinforcement Based on Backtest Sharpe:")
    for strategy, adj in weights.items():
        print(f"{strategy}: {'Reinforced' if adj > 1 else 'Decayed' if adj < 1 else 'Neutral'} ({adj})")

    save_adjusted_weights(weights)
