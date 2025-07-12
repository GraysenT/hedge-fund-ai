```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

class DataPreprocessor:
    def __init__(self, scale_data=True):
        self.scale_data = scale_data
        self.scaler = StandardScaler()

    def preprocess(self, data):
        if self.scale_data:
            data = self.scaler.fit_transform(data)
        return data

class PCAComponent:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.pca = PCA(n_components=self.n_components)

    def reduce_dimensions(self, data):
        reduced_data = self.pca.fit_transform(data)
        return reduced_data

class KMeansCluster:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=self.n_clusters)

    def cluster_data(self, data):
        self.kmeans.fit(data)
        return self.kmeans.labels_

class SystemIntelligence:
    def __init__(self, n_components=2, n_clusters=3, scale_data=True):
        self.data_preprocessor = DataPreprocessor(scale_data=scale_data)
        self.pca_component = PCAComponent(n_components=n_components)
        self.kmeans_cluster = KMeansCluster(n_clusters=n_clusters)

    def process_and_cluster(self, data):
        preprocessed_data = self.data_preprocessor.preprocess(data)
        reduced_data = self.pca_component.reduce_dimensions(preprocessed_data)
        cluster_labels = self.kmeans_cluster.cluster_data(reduced_data)
        return reduced_data, cluster_labels

# Example usage:
if __name__ == "__main__":
    # Load example data
    data = load_iris().data

    # Initialize system intelligence
    system_intelligence = SystemIntelligence(n_components=2, n_clusters=3, scale_data=True)

    # Process and cluster the data
    reduced_data, cluster_labels = system_intelligence.process_and_cluster(data)

    print("Reduced Data Shape:", reduced_data.shape)
    print("Cluster Labels:", cluster_labels)
```

This Python code defines a modular system for processing and clustering data. It includes classes for data preprocessing, dimensionality reduction using PCA, and clustering using KMeans. The `SystemIntelligence` class integrates these components to provide a streamlined workflow for transforming and clustering data. The example usage demonstrates how to apply this system to the Iris dataset.