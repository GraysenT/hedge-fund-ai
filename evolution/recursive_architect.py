import random

class EvolutionArchitect:
    def __init__(self):
        self.generations = []

    def evolve_evolution(self, previous_config):
        new_config = {
            "mutation_rate": previous_config["mutation_rate"] * random.uniform(0.9, 1.1),
            "selection_pressure": previous_config["selection_pressure"] + random.uniform(-0.01, 0.01),
            "diversity_bias": previous_config["diversity_bias"] + random.uniform(-0.02, 0.02),
        }
        self.generations.append(new_config)
        return new_config

    def get_latest_plan(self):
        return self.generations[-1] if self.generations else None