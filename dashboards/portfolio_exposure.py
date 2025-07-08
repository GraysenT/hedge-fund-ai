import streamlit as st
import os
import json
import pandas as pd
import plotly.express as px

REBALANCED_PATH = "strategy_memory/rebalanced_weights.json"
POSITION_TAGS_PATH = "strategy_memory/long_short_tags.json"

st.set_page_config(page_title="📊 Portfolio Exposure", layout="wide")
st.title("📊 Portfolio Exposure Overview")

# Load data
def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

weights = load_json(REBALANCED_PATH)
tags = load_json(POSITION_TAGS_PATH)

if not weights:
    st.warning("⚠️ No rebalanced weights found. Run the rebalancer to generate output.")
    st.stop()

# Create DataFrame
data = []
for strat, weight in weights.items():
    tag = tags.get(strat, "long")
    direction = "Long" if weight >= 0 else "Short"
    data.append({"Strategy": strat, "Weight": weight, "Tag": tag, "Direction": direction})

exposure_df = pd.DataFrame(data).sort_values(by="Weight", ascending=False)

# Exposure stats
net_exposure = round(exposure_df["Weight"].sum(), 4)
gross_exposure = round(exposure_df["Weight"].abs().sum(), 4)

st.metric("📉 Net Exposure", f"{net_exposure:.2f}")
st.metric("📈 Gross Exposure", f"{gross_exposure:.2f}")

# Charts
st.subheader("📊 Strategy Weights by Direction")
fig = px.bar(exposure_df, x="Strategy", y="Weight", color="Direction", title="Long vs Short Allocations")
fig.update_layout(xaxis_title="Strategy", yaxis_title="Weight", legend_title="Direction")
st.plotly_chart(fig, use_container_width=True)

# Table view
st.subheader("📋 Detailed Allocation Table")
st.dataframe(exposure_df, use_container_width=True)

# Download button
st.download_button(
    label="📥 Download Rebalanced Portfolio",
    data=json.dumps(weights, indent=2),
    file_name="rebalanced_weights.json",
    mime="application/json"
)
