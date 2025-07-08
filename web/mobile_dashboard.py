import streamlit as st
import json
import os

st.set_page_config(page_title="📱 Mobile Fund View", layout="centered")

st.title("📊 Fund Snapshot")

with open("memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]) as f:
    cap = json.load(f)

st.subheader("💸 Capital Allocation")
for strat, val in cap.items():
    st.write(f"{strat}: ${round(val * 1_000_000, 2)}")

perf = sorted(os.listdir("memory/performance"))[-1]
with open(f"memory/performance/{perf}") as f:
    data = json.load(f)

st.subheader("📈 Daily PnL")
for k, v in data.items():
    st.write(f"{k}: {round(v['pnl'], 2)}")

if st.button("📤 Send Push Summary"):
    from alerts.push_alerts import send_push
    msg = "\n".join([f"{k}: ${round(v['pnl'],2)}" for k,v in data.items()])
    send_push("📱 Daily Summary", msg)
    st.success("Push sent")
