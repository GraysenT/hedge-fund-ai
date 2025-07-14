from abc import ABC, abstractmethod
from typing import Dict, Any

class StrategyBase(ABC):
    def __init__(self, name: str, parameters: Dict[str, Any]):
        self.name = name
        self.parameters = parameters
        self.performance_score = 0.0

    @abstractmethod
    def generate_signal(self, market_data: Dict[str, Any]) -> str:
        pass

    def mutate_parameters(self):
        # Basic mutation example — override in child for custom behavior
        for k, v in self.parameters.items():
            if isinstance(v, (int, float)):
                self.parameters[k] += 0.01 * v

    def score(self, pnl: float, sharpe: float):
        self.performance_score = 0.7 * pnl + 0.3 * sharpe