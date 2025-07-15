laws = ['no overleverage', 'respect volatility']
def obey(strategy):
    return all(rule in strategy for rule in laws)
