import copy

def fork_agent(agent, variation_id):
    """
    Creates a variant of an agent with memory and new goal adaptation.
    """
    new_agent = copy.deepcopy(agent)
    new_agent["id"] = f"{agent['id']}_fork{variation_id}"
    new_agent["origin"] = agent["id"]
    new_agent["goals"].append("evolve_from_legacy")
    return new_agent