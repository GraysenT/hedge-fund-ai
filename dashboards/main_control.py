import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="🧠 Main Control Dashboard", layout="wide")
st.title("🧠 Master Control Panel")

# Define dashboard runner wrappers with safe exec
def load_dashboard(path):
    try:
        with open(path) as f:
            code = f.read()
            exec(code, globals())
    except Exception as e:
        st.error(f"Failed to load {path}: {e}")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Strategy Control",
    "💰 Performance",
    "🛡️ Alpha Health",
    "📊 Exposure",
    "🧬 Evolution History"
])

with tab1:
    st.markdown("### 📈 Strategy Control View")
    load_dashboard("dashboards/strategy_control.py")

with tab2:
    st.markdown("### 💰 Performance Tracker View")
    load_dashboard("dashboards/performance_tracker.py")

with tab3:
    st.markdown("### 🛡️ Alpha Health Monitor View")
    load_dashboard("dashboards/alpha_health_dashboard.py")

with tab4:
    st.markdown("### 📊 Exposure Dashboard View")
    load_dashboard("dashboards/exposure_dashboard.py")

with tab5:
    st.markdown("### 🧬 Evolution Snapshot Browser")
    load_dashboard("dashboards/evolution_browser.py")
