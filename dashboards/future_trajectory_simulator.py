```python
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Sample data: Year and number of projects in technology
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Projects': [120, 150, 180, 220, 260, 300, 340, 380]
}

df = pd.DataFrame(data)

# Reshape data for modeling
X = df['Year'].values.reshape(-1, 1)
y = df['Projects'].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future trends
future_years = np.array([2023, 2024, 2025, 2026, 2027]).reshape(-1, 1)
future_projects = model.predict(future_years)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.scatter(X, y, color='blue', label='Historical Data')
plt.plot(X, model.predict(X), color='green', linestyle='-', label='Trend Line')
plt.scatter(future_years, future_projects, color='red', label='Future Projections')
plt.title('Project Evolution Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Projects')
plt.legend()
plt.grid(True)
plt.show()
```