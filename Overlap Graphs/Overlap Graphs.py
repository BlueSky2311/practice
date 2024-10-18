def parse_fasta(file_content):
    """
    Parses a list of strings in FASTA format.

    Args:
        file_content (list of str): The FASTA formatted input.

    Returns:
        dict: A dictionary mapping labels to their corresponding DNA sequences.
    """
    sequences = {}
    label = None
    seq_lines = []

    for line in file_content:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if line.startswith('>'):
            if label:
                sequences[label] = ''.join(seq_lines)
            label = line[1:]  # Remove '>'
            seq_lines = []
        else:
            seq_lines.append(line)
    if label:
        sequences[label] = ''.join(seq_lines)
    
    return sequences

def build_overlap_graph(sequences, k=3):
    """
    Builds an overlap graph O_k for the given sequences.

    Args:
        sequences (dict): A dictionary mapping labels to DNA sequences.
        k (int): The length of the suffix and prefix to overlap.

    Returns:
        list of tuple: A list of tuples representing directed edges (source, target).
    """
    edges = []
    for source_label, source_seq in sequences.items():
        if len(source_seq) < k:
            continue  # Skip sequences shorter than k
        suffix = source_seq[-k:]
        for target_label, target_seq in sequences.items():
            if source_label == target_label:
                continue  # Prevent self-loop
            if len(target_seq) < k:
                continue  # Skip sequences shorter than k
            prefix = target_seq[:k]
            if suffix == prefix:
                edges.append((source_label, target_label))
    return edges

def main(input_file=r"C:\Users\Blue\Desktop\rosalind\Overlap Graphs\rosalind_grph.txt", output_file=r"C:\Users\Blue\Desktop\rosalind\Overlap Graphs\results", k=3):
    """
    Reads DNA sequences from an input file, constructs the overlap graph,
    and writes the adjacency list to an output file.

    Args:
        input_file (str): Path to the input file in FASTA format.
        output_file (str): Path to the output file for the adjacency list.
        k (int): The length of the suffix and prefix to overlap.
    """
    try:
        with open(input_file, 'r') as infile:
            fasta_input = infile.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading '{input_file}': {e}")
        return

    # Parse FASTA format
    sequences = parse_fasta(fasta_input)

    # Build the overlap graph O_k
    overlap_edges = build_overlap_graph(sequences, k)

    try:
        with open(output_file, 'w') as outfile:
            for edge in overlap_edges:
                outfile.write(f"{edge[0]} {edge[1]}\n")
    except Exception as e:
        print(f"An error occurred while writing to '{output_file}': {e}")
        return

    print(f"Overlap graph adjacency list has been written to '{output_file}'.")

if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Construct an overlap graph O3 from DNA sequences in FASTA format.")
    parser.add_argument('-i', '--input', type=str, default=r"C:\Users\Blue\Desktop\rosalind\Overlap Graphs\rosalind_grph.txt", help="Input file in FASTA format (default: input.txt)")
    parser.add_argument('-o', '--output', type=str, default=r"C:\Users\Blue\Desktop\rosalind\Overlap Graphs\results.txt", help="Output file for adjacency list (default: output.txt)")
    parser.add_argument('-k', '--overlap', type=int, default=3, help="Length of suffix and prefix to overlap (default: 3)")

    args = parser.parse_args()

    main(input_file=args.input, output_file=args.output, k=args.overlap)