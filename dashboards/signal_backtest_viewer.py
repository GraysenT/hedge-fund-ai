
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Signal Backtest Viewer", layout="wide")
st.title("📘 Signal Backtest Dashboard")

log_path = os.path.join("logs", "signal_log.csv")

if not os.path.exists(log_path):
    st.error("🚫 No signal log found. Run the system to generate signals.")
else:
    df = pd.read_csv(log_path)
    if df.empty:
        st.warning("⚠️ Signal log is empty.")
    else:
        df["Date"] = pd.to_datetime(df["Date"])

        st.success(f"✅ Loaded {len(df)} signals.")
        st.dataframe(df.sort_values("Date", ascending=False))

        # === FILTERS ===
        st.sidebar.header("🔍 Filter Signals")
        asset_filter = st.sidebar.multiselect(
            "Assets", options=df["Asset"].unique(), default=list(df["Asset"].unique()))
        signal_filter = st.sidebar.multiselect(
            "Signal Type", options=["Buy", "Sell", "Hold"], default=["Buy", "Sell", "Hold"])
        date_range = st.sidebar.date_input("Date Range", [])

        filtered = df[df["Asset"].isin(
            asset_filter) & df["Signal"].isin(signal_filter)]

        if len(date_range) == 2:
            filtered = filtered[
                (df["Date"] >= pd.to_datetime(date_range[0])) &
                (df["Date"] <= pd.to_datetime(date_range[1]))
            ]

        st.subheader("📄 Filtered Signal Results")
        st.dataframe(filtered.sort_values("Date", ascending=False))

        # === METRICS ===
        st.divider()
        st.subheader("📊 Summary Metrics")

        total = len(filtered)
        buy_pct = round((filtered["Signal"] == "Buy").mean() * 100, 2)
        sell_pct = round((filtered["Signal"] == "Sell").mean() * 100, 2)
        hold_pct = round((filtered["Signal"] == "Hold").mean() * 100, 2)

        st.metric("Total Signals", total)
        col1, col2, col3 = st.columns(3)
        col1.metric("Buy %", f"{buy_pct}%")
        col2.metric("Sell %", f"{sell_pct}%")
        col3.metric("Hold %", f"{hold_pct}%")

        # === OPTIONAL: Load Backtest Results from Cached File ===
        backtest_path = os.path.join("logs", "backtest_results.csv")
        if os.path.exists(backtest_path):
            st.subheader("📈 Backtest Results (Imported)")
            bt_df = pd.read_csv(backtest_path)
            st.dataframe(bt_df)
            acc = round(bt_df["Correct"].value_counts(
                normalize=True).get("✅", 0) * 100, 2)
            avg_ret = round(bt_df["Return (%)"].mean(), 2)
            st.metric("Accuracy", f"{acc}%")
            st.metric("Avg Return", f"{avg_ret}%")

            st.line_chart(bt_df["Return (%)"])

        st.download_button("📥 Export Filtered Signals", filtered.to_csv(
            index=False), "filtered_signals.csv")
