# classification_service.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.route("/classify_bmi", methods=["POST"])
def classify_bmi_endpoint():
    data = request.get_json()
    bmi = data["bmi"]
    classification = classify_bmi(bmi)
    return jsonify({"classification": classification})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
