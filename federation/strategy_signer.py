from federation.identity import NodeIdentity
import hashlib
import base64

class StrategySigner:
    def __init__(self):
        self.id = NodeIdentity()

    def fingerprint(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return hashlib.sha256(data).hexdigest()

    def sign_strategy(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        signature = self.id.sign(data)
        return {
            "strategy_file": os.path.basename(file_path),
            "fingerprint": self.fingerprint(file_path),
            "signature": base64.b64encode(signature).decode(),
            "public_key": self.id.export_public_key().decode()
        }
