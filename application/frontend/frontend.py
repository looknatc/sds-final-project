# import flask

# app = flask.Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if flask.request.method == "POST":
#         weight = float(flask.request.form.get("weight"))
#         height = float(flask.request.form.get("height"))

#         result = calculate_bmi(weight, height)
#         return flask.jsonify({
#             "bmi": result
#         })

#     else:
#         return flask.render_template("index.html")

# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
# @app.route("/")
# def home():
#     return "Hello, Flask!"

# frontend_service.py
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

app.template_folder = "templates"  # Change "templates" to your folder name if it's different


@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     weight = float(request.form["weight"])
    #     height = float(request.form["height"])
    #     # You can make a request to the Calculator Service here
    #     # bmi = make_request_to_calculator_service(weight, height)
    #     return f"Weight: {weight}, Height: {height}, BMI: {bmi}"
    return render_template("index.html")

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    return receive_data_to("http://calculation-service:5001/calculate_bmi")
    # receive_data_to("http://localhost:5001/calculate_bmi")
@app.route('/calculate_bmi', methods=['GET'])
def calculate_bmi2():
    # Access query parameters using request.args
    weight = float(request.args.get('weight', 0))
    height = float(request.args.get('height', 0))
    data = {"weight":weight,"height":height}
    response = requests.post("http://calculation-service:5001/calculate_bmi", json=data)
    if response.status_code == 200:
        return response.text
    else:
        return jsonify({'status': 'error', 'message': 'Failed to forward data'})

@app.route('/classify_bmi', methods=['GET'])
def classify_bmi():
    # Access query parameters using request.args
    bmi = float(request.args.get('bmi', 0))
    data = {"bmi":bmi}
    response = requests.post("http://classification-service:5002/classify_bmi", json=data)
    if response.status_code == 200:
        return response.text
    else:
        return jsonify({'status': 'error', 'message': 'Failed to forward data'})
    
@app.route('/assess_risk', methods=['GET'])
def assess_risk():
    # Access query parameters using request.args
    classification = request.args.get('classification', 0)
    data = {"classification":classification}
    response = requests.post("http://risk-service:5003/assess_risk", json=data)
    if response.status_code == 200:
        return response.text
    else:
        return jsonify({'status': 'error', 'message': 'Failed to forward data'})
# @app.route('/calculate_bmi', methods=['POST'])
# def calculate_bmi():
#     receive_data_to("http://calculation-service:5001/calculate_bmi")

# @app.route('/calculate_bmi', methods=['POST'])
# def calculate_bmi():
#     receive_data_to("http://calculation-service:5001/calculate_bmi")

# @app.route('/receive_data', methods=['POST'])
def receive_data_to(target_url):
    # Get data from the incoming POST request
    data = request.get_json()

    # Do any processing with the data if needed

    # Forward the data to another URL
    # target_url = 'http://example.com/destination'
    response = requests.post(target_url, json=data)

    # Check the response from the destination URL
    if response.status_code == 200:
        return response.text
    else:
        return jsonify({'status': 'error', 'message': 'Failed to forward data'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

