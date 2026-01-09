def bmi_guidance(bmi):
    if bmi < 18.5:
        return {
            "category": "Underweight",
            "reason": "Low calorie intake or fast metabolism",
            "tips": [
                "Eat nutritious food",
                "Increase protein intake",
                "Consult a doctor if needed"
            ]
        }

    elif bmi < 25:
        return {
            "category": "Normal",
            "reason": "Healthy body balance",
            "tips": [
                "Maintain current lifestyle",
                "Exercise regularly",
                "Stay hydrated"
            ]
        }

    else:
        return {
            "category": "Overweight",
            "reason": "Low activity or unhealthy diet",
            "tips": [
                "Walk daily",
                "Avoid junk food",
                "Reduce sugar intake"
            ]
        }
