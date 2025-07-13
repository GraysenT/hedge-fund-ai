from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
import os

class NodeIdentity:
    def __init__(self, key_path="federation/private_key.pem"):
        self.key_path = key_path
        if not os.path.exists(key_path):
            self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            with open(key_path, "wb") as f:
                f.write(self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))
        else:
            with open(key_path, "rb") as f:
                self.private_key = serialization.load_pem_private_key(f.read(), password=None)
        self.public_key = self.private_key.public_key()

    def sign(self, data: bytes):
        return self.private_key.sign(data, hashes.SHA256())

    def export_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )