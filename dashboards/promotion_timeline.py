Here's a Python script that simulates a timeline of logic promotions and mutation evolution epochs. The script uses a simple model where logic promotions are represented by increasing complexity or efficiency in a system, and mutation evolution epochs represent periods of random changes that may lead to improvements or variations in the system.

```python
import random

class System:
    def __init__(self):
        self.complexity = 1
        self.efficiency = 1

    def promote_logic(self):
        self.complexity += random.randint(1, 3)
        self.efficiency += random.random()

    def mutate(self):
        mutation_factor = random.uniform(0.9, 1.1)
        self.complexity *= mutation_factor
        self.efficiency *= mutation_factor

    def display_status(self, epoch):
        print(f"Epoch {epoch}: Complexity = {self.complexity:.2f}, Efficiency = {self.efficiency:.2f}")

def simulate_timeline(epochs, promotion_interval, mutation_chance):
    system = System()
    for epoch in range(1, epochs + 1):
        if epoch % promotion_interval == 0:
            system.promote_logic()
        
        if random.random() < mutation_chance:
            system.mutate()

        system.display_status(epoch)

# Parameters
total_epochs = 50
promotion_every_n_epochs = 5
mutation_probability = 0.2

simulate_timeline(total_epochs, promotion_every_n_epochs, mutation_probability)
```

### Explanation:
- The `System` class represents a system with attributes for complexity and efficiency.
- The `promote_logic` method increases the complexity and efficiency deterministically.
- The `mutate` method applies a random mutation factor to both complexity and efficiency, simulating random evolutionary changes.
- The `simulate_timeline` function runs the simulation for a specified number of epochs, applying logic promotions and mutations based on the given intervals and probabilities.
- The `display_status` method prints the current state of the system at each epoch.

You can adjust the `total_epochs`, `promotion_every_n_epochs`, and `mutation_probability` to see how different parameters affect the system's evolution over time.