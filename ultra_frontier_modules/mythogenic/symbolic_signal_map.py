def map_symbols_to_themes(symbols):
    """
    Translates real-world symbolic behavior into mythic themes.
    E.g., 'gold', 'AI', 'WallStreetBets' → belief clusters
    """
    mapping = {}
    for s in symbols:
        if "gold" in s.lower():
            mapping[s] = "Wealth Preservation Myth"
        elif "btc" in s.lower() or "crypto" in s.lower():
            mapping[s] = "Decentralized Rebellion Myth"
        elif "ai" in s.lower():
            mapping[s] = "Superintelligence Ascension Myth"
        elif "federal" in s.lower():
            mapping[s] = "Monetary Control Myth"
        else:
            mapping[s] = "Unclassified Narrative"
    return mapping