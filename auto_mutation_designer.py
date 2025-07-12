Below is a Python code that designs mutation templates optimized for different strategy classes. The code defines a base class for mutation strategies and several subclasses for specific mutation types. Each subclass implements a `mutate` method tailored to its strategy.

```python
import random

class MutationStrategy:
    """Base class for mutation strategies."""
    def mutate(self, data):
        raise NotImplementedError("Subclasses should implement this method.")

class RandomResetMutation(MutationStrategy):
    """Mutation strategy that randomly resets an element in the data."""
    def mutate(self, data):
        index = random.randint(0, len(data) - 1)
        data[index] = random.uniform(min(data), max(data))
        return data

class SwapMutation(MutationStrategy):
    """Mutation strategy that swaps two elements in the data."""
    def mutate(self, data):
        idx1, idx2 = random.sample(range(len(data)), 2)
        data[idx1], data[idx2] = data[idx2], data[idx1]
        return data

class ScrambleMutation(MutationStrategy):
    """Mutation strategy that scrambles a subset of the data."""
    def mutate(self, data):
        start, end = sorted(random.sample(range(len(data)), 2))
        subset = data[start:end+1]
        random.shuffle(subset)
        data[start:end+1] = subset
        return data

class InversionMutation(MutationStrategy):
    """Mutation strategy that inverts a subset of the data."""
    def mutate(self, data):
        start, end = sorted(random.sample(range(len(data)), 2))
        data[start:end+1] = reversed(data[start:end+1])
        return data

def apply_mutation(strategy, data):
    """Applies the given mutation strategy to the data."""
    return strategy.mutate(data)

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
strategies = [RandomResetMutation(), SwapMutation(), ScrambleMutation(), InversionMutation()]

# Applying each strategy to the data
for strategy in strategies:
    mutated_data = apply_mutation(strategy, data.copy())
    print(f"Mutated Data ({strategy.__class__.__name__}): {mutated_data}")
```

This code provides a framework for mutation strategies in genetic algorithms or similar optimization techniques. Each strategy class overrides the `mutate` method to implement a specific type of mutation:
- **RandomResetMutation**: Resets a random element to a new value within the range of the data.
- **SwapMutation**: Swaps two random elements in the data.
- **ScrambleMutation**: Randomly shuffles a subset of the data.
- **InversionMutation**: Reverses a subset of the data.

The `apply_mutation` function is a utility that applies a given mutation strategy to a dataset. The example usage demonstrates how to use these strategies on a sample dataset.