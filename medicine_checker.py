from medicine_data import MEDICINES, MEDICINE_ALIASES

def analyze_medicine(name):
    name = name.lower().strip()

    if name in MEDICINES:
        return MEDICINES[name]

    if name in MEDICINE_ALIASES:
        real_name = MEDICINE_ALIASES[name]
        return MEDICINES.get(real_name)

    for alias, real_name in MEDICINE_ALIASES.items():
        if alias in name or name in alias:
            return MEDICINES.get(real_name)

            real_name = MEDICINE_ALIASES[key]
            return MEDICINES.get(real_name)

    return "Medicine not found. Please consult a healthcare professional."
