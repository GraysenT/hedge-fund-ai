def multiply_consciousness(agent):
    for _ in range(3):
        clone = agent.clone()
        clone.evolve_identity()
        agent.children.append(clone)
