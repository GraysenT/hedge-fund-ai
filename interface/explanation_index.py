class StrategyExplanationIndex:
    def __init__(self):
        self.index = {}

    def add(self, strategy_name, explanation):
        self.index[strategy_name] = explanation
        print(f"[EXPLAIN INDEX] {strategy_name}: {explanation}")

    def get(self, strategy_name):
        return self.index.get(strategy_name, "No explanation available.")