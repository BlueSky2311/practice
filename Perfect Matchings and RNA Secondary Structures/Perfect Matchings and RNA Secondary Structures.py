from math import factorial

def perfect_matchings(rna_sequence):
    """
    Calculate the total number of perfect matchings of basepair edges
    in the bonding graph of the RNA sequence.
    """
    # Count occurrences of 'A', 'U', 'C', 'G'
    a_count = rna_sequence.count('A')
    u_count = rna_sequence.count('U')
    c_count = rna_sequence.count('C')
    g_count = rna_sequence.count('G')

    # Ensure the sequence has equal numbers of 'A'-'U' and 'C'-'G'
    if a_count != u_count or c_count != g_count:
        return 0

    # Calculate factorial(a_count) * factorial(c_count) for perfect matchings
    return factorial(a_count) * factorial(c_count)

# Read RNA sequence from a file
def read_rna_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Concatenate lines after the first (which contains the identifier)
        rna_sequence = ''.join(line.strip() for line in lines[1:])
    return rna_sequence

# Path to the input file
file_path = r"C:\Users\Blue\Downloads\Documents\rosalind_pmch.txt"

# Read RNA sequence and compute result
rna_sequence = read_rna_from_file(file_path)
result = perfect_matchings(rna_sequence)

print(result)  # Output the total number of perfect matchings