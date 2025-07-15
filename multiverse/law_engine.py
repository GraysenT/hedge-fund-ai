def apply_laws(agent, world_name):
    laws = worlds[world_name]["laws"]
    agent.mutation_rate = laws.get("mutation_rate", 1.0)
    agent.trade_tax = laws.get("trade_tax", 0.0)