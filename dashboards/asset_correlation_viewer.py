import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Strategy-Asset Correlation Viewer", layout="wide")

st.title("🔗 Strategy-to-Asset Correlation Viewer")

# Placeholder correlation matrix
strategies = ["LSTM", "MacroEdge", "TrendAlpha", "StatArb"]
assets = ["AAPL", "SPY", "BTC", "GOLD"]
data = pd.DataFrame({
    strategy: [round(0.6 + 0.4 * i/len(assets), 2) for i in range(len(assets))]
    for strategy in strategies
}, index=assets)

st.write("### Correlation Matrix")
fig, ax = plt.subplots()
sns.heatmap(data.T, annot=True, cmap="Blues", fmt=".2f", ax=ax)
st.pyplot(fig)