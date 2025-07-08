import streamlit as st
import os
import json
import pandas as pd

st.set_page_config(page_title="📜 Evolution Browser", layout="wide")
st.title("📜 Daily Evolution Snapshot Viewer")

SNAPSHOT_FOLDER = "snapshots"

# Load all JSON snapshot files
files = [f for f in os.listdir(SNAPSHOT_FOLDER) if f.startswith("evolution_") and f.endswith(".json")]
files.sort(reverse=True)

if not files:
    st.warning("No evolution snapshot files found.")
else:
    selected = st.selectbox("Select a snapshot date", files)

    with open(os.path.join(SNAPSHOT_FOLDER, selected)) as f:
        data = json.load(f)

    st.markdown(f"### 📅 Snapshot Timestamp: `{data['timestamp']}`")

    st.markdown("### 🧠 Strategy Weights")
    weights_df = pd.DataFrame.from_dict(data["weights"], orient="index", columns=["Weight"])
    st.dataframe(weights_df.style.format({"Weight": "{:.2%}"}))

    st.markdown("### 📴 Muted Strategies")
    st.write(data["muted"])

    st.markdown("### 📬 Alerts")
    for alert in data["alerts"]:
        st.warning(alert)

    st.markdown("### 🩺 Alpha Health Report")
    st.dataframe(pd.DataFrame.from_dict(data["alpha_health"], orient="index"))
