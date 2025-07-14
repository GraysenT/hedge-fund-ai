import random
from core.strategy_performance import StrategyPerformance
from evolution.evolution_engine import EvolutionEngine
from strategies.trend_following import TrendFollowingStrategy
from strategies.mean_reversion import MeanReversionStrategy

class RecursiveAgent:
    def __init__(self, market: str):
        self.market = market
        self.strategies = [
            TrendFollowingStrategy("Trend", {"base": 1}),
            MeanReversionStrategy("Mean", {"base": 1})
        ]
        self.performance = StrategyPerformance()
        self.evolver = EvolutionEngine(self.strategies)
        self.iteration = 0
        self.manual_signal = None

    def step(self, market_data):
        for strat in self.strategies:
            signal = strat.generate_signal(market_data)

            # Inject dream signal override
            if self.manual_signal:
                signal = self.manual_signal
                print(f"🧠 [Agent {self.market}] Using manual signal: {signal}")
                self.manual_signal = None

            reward = random.uniform(-0.3, 1.2)
            strat.score(reward, 1.0)
            self.performance.update(strat.name, reward, 1.0)

        if self.iteration % 50 == 0:
            self.strategies = self.evolver.evolve(self.strategies)

        self.iteration += 1

    def export_state(self):
        return {
            "market": self.market,
            "strategy_scores": {s.name: s.performance_score for s in self.strategies}
        }