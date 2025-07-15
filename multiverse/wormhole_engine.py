def send_through_wormhole(agent, source, target):
    if not is_accessible(target): return "🛑 World is sealed."
    worlds[source]["agents"].remove(agent)
    worlds[target]["agents"].append(agent)
    return f"🌌 Agent {agent.id} sent from {source} to {target}"