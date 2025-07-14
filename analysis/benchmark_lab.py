def benchmark_strategies(strategies):
    scores = {s.name: s.backtest() for s in strategies}
    return scores