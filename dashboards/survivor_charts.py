Below is a Python script that uses matplotlib and pandas to plot the top surviving modules, strategies, and alpha builders over time. This example assumes you have data in a CSV format with columns for time, module names, strategy names, alpha builder names, and their respective survival scores or counts. Adjust the data reading and processing parts as per your actual data structure.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Assuming the CSV has columns 'Time', 'Module', 'Strategy', 'AlphaBuilder', 'ModuleScore', 'StrategyScore', 'AlphaBuilderScore'
# You might need to adjust column names based on your actual data

# Group by time and module, strategy, alpha builder and sum the scores or counts
module_data = data.groupby(['Time', 'Module']).sum()['ModuleScore'].reset_index()
strategy_data = data.groupby(['Time', 'Strategy']).sum()['StrategyScore'].reset_index()
alpha_builder_data = data.groupby(['Time', 'AlphaBuilder']).sum()['AlphaBuilderScore'].reset_index()

# Function to plot top N items over time
def plot_top_items_over_time(df, time_col, item_col, score_col, top_n, title, ax):
    top_items = df.groupby(item_col).sum().nlargest(top_n, score_col).index
    filtered_df = df[df[item_col].isin(top_items)]
    pivot_df = filtered_df.pivot(index=time_col, columns=item_col, values=score_col)
    pivot_df.plot(ax=ax)
    ax.set_title(title)
    ax.set_xlabel('Time')
    ax.set_ylabel('Score')
    ax.legend(title=item_col)

# Create subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))

# Plot top 5 modules, strategies, and alpha builders over time
plot_top_items_over_time(module_data, 'Time', 'Module', 'ModuleScore', 5, 'Top 5 Modules Over Time', axes[0])
plot_top_items_over_time(strategy_data, 'Time', 'Strategy', 'StrategyScore', 5, 'Top 5 Strategies Over Time', axes[1])
plot_top_items_over_time(alpha_builder_data, 'Time', 'AlphaBuilder', 'AlphaBuilderScore', 5, 'Top 5 Alpha Builders Over Time', axes[2])

# Adjust layout
plt.tight_layout()
plt.show()
```

### Explanation:
1. **Data Loading**: The script starts by loading data from a CSV file.
2. **Data Grouping**: It groups the data by 'Time' and the respective categories ('Module', 'Strategy', 'AlphaBuilder'), summing up their scores.
3. **Plotting Function**: `plot_top_items_over_time` is a function designed to filter and plot the top N items in each category over time.
4. **Plotting**: It creates three subplots for modules, strategies, and alpha builders, showing the top 5 in each category over time based on their scores.
5. **Visualization**: Uses matplotlib to create line plots for each category, adjusting the layout for better readability.

Make sure to adjust the column names and file path according to your actual data setup. This script assumes a specific structure but can be adapted to various data formats.