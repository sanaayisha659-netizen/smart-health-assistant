from medicine_data import MEDICINES, MEDICINE_ALIASES
from symptom_checker import ai_symptom_analysis
from health_guidance import bmi_guidance


def ai_brain(user_input):
    text = user_input.lower()

    if "bmi" in text:
        return (
            "🤖 AI Assistant\n"
            "BMI helps understand body weight health.\n"
            "Normal BMI range is 18.5 – 24.9.\n"
            "Use the BMI calculator for accurate result."
        )

    symptom_result = ai_symptom_analysis(text)
    if symptom_result:
        reply = "🧠 AI Symptom Analysis:\n"
        for item in symptom_result:
            reply += f"\nSymptom: {item['symptom']}\n"
            reply += f"Possible Cause: {item['cause']}\n"
            reply += "Remedies:\n"
            for r in item["remedies"]:
                reply += f"- {r}\n"
            reply += f"Doctor Advice: {item['doctor']}\n"
        return reply

    for alias, real_name in MEDICINE_ALIASES.items():
        if alias in text:
            med = MEDICINES.get(real_name)
            if med:
                return (
                    f"💊 Medicine: {real_name.capitalize()}\n"
                    f"📌 Uses: {med}\n"
                    f"⚠️ Always follow doctor advice."
                )

    if "water" in text:
        return (
            "💧 AI Health Tip\n"
            "Drink 2–3 litres of water daily.\n"
            "Increase intake during hot weather or exercise."
        )

    if "exercise" in text:
        return (
            "🏃 AI Health Tip\n"
            "At least 30 minutes of physical activity daily is recommended."
        )

    return (
        "🤖 Smart Health AI Assistant\n"
        "I can help with:\n"
        "- Symptoms & remedies\n"
        "- Medicine information\n"
        "- BMI & health guidance\n"
        "- General health tips\n"
        "⚠️ This is not a medical diagnosis."
    )
