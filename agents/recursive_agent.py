import random
from core.strategy_performance import StrategyPerformance
from evolution.evolution_engine import EvolutionEngine
from strategies.trend_following import TrendFollowingStrategy
from strategies.mean_reversion import MeanReversionStrategy

class RecursiveAgent:
    def __init__(self, market: str):
        self.market = market
        self.performance = StrategyPerformance()
        self.strategies = [
            TrendFollowingStrategy("Trend", {"base": 1}),
            MeanReversionStrategy("MeanReversion", {"base": 1})
        ]
        self.evolver = EvolutionEngine(self.strategies)
        self.iteration = 0

    def step(self, market_data):
        for strat in self.strategies:
            signal = strat.generate_signal(market_data)
            reward = random.uniform(-0.3, 1.2)
            strat.score(reward, 1.0)
            self.performance.update(strat.name, reward, 1.0)

        if self.iteration % 50 == 0:
            self.evolver.run_generation()

        self.iteration += 1

    def export_state(self):
        return {
            "market": self.market,
            "strategy_scores": {
                s.name: s.performance_score for s in self.strategies
            }
        }