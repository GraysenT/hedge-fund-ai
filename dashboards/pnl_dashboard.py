import streamlit as st
import pandas as pd
import os
from performance.realized_pnl_tracker import RealizedPnLTracker

st.set_page_config(page_title="💰 Realized P&L Dashboard", layout="wide")
st.title("💰 Realized Profit & Loss by Strategy")

LOG_FILE = "trade_logs.csv"

if not os.path.exists(LOG_FILE):
    st.warning("No trade log file found yet.")
else:
    tracker = RealizedPnLTracker()
    df = tracker.load_trade_log(LOG_FILE)
    pnl_df = tracker.compute_realized_pnl(df)

    if pnl_df.empty:
        st.info("No closed trades to compute realized P&L yet.")
    else:
        pnl_df["date"] = pd.to_datetime(pnl_df["timestamp"]).dt.date

        st.markdown("### 📈 Cumulative Realized P&L by Strategy")
        cumulative = pnl_df.groupby("strategy")["realized_pnl"].sum().sort_values(ascending=False)
        st.bar_chart(cumulative)

        st.markdown("### 📆 Daily Realized P&L Over Time")
        daily = pnl_df.groupby(["date", "strategy"])["realized_pnl"].sum().unstack().fillna(0)
        st.line_chart(daily)

        st.markdown("### 🧾 Recent Realized Trades")
        st.dataframe(pnl_df.sort_values("timestamp", ascending=False).head(20))
