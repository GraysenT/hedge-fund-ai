import streamlit as st
import pandas as pd

st.set_page_config(page_title="Signal Monitor", layout="wide")

st.title("📡 Signal Monitor")

# Placeholder Data
signal_data = pd.DataFrame([
    {"Symbol": "AAPL", "Strategy": "LSTM", "Confidence": 0.93, "Action": "BUY"},
    {"Symbol": "ETHUSD", "Strategy": "TrendAlpha", "Confidence": 0.88, "Action": "BUY"},
    {"Symbol": "GLD", "Strategy": "MacroTrend", "Confidence": 0.76, "Action": "HOLD"},
    {"Symbol": "SPY", "Strategy": "VolatilitySwitch", "Confidence": 0.95, "Action": "SELL"}
])

st.dataframe(signal_data.style
    .background_gradient(subset=["Confidence"], cmap='Greens')
    .applymap(lambda x: 'color: red' if isinstance(x, str) and x == "SELL" else '')
)
