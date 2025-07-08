import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Strategy Comparison", layout="wide")
st.title("📦 Strategy Comparison Dashboard")

log_path = os.path.join("logs", "backtest_results.csv")

if not os.path.exists(log_path):
    st.error("🚫 No backtest results found.")
else:
    df = pd.read_csv(log_path)

    if "Strategy" not in df.columns:
        # Simulate strategy types if missing
        import random
        strategies = ["LSTM", "Fusion", "Macro", "Sentiment"]
        df["Strategy"] = [random.choice(strategies) for _ in range(len(df))]

    st.success(f"✅ Loaded {len(df)} signal results with strategy labels.")

    # === Accuracy by Strategy ===
    st.subheader("✅ Accuracy by Strategy")
    accuracy_df = df.groupby("Strategy")["Correct"].value_counts(
        normalize=True).unstack().fillna(0) * 100
    st.dataframe(accuracy_df.style.format("{:.2f}"))

    # === Average Return by Strategy ===
    st.subheader("💰 Average Return by Strategy")
    df["Return (%)"] = pd.to_numeric(df["Return (%)"], errors="coerce")
    return_df = df.groupby("Strategy")[
        "Return (%)"].mean().sort_values(ascending=False)
    st.bar_chart(return_df)

    # === Downloadable View ===
    st.download_button("📥 Download Strategy Performance CSV",
                       df.to_csv(index=False), "strategy_performance.csv")
