#!/bin/bash

echo "🚀 Bootstrapping Hedge Fund AI environment..."

# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Create .env if not present
if [ ! -f .env ]; then
  echo "🔧 Copying .env.template to .env..."
  cp .env.template .env
else
  echo "✅ .env already exists"
fi

# 4. Prime logs and memory folders
mkdir -p logs memory reports
touch logs/trade_history.json logs/signal_events.json

# 5. Start evolution loop (optional)
echo "✅ Setup complete. You can now run:"
echo "   → source venv/bin/activate"
echo "   → python3 evolve.py"
echo "   → python3 runloop.py"