"""
GC Content Analyzer
Practices: string methods, len(), count(), nested conditions
"""

DNA_sequence = input("Enter a DNA sequence: ").upper()
len1 = len(DNA_sequence)

if len1 == 0:
    print("The DNA sequence is empty. Please enter a valid DNA sequence.")
else:
    count_G = DNA_sequence.count("G")
    count_C = DNA_sequence.count("C")
    gc_content = ((count_G + count_C) / len1) * 100

    if gc_content > 60:
        print("High GC content:", gc_content, "%")
    elif 40 <= gc_content <= 60:
        print("Moderate GC content:", gc_content, "%")
    else:
        print("Low GC content:", gc_content, "%")
