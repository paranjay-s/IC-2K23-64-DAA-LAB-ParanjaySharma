"""
Design and Analysis of Algorithms - Coursework Task 9
Title: Minimum Cost Spanning Tree (MST) using Kruskal's Algorithm

Algorithmic Paradigm: Greedy Strategy
Mechanism:
    1. Sort all edges in non-decreasing order of their weights.
    2. Use Disjoint Set Union (DSU) with Path Compression and Union by Rank
       to detect and prevent cycles.
    3. Greedily pick the smallest edge. If it connects two disjoint components,
       include it in the MST and union the sets.
    4. Repeat until (V - 1) edges are included.

Time Complexity:
    - Sorting edges: O(E log E) = O(E log V)
    - DSU operations: O(E * alpha(V)), where alpha is the inverse Ackermann function
    - Overall Time Complexity: O(E log E)
Space Complexity: O(V + E) for edge list and DSU parent/rank arrays
"""

class DisjointSetUnion:
    """Disjoint Set Union (Union-Find) with Path Compression and Union by Rank."""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        """Finds representative of set containing item with path compression."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, u, v) -> bool:
        """Unions the sets containing u and v. Returns True if merged, False if cycle."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Already in same set (would form a cycle)

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal_mst(vertices: list, edges: list):
    """
    Finds the Minimum Spanning Tree using Kruskal's Algorithm.
    
    Parameters:
        vertices (list): List of graph vertices.
        edges (list of tuple): List of edges (u, v, weight).
        
    Returns:
        tuple: (mst_edges, total_cost)
    """
    # 1. Sort all edges by weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    dsu = DisjointSetUnion(vertices)
    mst_edges = []
    total_cost = 0

    # 2. Greedily add edges that do not form a cycle
    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight
            # Early termination when V - 1 edges are found
            if len(mst_edges) == len(vertices) - 1:
                break

    return mst_edges, total_cost


def main():
    print("=" * 65)
    print(" TASK 9: MINIMUM SPANNING TREE (KRUSKAL'S ALGORITHM) ")
    print("=" * 65)

    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
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

    print("Graph Vertices:", vertices)
    print("Input Edges and Weights:")
    for u, v, w in edges:
        print(f"  ({u} - {v}) with weight {w}")

    mst_edges, total_cost = kruskal_mst(vertices, edges)

    print("\nEdges Included in Kruskal's Minimum Spanning Tree:")
    print(f"{'Edge':<16} | {'Weight':<8}")
    print("-" * 28)
    for u, v, w in mst_edges:
        print(f"({u} <---> {v}){'':<5} | {w:<8}")

    print("-" * 28)
    print(f"Total Minimum Cost of Spanning Tree: {total_cost}")
    print("=" * 65)


if __name__ == "__main__":
    main()

