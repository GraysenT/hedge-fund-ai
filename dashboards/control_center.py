import streamlit as st
import pandas as pd
from utils.loaders import load_json, load_csv
from utils.paths import *

st.set_page_config(layout="wide", page_title="🧠 Control Center")

st.title("🧠 Hedge Fund AI - Master Control Center")

tabs = st.tabs([
    "Live Signals", "Strategies", "Trades", "Alpha Health", "Overrides", "Deployment"
])

with tabs[0]:
    st.header("📡 Live Signals")
    try:
        signals = load_json(SIGNAL_LOG)
        st.dataframe(pd.DataFrame(signals).sort_values("confidence", ascending=False), use_container_width=True)
    except:
        st.warning("No signals loaded.")

with tabs[1]:
    st.header("📘 Strategies")
    try:
        strategies = load_json(STRATEGY_STATUS_FILE)
        st.dataframe(pd.DataFrame(strategies).sort_values("Confidence", ascending=False), use_container_width=True)
    except:
        st.warning("No strategy status file found.")

with tabs[2]:
    st.header("💼 Trade Journal")
    try:
        trades = pd.read_csv(TRADE_LOG_FILE)
        st.dataframe(trades.sort_values("Timestamp", ascending=False), use_container_width=True)
    except:
        st.warning("Trade log missing.")

with tabs[3]:
    st.header("🩺 Alpha Health Monitor")
    try:
        health = pd.read_csv(ALPHA_HEALTH_FILE)
        st.dataframe(health.sort_values("AlphaHealth", ascending=False), use_container_width=True)
    except:
        st.warning("Alpha health file not found.")

with tabs[4]:
    st.header("🎛 Manual Overrides")
    try:
        overrides = load_json(OVERRIDE_FILE)
        st.json(overrides)
    except:
        st.warning("No overrides active.")

with tabs[5]:
    st.header("🚀 Deployment Status")
    try:
        status = load_json(DEPLOYMENT_STATUS_FILE)
        st.dataframe(pd.DataFrame(status), use_container_width=True)
    except:
        st.warning("No deployment status file found.")