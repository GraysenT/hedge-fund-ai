import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(page_title="Capital Impact Timeline", layout="wide")

st.title("💹 Capital Impact Timeline")

# Placeholder timeline data
np.random.seed(42)
timeline = pd.DataFrame({
    "Time": pd.date_range(start="2024-07-01", periods=30, freq="D"),
    "Capital Impact": np.random.randn(30).cumsum()
})

chart = alt.Chart(timeline).mark_line(point=True).encode(
    x="Time",
    y="Capital Impact"
).properties(width=900)

st.altair_chart(chart)