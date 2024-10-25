# Monoisotopic mass table for amino acids
mass_table = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
}

# Function to calculate the total weight of a protein string
def calculate_protein_mass(protein_string):
    total_mass = 0.0
    for aa in protein_string:
        total_mass += mass_table.get(aa, 0)  # Add the mass of each amino acid
    return total_mass

# Input: protein string (you can change it to test other strings)
protein_string = input("Enter a protein string: ").strip()

# Calculate and print the total mass
total_mass = calculate_protein_mass(protein_string)
print(f"Total mass of the protein string: {total_mass:.3f}")
