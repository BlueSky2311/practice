# RNA codon table mapping
CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def translate_rna_to_protein(rna):
    protein = []
    
    # Traverse the RNA string in steps of 3 (codon size)
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            if amino_acid == "Stop":
                break  # Stop translation at a stop codon
            protein.append(amino_acid)
    
    return ''.join(protein)

# Read the RNA string from a file
with open(r"C:\Users\Blue\Desktop\rosalind\Translating RNA into Protein\rosalind_prot.txt", 'r') as file:
    rna_string = file.readline().strip()  # Read and strip any newlines or spaces

# Translate the RNA to a protein string
protein_string = translate_rna_to_protein(rna_string)

# Print the resulting protein string
print(protein_string)
