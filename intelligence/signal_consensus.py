from collections import defaultdict

class SignalConsensus:
    def __init__(self):
        self.votes = defaultdict(list)

    def vote(self, signal):
        symbol = signal.get("symbol")
        action = signal.get("action")
        confidence = signal.get("confidence")
        self.votes[symbol].append((action, confidence))

    def compute_consensus(self):
        results = {}
        for symbol, actions in self.votes.items():
            vote_totals = defaultdict(float)
            for action, confidence in actions:
                vote_totals[action] += confidence
            consensus_action = max(vote_totals, key=vote_totals.get)
            consensus_confidence = vote_totals[consensus_action] / len(actions)
            results[symbol] = {
                "action": consensus_action,
                "confidence": round(consensus_confidence, 3),
                "votes": len(actions)
            }
        return results