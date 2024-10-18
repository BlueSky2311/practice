def find_substring_locations(s, t):
    # Initialize an empty list to store the starting positions
    positions = []
    
    # Loop through the string 's' to find all occurrences of 't'
    for i in range(len(s) - len(t) + 1):
        # Check if the substring of s starting at i matches t
        if s[i:i + len(t)] == t:
            # Append the position to the list (1-based index)
            positions.append(i + 1)
    
    return positions

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read both s and t from the file, assuming they are on separate lines
        s = file.readline().strip()
        t = file.readline().strip()
    return s, t

if __name__ == "__main__":
    # Specify the input file name
    input_file = r"C:\Users\Blue\Desktop\rosalind\Finding a Motif in DNA\rosalind_subs.txt"  # Change to your file path if needed
    
    # Read the strings s and t from the file
    s, t = read_input_from_file(input_file)
    
    # Find locations of substring t in s
    locations = find_substring_locations(s, t)
    
    # Print all locations as space-separated values
    print(" ".join(map(str, locations)))
