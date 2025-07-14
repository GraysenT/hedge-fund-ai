from collections import defaultdict, Counter

class VotingEngine:
    def __init__(self):
        self.votes = defaultdict(list)

    def register_vote(self, market: str, strategy: str, signal: str):
        self.votes[market].append((strategy, signal))

    def resolve_votes(self):
        resolved = {}
        for market, signals in self.votes.items():
            count = Counter([s for _, s in signals])
            resolved[market] = count.most_common(1)[0][0]  # 'buy', 'sell', 'hold'
        self.votes.clear()
        return resolved
    
    def vote_on_signals(signals):
        return signals