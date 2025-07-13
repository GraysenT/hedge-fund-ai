def adaptive_weight(sim_results, live_pnl):
    if sim_results["avg_roi"] > 0.02 and live_pnl < 0:
        return 0.3  # reduce live exposure
    elif live_pnl > 0.01:
        return 1.0  # full confidence
    return 0.5  # default

def feedback_to_execution(sim_output, live_context):
    weight = adaptive_weight(sim_output, live_context["pnl"])
    if weight > 0.5:
        deploy_signal(sim_output["top_signal"], "ETH/USDT", live_context["price"], balance=live_context["balance"])