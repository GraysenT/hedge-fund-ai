Below is a Python script that reads options data to calculate skew, convexity, and directional lean from an options surface. The script assumes you have access to options data, which typically includes strike prices, implied volatilities, and other relevant details for different expiration dates.

This example uses synthetic data and pandas for data manipulation, numpy for numerical operations, and matplotlib for plotting the implied volatility surface, which helps visualize skew, convexity, and directional lean.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic options data
np.random.seed(0)
strikes = np.linspace(50, 150, 11)
expirations = np.array([30, 60, 90, 120, 150])  # days to expiration
data = []

for days in expirations:
    for strike in strikes:
        iv = 0.2 - 0.1 * (strike - 100) / 50 + 0.05 * np.random.randn()
        iv = max(iv, 0.05)  # ensure non-negative IV
        data.append([days, strike, iv])

df = pd.DataFrame(data, columns=['Days', 'Strike', 'IV'])

# Pivot table to create a 2D grid of IVs
iv_surface = df.pivot('Days', 'Strike', 'IV')

# Plotting the IV surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(strikes, expirations)
Z = iv_surface.values

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('Strike Price')
ax.set_ylabel('Days to Expiration')
ax.set_zlabel('Implied Volatility')
ax.set_title('Implied Volatility Surface')

plt.show()

# Analyzing skew, convexity, and directional lean
# Skew: Difference in IV between low and high strikes
skew = iv_surface.max(axis=1) - iv_surface.min(axis=1)

# Convexity: Second derivative with respect to strike
second_derivatives = []
for index, row in iv_surface.iterrows():
    coefs = np.polyfit(row.index, row.values, 2)
    second_derivatives.append(coefs[0])  # The quadratic coefficient

iv_surface['Convexity'] = second_derivatives

# Directional Lean: Direction and magnitude of skew
directional_lean = (iv_surface.iloc[:, -3] - iv_surface.iloc[:, 0]) / iv_surface.iloc[:, 0]

# Output results
print("Skew by Expiration:")
print(skew)
print("\nConvexity by Expiration:")
print(iv_surface['Convexity'])
print("\nDirectional Lean by Expiration:")
print(directional_lean)
```

### Explanation:
1. **Data Generation**: Synthetic data for implied volatility (IV) is created based on strike prices and days to expiration. The IV is modeled to decrease as the strike price moves away from an at-the-money value of 100, with some random noise.

2. **IV Surface Plot**: The script plots the IV surface using a 3D plot, where the x-axis represents the strike price, the y-axis represents days to expiration, and the z-axis represents the IV.

3. **Skew Analysis**: Skew is calculated as the difference in IV between the highest and lowest strikes for each expiration.

4. **Convexity Analysis**: Convexity is estimated by fitting a second-degree polynomial to the IVs across strikes for each expiration and extracting the coefficient of the quadratic term.

5. **Directional Lean**: Directional lean is calculated as the relative difference in IV between the first and last strike, indicating whether the IV curve leans towards higher or lower strikes.

This script provides a basic framework and can be adapted to use real market data and more sophisticated models for IV surface analysis.