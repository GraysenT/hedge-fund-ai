import pandas as pd
import random

class RLAgent:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1
        self.gamma = 0.95

    def update(self, state, action, reward, next_state):
        state_key = f"{state}:{action}"
        next_max = max([self.q_table.get(f"{next_state}:{a}", 0) for a in ["buy", "sell", "hold"]])
        old_value = self.q_table.get(state_key, 0)
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[state_key] = new_value

    def act(self, state):
        options = ["buy", "sell", "hold"]
        return max(options, key=lambda a: self.q_table.get(f"{state}:{a}", 0))