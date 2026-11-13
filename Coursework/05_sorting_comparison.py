"""
Design and Analysis of Algorithms - Coursework Task 5
Title: Comparative Analysis of Four Sorting Techniques:
       Selection Sort, Merge Sort, Insertion Sort, and Radix Sort

Crucial Requirements Met:
    1. Implementation of all 4 sorting algorithms.
    2. Random number generator to produce benchmark input lists.
    3. Verifier function to validate sorted output for every algorithm.
    4. Benchmarking across varying input sizes (n = 100, 200 ... 10000).
    5. Save benchmark data (n and execution times) to CSV/text file.
    6. Matplotlib comparison graph plotting Time Taken vs. Input Size (n).

Complexity Summary:
    - Selection Sort: Time O(n^2), Space O(1)
    - Merge Sort:     Time O(n log n), Space O(n)
    - Insertion Sort: Time O(n^2), Space O(1)
    - Radix Sort:     Time O(d * (n + k)), Space O(n + k)
"""

import time
import random
import csv
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# -------------------------------------------------------------
# 1. Selection Sort
# -------------------------------------------------------------
def selection_sort(arr: list) -> list:
    """Sorts an array using Selection Sort algorithm."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# -------------------------------------------------------------
# 2. Merge Sort
# -------------------------------------------------------------
def merge_sort(arr: list) -> list:
    """Sorts an array using Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge step
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# -------------------------------------------------------------
# 3. Insertion Sort
# -------------------------------------------------------------
def insertion_sort(arr: list) -> list:
    """Sorts an array using Insertion Sort algorithm."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# -------------------------------------------------------------
# 4. Radix Sort (LSD with Counting Sort Subroutine)
# -------------------------------------------------------------
def counting_sort_by_digit(arr: list, exp: int) -> list:
    """Counting sort subroutine for Radix Sort on digit exp (1, 10, 100...)."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr: list) -> list:
    """
    Sorts a non-negative integer array using LSD Radix Sort.
    Handles signed integers by mapping them to non-negative offsets.
    """
    if not arr:
        return []

    min_val = min(arr)
    # Offset numbers if array contains negative values
    shift = -min_val if min_val < 0 else 0
    shifted_arr = [x + shift for x in arr]

    max_val = max(shifted_arr)
    exp = 1
    current = shifted_arr
    while max_val // exp > 0:
        current = counting_sort_by_digit(current, exp)
        exp *= 10

    # Shift back
    return [x - shift for x in current]


# -------------------------------------------------------------
# Verifier Function
# -------------------------------------------------------------
def verify_sorted(original: list, sorted_arr: list) -> bool:
    """Verifier function checking array is sorted in non-decreasing order."""
    if len(original) != len(sorted_arr):
        return False
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] > sorted_arr[i + 1]:
            return False
    return True


# -------------------------------------------------------------
# Benchmarking Harness
# -------------------------------------------------------------
def run_sorting_benchmarks(sizes: list) -> dict:
    """
    Runs benchmarking across all 4 sorting techniques for specified input sizes.
    """
    algorithms = {
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Radix Sort": radix_sort,
    }

    results = {name: [] for name in algorithms}
    results["sizes"] = sizes

    header = f"{'Size (n)':<10} | " + " | ".join(f"{name:<16}" for name in algorithms)
    print(header)
    print("-" * len(header))

    for n in sizes:
        # Generate random array of integers
        test_data = [random.randint(1, 100_000) for _ in range(n)]
        row_str = f"{n:<10} | "

        for name, func in algorithms.items():
            start_time = time.perf_counter()
            sorted_data = func(test_data)
            elapsed = time.perf_counter() - start_time

            # Verify sorting correctness
            if not verify_sorted(test_data, sorted_data):
                raise ValueError(f"Verification FAILED for {name} on n={n}!")

            results[name].append(elapsed)
            row_str += f"{elapsed:<16.6f} | "

        print(row_str)

    return results


def save_benchmarks_to_csv(results: dict, filepath: str):
    """Saves multi-algorithm benchmarking data to CSV file."""
    sizes = results["sizes"]
    algos = [k for k in results if k != "sizes"]

    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Input_Size_n"] + [a.replace(" ", "_") for a in algos])
        for idx, n in enumerate(sizes):
            row = [n] + [results[a][idx] for a in algos]
            writer.writerow(row)
    print(f"\n[+] Benchmark CSV saved to: {filepath}")


def plot_comparison(results: dict, filepath: str):
    """Plots comparative time complexity graph using Matplotlib."""
    sizes = results["sizes"]
    algos = [k for k in results if k != "sizes"]

    colors = {
        "Selection Sort": "#e74c3c",  # Red (O(n^2))
        "Merge Sort": "#2ecc71",      # Green (O(n log n))
        "Insertion Sort": "#f39c12",  # Orange (O(n^2))
        "Radix Sort": "#3498db"       # Blue (O(nk))
    }

    plt.figure(figsize=(11, 7))
    for algo in algos:
        plt.plot(
            sizes, results[algo],
            marker='o',
            color=colors.get(algo, 'black'),
            linewidth=2,
            markersize=5,
            label=algo
        )

    plt.title("Empirical Time Complexity Comparison: Sorting Algorithms", fontsize=14, fontweight='bold')
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()

    plt.savefig(filepath, dpi=300)
    plt.close()
    print(f"[+] Comparison graph saved to: {filepath}")


def main():
    print("=" * 78)
    print(" TASK 5: FOUR SORTING TECHNIQUES - BENCHMARK & COMPARISON ")
    print("=" * 78)

    # Benchmark sizes up to 10,000
    test_sizes = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "sorting_benchmark.csv")
    plot_file = os.path.join(base_dir, "sorting_comparison.png")

    results = run_sorting_benchmarks(test_sizes)
    save_benchmarks_to_csv(results, csv_file)
    plot_comparison(results, plot_file)
    print("=" * 78)


if __name__ == "__main__":
    main()
