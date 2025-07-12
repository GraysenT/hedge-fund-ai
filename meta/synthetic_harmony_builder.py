```python
class StrategicHarmonyBlender:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        """Add a strategy to the blender."""
        self.strategies.append(strategy)

    def evaluate_strategies(self, context):
        """Evaluate and blend strategies based on the given context."""
        results = []
        weights = []
        
        # Evaluate each strategy and determine its weight based on the context
        for strategy in self.strategies:
            result, weight = strategy.evaluate(context)
            results.append(result)
            weights.append(weight)
        
        # Normalize weights
        total_weight = sum(weights)
        if total_weight == 0:
            return None  # Avoid division by zero if no weights are provided
        normalized_weights = [w / total_weight for w in weights]
        
        # Blend results based on weights
        blended_result = sum(r * w for r, w in zip(results, normalized_weights))
        return blended_result

class Strategy:
    def __init__(self, name, logic_function):
        self.name = name
        self.logic_function = logic_function

    def evaluate(self, context):
        """Evaluate this strategy with the given context."""
        return self.logic_function(context)

# Example usage
def strategy1_logic(context):
    # Some complex logic that returns a result and a weight
    return context.get('data') * 2, 0.7

def strategy2_logic(context):
    # Another logic that returns a different result and a weight
    return context.get('data') + 5, 0.3

# Create strategies
strategy1 = Strategy("Increase and Weight Heavily", strategy1_logic)
strategy2 = Strategy("Add and Weight Lightly", strategy2_logic)

# Create blender and add strategies
blender = StrategicHarmonyBlender()
blender.add_strategy(strategy1)
blender.add_strategy(strategy2)

# Create a context and evaluate blended strategies
context = {'data': 10}
blended_result = blender.evaluate_strategies(context)
print("Blended Result:", blended_result)
```

This code defines a system for blending strategies that might have conflicting logic. Each strategy is evaluated with a context, and returns both a result and a weight indicating its importance or relevance in the current context. The `StrategicHarmonyBlender` class then blends these results based on their weights to achieve a balanced outcome.