import streamlit as st
from runloop import get_live_market_state, MultiAgentOrchestrator, StrategyAgent, RiskAgent, MacroAgent, SentimentAgent, NewsAgent, TechnicalAgent, CorrelationAgent, LiquidityAgent, MemoryRetrievalAgent, GPTReflectiveAgent

agents = [
    StrategyAgent("StratA"),
    RiskAgent("RiskControl"),
    MacroAgent("MacroAgent"),
    SentimentAgent("SentimentAgent"),
    NewsAgent("NewsAgent"),
    TechnicalAgent("TechnicalAgent"),
    CorrelationAgent("CorrelationAgent"),
    LiquidityAgent("LiquidityAgent"),
    MemoryRetrievalAgent("MemoryAgent"),
    GPTReflectiveAgent("MetaAgentGPT")
]

orchestrator = MultiAgentOrchestrator(agents)
st.title("🧠 Real-Time Agent Trading Dashboard")

for _ in range(10):
    market_state = get_live_market_state()
    decision, summary = orchestrator.run(market_state)
    st.subheader(f"📊 Market State")
    st.json(market_state)
    st.subheader(f"🗳 Agent Proposals")
    st.json(summary)
    st.success(f"💡 Final Decision: {decision}")
