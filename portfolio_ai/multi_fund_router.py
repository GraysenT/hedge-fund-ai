import json
import os

FUND_CONFIG = {
    "AlphaCore": ["stat_arb", "momentum", "macro_sentiment"],
    "CryptoEdge": ["crypto_breakout", "stat_arb", "tweet_flow"],
    "QuantMacro": ["macro_sentiment", "volatility_rotation", "futures_spread"]
}

def route_strategies_to_funds(all_strategies):
    routed = {fund: [] for fund in FUND_CONFIG}

    for strat in all_strategies:
        for fund, allowed in FUND_CONFIG.items():
            if any(tag in strat["strategy"].lower() for tag in allowed):
                routed[fund].append(strat)

    for fund, subset in routed.items():
        os.makedirs(f"memory/funds/{fund}", exist_ok=True)
        with open(f"memory/funds/{fund}/allocations.json", "w") as f:
            json.dump(subset, f, indent=2)

    print("🏦 Strategies routed to multi-fund architecture.")
    return routed

if __name__ == "__main__":
    with open("memory/optimized_allocations.json") as f:
        strategies = json.load(f)
    route_strategies_to_funds(strategies)