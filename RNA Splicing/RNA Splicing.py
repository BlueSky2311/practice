import os

# Standard codon table
CODON_TABLE = {
    'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
}

def parse_fasta(file_content):
    fasta_entries = {}
    current_label = ""
    current_seq = []
    for line in file_content:
        line = line.strip()
        if line.startswith('>'):
            if current_label:
                fasta_entries[current_label] = ''.join(current_seq)
            current_label = line[1:]
            current_seq = []
        else:
            current_seq.append(line)
    if current_label:
        fasta_entries[current_label] = ''.join(current_seq)
    return fasta_entries

def remove_introns(s, introns):
    for intron in introns:
        s = s.replace(intron, '')
    return s

def transcribe(dna):
    return dna.replace('T', 'U')

def translate(rna):
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3:
            break
        amino_acid = CODON_TABLE.get(codon, '')
        if amino_acid == 'Stop' or amino_acid == '':
            break
        protein.append(amino_acid)
    return ''.join(protein)

def main():
    # Specify the input file path
    input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_splc.txt"
    
    # Read input file
    try:
        with open(input_file, 'r') as f:
            file_content = f.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return
    
    # Parse FASTA entries
    fasta_entries = parse_fasta(file_content)
    
    # Extract main DNA string (first entry)
    labels = list(fasta_entries.keys())
    if not labels:
        print("Error: No FASTA entries found in the input file.")
        return
    main_dna = fasta_entries[labels[0]]
    
    # Extract introns (rest of the entries)
    introns = [fasta_entries[label] for label in labels[1:]]
    
    # Remove introns from main DNA
    exon_dna = remove_introns(main_dna, introns)
    
    # Transcribe DNA to RNA
    rna = transcribe(exon_dna)
    
    # Translate RNA to protein
    protein = translate(rna)
    
    # Prepare output file path
    input_dir = os.path.dirname(input_file)
    output_file = os.path.join(input_dir, 'output.txt')
    
    # Write protein to output file
    try:
        with open(output_file, 'w') as f:
            f.write(protein)
        print(f"Protein string successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()
