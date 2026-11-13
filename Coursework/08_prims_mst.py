"""
Design and Analysis of Algorithms - Coursework Task 8
Title: Minimum Cost Spanning Tree (MST) using Prim's Algorithm

Algorithmic Paradigm: Greedy Strategy
Mechanism:
    Maintains a cut between visited and unvisited vertices. At each step,
    greedily selects the minimum weight cross-edge that connects a vertex in the
    tree to an unvisited vertex outside the tree, using a priority queue (min-heap).

Time Complexity:
    - Using Min-Heap Priority Queue: O(E log V), where V = vertices, E = edges
Space Complexity:
    - O(V + E) for adjacency list and heap storage
"""

import heapq
from collections import defaultdict


class Graph:
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.adj = defaultdict(list)

    def add_edge(self, u, v, weight: int):
        """Adds an undirected weighted edge between u and v."""
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    def prim_mst(self, start_vertex=None):
        """
        Finds the Minimum Spanning Tree using Prim's Algorithm.
        
        Returns:
            tuple: (mst_edges, total_cost)
        """
        if not self.vertices:
            return [], 0

        if start_vertex is None:
            start_vertex = self.vertices[0]

        visited = set()
        mst_edges = []
        total_cost = 0

        # Min-heap storing tuples: (weight, u, v)
        min_heap = []

        # Mark start vertex as visited and push its incident edges
        visited.add(start_vertex)
        for weight, neighbor in self.adj[start_vertex]:
            heapq.heappush(min_heap, (weight, start_vertex, neighbor))

        # Loop until MST contains V - 1 edges or heap is empty
        while min_heap and len(visited) < len(self.vertices):
            weight, u, v = heapq.heappop(min_heap)

            # If destination is already visited, skip to avoid cycles
            if v in visited:
                continue

            # Include edge (u, v) in MST
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_cost += weight

            # Push all incident edges from newly visited vertex v
            for next_weight, next_neighbor in self.adj[v]:
                if next_neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, next_neighbor))

        return mst_edges, total_cost


def main():
    print("=" * 65)
    print(" TASK 8: MINIMUM SPANNING TREE (PRIM'S ALGORITHM) ")
    print("=" * 65)

    # Standard undirected weighted graph
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    g = Graph(vertices)

    # Adding weighted undirected edges
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('C', 'D', 3),
        ('C', 'E', 2),
        ('C', 'F', 4),
        ('D', 'F', 3),
        ('E', 'F', 3)
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Graph Vertices:", vertices)
    print("Input Edges and Weights:")
    for u, v, w in edges:
        print(f"  ({u} - {v}) with weight {w}")

    mst_edges, total_cost = g.prim_mst(start_vertex='A')

    print("\nEdges Included in Prim's Minimum Spanning Tree:")
    print(f"{'Edge':<16} | {'Weight':<8}")
    print("-" * 28)
    for u, v, w in mst_edges:
        print(f"({u} <---> {v}){'':<5} | {w:<8}")

    print("-" * 28)
    print(f"Total Minimum Cost of Spanning Tree: {total_cost}")
    print("=" * 65)


if __name__ == "__main__":
    main()
