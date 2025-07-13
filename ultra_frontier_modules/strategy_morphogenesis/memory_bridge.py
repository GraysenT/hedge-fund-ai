def extract_morph_triggers(memory_log, signal_name):
    """
    Extracts morph instructions from long-term memory.
    Looks for outcome-mapped failures or underperformance tags.
    """
    triggers = []
    for m in memory_log:
        if m.get("strategy") == signal_name and m.get("outcome") == "underperform":
            triggers.append({
                "context": m.get("context", "unknown"),
                "adjustment": m.get("suggested_fix", {})
            })
    return triggers