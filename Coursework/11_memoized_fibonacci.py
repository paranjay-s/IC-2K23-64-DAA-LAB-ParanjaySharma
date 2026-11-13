"""
Design and Analysis of Algorithms - Coursework Task 11
Title: Memoised Fibonacci Series (Top-Down Dynamic Programming)

Algorithmic Paradigm: Dynamic Programming (Memoization)
Principle:
    Stores the results of expensive recursive function calls in a cache/lookup table.
    When the same inputs occur again, returns the cached result instead of recomputing,
    thereby transforming exponential time O(2^n) into linear time O(n).

Time Complexity:
    - Naive Recursion:    O(2^n)
    - Memoized Recursion: O(n)
Space Complexity: O(n) for recursion stack + memo cache
"""

# Call counters for empirical demonstration
naive_calls = 0
memo_calls = 0


def fibonacci_naive(n: int) -> int:
    """Computes nth Fibonacci number using naive exponential recursion."""
    global naive_calls
    naive_calls += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memo(n: int, memo: dict = None) -> int:
    """Computes nth Fibonacci number using Top-Down Memoization."""
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    # Compute and store in memo dictionary
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def generate_fibonacci_series(terms: int) -> list:
    """Generates the full Fibonacci series for a given number of terms."""
    memo = {}
    series = [fibonacci_memo(i, memo) for i in range(terms)]
    return series


def main():
    global naive_calls, memo_calls
    print("=" * 68)
    print(" TASK 11: MEMOISED FIBONACCI SERIES (DYNAMIC PROGRAMMING) ")
    print("=" * 68)

    # 1. Comparison of Call Counts for moderate n
    print("Comparison of Function Call Overhead (n = 20):")
    n_compare = 20

    naive_calls = 0
    val_naive = fibonacci_naive(n_compare)
    calls_naive = naive_calls

    memo_calls = 0
    val_memo = fibonacci_memo(n_compare, {})
    calls_memo = memo_calls

    print(f"  Result F({n_compare}): {val_memo}")
    print(f"  Naive Recursive Function Calls:    {calls_naive:>8,}")
    print(f"  Memoized Recursive Function Calls: {calls_memo:>8,}")
    print(f"  Efficiency Gain: {calls_naive / calls_memo:.1f}x fewer function calls!\n")

    # 2. Generating sequence of first 15 Fibonacci numbers
    num_terms = 15
    fib_series = generate_fibonacci_series(num_terms)
    print(f"First {num_terms} Terms of Fibonacci Series:")
    print(" ", fib_series, "\n")

    # 3. Demonstration of large n computed instantaneously
    large_n_values = [30, 50, 75, 100]
    print("Computing Large Fibonacci Numbers with Memoization:")
    shared_memo = {0: 0, 1: 1}
    for val in large_n_values:
        ans = fibonacci_memo(val, shared_memo)
        print(f"  F({val:<3}) = {ans}")

    print("=" * 68)


if __name__ == "__main__":
    main()
