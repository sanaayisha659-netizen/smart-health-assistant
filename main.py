from bmi_tool import calculate_bmi
from symptom_checker import analyze_symptom
from disclaimer import show_disclaimer

show_disclaimer()

print("🩺 Smart Health Assistant")
print("1. BMI Calculator")
print("2. Symptom Checker")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi, status = calculate_bmi(weight, height)
    print("Your BMI:", bmi)
    print("Health Status:", status)

elif choice == "2":
    symptom = input("Enter your symptom: ")
    result = analyze_symptom(symptom)
    print("Possible reason:", result)

else:
    print("Invalid option")
