from medicine_data import MEDICINES, MEDICINE_ALIASES
from symptom_checker import analyze_symptom


def ai_brain(user_input):
    text = user_input.lower().strip()

    # BMI
    if "bmi" in text:
        return (
            "📊 BMI Information\n"
            "• BMI helps understand body weight health\n"
            "• Normal range: 18.5 – 24.9\n"
            "• Use the BMI calculator for accurate results"
        )

    # SYMPTOM CHECK
    symptom_result = analyze_symptom(text)
    if isinstance(symptom_result, list):
        reply = "🩺 AI Symptom Analysis:\n\n"
        for item in symptom_result:
            reply += f"🔹 Symptom: {item['symptom']}\n"
            reply += f"   Cause: {item['cause']}\n"
            reply += "   Remedies:\n"
            for r in item["remedies"]:
                reply += f"   - {r}\n"
            reply += f"   Doctor Advice: {item['doctor']}\n\n"
        return reply

    # MEDICINE CHECK
    for alias, real_name in MEDICINE_ALIASES.items():
        if alias in text:
            med = MEDICINES.get(real_name)
            if med:
                return (
                    f"💊 Medicine: {med['name']}\n"
                    f"Uses: {med['uses']}\n"
                    f"Dosage: {med['dosage']}\n"
                    f"Warning: {med['warning']}"
                )

    # WATER
    if "water" in text:
        return (
            "💧 Water Intake Tip\n"
            "• Drink 2–3 litres daily\n"
            "• Increase during heat or exercise"
        )

    # EXERCISE
    if "exercise" in text:
        return (
            "🏃 Exercise Tip\n"
            "• At least 30 minutes daily is recommended"
        )

    # DEFAULT RESPONSE
    return (
        "🤖 Smart Health AI Assistant\n"
        "I can help with:\n"
        "• Symptoms & remedies\n"
        "• Medicine information\n"
        "• BMI & health guidance\n"
        "• General health tips\n\n"
        "⚠️ This is not a medical diagnosis."
    )
