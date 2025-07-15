def stat_arb_signal(spread):
    return 'buy' if spread < -1.5 else 'sell' if spread > 1.5 else 'hold'
