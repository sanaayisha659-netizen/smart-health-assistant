MEDICINES = {
    "paracetamol": "Used to reduce fever and relieve mild to moderate pain.",
    "ibuprofen": "Used for pain, fever, and inflammation.",
    "diclofenac": "Used for muscle pain, joint pain, and inflammation.",
    "aspirin": "Used for pain relief and to reduce fever (not for children).",

    "cetirizine": "Used to treat allergy symptoms like sneezing and itching.",
    "loratadine": "Used for allergic reactions and hay fever.",
    "chlorpheniramine": "Used to treat cold and allergy symptoms.",
    "diphenhydramine": "Used for allergy and cough relief.",
    "salbutamol": "Used to relieve asthma and breathing problems.",
    "montelukast": "Used to manage allergies and asthma.",

    "pantoprazole": "Used for acid reflux and stomach ulcers.",
    "omeprazole": "Used to reduce stomach acid.",
    "ranitidine": "Used for acidity and heartburn.",
    "domperidone": "Used to relieve nausea and vomiting.",
    "ondansetron": "Used to prevent vomiting and nausea.",
    "loperamide": "Used to treat diarrhea.",
    "ors": "Used to prevent or treat dehydration.",

    "amoxicillin": "An antibiotic used to treat bacterial infections.",
    "azithromycin": "Used to treat bacterial infections (doctor prescribed).",
    "ciprofloxacin": "Used for bacterial infections.",
    "doxycycline": "Used to treat infections and acne.",
  
    "metformin": "Used to control blood sugar levels in diabetes.",
    "glimepiride": "Used to manage type 2 diabetes.",
    "insulin": "Used to regulate blood sugar levels.",

    "amlodipine": "Used to manage high blood pressure.",
    "atenolol": "Used for blood pressure and heart conditions.",
    "losartan": "Used to treat high blood pressure.",
    "enalapril": "Used to manage hypertension and heart failure.",

    "vitamin c": "Supports immunity and treats vitamin C deficiency.",
    "vitamin d": "Supports bone health and immunity.",
    "vitamin b12": "Used to treat nerve problems and deficiency.",
    "iron tablet": "Used to treat iron deficiency anemia.",
    "calcium": "Used to strengthen bones and teeth.",

    "alprazolam": "Used for anxiety disorders (doctor prescribed).",
    "sertraline": "Used to treat depression and anxiety.",
    "diazepam": "Used for anxiety and muscle relaxation.",

    "calamine lotion": "Used to relieve itching and skin irritation.",
    "hydrocortisone cream": "Used for skin inflammation and allergies.",
    "clotrimazole": "Used to treat fungal infections.",

    "mefenamic acid": "Used to relieve menstrual pain.",
    "folic acid": "Used during pregnancy and to prevent anemia.",

    "antiseptic cream": "Used to prevent infection in minor cuts.",
    "iodine solution": "Used for wound cleaning.",
    "bandage": "Used to cover and protect wounds."
}
BASE_MEDICINES = {
    "paracetamol": ["dolo", "crocin", "calpol", "p 650", "dolokind"],
    "ibuprofen": ["brufen", "ibuflam", "ibu", "combiflam"],
    "cetirizine": ["cetzine", "zyrtec", "okacet", "allegra"],
    "pantoprazole": ["pantocid", "pan 40", "pantodac"],
    "omeprazole": ["omez", "omez d"],
    "metformin": ["glyciphage", "glycomet", "glycomet gp"],
    "amlodipine": ["amlodac", "amlong", "amlo"],
    "azithromycin": ["azee", "azithral", "azi"],
    "amoxicillin": ["amox", "novamox"],
    "vitamin d": ["vit d", "vit d3", "cholecalciferol"],
    "vitamin c": ["vit c", "limcee"],
    "vitamin b12": ["b12", "mecobalamin"],
}
MEDICINE_ALIASES = {}

for real_name, aliases in BASE_MEDICINES.items():
    real = real_name.lower()

    for alias in aliases:
        MEDICINE_ALIASES[alias.lower()] = real

    MEDICINE_ALIASES[real[:3]] = real
    MEDICINE_ALIASES[real[:4]] = real
    MEDICINE_ALIASES[real[:5]] = real

    MEDICINE_ALIASES[real.replace("a", "e")] = real
    MEDICINE_ALIASES[real.replace("e", "a")] = real
    MEDICINE_ALIASES[real.replace("amol", "emol")] = real
    MEDICINE_ALIASES[real.replace("emol", "amol")] = real
