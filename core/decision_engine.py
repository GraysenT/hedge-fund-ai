class DecisionEngine:
    def __init__(self):
        self.strategy_scores = {}

    def register_score(self, strategy_name: str, score: float):
        self.strategy_scores[strategy_name] = score

    def best_strategy(self):
        if not self.strategy_scores:
            return None
        return max(self.strategy_scores.items(), key=lambda x: x[1])[0]

    def clear(self):
        self.strategy_scores = {}