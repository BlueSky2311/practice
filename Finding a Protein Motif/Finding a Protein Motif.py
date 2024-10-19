import os
import urllib.request
import urllib.error
import re

def fetch_fasta_primary(uniprot_id):
    """
    Fetches the FASTA sequence using the primary URL: http://www.uniprot.org/uniprot/{uniprot_id}.fasta

    Parameters:
        uniprot_id (str): The UniProt access ID.

    Returns:
        str or None: The first protein sequence in uppercase without line breaks, or None if fetching fails.
    """
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    try:
        with urllib.request.urlopen(url) as response:
            fasta = response.read().decode('utf-8')
            sequence = extract_first_sequence(fasta)
            return sequence
    except urllib.error.HTTPError as e:
        # HTTPError indicates that the primary URL failed (e.g., 404 Not Found)
        # You can log the error or handle it as needed
        # For debugging, uncomment the following line:
        # print(f"Primary URL Error for {uniprot_id}: {e}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle other exceptions such as network issues
        # For debugging, uncomment the following line:
        # print(f"Primary URL Exception for {uniprot_id}: {e}", file=sys.stderr)
        return None

def fetch_fasta_fallback(uniprot_id):
    """
    Fetches the FASTA sequence using the fallback URL: https://rest.uniprot.org/unisave/{uniprot_id}?format=fasta

    Parameters:
        uniprot_id (str): The UniProt access ID.

    Returns:
        str or None: The first protein sequence in uppercase without line breaks, or None if fetching fails.
    """
    url = f"https://rest.uniprot.org/unisave/{uniprot_id}?format=fasta"
    try:
        with urllib.request.urlopen(url) as response:
            fasta = response.read().decode('utf-8')
            sequence = extract_first_sequence(fasta)
            return sequence
    except Exception as e:
        # Handle all exceptions (network issues, invalid ID, etc.)
        # For debugging, uncomment the following line:
        print(f"Fallback URL Error for {uniprot_id}: {e}", file=sys.stderr)
        return None

def extract_first_sequence(fasta):
    """
    Extracts the first protein sequence from a FASTA-formatted string.

    Parameters:
        fasta (str): The FASTA-formatted data.

    Returns:
        str or None: The first protein sequence in uppercase without line breaks, or None if no sequence is found.
    """
    # Split the FASTA into individual sequences based on the '>' delimiter
    sequences = fasta.strip().split('>')
    if len(sequences) < 2:
        return None  # No sequence found
    first_sequence = sequences[1]  # The first sequence after the initial '>'
    lines = first_sequence.strip().split('\n')
    if len(lines) < 2:
        return None  # No sequence lines found
    # Join all lines after the header and convert to uppercase
    sequence = ''.join(lines[1:]).upper()
    return sequence

def fetch_fasta(uniprot_id):
    """
    Attempts to fetch the FASTA sequence using the primary URL first.
    If it fails, attempts to use the fallback URL.

    Parameters:
        uniprot_id (str): The UniProt access ID.

    Returns:
        str or None: The first protein sequence in uppercase without line breaks, or None if fetching fails.
    """
    sequence = fetch_fasta_primary(uniprot_id)
    if sequence:
        return sequence
    else:
        # Attempt to fetch using the fallback URL
        return fetch_fasta_fallback(uniprot_id)

def find_motif(sequence):
    """
    Finds all starting positions of the N-glycosylation motif in the sequence.

    The motif N{P}[ST]{P} is represented by the regex pattern 'N[^P][ST][^P]'.

    Parameters:
        sequence (str): The protein sequence.

    Returns:
        list of int: 1-based starting positions where the motif is found.
    """
    # Define the regex pattern for the motif
    pattern = re.compile(r'N[^P][ST][^P]')
    # Find all non-overlapping matches and collect their starting positions
    positions = [match.start() + 1 for match in pattern.finditer(sequence)]
    return positions

def process_uniprot_ids(input_file_path, output_file_path):
    """
    Processes UniProt IDs to find N-glycosylation motifs and writes the results to an output file.

    Parameters:
        input_file_path (str): Path to the input file containing UniProt IDs.
        output_file_path (str): Path to the output file where results will be written.
    """
    # Read UniProt IDs from the input file, stripping any whitespace
    with open(input_file_path, 'r') as infile:
        original_ids = [line.strip() for line in infile if line.strip()]

    # Prepare a list of tuples: (original_id, query_id)
    id_pairs = []
    for original_id in original_ids:
        # If the ID contains '_', extract the part before the first '_'
        if '_' in original_id:
            query_id = original_id.split('_')[0]
        else:
            query_id = original_id
        id_pairs.append((original_id, query_id))

    # Open the output file for writing
    with open(output_file_path, 'w') as outfile:
        # Process each UniProt ID
        for original_id, query_id in id_pairs:
            sequence = fetch_fasta(query_id)
            if sequence:
                motif_positions = find_motif(sequence)
                if motif_positions:
                    outfile.write(f"{original_id}\n")
                    positions_str = ' '.join(map(str, motif_positions))
                    outfile.write(f"{positions_str}\n")

def main():
    """
    Main function to define input and output file paths and initiate processing.
    """
    # Define the input file path
    input_file_path = r"C:\Users\Blue\Downloads\Documents\rosalind_mprt.txt"

    # Validate that the input file exists
    if not os.path.isfile(input_file_path):
        print(f"Error: Input file '{input_file_path}' does not exist.")
        return

    # Derive the output file path by appending '_output.txt' to the input filename
    input_dir, input_filename = os.path.split(input_file_path)
    filename_without_ext, _ = os.path.splitext(input_filename)
    output_filename = f"{filename_without_ext}_output.txt"
    output_file_path = os.path.join(input_dir, output_filename)

    # Process the UniProt IDs and write the results
    process_uniprot_ids(input_file_path, output_file_path)

    print(f"Processing complete. Results saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
