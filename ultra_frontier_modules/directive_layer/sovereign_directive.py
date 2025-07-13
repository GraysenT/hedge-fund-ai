from datetime import datetime
import uuid

class SovereignDirective:
    def __init__(self, tag, conditions, directive_text):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.now().isoformat()
        self.tag = tag  # e.g. "CapitalDefense", "ConvictionBoost"
        self.conditions = conditions  # e.g. {"volatility": ">0.4", "capital_drawdown": ">3%"}
        self.directive = directive_text
        self.status = "active"

    def deactivate(self, reason="auto-expired"):
        self.status = "inactive"
        self.deactivated_at = datetime.now().isoformat()
        self.reason = reason

    def serialize(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "tag": self.tag,
            "conditions": self.conditions,
            "directive": self.directive,
            "status": self.status,
            "deactivated_at": getattr(self, "deactivated_at", None),
            "reason": getattr(self, "reason", None)
        }