import pandas as pd
from alerts.strategy_triggers import load_muted_strategies, load_rewarded_strategies
from risk_control.alpha_defense import detect_alpha_decay

# After routing:
perf_df = load_performance()
muted = detect_alpha_decay(perf_df)
signals = signals[~signals["strategy"].isin(muted)]

def route_signal(signal_df):
    """
    Filters signals based on current trigger status:
    - Mutes signals from auto-muted strategies.
    - Optionally boosts scores for rewarded strategies.
    """
    muted = load_muted_strategies()
    rewarded = load_rewarded_strategies()

    if not signal_df.empty:
        # Remove muted strategy signals
        signal_df = signal_df[~signal_df['strategy'].isin(muted)]

        # Optional: boost confidence for rewarded strategies
        signal_df.loc[signal_df['strategy'].isin(rewarded), 'confidence'] *= 1.1
        signal_df['confidence'] = signal_df['confidence'].clip(upper=1.0)

    return signal_df
