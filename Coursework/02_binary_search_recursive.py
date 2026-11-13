"""
Design and Analysis of Algorithms - Coursework Task 2
Title: Binary Search using recursion (Divide and Conquer approach)

Recurrence Relation:
    T(n) = T(n/2) + O(1)
    By Master Theorem: Time Complexity = O(log n)

Time Complexity:
    - Best Case: O(1)
    - Average Case: O(log n)
    - Worst Case: O(log n)
Space Complexity: O(log n) auxiliary stack space
"""

def binary_search_recursive(arr: list, low: int, high: int, target: int) -> int:
    """
    Performs recursive binary search on a sorted list.
    
    Parameters:
        arr (list): A sorted list of comparable elements.
        low (int): Lower bound index of the search subarray.
        high (int): Upper bound index of the search subarray.
        target (int): Element to search for.
        
    Returns:
        int: Index of target if found, else -1.
    """
    # Base case: search space exhausted
    if low > high:
        return -1

    mid = low + (high - low) // 2

    # Element found at mid
    if arr[mid] == target:
        return mid
    # Element is smaller than mid, search in left subarray
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    # Element is greater than mid, search in right subarray
    else:
        return binary_search_recursive(arr, mid + 1, high, target)


def binary_search(arr: list, target: int) -> int:
    """Convenience wrapper for recursive binary search."""
    return binary_search_recursive(arr, 0, len(arr) - 1, target)


def main():
    print("=" * 60)
    print(" TASK 2: BINARY SEARCH USING RECURSION ")
    print("=" * 60)

    sample_list = [5, 12, 19, 27, 34, 45, 58, 70, 83, 96]
    print(f"Sorted Input Array: {sample_list}\n")

    test_targets = [5, 34, 96, 50, 100]

    for target in test_targets:
        idx = binary_search(sample_list, target)
        if idx != -1:
            print(f"  Target {target:3d} -> Found at index {idx} (arr[{idx}] = {sample_list[idx]})")
        else:
            print(f"  Target {target:3d} -> Not found in array")
    print("=" * 60)


if __name__ == "__main__":
    main()
