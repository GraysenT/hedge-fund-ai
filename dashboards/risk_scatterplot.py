import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(page_title="Risk Correlation Scatterplot", layout="wide")

st.title("🔬 Risk-Return Scatterplot")

# Placeholder data
strategies = ["LSTM", "TrendAlpha", "MacroEdge", "StatArb"]
data = pd.DataFrame({
    "Strategy": strategies,
    "Return": np.random.rand(4) * 0.25,
    "Risk": np.random.rand(4) * 0.2
})

chart = alt.Chart(data).mark_circle(size=200).encode(
    x="Risk",
    y="Return",
    color="Strategy",
    tooltip=["Strategy", "Return", "Risk"]
).interactive()

st.altair_chart(chart, use_container_width=True)
