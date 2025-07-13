from path.to.intelligence_genesis import Intelligence


def simulate_intelligence(constraints, steps):
    intelligence = Intelligence(constraints)
    for _ in range(steps):
        next(intelligence.persist())