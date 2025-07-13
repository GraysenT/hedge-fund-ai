import numpy as np
import random

class RLController:
    def __init__(self, strategies):
        self.strategies = strategies
        self.q_table = {s.name: 0.0 for s in strategies}

    def select(self):
        # ε-greedy selection
        if random.random() < 0.1:
            return random.choice(self.strategies)
        return max(self.strategies, key=lambda s: self.q_table[s.name])

    def update(self, strategy_name, reward):
        self.q_table[strategy_name] = 0.9 * self.q_table[strategy_name] + 0.1 * reward