```python
# Define a function to check if a decision violates system-wide purpose or ethics
def check_decision(decision):
    # Define system-wide purpose and ethical guidelines
    system_purpose = "Serve and protect user data and privacy."
    ethical_guidelines = [
        "Do not harm users.",
        "Ensure user privacy and data protection.",
        "Operate transparently and with accountability."
    ]

    # Define potential violations
    violations = {
        "harm": "Decision may cause harm to users.",
        "privacy": "Decision may violate user privacy.",
        "transparency": "Decision lacks transparency and accountability."
    }

    # Check for violations
    decision_violations = []
    if "harm" in decision:
        decision_violations.append(violations["harm"])
    if "leak" in decision or "sell data" in decision:
        decision_violations.append(violations["privacy"])
    if "hide" in decision or "secret" in decision:
        decision_violations.append(violations["transparency"])

    # Return the result
    if decision_violations:
        return f"Decision violates ethics: {', '.join(decision_violations)}"
    else:
        return "No ethical violations detected."

# Example usage
decision_input = "sell data"
result = check_decision(decision_input)
print(result)
```