import os
import slack_sdk
from slack_sdk.web import WebClient
from flask import Flask, request, Response

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def events():
    data = request.form
    text = data.get("text", "").lower()
    user = data.get("user_name")

    if "alpha" in text:
        response = "Top strategies: gen_strat_r2 (+$121), agent_macro (+$88)"
    elif "leaderboard" in text:
        response = "Use: `python3 dashboards/agent_leaderboard.py`"
    elif "evolve" in text:
        subprocess.run(["python3", "evolve.py"])
        response = "🔁 Evolution triggered."
    else:
        response = "Available: `/fund alpha`, `/fund leaderboard`, `/fund evolve`"

    return Response(response, content_type="text/plain")

if __name__ == "__main__":
    app.run(port=5004)
    