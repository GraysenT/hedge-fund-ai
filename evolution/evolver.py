import random
import copy

class StrategyEvolver:
    def __init__(self, mutation_rate=0.1):
        self.mutation_rate = mutation_rate

    def evolve(self, strategies):
        survivors = sorted(strategies, key=lambda s: s.performance_score, reverse=True)[:len(strategies)//2]
        new_generation = []

        for strat in survivors:
            clone = self._mutate_strategy(copy.deepcopy(strat))
            new_generation.append(clone)

        return survivors + new_generation

    def _mutate_strategy(self, strategy):
        for k, v in strategy.parameters.items():
            if isinstance(v, (int, float)) and random.random() < self.mutation_rate:
                strategy.parameters[k] *= random.uniform(0.9, 1.1)
        strategy.name += "_mutated"
        return strategy