"""
The Lab Database
Practices: dictionaries, functions, filtering with conditions
"""

patient_database = {
    "P-101": "Healthy",
    "P-102": "Mutated",
    "P-103": "Healthy",
}


def filter_healthy(patient_list):
    cleared_patients = []
    for patient_id in patient_list:
        if patient_id in patient_database and patient_database[patient_id] == "Healthy":
            cleared_patients.append(patient_id)
    return cleared_patients


print(filter_healthy(["P-101", "P-999", "P-102", "P-103"]))
