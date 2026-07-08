"""
Reusable AT-Content Calculator
Practices: functions, return values, reusability
"""

def calculate_at_content(sequence):
    sequence = sequence.upper()
    if len(sequence) == 0:
        print("The DNA sequence is empty. Please enter a valid DNA sequence.")
        return None
    count_A = sequence.count("A")
    count_T = sequence.count("T")
    at_content = ((count_A + count_T) / len(sequence)) * 100
    return at_content


print("AT content of the sequence is:", calculate_at_content("ATATGC"), "%")
