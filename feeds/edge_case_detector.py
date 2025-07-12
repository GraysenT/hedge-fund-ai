```python
import pandas as pd

def detect_rare_conditions(data, threshold=0.05):
    """
    Detects rare data conditions in a DataFrame based on a given threshold for categorical columns.
    
    Parameters:
        data (pd.DataFrame): The DataFrame to analyze.
        threshold (float): The threshold to consider a value as rare. Default is 0.05 (5%).
    
    Returns:
        dict: A dictionary with column names as keys and lists of rare values as values.
    """
    rare_conditions = {}
    for column in data.columns:
        if data[column].dtype == 'object' or pd.api.types.is_categorical_dtype(data[column]):
            value_counts = data[column].value_counts(normalize=True)
            rare_values = value_counts[value_counts < threshold].index.tolist()
            if rare_values:
                rare_conditions[column] = rare_values
    return rare_conditions

def detect_risky_conditions(data, custom_conditions):
    """
    Detects risky data conditions based on custom conditions provided by the user.
    
    Parameters:
        data (pd.DataFrame): The DataFrame to analyze.
        custom_conditions (dict): A dictionary with column names as keys and functions that define risky conditions as values.
    
    Returns:
        dict: A dictionary with column names as keys and DataFrames of risky data as values.
    """
    risky_conditions = {}
    for column, condition_func in custom_conditions.items():
        risky_data = data[data[column].apply(condition_func)]
        if not risky_data.empty:
            risky_conditions[column] = risky_data
    return risky_conditions

# Example usage:
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'Age': [25, 30, 45, 60, 100, 110, 20, 30, 90],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female'],
        'Income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000]
    })

    # Detect rare conditions
    rare_conditions = detect_rare_conditions(data, threshold=0.1)
    print("Rare conditions found:")
    print(rare_conditions)

    # Define custom risky conditions
    custom_conditions = {
        'Age': lambda x: x > 100,  # Age greater than 100 might be considered risky or erroneous
        'Income': lambda x: x > 120000  # Income unusually high might be risky or erroneous
    }

    # Detect risky conditions
    risky_conditions = detect_risky_conditions(data, custom_conditions)
    print("Risky conditions found:")
    for column, risky_data in risky_conditions.items():
        print(f"Column: {column}")
        print(risky_data)
```