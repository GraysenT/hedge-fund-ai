```python
import random

class SystemRobustnessTester:
    def __init__(self, system, failure_scenarios):
        """
        Initialize the robustness tester.
        
        :param system: A callable that represents the system to be tested.
        :param failure_scenarios: A list of functions that simulate different failure scenarios.
        """
        self.system = system
        self.failure_scenarios = failure_scenarios

    def test_scenario(self, scenario):
        """
        Test a single failure scenario.
        
        :param scenario: A function that modifies the system to simulate a failure.
        :return: True if the system handles the failure, False otherwise.
        """
        try:
            scenario(self.system)
            self.system.reset()
            return True
        except Exception as e:
            print(f"Failure in scenario: {scenario.__name__} - {str(e)}")
            return False

    def run_tests(self):
        """
        Run all failure scenarios and score the system robustness.
        
        :return: The robustness score as a percentage of passed scenarios.
        """
        passed = 0
        for scenario in self.failure_scenarios:
            if self.test_scenario(scenario):
                passed += 1
        
        total = len(self.failure_scenarios)
        score = (passed / total) * 100
        return score

# Example usage:

class ExampleSystem:
    def __init__(self):
        self.state = "operational"

    def reset(self):
        self.state = "operational"

    def process_data(self, data):
        if self.state != "operational":
            raise Exception("System is not operational")
        # Process data logic here
        return "processed"

# Define failure scenarios
def power_failure(system):
    system.state = "power outage"

def software_bug(system):
    system.state = "error"

def hardware_failure(system):
    system.state = "hardware damage"

# Create system and tester
system = ExampleSystem()
scenarios = [power_failure, software_bug, hardware_failure]
tester = SystemRobustnessTester(system, scenarios)

# Run robustness test
robustness_score = tester.run_tests()
print(f"System Robustness Score: {robustness_score}%")
```