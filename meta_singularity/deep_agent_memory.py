```python
class HistoricalEvent:
    def __init__(self, year, event_description):
        self.year = year
        self.event_description = event_description

    def __str__(self):
        return f"{self.year}: {self.event_description}"

class HistoryLog:
    def __init__(self):
        self.events = []

    def add_event(self, year, description):
        event = HistoricalEvent(year, description)
        self.events.append(event)
        self.events.sort(key=lambda x: x.year)

    def display_events(self):
        for event in self.events:
            print(event)

# Example usage
history = HistoryLog()
history.add_event(1776, "Declaration of Independence of the United States.")
history.add_event(1945, "End of World War II.")
history.add_event(1989, "Fall of the Berlin Wall.")

history.display_events()
```