Below is a Python code example that uses a simple machine learning model to classify signals into four regimes: momentum, mean-reversion, volatility, or sentiment. This example uses a decision tree classifier, which is suitable for handling categorical data and easy to interpret.

First, you'll need to install the necessary library, `scikit-learn`, if you haven't already:

```bash
pip install scikit-learn
```

Here's the Python code:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Example data generation
def generate_data(n_samples=1000):
    np.random.seed(0)
    data = {
        'signal_strength': np.random.rand(n_samples),
        'signal_frequency': np.random.randint(1, 10, n_samples),
        'signal_volatility': np.random.rand(n_samples),
        'previous_returns': np.random.randn(n_samples),
        'regime': np.random.choice(['momentum', 'mean-reversion', 'volatility', 'sentiment'], n_samples)
    }
    return pd.DataFrame(data)

# Prepare the data
df = generate_data()
X = df[['signal_strength', 'signal_frequency', 'signal_volatility', 'previous_returns']]
y = df['regime']

# Encode the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Create and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Example of predicting a new data point
new_data = np.array([[0.5, 5, 0.3, 0.1]])  # Example new data point
new_prediction = model.predict(new_data)
print("Predicted regime for new data point:", label_encoder.inverse_transform(new_prediction)[0])
```

### Explanation:
1. **Data Generation**: The `generate_data` function creates a synthetic dataset with features that might represent different aspects of trading signals and a target variable 'regime' with four categories.

2. **Data Preparation**: The features are extracted into `X` and the target into `y`. The target variable is encoded into numeric format using `LabelEncoder`.

3. **Model Training**: The data is split into training and testing sets. A `DecisionTreeClassifier` is trained on the training data.

4. **Model Evaluation**: The trained model is used to predict the regimes on the test set, and the predictions are evaluated using accuracy and a classification report.

5. **Prediction**: The model is used to predict the regime for a new data point.

This code serves as a basic framework and should be adapted and expanded based on the specific characteristics and quality of your real-world data.