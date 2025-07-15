def invert_causality(world_name, outcome):
    for event in reversed(worlds[world_name]["history"]):
        if "decision" in event:
            event["adjusted"] = True
            event["influenced_by_future"] = outcome
            break