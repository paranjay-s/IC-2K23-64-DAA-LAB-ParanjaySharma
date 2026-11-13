"""
Design and Analysis of Algorithms - Coursework Task 10
Title: 0/1 Knapsack Problem using Dynamic Programming (Tabulation)

Algorithmic Paradigm: Dynamic Programming
Principle:
    Optimal Substructure & Overlapping Subproblems.
    Each item can either be included (1) or excluded (0).

Recurrence Relation:
    dp[i][w] = dp[i-1][w]                                    if wt[i-1] > w
    dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]]) otherwise

Time Complexity: O(n * W), where n is number of items and W is knapsack capacity
Space Complexity: O(n * W) for the 2D tabulation table
"""

def knapsack_01_dp(weights: list, values: list, capacity: int):
    """
    Solves 0/1 Knapsack using Bottom-Up Dynamic Programming.
    
    Parameters:
        weights (list): List of positive integer weights.
        values (list): List of corresponding item values.
        capacity (int): Total integer weight capacity.
        
    Returns:
        tuple: (max_profit, selected_item_indices, dp_table)
    """
    n = len(weights)
    # Initialize DP table of size (n + 1) x (capacity + 1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]
        for w in range(capacity + 1):
            if wt <= w:
                dp[i][w] = max(dp[i - 1][w], val + dp[i - 1][w - wt])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the specific items selected
    selected_indices = []
    curr_w = capacity
    for i in range(n, 0, -1):
        # If value differs from the cell above, item i-1 was included
        if dp[i][curr_w] != dp[i - 1][curr_w]:
            selected_indices.append(i - 1)
            curr_w -= weights[i - 1]

    selected_indices.reverse()
    max_profit = dp[n][capacity]

    return max_profit, selected_indices, dp


def print_dp_table(dp: list, capacity: int):
    """Utility to print the 2D DP matrix neatly."""
    header = f"{'Item/Cap':<10} | " + " ".join(f"{w:>4}" for w in range(capacity + 1))
    print(header)
    print("-" * len(header))
    for i, row in enumerate(dp):
        row_str = f"Item {i:<5} | " + " ".join(f"{val:>4}" for val in row)
        print(row_str)


def main():
    print("=" * 70)
    print(" TASK 10: 0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING) ")
    print("=" * 70)

    # Sample dataset
    item_names = ["Laptop", "Camera", "Watch", "Smartphone"]
    weights = [2, 3, 1, 4]
    values = [40, 50, 20, 60]
    knapsack_capacity = 5

    print(f"Knapsack Capacity: {knapsack_capacity} kg\n")
    print("Available Items:")
    print(f"{'Index':<6} | {'Item Name':<14} | {'Weight (kg)':<12} | {'Value ($)':<10}")
    print("-" * 50)
    for idx in range(len(weights)):
        print(f"{idx:<6} | {item_names[idx]:<14} | {weights[idx]:<12} | {values[idx]:<10}")

    max_profit, selected, dp = knapsack_01_dp(weights, values, knapsack_capacity)

    print("\nDP Tabulation Table (dp[item][capacity]):")
    print_dp_table(dp, knapsack_capacity)

    print("\nOptimal Solution Summary:")
    print(f"Maximum Total Value: ${max_profit}")
    print(f"Selected Items:")
    total_weight = 0
    for idx in selected:
        print(f"  - {item_names[idx]} (Weight: {weights[idx]} kg, Value: ${values[idx]})")
        total_weight += weights[idx]
    print(f"Total Weight Consumed: {total_weight} / {knapsack_capacity} kg")
    print("=" * 70)


if __name__ == "__main__":
    main()
