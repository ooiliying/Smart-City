import random
import json
from datetime import datetime, timedelta

# ----- Name Pools -----

# Malay names
malay_first_names = [
    "Ahmad", "Siti", "Mohd", "Aisyah", "Faiz", "Nurul", "Azlan", "Farah", "Hafiz", "Zahra",
    "Ismail", "Liyana", "Fadzil", "Salmah", "Razak", "Sharifah", "Halim", "Rosli", "Nadia", "Faizal"
]
malay_family_names = [
    "Abdullah", "Rahman", "Ismail", "Othman", "Aziz", "Hassan", "Salleh", "Mahmud", "Zainal", "Kamari"
]

# Chinese names
chinese_surnames = ["Tan", "Lim", "Lee", "Chong", "Goh", "Ng", "Wong", "Chan", "Teo", "Loh"]
chinese_given_names = ["Wei", "Li", "Xiao", "Jun", "Fang", "Hui", "Ming", "Yan", "Ling", "Jie", "Ting", "Qiang"]

# Indian names
indian_given_names = [
    "Raj", "Anil", "Priya", "Deepa", "Suresh", "Kumar", "Lakshmi", "Ravi", "Mani", "Arjun",
    "Kavitha", "Ramesh", "Sneha", "Vijay", "Divya"
]
indian_fathers_names = ["Singh", "Kumar", "Reddy", "Das", "Nair", "Patel", "Sharma", "Iyer", "Gupta", "Chandran"]

# ----- Pools for medical information -----

# Symptoms
symptoms_pool = [
    "Fever", "Fatigue", "Cough", "Headache", "Nausea", "Shortness of breath", "Chest pain",
    "Back pain", "Abdominal pain", "Joint pain", "Dizziness", "No symptoms"
]

# Chronic conditions
chronic_conditions_pool = ["Diabetes", "Hypertension", "Asthma", "Kidney Disease", "None"]

# Family medical conditions
family_conditions = ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "None"]

# Lab test templates (basic ones, can be expanded)
lab_tests = [
    {
        "testType": "Blood Test",
        "results": ["Hemoglobin: 13.8 g/dL, WBC: 6.0 x10^9/L", "Hemoglobin: 12.5 g/dL, WBC: 5.5 x10^9/L"],
        "remarks": ["Normal", "Slight anemia"]
    },
    {
        "testType": "Liver Function Test",
        "results": ["ALT: 25 U/L, AST: 20 U/L", "ALT: 40 U/L, AST: 35 U/L"],
        "remarks": ["Normal", "Mildly elevated"]
    }
]

# ----- Disease Progression -----

diseases_progression = {
    "Dengue": {
        1: ["Fever", "Fatigue"],
        2: ["Headache", "Nausea"],
        3: ["Rash", "Bleeding", "Joint pain"],
        4: ["Severe dehydration", "Severe fatigue", "Shock"]
    },
    "Stroke": {
        1: ["Sudden numbness", "Weakness", "Difficulty speaking"],
        2: ["Permanent neurological deficits", "Speech therapy"],
        3: ["Rehabilitation", "Physical therapy"]
    },
    "Tuberculosis": {
        1: ["Cough", "Fever", "Night sweats"],
        2: ["Severe coughing with blood", "Chest pain"],
        3: ["Difficulty breathing", "Organ damage"]
    }
}

chronic_diseases_progression = {
    "Hypertension": {
        1: ["Asymptomatic", "Headache"],
        2: ["Dizziness", "Chest pain"],
        3: ["Shortness of breath", "Heart failure"]
    },
    "Diabetes": {
        1: ["Increased thirst", "Frequent urination", "Fatigue"],
        2: ["Blurred vision", "Slow wound healing"],
        3: ["Numbness in extremities", "Kidney failure"]
    },
    "Asthma": {
        1: ["Shortness of breath", "Wheezing"],
        2: ["Coughing", "Wheezing", "Breathlessness"],
        3: ["Frequent respiratory infections", "Severe shortness of breath"]
    },
    "Heart Disease": {
        1: ["Chest pain", "Shortness of breath", "Fatigue"],
        2: ["Angina", "Frequent chest pain"],
        3: ["Heart attack", "Heart failure"]
    },
    "Cancer": {
        1: ["Unexplained weight loss", "Fatigue", "Pain"],
        2: ["Increased pain", "Metastasis", "Organ failure"],
        3: ["Chemotherapy", "Palliative care"]
    }
}

