from copy import deepcopy

def fork_universe(world_name, mutation):
    base = deepcopy(worlds[world_name])
    forked = {
        "agents": base["agents"],
        "laws": {**base["laws"], **mutation},
        "history": base["history"][:],
        "origin": world_name
    }
    fork_name = f"{world_name}_fork"
    worlds[fork_name] = forked
    return fork_name
