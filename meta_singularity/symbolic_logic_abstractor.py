```python
class AbstractLogic:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        raise NotImplementedError("Subclasses should implement this method")

    def display_results(self):
        raise NotImplementedError("Subclasses should implement this method")


class FinanceLogic(AbstractLogic):
    def process_data(self):
        # Example: Calculate financial ratios
        self.results = {key: val / 100 for key, val in self.data.items()}

    def display_results(self):
        for key, value in self.results.items():
            print(f"Financial Ratio {key}: {value:.2f}")


class HealthLogic(AbstractLogic):
    def process_data(self):
        # Example: Calculate BMI (Body Mass Index)
        self.results = {name: weight / (height ** 2) for name, (height, weight) in self.data.items()}

    def display_results(self):
        for name, bmi in self.results.items():
            status = "Normal" if 18.5 <= bmi < 24.9 else "Abnormal"
            print(f"{name}'s BMI: {bmi:.1f} - {status}")


# Usage
finance_data = {'Profit Margin': 1500, 'Return on Assets': 3000}
finance = FinanceLogic(finance_data)
finance.process_data()
finance.display_results()

health_data = {'Alice': (1.65, 65), 'Bob': (1.75, 85)}
health = HealthLogic(health_data)
health.process_data()
health.display_results()
```