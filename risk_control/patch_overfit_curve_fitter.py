```python
# File: risk_control/patch_overfit_curve_fitter.py

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

class PatchOverfitCurveFitter:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.model = Ridge(alpha=self.alpha)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)

    def cross_val_score(self, X, y, cv=5):
        return cross_val_score(self.model, X, y, cv=cv)

if __name__ == "__main__":
    # Example usage
    X = np.random.rand(100, 1)
    y = 3 * X.squeeze() + 2 + np.random.randn(100)

    patch_overfit_curve_fitter = PatchOverfitCurveFitter(alpha=0.5)
    patch_overfit_curve_fitter.fit(X, y)

    print("Model score: ", patch_overfit_curve_fitter.score(X, y))
    print("Cross validation score: ", patch_overfit_curve_fitter.cross_val_score(X, y, cv=5))
```

This module provides a class `PatchOverfitCurveFitter` that uses Ridge Regression to add a risk constraint to the overfitting-prone curve fitting process. The `alpha` parameter controls the strength of the regularization, and can be tuned to balance the trade-off between bias and variance. The `fit`, `predict`, `score`, and `cross_val_score` methods provide a familiar interface for users of scikit-learn. The example usage demonstrates how to create an instance of the class, fit it to data, and evaluate its performance.