Below is a Python script that simulates genetic mutations over multiple generations and tracks which mutation patterns tend to survive. The script uses a simple model where each individual has a genome represented as a string of binary digits. A mutation can flip a bit from 0 to 1 or from 1 to 0. The fitness of an individual is determined by the number of 1s in the genome, simulating a scenario where having more 1s is advantageous for survival.

```python
import random

def generate_initial_population(size, genome_length):
    return [''.join(random.choice('01') for _ in range(genome_length)) for _ in range(size)]

def mutate(genome, mutation_rate):
    return ''.join(bit if random.random() > mutation_rate else str(1 - int(bit)) for bit in genome)

def get_fitness(genome):
    return genome.count('1')

def select_population(population, fitnesses, num_to_select):
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [genome for genome, fitness in sorted_population[:num_to_select]]

def simulate_generation(current_population, mutation_rate):
    mutated_population = [mutate(genome, mutation_rate) for genome in current_population]
    fitnesses = [get_fitness(genome) for genome in mutated_population]
    return select_population(mutated_population, fitnesses, len(current_population))

def simulate_evolution(population_size, genome_length, mutation_rate, generations):
    population = generate_initial_population(population_size, genome_length)
    history = []

    for _ in range(generations):
        population = simulate_generation(population, mutation_rate)
        history.append(population)

    return history

def count_genome_occurrences(history):
    genome_occurrence = {}
    for generation in history:
        for genome in generation:
            if genome in genome_occurrence:
                genome_occurrence[genome] += 1
            else:
                genome_occurrence[genome] = 1
    return genome_occurrence

# Parameters
population_size = 100
genome_length = 10
mutation_rate = 0.01
generations = 50

# Simulation
evolution_history = simulate_evolution(population_size, genome_length, mutation_rate, generations)
genome_occurrences = count_genome_occurrences(evolution_history)

# Display the most persistent genomes
persistent_genomes = sorted(genome_occurrences.items(), key=lambda x: x[1], reverse=True)
print("Most persistent genomes:")
for genome, count in persistent_genomes[:10]:
    print(f"Genome: {genome}, Occurrences: {count}")
```

This script includes functions to:
- Generate an initial random population.
- Mutate the population.
- Calculate fitness based on the number of 1s in the genome.
- Select the fittest individuals to form the next generation.
- Simulate multiple generations.
- Count how often each genome appears throughout the generations.

The output lists the most persistent genomes, i.e., those that appear most frequently across generations, suggesting they have beneficial mutation patterns that help them survive. Adjust the parameters like `population_size`, `genome_length`, `mutation_rate`, and `generations` to explore different evolutionary dynamics.