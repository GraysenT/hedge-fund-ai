import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="PnL vs Signal Correlation", layout="wide")

st.title("📈 PnL vs Signal Correlation")

# Placeholder data
np.random.seed(42)
data = pd.DataFrame({
    "LSTM_Signal": np.random.rand(50),
    "TrendAlpha_Signal": np.random.rand(50),
    "StatArb_Signal": np.random.rand(50),
    "MacroEdge_Signal": np.random.rand(50),
    "PnL": np.random.randn(50).cumsum()
})

corr = data.corr()

st.write("### Correlation Matrix")
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)