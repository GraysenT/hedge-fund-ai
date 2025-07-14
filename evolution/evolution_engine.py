from evolution.genetic_optimizer import GeneticOptimizer
from evolution.rl_controller import RLController

class EvolutionEngine:
    def __init__(self, strategies):
        self.strategies = strategies
        self.genetic = GeneticOptimizer(strategies)
        self.rl = RLController(strategies)

    def run_generation(self):
        self.strategies = self.genetic.evolve()

    def evolve(self, strategies):
        return self.genetic.evolve(strategies)

    def select_strategy(self):
        return self.rl.select()

    def update_rewards(self, strategy_name, reward):
        self.rl.update(strategy_name, reward)