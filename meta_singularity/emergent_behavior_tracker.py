```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class BehaviorDetector:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=self.n_clusters)

    def fit(self, data):
        """
        Fit the KMeans model to the data.
        """
        self.kmeans.fit(data)
        self.labels = self.kmeans.labels_
        self.centers = self.kmeans.cluster_centers_

    def predict(self, data):
        """
        Predict the closest cluster each sample in data belongs to.
        """
        return self.kmeans.predict(data)

    def detect_new_behaviors(self, data, threshold=0.1):
        """
        Detect new behaviors by finding data points that are significantly far from any cluster centers.
        """
        distances = self.kmeans.transform(data)
        min_distances = np.min(distances, axis=1)
        threshold_distance = np.max(min_distances) * (1 + threshold)
        new_behaviors = data[min_distances > threshold_distance]
        return new_behaviors

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(42)
    data1 = np.random.normal(loc=0, scale=1, size=(100, 2))
    data2 = np.random.normal(loc=5, scale=1, size=(100, 2))
    data3 = np.random.normal(loc=10, scale=1, size=(100, 2))
    data = np.vstack((data1, data2, data3))

    # Add some new behavior data
    new_behavior_data = np.random.normal(loc=20, scale=1, size=(10, 2))
    data_with_new = np.vstack((data, new_behavior_data))

    # Initialize and fit the detector
    detector = BehaviorDetector(n_clusters=3)
    detector.fit(data)

    # Detect new behaviors
    new_behaviors = detector.detect_new_behaviors(data_with_new)
    print("Detected new behaviors:\n", new_behaviors)
```