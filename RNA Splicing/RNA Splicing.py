import os

# RNA codon table for translation
CODON_TABLE = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S',
    'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
    'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R',
    'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T',
    'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S',
    'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

# Function to translate RNA to protein using the codon table
def translate_rna_to_protein(rna):
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acid = CODON_TABLE.get(codon, 'Stop')
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    return ''.join(protein)

# Function to remove introns from the DNA sequence
def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna

# Function to transcribe DNA to RNA (replace T with U)
def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')

# Read input from the .txt file
input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_splc.txt"  # Replace with your actual input file path

# Extract the directory path of the input file
input_directory = os.path.dirname(input_file)

# Read the input data
with open(input_file, 'r') as file:
    data = file.read().strip().splitlines()

# Debugging step: print the raw input data
print("Raw input data:", data)

# The first line is the main DNA sequence (s), and the following lines are introns
dna_sequence = data[0]  # The main DNA string
introns = data[1:]  # The introns to remove

# Debugging step: print the DNA sequence and introns
print("DNA sequence before intron removal:", dna_sequence)
print("Introns:", introns)

# Remove introns from the DNA sequence
exon_sequence = remove_introns(dna_sequence, introns)

# Debugging step: print the exon sequence after intron removal
print("Exon sequence after intron removal:", exon_sequence)

# Transcribe the remaining DNA to RNA
rna_sequence = transcribe_dna_to_rna(exon_sequence)

# Debugging step: print the transcribed RNA sequence
print("RNA sequence:", rna_sequence)

# Translate the RNA sequence to a protein string
protein_string = translate_rna_to_protein(rna_sequence)

# Debugging step: print the protein string
print("Protein string:", protein_string)

# Set the output file path in the same directory as the input file
output_file = os.path.join(input_directory, "output_protein.txt")

# Write the result to the output file
with open(output_file, 'w') as file:
    file.write(protein_string)

print(f"The protein string has been written to {output_file}")
