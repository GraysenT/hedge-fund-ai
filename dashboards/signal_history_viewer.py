import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Signal History Viewer", layout="wide")
st.title("📘 Signal History Viewer – AI Forecast Log")

log_path = os.path.join("logs", "signal_log.csv")
weights_path = os.path.join("logs", "portfolio_memory.csv")

if not os.path.exists(log_path):
    st.error("🚫 No signal_log.csv file found. Please run the signal fusion engine first.")
else:
    df = pd.read_csv(log_path)
    if df.empty:
        st.warning("⚠️ Signal log is empty.")
    else:
        df["Date"] = pd.to_datetime(df["Date"])

        st.success(f"✅ Loaded {len(df)} logged signals.")
        st.dataframe(df.sort_values("Date", ascending=False))

        st.divider()
        st.subheader("🔍 Filter Your Signal History")

        asset_filter = st.multiselect("Select Assets", options=sorted(df["Asset"].unique()), default=df["Asset"].unique())
        signal_filter = st.multiselect("Signal Type", options=["Buy", "Sell", "Hold"], default=["Buy", "Sell", "Hold"])
        date_range = st.date_input("Date Range", [])

        filtered = df[df["Asset"].isin(asset_filter) & df["Signal"].isin(signal_filter)]

        if len(date_range) == 2:
            filtered = filtered[
                (filtered["Date"] >= pd.to_datetime(date_range[0])) &
                (filtered["Date"] <= pd.to_datetime(date_range[1]))
            ]

        st.write("📄 Filtered Signal Results")
        st.dataframe(filtered.sort_values("Date", ascending=False))

        st.download_button("📥 Download Filtered CSV", filtered.to_csv(index=False), "filtered_signals.csv")

        # === SIGNAL + WEIGHT OVERLAY ===
        st.divider()
        st.subheader("📊 Signal + Strategy Weight Overlay")

        if not os.path.exists(weights_path):
            st.warning("⚠️ Cannot display overlay — no portfolio memory found.")
        else:
            weights_df = pd.read_csv(weights_path)
            weights_df["Date"] = pd.to_datetime(weights_df["Date"])
            merged = pd.merge(filtered, weights_df, how="left", on=["Date", "Strategy"])

            st.write("🧠 Signals with weights applied at execution:")
            st.dataframe(merged[["Date", "Asset", "Signal", "Confidence", "Strategy", "Weight"]])
            st.caption("Shows which strategy generated each signal and how much capital it had at the time.")
            