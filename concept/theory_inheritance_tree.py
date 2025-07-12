def build_theory_tree(agent_history):
    """
    Tracks the evolution of philosophical strategy frameworks
    from one generation of agents to the next.
    """
    tree = {}
    for agent in agent_history:
        parent = agent.get("origin")
        belief = agent.get("belief", "undefined")
        tree[agent["id"]] = {"from": parent, "belief": belief}
    return tree