DEPLOYABLE_THEATERS = {
    "US_Equities": ["options_guard", "macro_oracle"],
    "Commodities": ["commodity_trader", "vol_spike_detector"],
    "Asia": ["futures_allocator", "currency_swarm"],
    "Crypto": ["degen_optimizer", "signal_sentinel"]
}

def get_agents_for_zone(zone):
    return DEPLOYABLE_THEATERS.get(zone, [])