# ----- Helper Functions -----

def random_date(start_year=1940, end_year=2010):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def random_nric(dob):
    yy = dob.strftime("%y")
    mm = dob.strftime("%m")
    dd = dob.strftime("%d")
    place_code = random.randint(1, 20)
    serial = random.randint(1000, 9999)
    return f"{yy}{mm}{dd}-{place_code:02d}-{serial}"

def generate_malay_name():
    first = random.choice(malay_first_names)
    gender = random.choice(["male", "female"])
    middle = "bin" if gender == "male" else "binti"
    father = random.choice(malay_first_names)
    family = random.choice(malay_family_names)
    return f"{first} {middle} {father} {family}"

def generate_chinese_name():
    surname = random.choice(chinese_surnames)
    given = ''.join(random.choices(chinese_given_names, k=random.choice([1, 2])))
    return f"{surname} {given}"

def generate_indian_name():
    given = random.choice(indian_given_names)
    father = random.choice(indian_fathers_names)
    return f"{given} {father}"

def generate_address():
    street_num = random.randint(1, 150)
    street_names = ["Jalan Damai", "Jalan Bunga Raya", "Jalan Bukit Bintang", "Jalan Tun Razak", "Jalan Ampang"]
    city = random.choice(["Cyberjaya", "Putrajaya", "Kuala Lumpur", "Selangor"])
    return f"No. {street_num}, {random.choice(street_names)}, {city}, Malaysia"

def generate_family_history():
    return {
        "father": random.choice(family_conditions),
        "mother": random.choice(family_conditions),
        "siblings": random.choice(family_conditions)
    }

def generate_transfer_info():
    if random.random() < 0.3:
        transfer_date = datetime.today() - timedelta(days=random.randint(0, 365))
        return {
            "isTransferred": True,
            "fromHospital": random.choice(["Serdang Hospital", "HKL", "Putrajaya Hospital"]),
            "toHospital": "Cyberjaya Hospital",
            "transferDate": format_date(transfer_date),
            "reason": random.choice(["Specialist Care", "Surgery Follow-up", "Rehabilitation"]),
            "details": {
                "surgeryType": random.choice(["Appendectomy", "Heart Bypass", "None"]),
                "notes": "Transferred for follow-up care"
            }
        }
    else:
        return {
            "isTransferred": False,
            "fromHospital": None,
            "toHospital": None,
            "transferDate": None,
            "reason": None,
            "details": None
        }

def generate_chronic_conditions():
    conds = random.sample(chronic_conditions_pool, k=random.randint(0, 2))
    return [c for c in conds if c != "None"]

# ----- Disease Progression Generator -----

def generate_disease_progression(patient, disease_type):
    progression = diseases_progression.get(disease_type) or chronic_diseases_progression.get(disease_type)
    if not progression:
        return patient

    num_visits = random.randint(1, len(progression))
    for visit in range(1, num_visits + 1):
        symptoms = progression[visit]
        patient['historicalLabReports'].append({
            "testType": f"{disease_type} Diagnosis",
            "testResult": "Positive",
            "reportDate": format_date(datetime.today() - timedelta(days=(num_visits - visit) * 30)),
            "remarks": f"Stage {visit} of {disease_type}",
            "symptoms": symptoms
        })

    return patient

# ----- Patient Generator -----

def generate_patients_with_diseases(malay, chinese, indian):
    patients = []

    def create_patient(name_fn):
        dob = random_date()
        patient = {
            "nric": random_nric(dob),
            "name": name_fn(),
            "dob": format_date(dob),
            "address": generate_address(),
            "historicalLabReports": [],
            "familyMedicalHistory": generate_family_history(),
            "transferInfo": generate_transfer_info(),
            "chronicConditions": generate_chronic_conditions(),
            "previousSymptoms": []
        }

        disease = random.choice(list(diseases_progression.keys()) + list(chronic_diseases_progression.keys()))
        return generate_disease_progression(patient, disease)

    for _ in range(malay):
        patients.append(create_patient(generate_malay_name))
    for _ in range(chinese):
        patients.append(create_patient(generate_chinese_name))
    for _ in range(indian):
        patients.append(create_patient(generate_indian_name))

    random.shuffle(patients)
    return patients

# ----- Run & Output -----

if __name__ == "__main__":
    patients = generate_patients_with_diseases(200, 100, 100)  # Generate 400 sample patients
    print(json.dumps(patients, indent=2))
