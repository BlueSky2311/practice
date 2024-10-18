def count_rabbits(n, m):
    # Initialize list where index 0 is age 0 (newborns)
    ages = [1] + [0] * (m - 1)
    
    for month in range(2, n + 1):
        # Number of new born rabbits is the sum of all mature rabbits
        new_borns = sum(ages[1:])
        # Age the rabbits: shift right, oldest die
        ages = [new_borns] + ages[:-1]
    
    # Total rabbits alive after n months
    return sum(ages)

if __name__ == "__main__":
    import sys
    # Read input
    input_line = sys.stdin.read().strip()
    if not input_line:
        # Handle empty input
        n, m = 0, 0
    else:
        n, m = map(int, input_line.split())
    # Compute and print the result
    print(count_rabbits(n, m))
