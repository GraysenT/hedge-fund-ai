import time

class StrategyScoreTracker:
    def __init__(self):
        self.scores = {}

    def update_score(self, strategy_name, reward, decay=0.01):
        if strategy_name not in self.scores:
            self.scores[strategy_name] = 0

        self.scores[strategy_name] *= (1 - decay)
        self.scores[strategy_name] += reward

    def get_score(self, strategy_name):
        return self.scores.get(strategy_name, 0)

    def log_scores(self):
        print("[STRATEGY SCORES]")
        for strategy, score in self.scores.items():
            print(f" - {strategy}: {score:.4f}")
