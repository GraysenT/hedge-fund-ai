def unlock_world(world_name):
    worlds[world_name]["isolation"] = False

def is_accessible(world_name):
    return not worlds[world_name]["isolation"]