```python
import matplotlib.pyplot as plt
import numpy as np

# Define a simple model for a sustainable investment strategy
class SustainableInvestment:
    def __init__(self, initial_investment, growth_rate, sustainability_factor):
        self.initial_investment = initial_investment
        self.growth_rate = growth_rate
        self.sustainability_factor = sustainability_factor

    def calculate_growth(self, years):
        """Calculate investment growth over a number of years considering sustainability."""
        investment_value = self.initial_investment
        values = []
        
        for year in range(years):
            # Investment grows based on growth rate adjusted by sustainability factor
            investment_growth = investment_value * self.growth_rate
            sustainable_growth = investment_growth * self.sustainability_factor
            investment_value += sustainable_growth
            values.append(investment_value)
        
        return values

# Parameters
initial_investment = 1000  # Initial amount invested
growth_rate = 0.07  # Annual growth rate
sustainability_factor = 0.8  # Factor to adjust growth for sustainability

# Create an instance of SustainableInvestment
investment = SustainableInvestment(initial_investment, growth_rate, sustainability_factor)

# Simulate investment growth over 20 years
years = 20
investment_values = investment.calculate_growth(years)

# Plotting the results
years_range = np.arange(1, years + 1)
plt.figure(figsize=(10, 5))
plt.plot(years_range, investment_values, marker='o', linestyle='-', color='b')
plt.title('Sustainable Investment Growth Over 20 Years')
plt.xlabel('Years')
plt.ylabel('Investment Value')
plt.grid(True)
plt.show()
```

This Python code models a sustainable investment strategy where growth is adjusted by a sustainability factor, simulating a more responsible investment approach that may not seek immediate high returns ("alpha") but focuses on long-term sustainability and stability.