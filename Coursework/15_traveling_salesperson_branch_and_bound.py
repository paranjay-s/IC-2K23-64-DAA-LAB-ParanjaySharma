"""
Design and Analysis of Algorithms - Coursework Task 15
Title: Traveling Salesperson Problem (TSP) using Branch and Bound
       (with Best-First Priority Search / Dijkstra Analogy)

Algorithmic Paradigm: Branch and Bound / Best-First Search
Principle:
    - Explores a state-space tree where each state represents a partial tour.
    - Uses a Min-Heap Priority Queue (analogous to Dijkstra's algorithm) to explore
      states with the lowest estimated lower bound first.
    - Bounding Function: Calculates a lower bound on the completion cost of any tour
      extending from the current node:
          Lower Bound = current_cost + sum(min_outgoing_edge(unvisited_v))
    - Pruning: If lower_bound >= current_best_solution_cost, that branch is pruned.
    - Once a complete valid tour is found, the global upper bound is tightened.

Time Complexity: O(2^N * N^2) in worst case, but heavily pruned by bounding function
Space Complexity: O(N * 2^N) for priority queue state storage
"""

import heapq


class Node:
    """Represents a state node in the TSP Branch and Bound tree."""
    def __init__(self, level: int, path: list, bound: float, cost: float):
        self.level = level    # Number of cities visited so far
        self.path = path      # Partial tour list
        self.bound = bound    # Estimated lower bound of tour completing through this node
        self.cost = cost      # Actual cost incurred so far

    def __lt__(self, other):
        # Priority queue orders by lowest bound first (Best-First / Dijkstra style)
        return self.bound < other.bound


def calculate_initial_bound(dist_matrix: list, n: int) -> float:
    """Computes the baseline lower bound for the root node."""
    initial_bound = 0.0
    for i in range(n):
        # Add sum of minimum outgoing edges for each vertex
        row_min = min(dist_matrix[i][j] for j in range(n) if i != j)
        initial_bound += row_min
    return initial_bound


def calculate_child_bound(dist_matrix: list, n: int, curr_node: Node, next_city: int) -> float:
    """
    Computes lower bound for branching to next_city from curr_node.
    """
    last_city = curr_node.path[-1]
    new_cost = curr_node.cost + dist_matrix[last_city][next_city]

    # Bound estimate: new_cost + minimum outgoing edge for all remaining unvisited cities
    visited_set = set(curr_node.path) | {next_city}
    unvisited_bound = 0

    for i in range(n):
        if i not in visited_set:
            # Find min outgoing edge from city i to any city not yet visited (or back to start)
            candidates = [dist_matrix[i][j] for j in range(n) if i != j and (j not in visited_set or j == curr_node.path[0])]
            if candidates:
                unvisited_bound += min(candidates)

    # Edge from next_city to remaining or start
    if len(visited_set) < n:
        candidates = [dist_matrix[next_city][j] for j in range(n) if j not in visited_set]
        if candidates:
            unvisited_bound += min(candidates)
    else:
        # Returning to start city
        unvisited_bound += dist_matrix[next_city][curr_node.path[0]]

    return new_cost + unvisited_bound


def solve_tsp_branch_and_bound(dist_matrix: list):
    """
    Solves Traveling Salesperson Problem using Branch and Bound.
    
    Returns:
        tuple: (best_tour, min_cost, pruned_branches, total_expanded)
    """
    n = len(dist_matrix)
    start_city = 0

    init_bound = calculate_initial_bound(dist_matrix, n)
    root = Node(level=1, path=[start_city], bound=init_bound, cost=0.0)

    # Priority queue for Best-First Search (similar to Dijkstra's exploration)
    pq = []
    heapq.heappush(pq, root)

    best_cost = float('inf')
    best_tour = []
    pruned_count = 0
    expanded_count = 0

    while pq:
        curr = heapq.heappop(pq)
        expanded_count += 1

        # Prune if the lower bound cannot beat the best found complete tour
        if curr.bound >= best_cost:
            pruned_count += 1
            continue

        # If all cities have been visited, complete tour back to start_city
        if curr.level == n:
            final_cost = curr.cost + dist_matrix[curr.path[-1]][start_city]
            if final_cost < best_cost:
                best_cost = final_cost
                best_tour = curr.path + [start_city]
            continue

        # Branch out to all unvisited cities
        for next_city in range(n):
            if next_city not in curr.path:
                next_cost = curr.cost + dist_matrix[curr.path[-1]][next_city]
                next_bound = calculate_child_bound(dist_matrix, n, curr, next_city)

                # Pruning condition
                if next_bound < best_cost:
                    child = Node(
                        level=curr.level + 1,
                        path=curr.path + [next_city],
                        bound=next_bound,
                        cost=next_cost
                    )
                    heapq.heappush(pq, child)
                else:
                    pruned_count += 1

    return best_tour, best_cost, pruned_count, expanded_count


