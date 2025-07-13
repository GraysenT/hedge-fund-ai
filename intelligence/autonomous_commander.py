import random

class AutonomousStrategyCommander:
    def __init__(self, strategies, tracker):
        self.strategies = strategies
        self.tracker = tracker

    def analyze(self):
        best = max(self.strategies, key=lambda s: s.performance_score)
        worst = min(self.strategies, key=lambda s: s.performance_score)
        return best, worst

    def evolve(self, evolution_engine):
        _, worst = self.analyze()
        if worst.performance_score < 0:
            evolution_engine.run_generation()
            print(f"⚙️ Commander triggered evolution")

    def allocate_focus(self):
        return sorted(self.strategies, key=lambda s: s.performance_score, reverse=True)