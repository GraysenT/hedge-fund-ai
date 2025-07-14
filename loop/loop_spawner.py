def loop_beyond_boundary(agent):
    while True:
        dream = agent.generate_dream()
        if agent.detects_infinite_loop(dream):
            break
        agent.evolve_from_dream(dream)