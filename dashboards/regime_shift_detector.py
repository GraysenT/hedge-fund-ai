Below is a Python script that simulates monitoring and detecting transitions in macroeconomic regimes using synthetic data. The script uses a simple regime-switching model approach with two states (e.g., growth and recession) and generates a live plot that updates in real-time to show the current regime and any recent transitions.

To implement this, we'll use libraries such as `numpy` for numerical operations, `matplotlib` for plotting, and `time` to simulate real-time data flow. This example assumes a simplistic random generation of macro states to illustrate the concept:

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Parameters
states = ['Growth', 'Recession']
state_colors = {'Growth': 'green', 'Recession': 'red'}
transition_probabilities = np.array([
    [0.90, 0.10],  # Probability of staying in Growth or switching to Recession
    [0.15, 0.85]   # Probability of switching to Growth or staying in Recession
])

# Initial state
current_state_idx = np.random.choice([0, 1])

# History of states
state_history = [current_state_idx]

def update_state():
    global current_state_idx
    current_state_idx = np.random.choice([0, 1], p=transition_probabilities[current_state_idx])
    state_history.append(current_state_idx)

def animate(i):
    update_state()
    
    # Clear the current plot
    plt.cla()
    
    # Plot the history of states
    colors = [state_colors[states[s]] for s in state_history[-50:]]  # Last 50 states
    plt.bar(range(len(state_history[-50:])), [1]*50, color=colors)
    
    plt.ylim(0, 1)
    plt.title('Live View of Macroeconomic Regime')
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.xticks([])
    plt.xlabel('Time (latest 50 observations on the right)')
    plt.ylabel('State')

fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=1000)  # Update every second

plt.show()
```

This script sets up a regime-switching model with two states and simulates transitions between these states based on predefined probabilities. The matplotlib animation module is used to update the plot in real-time, showing the last 50 observed states as a bar plot where the color indicates the current macroeconomic regime.

To run this script, ensure you have the necessary Python environment with `matplotlib` and `numpy` installed. This example is purely illustrative and uses random transitions; in a real-world scenario, you would replace the random state generation with real macroeconomic data analysis and state detection logic.