import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="News Reaction Map", layout="wide")

st.title("📰 News Reaction Heatmap")

# Placeholder sentiment reaction data
news_effects = pd.DataFrame({
    "Headline": [
        "Fed raises rates",
        "Crypto ETF approved",
        "China GDP misses forecast",
        "Tech earnings beat"
    ],
    "SPY Impact": [0.012, -0.002, -0.015, 0.014],
    "BTC Impact": [-0.004, 0.032, -0.005, 0.006],
    "AAPL Impact": [-0.003, 0.001, -0.009, 0.021]
})

st.write("### Impact of Recent Headlines on Key Assets")
fig, ax = plt.subplots()
sns.heatmap(news_effects.set_index("Headline"), annot=True, cmap="coolwarm", fmt=".3f", ax=ax)
st.pyplot(fig)