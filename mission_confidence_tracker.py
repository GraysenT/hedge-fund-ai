```python
class MissionAlignmentTracker:
    def __init__(self, initial_mission_statement):
        self.mission_statement = initial_mission_statement
        self.confidence_level = 100  # Initial confidence level at 100%

    def report_activity(self, activity_description):
        # This method would be more complex in a real system, involving analysis of the activity.
        print(f"Activity reported: {activity_description}")
        # Placeholder for activity alignment check
        if "aligned" in activity_description:
            self.adjust_confidence(True)
        else:
            self.adjust_confidence(False)

    def adjust_confidence(self, is_aligned):
        if is_aligned:
            if self.confidence_level < 100:
                self.confidence_level += 1
        else:
            self.confidence_level -= 10
            if self.confidence_level < 0:
                self.confidence_level = 0
        print(f"Confidence Level adjusted to: {self.confidence_level}%")

    def get_confidence_level(self):
        return self.confidence_level

# Example usage
tracker = MissionAlignmentTracker("Ensure user data privacy and security.")
tracker.report_activity("Implemented end-to-end encryption, aligned with our mission.")
tracker.report_activity("Collected extra user data for analysis, not aligned with our mission.")
print(f"Current Confidence Level: {tracker.get_confidence_level()}%")
```