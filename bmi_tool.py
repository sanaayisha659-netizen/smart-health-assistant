def calculate_bmi(weight, height):
    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return round(bmi, 2), status
