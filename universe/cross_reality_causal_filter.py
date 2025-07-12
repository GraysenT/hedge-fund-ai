def filter_causal_truths(all_signals):
    """
    Retains only causal beliefs that hold across multiple universes or simulations.
    """
    truth_set = []
    for sig in all_signals:
        if sig.get("passed_sim_universe") and sig.get("passed_real_universe"):
            truth_set.append(sig)
    return truth_set