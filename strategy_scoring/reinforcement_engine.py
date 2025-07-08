class ReinforcementEngine:
    def apply(self, base_weights: dict, performance_log=None, realized_pnl=None):
        """
        Boost strategies with strong recent performance.
        Can use either reward log or realized P&L.
        """
        reinforced = {}

        if realized_pnl:
            # Reinforce using actual P&L per strategy
            total_pnl = sum([max(p, 0) for p in realized_pnl.values()])
            for strat, weight in base_weights.items():
                pnl = max(realized_pnl.get(strat, 0), 0)
                boost = pnl / total_pnl if total_pnl > 0 else 0
                reinforced[strat] = weight * (1 + boost)
        elif performance_log is not None and not performance_log.empty:
            reward_by_strategy = performance_log.groupby("strategy")["reward"].mean().to_dict()
            for strat, weight in base_weights.items():
                reward = reward_by_strategy.get(strat, 0)
                reinforced[strat] = weight * (1 + reward)
        else:
            # Fallback: no data
            reinforced = base_weights

        # Normalize
        total = sum(reinforced.values())
        if total > 0:
            for k in reinforced:
                reinforced[k] /= total
        else:
            reinforced = base_weights

        return reinforced
