# calculator_service.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/calculate_bmi", methods=["POST"])
def calculate_bmi():
    data = request.get_json()
    weight = data["weight"]
    height = data["height"]
    bmi = weight / (height ** 2)
    return jsonify({"bmi": bmi})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
