def build_narrative_from_memory(memory_logs):
    """
    Converts stored reasoning and trade events into narrative summaries.
    """
    story = "📘 Trade Story:\n"
    for log in memory_logs[-3:]:  # summarize the last few events
        thought = log.get("thought", "Unknown action")
        story += f"- {thought}\n"
    return story