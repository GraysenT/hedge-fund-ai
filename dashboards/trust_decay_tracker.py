```python
import matplotlib.pyplot as plt
import numpy as np

# Data: Trust levels over time for different chart modules
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
trust_levels = {
    'matplotlib': np.array([80, 78, 75, 73, 70, 68, 65]),
    'seaborn': np.array([0, 20, 40, 55, 60, 62, 63]),
    'plotly': np.array([0, 0, 10, 30, 50, 65, 70]),
    'bokeh': np.array([0, 0, 5, 20, 35, 45, 50])
}

# Plotting
plt.figure(figsize=(10, 6))
for module, trust in trust_levels.items():
    plt.plot(years, trust, label=module, marker='o')

plt.title('Trust Levels in Chart Modules Over Time')
plt.xlabel('Year')
plt.ylabel('Trust Level (%)')
plt.legend(title='Chart Modules')
plt.grid(True)
plt.show()
```