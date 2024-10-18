from Bio.Seq import Seq
from Bio import SeqIO

def find_proteins_from_orfs(file_path):
    # Read the sequence from the input file in FASTA format
    record = SeqIO.read(file_path, "fasta")
    dna_seq = record.seq

    # Convert given DNA sequence into RNA
    rna_seq = dna_seq.transcribe()

    # Obtain the reverse complement of the given DNA (right to left)
    reverse_complement_dna = dna_seq.reverse_complement()

    # Convert the reverse complement of DNA into RNA
    reverse_complement_rna = reverse_complement_dna.transcribe()

    # Get all six reading frames (three from given RNA, three from reverse complement RNA)
    frames = [rna_seq, rna_seq[1:], rna_seq[2:], reverse_complement_rna, reverse_complement_rna[1:], reverse_complement_rna[2:]]

    # Set to store unique protein strings
    proteins = set()

    # Function to extract proteins from ORFs in a given sequence
    def extract_proteins(seq):
        start_codon = 'M'
        stop_codon = '*'
        current_protein = ""
        recording = False
        for aa in seq:
            if aa == start_codon:
                recording = True
                current_protein = aa
            elif recording:
                current_protein += aa
                if aa == stop_codon:
                    proteins.add(current_protein[:-1])  # Add protein without stop codon
                    recording = False

    # Translate each reading frame to find ORFs
    for frame in frames:
        trimmed_frame = frame[:len(frame) - (len(frame) % 3)]  # Trim sequence to a multiple of three
        translated_frame = trimmed_frame.translate(to_stop=False)
        extract_proteins(str(translated_frame))

    # Write the unique protein strings to a new text file
    output_file_path = file_path.rsplit('.', 1)[0] + "_proteins.txt"
    with open(output_file_path, "w") as output_file:
        for protein in proteins:
            output_file.write(protein + "\n")
        output_file.write("\n")  # Add final line ending after the last candidate

# Example usage with the specified file path
find_proteins_from_orfs(r"C:\Users\Blue\Downloads\Documents\rosalind_orf.txt")
