ZONE_MAP = {
    "Americas": ["commodity_trader", "options_guard"],
    "Europe": ["macro_watcher", "futures_allocator"],
    "Asia": ["volatility_swarm", "sentiment_scout"],
    "Global": ["meta_signal", "long_term_forecaster"]
}

def get_zone_agents(region):
    return ZONE_MAP.get(region, [])