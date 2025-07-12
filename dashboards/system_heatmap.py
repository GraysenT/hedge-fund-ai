Below is a Python script that creates a live heatmap using Matplotlib and Seaborn to visualize strategy activity, capital, and logic churn. This example assumes you have a data source that updates these metrics in real-time, which could be a database, API, or any other data stream. For simplicity, I'll simulate real-time data updates using random numbers.

You'll need to install the following packages if you haven't already:
```bash
pip install matplotlib seaborn numpy pandas
```

Here's the Python code:

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simulating real-time data updates
def get_realtime_data():
    # Simulate data: 3 strategies, 3 metrics (activity, capital, logic churn)
    data = np.random.rand(3, 3) * 100
    columns = ['Strategy Activity', 'Capital', 'Logic Churn']
    index = ['Strategy 1', 'Strategy 2', 'Strategy 3']
    return pd.DataFrame(data, columns=columns, index=index)

def update(frame):
    data = get_realtime_data()
    sns.heatmap(data, annot=True, fmt=".1f", cmap='coolwarm', ax=ax)
    ax.set_title('Live Heatmap of Strategy Metrics')
    plt.draw()

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create an animation
ani = FuncAnimation(fig, update, interval=1000)  # Update every second

plt.show()
```

### Explanation:
1. **get_realtime_data function**: This function simulates the generation of real-time data. In a real-world scenario, you would replace this function's content with the code to fetch data from your actual data source.

2. **update function**: This function is called periodically by the animation. It fetches new data, creates a heatmap from it, and updates the plot.

3. **FuncAnimation**: This is used to animate the heatmap. It calls the `update` function every 1000 milliseconds (i.e., every second).

4. **sns.heatmap**: This function from Seaborn creates the heatmap. It's called with `annot=True` to annotate cells with the numeric values, `fmt=".1f"` to format the numbers to one decimal place, and `cmap='coolwarm'` for the color mapping.

This script will continuously update the heatmap every second, showing changes in strategy activity, capital, and logic churn in real-time. Adjust the `interval` parameter in `FuncAnimation` for faster or slower updates.