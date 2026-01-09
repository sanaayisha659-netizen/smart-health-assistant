def calculate_bmi(weight, height_in_cm):
    height_in_meters = height_in_cm/100
    bmi = weight/(height_in_meters**2)
    return round(bmi,2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return round(bmi, 2), status


