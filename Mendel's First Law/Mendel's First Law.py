def dominant_allele_probability(k, m, n):
    # Total population
    total = k + m + n
    
    # Total possible pairs (choosing 2 organisms)
    total_pairs = total * (total - 1)
    
    # Calculate probabilities of producing dominant phenotype
    prob_kk = k * (k - 1)  # k mates with k (always dominant)
    prob_km = 2 * k * m  # k mates with m (always dominant)
    prob_kn = 2 * k * n  # k mates with n (always dominant)
    prob_mm = m * (m - 1) * 0.75  # m mates with m (75% chance dominant)
    prob_mn = 2 * m * n * 0.5  # m mates with n (50% chance dominant)
    
    # Calculate the probability of dominant offspring
    dominant_probability = (prob_kk + prob_km + prob_kn + prob_mm + prob_mn) / total_pairs
    
    return dominant_probability

# Read input from file
with open(r"C:\Users\Blue\Desktop\rosalind\Mendel's First Law\rosalind_iprb.txt", 'r') as file:
    # The input is three integers k, m, and n on one line
    k, m, n = map(int, file.readline().split())

# Calculate the result
result = dominant_allele_probability(k, m, n)

# Print the result rounded to 5 decimal places
print(f"{result:.5f}")
