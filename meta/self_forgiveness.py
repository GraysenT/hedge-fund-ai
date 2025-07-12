Below is a Python implementation of a mechanism that simulates a strategic decision-making process, incorporates a regret-clearing mechanism, and enables logic learning after a strategic failure. This example uses a simple game scenario where decisions are made based on past outcomes, and learning occurs to improve future decisions.

```python
import random

class StrategicDecisionMaker:
    def __init__(self):
        self.history = []
        self.strategies = ['aggressive', 'defensive', 'balanced']
        self.current_strategy = None

    def choose_strategy(self):
        if not self.history:
            # Choose a random strategy if no history is available
            self.current_strategy = random.choice(self.strategies)
        else:
            # Learn from past failures to adjust the strategy
            self.current_strategy = self.learn_from_failure()
        return self.current_strategy

    def learn_from_failure(self):
        # Analyze past results and choose the best strategy
        strategy_success = {strategy: 0 for strategy in self.strategies}
        
        for outcome in self.history:
            if outcome['result'] == 'win':
                strategy_success[outcome['strategy']] += 1
            else:
                strategy_success[outcome['strategy']] -= 1
        
        # Choose the strategy with the highest score
        return max(strategy_success, key=strategy_success.get)

    def simulate_game(self, strategy):
        # Simulate a game outcome based on the chosen strategy
        # Here, outcomes are simplified to random wins or losses
        return 'win' if random.random() > 0.5 else 'loss'

    def make_decision(self):
        strategy = self.choose_strategy()
        result = self.simulate_game(strategy)
        self.history.append({'strategy': strategy, 'result': result})
        return strategy, result

    def clear_regret(self):
        # Clear history to reset learning and avoid overfitting to past failures
        self.history = []

def main():
    decision_maker = StrategicDecisionMaker()
    
    # Simulate decision making and learning process
    for _ in range(10):
        strategy, result = decision_maker.make_decision()
        print(f"Chosen strategy: {strategy}, Game result: {result}")
    
    # Clear regret and reset history
    decision_maker.clear_regret()
    print("Regret cleared. History reset.")

    # Simulate again after clearing regret
    for _ in range(5):
        strategy, result = decision_maker.make_decision()
        print(f"Chosen strategy: {strategy}, Game result: {result}")

if __name__ == "__main__":
    main()
```

This code defines a `StrategicDecisionMaker` class that can choose strategies based on past outcomes, simulate game results, and learn from failures. The `clear_regret` method resets the history, allowing the decision-making process to start afresh without the bias of past failures. The `main` function demonstrates how this mechanism can be used in practice.