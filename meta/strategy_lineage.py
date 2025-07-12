Here is a Python script that simulates the mutation of strategies and tracks their lineage and traits across generations. This example uses a simple genetic algorithm approach where each strategy has traits represented by bits in a string. Mutation occurs randomly, and the script keeps track of each strategy's lineage.

```python
import random

class Strategy:
    def __init__(self, traits, generation=0, ancestors=None):
        self.traits = traits
        self.generation = generation
        self.ancestors = ancestors if ancestors is not None else []

    def mutate(self):
        # Choose a random position to mutate
        mutation_point = random.randint(0, len(self.traits) - 1)
        new_traits = list(self.traits)
        
        # Flip the bit at the mutation point
        new_traits[mutation_point] = '1' if self.traits[mutation_point] == '0' else '0'
        new_traits = ''.join(new_traits)
        
        # Create a new strategy with the mutated traits
        return Strategy(new_traits, self.generation + 1, self.ancestors + [self])

    def __str__(self):
        return f"Generation {self.generation}: Traits = {self.traits}"

def simulate_generations(initial_traits, num_generations):
    current_strategies = [Strategy(initial_traits)]
    
    for generation in range(num_generations):
        next_generation = []
        print(f"Generation {generation + 1}")
        
        for strategy in current_strategies:
            # Each strategy can mutate into a new strategy
            mutated_strategy = strategy.mutate()
            next_generation.append(mutated_strategy)
            print(f"  Origin: {strategy.traits} -> Mutated: {mutated_strategy.traits}")
        
        current_strategies = next_generation

# Example usage
initial_traits = '0000'
num_generations = 5
simulate_generations(initial_traits, num_generations)
```

This script defines a `Strategy` class with methods for mutation and a function `simulate_generations` to simulate the evolution of strategies over multiple generations. Each strategy mutates by flipping a random bit in its trait string. The lineage (ancestors) of each strategy is tracked, and the script prints the traits of strategies in each generation along with their mutations. Adjust the `initial_traits` and `num_generations` as needed to explore different scenarios.