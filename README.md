# 🧠 Hedge Fund AI System

This is a fully autonomous, self-evolving hedge fund AI engine that runs:

- 📈 Real-time backtests and Sharpe tracking
- 🧬 Live strategy evolution and forking
- 🤖 Multi-agent trading execution
- 📊 Streamlit dashboard at port `8500`
- 🚀 FastAPI orchestrator at port `8000`

## Components
- `main.py`: Launches all modules in parallel threads
- `orchestrator/`: FastAPI routes, agent spawning
- `dashboard/`: Streamlit dashboard
- `evolution/`: Mutation and optimization engine
- `execution/`: Trading loop
- `forking/`: Agent auto-forking system
- `registry/`: Shared agent memory

## Deploy

To deploy on AWS EC2:

```bash
bash deploy/ec2-launch.sh