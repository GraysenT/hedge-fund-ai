from data.symbol_universe import get_universe
from data.volatility_filter import rank_by_volatility
from data.live_symbol_selector import get_trending_symbols

def build_dynamic_symbol_set():
    base = get_universe()
    vol_filtered = rank_by_volatility(base)
    trending = get_trending_symbols()

    selected = list(set([s for s, _ in vol_filtered] + trending))
    print(f"✅ Final dynamic universe: {selected[:10]} ... ({len(selected)} total)")
    return selected

if __name__ == "__main__":
    build_dynamic_symbol_set()
