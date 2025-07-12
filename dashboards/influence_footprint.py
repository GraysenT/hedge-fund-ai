Here is a Python script that uses a simple linear regression model to estimate the effect of a system's output on external market behavior. This example assumes you have historical data of system outputs and corresponding market responses. The script uses the `scikit-learn` library to create and train the model.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Example data: replace this with your actual data source
# Assuming 'system_output' is the output of your system and 'market_response' is the market behavior
data = {
    'system_output': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'market_response': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Features (independent variables)
X = df[['system_output']]

# Target variable (dependent variable)
y = df['market_response']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Displaying the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Using the model to predict a new market response
new_system_output = np.array([[110]])  # Example new system output
predicted_market_response = model.predict(new_system_output)
print("Predicted Market Response for System Output 110:", predicted_market_response[0])
```

This script:
1. Creates a dataset.
2. Splits the dataset into training and testing sets.
3. Trains a linear regression model on the training data.
4. Evaluates the model using the test data.
5. Prints out the mean squared error and R² score to assess the model's performance.
6. Displays the model's coefficients and intercept.
7. Predicts the market response for a new system output.

Replace the example data with your actual dataset to use this script effectively in a real-world scenario.