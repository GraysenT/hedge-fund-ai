from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

print("🚀 Orchestrator Flask server starting...")

AGENTS = {
    "strategy": "http://agent_strategy:5100/propose",
    "macro": "http://agent_macro:5101/propose"
}

@app.route("/run", methods=["POST"])
def run():
    print("🔥 /run endpoint was HIT")
    try:
        market_state = request.get_json()
        print("📈 Market state:", market_state)

        votes = {}
        for name, url in AGENTS.items():
            try:
                res = requests.post(url, json=market_state, timeout=5)
                res.raise_for_status()
                agent_response = res.json()
                votes[name] = agent_response.get("proposal", "error")
            except Exception as e:
                print(f"❌ Error from {name}: {e}")
                votes[name] = f"error: {str(e)}"

        print("🗳️ Final votes:", votes)
        return jsonify(votes), 200

    except Exception as e:
        print("❌ Exception in /run route:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("✅ Flask is booting")
    app.run(host="0.0.0.0", port=5000)