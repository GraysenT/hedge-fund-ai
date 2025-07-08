import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Risk Flag Timeline", layout="wide")

st.title("🚨 Risk Flag Timeline")

# Placeholder data
log = pd.DataFrame([
    {"Time": "2024-07-01 09:30", "Flag": "High Drawdown", "Severity": 0.82},
    {"Time": "2024-07-01 10:10", "Flag": "Vol Spike", "Severity": 0.74},
    {"Time": "2024-07-01 10:55", "Flag": "Strategy Drift", "Severity": 0.67},
    {"Time": "2024-07-01 11:35", "Flag": "Low Confidence", "Severity": 0.59},
])

chart = alt.Chart(log).mark_bar().encode(
    x="Time",
    y="Severity",
    color="Flag",
    tooltip=["Time", "Flag", "Severity"]
).properties(width=900)

st.altair_chart(chart)