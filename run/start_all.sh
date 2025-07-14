source venv/bin/activate
export PYTHONPATH=$(pwd)

# Launch GodLoop in background
nohup python3 simulation/god_loop.py > logs/godloop.log 2>&1 &

# Start API (if needed)
nohup uvicorn api.venture_portal:app --port 8081 > logs/api.log 2>&1 &

# Start Streamlit Dashboard
nohup streamlit run dashboard/economy_dashboard.py > logs/dashboard.log 2>&1 &