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

def find_subsequence_indices(s, t):
    """Finds the indices of t as a subsequence in s."""
    indices = []
    start = 0  # Start position in s
    
    for char in t:
        # Find the next occurrence of char in s starting from 'start'
        pos = s.find(char, start)
        if pos == -1:
            raise ValueError("Subsequence not found")
        indices.append(pos + 1)  # Convert 0-based index to 1-based
        start = pos + 1  # Move to the next position in s
    
    return indices

# Main code
input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_sseq.txt"
sequences = parse_fasta(input_file)

s = sequences[0]  # First sequence (s)
t = sequences[1]  # Second sequence (t)

result = find_subsequence_indices(s, t)
print(" ".join(map(str, result)))
