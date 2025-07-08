import streamlit as st
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = os.getenv("FINNHUB_API_KEY")
symbol = st.selectbox("Symbol", ["AAPL", "TSLA", "MSFT"])

def get_quote(sym):
    url = f"https://finnhub.io/api/v1/quote?symbol={sym}&token={API_KEY}"
    return requests.get(url).json()["c"]

df = pd.read_csv(f"data/price_history/{symbol}.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
price = get_quote(symbol)

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["close"], label="Close Price")
plt.axhline(price, color="red", linestyle="--", label=f"Live: ${price}")
plt.legend()
plt.title(f"{symbol} Price Chart with Live Overlay")
st.pyplot(plt)
