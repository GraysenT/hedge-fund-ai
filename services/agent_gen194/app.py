
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/propose", methods=["POST"])
def propose():
    data = request.get_json()
    score = hash(str(data)) % 100
    decision = "buy" if score % 2 == 0 else "sell"
    return jsonify({"agent": "Gen194", "proposal": decision})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5319)
