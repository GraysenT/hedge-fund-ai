import random

AGENTS = ["agent_macro", "agent_lstm", "agent_vol"]

def simulate_negotiation():
    proposals = {}
    for a in AGENTS:
        strat = f"{a}_proposal_{random.randint(1000, 9999)}"
        allocation = random.randint(5, 20)
        proposals[a] = {"strategy": strat, "requested": allocation}

    print("🤝 Initial Proposals:")
    for a, p in proposals.items():
        print(f"{a} wants ${p['requested']}k for {p['strategy']}")

    agreed = []
    for a, p in proposals.items():
        accepted = random.choice([True, False])
        if accepted:
            agreed.append((a, p["strategy"]))
            print(f"✅ {p['strategy']} approved for funding.")
        else:
            print(f"❌ {p['strategy']} rejected.")

if __name__ == "__main__":
    simulate_negotiation()
    