import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Alpha Saturation Map", layout="wide")

st.title("💥 Alpha Saturation Heatmap")

strategies = ["LSTM", "TrendAlpha", "StatArb", "MacroEdge"]
assets = ["AAPL", "SPY", "BTC", "GOLD"]
data = np.random.rand(len(strategies), len(assets)) * 100

saturation_df = pd.DataFrame(data, index=strategies, columns=assets)

st.write("### Alpha Exposure Across Strategies and Assets")
fig, ax = plt.subplots()
sns.heatmap(saturation_df, annot=True, cmap="Reds", fmt=".1f", ax=ax)
st.pyplot(fig)
