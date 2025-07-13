import random

class GeneticOptimizer:
    def __init__(self, strategies):
        self.population = strategies

    def evolve(self):
        sorted_population = sorted(self.population, key=lambda s: s.performance_score, reverse=True)
        survivors = sorted_population[:len(self.population)//2]

        children = []
        for _ in range(len(self.population) - len(survivors)):
            parent = random.choice(survivors)
            child = self.clone_and_mutate(parent)
            children.append(child)

        self.population = survivors + children
        return self.population

    def clone_and_mutate(self, parent):
        new_params = parent.parameters.copy()
        for k in new_params:
            if isinstance(new_params[k], (int, float)):
                new_params[k] *= random.uniform(0.95, 1.05)
        return parent.__class__(name=f"{parent.name}_mutated", parameters=new_params)