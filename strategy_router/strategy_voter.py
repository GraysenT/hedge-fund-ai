import json
import os

CONF_RISK_DB = "memory/confidence_vs_risk.json"
VOTE_DB = "memory/strategy_votes.json"
THRESHOLD = 0.5

def run_strategy_vote():
    if not os.path.exists(CONF_RISK_DB):
        print("❌ No confidence-risk data.")
        return

    with open(CONF_RISK_DB, "r") as f:
        data = json.load(f)

    votes = []
    for d in data:
        vote = {
            "idea": d["idea"],
            "confidence": d["confidence"],
            "risk": d["risk"],
            "signal_strength": d["signal_strength"],
            "vote": "approve" if d["signal_strength"] > THRESHOLD else "deny"
        }
        votes.append(vote)

    with open(VOTE_DB, "w") as f:
        json.dump(votes, f, indent=2)

    print(f"🗳️ Voted on {len(votes)} strategies.")

if __name__ == "__main__":
    run_strategy_vote()
    