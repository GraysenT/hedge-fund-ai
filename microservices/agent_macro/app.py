from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/propose", methods=["POST"])
def propose():
    gdp = request.get_json().get("gdp_growth", 0)
    decision = "bullish" if gdp > 2 else "cautious"
    return jsonify({"agent": "MacroAgent", "proposal": decision})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)