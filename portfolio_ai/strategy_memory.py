Below is a Python code example that defines a system to store and manage historical allocation, performance, and decay curves for each investment strategy. This example uses classes and dictionaries to manage the data efficiently.

```python
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class Strategy:
    def __init__(self, name):
        self.name = name
        self.allocations = {}  # Dates and allocations
        self.performance = {}  # Dates and performance metrics
        self.decay_curves = {}  # Dates and decay curve data

    def add_allocation(self, date, allocation):
        self.allocations[date] = allocation

    def add_performance(self, date, performance):
        self.performance[date] = performance

    def add_decay_curve(self, date, decay_curve):
        self.decay_curves[date] = decay_curve

    def get_allocation_on(self, date):
        return self.allocations.get(date, None)

    def get_performance_on(self, date):
        return self.performance.get(date, None)

    def plot_decay_curve(self, date):
        decay_curve = self.decay_curves.get(date, None)
        if decay_curve is not None:
            plt.figure(figsize=(10, 5))
            plt.plot(decay_curve, label=f'Decay Curve on {date}')
            plt.title(f'Decay Curve for {self.name} on {date}')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print(f"No decay curve data available for {date}")

class Portfolio:
    def __init__(self):
        self.strategies = {}

    def add_strategy(self, strategy):
        self.strategies[strategy.name] = strategy

    def add_data(self, strategy_name, date, allocation=None, performance=None, decay_curve=None):
        strategy = self.strategies.get(strategy_name)
        if not strategy:
            print(f"Strategy {strategy_name} not found.")
            return

        if allocation is not None:
            strategy.add_allocation(date, allocation)
        if performance is not None:
            strategy.add_performance(date, performance)
        if decay_curve is not None:
            strategy.add_decay_curve(date, decay_curve)

    def get_strategy_info(self, strategy_name, date):
        strategy = self.strategies.get(strategy_name)
        if not strategy:
            print(f"Strategy {strategy_name} not found.")
            return

        allocation = strategy.get_allocation_on(date)
        performance = strategy.get_performance_on(date)
        print(f"Allocation on {date}: {allocation}")
        print(f"Performance on {date}: {performance}")
        strategy.plot_decay_curve(date)

# Example usage
portfolio = Portfolio()
strategy1 = Strategy("Equity Growth")
portfolio.add_strategy(strategy1)

# Simulating data entry
current_date = datetime.now().date()
allocation_data = 50  # 50% allocation
performance_data = 0.05  # 5% performance
decay_curve_data = np.exp(-0.1 * np.arange(100))  # Exponential decay curve

portfolio.add_data("Equity Growth", current_date, allocation_data, performance_data, decay_curve_data)

# Retrieve and plot data
portfolio.get_strategy_info("Equity Growth", current_date)
```

This code defines a `Strategy` class to hold allocation, performance, and decay curve data for each strategy. It also defines a `Portfolio` class to manage multiple strategies. The example demonstrates how to add data to a strategy and retrieve it, including plotting a decay curve. Adjustments can be made to fit specific data structures and requirements.