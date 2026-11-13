"""
Design and Analysis of Algorithms - Coursework Task 1
Title: Binary Search without using recursion (Iterative approach)

Time Complexity:
    - Best Case: O(1)
    - Average Case: O(log n)
    - Worst Case: O(log n)
Space Complexity: O(1)
"""

def binary_search_iterative(arr: list, target: int) -> int:
    """
    Performs iterative binary search on a sorted list.
    
    Parameters:
        arr (list): A sorted list of comparable elements.
        target (int): The element to search for.
        
    Returns:
        int: The 0-based index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate mid index avoiding potential integer overflow
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Target lies in right half
        else:
            high = mid - 1  # Target lies in left half

    return -1  # Target not present in list


def main():
    print("=" * 60)
    print(" TASK 1: BINARY SEARCH WITHOUT RECURSION (ITERATIVE) ")
    print("=" * 60)

    sample_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    print(f"Sorted Input Array: {sample_list}\n")

    test_targets = [11, 55, 99, 40, 105]

    for target in test_targets:
        idx = binary_search_iterative(sample_list, target)
        if idx != -1:
            print(f"  Target {target:3d} -> Found at index {idx} (arr[{idx}] = {sample_list[idx]})")
        else:
            print(f"  Target {target:3d} -> Not found in array")
    print("=" * 60)


if __name__ == "__main__":
    main()

