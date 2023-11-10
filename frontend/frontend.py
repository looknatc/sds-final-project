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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

