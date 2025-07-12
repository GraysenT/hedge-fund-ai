import random

class Strategy:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.parameters = self.generate_parameters()

    def generate_parameters(self):
        # Generate random parameters for the strategy
        return {
            'param1': random.randint(1, 100),
            'param2': random.uniform(0.1, 1.0),
            'param3': random.choice(['A', 'B', 'C'])
        }

    def mutate(self):
        # Mutate the strategy parameters slightly
        mutation = {
            'param1': self.parameters['param1'] + random.randint(-10, 10),
            'param2': max(0.1, min(self.parameters['param2'] + random.uniform(-0.1, 0.1), 1.0)),
            'param3': random.choice(['A', 'B', 'C'])
        }
        return mutation

    def __repr__(self):
        return f"{self.name} (Score: {self.score}, Params: {self.parameters})"

def spawn_new_generation(ancestors, num_offspring):
    new_generation = []
    for ancestor in ancestors:
        for _ in range(num_offspring):
            new_strategy = Strategy(f"{ancestor.name}-child", 0)
            new_strategy.parameters = ancestor.mutate()
            new_generation.append(new_strategy)
    return new_generation

def evaluate_strategy(strategy):
    # Simulate evaluation of the strategy (placeholder)
    strategy.score = random.randint(0, 100)

def recursive_improvement(strategies, depth):
    if depth == 0:
        return strategies

    # Evaluate all strategies
    for strategy in strategies:
        evaluate_strategy(strategy)

    # Sort strategies by score
    strategies.sort(key=lambda x: x.score, reverse=True)

    # Select the top half of strategies as ancestors for the next generation
    num_ancestors = len(strategies) // 2
    ancestors = strategies[:num_ancestors]

    # Spawn new generation from the best ancestors
    new_generation = spawn_new_generation(ancestors, 2)  # Each ancestor spawns 2 offspring

    # Recursive call to improve the next generation
    return recursive_improvement(new_generation, depth - 1)

# Initial set of strategies
initial_strategies = [Strategy(f"Strategy{i}", 0) for i in range(10)]

# Improve strategies recursively
final_strategies = recursive_improvement(initial_strategies, 3)

# Print the final strategies
for strategy in final_strategies:
    print(strategy)