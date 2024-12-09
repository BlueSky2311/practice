def parse_fasta(filename):
    """Parses a FASTA file and returns sequences as a list."""
    sequences = []
    with open(filename, 'r') as file:
        seq = ""
        for line in file:
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line.strip()
        if seq:
            sequences.append(seq)
    return sequences

def calculate_transition_transversion_ratio(s1, s2):
    """Calculates the transition/transversion ratio."""
    transitions = 0
    transversions = 0
    
    # Define purines and pyrimidines
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    
    for a, b in zip(s1, s2):
        if a != b:  # Only count mismatches
            if (a in purines and b in purines) or (a in pyrimidines and b in pyrimidines):
                transitions += 1
            else:
                transversions += 1
    
    # Calculate ratio
    if transversions == 0:
        return float('inf')  # Avoid division by zero
    return transitions / transversions

# Main code
input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_tran.txt"
sequences = parse_fasta(input_file)

s1 = sequences[0]
s2 = sequences[1]

# Compute the ratio
ratio = calculate_transition_transversion_ratio(s1, s2)
print(f"{ratio:.10f}")
