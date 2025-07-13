import uuid
from datetime import datetime

class SovereignNode:
    def __init__(self, name, jurisdiction, authority_level=0.5):
        self.id = str(uuid.uuid4())
        self.name = name
        self.jurisdiction = jurisdiction  # e.g., "commodities", "EU", "crypto"
        self.authority = authority_level
        self.treaties = {}
        self.last_decision = None

    def propose_treaty(self, target_node_id, terms):
        self.treaties[target_node_id] = {
            "terms": terms,
            "timestamp": datetime.now().isoformat()
        }

    def log_decision(self, decision_summary):
        self.last_decision = {
            "summary": decision_summary,
            "timestamp": datetime.now().isoformat()
        }