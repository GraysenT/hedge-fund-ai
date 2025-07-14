import pandas as pd
from strategies import stat_arb_engine, macro_sentiment

def replay_strategy(strategy_fn, historical_data):
    signals = []
    for i in range(10, len(historical_data)):
        window = historical_data.iloc[:i]
        result = strategy_fn.generate(window)
        signals.extend(result)
    return signals