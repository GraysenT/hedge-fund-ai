worlds = {}

def spawn_world(name, config):
    worlds[name] = {
        "agents": [],
        "laws": config["laws"],
        "isolation": config.get("isolated", True),
        "history": [],
    }
    return worlds[name]