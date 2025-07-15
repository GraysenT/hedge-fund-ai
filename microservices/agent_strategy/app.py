from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/propose", methods=["POST"])
def propose():
    data = request.get_json()
    momentum = data.get("momentum", 0)
    decision = "buy" if momentum > 0 else "sell"
    return jsonify({"agent": "StrategyAgent", "proposal": decision})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)