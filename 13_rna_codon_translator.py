"""
RNA Codon Translator
Practices: dictionaries, functions, string methods
"""

def translate_codon(codon_input):
    codon_input = codon_input.upper()
    codon_table = {
        "AUG": "Methionine (Start Codon)",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
    }
    if codon_input in codon_table:
        return codon_table[codon_input]
    else:
        return "Invalid codon. Please enter a valid RNA codon (e.g., AUG, UUU, UUC)."


print(translate_codon("aug"))
print(translate_codon("UUU"))
print(translate_codon("GCA"))
