```python
import datetime

class SystemHistory:
    def __init__(self):
        self.events = []

    def add_event(self, event_type, description):
        event = {
            'date': datetime.datetime.now(),
            'type': event_type,
            'description': description
        }
        self.events.append(event)

    def get_timeline(self):
        return sorted(self.events, key=lambda x: x['date'])

    def __str__(self):
        timeline = self.get_timeline()
        return '\n'.join([f"{event['date']} - {event['type']}: {event['description']}" for event in timeline])

# Example usage
history = SystemHistory()
history.add_event('birth', 'Initial deployment of the system.')
history.add_event('upgrade', 'System upgraded to version 1.1.')
history.add_event('mutation', 'System self-modified for improved performance.')
history.add_event('death', 'System decommissioned due to obsolescence.')

print(history)
```