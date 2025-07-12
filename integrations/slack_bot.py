import os
from slack_bolt import App

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

app = App(token=SLACK_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

@app.command("/mute")
def mute_command(ack, command):
    ack()
    strategy = command["text"].strip()
    os.system(f"python3 cli/command_router.py {strategy} --boost 0.0")
    return f"✅ {strategy} muted."

@app.command("/boost")
def boost_command(ack, command):
    ack()
    args = command["text"].strip().split()
    strategy, boost = args[0], float(args[1])
    os.system(f"python3 cli/command_router.py {strategy} --boost {boost}")
    return f"✅ {strategy} boosted to {boost}"

if __name__ == "__main__":
    app.start(port=3000)