import math
from scipy.stats import binom

def calculate_probability(k, N):
    """
    Calculate the probability that at least N individuals in the k-th generation
    have the genotype Aa Bb.
    
    k: generation number (0 <= k <= 7)
    N: minimum number of individuals with genotype Aa Bb
    """
    # Total number of individuals in the k-th generation
    total_individuals = 2 ** k
    
    # Probability that a single individual has genotype Aa Bb
    p_AaBb = 1 / 4
    
    # Calculate the cumulative probability for getting at least N Aa Bb individuals
    # Use the complement of the CDF for the binomial distribution
    probability = 1 - binom.cdf(N - 1, total_individuals, p_AaBb)
    
    return probability

def main():
    # Read the input from a .txt file
    input_file = r"C:\Users\Blue\Desktop\rosalind\Independent Alleles\rosalind_lia.txt"  # Change to the correct file path
    with open(input_file, 'r') as file:
        k, N = map(int, file.readline().strip().split())
    
    # Calculate the probability
    result = calculate_probability(k, N)
    
    # Print the result
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()
