import streamlit as st
import subprocess

st.set_page_config(page_title="🧠 Hedge Fund AI: Dashboard Hub", layout="centered")
st.title("🧠 Hedge Fund AI: Dashboard Hub")

st.markdown("Select a dashboard to launch in a new window or tab:")

dashboards = {
    "📈 PnL Tracker": "dashboards/pnl_dashboard.py",
    "🛠 Self-Build Engine": "dashboards/self_build_dashboard.py",
    "🚦 Strategy Triggers": "dashboards/strategy_trigger_view.py",
    "🧠 Signal History": "dashboards/signal_history_viewer.py",
    "🛡 Patch Monitor": "dashboards/patch_monitor.py"
}

for label, path in dashboards.items():
    if st.button(label):
        st.markdown(f"`streamlit run {path}`")
        subprocess.Popen(["streamlit", "run", path])
        st.success(f"Launched {label}")

st.markdown("---")
st.caption("Your system is running in real time. Use this hub to inspect, control, and optimize.")