import streamlit as st
import os
import json
import pandas as pd

SNAPSHOT_DIR = "strategy_memory/history"

st.set_page_config(page_title="📂 Snapshot History", layout="wide")
st.title("📂 Strategy Snapshot History")

# Get list of snapshot files
snapshots = sorted([f for f in os.listdir(SNAPSHOT_DIR) if f.endswith('.json')], reverse=True)

if not snapshots:
    st.warning("No snapshots found in strategy_memory/history")
    st.stop()

selected = st.selectbox("Select a snapshot", snapshots)

with open(os.path.join(SNAPSHOT_DIR, selected), 'r') as f:
    snapshot = json.load(f)

st.markdown(f"### 🕒 Timestamp: `{snapshot['timestamp']}`")

# Show tables
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Base Weights")
    st.dataframe(pd.DataFrame(snapshot['base_weights'].items(), columns=["Strategy", "Weight"]))

with col2:
    st.subheader("🧠 Reinforce Multipliers")
    st.dataframe(pd.DataFrame(snapshot['reinforce_weights'].items(), columns=["Strategy", "Multiplier"]))

st.subheader("✅ Final Allocated Weights")
df_final = pd.DataFrame(snapshot['final_weights'].items(), columns=["Strategy", "Final Weight"]).sort_values(by="Final Weight", ascending=False)
st.dataframe(df_final, use_container_width=True)

st.download_button(
    label="📥 Download This Snapshot",
    data=json.dumps(snapshot, indent=2),
    file_name=selected,
    mime="application/json"
)
