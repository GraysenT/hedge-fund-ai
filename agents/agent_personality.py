AGENT_PERSONALITIES = {
    "agent_alpha": "aggressive",
    "agent_macro": "defensive",
    "agent_momentum": "trend",
    "agent_meanrev": "contrarian"
}

def get_personality(agent):
    return AGENT_PERSONALITIES.get(agent, "neutral")

def adjust_vote_by_personality(agent, strategy_rating):
    personality = get_personality(agent)
    if personality == "aggressive" and "Proposed" in strategy_rating:
        return 2
    elif personality == "defensive" and "Hybrid" in strategy_rating:
        return -1
    return 0

if __name__ == "__main__":
    print("🧬 agent_alpha:", get_personality("agent_alpha"))

    