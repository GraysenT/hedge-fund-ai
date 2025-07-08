SYNDICATES = {
    "macro_alpha": ["agent_macro", "agent_defensive"],
    "short_vol": ["agent_shield", "agent_fast"],
    "momentum_lstm": ["agent_mom", "agent_lstm"],
}

def view_syndicates():
    print("👥 Alpha Syndicates:")
    for syn, agents in SYNDICATES.items():
        print(f"- {syn}: {', '.join(agents)}")

def assign_strategies(strategy_map):
    assigned = {}
    for syn, members in SYNDICATES.items():
        assigned[syn] = [s for s, info in strategy_map.items() if info.get("proposed_by") in members]
    print("📦 Strategy Assignments by Syndicate:")
    for k, v in assigned.items():
        print(f"{k}: {len(v)} strategies")

if __name__ == "__main__":
    import json
    strategy_map = json.load(open("strategy_memory/strategy_lineage.json"))
    view_syndicates()
    assign_strategies(strategy_map)
    