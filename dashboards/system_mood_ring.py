Below is a Python script that estimates an 'emotional state' based on three input metrics: volatility, conflict, and regret. The script uses a simple scoring system to determine the emotional state, which could be "Stable", "Concerned", or "Unstable". Each metric is assumed to be a numerical value where higher values indicate higher levels of each respective metric.

```python
def estimate_emotional_state(volatility, conflict, regret):
    # Define thresholds for each metric
    volatility_thresholds = (0.3, 0.7)
    conflict_thresholds = (0.3, 0.7)
    regret_thresholds = (0.3, 0.7)

    # Calculate scores based on thresholds
    volatility_score = 1 if volatility < volatility_thresholds[0] else 2 if volatility < volatility_thresholds[1] else 3
    conflict_score = 1 if conflict < conflict_thresholds[0] else 2 if conflict < conflict_thresholds[1] else 3
    regret_score = 1 if regret < regret_thresholds[0] else 2 if regret < regret_thresholds[1] else 3

    # Calculate total score
    total_score = volatility_score + conflict_score + regret_score

    # Determine emotional state based on total score
    if total_score <= 4:
        emotional_state = "Stable"
    elif total_score <= 7:
        emotional_state = "Concerned"
    else:
        emotional_state = "Unstable"

    return emotional_state

# Example usage
volatility = 0.5  # Example value for volatility
conflict = 0.4    # Example value for conflict
regret = 0.6      # Example value for regret

emotional_state = estimate_emotional_state(volatility, conflict, regret)
print(f"The estimated emotional state is: {emotional_state}")
```

This script defines a function `estimate_emotional_state` that takes three parameters: `volatility`, `conflict`, and `regret`. Each parameter is expected to be a float between 0 and 1. The function calculates a score for each metric based on predefined thresholds, sums these scores, and then determines the emotional state based on the total score. Adjust the thresholds and scoring system as needed to fit specific requirements or to refine the model's sensitivity.