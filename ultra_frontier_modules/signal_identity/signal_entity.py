import uuid
from datetime import datetime

class SignalEntity:
    def __init__(self, strategy_name, asset, raw_value, confidence, reason):
        self.id = str(uuid.uuid4())
        self.strategy = strategy_name
        self.asset = asset
        self.raw_value = raw_value
        self.confidence = confidence
        self.reason = reason
        self.timestamp = datetime.now().isoformat()
        self.history = []

    def attach_outcome(self, pnl, was_executed, notes=""):
        outcome = {
            "timestamp": datetime.now().isoformat(),
            "pnl": pnl,
            "executed": was_executed,
            "notes": notes
        }
        self.history.append(outcome)

    def reflect(self):
        if not self.history:
            return "No outcome yet."
        last = self.history[-1]
        return f"{self.id[:6]} [{self.strategy}] -> PnL: {last['pnl']} (Executed: {last['executed']})"

    def serialize(self):
        return {
            "id": self.id,
            "strategy": self.strategy,
            "asset": self.asset,
            "value": self.raw_value,
            "confidence": self.confidence,
            "reason": self.reason,
            "created": self.timestamp,
            "history": self.history
        }