import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Alpha Heatmap by Regime", layout="wide")

st.title("🔍 Alpha Heatmap by Regime")

# Placeholder matrix
strategies = ["LSTM", "TrendAlpha", "MacroEdge", "StatArb"]
regimes = ["Growth", "Inflation", "Recession", "Neutral"]
data = np.random.rand(len(strategies), len(regimes))

heat_df = pd.DataFrame(data, index=strategies, columns=regimes)

st.write("### Regime-Conditioned Alpha Performance")
fig, ax = plt.subplots()
sns.heatmap(heat_df, annot=True, cmap="YlOrRd", ax=ax)
st.pyplot(fig)