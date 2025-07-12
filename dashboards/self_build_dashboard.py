import streamlit as st
import os
from utils.paths import SELF_BUILD_LOG

st.set_page_config(page_title="Self-Build Dashboard", layout="wide")

st.title("🤖 Self-Build AI Module Tracker")

if not os.path.exists(SELF_BUILD_LOG):
    st.warning("No build log found.")
else:
    with open(SELF_BUILD_LOG, "r") as f:
        logs = f.readlines()

    logs = logs[-200:]  # show recent 200 events
    for line in reversed(logs):
        if "✅" in line:
            st.success(line.strip())
        elif "🛠️" in line:
            st.info(line.strip())
        elif "❌" in line or "⚠️" in line:
            st.error(line.strip())
        else:
            st.write(line.strip())