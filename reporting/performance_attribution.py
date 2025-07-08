import json
import os

PERF_PATH = "memory/performance"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def attribute():
    perf = sorted(os.listdir(PERF_PATH))[-1]
    perf_data = json.load(open(f"{PERF_PATH}/{perf}"))

    lineage = json.load(open(LINEAGE_PATH))
    by_model, by_agent, by_signal = {}, {}, {}

    for strat, result in perf_data.items():
        info = lineage.get(strat, {})
        model = info.get("model", "unknown")
        agent = info.get("proposed_by", "unknown")
        sig = info.get("rating", "unknown")

        for category, label in [("model", model), ("agent", agent), ("signal", sig)]:
            container = {"model": by_model, "agent": by_agent, "signal": by_signal}[category]
            if label not in container:
                container[label] = 0
            container[label] += result["pnl"]

    print("📊 Attribution by Model:\n", by_model)
    print("🧠 Attribution by Agent:\n", by_agent)
    print("🔍 Attribution by Signal:\n", by_signal)

if __name__ == "__main__":
    attribute()
    