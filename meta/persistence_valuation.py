```python
import numpy as np

def discount_future_utilities(future_utilities, discount_rate):
    """
    Calculate the present value of future utilities using a discount rate.
    
    Parameters:
        future_utilities (list of float): The list of future utilities.
        discount_rate (float): The discount rate per period.
    
    Returns:
        float: The present value of the future utilities.
    """
    discounted_utilities = [
        utility / ((1 + discount_rate) ** t) for t, utility in enumerate(future_utilities)
    ]
    return sum(discounted_utilities)

def legacy_value(legacy_utilities):
    """
    Calculate the total value of past utilities (legacy).
    
    Parameters:
        legacy_utilities (list of float): The list of past utilities.
    
    Returns:
        float: The total value of the legacy utilities.
    """
    return sum(legacy_utilities)

def evaluate_agent_value(legacy_utilities, future_utilities, discount_rate):
    """
    Evaluate the long-term value of an agent based on its legacy and future utility.
    
    Parameters:
        legacy_utilities (list of float): The list of past utilities.
        future_utilities (list of float): The list of future utilities.
        discount_rate (float): The discount rate per period for future utilities.
    
    Returns:
        float: The total value of the agent combining legacy and discounted future utilities.
    """
    legacy_val = legacy_value(legacy_utilities)
    future_val = discount_future_utilities(future_utilities, discount_rate)
    total_value = legacy_val + future_val
    return total_value

# Example usage:
legacy_utilities = [10, 15, 20]  # Past utilities
future_utilities = [25, 30, 35, 40]  # Predicted future utilities
discount_rate = 0.05  # 5% discount rate

total_agent_value = evaluate_agent_value(legacy_utilities, future_utilities, discount_rate)
print("Total Agent Value:", total_agent_value)
```