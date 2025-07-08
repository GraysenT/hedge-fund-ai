echo "🔁 Starting Self-Healing Agent + FastAPI Control + Cron..."

# Start cron (for snapshots, reporting, etc)
cron

# Start FastAPI control server (optional)
uvicorn api.control_api:app --host 0.0.0.0 --port 8080 &

# Start self-healing agent loop
python3 ai/self_healing_agent.py