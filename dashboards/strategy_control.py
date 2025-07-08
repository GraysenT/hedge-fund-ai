import streamlit as st
import pandas as pd
from alerts.strategy_triggers import (
    load_muted_strategies_df,
    load_rewarded_strategies_df,
)
from portfolio_ai.full_allocator import load_allocation_snapshot

st.set_page_config(layout="wide")
st.title("📊 Strategy Control Dashboard")

# Load Data
alloc_df = load_allocation_snapshot()
muted_df = load_muted_strategies_df()
rewarded_df = load_rewarded_strategies_df()

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📉 Muted Strategies")
    if muted_df.empty:
        st.info("No strategies are currently muted.")
    else:
        st.dataframe(muted_df, use_container_width=True)

with col2:
    st.subheader("🏆 Rewarded Strategies")
    if rewarded_df.empty:
        st.info("No strategies are currently rewarded.")
    else:
        st.dataframe(rewarded_df, use_container_width=True)

st.divider()

st.subheader("🧠 Allocation Snapshot (Live Strategy Weights)")
if alloc_df.empty:
    st.warning("No allocation data found.")
else:
    st.dataframe(alloc_df, use_container_width=True)
    