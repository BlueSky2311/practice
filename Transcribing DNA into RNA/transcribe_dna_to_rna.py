def transcribe_dna_to_rna(dna_string):
    """
    Transcribes a DNA string into its corresponding RNA string by replacing all 'T's with 'U's.

    Parameters:
    dna_string (str): The DNA string to be transcribed.

    Returns:
    str: The transcribed RNA string.
    """
    # Replace all occurrences of 'T' with 'U'
    rna_string = dna_string.replace('T', 'U')
    return rna_string

if __name__ == "__main__":
    import sys

    # Read the DNA string from standard input
    # This allows for input redirection or manual input
    dna_input = sys.stdin.read().strip().upper()  # Convert to uppercase to handle lowercase inputs

    # Transcribe DNA to RNA
    rna_output = transcribe_dna_to_rna(dna_input)

    # Print the RNA string
    print(rna_output)
