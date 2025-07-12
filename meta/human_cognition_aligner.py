```python
import numpy as np
import matplotlib.pyplot as plt

def plot_decision_boundaries(X, y, model):
    """
    Function to plot decision boundaries of a classifier.
    
    Parameters:
    - X: Features data
    - y: Target labels
    - model: Trained classifier model
    """
    # Create a mesh grid based on data limits
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    # Predict classifications for each point in the mesh grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=20)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')
    plt.show()

def interpret_model_decision(X, y, model, feature_names):
    """
    Function to interpret model decisions using feature importance.
    
    Parameters:
    - X: Features data
    - y: Target labels
    - model: Trained classifier model
    - feature_names: List of feature names
    """
    # Check if the model has attribute 'feature_importances_'
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        # Print the feature ranking
        print("Feature ranking:")
        for f in range(X.shape[1]):
            print(f"{f + 1}. feature {feature_names[indices[f]]} ({importances[indices[f]]:.3f})")
    else:
        print("The model does not support feature importance.")

# Example usage:
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic data
X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)
feature_names = ['Feature 1', 'Feature 2']

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X, y)

# Plot decision boundaries
plot_decision_boundaries(X, y, model)

# Interpret model decisions
interpret_model_decision(X, y, model, feature_names)
```