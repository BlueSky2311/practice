def read_fasta(file_path):
    """Reads a FASTA file and returns a list of sequences."""
    sequences = []
    with open(file_path, 'r') as file:
        current_seq = []
        for line in file:
            if line.startswith('>'):
                if current_seq:
                    sequences.append(''.join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line.strip())
        if current_seq:
            sequences.append(''.join(current_seq))
    return sequences

def find_overlap(a, b, min_length=1):
    """Find the maximum overlap between strings a and b."""
    max_overlap = 0
    for start in range(len(a)):
        # Find overlap of b starting at some point in a
        if a[start:] == b[:len(a) - start]:
            max_overlap = len(a) - start
            break
    return max_overlap

def merge_sequences(sequences):
    """Construct the shortest superstring containing all sequences."""
    while len(sequences) > 1:
        max_overlap = -1
        best_pair = None
        best_merged = None

        # Find the pair of sequences with the maximum overlap
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i != j:
                    overlap = find_overlap(sequences[i], sequences[j], min_length=1)
                    if overlap > max_overlap:
                        max_overlap = overlap
                        best_pair = (i, j)
                        best_merged = sequences[i] + sequences[j][overlap:]

        # Ensure a valid pair was found
        if best_pair is None:
            raise ValueError("No valid overlaps found; input data might be incomplete or invalid.")

        # Replace the best pair with the merged sequence
        i, j = best_pair
        sequences[i] = best_merged
        sequences.pop(j)

    return sequences[0]

# Input file path (update with the actual path to your FASTA file)
input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_long.txt"

# Read sequences from the input file
sequences = read_fasta(input_file)

# Solve for the shortest superstring
try:
    shortest_superstring = merge_sequences(sequences)
    print(shortest_superstring)

    # Optionally, save the result to an output file
    with open("output.txt", "w") as output_file:
        output_file.write(shortest_superstring + "\n")

except ValueError as e:
    print(f"Error: {e}")
