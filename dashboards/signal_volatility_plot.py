To create a Python script that charts the volatility of each live signal over time by agent and category, we'll need to simulate or use a dataset containing the relevant information. Since no specific dataset was provided, I'll assume a structure and generate a sample dataset for demonstration purposes. We will use `pandas` for data manipulation and `matplotlib` for plotting.

Here's a Python script that accomplishes this:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate some data
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
agents = ['Agent1', 'Agent2', 'Agent3']
categories = ['Category1', 'Category2', 'Category3']

data = {
    'Date': np.tile(dates, len(agents) * len(categories)),
    'Agent': np.repeat(agents, len(dates) * len(categories)),
    'Category': np.repeat(np.tile(categories, len(agents)), len(dates)),
    'Signal': np.random.randn(len(dates) * len(agents) * len(categories)) * 100
}

df = pd.DataFrame(data)

# Calculate rolling volatility (standard deviation of signals)
window_size = 10  # Define window size for rolling calculation
df['Volatility'] = df.groupby(['Agent', 'Category'])['Signal'].transform(lambda x: x.rolling(window=window_size).std())

# Plotting
fig, axes = plt.subplots(nrows=len(agents), ncols=len(categories), figsize=(15, 10), sharex=True)
fig.suptitle('Volatility of Live Signals Over Time by Agent and Category')

for i, agent in enumerate(agents):
    for j, category in enumerate(categories):
        ax = axes[i][j]
        subset = df[(df['Agent'] == agent) & (df['Category'] == category)]
        ax.plot(subset['Date'], subset['Volatility'], label=f'{agent} - {category}')
        ax.set_title(f'{agent} - {category}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Volatility')
        ax.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
```

### Explanation:
1. **Data Simulation**: We create a dataset with random signals for three agents and three categories over 100 days.
2. **Volatility Calculation**: We calculate the rolling volatility using a window size of 10 days. Volatility is computed as the standard deviation of the signal values within the window.
3. **Plotting**: We create a subplot for each combination of agent and category. Each subplot shows how the volatility of the signals changes over time.

This script assumes you have `pandas`, `numpy`, and `matplotlib` installed. If not, you can install them using pip:

```bash
pip install pandas numpy matplotlib
```

Adjust the `window_size` or other parameters as needed to fit the specific requirements or characteristics of your actual dataset.