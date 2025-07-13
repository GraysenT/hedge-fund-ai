import uuid
from datetime import datetime

class DeploymentOrder:
    def __init__(self, target_zone, agent_id, operation_type="scan", conditions=None):
        self.id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.target_zone = target_zone  # e.g., "Energy", "Asia", "Options"
        self.operation = operation_type
        self.conditions = conditions or {}
        self.issued_at = datetime.now().isoformat()
        self.status = "Dispatched"

    def complete(self, outcome_summary):
        self.status = "Completed"
        self.completed_at = datetime.now().isoformat()
        self.outcome = outcome_summary

    def serialize(self):
        return {
            "id": self.id,
            "agent_id": self.agent_id,
            "target_zone": self.target_zone,
            "operation": self.operation,
            "conditions": self.conditions,
            "status": self.status,
            "issued_at": self.issued_at,
            "completed_at": getattr(self, "completed_at", None),
            "outcome": getattr(self, "outcome", "")
        }