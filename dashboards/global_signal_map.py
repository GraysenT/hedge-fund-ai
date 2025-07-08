import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Signal Map", layout="wide")

st.title("🌍 Global Signal Influence Map")

# Placeholder data
signal_map = pd.DataFrame([
    {"Region": "US", "Active Signals": 12, "Dominant Strategy": "LSTM"},
    {"Region": "Europe", "Active Signals": 8, "Dominant Strategy": "MacroEdge"},
    {"Region": "Asia", "Active Signals": 5, "Dominant Strategy": "TrendAlpha"},
    {"Region": "Emerging", "Active Signals": 3, "Dominant Strategy": "StatArb"},
])

st.dataframe(signal_map.style.background_gradient(subset=["Active Signals"], cmap="YlGnBu"))