```python
import random

def evaluate_strategy(strategy):
    """ Simulate evaluation of a strategy. Returns a score. """
    return sum(strategy)  # Example: sum of elements as performance score

def crossover(parent1, parent2):
    """ Perform crossover between two strategies to create a new strategy. """
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(strategy, mutation_rate=0.1):
    """ Mutate a strategy by randomly altering its elements. """
    return [gene if random.random() > mutation_rate else random.randint(0, 10) for gene in strategy]

def genetic_algorithm(population, generations=100, mutation_rate=0.1):
    """ Run a genetic algorithm to evolve strategies. """
    population_size = len(population)
    for _ in range(generations):
        # Evaluate all strategies in the population
        scores = [evaluate_strategy(strategy) for strategy in population]
        
        # Selection of parents based on their scores
        sorted_population = [x for _, x in sorted(zip(scores, population), reverse=True, key=lambda x: x[0])]
        top_performers = sorted_population[:population_size // 2]  # Select top half
        
        # Crossover to create new population
        new_population = top_performers[:]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_performers, 2)
            child = crossover(parent1, parent2)
            new_population.append(child)
        
        # Mutation
        new_population = [mutate(individual, mutation_rate) for individual in new_population]
        
        population = new_population
    
    return population

# Initial population of 10 strategies with 5 traits each
initial_population = [[random.randint(0, 10) for _ in range(5)] for _ in range(10)]

# Run genetic algorithm
final_population = genetic_algorithm(initial_population)

# Evaluate and print the best strategy
final_scores = [evaluate_strategy(strategy) for strategy in final_population]
best_strategy = final_population[final_scores.index(max(final_scores))]
print("Best Strategy:", best_strategy)
```