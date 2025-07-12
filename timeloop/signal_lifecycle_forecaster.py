def forecast_signal_lifecycle(signal_history):
    """
    Predicts stage of lifecycle: emergence, peak, decay, or latent.
    """
    if len(signal_history) < 5:
        return "emerging"
    deltas = [signal_history[i] - signal_history[i-1] for i in range(1, len(signal_history))]
    if all(d > 0 for d in deltas):
        return "ascending"
    elif all(d < 0 for d in deltas):
        return "decaying"
    else:
        return "latent"