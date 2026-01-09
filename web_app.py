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
@app.route("/bp", methods=["GET", "POST"])
def bp():
    result = None

    if request.method == "POST":
        systolic = int(request.form["systolic"])
        diastolic = int(request.form["diastolic"])

        if systolic < 90 or diastolic < 60:
            status = "Low Blood Pressure"
            advice = "Drink fluids, avoid sudden standing, consult doctor if frequent."
        elif systolic <= 120 and diastolic <= 80:
            status = "Normal Blood Pressure"
            advice = "Maintain healthy diet and regular exercise."
        elif systolic <= 139 or diastolic <= 89:
            status = "Pre-High Blood Pressure"
            advice = "Reduce salt, manage stress, monitor regularly."
        else:
            status = "High Blood Pressure"
            advice = "Consult a doctor, reduce salt, exercise regularly."

        result = {
            "status": status,
            "advice": advice
        }

    return render_template("bp.html", result=result)

@app.route("/symptom", methods=["GET", "POST"])
def symptom():
    result = None
    if request.method == "POST":
        symptom = request.form["symptom"]
        result = analyze_symptom(symptom)
    return render_template("symptom.html", result=result)
from datetime import datetime, timedelta

@app.route("/cycle", methods=["GET", "POST"])
def cycle():
    result = None

    if request.method == "POST":
        last_period = request.form["last_period"]
        cycle_length = int(request.form["cycle_length"])

        last_date = datetime.strptime(last_period, "%Y-%m-%d")
        next_period = last_date + timedelta(days=cycle_length)
        ovulation = next_period - timedelta(days=14)
        fertile_start = ovulation - timedelta(days=5)
        fertile_end = ovulation + timedelta(days=1)

        result = {
            "next_period": next_period.strftime("%d %B %Y"),
            "ovulation": ovulation.strftime("%d %B %Y"),
            "fertile": f"{fertile_start.strftime('%d %B')} - {fertile_end.strftime('%d %B %Y')}"
        }

    return render_template("cycle.html", result=result)
@app.route("/diabetes", methods=["GET", "POST"])
def diabetes():
    result = None

    if request.method == "POST":
        sugar = int(request.form["sugar"])

        if sugar < 70:
            status = "Low Blood Sugar (Hypoglycemia)"
            advice = "Eat immediately. Consult a doctor if frequent."
        elif sugar <= 99:
            status = "Normal"
            advice = "Maintain healthy diet and exercise."
        elif sugar <= 125:
            status = "Prediabetes"
            advice = "Reduce sugar intake, exercise regularly."
        else:
            status = "Diabetes"
            advice = "Consult a doctor. Follow medical advice strictly."

        result = {
            "status": status,
            "advice": advice
        }

    return render_template("diabetes.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)



