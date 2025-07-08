import json
import os
from datetime import datetime

MEMORY_PATH = "agents/agent_long_term_memory.json"
ORDERS_PATH = "memory/order_logs"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def update_agent_memory():
    lineage = json.load(open(LINEAGE_PATH))
    orders = json.load(open(os.path.join(ORDERS_PATH, sorted(os.listdir(ORDERS_PATH))[-1])))

    memory = json.load(open(MEMORY_PATH)) if os.path.exists(MEMORY_PATH) else {}

    for order in orders:
        strategy = order["strategy"]
        agent = lineage.get(strategy, {}).get("proposed_by", "unknown")

        if agent not in memory:
            memory[agent] = {"trades": [], "mutations": [], "pnl": 0}

        memory[agent]["trades"].append({
            "symbol": order["symbol"],
            "action": order["action"],
            "confidence": order["confidence"],
            "capital": order["capital"],
            "timestamp": order["timestamp"]
        })
        memory[agent]["pnl"] += order.get("pnl", 0)

        if "mut" in strategy:
            memory[agent]["mutations"].append(strategy)

    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
    print("🧠 Agent memory updated.")

if __name__ == "__main__":
    update_agent_memory()
    