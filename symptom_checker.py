from health_data import SYMPTOMS

def analyze_symptom(symptom):
    symptom = symptom.lower()
    return SYMPTOMS.get(
        symptom,
        "Symptom not found. Please consult a doctor."
    )
