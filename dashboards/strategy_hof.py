import os
import json
import streamlit as st
import pandas as pd

HOF_PATH = "strategy_memory/strategy_hof.json"

st.set_page_config(page_title="🏆 Strategy Hall of Fame", layout="wide")
st.title("🏆 Strategy Hall of Fame Viewer")

if not os.path.exists(HOF_PATH):
    st.warning("No Hall of Fame data found. Run recursive_generator.py to populate.")
    st.stop()

with open(HOF_PATH, 'r') as f:
    hof = json.load(f)

if not hof:
    st.warning("Hall of Fame is currently empty.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame.from_dict(hof, orient='index')
df.index.name = "Strategy"
df.reset_index(inplace=True)

# Filter
min_sharpe = st.sidebar.slider("Minimum Sharpe", 0.0, 3.0, 1.0, 0.1)
df_filtered = df[df["sharpe"] >= min_sharpe]

st.subheader("📋 Top Strategies")
st.dataframe(df_filtered.sort_values(by="sharpe", ascending=False), use_container_width=True)

# Download
st.download_button(
    label="📥 Download Hall of Fame",
    data=df_filtered.to_csv(index=False),
    file_name="strategy_hall_of_fame.csv",
    mime="text/csv"
)
