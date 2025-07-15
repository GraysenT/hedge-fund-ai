sudo apt update -y
sudo apt install -y python3-pip tmux git

# Clone your code
git clone https://github.com/yourname/hedge-fund-ai.git
cd hedge-fund-ai

# Install deps
pip3 install -r requirements.txt

# Run inside tmux
tmux new -d -s hedge "python3 main.py"