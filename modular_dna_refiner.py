```python
class DNA:
    def __init__(self, genes):
        self.genes = genes

    def mutate(self, mutation_rate):
        import random
        mutated_genes = []
        for gene in self.genes:
            if random.random() < mutation_rate:
                mutated_genes.append(random.choice(['A', 'T', 'C', 'G']))
            else:
                mutated_genes.append(gene)
        return DNA(mutated_genes)

    def crossover(self, other):
        import random
        crossover_point = random.randint(0, len(self.genes))
        child_genes = self.genes[:crossover_point] + other.genes[crossover_point:]
        return DNA(child_genes)

    def __str__(self):
        return ''.join(self.genes)

class Organism(DNA):
    def __init__(self, genes):
        super().__init__(genes)

    def reproduce(self, partner, mutation_rate=0.01):
        child_dna = self.crossover(partner)
        child_dna = child_dna.mutate(mutation_rate)
        return Organism(child_dna.genes)

# Example usage
parent1 = Organism(['A', 'T', 'G', 'C', 'A', 'C'])
parent2 = Organism(['T', 'G', 'C', 'A', 'T', 'G'])

child = parent1.reproduce(parent2)
print(f"Child DNA: {child}")
```