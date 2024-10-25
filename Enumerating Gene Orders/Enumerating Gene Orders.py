import itertools

def generate_permutations(n, output_file):
    # Generate all permutations of the sequence from 1 to n
    perm = list(itertools.permutations(range(1, n + 1)))
    
    # Write the total number of permutations to the file
    with open(output_file, 'w') as f:
        f.write(f"{len(perm)}\n")
        
        # Write each permutation on a new line
        for p in perm:
            f.write(" ".join(map(str, p)) + "\n")

# Prompt for input from the user
n = int(input("Enter a positive integer n (n ≤ 7): "))

# Specify the output file name
output_file = r"C:\Users\Blue\Downloads\Documents\result_rosalind_perm.txt"

# Generate and write the permutations to the output file
generate_permutations(n, output_file)

print(f"The output has been written to {output_file}")
