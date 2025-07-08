import streamlit as st
import pandas as pd

st.set_page_config(page_title="Risk & Regime Monitor", layout="wide")

st.title("⚠️ Risk & Regime Monitor")

# Placeholder data
regime_data = pd.DataFrame({
    "Macro Regime": ["Disinflation", "Growth Slowdown"],
    "Volatility": ["Low", "Rising"],
    "Risk Appetite": ["Moderate", "Fading"],
    "Equity Bias": ["Neutral", "Cautious"],
    "Hedge Status": ["Passive", "Active"]
})

st.dataframe(regime_data.style
    .highlight_max(axis=0)
    .applymap(lambda x: 'color: red' if x in ["Cautious", "Fading", "Active"] else '')
)