import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="⏱️ Performance Diagnostics", layout="wide")
st.title("⏱️ Execution Performance Diagnostics")

st.markdown("Upload or load tick-level execution simulation results below:")

uploaded_file = st.file_uploader("📄 Upload execution results CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["signal_time", "execution_time"])
    st.success("✅ Data loaded successfully!")

    st.markdown("### 📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Delay (s)", f"{df['delay_sec'].mean():.3f}")
    with col2:
        st.metric("Average Slippage", f"{df['slippage'].mean():.5f}")
    with col3:
        st.metric("Total Trades", f"{len(df)}")

    st.markdown("### ⏳ Delay Distribution")
    fig1, ax1 = plt.subplots()
    ax1.hist(df["delay_sec"], bins=30, color="skyblue", edgecolor="black")
    ax1.set_title("Signal Delay Distribution (seconds)")
    ax1.set_xlabel("Delay (s)")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    st.markdown("### 📉 Slippage by Signal Confidence")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["confidence"], df["slippage"], alpha=0.6)
    ax2.set_title("Slippage vs Signal Confidence")
    ax2.set_xlabel("Signal Confidence")
    ax2.set_ylabel("Slippage")
    st.pyplot(fig2)

    st.markdown("### 📈 Execution Time vs Signal Time")
    fig3, ax3 = plt.subplots()
    ax3.plot(df["signal_time"], df["execution_price"], label="Execution Price", alpha=0.7)
    ax3.set_title("Execution Price Over Time")
    ax3.set_xlabel("Signal Time")
    ax3.set_ylabel("Price")
    st.pyplot(fig3)

else:
    st.info("Awaiting CSV upload...")
