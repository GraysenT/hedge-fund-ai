class TradeExecutor:
    def __init__(self, execution_threshold=0.05):
        """
        Args:
            execution_threshold: minimum change required to trigger a trade (e.g., 5%)
        """
        self.execution_threshold = execution_threshold

    def generate_orders(self, current_positions, target_weights):
        """
        Args:
            current_positions (dict): strategy -> current weight
            target_weights (dict): strategy -> desired weight
        Returns:
            list of dicts: each dict is an order with strategy, action, delta
        """
        orders = []
        strategies = set(current_positions.keys()).union(target_weights.keys())

        for strat in strategies:
            current = current_positions.get(strat, 0.0)
            target = target_weights.get(strat, 0.0)
            delta = target - current

            if abs(delta) >= self.execution_threshold:
                action = "buy" if delta > 0 else "sell"
                orders.append({
                    "strategy": strat,
                    "action": action,
                    "delta_weight": round(delta, 4),
                    "from": round(current, 4),
                    "to": round(target, 4)
                })

        return orders
