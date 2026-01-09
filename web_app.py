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
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

