import streamlit as st
import pandas as pd
from reporting.alpha_attribution import compute_alpha_attribution

st.set_page_config(layout="wide", page_title="🌲 Alpha Attribution Tree")

st.title("🌲 Alpha Attribution Breakdown")

attribution = compute_alpha_attribution("logs/trades.csv")

st.subheader("📘 By Strategy")
st.bar_chart(attribution["ByStrategy"])

st.subheader("💠 By Asset")
st.bar_chart(attribution["ByAsset"])

st.subheader("🧠 By Signal Source")
st.bar_chart(attribution["BySignal"])