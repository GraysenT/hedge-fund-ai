import json
import os
from datetime import datetime

PROPOSALS_PATH = "meta/constitution_proposals.json"

def propose_amendment(field, new_value, proposer):
    proposals = json.load(open(PROPOSALS_PATH)) if os.path.exists(PROPOSALS_PATH) else []
    proposals.append({
        "field": field,
        "new_value": new_value,
        "proposer": proposer,
        "votes": {},
        "status": "pending",
        "timestamp": datetime.now().isoformat()
    })
    with open(PROPOSALS_PATH, "w") as f:
        json.dump(proposals, f, indent=2)
    print(f"📜 Amendment proposed for '{field}' → {new_value}")

def vote_amendment(index, agent, vote):
    proposals = json.load(open(PROPOSALS_PATH))
    proposals[index]["votes"][agent] = vote

    yes = list(proposals[index]["votes"].values()).count("yes")
    if yes >= 3:
        # Apply the amendment
        const = json.load(open("meta/constitution.json"))
        const["rules"][proposals[index]["field"]] = proposals[index]["new_value"]
        with open("meta/constitution.json", "w") as f:
            json.dump(const, f, indent=2)
        proposals[index]["status"] = "approved"
        print(f"✅ Amendment applied to {proposals[index]['field']}.")

    with open(PROPOSALS_PATH, "w") as f:
        json.dump(proposals, f, indent=2)

if __name__ == "__main__":
    propose_amendment("confidence_min", 0.75, "agent_macro")
    vote_amendment(0, "agent_macro", "yes")
    vote_amendment(0, "agent_lstm", "yes")
    vote_amendment(0, "agent_momentum", "yes")
    