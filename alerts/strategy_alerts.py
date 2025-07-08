import pandas as pd
from risk_control.alpha_defense import AlphaDefense
from performance.realized_pnl_tracker import RealizedPnLTracker

class StrategyAlertEngine:
    def __init__(self, log_file="trade_logs.csv"):
        self.log_file = log_file
        self.tracker = RealizedPnLTracker()
        self.defender = AlphaDefense()

    def get_muted_and_alerts(self):
        try:
            trade_df = self.tracker.load_trade_log(self.log_file)
            pnl_df = self.tracker.compute_realized_pnl(trade_df)
            report = self.defender.evaluate(pnl_df)
        except Exception as e:
            return [], [], f"Error: {e}"

        muted = []
        alerts = []

        for strat, stats in report.items():
            status = stats["status"]
            if status == "decayed":
                muted.append(strat)
                alerts.append(f"🔴 {strat} marked as decayed — auto-muted")
            elif status == "at_risk":
                alerts.append(f"🟡 {strat} at risk (Hit rate: {stats['hit_rate']:.0%}, PnL: ${stats['pnl']:.2f})")

        return muted, alerts, None
