import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Volatility Radar", layout="wide")

st.title("🌪️ Real-Time Volatility Radar")

# Placeholder data
assets = ["AAPL", "SPY", "BTC", "ETH", "GOLD"]
data = pd.DataFrame({
    "Asset": assets,
    "Volatility %": np.random.uniform(1.5, 5.0, size=len(assets))
})

st.dataframe(data.style.background_gradient(subset=["Volatility %"], cmap="Oranges"))
