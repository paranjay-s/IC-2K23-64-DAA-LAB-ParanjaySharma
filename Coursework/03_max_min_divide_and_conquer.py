"""
Design and Analysis of Algorithms - Coursework Task 3
Title: Find Maximum and Minimum Element using Divide and Conquer

Algorithmic Paradigm: Divide and Conquer
Recurrence Relation:
    T(n) = 2 * T(n/2) + 2  (for n > 2)
    T(2) = 1
    T(1) = 0
Total Comparisons:
    Takes approx 3n/2 - 2 comparisons, compared to 2n - 2 in naive linear scan.

Time Complexity: O(n)
Space Complexity: O(log n) auxiliary stack space
"""

def find_min_max_dc(arr: list, low: int, high: int):
    """
    Finds maximum and minimum in arr[low..high] using Divide and Conquer.
    
    Returns:
        tuple: (min_element, max_element, comparison_count)
    """
    # Case 1: Only one element in subarray
    if low == high:
        return arr[low], arr[low], 0

    # Case 2: Exactly two elements in subarray
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high], 1
        else:
            return arr[high], arr[low], 1

    # Case 3: More than two elements -> Divide
    mid = (low + high) // 2
    left_min, left_max, left_comps = find_min_max_dc(arr, low, mid)
    right_min, right_max, right_comps = find_min_max_dc(arr, mid + 1, high)

    # Conquer / Combine: 2 comparisons
    overall_min = left_min if left_min < right_min else right_min
    overall_max = left_max if left_max > right_max else right_max
    total_comps = left_comps + right_comps + 2

    return overall_min, overall_max, total_comps


def find_min_max(arr: list):
    """Convenience wrapper for the divide and conquer min-max function."""
    if not arr:
        raise ValueError("Cannot find min/max of an empty list.")
    return find_min_max_dc(arr, 0, len(arr) - 1)


def main():
    print("=" * 65)
    print(" TASK 3: MAX AND MIN USING DIVIDE AND CONQUER ")
    print("=" * 65)

    test_arrays = [
        [1000, 11, 445, 1, 330, 3000],
        [70, 250, -10, 85, 900, 3, 45, 120, -50],
        [42],
        [15, 29],
        [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    ]

    for i, arr in enumerate(test_arrays, 1):
        min_val, max_val, comps = find_min_max(arr)
        naive_comps = 2 * (len(arr) - 1) if len(arr) > 1 else 0
        print(f"Test Case {i}: Array = {arr}")
        print(f"  -> Array Length: {len(arr)}")
        print(f"  -> Minimum: {min_val}")
        print(f"  -> Maximum: {max_val}")
        print(f"  -> D&C Comparisons: {comps} (Naive would be: {naive_comps})\n")

    print("=" * 65)


if __name__ == "__main__":
    main()

