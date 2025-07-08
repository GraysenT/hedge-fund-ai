import streamlit as st
from global.global_hours import GlobalMarketHours
import time

st.set_page_config(page_title="🌍 Global Market Status", layout="wide")
st.title("🌍 Global Market Activity Dashboard")

gh = GlobalMarketHours()

status = gh.get_exchange_status()
local_times = gh.get_current_local_times()
open_exchanges = gh.get_open_exchanges()

st.markdown("### 📅 Real-Time Exchange Status")
for exchange in status:
    col1, col2 = st.columns(2)
    with col1:
        emoji = "🟢 Open" if status[exchange] else "🔴 Closed"
        st.markdown(f"**{exchange}:** {emoji}")
    with col2:
        st.markdown(f"Local Time: `{local_times[exchange]}`")

st.markdown("---")
st.markdown("### 🔁 This page auto-refreshes every 15 seconds.")
time.sleep(15)
st.experimental_rerun()
