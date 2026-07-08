"""
The Full Sequence Translator
Practices: dictionaries, loops with step size, list building
"""

def translate_sequence(rna_sequence):
    rna_sequence = rna_sequence.upper()
    codon_table = {
        "AUG": "Methionine (Start Codon)",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UAG": "Stop Codon",
    }
    protein_chain = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        if codon in codon_table:
            protein_chain.append(codon_table[codon])
        else:
            protein_chain.append("Invalid codon")
    return protein_chain


print(translate_sequence("AUGUUUUUCAUG"))
