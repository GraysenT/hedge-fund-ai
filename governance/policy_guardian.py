```python
class SafetyModule:
    def __init__(self, policy_rules):
        self.policy_rules = policy_rules

    def check_compliance(self, action, context):
        for rule in self.policy_rules:
            if not rule(action, context):
                return False
        return True

    def override_action(self, action, context):
        if self.check_compliance(action, context):
            return action
        else:
            return self.safe_alternative(action, context)

    def safe_alternative(self, action, context):
        # Define a safe default action
        return "default_safe_action"

def policy_rule_1(action, context):
    # Example rule: Ensure no action is harmful
    return not context.get('is_harmful', False)

def policy_rule_2(action, context):
    # Example rule: Ensure action is allowed under current conditions
    return context.get('is_allowed', True)

# Example usage
safety_module = SafetyModule([policy_rule_1, policy_rule_2])
action = "example_action"
context = {"is_harmful": False, "is_allowed": True}

safe_action = safety_module.override_action(action, context)
print(f"Action taken: {safe_action}")
```