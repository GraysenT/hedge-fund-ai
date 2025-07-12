```python
def evaluate_system_resilience(recovery_score, regeneration_score, persistence_score):
    """
    Evaluates the overall resilience of a system based on three components:
    recovery, regeneration, and persistence.

    Args:
    recovery_score (int): Score indicating how well the system can recover from disruptions (0-100).
    regeneration_score (int): Score indicating the system's ability to regenerate after damage (0-100).
    persistence_score (int): Score indicating the system's ability to persist under continuous stress (0-100).

    Returns:
    str: A string rating of the system's overall resilience.
    """
    if not all(isinstance(score, int) for score in [recovery_score, regeneration_score, persistence_score]):
        return "Invalid input: All scores must be integers."

    if not all(0 <= score <= 100 for score in [recovery_score, regeneration_score, persistence_score]):
        return "Invalid input: Scores must be between 0 and 100."

    average_score = (recovery_score + regeneration_score + persistence_score) / 3

    if average_score >= 80:
        return "Highly Resilient"
    elif average_score >= 50:
        return "Moderately Resilient"
    else:
        return "Low Resilience"

# Example usage:
print(evaluate_system_resilience(85, 90, 80))  # Output: Highly Resilient
print(evaluate_system_resilience(60, 50, 55))  # Output: Moderately Resilient
print(evaluate_system_resilience(30, 40, 35))  # Output: Low Resilience
```
This Python function evaluates the resilience of a system based on three scores: recovery, regeneration, and persistence. It returns a string describing the system's resilience level.