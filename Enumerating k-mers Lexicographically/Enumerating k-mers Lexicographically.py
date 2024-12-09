from itertools import product

def lexicographic_strings(file_path):
    # Read input from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse the input
    alphabet = lines[0].strip().split()
    n = int(lines[1].strip())
    
    # Generate all possible strings of length n from the alphabet
    combinations = product(alphabet, repeat=n)
    result = [''.join(combination) for combination in combinations]
    
    return result

input_file = "input.txt"

# Solve the problem
output = lexicographic_strings(input_file)

# Print the output
with open("output.txt", "w") as output_file:
    for string in output:
        output_file.write(string + "\n")
