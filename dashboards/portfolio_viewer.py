import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Portfolio Viewer", layout="wide")
st.title("💼 Portfolio Strategy Allocator")

file_path = os.path.join("logs", "strategy_weights.csv")

if not os.path.exists(file_path):
    st.error("🚫 No portfolio weights found. Run the portfolio allocator first.")
else:
    df = pd.read_csv(file_path)

    st.success("✅ Portfolio weights loaded.")
    st.dataframe(df.style.format(
        {"Avg Return": "{:.2f}", "Accuracy": "{:.2%}", "Weight": "{:.2%}"}))

    st.divider()
    st.subheader("📊 Strategy Weights")

    chart_data = df.set_index("Strategy")["Weight"]
    st.bar_chart(chart_data)

    st.subheader("📈 Accuracy vs Return")
    st.line_chart(df.set_index("Strategy")[["Accuracy", "Avg Return"]])

    st.download_button("📥 Export Weights CSV", df.to_csv(
        index=False), "strategy_weights.csv")
