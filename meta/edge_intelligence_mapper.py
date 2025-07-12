```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation

def generate_artificial_intelligence_map(size=(100, 100), threshold=0.5):
    """
    Generates a random map of explored intelligence areas.
    """
    np.random.seed(0)
    return np.random.rand(*size) > threshold

def find_intelligence_boundary(intelligence_map):
    """
    Identifies the boundary of the explored intelligence areas.
    """
    struct = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])
    dilated_map = binary_dilation(intelligence_map, structure=struct)
    boundary_map = dilated_map & ~intelligence_map
    return boundary_map

def plot_intelligence_map(intelligence_map, boundary_map):
    """
    Plots the intelligence map and its boundary.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(intelligence_map, cmap='gray', interpolation='none')
    plt.contour(boundary_map, colors='red', linewidths=1.5)
    plt.title('Intelligence Map and Boundary')
    plt.show()

# Generate the map of current intelligence
intelligence_map = generate_artificial_intelligence_map()

# Find the boundary of the explored intelligence
boundary_map = find_intelligence_boundary(intelligence_map)

# Plot the map and the boundary
plot_intelligence_map(intelligence_map, boundary_map)
```