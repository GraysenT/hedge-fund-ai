To create a Python program that scans logic seeds (initial conditions or parameters) to predict which are most likely to generate future high-alpha offspring (high-performing outcomes), we can simulate a genetic algorithm. This algorithm will evolve a population of seeds based on their performance, measured by an alpha score, to identify the most promising seeds.

Here's a Python script using a simple genetic algorithm framework to achieve this. The script includes functions for initialization, evaluation, selection, crossover, mutation, and the main evolutionary loop:

```python
import random

# Parameters
population_size = 100
num_generations = 50
crossover_rate = 0.7
mutation_rate = 0.1
seed_length = 10  # Length of the binary seed

# Initialize population with random seeds
def initialize_population(size):
    return [[random.randint(0, 1) for _ in range(seed_length)] for _ in range(size)]

# Evaluate performance of a seed (alpha score)
def evaluate(seed):
    # Example: simple function where high alpha is the sum of 1s in the seed
    return sum(seed)

# Selection process (tournament selection)
def selection(population, scores, k=3):
    selected = []
    for _ in range(len(population)):
        participants = random.sample(list(zip(population, scores)), k)
        winner = max(participants, key=lambda x: x[1])
        selected.append(winner[0])
    return selected

# Crossover between two seeds
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point = random.randint(1, seed_length - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2

# Mutation of a seed
def mutate(seed):
    for i in range(len(seed)):
        if random.random() < mutation_rate:
            seed[i] = 1 - seed[i]
    return seed

# Main genetic algorithm loop
def genetic_algorithm():
    population = initialize_population(population_size)
    best_score = 0
    best_seed = None
    
    for generation in range(num_generations):
        scores = [evaluate(seed) for seed in population]
        if max(scores) > best_score:
            best_score = max(scores)
            best_seed = population[scores.index(best_score)]
        
        selected = selection(population, scores)
        next_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected[i], selected[i+1]
            child1, child2 = crossover(parent1, parent2)
            next_population.extend([mutate(child1), mutate(child2)])
        
        population = next_population
        print(f"Generation {generation + 1}: Best Score {best_score}")
    
    return best_seed, best_score

# Run the genetic algorithm
best_seed, best_score = genetic_algorithm()
print(f"Best seed found: {best_seed} with alpha score: {best_score}")
```

This script defines a genetic algorithm for evolving a population of binary seeds. Each seed's performance (alpha score) is simply calculated as the sum of its elements (number of 1s), which you can replace with a more complex function relevant to your specific application. The algorithm includes tournament selection, single-point crossover, and point mutation. Adjust the parameters and functions as needed to fit the specific characteristics and complexity of your problem domain.