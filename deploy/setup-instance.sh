```bash
#!/bin/bash
sudo apt update -y
sudo apt install -y python3-pip git tmux
git clone https://github.com/GraysenT/hedge-fund-ai.git
cd hedge-fund-ai
pip3 install -r requirements.txt
tmux new -d -s hedge "python3 main.py"