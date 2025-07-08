import streamlit as st
import pandas as pd
import os
import json

st.set_page_config(page_title="Hedge Fund AI Control Center", layout="wide")

st.title("💹 Hedge Fund AI Control Center")

# === LIVE SIGNALS ===
st.subheader("📡 Live Signals")
if os.path.exists("logs/signal_events.json"):
    try:
        signals = pd.read_json("logs/signal_events.json")
        st.dataframe(signals.tail(10), use_container_width=True)
    except:
        st.warning("⚠️ Could not load signals.")
else:
    st.info("No signal log yet.")

# === TRADE HISTORY ===
st.subheader("💰 Recent Trades")
if os.path.exists("logs/trade_history.json"):
    try:
        trades = pd.read_json("logs/trade_history.json")
        trades["timestamp"] = pd.to_datetime(trades["timestamp"])
        st.dataframe(trades.tail(10), use_container_width=True)

        pnl_chart = trades.groupby("timestamp")["pnl"].sum().cumsum()
        st.line_chart(pnl_chart)
    except:
        st.warning("⚠️ Could not load trades.")
else:
    st.info("No trades yet.")

# === STRATEGY ALLOCATIONS ===
st.subheader("📈 Current Allocations")
if os.path.exists("memory/optimized_allocations.json"):
    try:
        alloc = pd.read_json("memory/optimized_allocations.json")
        if "strategy" in alloc.columns and "weight" in alloc.columns:
            st.bar_chart(alloc.set_index("strategy")["weight"])
        else:
            st.warning("⚠️ Allocation file missing required columns.")
    except:
        st.warning("⚠️ Could not parse allocation data.")
else:
    st.warning("No allocation data found.")

# === SYSTEM STATUS ===
st.subheader("🛡️ System Status")
files = [
    "memory/deployability_scores.json",
    "memory/confidence_vs_risk.json",
    "memory/optimized_allocations.json",
    "memory/alpha_attribution.json",
    "memory/global_risk_matrix.json",
    "logs/trade_history.json"
]

for f in files:
    if os.path.exists(f) and os.stat(f).st_size > 0:
        st.success(f"✅ {f}")
    else:
        st.error(f"❌ {f} missing or empty")

st.markdown("---")
st.caption("© 2025 Hedge Fund AI | Graysen Torczon")