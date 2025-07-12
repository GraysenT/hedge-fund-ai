The following Python code demonstrates a simple way to detect undue pressure or bias in a system, which could be influenced by internal politics or external inputs. This example uses a hypothetical scenario where the system receives inputs (e.g., decisions, ratings) from various sources, and we need to check if these inputs deviate significantly from the norm, which might indicate bias or undue pressure.

We'll use statistical methods to detect outliers, which could be indicative of bias. The Z-score method is one approach to identify outliers in the data, which are data points that are far away from the mean. High Z-scores (e.g., above 3 or below -3) indicate potential undue influence.

```python
import numpy as np
from scipy.stats import zscore

# Example data: ratings or decisions from different sources
data = np.array([85, 87, 86, 88, 90, 85, 84, 110, 83, 82, 85, 87])

# Calculate Z-scores of the data
z_scores = zscore(data)

# Define a threshold for identifying outliers
threshold = 3

# Detect potential undue pressure or bias
outliers = np.where(np.abs(z_scores) > threshold)
outlier_values = data[outliers]

print("Data: ", data)
print("Z-scores: ", z_scores)
print("Outliers indicating potential bias or undue pressure: ", outlier_values)
```

### Explanation:
1. **Data Collection**: The `data` array represents inputs from various sources, which could be ratings, decisions, or any numerical input susceptible to bias.
2. **Z-score Calculation**: `zscore(data)` computes the Z-score for each data point, which measures how many standard deviations an element is from the mean.
3. **Outlier Detection**: Outliers are detected by checking where the absolute Z-scores exceed the threshold (set at 3). This threshold can be adjusted based on the sensitivity required.
4. **Reporting**: The script prints the original data, the calculated Z-scores, and any values considered outliers, which might indicate undue pressure or bias.

This script can be adapted to monitor various types of numerical inputs and can be integrated into larger systems to continuously monitor for signs of bias or undue influence.