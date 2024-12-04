import math

def compute_log_probabilities(dna_string, gc_contents):
    """
    Compute the common logarithm of the probability that a random string constructed
    with the given GC-content matches the DNA string exactly.

    Parameters:
    dna_string (str): DNA string
    gc_contents (list): Array of GC-contents

    Returns:
    list: Array of log probabilities
    """
    log_probs = []
    for gc_content in gc_contents:
        # Probability of GC and AT pairs
        gc_prob = gc_content / 2
        at_prob = (1 - gc_content) / 2

        # Compute the log probability for the DNA string
        prob = 1.0
        for nucleotide in dna_string:
            if nucleotide in 'GgCc':
                prob *= gc_prob
            elif nucleotide in 'AaTt':
                prob *= at_prob

        # Compute the logarithm (base 10) of the probability
        log_prob = math.log10(prob)
        log_probs.append(log_prob)

    return log_probs

def read_input_file(file_path):
    """
    Read DNA string and GC-content array from a file.

    Parameters:
    file_path (str): Path to the input file

    Returns:
    tuple: DNA string and GC-content list
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        dna_string = lines[0].strip()  # First line is the DNA string
        gc_contents = list(map(float, lines[1].strip().split()))  # Second line is the GC-content list
    return dna_string, gc_contents

def main():
    # Path to the input file
    file_path = r"C:\Users\Blue\Downloads\Documents\rosalind_prob.txt"

    # Read input from the file
    dna_string, gc_contents = read_input_file(file_path)

    # Compute the log probabilities
    result = compute_log_probabilities(dna_string, gc_contents)

    # Print the result
    print(" ".join(f"{x:.3f}" for x in result))

if __name__ == "__main__":
    main()
