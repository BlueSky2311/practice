def hamming_distance(s, t):
    # Initialize the distance counter
    distance = 0

    # Iterate over both strings and compare each character
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    
    return distance

# Read input from the file
with open(r"C:\Users\Blue\Desktop\rosalind\Counting Point Mutations\rosalind_hamm.txt", 'r') as file:
    # Read the two DNA strings from the file
    s = file.readline().strip()  # First DNA string
    t = file.readline().strip()  # Second DNA string

# Ensure the strings are of equal length
if len(s) != len(t):
    raise ValueError("The two DNA strings must be of equal length.")

# Get the Hamming distance
result = hamming_distance(s, t)

# Output the result
print(result)
