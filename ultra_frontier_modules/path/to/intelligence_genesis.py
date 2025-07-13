import random


class Intelligence:
    def __init__(self, constraints):
        self.constraints = constraints
        self.state = self._init_state()

    def _init_state(self):
        return {constraint: random.random() for constraint in self.constraints}

    def evolve(self):
        for constraint in self.constraints:
            self.state[constraint] += random.uniform(-0.05, 0.05)
            self.state[constraint] = max(0, min(self.state[constraint], 1))

    def persist(self):
        while True:
            self.evolve()
            yield self.state