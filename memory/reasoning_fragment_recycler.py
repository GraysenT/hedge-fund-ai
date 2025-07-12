def extract_logic_fragments(memory_entries):
    """
    Pulls reusable pieces of reasoning from past memory log entries.
    """
    fragments = []
    for entry in memory_entries:
        thought = entry.get("thought", "")
        if "if" in thought and "then" in thought:
            fragments.append(thought)
    return fragments