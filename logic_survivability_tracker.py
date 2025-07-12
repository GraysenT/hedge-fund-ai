```python
import random

def mutate_logic_module(module, mutation_rate=0.1):
    """ Mutate the logic module by randomly flipping some of its bits. """
    return [
        not bit if random.random() < mutation_rate else bit
        for bit in module
    ]

def test_logic_module(module):
    """ Test the logic module by evaluating its performance on a hypothetical task. """
    # Example task: Count the number of True values and consider it a score
    return sum(module)

def simulate_evolution(initial_module, generations=100, mutation_rate=0.1):
    """ Simulate the evolution of a logic module over a number of generations. """
    current_module = initial_module
    scores = []
    
    for _ in range(generations):
        current_module = mutate_logic_module(current_module, mutation_rate)
        score = test_logic_module(current_module)
        scores.append(score)
    
    return scores

def main():
    # Initial logic module: a list of boolean values
    initial_module = [random.choice([True, False]) for _ in range(10)]
    
    # Parameters
    generations = 200
    mutation_rate = 0.05
    
    # Simulate evolution
    scores = simulate_evolution(initial_module, generations, mutation_rate)
    
    # Output the results
    print("Initial module:", initial_module)
    print("Survival scores over generations:", scores)

if __name__ == "__main__":
    main()
```