import hashlib
import json

class ChainLedger:
    def __init__(self):
        self.chain = []

    def add_entry(self, data: dict):
        prev_hash = self.chain[-1]["hash"] if self.chain else "0" * 64
        block = {
            "data": data,
            "prev_hash": prev_hash,
        }
        block_json = json.dumps(block, sort_keys=True).encode()
        block["hash"] = hashlib.sha256(block_json).hexdigest()
        self.chain.append(block)

    def validate(self):
        for i in range(1, len(self.chain)):
            if self.chain[i]["prev_hash"] != self.chain[i-1]["hash"]:
                return False
        return True