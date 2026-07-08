"""
Genetic Mutation Scanner
Practices: functions, list comparison, indexing, mutation/repair logic
"""

def scan_mutation(ref, patient):
    if len(ref) != len(patient):
        print("Error: Sequences must be of the same length.")
        return None

    for i in range(len(ref)):
        if ref[i] != patient[i]:
            print(f"Mutation found at position {i}: Reference = {ref[i]}, Patient = {patient[i]}")
            patient[i] = ref[i]
            print(f"Patient sequence {i} corrected to match reference: {ref[i]}")
        else:
            print(f"No mutation at position {i}: Reference = {ref[i]}, Patient = {patient[i]}")

    print("\nFinal repaired patient sequence:", patient)


scan_mutation(["A", "T", "G", "C", "A"], ["A", "T", "A", "C", "G"])
