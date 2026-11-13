"""
Design and Analysis of Algorithms - Coursework Task 13
Title: Breadth First Search (BFS) Traversal and Shortest Path

Algorithmic Paradigm: Graph Traversal
Mechanism:
    Explores neighbor vertices level by level using a FIFO queue.
    Guarantees finding the shortest path (in terms of number of edges)
    in unweighted graphs.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
Space Complexity: O(V) for the queue, visited set, and distance mapping
"""

from collections import deque, defaultdict


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        """Adds an edge between vertex u and vertex v."""
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def bfs_traversal(self, start_node) -> list:
        """Performs standard BFS traversal from start_node."""
        visited = {start_node}
        queue = deque([start_node])
        traversal_order = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in sorted(self.adj[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def shortest_path_bfs(self, start_node, target_node):
        """
        Finds the unweighted shortest path and edge distance from start to target.
        
        Returns:
            tuple: (path_list, distance)
        """
        if start_node == target_node:
            return [start_node], 0

        visited = {start_node}
        queue = deque([start_node])
        parent = {start_node: None}
        distance = {start_node: 0}

        while queue:
            curr = queue.popleft()

            if curr == target_node:
                # Reconstruct path
                path = []
                temp = target_node
                while temp is not None:
                    path.append(temp)
                    temp = parent[temp]
                path.reverse()
                return path, distance[target_node]

            for neighbor in sorted(self.adj[curr]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    distance[neighbor] = distance[curr] + 1
                    queue.append(neighbor)

        return [], float('inf')


def main():
    print("=" * 65)
    print(" TASK 13: BREADTH FIRST SEARCH (BFS) ")
    print("=" * 65)

    # Sample Graph Creation
    g = Graph(directed=False)
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('D', 'H'), ('E', 'H'),
        ('G', 'H')
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Graph Structure (Adjacency List):")
    for node in sorted(g.adj.keys()):
        print(f"  Node {node} -> {g.adj[node]}")

    start_vertex = 'A'
    bfs_order = g.bfs_traversal(start_vertex)
    print(f"\nBFS Traversal Order starting from '{start_vertex}':")
    print(f"  {' -> '.join(bfs_order)}")

    target_vertex = 'H'
    shortest_path, dist = g.shortest_path_bfs(start_vertex, target_vertex)
    print(f"\nShortest Path from '{start_vertex}' to '{target_vertex}' via BFS:")
    print(f"  Path:     {' -> '.join(shortest_path)}")
    print(f"  Distance: {dist} edge(s)")
    print("=" * 65)


if __name__ == "__main__":
    main()

