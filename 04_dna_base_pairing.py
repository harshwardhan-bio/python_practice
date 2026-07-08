"""
DNA Base Pairing System
Practices: match/case (structural pattern matching), string methods
"""

Pair = input("Enter a DNA base (A, T, C, G): ").upper()

match Pair:
    case "A":
        print("Adenine pairs with Thymine (T).")
    case "T":
        print("Thymine pairs with Adenine (A).")
    case "C":
        print("Cytosine pairs with Guanine (G).")
    case "G":
        print("Guanine pairs with Cytosine (C).")
    case _:
        print("Invalid DNA base! Please enter a valid DNA base (A, T, C, G).")
