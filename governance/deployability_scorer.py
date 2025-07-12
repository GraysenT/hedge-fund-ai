```python
import pandas as pd

def evaluate_modules(data, thresholds):
    """
    Evaluate each module based on provided thresholds and determine if they are eligible for deployment.

    Args:
    data (pd.DataFrame): DataFrame containing module scores.
    thresholds (dict): Dictionary with module names as keys and minimum score thresholds as values.

    Returns:
    pd.DataFrame: DataFrame indicating eligibility of each module for deployment.
    """
    # Initialize a DataFrame to store eligibility results
    results = pd.DataFrame(index=data.index)
    
    # Iterate through each threshold and determine eligibility
    for module, threshold in thresholds.items():
        if module in data.columns:
            results[f"{module}_eligible"] = data[module] >= threshold
        else:
            results[f"{module}_eligible"] = False  # Mark as False if module score is not present

    return results

# Example usage:
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'ModuleA': [75, 88, 90, 65, 70],
        'ModuleB': [80, 85, 88, 90, 95],
        'ModuleC': [50, 60, 55, 65, 70]
    })

    # Thresholds for each module
    thresholds = {
        'ModuleA': 70,
        'ModuleB': 85,
        'ModuleC': 60
    }

    # Evaluate modules
    eligibility_results = evaluate_modules(data, thresholds)
    print(eligibility_results)
```