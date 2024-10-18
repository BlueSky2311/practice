def count_dna_nucleotides(dna_string):
    """
    Counts the number of 'A', 'C', 'G', and 'T' in the given DNA string.

    Parameters:
    dna_string (str): The DNA string to be analyzed.

    Returns:
    tuple: A tuple containing counts of 'A', 'C', 'G', and 'T' respectively.
    """
    count_A = dna_string.count('A')
    count_C = dna_string.count('C')
    count_G = dna_string.count('G')
    count_T = dna_string.count('T')
    return count_A, count_C, count_G, count_T

if __name__ == "__main__":
    import sys

    # Read the DNA string from standard input
    dna_input = sys.stdin.read().strip().upper()  # Convert to uppercase to handle lowercase inputs

    # Count the nucleotides
    counts = count_dna_nucleotides(dna_input)

    # Print the counts separated by spaces
    print(' '.join(map(str, counts)))
