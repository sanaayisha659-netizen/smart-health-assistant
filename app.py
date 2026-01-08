from flask import Flask, render_template, request
from bmi_tool import calculate_bmi
from symptom_checker import analyze_symptom

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    result = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi_value, status = calculate_bmi(weight, height)
        result = f"BMI: {bmi_value} | Status: {status}"
    return render_template("bmi.html", result=result)

@app.route("/symptom", methods=["GET", "POST"])
def symptom():
    result = None
    if request.method == "POST":
        symptom = request.form["symptom"]
        result = analyze_symptom(symptom)
    return render_template("symptom.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
