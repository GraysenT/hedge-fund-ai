```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

def predict_sales(data, num_clusters):
    """
    Predicts future sales based on clustering similar historical data points and using linear regression within each cluster.

    Parameters:
    - data (list of tuples): Each tuple contains (feature_vector, sales), where feature_vector is a list of features and sales is the sales value.

    Returns:
    - list of predicted sales values for each input data point.
    """

    # Extract features and sales from the data
    features = np.array([d[0] for d in data])
    sales = np.array([d[1] for d in data])

    # Clustering
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(features)

    # Prepare to store predictions
    predictions = np.zeros_like(sales)

    # Apply Linear Regression within each cluster
    for cluster in range(num_clusters):
        cluster_indices = np.where(clusters == cluster)[0]
        cluster_features = features[cluster_indices]
        cluster_sales = sales[cluster_indices]

        if len(cluster_indices) > 1:  # Need at least two points to fit linear regression
            model = LinearRegression()
            model.fit(cluster_features, cluster_sales)
            predictions[cluster_indices] = model.predict(cluster_features)
        else:
            # If only one point in the cluster, use its own sales value as prediction
            predictions[cluster_indices] = cluster_sales

    return predictions.tolist()

# Example usage:
data = [
    ([1.0, 2.0, 3.0], 200),
    ([1.1, 2.1, 3.1], 220),
    ([0.9, 1.9, 2.9], 180),
    ([7.0, 8.0, 9.0], 800),
    ([7.1, 8.1, 9.1], 820),
    ([6.9, 7.9, 8.9], 780)
]

num_clusters = 2
predicted_sales = predict_sales(data, num_clusters)
print("Predicted Sales:", predicted_sales)
```