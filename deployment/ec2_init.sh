sudo apt update -y
sudo apt install python3-pip -y
pip3 install -r deployment/requirements.txt
nohup python3 deployment/main.py > logs/runtime.log 2>&1 &