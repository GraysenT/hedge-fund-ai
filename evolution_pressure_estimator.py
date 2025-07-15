```python
import random

class EvolutionarySystem:
    def __init__(self, initial_pressure=0.5, mutation_rate=0.1, decay_rate=0.05, growth_rate=0.1):
        self.pressure = initial_pressure
        self.mutation_rate = mutation_rate
        self.decay_rate = decay_rate
        self.growth_rate = growth_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        # Initialize a simple population with random values
        return [random.random() for _ in range(100)]

    def measure_pressure(self):
        # Simulate pressure based on external factors
        external_signals = random.random()
        if external_signals < 0.3:
            self.pressure -= self.decay_rate
        elif external_signals > 0.7:
            self.pressure += self.growth_rate
        self.pressure = max(0, min(1, self.pressure))  # Keep pressure within bounds

    def mutate_population(self):
        # Mutate the population based on the current pressure
        for i in range(len(self.population)):
            if random.random() < self.pressure * self.mutation_rate:
                self.population[i] += random.uniform(-0.1, 0.1)
                self.population[i] = max(0, min(1, self.population[i]))  # Keep within bounds

    def evolve(self):
        self.measure_pressure()
        self.mutate_population()

    def run_simulation(self, steps=100):
        for _ in range(steps):
            self.evolve()
            print(f"Current Pressure: {self.pressure}")
            print(f"Sample of Population: {self.population[:5]}")

# Example usage
evolution_system = EvolutionarySystem()
evolution_system.run_simulation()
```