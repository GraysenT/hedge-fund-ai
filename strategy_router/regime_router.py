def filter_by_regime(signals_df, regime):
    return signals_df[signals_df.get("regime", "neutral") == regime]