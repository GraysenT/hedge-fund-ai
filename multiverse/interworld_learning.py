def transfer_policy(src, dest, policy_fn):
    for agent in worlds[dest]["agents"]:
        if policy_fn(agent):
            agent.learn(worlds[src]["best_strategy"])