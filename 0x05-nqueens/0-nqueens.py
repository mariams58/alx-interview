#!/usr/bin/python3
import sys


def solve_nqueens(n):
    """Solve the N-Queens puzzle given an int N"""
    solutions = []
    board = []


    def safe_pos(row, col):
        """Check if placing a queen at position is safe from other Queens"""
        for r, c in board:
            if c == col or r + c == row + col or r - c == row - col:
                return False
        return True


    def place_queens(row):
        """Places Queens row by row using recursion"""
        if row == n:
            # Add current position to board
            solutions.append(board[:])
            return


        for col in range(n):
            if safe_pos(row, col):
                board.append([row, col])
                place_queens(row + 1)
                # Backtrack by removing queen
                board.pop()
    # places Queens recursively
    place_queens(0)
    return solutions


def main():
    """Main function of the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    # Solving the puzzle problem
    results = solve_nqueens(n)
    # Printing results per line
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
