```python
import numpy as np

def combine_features(*feature_sources):
    """
    Combine multiple sources of features into a unified feature vector.
    
    Parameters:
    *feature_sources: variable number of arrays/lists where each represents a source of features.
    
    Returns:
    numpy.ndarray: A unified feature vector.
    """
    # Concatenate all feature sources along the last axis
    unified_features = np.concatenate([np.asarray(features) for features in feature_sources], axis=-1)
    return unified_features

# Example usage:
# Assuming we have features from three different sources
features_source1 = np.array([[1, 2], [3, 4]])
features_source2 = np.array([[5, 6], [7, 8]])
features_source3 = np.array([[9, 10], [11, 12]])

# Combine features
combined_features = combine_features(features_source1, features_source2, features_source3)
print("Combined Features:\n", combined_features)
```