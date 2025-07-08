import streamlit as st
import pandas as pd

st.set_page_config(page_title="Latency Tracker", layout="wide")

st.title("⚡ Execution Latency Monitor")

# Placeholder data
latency_data = pd.DataFrame([
    {"Module": "Executor", "Latency (ms)": 42.1},
    {"Module": "Signal Router", "Latency (ms)": 15.3},
    {"Module": "Reinforcement Engine", "Latency (ms)": 21.8},
    {"Module": "Cache Lookup", "Latency (ms)": 5.9},
])

st.dataframe(latency_data.style.background_gradient(subset=["Latency (ms)"], cmap="Reds"))