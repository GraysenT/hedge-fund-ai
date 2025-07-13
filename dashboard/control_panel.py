import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")
st.title("🧠 Hedge Fund AI - Strategy Control Panel")

# Strategies
strategies = requests.get("http://localhost:8080/strategies").json()
st.sidebar.subheader("Strategies")
selected = st.sidebar.radio("Select a Strategy", strategies)

# Live Signal Test
st.subheader(f"🚨 Live Signal from {selected}")
input_price = st.number_input("Price", value=100.0)
input_ma = st.number_input("Moving Avg", value=98.0)

if st.button("Generate Signal"):
    response = requests.post("http://localhost:8080/signal", json={"data": {
        "price": input_price, "ma": input_ma
    }}).json()
    st.metric(label="Signal", value=response.get(selected))

# Logs
st.subheader("📈 Signal Logs")
log_data = pd.read_csv("logs/signal_log.csv")
st.dataframe(log_data.tail(20), use_container_width=True)