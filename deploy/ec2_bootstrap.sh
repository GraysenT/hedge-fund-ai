#!/bin/bash
sudo apt update && sudo apt install -y python3-pip git screen
git clone https://github.com/GraysenT/hedge-fund-ai.git
cd hedge-fund-ai
pip3 install -r requirements.txt
screen -dmS mainloop python3 runloop.py
screen -dmS evolution python3 evolve.py
screen -dmS dashboard streamlit run dashboard/dashboard_app.py --server.port 8501
screen -dmS api uvicorn api.main:app --port 8000