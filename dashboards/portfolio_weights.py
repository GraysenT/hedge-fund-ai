import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio Weights", layout="wide")

st.title("📊 Portfolio Allocation Weights")

# Placeholder allocation weights
weights = {
    "LSTM": 0.32,
    "TrendAlpha": 0.21,
    "MacroEdge": 0.27,
    "StatArb": 0.20
}

weight_df = pd.DataFrame(list(weights.items()), columns=["Strategy", "Weight"])

st.bar_chart(weight_df.set_index("Strategy"))

st.dataframe(weight_df.style.background_gradient(subset=["Weight"], cmap="Blues"))