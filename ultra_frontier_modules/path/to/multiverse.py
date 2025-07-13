import json
import numpy as np


class Multiverse:
    def __init__(self):
        self.histories = {}
        self.futures = {}

    def add_history(self, universe_id, history):
        self.histories[universe_id] = history

    def add_future(self, universe_id, future):
        self.futures[universe_id] = future

    def get_divergence(self, universe_id1, universe_id2):
        history1 = self.histories.get(universe_id1, [])
        history2 = self.histories.get(universe_id2, [])
        divergence = np.linalg.norm(np.array(history1) - np.array(history2))
        return divergence

    def get_convergence(self, universe_id1, universe_id2):
        future1 = self.futures.get(universe_id1, [])
        future2 = self.futures.get(universe_id2, [])
        convergence = np.linalg.norm(np.array(future1) - np.array(future2))
        return convergence