import streamlit as st
import subprocess
import os
import json

st.set_page_config(page_title="Hedge Fund AI Dashboard", layout="wide")

st.title("🧠 Unified Hedge Fund AI System")

st.sidebar.title("📊 Modules")

options = [
    "Capital Allocation",
    "Strategy Lineage",
    "Agent Leaderboard",
    "Performance Summary",
    "Plugin Leaderboard",
    "Run Plugin",
    "Send Push Alert",
    "Visual Lineage Tree",
    "Trigger Evolution Loop",
]

choice = st.sidebar.radio("Select View", options)

if choice == "Capital Allocation":
    path = "memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]
    st.header("💸 Capital Allocation")
    st.json(json.load(open(path)))

elif choice == "Strategy Lineage":
    subprocess.run(["python3", "dashboards/lineage_viewer.py"])
    st.success("👁 View console for lineage tree")

elif choice == "Agent Leaderboard":
    subprocess.run(["python3", "dashboards/agent_leaderboard.py"])
    st.success("👁 View console for leaderboard")

elif choice == "Performance Summary":
    subprocess.run(["python3", "dashboards/strategy_leaderboard.py"])
    st.success("👁 View console for PnL summary")

elif choice == "Plugin Leaderboard":
    subprocess.run(["python3", "dashboards/plugin_leaderboard.py"])
    st.success("👁 View console for plugin log")

elif choice == "Run Plugin":
    name = st.text_input("Enter plugin name:")
    if st.button("Run"):
        subprocess.run(["python3", "plugins/plugin_sandbox.py", name])
        st.success(f"Ran plugin: {name}")

elif choice == "Send Push Alert":
    msg = st.text_input("Enter message to send")
    if st.button("Send"):
        from alerts.push_alerts import send_push
        send_push("📣 System Alert", msg)
        st.success("Push sent!")

elif choice == "Visual Lineage Tree":
    subprocess.run(["python3", "dashboards/visual_replay.py"])
    st.success("👁 View console or popup for strategy lineage")

elif choice == "Trigger Evolution Loop":
    subprocess.run(["python3", "evolve.py"])
    st.success("🔁 Evolution cycle complete.")
