```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Example data: Agent performance in various metrics
data = {
    'AgentID': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'Sales': [200, 150, 340, 120, 240],
    'CustomerSatisfaction': [90, 85, 95, 80, 92],
    'ProductKnowledge': [85, 80, 90, 78, 88],
    'LastCycleRank': [2, 3, 1, 5, 4],
    'WillDominateNextCycle': [0, 0, 1, 0, 1]  # 1 means will dominate, 0 means will not
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['Sales', 'CustomerSatisfaction', 'ProductKnowledge', 'LastCycleRank']]
y = df['WillDominateNextCycle']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Predict which agents are likely to dominate next cycle
predictions = model.predict(X)
df['PredictedDomination'] = predictions

# Output the predictions
print(df[['AgentID', 'PredictedDomination']])
```