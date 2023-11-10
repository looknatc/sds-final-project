# frontend_application_service.py
from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


FRONTEND_MICROSERVICE_URL = "http://frontend-microservice:5004"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_data():
    # content_type = request.headers.get('Content-Type')
    # if content_type != 'application/json':
    #     return jsonify({'error': 'Unsupported Media Type'}), 415
    data = request.get_json()

    # Forward user input to the Frontend Microservice
    frontend_microservice_response = requests.post(
        f"{FRONTEND_MICROSERVICE_URL}/submit_data",
        json=data
    ).json()

    return jsonify(frontend_microservice_response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
