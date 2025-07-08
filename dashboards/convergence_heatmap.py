import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Alpha Convergence Heatmap", layout="wide")

st.title("📉 Alpha Convergence Heatmap")

# Placeholder synthetic matrix
strategies = ["LSTM", "TrendAlpha", "MacroEdge", "StatArb"]
data = np.random.uniform(0.7, 1.0, size=(4, 4))  # confidence similarity

df = pd.DataFrame(data, index=strategies, columns=strategies)

st.write("### Signal Alignment Across Strategies")
fig, ax = plt.subplots()
sns.heatmap(df, annot=True, cmap="Greens", fmt=".2f", ax=ax)
st.pyplot(fig)