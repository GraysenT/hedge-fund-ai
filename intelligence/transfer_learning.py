def transfer_top_strategies(source_agent, target_agent, top_n=1):
    sorted_strats = sorted(source_agent.strategies, key=lambda s: s.performance_score, reverse=True)
    for strat in sorted_strats[:top_n]:
        clone = strat.__class__(name=f"{strat.name}_clone", parameters=dict(strat.parameters))
        target_agent.strategies.append(clone)
        print(f"🔁 Transferred {strat.name} to {target_agent.market}")