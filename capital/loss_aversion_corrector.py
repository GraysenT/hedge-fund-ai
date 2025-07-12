def correct_excessive_caution(agent, drawdown_threshold=0.05):
    """
    Prevents overreaction to drawdown if agent has shown stable recovery in past.
    """
    recent_drawdowns = agent.get("drawdowns", [])
    if recent_drawdowns and max(recent_drawdowns[-5:]) < drawdown_threshold:
        agent["risk_profile"] = "re-engage"
    return agent