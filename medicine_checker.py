from health_data import MEDICINES

def analyze_medicine(name):
    name = name.lower().strip()
    return MEDICINES.get(
        name,
        "Medicine not found. Please consult a healthcare professional."
    )
