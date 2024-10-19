import os

#Overview code function:
    #read_fasta(file_path): Reads the DNA sequence from the specified FASTA-formatted input file.
    #reverse_complement(dna): Generates the reverse complement of the provided DNA sequence.
    #translate(dna_seq): Translates a DNA sequence into a protein string until a stop codon is encountered.
    #find_orfs(dna): Searches for all distinct protein strings derived from ORFs across all six reading frames.
    #write_output(proteins, output_path): Writes the resulting protein strings to the specified output file, each on a new line.

# Define the standard genetic code mapping
genetic_code = {
    'TTT':'F', 'CTT':'L', 'ATT':'I', 'GTT':'V',
    'TTC':'F', 'CTC':'L', 'ATC':'I', 'GTC':'V',
    'TTA':'L', 'CTA':'L', 'ATA':'I', 'GTA':'V',
    'TTG':'L', 'CTG':'L', 'ATG':'M', 'GTG':'V',
    'TCT':'S', 'CCT':'P', 'ACT':'T', 'GCT':'A',
    'TCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'TCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'TCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
    'TAT':'Y', 'CAT':'H', 'AAT':'N', 'GAT':'D',
    'TAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'TAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'TAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'TGT':'C', 'CGT':'R', 'AGT':'S', 'GGT':'G',
    'TGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'TGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'TGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
}

def read_fasta(file_path):
    """
    Reads a FASTA formatted file and returns the concatenated DNA sequence.
    
    Parameters:
        file_path (str): Path to the FASTA file.
        
    Returns:
        str: Concatenated DNA sequence.
    """
    sequence = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                if line.startswith('>'):
                    continue  # Skip header lines
                sequence.append(line.upper())
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)
    return ''.join(sequence)

def reverse_complement(dna):
    """
    Returns the reverse complement of a DNA sequence.
    
    Parameters:
        dna (str): Original DNA sequence.
        
    Returns:
        str: Reverse complement of the DNA sequence.
    """
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    try:
        return ''.join(complement.get(base, base) for base in reversed(dna))
    except KeyError as e:
        print(f"Invalid nucleotide found in the DNA sequence: {e}")
        exit(1)

def translate(dna_seq):
    """
    Translates a DNA sequence into a protein string until a stop codon is encountered.
    
    Parameters:
        dna_seq (str): DNA sequence starting with a start codon.
        
    Returns:
        str: Translated protein string.
    """
    protein = []
    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i:i+3]
        if len(codon) < 3:
            break  # Incomplete codon at the end
        amino_acid = genetic_code.get(codon, '')
        if amino_acid == 'Stop':
            break  # Stop translation at stop codon
        if amino_acid:
            protein.append(amino_acid)
        else:
            break  # Invalid or unknown codon
    return ''.join(protein)

def find_orfs(dna):
    """
    Finds all distinct protein strings from ORFs in all six reading frames.
    
    Parameters:
        dna (str): Original DNA sequence.
        
    Returns:
        set: A set of unique protein strings.
    """
    proteins = set()
    sequences = [dna, reverse_complement(dna)]
    
    for seq in sequences:
        for frame in range(3):
            i = frame
            while i + 3 <= len(seq):
                codon = seq[i:i+3]
                if codon == 'ATG':  # Start codon
                    # Translate from this position
                    protein = []
                    j = i
                    while j + 3 <= len(seq):
                        current_codon = seq[j:j+3]
                        amino_acid = genetic_code.get(current_codon, '')
                        if amino_acid == 'Stop':
                            break  # Stop codon encountered
                        if not amino_acid:
                            break  # Invalid or unknown codon
                        protein.append(amino_acid)
                        j += 3
                    if protein:
                        proteins.add(''.join(protein))
                i += 3  # Move to the next codon in the current frame
    return proteins

def write_output(proteins, output_path):
    """
    Writes the protein strings to an output file, each on a separate line.
    
    Parameters:
        proteins (set): Set of unique protein strings.
        output_path (str): Path to the output text file.
    """
    try:
        with open(output_path, 'w') as file:
            for protein in proteins:
                file.write(protein + '\n')
        print(f"Successfully wrote the protein strings to {output_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        exit(1)

def main():
    # Define the input and output file paths
    input_path = r"C:\Users\Blue\Downloads\Documents\rosalind_orf.txt"
    
    # Derive the output file path by appending '_output.txt' to the input filename
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_output.txt"
    
    # Read the DNA sequence from the input file
    dna_sequence = read_fasta(input_path)
    
    # Find all distinct ORF-derived protein strings
    orf_proteins = find_orfs(dna_sequence)
    
    # Write the results to the output file
    write_output(orf_proteins, output_path)

if __name__ == "__main__":
    main()
