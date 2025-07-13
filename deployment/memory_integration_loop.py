from agents.meta_coordinator import MetaCoordinator
from memory.agent_memory_store import AgentMemoryStore
from intelligence.transfer_learning import transfer_top_strategies

store = AgentMemoryStore()
coordinator = MetaCoordinator()

# 1. Load last memory snapshot
memories = store.load()

# 2. Inject strategies from best past agent
if "equities" in memories and "crypto" in coordinator.agents:
    top_agent = coordinator.agents["equities"]
    target = coordinator.agents["crypto"]
    transfer_top_strategies(top_agent, target, top_n=2)

# 3. Run a few steps and write new memory
for i in range(10):
    coordinator.run_step({
        "equities": {"price": 105, "ma": 100},
        "crypto": {"price": 19500, "ma": 20000}
    })

# 4. Save final memory snapshot
for market, agent in coordinator.agents.items():
    store.write_agent_state(market, agent.export_state())