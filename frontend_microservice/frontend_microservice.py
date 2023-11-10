# frontend_microservice.py
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

CALCULATION_BMI_SERVICE_URL = "http://calculator-service:5001"
CLASSIFICATION_SERVICE_URL = "http://classification-service:5002"
RISK_SERVICE_URL = "http://risk-service:5003"

@app.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.get_json()

    # Forward user input to the Calculation BMI Service
    bmi_result = requests.post(
        f"{CALCULATION_BMI_SERVICE_URL}/calculate_bmi",
        json=data
    ).json()

    # Forward BMI result to the Classification Service
    classification_result = requests.post(
        f"{CLASSIFICATION_SERVICE_URL}/classify_bmi",
        json={"bmi": bmi_result['bmi']}
    ).json()

    # Forward classification to the Risk Service
    risk_assessment = requests.post(
        f"{RISK_SERVICE_URL}/assess_risk",
        json={"classification": classification_result['classification']}
    ).json()

    # Combine results and respond to the Frontend Application Service
    final_result = {
        'bmi_result': bmi_result,
        'classification_result': classification_result,
        'risk_assessment': risk_assessment
    }

    return jsonify(final_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
