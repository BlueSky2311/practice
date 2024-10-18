def count_rna_strings(protein_string):
    # The RNA codon table mapping amino acids to their possible codons
    codon_table = {
        'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4, 'S': 6, 'P': 4, 'T': 4, 'A': 4,
        'Y': 2, '*': 3, 'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2, 'E': 2, 'C': 2,
        'W': 1, 'R': 6, 'G': 4
    }

    MOD = 1000000
    total_rna_strings = 1

    # Calculate the total number of possible RNA strings modulo MOD
    for amino_acid in protein_string:
        total_rna_strings *= codon_table[amino_acid]
        total_rna_strings %= MOD

    # Consider the stop codon
    total_rna_strings *= codon_table['*']
    total_rna_strings %= MOD

    return total_rna_strings

if __name__ == "__main__":
    # Read the protein string from an input file
    with open(r"C:\Users\Blue\Downloads\Documents\rosalind_mrna.txt", "r") as file:
        protein_string = file.readline().strip()
    
    result = count_rna_strings(protein_string)
    print(result)
