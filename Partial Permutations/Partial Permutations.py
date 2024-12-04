def partial_permutations(n, k):
    """
    Calculate P(n, k) modulo 1,000,000
    where P(n, k) = n * (n - 1) * ... * (n - k + 1).
    """
    mod = 1_000_000
    result = 1
    for i in range(k):
        result = (result * (n - i)) % mod
    return result

if __name__ == "__main__":
    # Accept input for n and k
    print("Enter values for n and k separated by a space (e.g., '21 7'):")
    n, k = map(int, input().strip().split())

    # Validate input
    if not (1 <= k <= n <= 100):
        print("Invalid input! Ensure 1 ≤ k ≤ n ≤ 100.")
    else:
        # Compute and print the result
        result = partial_permutations(n, k)
        print(f"The total number of partial permutations P({n}, {k}) modulo 1,000,000 is: {result}")
