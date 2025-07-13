import uuid
from datetime import datetime

class StrategicTreaty:
    def __init__(self, node_a, node_b, terms, duration_days=30):
        self.id = str(uuid.uuid4())
        self.parties = [node_a, node_b]
        self.terms = terms  # e.g., {"share_signals": True, "risk_sync": True}
        self.duration = duration_days
        self.signed_at = datetime.now().isoformat()
        self.status = "Active"

    def revoke(self, reason=""):
        self.status = "Revoked"
        self.revoked_reason = reason
        self.revoked_at = datetime.now().isoformat()

    def serialize(self):
        return {
            "id": self.id,
            "parties": self.parties,
            "terms": self.terms,
            "status": self.status,
            "signed_at": self.signed_at,
            "revoked_at": getattr(self, "revoked_at", None),
            "revoked_reason": getattr(self, "revoked_reason", "")
        }