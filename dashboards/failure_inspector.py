import streamlit as st
import pandas as pd
from reinforcement.failure_classifier import load_failure_data

st.set_page_config(layout="wide")
st.title("🚨 Signal Failure Inspector")

df = load_failure_data()

if df.empty:
    st.warning("No classified signal failures found.")
else:
    df["date"] = pd.to_datetime(df["date"])

    st.subheader("📋 All Failures and Causes")
    st.dataframe(df.sort_values("date", ascending=False), use_container_width=True)

    st.subheader("📊 Failure Count by Reason")
    reason_count = df["failure_reason"].value_counts()
    st.bar_chart(reason_count)

    st.subheader("🔥 Failure Heatmap by Strategy")
    heatmap_df = (
        df[df["failure"] == True]
        .groupby(["strategy", "failure_reason"])
        .size()
        .unstack()
        .fillna(0)
    )
    st.dataframe(heatmap_df.style.background_gradient(cmap="OrRd"))
    