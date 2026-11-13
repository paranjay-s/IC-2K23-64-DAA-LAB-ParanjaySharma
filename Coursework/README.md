# Design and Analysis of Algorithms - Coursework Lab

This repository directory contains complete, verified Python implementations for all 15 coursework problems for the **Design and Analysis of Algorithms (DAA)** laboratory.

---

## Course Outcomes (COs)

- **CO1:** Develop programs for sorting a given set of elements and analyse its time complexity.
- **CO2:** Solve and analyse the problems using greedy methods.
- **CO3:** Solve and analyse the problems using dynamic programming.
- **CO4:** Apply backtracking method to solve various problems.
- **CO5:** Apply branch and bound method to solve 0/1 knapsack problem.

---

## Coursework Tasks to Course Outcomes Mapping

| Q# | Problem Description | Implementation File | Algorithmic Paradigm | Time Complexity | Space Complexity | Mapped Outcome |
|:--:|:--------------------|:--------------------|:---------------------|:---------------:|:----------------:|:--------------:|
| 1 | Binary Search without recursion | [`01_binary_search_iterative.py`](01_binary_search_iterative.py) | Decrease and Conquer | $O(\log n)$ | $O(1)$ | **CO1** |
| 2 | Binary Search using recursion | [`02_binary_search_recursive.py`](02_binary_search_recursive.py) | Divide and Conquer | $O(\log n)$ | $O(\log n)$ | **CO1** |
| 3 | Max & Min element using Divide and Conquer | [`03_max_min_divide_and_conquer.py`](03_max_min_divide_and_conquer.py) | Divide and Conquer | $O(n)$ | $O(\log n)$ | **CO1** |
| 4 | Quick Sort with Benchmarking & Matplotlib Plot | [`04_quick_sort_analysis.py`](04_quick_sort_analysis.py) | Divide and Conquer | $O(n \log n)$ avg | $O(\log n)$ | **CO1** |
| 5 | Selection, Merge, Insertion, and Radix Sort with Benchmarking & Plot | [`05_sorting_comparison.py`](05_sorting_comparison.py) | Sorting & Complexity Analysis | $O(n^2)$ / $O(n \log n)$ / $O(nk)$ | $O(1)$ / $O(n)$ | **CO1** |
| 6 | Fractional Knapsack Problem | [`06_knapsack_greedy.py`](06_knapsack_greedy.py) | Greedy Strategy | $O(n \log n)$ | $O(n)$ | **CO2** |
| 7 | Job Sequencing with Deadlines | [`07_job_sequencing_greedy.py`](07_job_sequencing_greedy.py) | Greedy Strategy | $O(n \log n + n \cdot D)$ | $O(D)$ | **CO2** |
| 8 | Minimum Cost Spanning Tree (Prim's Algorithm) | [`08_prims_mst.py`](08_prims_mst.py) | Greedy Strategy | $O(E \log V)$ | $O(V + E)$ | **CO2** |
| 9 | Minimum Cost Spanning Tree (Kruskal's Algorithm) | [`09_kruskals_mst.py`](09_kruskals_mst.py) | Greedy Strategy | $O(E \log E)$ | $O(V + E)$ | **CO2** |
| 10 | 0/1 Knapsack Problem | [`10_01_knapsack_dp.py`](10_01_knapsack_dp.py) | Dynamic Programming | $O(n \cdot W)$ | $O(n \cdot W)$ | **CO3** |
| 11 | Memoised Fibonacci Series | [`11_memoized_fibonacci.py`](11_memoized_fibonacci.py) | Dynamic Programming | $O(n)$ | $O(n)$ | **CO3** |
| 12 | Depth First Search (DFS) | [`12_depth_first_search.py`](12_depth_first_search.py) | Graph Traversal / Backtracking | $O(V + E)$ | $O(V)$ | **CO4** |
| 13 | Breadth First Search (BFS) | [`13_breadth_first_search.py`](13_breadth_first_search.py) | Graph Traversal | $O(V + E)$ | $O(V)$ | **CO4** |
| 14 | The 8-Queens Problem | [`14_eight_queens_backtracking.py`](14_eight_queens_backtracking.py) | Backtracking | $O(N!)$ | $O(N)$ | **CO4** |
| 15 | Traveling Salesperson Problem & 0/1 Knapsack | [`15_traveling_salesperson_branch_and_bound.py`](15_traveling_salesperson_branch_and_bound.py) | Branch and Bound (Best-First Search) | Exponential (Pruned) | Exponential | **CO5** |

---

## Detailed Task Descriptions

### 1. Binary Search without Recursion (`01_binary_search_iterative.py`)
- **Outcome:** CO1
- **Approach:** Iterative pointer adjustment using a `while` loop with midpoint calculations avoiding overflow.
- **Complexity:** Time: $O(\log n)$ worst/average, $O(1)$ best; Space: $O(1)$.

### 2. Binary Search with Recursion (`02_binary_search_recursive.py`)
- **Outcome:** CO1
- **Approach:** Classic divide-and-conquer recurrence $T(n) = T(n/2) + O(1)$.
- **Complexity:** Time: $O(\log n)$; Space: $O(\log n)$ call stack frames.

### 3. Max & Min Element using Divide and Conquer (`03_max_min_divide_and_conquer.py`)
- **Outcome:** CO1
- **Approach:** Divides list into two halves until base cases of 1 or 2 elements are reached, combining results in $\approx \frac{3n}{2} - 2$ comparisons instead of $2n - 2$.
- **Complexity:** Time: $O(n)$; Space: $O(\log n)$.

### 4. Quick Sort with Empirical Time Complexity Analysis (`04_quick_sort_analysis.py`)
- **Outcome:** CO1
- **Crucial Features:**
  - Random number generator generates lists for sizes $n \in [100, 200 \dots 10000]$.
  - Automated `verify_sorted()` function validates non-decreasing order and element integrity.
  - Generates and writes metrics to `quicksort_benchmark.csv`.
  - Uses `matplotlib` to render and save empirical runtime curve to `quicksort_benchmark.png`.
- **Complexity:** Time: $O(n \log n)$ average/best, $O(n^2)$ worst; Space: $O(\log n)$.

### 5. Comparative Analysis of Four Sorting Techniques (`05_sorting_comparison.py`)
- **Outcome:** CO1
- **Crucial Features:**
  - Implements Selection Sort, Merge Sort, Insertion Sort, and LSD Radix Sort.
  - Uses random data generator and strict verifier across varying input sizes up to $n = 10,000$.
  - Saves all execution times to `sorting_benchmark.csv`.
  - Generates multi-curve comparative plot saved to `sorting_comparison.png`, demonstrating $O(n^2)$ vs. $O(n \log n)$ vs. $O(nk)$.

### 6. Fractional Knapsack using Greedy Strategy (`06_knapsack_greedy.py`)
- **Outcome:** CO2
- **Approach:** Calculates value-to-weight ratios, sorts in descending order, greedily accumulates whole items, and takes a fraction of the boundary item.
- **Complexity:** Time: $O(n \log n)$; Space: $O(n)$.

### 7. Job Sequencing with Deadlines (`07_job_sequencing_greedy.py`)
- **Outcome:** CO2
- **Approach:** Sorts jobs by profit in descending order; greedily schedules each job in the latest available time slot on or before its deadline.
- **Complexity:** Time: $O(n \log n + n \cdot D)$; Space: $O(D)$.

### 8. Minimum Cost Spanning Tree via Prim's Algorithm (`08_prims_mst.py`)
- **Outcome:** CO2
- **Approach:** Min-heap priority queue greedily selects the minimum-weight cross-edge connecting the visited tree to an unvisited vertex.
- **Complexity:** Time: $O(E \log V)$; Space: $O(V + E)$.

### 9. Minimum Cost Spanning Tree via Kruskal's Algorithm (`09_kruskals_mst.py`)
- **Outcome:** CO2
- **Approach:** Sorts all graph edges by weight; uses Disjoint Set Union (DSU) with Path Compression and Union by Rank to greedily pick non-cycle-forming edges.
- **Complexity:** Time: $O(E \log E)$; Space: $O(V + E)$.

### 10. 0/1 Knapsack Problem using Dynamic Programming (`10_01_knapsack_dp.py`)
- **Outcome:** CO3
- **Approach:** Bottom-up 2D tabulation solving subproblems $dp[i][w]$ with full table visualization and backtracking for selected item subsets.
- **Complexity:** Time: $O(n \cdot W)$; Space: $O(n \cdot W)$.

### 11. Memoised Fibonacci Series (`11_memoized_fibonacci.py`)
- **Outcome:** CO3
- **Approach:** Top-down dynamic programming caching intermediate results in a lookup table, drastically cutting call stack overhead from $O(2^n)$ to $O(n)$.
- **Complexity:** Time: $O(n)$; Space: $O(n)$.

### 12. Depth First Search (`12_depth_first_search.py`)
- **Outcome:** CO4
- **Approach:** Explores as deep as possible before backtracking; features both recursive and explicit stack iterative implementations, plus path-finding.
- **Complexity:** Time: $O(V + E)$; Space: $O(V)$.

### 13. Breadth First Search (`13_breadth_first_search.py`)
- **Outcome:** CO4
- **Approach:** Level-order exploration using a FIFO `collections.deque` queue; guarantees finding shortest paths in unweighted graphs.
- **Complexity:** Time: $O(V + E)$; Space: $O(V)$.

### 14. The 8-Queens Problem (`14_eight_queens_backtracking.py`)
- **Outcome:** CO4
- **Approach:** State-space tree search placing queens row by row with diagonal and column pruning; finds all 92 distinct solutions and prints ASCII chessboards.
- **Complexity:** Time: $O(N!)$; Space: $O(N)$.

### 15. Traveling Salesperson Problem & 0/1 Knapsack via Branch and Bound (`15_traveling_salesperson_branch_and_bound.py`)
- **Outcome:** CO5
- **Approach:**
  - Solves TSP using Best-First Search with a priority queue (analogous to Dijkstra's exploration), computing lower bounds on reduced matrices/outgoing edges to aggressively prune subtrees.
  - Includes a companion Branch and Bound implementation for 0/1 Knapsack to directly address Course Outcome CO5.
- **Complexity:** Worst-case exponential, heavily pruned in practice.

---

## How to Execute the Scripts

Run any script directly using Python 3:

```bash
cd Coursework

# Run individual algorithms
python3 01_binary_search_iterative.py
python3 02_binary_search_recursive.py
python3 03_max_min_divide_and_conquer.py
python3 04_quick_sort_analysis.py
python3 05_sorting_comparison.py
python3 06_knapsack_greedy.py
python3 07_job_sequencing_greedy.py
python3 08_prims_mst.py
python3 09_kruskals_mst.py
python3 10_01_knapsack_dp.py
python3 11_memoized_fibonacci.py
python3 12_depth_first_search.py
python3 13_breadth_first_search.py
python3 14_eight_queens_backtracking.py
python3 15_traveling_salesperson_branch_and_bound.py
```

