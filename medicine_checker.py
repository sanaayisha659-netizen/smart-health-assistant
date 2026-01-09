from medicine_data import MEDICINES

def analyze_medicine(name):
    name = name.lower().strip()

    if name in MEDICINES:
        return MEDICINES[name]

    for key in MEDICINES:
        if name in key or key in name:
            return MEDICINES[key]

    return "Medicine not found. Please consult a healthcare professional."
