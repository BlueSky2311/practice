from collections import Counter

def read_fasta_file(filename):
    """Function to parse the input FASTA file and return a list of sequences."""
    sequences = []
    seq = ''
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line.strip()
        if seq:
            sequences.append(seq)
    return sequences

def calculate_profile_matrix(sequences):
    """Function to calculate the profile matrix from a list of DNA sequences."""
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    seq_length = len(sequences[0])
    
    # Initialize profile matrix columns
    for base in profile.keys():
        profile[base] = [0] * seq_length
    
    for i in range(seq_length):
        column = [seq[i] for seq in sequences]
        counts = Counter(column)
        
        for base in profile.keys():
            profile[base][i] = counts.get(base, 0)
    
    return profile

def calculate_consensus_string(profile):
    """Function to generate the consensus string from the profile matrix."""
    consensus = ''
    seq_length = len(profile['A'])
    
    for i in range(seq_length):
        max_count = 0
        max_base = ''
        
        for base in 'ACGT':
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                max_base = base
        
        consensus += max_base
    
    return consensus

def export_to_txt(consensus, profile, output_file):
    """Function to export the consensus string and profile matrix to a text file."""
    with open(output_file, 'w') as file:
        # Write consensus string
        file.write(consensus + '\n')
        
        # Write profile matrix
        for base in 'ACGT':
            profile_line = f"{base}: {' '.join(map(str, profile[base]))}\n"
            file.write(profile_line)

# Main function
def main():
    # Replace with the path to your input .txt file and output .txt file
    input_file = r"C:\Users\Blue\Desktop\rosalind\Consensus and Profile_Finding a Most Likely Common Ancestor\rosalind_cons.txt"
    output_file = r"C:\Users\Blue\Desktop\rosalind\Consensus and Profile_Finding a Most Likely Common Ancestor\results.txt"
    
    # Read the sequences from the file
    sequences = read_fasta_file(input_file)

    # Calculate profile matrix
    profile_matrix = calculate_profile_matrix(sequences)

    # Calculate consensus string
    consensus_string = calculate_consensus_string(profile_matrix)

    # Export the consensus string and profile matrix to a .txt file
    export_to_txt(consensus_string, profile_matrix, output_file)

    print(f"Results have been exported to {output_file}")

if __name__ == '__main__':
    main()
