# risk_service.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def assess_risk(classification):
    if classification == "Underweight":
        return "Potential nutritional deficiency. Consult a healthcare professional."
    elif classification == "Overweight":
        return "Higher risk of heart disease and diabetes. Consider a healthier lifestyle."
    elif classification == "Obesity":
        return "Significant health risks. Seek medical advice and adopt a healthier lifestyle."
    else:
        return "Your BMI is in a healthy range. Keep up the good work!"

@app.route("/assess_risk", methods=["POST"])
def assess_risk_endpoint():
    data = request.get_json()
    classification = data["classification"]
    risk_assessment = assess_risk(classification)
    return jsonify({"risk_assessment": risk_assessment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
