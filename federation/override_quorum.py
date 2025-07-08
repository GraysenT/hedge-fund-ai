import random

def vote_on_strategy(strategy_id):
    peers = ["node1", "node2", "node3", "node4"]
    votes = [random.choice(["allow", "veto", "boost"]) for _ in peers]

    allow = votes.count("allow")
    veto = votes.count("veto")
    boost = votes.count("boost")

    if veto >= 2:
        decision = "❌ STRATEGY VETOED"
    elif boost >= 2:
        decision = "✅ STRATEGY BOOSTED"
    else:
        decision = "⚖️ STRATEGY ALLOWED"

    print(f"Strategy: {strategy_id}\nVotes: {votes}\n→ {decision}")

if __name__ == "__main__":
    vote_on_strategy("gen_strat_r4_mut8023")
    