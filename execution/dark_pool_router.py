def execute_dark(order, venues):
    best_liquidity = max(venues, key=lambda v: v.get_liquidity(order.symbol))
    return best_liquidity.execute(order)