def read_fasta(filename):
    """Read sequences from a FASTA file."""
    sequences = []
    with open(filename, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:  # Save the previous sequence before starting a new one
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line  # Concatenate sequence lines
        if sequence:  # Add the last sequence
            sequences.append(sequence)
    return sequences

def is_common_substring(substring, sequences):
    """Check if a substring is common to all sequences."""
    return all(substring in sequence for sequence in sequences)

def find_longest_common_substring(sequences):
    """Find the longest common substring among the sequences."""
    first_sequence = sequences[0]
    longest_common_substring = ""
    
    # Try all possible substrings of the first sequence
    for i in range(len(first_sequence)):
        for j in range(i + 1, len(first_sequence) + 1):
            candidate = first_sequence[i:j]
            if len(candidate) > len(longest_common_substring) and is_common_substring(candidate, sequences):
                longest_common_substring = candidate
    
    return longest_common_substring

def main():
    filename = r"C:\Users\Blue\Desktop\rosalind\Finding a Shared Motif\rosalind_lcsm.txt"
    sequences = read_fasta(filename)
    longest_common_substring = find_longest_common_substring(sequences)
    print(longest_common_substring)

if __name__ == "__main__":
    main()
