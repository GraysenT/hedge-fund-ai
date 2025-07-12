import pandas as pd
import random

def simulate_strategy(strategy_fn, market_data, iterations=10):
    """
    Simulates a given strategy function over market data.
    Returns list of Sharpe ratios or PnL summaries.
    """
    results = []
    for _ in range(iterations):
        signals = strategy_fn(market_data)
        pnl = sum(s.get("pnl", random.uniform(-1, 1)) for s in signals)
        sharpe = pnl / (0.01 + abs(pnl))  # fake risk proxy
        results.append({"pnl": pnl, "sharpe": sharpe})
    return results