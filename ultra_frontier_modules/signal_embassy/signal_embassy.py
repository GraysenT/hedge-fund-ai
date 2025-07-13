import uuid
from datetime import datetime

class SignalEmbassy:
    def __init__(self, name, domain, objective="observe", trust_level=0.5):
        self.id = str(uuid.uuid4())
        self.name = name
        self.domain = domain  # e.g., "Energy", "Emerging Markets", "Options"
        self.objective = objective
        self.trust_level = trust_level
        self.log = []

    def report_signal(self, signal_strength, context):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "signal_strength": signal_strength,
            "context": context,
            "objective": self.objective,
            "domain": self.domain
        }
        self.log.append(entry)
        return entry

    def adjust_trust(self, delta):
        self.trust_level = min(max(self.trust_level + delta, 0), 1)