# ----------------------------------------------------------------------
# Bonus: 0/1 Knapsack using Branch and Bound (Demonstrating CO5 explicit syllabus)
# ----------------------------------------------------------------------
class KnapsackNode:
    def __init__(self, level: int, profit: float, weight: float, bound: float, taken: list):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.taken = taken

    def __lt__(self, other):
        # Max-heap emulation by comparing bound (higher upper bound prioritized)
        return self.bound > other.bound


def knapsack_01_branch_and_bound(weights: list, values: list, capacity: float):
    """
    Solves 0/1 Knapsack problem using Branch and Bound (Best-First Search).
    """
    n = len(weights)
    # Sort items by value/weight ratio descending
    items = sorted(
        [{"id": i, "w": weights[i], "v": values[i], "r": values[i] / weights[i]} for i in range(n)],
        key=lambda x: x["r"],
        reverse=True
    )

    def bound(level, curr_profit, curr_weight):
        if curr_weight >= capacity:
            return 0
        profit_bound = curr_profit
        total_w = curr_weight
        idx = level
        while idx < n and total_w + items[idx]["w"] <= capacity:
            total_w += items[idx]["w"]
            profit_bound += items[idx]["v"]
            idx += 1
        if idx < n:
            profit_bound += (capacity - total_w) * items[idx]["r"]
        return profit_bound

    pq = []
    root_bound = bound(0, 0, 0)
    heapq.heappush(pq, KnapsackNode(0, 0, 0, root_bound, []))
    max_profit = 0
    best_taken = []

    while pq:
        curr = heapq.heappop(pq)
        if curr.bound <= max_profit:
            continue
        if curr.level == n:
            if curr.profit > max_profit:
                max_profit = curr.profit
                best_taken = curr.taken
            continue

        item = items[curr.level]
        # Branch 1: Include item if within capacity
        if curr.weight + item["w"] <= capacity:
            incl_profit = curr.profit + item["v"]
            incl_weight = curr.weight + item["w"]
            incl_bound = bound(curr.level + 1, incl_profit, incl_weight)
            if incl_profit > max_profit:
                max_profit = incl_profit
                best_taken = curr.taken + [item["id"]]
            if incl_bound > max_profit:
                heapq.heappush(pq, KnapsackNode(curr.level + 1, incl_profit, incl_weight, incl_bound, curr.taken + [item["id"]]))

        # Branch 2: Exclude item
        excl_bound = bound(curr.level + 1, curr.profit, curr.weight)
        if excl_bound > max_profit:
            heapq.heappush(pq, KnapsackNode(curr.level + 1, curr.profit, curr.weight, excl_bound, curr.taken))

    return max_profit, best_taken


def main():
    print("=" * 70)
    print(" TASK 15: TRAVELING SALESPERSON PROBLEM (BRANCH & BOUND) ")
    print("=" * 70)

    # City names and distance matrix (Asymmetric/Symmetric TSP instance)
    city_names = ["City A (0)", "City B (1)", "City C (2)", "City D (3)", "City E (4)"]
    distance_matrix = [
        [0,  10, 12, 29, 25],
        [10, 0,  35, 15, 20],
        [12, 35, 0,  30, 10],
        [29, 15, 30, 0,  18],
        [25, 20, 10, 18, 0 ]
    ]

    print("Distance Matrix (Adjacency Matrix):")
    header = f"{'Cities':<14} | " + " ".join(f"{c:>8}" for c in ["A(0)", "B(1)", "C(2)", "D(3)", "E(4)"])
    print(header)
    print("-" * len(header))
    for i, row in enumerate(distance_matrix):
        print(f"{city_names[i]:<14} | " + " ".join(f"{val:>8}" for val in row))

    tour, min_cost, pruned, expanded = solve_tsp_branch_and_bound(distance_matrix)

    print("\n--- Optimal TSP Solution ---")
    tour_named = [city_names[idx] for idx in tour]
    print(f"Optimal Hamiltonian Tour:  {' -> '.join(tour_named)}")
    print(f"Index Route:               {' -> '.join(map(str, tour))}")
    print(f"Minimum Tour Travel Cost:  {min_cost}")
    print(f"Search Statistics:         {expanded} nodes expanded, {pruned} branches pruned")

    print("\n" + "-" * 70)
    print("BONUS: 0/1 Knapsack via Branch & Bound (Addressing Course Outcome CO5):")
    k_weights = [2, 4, 6, 9]
    k_values = [10, 10, 12, 18]
    k_cap = 15
    k_max_p, k_items = knapsack_01_branch_and_bound(k_weights, k_values, k_cap)
    print(f"Knapsack Capacity: {k_cap}, Weights: {k_weights}, Values: {k_values}")
    print(f"Optimal Value: {k_max_p}, Selected Item Indices: {sorted(k_items)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
