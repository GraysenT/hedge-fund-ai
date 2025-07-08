import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Multi-Agent Alpha Comparison", layout="wide")

st.title("🤖 Multi-Agent Alpha Comparison")

agents = ["AgentA", "AgentB", "AgentC"]
metrics = ["Return", "Sharpe", "Drawdown"]
data = np.random.rand(len(agents), len(metrics))

df = pd.DataFrame(data, index=agents, columns=metrics)
st.dataframe(df.style.background_gradient(cmap="YlGnBu"))