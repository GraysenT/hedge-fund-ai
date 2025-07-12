```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data for recursion levels and intelligence scores
recursion_levels = np.array([1, 2, 3, 4, 5])
intelligence_scores = np.array([70, 75, 80, 85, 90])
health_scores = np.array([65, 68, 72, 76, 79])

def plot_dashboard(recursion_levels, intelligence_scores, health_scores):
    fig, ax1 = plt.subplots()

    # Plotting intelligence scores
    color = 'tab:red'
    ax1.set_xlabel('Recursion Level')
    ax1.set_ylabel('Intelligence Score', color=color)
    ax1.plot(recursion_levels, intelligence_scores, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Creating a twin axis for health scores
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Health Score', color=color)
    ax2.plot(recursion_levels, health_scores, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # Adding a title and a legend
    plt.title('Meta-level Health and Growth Score Dashboard')
    fig.tight_layout()
    plt.show()

plot_dashboard(recursion_levels, intelligence_scores, health_scores)
```