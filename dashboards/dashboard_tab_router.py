import streamlit as st

st.set_page_config(page_title="Hedge Fund AI Dashboard", layout="wide")

st.sidebar.title("🧭 Navigation")
selection = st.sidebar.radio("Select View:", [
    "Global Control",
    "Signal Monitor",
    "Alpha Health",
    "Risk & Regime",
    "Strategy Heritage"
])

if selection == "Global Control":
    exec(open("dashboards/global_control.py").read())
elif selection == "Signal Monitor":
    exec(open("dashboards/signal_monitor.py").read())
elif selection == "Alpha Health":
    exec(open("dashboards/alpha_health.py").read())
elif selection == "Risk & Regime":
    exec(open("dashboards/risk_and_regime.py").read())
elif selection == "Strategy Heritage":
    st.title("📜 Strategy Heritage Viewer")
    st.write("View ancestry and evolution of all deployed strategies.")
    exec(open("memory/strategy_heritage.py").read())