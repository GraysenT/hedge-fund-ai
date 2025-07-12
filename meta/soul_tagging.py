```python
# Importing necessary libraries
import pandas as pd
import numpy as np

# Sample data: List of modules with some attributes
data = {
    'Module': ['Authentication', 'Payment Gateway', 'User Profile', 'Inventory Management', 'Shipping'],
    'Purpose': ['Login and security', 'Handling transactions', 'Store user data', 'Manage stock', 'Manage deliveries'],
    'Origin': ['Internal', 'External', 'Internal', 'Internal', 'External'],
    'Strategy Family': ['Security', 'Financial', 'Data Handling', 'Logistics', 'Logistics'],
    'Risk Class': ['High', 'Critical', 'Medium', 'High', 'Medium']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
```