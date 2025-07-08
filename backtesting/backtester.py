import os
import pandas as pd
import numpy as np
from datetime import datetime

# Placeholder paths - adapt to match your data locations
HISTORICAL_SIGNALS_PATH = "data/historical_signals.csv"
HISTORICAL_PRICES_PATH = "data/historical_prices.csv"
BACKTEST_RESULTS_PATH = "backtesting/results/"


def load_data():
    signals = pd.read_csv(HISTORICAL_SIGNALS_PATH, parse_dates=['timestamp'])
    prices = pd.read_csv(HISTORICAL_PRICES_PATH, parse_dates=['timestamp'])
    return signals, prices


def backtest(signals, prices):
    merged = pd.merge(signals, prices, on=['timestamp', 'asset'], how='inner')
    merged.sort_values(by=['asset', 'timestamp'], inplace=True)

    merged['position'] = merged['signal'].shift(1)  # lag signal to avoid lookahead bias
    merged['returns'] = merged['price'].pct_change()
    merged['strategy_returns'] = merged['position'] * merged['returns']

    performance = (
        merged.groupby('asset')['strategy_returns']
        .agg(['sum', 'mean', 'std', 'count'])
        .rename(columns={'sum': 'total_return', 'mean': 'avg_return', 'std': 'volatility'})
    )
    performance['sharpe_ratio'] = performance['avg_return'] / performance['volatility'] * np.sqrt(252)
    return merged, performance.reset_index()


def save_results(log_df, perf_df):
    if not os.path.exists(BACKTEST_RESULTS_PATH):
        os.makedirs(BACKTEST_RESULTS_PATH)

    date_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_df.to_csv(f"{BACKTEST_RESULTS_PATH}backtest_log_{date_str}.csv", index=False)
    perf_df.to_csv(f"{BACKTEST_RESULTS_PATH}backtest_perf_{date_str}.csv", index=False)
    print(f"✅ Backtest results saved to {BACKTEST_RESULTS_PATH}")


if __name__ == '__main__':
    signals, prices = load_data()
    log, perf = backtest(signals, prices)
    save_results(log, perf)
