from itertools import permutations, product

def signed_permutations(n):
    """
    Generate all signed permutations of length n.

    Parameters:
    n (int): Positive integer

    Returns:
    list: A list of signed permutations
    """
    # Generate the base numbers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Generate all permutations of the numbers
    perm = permutations(numbers)
    
    # Generate all signed permutations
    signed_perms = []
    for p in perm:
        for s in product([-1, 1], repeat=n):
            signed_perms.append([a * b for a, b in zip(p, s)])
    
    return signed_perms

def main():
    # Input the value of n
    n = int(input("Enter a positive integer n: "))
    
    # Get all signed permutations
    result = signed_permutations(n)
    
    # Output file
    output_file = "signed_permutations.txt"
    
    # Write results to file
    with open(output_file, "w") as f:
        # Write the total number of permutations
        f.write(f"{len(result)}\n")
        
        # Write each permutation
        for perm in result:
            f.write(" ".join(map(str, perm)) + "\n")
    
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
