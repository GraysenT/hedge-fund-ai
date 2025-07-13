import uuid
from datetime import datetime

class NarrativeSignal:
    def __init__(self, theme, domain, source_module, confidence):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.now().isoformat()
        self.theme = theme
        self.domain = domain
        self.source = source_module
        self.confidence = confidence

    def serialize(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "theme": self.theme,
            "domain": self.domain,
            "source": self.source,
            "confidence": self.confidence
        }