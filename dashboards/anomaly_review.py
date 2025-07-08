import streamlit as st
import pandas as pd

st.set_page_config(page_title="Anomaly-Triggered Signal Review", layout="wide")

st.title("🧠 Anomaly-Triggered Signal Review")

# Placeholder data
anomalies = pd.DataFrame([
    {"Timestamp": "2024-07-01 09:30", "Symbol": "AAPL", "Reason": "Volatility Spike", "Confidence": 0.91},
    {"Timestamp": "2024-07-01 10:15", "Symbol": "ETH", "Reason": "Dark Pool Alert", "Confidence": 0.87},
    {"Timestamp": "2024-07-01 11:45", "Symbol": "SPY", "Reason": "Macro Switch", "Confidence": 0.78},
])

st.dataframe(anomalies.style.background_gradient(subset=["Confidence"], cmap="OrRd"))
