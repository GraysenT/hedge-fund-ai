Here's a Python code example that demonstrates a simple genetic algorithm with controls for mutation rate, randomness, and crossover during the logic generation process. This example will use a genetic algorithm to find a string that matches a target string, which is a common introductory problem for genetic algorithms.

```python
import random

class Individual:
    def __init__(self, genes, mutation_rate):
        self.genes = genes
        self.mutation_rate = mutation_rate
        self.fitness = 0

    def mutate(self):
        new_genes = []
        for gene in self.genes:
            if random.random() < self.mutation_rate:
                new_genes.append(chr(random.randint(32, 126)))
            else:
                new_genes.append(gene)
        self.genes = new_genes

    def calculate_fitness(self, target):
        self.fitness = sum(1 for a, b in zip(self.genes, target) if a == b)

def crossover(parent1, parent2):
    child_genes = []
    for g1, g2 in zip(parent1.genes, parent2.genes):
        child_genes.append(g1 if random.random() > 0.5 else g2)
    return Individual(child_genes, parent1.mutation_rate)

def generate_initial_population(size, gene_length, mutation_rate):
    population = []
    for _ in range(size):
        genes = [chr(random.randint(32, 126)) for _ in range(gene_length)]
        population.append(Individual(genes, mutation_rate))
    return population

def genetic_algorithm(target, population_size, mutation_rate, generations):
    gene_length = len(target)
    population = generate_initial_population(population_size, gene_length, mutation_rate)

    for generation in range(generations):
        for individual in population:
            individual.calculate_fitness(target)

        population.sort(key=lambda x: x.fitness, reverse=True)
        if population[0].fitness == gene_length:
            print(f"Target reached in generation {generation}")
            print("".join(population[0].genes))
            return

        next_generation = population[:2]  # Elitism: carry the best two to the next generation

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)  # Tournament selection from the top 10
            child = crossover(parent1, parent2)
            child.mutate()
            next_generation.append(child)

        population = next_generation

    print("Final best solution:")
    print("".join(population[0].genes))

target_string = "Hello, World!"
population_size = 100
mutation_rate = 0.01
generations = 1000

genetic_algorithm(target_string, population_size, mutation_rate, generations)
```

This code defines a simple genetic algorithm to evolve a population of strings towards a target string. It includes mutation (with a specified mutation rate), crossover, and basic selection mechanisms. Adjust the `mutation_rate`, `population_size`, and `generations` to see how they affect the convergence towards the target string.