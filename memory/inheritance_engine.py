def inherit_memory(child, parent):
    child.memory = parent.memory[-100:]  # recent memory only
    child.beliefs = parent.beliefs.copy()
    child.temporal_alignment = parent.temporal_alignment