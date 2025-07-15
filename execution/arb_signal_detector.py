def detect_arbitrage(quotes):
    for s1 in quotes:
        for s2 in quotes:
            if quotes[s1] < quotes[s2]:
                return (s1, s2)