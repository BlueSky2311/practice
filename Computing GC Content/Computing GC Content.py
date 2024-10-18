def parse_fasta_from_file(file_path):
    sequences = {}
    current_label = None
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(">"):
                current_label = line[1:].strip()
                sequences[current_label] = ""
            else:
                sequences[current_label] += line.strip()
    return sequences

def gc_content(dna_sequence):
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    return (g_count + c_count) / len(dna_sequence) * 100

def calculate_and_display_gc_content(file_path):
    sequences = parse_fasta_from_file(file_path)
    highest_gc_id = None
    highest_gc_content = 0.0
    
    # Display GC content for each sequence
    for label, sequence in sequences.items():
        gc = gc_content(sequence)
        print(f"{label}: {gc:.6f}% GC-content")
        
        if gc > highest_gc_content:
            highest_gc_content = gc
            highest_gc_id = label
    
    print("\nSequence with highest GC-content:")
    print(f"{highest_gc_id}: {highest_gc_content:.6f}% GC-content")

# Example usage
file_path = r"C:\Users\Blue\Desktop\rosalind\Computing GC Content\rosalind_gc.txt"  # Replace with your .fasta file path
calculate_and_display_gc_content(file_path)