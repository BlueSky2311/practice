# Minimum Edges to Make a Tree

## Problem Description
Given an undirected graph with n nodes and an adjacency list, find the minimum number of edges that need to be added to make the graph a tree.

A tree is a connected graph with no cycles. It has exactly n-1 edges for n nodes.

## Solution Approach
To transform a graph into a tree, we need to:
1. Ensure the graph is connected (has only one connected component)
2. Ensure there are no cycles (exactly n-1 edges)

The solution follows these steps:
1. Count the number of connected components (c) in the graph using BFS or DFS
2. Count the number of existing edges (e) in the graph
3. Calculate the minimum number of edges to add:
   - To connect c components, we need (c-1) edges
   - A tree with n nodes must have exactly (n-1) edges
   - If there are cycles, we need to remove them (but the problem only asks for edges to add)

The final formula is: max(0, (n-1) - e)

## Time and Space Complexity
- Time Complexity: O(n + e) where n is the number of nodes and e is the number of edges
- Space Complexity: O(n + e) for the adjacency list and visited array

## Input Format
The first line contains an integer n (number of nodes).
The following lines contain pairs of integers representing edges in the graph.

## Output Format
A single integer representing the minimum number of edges to add to make the graph a tree.

## Example
For the sample input:
```
10
1 2
2 8
4 10
5 9
6 10
7 9
```

The output is:
```
3
```

This is because we need to add 3 more edges to connect all components and form a tree. 