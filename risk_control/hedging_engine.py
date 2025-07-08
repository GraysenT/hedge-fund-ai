import pandas as pd
from collections import defaultdict
from datetime import datetime

HEDGED_LOG = "execution_logs/hedging_actions.csv"

# Sample sector ETF hedges (expand as needed)
ETF_HEDGES = {
    "tech": "XLK",
    "energy": "XLE",
    "financials": "XLF",
    "broad": "SPY",
    "crypto": "BTC-USD"
}

# Sector tagging (simplified)
TICKER_SECTOR = {
    "AAPL": "tech",
    "MSFT": "tech",
    "GOOG": "tech",
    "META": "tech",
    "JPM": "financials",
    "XOM": "energy",
    "AMZN": "tech"
}

def estimate_sector_exposure(signal_df):
    """
    Estimate directional exposure by sector.
    """
    sector_exposure = defaultdict(float)

    for _, row in signal_df.iterrows():
        ticker = row.get("ticker", "")
        sector = TICKER_SECTOR.get(ticker, "broad")
        direction = 1 if row["signal"].lower().startswith("buy") else -1
        confidence = row.get("confidence", 0.5)
        sector_exposure[sector] += direction * confidence

    return dict(sector_exposure)

def generate_hedge_orders(exposure: dict, threshold=0.5):
    """
    Generate hedge trades based on exposure imbalance.
    """
    hedge_orders = []

    for sector, net_exposure in exposure.items():
        if abs(net_exposure) >= threshold:
            hedge_ticker = ETF_HEDGES.get(sector)
            if hedge_ticker:
                side = "sell" if net_exposure > 0 else "buy"
                hedge_orders.append({
                    "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    "hedge_ticker": hedge_ticker,
                    "side": side,
                    "sector": sector,
                    "exposure": round(net_exposure, 2)
                })

    return hedge_orders

def log_hedge_actions(orders):
    df = pd.DataFrame(orders)
    if not df.empty:
        try:
            pd.read_csv(HEDGED_LOG)  # Ensure file exists
            df.to_csv(HEDGED_LOG, mode="a", header=False, index=False)
        except FileNotFoundError:
            df.to_csv(HEDGED_LOG, index=False)
        print(f"✅ Logged {len(df)} hedge trades.")
    else:
        print("🟡 No hedge trades generated.")
        