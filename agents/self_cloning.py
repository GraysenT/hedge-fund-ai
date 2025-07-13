from agents.recursive_agent import RecursiveAgent

def spawn_market_agents(new_markets: list, agent_registry: dict):
    for m in new_markets:
        if m not in agent_registry:
            agent_registry[m] = RecursiveAgent(market=m)
            print(f"🧬 Spawned new market agent: {m}")