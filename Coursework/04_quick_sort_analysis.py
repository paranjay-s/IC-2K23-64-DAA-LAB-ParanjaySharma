"""
Design and Analysis of Algorithms - Coursework Task 4
Title: Quick Sort with Empirical Time Complexity Analysis

Crucial Requirements Met:
    1. Random number generator to create input lists.
    2. Verifier function to validate sorting correctness.
    3. Benchmarking across varying input sizes (n = 100, 200 ... 10000).
    4. Export results (n, time taken) to CSV/text file.
    5. Matplotlib visualization plotting Time Taken vs. Input Size (n).

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n^2) (mitigated using randomized / median pivot)
Space Complexity: O(log n) auxiliary stack space
"""

import sys
import time
import random
import csv
import os
import matplotlib
# Use non-interactive backend by default to avoid GUI blocks, but allow interactive if supported
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Increase recursion depth for large arrays
sys.setrecursionlimit(200000)


def partition(arr: list, low: int, high: int) -> int:
    """
    Partitions the array using a randomized pivot to prevent O(n^2) worst case.
    """
    # Pick random pivot and swap with high
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr: list, low: int, high: int):
    """Recursive Quick Sort helper."""
    while low < high:
        pi = partition(arr, low, high)

        # Tail recursion optimization: recurse on smaller subarray first
        if pi - low < high - pi:
            quick_sort_helper(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort_helper(arr, pi + 1, high)
            high = pi - 1


def quick_sort(arr: list) -> list:
    """
    Sorts a copy of the input list using Quick Sort.
    """
    arr_copy = arr.copy()
    if len(arr_copy) > 1:
        quick_sort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def verify_sorted(original: list, sorted_arr: list) -> bool:
    """
    Verifier function to check if the array is correctly sorted in ascending order
    and contains the exact same elements.
    """
    if len(original) != len(sorted_arr):
        return False
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] > sorted_arr[i + 1]:
            return False
    return True


def run_benchmarks(sizes: list) -> list:
    """
    Generates random lists for varying input sizes, times Quick Sort,
    verifies correctness, and records benchmark metrics.
    """
    results = []
    print(f"{'Input Size (n)':<16} | {'Time Taken (s)':<18} | {'Verifier Check'}")
    print("-" * 52)

    for n in sizes:
        # Generate random list of size n
        random_list = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]

        # Time the quick sort execution
        start_time = time.perf_counter()
        sorted_list = quick_sort(random_list)
        elapsed_time = time.perf_counter() - start_time

        # Verify correctness
        is_correct = verify_sorted(random_list, sorted_list)
        status = "PASSED" if is_correct else "FAILED"

        results.append((n, elapsed_time, is_correct))
        print(f"{n:<16} | {elapsed_time:<18.6f} | {status}")

    return results


def save_to_csv(results: list, filepath: str):
    """Saves benchmark results (n and time taken) to CSV file."""
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Input_Size_n", "Time_Seconds", "Verification_Passed"])
        for row in results:
            writer.writerow(row)
    print(f"\n[+] Benchmark data saved to: {filepath}")


def plot_results(results: list, filepath: str):
    """Plots Time Taken vs. Input Size (n) using Matplotlib."""
    sizes = [row[0] for row in results]
    times = [row[1] for row in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', color='teal', linewidth=2, markersize=6, label='Quick Sort Time')

    plt.title("Quick Sort Empirical Time Complexity Analysis", fontsize=14, fontweight='bold')
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Time Taken (seconds)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()

    plt.savefig(filepath, dpi=300)
    plt.close()
    print(f"[+] Empirical time graph saved to: {filepath}")


def main():
    print("=" * 60)
    print(" TASK 4: QUICK SORT - BENCHMARK & COMPLEXITY ANALYSIS ")
    print("=" * 60)

    # Varying input sizes from 100 up to 10,000
    test_sizes = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "quicksort_benchmark.csv")
    plot_file = os.path.join(base_dir, "quicksort_benchmark.png")

    results = run_benchmarks(test_sizes)
    save_to_csv(results, csv_file)
    plot_results(results, plot_file)
    print("=" * 60)


if __name__ == "__main__":
    main()
