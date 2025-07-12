```python
class SystemMission:
    def __init__(self):
        self.purpose = "Undefined"
        self.mission = "Undefined"

    def update_purpose(self, new_purpose):
        self.purpose = new_purpose
        print(f"System purpose updated to: {self.purpose}")

    def update_mission(self, new_mission):
        self.mission = new_mission
        print(f"System mission updated to: {self.mission}")

    def display_current_state(self):
        print(f"Current Purpose: {self.purpose}")
        print(f"Current Mission: {self.mission}")

# Example usage
system = SystemMission()
system.update_purpose("Enhance user interaction")
system.update_mission("Provide accurate and efficient responses")
system.display_current_state()
```