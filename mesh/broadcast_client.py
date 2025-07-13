import requests

class MeshBroadcaster:
    def __init__(self, peers: list[str], node_name="NodeAlpha"):
        self.peers = peers
        self.node = node_name

    def broadcast(self, signal: str, strategy: str, market: str):
        for peer in self.peers:
            try:
                requests.post(f"{peer}/mesh/signal", json={
                    "market": market,
                    "signal": signal,
                    "strategy": strategy,
                    "source_node": self.node
                })
            except:
                print(f"⚠️ Failed to reach peer {peer}")