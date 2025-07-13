from economy.capital_ledger import CapitalLedger
from memory.vector_memory import NeuralMemory
from societies.market_society import MarketSociety
from mesh.zk_voting import ZKVote

ledger = CapitalLedger()
memory = NeuralMemory()
society = MarketSociety("ETHUSD")

# Simulate agent
strategy_output = "buy"
zk = ZKVote(strategy_output)

# Voting cycle
if zk.reveal("buy"):
    ledger.update("agent.eth", +50)
    memory.insert({"symbol": "ETHUSD", "strategy": "agent.eth", "signal": "buy", "reward": 50})

society.register_agent("agent.eth", strategy_output)
society.govern()
society.evolve_policy()

print("✅ Global Memory Size:", len(memory.data))
print("💰 Capital:", ledger.leaderboard())
print("📜 Laws:", society.laws)