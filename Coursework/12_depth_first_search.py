"""
Design and Analysis of Algorithms - Coursework Task 12
Title: Depth First Search (DFS) Traversal and Applications

Algorithmic Paradigm: Graph Traversal / Backtracking
Mechanism:
    Explores as deep as possible along each branch before backtracking.
    Can be implemented recursively (using system call stack) or iteratively
    (using an explicit LIFO stack data structure).

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
Space Complexity: O(V) for visited set and call stack / auxiliary stack
"""

from collections import defaultdict


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        """Adds an edge between vertex u and vertex v."""
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def dfs_recursive(self, start_node) -> list:
        """Performs DFS traversal recursively starting from start_node."""
        visited = set()
        traversal_order = []

        def _dfs(node):
            visited.add(node)
            traversal_order.append(node)
            for neighbor in sorted(self.adj[node]):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start_node)
        return traversal_order

    def dfs_iterative(self, start_node) -> list:
        """Performs DFS traversal iteratively using an explicit stack."""
        visited = set()
        traversal_order = []
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                # Push neighbors in reverse sorted order so smaller items are processed first
                for neighbor in sorted(self.adj[node], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal_order

    def find_path(self, start, target, visited=None) -> list:
        """Finds any path from start to target using DFS."""
        if visited is None:
            visited = set()

        visited.add(start)
        if start == target:
            return [start]

        for neighbor in sorted(self.adj[start]):
            if neighbor not in visited:
                path = self.find_path(neighbor, target, visited)
                if path:
                    return [start] + path
        return []


def main():
    print("=" * 65)
    print(" TASK 12: DEPTH FIRST SEARCH (DFS) ")
    print("=" * 65)

    # Sample Graph Creation
    g = Graph(directed=False)
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('E', 'H')
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Graph Structure (Adjacency List):")
    for node in sorted(g.adj.keys()):
        print(f"  Node {node} -> {g.adj[node]}")

    start_vertex = 'A'
    order_rec = g.dfs_recursive(start_vertex)
    order_iter = g.dfs_iterative(start_vertex)

    print(f"\nDFS Traversal from root '{start_vertex}':")
    print(f"  Recursive DFS Order: {' -> '.join(order_rec)}")
    print(f"  Iterative DFS Order: {' -> '.join(order_iter)}")

    target = 'H'
    path = g.find_path(start_vertex, target)
    print(f"\nPath from '{start_vertex}' to '{target}' found via DFS:")
    print(f"  {' -> '.join(path) if path else 'No path exists'}")
    print("=" * 65)


if __name__ == "__main__":
    main()

