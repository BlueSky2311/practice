import os
import requests
import re

def fetch_fasta(uniprot_id):
    """
    Fetch the FASTA sequence for a given UniProt ID.
    Returns the sequence as a single string, or None if not found.
    """
    url = f"https://rest.uniprot.org/unisave/{uniprot_id}?format=fasta"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fasta = response.text
            # Parse FASTA: skip header, concatenate sequence lines
            lines = fasta.strip().split('\n')
            sequence = ''.join(lines[1:])  # Skip the first line (header)
            return sequence
        else:
            print(f"Warning: Unable to fetch {uniprot_id}. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {uniprot_id}: {e}")
        return None

def find_motif_positions(sequence):
    """
    Find all starting positions (1-based) of the N-glycosylation motif in the sequence.
    Motif pattern: N{P}[ST]{P} => N[^P][ST][^P]
    """
    pattern = re.compile(r'N[^P][ST][^P]')
    positions = [match.start() + 1 for match in pattern.finditer(sequence)]
    return positions

def main():
    # Specify the input file path
    input_file = r"C:\Users\Blue\Downloads\Documents\rosalind_mprt.txt"
    
    if not os.path.isfile(input_file):
        print(f"Error: File {input_file} does not exist.")
        return
    
    # Prepare output file path in the same directory
    input_dir = os.path.dirname(os.path.abspath(input_file))
    output_file = os.path.join(input_dir, "output.txt")
    
    # Read UniProt IDs
    with open(input_file, 'r') as f:
        uniprot_ids = [line.strip() for line in f if line.strip()]
    
    # Process IDs to handle the "*_" format
    processed_ids = [id.split('_')[0] if '_' in id else id for id in uniprot_ids]
    
    results = []
    
    for uniprot_id in processed_ids:
        print(f"Processing {uniprot_id}...")
        sequence = fetch_fasta(uniprot_id)
        if sequence:
            positions = find_motif_positions(sequence)
            if positions:
                results.append((uniprot_id, positions))
            else:
                print(f"No motifs found in {uniprot_id}.")
        else:
            print(f"Skipping {uniprot_id} due to fetch issues.")
    
    # Write results to output file
    with open(output_file, 'w') as f:
        for uniprot_id, positions in results:
            f.write(f"{uniprot_id}\n")
            positions_str = ' '.join(map(str, positions))
            f.write(f"{positions_str}\n")
    
    print(f"Results written to {output_file}.")

if __name__ == "__main__":
    main()
