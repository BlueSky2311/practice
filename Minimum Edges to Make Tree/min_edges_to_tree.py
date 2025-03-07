from collections import defaultdict, deque

def min_edges_to_make_tree(n, adjacency_list):
    """
    Calculate the minimum number of edges needed to add to make a graph a tree.
    
    Args:
        n: Number of nodes (1 to n)
        adjacency_list: List of edges as pairs [u, v]
    
    Returns:
        Minimum number of edges to add
    """
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in adjacency_list:
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph
    
    # Count the number of connected components using BFS
    visited = [False] * (n + 1)  # +1 because nodes are 1-indexed
    components = 0
    
    for node in range(1, n + 1):
        if not visited[node]:
            components += 1
            # BFS to mark all nodes in this component as visited
            queue = deque([node])
            visited[node] = True
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    # Count the number of edges in the graph
    edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2  # Divide by 2 because each edge is counted twice
    
    # Calculate the number of edges to add
    # For a tree with n nodes, we need exactly (n-1) edges
    # If we have multiple components, we need to add (components-1) edges to connect them
    # If we have cycles, we need to remove (edge_count - (n - components)) edges
    
    # The minimum number of edges to add is (n-1) - edge_count + (components-1)
    # This simplifies to: components - 1 - (edge_count - (n - components))
    # Further simplified: components - 1 - edge_count + n - components
    # Final formula: n - 1 - edge_count
    
    return max(0, n - 1 - edge_count)

def main():
    # Read input from file
    with open(r"C:\Users\Blue\Documents\GitHub\practice\Minimum Edges to Make Tree\input.txt", 'r') as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())
    adjacency_list = []
    
    for i in range(1, len(lines)):
        u, v = map(int, lines[i].strip().split())
        adjacency_list.append((u, v))
    
    result = min_edges_to_make_tree(n, adjacency_list)
    print(result)
    
    # Write output to file
    with open(r"C:\Users\Blue\Documents\GitHub\practice\Minimum Edges to Make Tree\output.txt", 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main() 