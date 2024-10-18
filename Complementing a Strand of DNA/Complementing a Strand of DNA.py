def reverse_complement(dna_sequence):
    # Dictionary to hold complement pairs
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the sequence and replace each nucleotide with its complement
    reverse_complement_seq = ''.join([complement[nucleotide] for nucleotide in reversed(dna_sequence)])
    
    return reverse_complement_seq

# Function to read input from a file and print the result
def process_file(input_file):
    # Read the DNA sequence from the input file
    with open(input_file, 'r') as file:
        dna_sequence = file.read().strip()
    
    # Get the reverse complement of the DNA sequence
    reverse_complement_seq = reverse_complement(dna_sequence)
    
    # Print the result to the console
    print(reverse_complement_seq)

# Sample usage
input_file = r'C:\Users\Blue\Desktop\rosalind\Complementing a Strand of DNA\rosalind_revc.txt'  # Input file with the DNA sequence
process_file(input_file)
