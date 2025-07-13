from typing import List, Dict
from core.strategy_base import StrategyBase

class EnsembleStrategy(StrategyBase):
    def __init__(self, name: str, parameters: Dict, strategies: List[StrategyBase]):
        super().__init__(name, parameters)
        self.strategies = strategies

    def generate_signal(self, market_data):
        votes = {"buy": 0, "sell": 0, "hold": 0}
        for strat in self.strategies:
            signal = strat.generate_signal(market_data)
            votes[signal] += 1
        return max(votes, key=votes.get)