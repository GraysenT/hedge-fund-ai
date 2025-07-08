import streamlit as st
import pandas as pd
from strategies.stat_arb_engine import generate_stat_arb_signals
from pathlib import Path

TRADE_LOG = Path("execution_logs/stat_arb_trades.csv")

st.set_page_config(layout="wide")
st.title("📉 Statistical Arbitrage Dashboard")

# ───────────────────────────────────────────────────────────────
# Live Signal Generation
# ───────────────────────────────────────────────────────────────
signals_df = generate_stat_arb_signals()

st.subheader("📊 Current Stat Arb Z-Score Signals")

if signals_df.empty:
    st.info("No active statistical arbitrage signals right now.")
else:
    st.dataframe(signals_df, use_container_width=True)

# ───────────────────────────────────────────────────────────────
# Executed Trade Log Viewer
# ───────────────────────────────────────────────────────────────
st.subheader("🧾 Executed Trades")

if TRADE_LOG.exists():
    trade_df = pd.read_csv(TRADE_LOG)
    if not trade_df.empty:
        st.dataframe(trade_df.sort_values("timestamp", ascending=False), use_container_width=True)

        st.subheader("📉 Spread vs. Z-Score Heatmap")
        st.line_chart(trade_df[["zscore", "spread"]])
    else:
        st.info("Trade log exists but is empty.")
else:
    st.info("No trades have been executed yet.")