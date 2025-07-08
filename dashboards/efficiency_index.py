import streamlit as st
import pandas as pd

st.set_page_config(page_title="Strategy Efficiency Index", layout="wide")

st.title("⚙️ Strategy Efficiency Index")

# Placeholder metrics
df = pd.DataFrame([
    {"Strategy": "LSTM", "Return": 0.23, "Drawdown": 0.08, "Trades": 120},
    {"Strategy": "TrendAlpha", "Return": 0.17, "Drawdown": 0.06, "Trades": 95},
    {"Strategy": "MacroEdge", "Return": 0.19, "Drawdown": 0.07, "Trades": 110},
    {"Strategy": "StatArb", "Return": 0.21, "Drawdown": 0.05, "Trades": 130},
])

df["Efficiency"] = df["Return"] / (df["Drawdown"] + 1e-5)
st.dataframe(df.style.background_gradient(subset=["Efficiency"], cmap="BuGn"))
