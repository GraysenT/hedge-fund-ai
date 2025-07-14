Below is a Python script that uses matplotlib to plot alpha decay curves for different strategies across epochs. The script assumes you have some hypothetical data for alpha values for each strategy at each epoch. You can modify the data as per your actual needs.

```python
import matplotlib.pyplot as plt
import numpy as np

# Example data: Alpha values for different strategies across epochs
epochs = np.arange(1, 11)  # Epochs from 1 to 10
strategy1 = np.exp(-0.1 * epochs)  # Exponential decay for strategy 1
strategy2 = np.exp(-0.2 * epochs)  # Exponential decay for strategy 2
strategy3 = np.exp(-0.3 * epochs)  # Exponential decay for strategy 3

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(epochs, strategy1, label='Strategy 1', marker='o')
plt.plot(epochs, strategy2, label='Strategy 2', marker='s')
plt.plot(epochs, strategy3, label='Strategy 3', marker='^')

# Adding titles and labels
plt.title('Alpha Decay Curves by Strategy')
plt.xlabel('Epoch')
plt.ylabel('Alpha Value')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
```

This script creates a line plot for three strategies showing how the alpha value decays over 10 epochs. Each strategy has a different decay rate. You can adjust the `epochs` and the decay rates in the exponential functions to fit your specific scenario. The use of markers (`o`, `s`, `^`) helps to distinguish between the strategies visually.