def analyze_symptom(user_input):
    user_input = user_input.lower().strip()
    user_input = ALIASES.get(user_input, user_input)

    if user_input in SYMPTOMS:
        return SYMPTOMS[user_input]

    for key in SYMPTOMS:
        if user_input in key or key in user_input:
            return SYMPTOMS[key]

    return "Symptom not recognised. Please consult a doctor."
