```python
class SystemPriorities:
    PURPOSE = 1
    STABILITY = 2
    RESILIENCE = 3
    PROFIT = 4

def decision_making(input_data, priority):
    if priority == SystemPriorities.PURPOSE:
        return prioritize_purpose(input_data)
    elif priority == SystemPriorities.STABILITY:
        return prioritize_stability(input_data)
    elif priority == SystemPriorities.RESILIENCE:
        return prioritize_resilience(input_data)
    elif priority == SystemPriorities.PROFIT:
        return prioritize_profit(input_data)
    else:
        raise ValueError("Invalid priority")

def prioritize_purpose(data):
    # Logic to prioritize purpose
    return f"Action based on purpose for {data}"

def prioritize_stability(data):
    # Logic to prioritize stability
    return f"Action based on stability for {data}"

def prioritize_resilience(data):
    # Logic to prioritize resilience
    return f"Action based on resilience for {data}"

def prioritize_profit(data):
    # Logic to prioritize profit
    return f"Action based on profit for {data}"

# Example usage
input_data = "System Input"
priority = SystemPriorities.PURPOSE
result = decision_making(input_data, priority)
print(result)
```