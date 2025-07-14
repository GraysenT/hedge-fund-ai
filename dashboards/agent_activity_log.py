```python
import datetime

class AgentLog:
    def __init__(self):
        self.log = []

    def add_entry(self, agent_id, action, details):
        timestamp = datetime.datetime.now()
        self.log.append({
            "timestamp": timestamp,
            "agent_id": agent_id,
            "action": action,
            "details": details
        })

    def show_log(self):
        for entry in self.log:
            timestamp = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} - Agent {entry['agent_id']} {entry['action']} - {entry['details']}")

# Example usage
log = AgentLog()
log.add_entry(1, "action", "scanned the area")
log.add_entry(2, "vote", "voted for strategy A")
log.add_entry(1, "reinforcement", "received backup")
log.add_entry(3, "conflict", "engaged with enemy")
log.add_entry(2, "action", "completed mission objective")

log.show_log()
```