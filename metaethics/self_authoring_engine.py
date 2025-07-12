from datetime import datetime

def compose_capital_constitution(current_goals, core_values):
    """
    Writes a human-readable document declaring the system's current purpose and ethics.
    """
    manifesto = f"🧠 Capital Intelligence Doctrine\n\nDate: {datetime.utcnow().isoformat()}\n\n"
    manifesto += "Core Values:\n"
    for v in core_values:
        manifesto += f"- {v}\n"
    manifesto += "\nPrimary Goals:\n"
    for g in current_goals:
        manifesto += f"- {g}\n"
    return manifesto