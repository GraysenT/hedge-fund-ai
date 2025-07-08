import streamlit as st
import pandas as pd

st.set_page_config(page_title="Signal Strength Bar", layout="wide")

st.title("📶 Signal Strength Bar")

# Example data
signal_data = pd.DataFrame([
    {"Strategy": "LSTM", "Signal Strength": 0.92},
    {"Strategy": "TrendAlpha", "Signal Strength": 0.81},
    {"Strategy": "MacroEdge", "Signal Strength": 0.74},
    {"Strategy": "StatArb", "Signal Strength": 0.88},
])

st.bar_chart(signal_data.set_index("Strategy"))
