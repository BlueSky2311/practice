import os

# Function to generate the reverse complement of a DNA sequence
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

# Function to find all reverse palindromes of length between 4 and 12
def find_reverse_palindromes(dna):
    results = []
    dna_length = len(dna)
    
    # Iterate through each possible starting point
    for i in range(dna_length):
        # Try every length from 4 to 12
        for length in range(4, 13):
            if i + length <= dna_length:  # Ensure we don't go out of bounds
                substring = dna[i:i+length]
                # Check if the substring is a reverse palindrome
                if substring == reverse_complement(substring):
                    # Record the position (1-based) and the length
                    results.append((i + 1, length))
    
    return results

# Input: DNA sequence
dna_sequence = input("Enter the DNA sequence: ").strip()

# Set the output directory and file name in the code
output_directory = r" "  # Change this path as needed
output_file = os.path.join(output_directory, "reverse_palindromes_output.txt")

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Find reverse palindromes
palindromes = find_reverse_palindromes(dna_sequence)

# Write the results to a .txt file
with open(output_file, 'w') as f:
    for pos, length in palindromes:
        f.write(f"{pos} {length}\n")

print(f"The output has been written to {output_file}")
