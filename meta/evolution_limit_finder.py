Here's a Python script that simulates the process of logic mutation in a simple genetic algorithm framework to find evolutionary ceilings and diminishing returns. The script uses a basic fitness function and demonstrates how mutations can lead to a plateau in improvements, illustrating the concept of diminishing returns in evolutionary computation.

```python
import random

def fitness_function(solution):
    """Simple fitness function: sum of elements in the solution."""
    return sum(solution)

def generate_initial_population(pop_size, gene_size):
    """Generate an initial population of random solutions."""
    return [[random.randint(0, 1) for _ in range(gene_size)] for _ in range(pop_size)]

def mutate(solution, mutation_rate):
    """Mutate a solution by flipping bits with a given mutation rate."""
    return [1 - gene if random.random() < mutation_rate else gene for gene in solution]

def best_solution(population):
    """Find the best solution in the current population."""
    return max(population, key=fitness_function)

def evolutionary_algorithm(pop_size, gene_size, mutation_rate, generations):
    """Run the evolutionary algorithm to find ceilings and diminishing returns."""
    population = generate_initial_population(pop_size, gene_size)
    best_fitness_over_time = []

    for generation in range(generations):
        # Mutate the population
        new_population = [mutate(individual, mutation_rate) for individual in population]
        
        # Evaluate the population
        best_individual = best_solution(new_population)
        best_fitness = fitness_function(best_individual)
        best_fitness_over_time.append(best_fitness)
        
        # Output the generation and best fitness
        print(f"Generation {generation}: Best Fitness = {best_fitness}")
        
        # Check for diminishing returns
        if generation > 0 and best_fitness_over_time[-1] <= best_fitness_over_time[-2]:
            print("Diminishing returns detected. No improvement in fitness.")
            break
        
        population = new_population

    return best_individual, best_fitness_over_time

# Parameters
population_size = 100
gene_length = 20
mutation_rate = 0.01
num_generations = 50

# Run the evolutionary algorithm
best_individual, fitness_history = evolutionary_algorithm(population_size, gene_length, mutation_rate, num_generations)
```

This script defines a simple genetic algorithm where each individual in the population is represented as a list of binary genes. The fitness function is the sum of the genes, so the optimal solution is all ones. The script includes mutation but no crossover, and it checks for diminishing returns by comparing the best fitness of the current generation to the previous one. If there's no improvement, it concludes that diminishing returns have occurred and stops the evolution.