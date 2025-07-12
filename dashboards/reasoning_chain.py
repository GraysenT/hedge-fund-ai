```python
def evaluate_criteria(criteria):
    """
    Evaluates the given criteria and returns a score.
    """
    score = 0
    for criterion, value in criteria.items():
        if criterion == "cost":
            if value <= 1000:
                score += 3
            elif value <= 5000:
                score += 2
            else:
                score += 1
        elif criterion == "performance":
            if value >= 9:
                score += 3
            elif value >= 7:
                score += 2
            else:
                score += 1
        elif criterion == "reliability":
            if value >= 95:
                score += 3
            elif value >= 90:
                score += 2
            else:
                score += 1
    return score

def compare_options(option1, option2):
    """
    Compares two options based on their scores and returns the better option.
    """
    score1 = evaluate_criteria(option1)
    score2 = evaluate_criteria(option2)
    
    if score1 > score2:
        return "Option 1 is better", score1, score2
    elif score2 > score1:
        return "Option 2 is better", score1, score2
    else:
        return "Both options are equally good", score1, score2

# Define the criteria for each option
option1_criteria = {"cost": 3000, "performance": 8, "reliability": 92}
option2_criteria = {"cost": 4500, "performance": 9, "reliability": 90}

# Compare the two options
decision, score1, score2 = compare_options(option1_criteria, option2_criteria)

# Print the decision and the scores
print(decision)
print("Score of Option 1:", score1)
print("Score of Option 2:", score2)
```