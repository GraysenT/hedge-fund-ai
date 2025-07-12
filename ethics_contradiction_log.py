```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='ethical_violations.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define ethical rules as a dictionary
ethical_rules = {
    "privacy": "Do not disclose personal information.",
    "fairness": "Treat all individuals equally.",
    "transparency": "Be open about decision-making processes.",
    "accountability": "Be responsible for decisions and their impacts."
}

# Function to check decisions against ethical rules
def check_decision(decision, context):
    violations = []
    for rule, description in ethical_rules.items():
        if rule in context and not context[rule]:
            violations.append(rule)
    return violations

# Function to log violations
def log_violations(decision, violations):
    for violation in violations:
        logging.info(f"Violation of {violation}: {ethical_rules[violation]} in decision: {decision}")

# Example usage
decision = "Implement user tracking without consent"
context = {
    "privacy": False,  # False indicates the decision violates the privacy rule
    "fairness": True,
    "transparency": True,
    "accountability": True
}

violations = check_decision(decision, context)
if violations:
    log_violations(decision, violations)
```

This Python code sets up a logging system to record any ethical violations based on predefined rules. It checks decisions against these rules and logs any violations to a file named `ethical_violations.log`.