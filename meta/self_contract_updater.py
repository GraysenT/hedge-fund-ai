```python
# Define the class to manage internal rules and contracts
class SystemRules:
    def __init__(self):
        # Initialize with default rules and contracts
        self.rules = {
            "data_privacy": "strict",
            "user_interaction": "polite",
            "error_handling": "robust"
        }
        self.contracts = {
            "service_level": "high",
            "uptime": "99.9%"
        }

    def update_rule(self, rule_name, new_value):
        # Update a specific rule
        if rule_name in self.rules:
            self.rules[rule_name] = new_value
            print(f"Rule '{rule_name}' updated to '{new_value}'.")
        else:
            print(f"Rule '{rule_name}' does not exist.")

    def update_contract(self, contract_name, new_value):
        # Update a specific contract
        if contract_name in self.contracts:
            self.contracts[contract_name] = new_value
            print(f"Contract '{contract_name}' updated to '{new_value}'.")
        else:
            print(f"Contract '{contract_name}' does not exist.")

    def display_rules(self):
        # Display all current rules
        print("Current System Rules:")
        for rule, value in self.rules.items():
            print(f"{rule}: {value}")

    def display_contracts(self):
        # Display all current contracts
        print("Current System Contracts:")
        for contract, value in self.contracts.items():
            print(f"{contract}: {value}")

# Example usage
system_rules = SystemRules()

# Display current rules and contracts
system_rules.display_rules()
system_rules.display_contracts()

# Update a rule and a contract
system_rules.update_rule("data_privacy", "enhanced")
system_rules.update_contract("uptime", "99.95%")

# Display updated rules and contracts
system_rules.display_rules()
system_rules.display_contracts()
```