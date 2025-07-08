import json
import os

AGENT_TOURNAMENT = "agents/agent_tournament_results.json"

def get_agent_tags(top_n=2):
    with open(AGENT_TOURNAMENT) as f:
        results = json.load(f)
    top = sorted(results.items(), key=lambda x: x[1]["pnl"], reverse=True)[:top_n]
    tags = []
    for agent, stats in top:
        for strat in stats["strategies"]:
            tags.append(f"{agent}:{strat}")
    return tags

def export_feedback_tags():
    tags = get_agent_tags()
    with open("models/agent_feedback_tags.json", "w") as f:
        json.dump(tags, f, indent=2)
    print(f"📡 Exported feedback tags to models/agent_feedback_tags.json")

if __name__ == "__main__":
    export_feedback_tags()
    