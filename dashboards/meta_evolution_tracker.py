import json
import os

LINEAGE = "strategy_memory/strategy_lineage.json"
AGENTS = "agents/agent_registry.json"

with open(LINEAGE) as f:
    lineage = json.load(f)

with open(AGENTS) as f:
    agents = json.load(f)

generations = [v["depth"] for v in lineage.values()]
proposed = sum(1 for v in lineage.values() if "Proposed" in v.get("rating", ""))
mutants = sum(1 for v in lineage.values() if "Hybrid" in v.get("rating", ""))

print("\n🧬 Meta-Evolution Tracker\n")
print(f"Total Strategies: {len(lineage)}")
print(f"Total Agents: {len(agents)}")
print(f"Max Strategy Depth: {max(generations)}")
print(f"Proposed by Agents: {proposed}")
print(f"Hybrid Mutations: {mutants}")
