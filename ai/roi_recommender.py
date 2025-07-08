def suggest_roi_improvements():
    # Placeholder logic — this will eventually use reinforcement + strategy logs
    return [
        {
            "description": "Increase capital weight to strategy_ema_fast after 5-day Sharpe > 2",
            "impact": "ROI +6%"
        },
        {
            "description": "Auto-mute strategy_news_sentiment due to high false signal rate",
            "impact": "risk reduction"
        }
    ]
    