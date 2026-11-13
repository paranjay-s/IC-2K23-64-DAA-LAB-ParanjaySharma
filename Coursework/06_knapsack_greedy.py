"""
Design and Analysis of Algorithms - Coursework Task 6
Title: Fractional Knapsack Problem using Greedy Strategy

Algorithmic Paradigm: Greedy Strategy
Greedy Choice Property:
    Always pick the item with the highest value-to-weight ratio (value / weight).
    If the remaining capacity cannot accommodate the whole item, take the fraction
    that fills the remaining capacity.

Time Complexity:
    - Sorting items: O(n log n)
    - Selecting items: O(n)
    - Total Time Complexity: O(n log n)
Space Complexity: O(n) for storing item ratios and results
"""

class Item:
    def __init__(self, name: str, weight: float, value: float):
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight if weight > 0 else 0

    def __repr__(self):
        return f"{self.name}(wt={self.weight}, val={self.value}, ratio={self.ratio:.2f})"


def fractional_knapsack(items: list, capacity: float):
    """
    Solves Fractional Knapsack using Greedy approach.
    
    Parameters:
        items (list of Item): List of items with weights and values.
        capacity (float): Maximum weight capacity of knapsack.
        
    Returns:
        tuple: (max_value, taken_details)
    """
    # Sort items by value/weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    taken_details = []

    for item in sorted_items:
        if remaining_capacity == 0:
            break

        if item.weight <= remaining_capacity:
            # Take the whole item
            fraction = 1.0
            total_value += item.value
            remaining_capacity -= item.weight
            taken_details.append({
                "item": item.name,
                "weight_taken": item.weight,
                "value_gained": item.value,
                "fraction": fraction
            })
        else:
            # Take fraction of the item to fill the remaining capacity
            fraction = remaining_capacity / item.weight
            value_gained = item.value * fraction
            total_value += value_gained
            taken_details.append({
                "item": item.name,
                "weight_taken": remaining_capacity,
                "value_gained": value_gained,
                "fraction": fraction
            })
            remaining_capacity = 0.0

    return total_value, capacity - remaining_capacity, taken_details


def main():
    print("=" * 70)
    print(" TASK 6: FRACTIONAL KNAPSACK USING GREEDY STRATEGY ")
    print("=" * 70)

    # Sample dataset
    items = [
        Item("Item 1", weight=10, value=60),
        Item("Item 2", weight=20, value=100),
        Item("Item 3", weight=30, value=120),
        Item("Item 4", weight=15, value=75),
        Item("Item 5", weight=5,  value=30)
    ]
    knapsack_capacity = 50.0

    print(f"Knapsack Total Capacity: {knapsack_capacity} units\n")
    print("Available Items:")
    print(f"{'Item':<10} | {'Weight':<10} | {'Value':<10} | {'Ratio (Val/Wt)':<15}")
    print("-" * 55)
    for it in items:
        print(f"{it.name:<10} | {it.weight:<10.1f} | {it.value:<10.1f} | {it.ratio:<15.2f}")

    total_val, total_wt, details = fractional_knapsack(items, knapsack_capacity)

    print("\nGreedy Selection Details:")
    print(f"{'Item':<10} | {'Fraction Taken':<16} | {'Weight Contrib':<16} | {'Value Contrib':<15}")
    print("-" * 65)
    for d in details:
        print(f"{d['item']:<10} | {d['fraction']*100:<15.1f}% | {d['weight_taken']:<16.2f} | {d['value_gained']:<15.2f}")

    print("-" * 65)
    print(f"Total Weight in Knapsack: {total_wt:.2f} / {knapsack_capacity}")
    print(f"Maximum Total Value Achieved: {total_val:.2f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
