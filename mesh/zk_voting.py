import hashlib

class ZKVote:
    def __init__(self, strategy_output: str):
        self.commitment = hashlib.sha256(strategy_output.encode()).hexdigest()

    def reveal(self, original_output: str):
        return self.commitment == hashlib.sha256(original_output.encode()).hexdigest()