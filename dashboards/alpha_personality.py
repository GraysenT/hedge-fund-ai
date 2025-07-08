import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alpha Personality Map", layout="wide")

st.title("🧬 Alpha Personality Visualizer")

personality_data = pd.DataFrame([
    {"Strategy": "LSTM", "Conviction": 0.92, "Volatility": 0.28, "Adaptivity": 0.67},
    {"Strategy": "TrendAlpha", "Conviction": 0.74, "Volatility": 0.15, "Adaptivity": 0.84},
    {"Strategy": "StatArb", "Conviction": 0.63, "Volatility": 0.22, "Adaptivity": 0.56},
    {"Strategy": "MacroEdge", "Conviction": 0.81, "Volatility": 0.19, "Adaptivity": 0.71},
])

st.bar_chart(personality_data.set_index("Strategy"))

st.dataframe(personality_data.style.background_gradient(cmap="Purples"))