import json
import random

def review_peer(file):
    peer = json.load(open(file))
    candidates = peer.get("strategies", {})
    performance = peer.get("performance", {})

    for strat, meta in candidates.items():
        if strat in performance and performance[strat]["pnl"] > 50:
            action = random.choice(["adopt", "mirror", "ignore"])
            print(f"🤝 {strat} → {action.upper()} (pnl: {performance[strat]['pnl']})")

if __name__ == "__main__":
    file = sorted(os.listdir("federation"))[-1]
    review_peer(f"federation/{file}")
    