import json
import os
from collections import defaultdict

def rate_peers():
    trust = defaultdict(float)
    for file in os.listdir("federation"):
        if "import_" not in file:
            continue
        peer = json.load(open(f"federation/{file}"))
        pnl = peer.get("performance", {})
        trust[file] = sum(v["pnl"] for v in pnl.values()) / max(1, len(pnl))

    print("🤝 Federation Trust Map:")
    for peer, score in sorted(trust.items(), key=lambda x: x[1], reverse=True):
        print(f"{peer}: Trust Score {round(score, 2)}")

if __name__ == "__main__":
    rate_peers()
    