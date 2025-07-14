import random
import copy

class GeneticOptimizer:
    def __init__(self, strategies):
        self.population = strategies  # Store original population

    def evolve(self, strategies=None):
        population = strategies or self.population
        if not population:
            print("⚠️ No strategies to evolve.")
            return []

        # Sort by performance score
        sorted_population = sorted(population, key=lambda s: getattr(s, 'performance_score', 0), reverse=True)
        survivors = sorted_population[:max(1, len(sorted_population)//2)]

        # Generate children via cloning + mutation
        children = []
        for _ in range(len(population) - len(survivors)):
            parent = random.choice(survivors)
            child = self.clone_and_mutate(parent)
            children.append(child)

        # Save and return new generation
        self.population = survivors + children
        return self.population

    def clone_and_mutate(self, parent):
        clone = copy.deepcopy(parent)
        clone.name = f"{parent.name}_mutated"
        clone.mutate_parameters()  # Assumes strategy has this method
        return clone