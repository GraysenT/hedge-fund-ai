import requests
import os

class SyncClient:
    def __init__(self, peer_url: str):
        self.peer_url = peer_url

    def send_strategy(self, file_path: str):
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            r = requests.post(f"{self.peer_url}/upload-strategy", files=files)
            return r.json()

    def fetch_peer_snapshot(self):
        r = requests.get(f"{self.peer_url}/strategies")
        return r.json()
