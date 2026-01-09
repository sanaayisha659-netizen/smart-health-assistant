from health_data import SYMPTOMS

ALIASES = {
    "head ache": "headache",
    "stomach ache": "stomach pain",
    "feverish": "fever",
    "cold": "runny nose",
    "bp": "high blood pressure"
}

def analyze_symptom(user_input):
    user_input = user_input.lower().strip()

    user_input = ALIASES.get(user_input, user_input)

    if user_input in SYMPTOMS:
        return SYMPTOMS[user_input]

    for key in SYMPTOMS:
        if key in user_input or user_input in key:
            return SYMPTOMS[key]

    return "Symptom not recognized. Please consult a doctor."
def analyze_symptom(user_input):
    user_input = user_input.lower().strip()
    user_input = ALIASES.get(user_input, user_input)

    if user_input in SYMPTOMS:
        return SYMPTOMS[user_input]

    for key in SYMPTOMS:
        if user_input in key or key in user_input:
            return SYMPTOMS[key]

    return "Symptom not recognised. Please consult a doctor."

