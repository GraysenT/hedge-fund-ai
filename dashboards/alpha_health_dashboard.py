import streamlit as st
import pandas as pd
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from risk_control.alpha_defense import AlphaDefense
from performance.realized_pnl_tracker import RealizedPnLTracker

st.set_page_config(page_title="🛡️ Alpha Health Monitor", layout="wide")
st.title("🛡️ Strategy Alpha Health Dashboard")

LOG_FILE = "trade_logs.csv"

if not os.path.exists(LOG_FILE):
    st.warning("No trade log file found.")
else:
    tracker = RealizedPnLTracker()
    trade_df = tracker.load_trade_log(LOG_FILE)
    pnl_df = tracker.compute_realized_pnl(trade_df)

    # ✅ DEBUG: Show exact column names and data
    st.write("DEBUG: Realized P&L Columns:", pnl_df.columns.tolist())
    st.dataframe(pnl_df)

    defender = AlphaDefense()

    if "strategy" in pnl_df.columns:
        report = defender.evaluate(pnl_df)

        report_df = pd.DataFrame.from_dict(report, orient="index").reset_index().rename(columns={"index": "Strategy"})

        st.markdown("### 🧠 Strategy Health Summary")
        st.dataframe(report_df.style.format({
            "pnl": "${:.2f}",
            "hit_rate": "{:.0%}"
        }))

        st.markdown("### 🔍 Status Legend")
        st.info("🟢 healthy | 🟡 at_risk | 🔴 decayed | ⚪ insufficient_data")
    else:
        st.error("❌ 'strategy' column is missing from realized P&L. Check trade log + tracker.")
