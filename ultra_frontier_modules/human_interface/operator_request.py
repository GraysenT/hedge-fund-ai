import uuid
from datetime import datetime

class OperatorRequest:
    def __init__(self, operator_id, content, category="override"):
        self.id = str(uuid.uuid4())
        self.operator_id = operator_id
        self.timestamp = datetime.now().isoformat()
        self.content = content
        self.category = category
        self.resolved = False
        self.response = None

    def attach_response(self, response_text):
        self.response = response_text
        self.resolved = True

    def serialize(self):
        return {
            "id": self.id,
            "operator_id": self.operator_id,
            "timestamp": self.timestamp,
            "content": self.content,
            "category": self.category,
            "resolved": self.resolved,
            "response": self.response
        }