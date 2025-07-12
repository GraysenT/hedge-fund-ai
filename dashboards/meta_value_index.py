```python
import numpy as np

class SystemUtilityTracker:
    def __init__(self):
        self.roi_data = []
        self.intelligence_data = []
        self.coverage_data = []
        self.resilience_data = []

    def add_data(self, roi, intelligence, coverage, resilience):
        self.roi_data.append(roi)
        self.intelligence_data.append(intelligence)
        self.coverage_data.append(coverage)
        self.resilience_data.append(resilience)

    def calculate_average(self, data):
        return np.mean(data)

    def get_average_roi(self):
        return self.calculate_average(self.roi_data)

    def get_average_intelligence(self):
        return self.calculate_average(self.intelligence_data)

    def get_average_coverage(self):
        return self.calculate_average(self.coverage_data)

    def get_average_resilience(self):
        return self.calculate_average(self.resilience_data)

    def get_total_system_utility(self):
        # Simple utility function that sums the normalized averages of each metric
        total_utility = (self.get_average_roi() + self.get_average_intelligence() +
                         self.get_average_coverage() + self.get_average_resilience())
        return total_utility

# Example usage
tracker = SystemUtilityTracker()
tracker.add_data(roi=120, intelligence=80, coverage=90, resilience=75)
tracker.add_data(roi=130, intelligence=85, coverage=95, resilience=80)

print("Average ROI:", tracker.get_average_roi())
print("Average Intelligence:", tracker.get_average_intelligence())
print("Average Coverage:", tracker.get_average_coverage())
print("Average Resilience:", tracker.get_average_resilience())
print("Total System Utility:", tracker.get_total_system_utility())
```