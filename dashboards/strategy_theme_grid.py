Below is a Python script that groups and visualizes strategies by macro theme, sector, or regime tag using pandas for data manipulation and matplotlib for visualization. This script assumes you have a dataset containing strategies with their respective tags for macro themes, sectors, or regimes.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: strategies with their respective macro theme, sector, and regime tag
data = {
    'Strategy': ['Strategy A', 'Strategy B', 'Strategy C', 'Strategy D', 'Strategy E'],
    'Macro Theme': ['Economic Growth', 'Market Volatility', 'Economic Growth', 'Inflation', 'Market Volatility'],
    'Sector': ['Technology', 'Finance', 'Healthcare', 'Technology', 'Energy'],
    'Regime Tag': ['Expansion', 'Recession', 'Expansion', 'Stagflation', 'Recession']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to group and visualize strategies
def group_and_visualize(df, group_by):
    grouped = df.groupby(group_by)['Strategy'].apply(list).reset_index()
    
    # Plotting
    fig, ax = plt.subplots()
    themes = grouped[group_by].tolist()
    strategies = grouped['Strategy'].tolist()
    strategies_count = [len(s) for s in strategies]

    ax.bar(themes, strategies_count, color='skyblue')
    ax.set_xlabel(group_by)
    ax.set_ylabel('Number of Strategies')
    ax.set_title(f'Number of Strategies by {group_by}')
    ax.set_xticklabels(themes, rotation=45, ha='right')

    # Annotate the number of strategies on top of each bar
    for i in range(len(themes)):
        ax.text(i, strategies_count[i] + 0.1, str(strategies_count[i]), ha='center')

    plt.show()

# Example usage:
group_and_visualize(df, 'Macro Theme')  # Group by Macro Theme
group_and_visualize(df, 'Sector')       # Group by Sector
group_and_visualize(df, 'Regime Tag')   # Group by Regime Tag
```

This script does the following:
1. Creates a sample dataset with strategies and their tags.
2. Defines a function `group_and_visualize` that:
   - Groups strategies by the specified tag (Macro Theme, Sector, or Regime Tag).
   - Visualizes the number of strategies in each group using a bar chart.
3. Calls the function with different grouping criteria to visualize the distribution of strategies.

Make sure to adjust the dataset and possibly the visualization parameters according to your specific needs and the complexity of your actual data.