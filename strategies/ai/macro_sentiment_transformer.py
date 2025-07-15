def macro_signal(macro):
    if macro['GDP'] > 3 and macro['CPI'] < 2:
        return 'bullish'
    return 'neutral'