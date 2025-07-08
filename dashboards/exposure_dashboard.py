import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📊 Exposure Monitor", layout="wide")
st.title("📊 Long/Short Exposure Dashboard")

SNAPSHOT_FILE = "snapshots/allocation_history.csv"

if not os.path.exists(SNAPSHOT_FILE):
    st.warning("No allocation history file found.")
else:
    df = pd.read_csv(SNAPSHOT_FILE)
    df["date"] = pd.to_datetime(df["date"])
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce")

    # Simulated directional tags (replace with live signals if connected)
    signal_map = {
        "US_Trend": "buy",
        "UK_Value": "buy",
        "Crypto_RSI": "sell"
    }

    df["direction"] = df["strategy"].map(signal_map).fillna("buy")
    df["signed_weight"] = df.apply(
        lambda row: -row["weight"] if row["direction"] == "sell" else row["weight"],
        axis=1
    )

    latest = df[df["date"] == df["date"].max()]

    long_exposure = latest[latest["signed_weight"] > 0]["signed_weight"].sum()
    short_exposure = -latest[latest["signed_weight"] < 0]["signed_weight"].sum()
    net_exposure = long_exposure - short_exposure
    gross_exposure = long_exposure + short_exposure

    # Exposure limits
    max_short = 0.4
    max_net = 1.0
    max_gross = 1.5

    st.markdown("### 🧠 Current Exposure Breakdown")
    col1, col2, col3 = st.columns(3)
    col1.metric("Long Exposure", f"{long_exposure:.2%}")
    col2.metric("Short Exposure", f"{short_exposure:.2%}")
    col3.metric("Net Exposure", f"{net_exposure:.2%}")

    st.markdown("### ⚠️ Exposure Limit Checks")
    if short_exposure > max_short:
        st.error(f"🔴 Short exposure exceeds limit: {short_exposure:.2%} > {max_short:.2%}")
    else:
        st.success("✅ Short exposure within limit")

    if abs(net_exposure) > max_net:
        st.error(f"🔴 Net exposure exceeds limit: {net_exposure:.2%} > ±{max_net:.2%}")
    else:
        st.success("✅ Net exposure within limit")

    if gross_exposure > max_gross:
        st.error(f"🔴 Gross exposure exceeds limit: {gross_exposure:.2%} > {max_gross:.2%}")
    else:
        st.success("✅ Gross exposure within limit")

    st.markdown("### 📋 Strategy Weight Breakdown")
    st.dataframe(latest[["strategy", "signed_weight", "status"]].set_index("strategy").style.format({
        "signed_weight": "{:.2%}"
    }))
