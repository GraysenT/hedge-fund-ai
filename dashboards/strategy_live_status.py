import pandas as pd
import streamlit as st
from utils.loaders import load_json, load_csv
from utils.paths import STRATEGY_STATUS_FILE, ALPHA_HEALTH_FILE

st.set_page_config(layout="wide", page_title="🔍 Strategy Live Status")

st.title("📊 Live Strategy Status Dashboard")

# Load data
status = load_json(STRATEGY_STATUS_FILE)
alpha = load_csv(ALPHA_HEALTH_FILE)

# Convert to DataFrame
status_df = pd.DataFrame(status)
if not status_df.empty:
    status_df = status_df.set_index("Strategy")

# Display filters
col1, col2 = st.columns(2)
with col1:
    strategy_filter = st.multiselect("Filter Strategies", status_df.index, default=status_df.index)
with col2:
    min_conf = st.slider("Min Confidence", 0.0, 1.0, 0.0)

filtered_df = status_df.loc[strategy_filter]
filtered_df = filtered_df[filtered_df["Confidence"] >= min_conf]

# Merge with alpha health if available
if not alpha.empty and "Strategy" in alpha.columns:
    alpha = alpha.set_index("Strategy")
    merged = filtered_df.join(alpha, how="left")
else:
    merged = filtered_df

st.dataframe(merged, use_container_width=True)