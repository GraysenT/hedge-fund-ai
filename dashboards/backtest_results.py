import pandas as pd
import plotly.express as px
import os
import streamlit as st

RESULTS_DIR = "backtesting/results"

st.set_page_config(page_title="📊 Backtest Results", layout="wide")
st.title("📊 Backtest Results Viewer")

# Load most recent performance file
perf_files = sorted([f for f in os.listdir(RESULTS_DIR) if f.startswith("backtest_perf")], reverse=True)
log_files = sorted([f for f in os.listdir(RESULTS_DIR) if f.startswith("backtest_log")], reverse=True)

if not perf_files or not log_files:
    st.warning("No backtest results found in backtesting/results.")
    st.stop()

perf_df = pd.read_csv(os.path.join(RESULTS_DIR, perf_files[0]))
log_df = pd.read_csv(os.path.join(RESULTS_DIR, log_files[0]))

# Sidebar filters
asset_filter = st.sidebar.selectbox("Select Asset", sorted(perf_df['asset'].unique()))

# Filtered performance
asset_perf = perf_df[perf_df['asset'] == asset_filter]
asset_log = log_df[log_df['asset'] == asset_filter].copy()

# Cumulative strategy return chart
asset_log['strategy_cum_return'] = (1 + asset_log['strategy_returns']).cumprod()
asset_log['market_cum_return'] = (1 + asset_log['returns']).cumprod()

fig = px.line(asset_log, x="timestamp", y=["strategy_cum_return", "market_cum_return"],
              labels={"value": "Cumulative Return", "timestamp": "Date"},
              title=f"Cumulative Returns – {asset_filter}")
fig.update_layout(legend_title_text="Strategy vs Market")

# Sharpe Ratio
st.subheader(f"📈 Performance Summary – {asset_filter}")
st.dataframe(asset_perf)
st.plotly_chart(fig, use_container_width=True)

# Trade Log
st.subheader("📄 Trade Log")
st.dataframe(asset_log[['timestamp', 'signal', 'position', 'price', 'returns', 'strategy_returns']])
