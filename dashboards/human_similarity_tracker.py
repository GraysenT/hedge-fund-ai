```python
from sklearn.metrics import accuracy_score

# Example data: human decisions and system decisions
human_decisions = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
system_decisions = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]

# Calculate the accuracy of system decisions against human decisions
accuracy = accuracy_score(human_decisions, system_decisions)

print(f"Accuracy of system decisions compared to human intuition: {accuracy:.2f}")
```