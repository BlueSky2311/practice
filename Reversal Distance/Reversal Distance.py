import heapq

def parse_permutation(s):
    return list(map(int, s.strip().split()))

def normalize_permutation(perm, target):
    if set(perm) != set(target):
        raise ValueError(f"Permutations must contain the same elements.\nperm1: {perm}\nperm2: {target}")
    m = {val: idx + 1 for idx, val in enumerate(target)}
    normalized = [m[val] for val in perm]
    return normalized

def count_breakpoints(perm):
    perm = [0] + list(perm) + [len(perm) + 1]
    breakpoints = sum(1 for i in range(len(perm) - 1) if perm[i + 1] - perm[i] != 1)
    return breakpoints

def reversal_distance(start_perm):
    n = len(start_perm)
    target_perm = tuple(range(1, n + 1))
    visited = set()
    heap = []
    # Adjusted heuristic: ceiling of half the number of breakpoints
    start_breakpoints = (count_breakpoints(start_perm) + 1) // 2
    heapq.heappush(heap, (start_breakpoints, 0, tuple(start_perm)))
    visited.add(tuple(start_perm))

    while heap:
        estimated_total_cost, g, perm = heapq.heappop(heap)
        if perm == target_perm:
            return g
        # Generate all possible reversals
        for i in range(n):
            for j in range(i + 1, n):
                new_perm = perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]
                if new_perm not in visited:
                    visited.add(new_perm)
                    h = (count_breakpoints(new_perm) + 1) // 2
                    heapq.heappush(heap, (g + 1 + h, g + 1, new_perm))
    return -1  # Should not reach here for valid permutations

def main():
    with open(r"C:\Users\Blue\Downloads\Documents\rosalind_rear.txt", 'r') as f:
        # Read all non-empty lines
        data = [line.strip() for line in f if line.strip()]
    if len(data) % 2 != 0:
        print("Error: The input file does not contain an even number of non-empty lines.")
        return
    pairs = []
    for i in range(0, len(data), 2):
        perm1 = parse_permutation(data[i])
        perm2 = parse_permutation(data[i + 1])
        pairs.append((perm1, perm2))

    results = []
    for index, (perm1, perm2) in enumerate(pairs):
        try:
            normalized_perm = normalize_permutation(perm1, perm2)
            dist = reversal_distance(normalized_perm)
            results.append(str(dist))
        except ValueError as e:
            print(f"Error processing pair {index + 1}:\n{e}")
            return
        except Exception as e:
            print(f"An unexpected error occurred while processing pair {index + 1}:\n{e}")
            return
    print(' '.join(results))

if __name__ == '__main__':
    main()
