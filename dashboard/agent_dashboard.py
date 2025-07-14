import streamlit as st
import os, json

st.set_page_config(layout="wide", page_title="Capital Intelligence Dashboard")
st.title("🧠 Capital Intelligence Dashboard")

markets = ["ETHUSD", "BTCUSD", "AAPL", "SPX", "SOLUSD"]
for m in markets:
    path = f"state/{m}.json"
    if os.path.exists(path):
        st.subheader(f"📈 {m}")
        with open(path) as f:
            st.json(json.load(f))