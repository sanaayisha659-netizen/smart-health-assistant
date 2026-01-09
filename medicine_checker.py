from medicine_data import MEDICINES, MEDICINE_ALIASES

def analyze_medicine(name):
    name = name.lower().strip()

    if name in MEDICINES:
        return MEDICINES[name]

    if name in MEDICINE_ALIASES:
        real_name = MEDICINE_ALIASES[name]
        return MEDICINES.get(real_name)

    for key in MEDICINE_ALIASES:
        if key in name or name in key:
            real_name = MEDICINE_ALIASES[key]
            return MEDICINES.get(real_name)

    return "Medicine not found. Please consult a healthcare professional."
