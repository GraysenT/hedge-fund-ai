import streamlit as st
import pandas as pd
from logs.performance_logger import get_sharpe_history

def render_sharpe_chart(agent_name):
    data = get_sharpe_history(agent_name)
    if not data:
        st.warning("No Sharpe data found.")
        return
    df = pd.DataFrame(data, columns=["Time", "Sharpe"])
    df["Time"] = pd.to_datetime(df["Time"], unit="s")
    st.line_chart(df.set_index("Time"))