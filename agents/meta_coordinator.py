from agents.recursive_agent import RecursiveAgent

class MetaCoordinator:
    def __init__(self):
        self.agents = {
            "equities": RecursiveAgent("equities"),
            "crypto": RecursiveAgent("crypto"),
            "forex": RecursiveAgent("forex")
        }

    def run_step(self, market_data_map):
        for market, agent in self.agents.items():
            data = market_data_map.get(market, {})
            agent.step(data)

    def global_strategy_snapshot(self):
        return {
            market: agent.export_state()
            for market, agent in self.agents.items()
        }

    def replicate_best(self):
        all_agents = list(self.agents.values())
        scores = [(a.market, max(s.performance_score for s in a.strategies)) for a in all_agents]
        best = max(scores, key=lambda x: x[1])
        clone_market = f"{best[0]}_clone_{len(self.agents)}"
        self.agents[clone_market] = RecursiveAgent(clone_market)
        print(f"🧬 Cloned {best[0]} into {clone_market}")
