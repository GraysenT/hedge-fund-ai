def inherit_legacy_memory(child_agent, parent_agent):
    """
    Links the child strategy agent with memory fragments and traits from its predecessor.
    """
    child_agent["lineage"] = parent_agent["id"]
    child_agent["memory"] = parent_agent.get("memory", [])[-5:]
    child_agent["values"] = parent_agent.get("values", {})
    return child_agent