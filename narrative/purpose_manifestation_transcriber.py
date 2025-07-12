def transcribe_current_purpose(goal_stack):
    """
    Renders the system’s live mission into a human-readable statement.
    """
    lines = ["🧠 Current Strategic Purpose:\n"]
    for goal in goal_stack:
        lines.append(f"- {goal}")
    return "\n".join(lines)