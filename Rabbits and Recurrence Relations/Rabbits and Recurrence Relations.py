def rabbit_pairs(n, k):
    # Initialize the first two months with 1 pair of rabbits
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Array to store the number of rabbit pairs each month
    rabbits = [0] * (n+1)
    rabbits[1] = 1  # Month 1
    rabbits[2] = 1  # Month 2

    # Build up the solution using the recurrence relation
    for month in range(3, n+1):
        rabbits[month] = rabbits[month-1] + k * rabbits[month-2]
    
    return rabbits[n]

# Read input from the file
with open(r"C:\Users\Blue\Desktop\rosalind\Rabbits and Recurrence Relations\rosalind_fib.txt", 'r') as file:
    # Assuming the input file contains two integers on the first line, separated by a space
    n, k = map(int, file.readline().split())

# Get the result
result = rabbit_pairs(n, k)

# Output the result (you can print or write to a file)
print(result)
