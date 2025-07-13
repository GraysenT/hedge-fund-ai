from .signal_registry import load_registry

def summarize_recent_signals(limit=5):
    registry = load_registry()
    recent = registry[-limit:]
    return [
        {
            "Strategy": s["strategy"],
            "Asset": s["asset"],
            "Confidence": s["confidence"],
            "Latest Outcome": s["history"][-1] if s["history"] else "No outcome yet"
        }
        for s in recent
    ]