import pandas as pd

class RealizedPnLTracker:
    def __init__(self):
        self.positions = {}

    def load_trade_log(self, filepath):
        df = pd.read_csv(filepath, parse_dates=["timestamp"])
        df = df[df["status"] == "success"]
        df = df.sort_values("timestamp")
        return df

    def compute_realized_pnl(self, df):
        pnl_records = []

        for _, row in df.iterrows():
            strategy = row["strategy"] if "strategy" in row else row.get("strategy", "Unknown")
            ticker = row.get("ticker", "UNKNOWN")
            key = (strategy, ticker)
            side = row.get("side")
            qty = row.get("qty")
            price = row.get("price")

            if side == "buy":
                self.positions.setdefault(key, []).append({"qty": qty, "price": price})
            elif side == "sell":
                open_trades = self.positions.get(key, [])
                remaining_qty = qty
                realized_pnl = 0.0
                while remaining_qty > 0 and open_trades:
                    open_trade = open_trades[0]
                    matched_qty = min(remaining_qty, open_trade["qty"])
                    pnl = matched_qty * (price - open_trade["price"])
                    realized_pnl += pnl
                    open_trade["qty"] -= matched_qty
                    remaining_qty -= matched_qty
                    if open_trade["qty"] == 0:
                        open_trades.pop(0)

                if qty > 0:
                    pnl_records.append({
                        "timestamp": row["timestamp"],
                        "strategy": strategy,
                        "ticker": ticker,
                        "qty": qty,
                        "sell_price": price,
                        "realized_pnl": round(realized_pnl, 2)
                    })

        result_df = pd.DataFrame(pnl_records)
        if "strategy" not in result_df.columns:
            result_df["strategy"] = "Unknown"
        return result_df
