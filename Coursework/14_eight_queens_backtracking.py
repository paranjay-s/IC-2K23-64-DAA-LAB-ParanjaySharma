"""
Design and Analysis of Algorithms - Coursework Task 14
Title: The 8-Queens Problem using Backtracking

Algorithmic Paradigm: Backtracking
Mechanism:
    Places queens row by row. At each row, checks if a column is safe from attack:
    1. No two queens in the same column.
    2. No two queens on the same main diagonal (row - col is constant).
    3. No two queens on the same anti-diagonal (row + col is constant).
    If a configuration violates safety constraints, the algorithm prunes that branch
    of the state-space tree and backtracks to try another position.

Time Complexity: O(N!) in worst-case state space exploration (significantly pruned)
Space Complexity: O(N) auxiliary space for board configuration and diagonal lookup sets
"""

def solve_n_queens(n: int = 8):
    """
    Solves the N-Queens problem using Backtracking.
    
    Returns:
        tuple: (list_of_solutions, states_explored)
    """
    solutions = []
    board = [-1] * n  # board[row] = col where queen is placed
    cols = set()
    diag1 = set()     # row - col
    diag2 = set()     # row + col
    states_explored = 0

    def backtrack(row: int):
        nonlocal states_explored
        states_explored += 1

        # Base case: All N queens successfully placed
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col

            # Check safety constraint
            if col not in cols and d1 not in diag1 and d2 not in diag2:
                # Place Queen
                board[row] = col
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack: Remove Queen and restore state
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)
                board[row] = -1

    backtrack(0)
    return solutions, states_explored


def print_chessboard(board: list, solution_number: int):
    """Prints a visual ASCII representation of an 8x8 chessboard solution."""
    n = len(board)
    print(f"\n--- Solution #{solution_number} (Queen Positions: {board}) ---")
    print("  " + "+---" * n + "+")
    for r in range(n):
        row_str = f"{r} |"
        for c in range(n):
            if board[r] == c:
                row_str += " Q |"
            else:
                row_str += " . |"
        print(row_str)
        print("  " + "+---" * n + "+")
    print("    " + "   ".join(str(c) for c in range(n)))


def main():
    print("=" * 65)
    print(" TASK 14: THE 8-QUEENS PROBLEM (BACKTRACKING) ")
    print("=" * 65)

    n = 8
    print(f"Solving {n}-Queens Problem...")
    solutions, states = solve_n_queens(n)

    print(f"Total Valid Solutions Found: {len(solutions)} (Expected for 8-Queens: 92)")
    print(f"Total Recursive States Explored: {states}")

    # Display first 2 solutions visually as examples
    print("\nVisual Board Representation for Sample Solutions:")
    for i in range(min(2, len(solutions))):
        print_chessboard(solutions[i], i + 1)

    print("\nFirst 5 Solution Vectors (row -> col mapping):")
    for idx in range(min(5, len(solutions))):
        print(f"  Sol #{idx + 1:2d}: {solutions[idx]}")

    print("=" * 65)


if __name__ == "__main__":
    main()
