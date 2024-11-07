#!/usr/bin/python3
"""
N Queens
"""

import sys


def place(board, row, col, size):
    """
    Determines if a queen can be placed on the board at the given row and column.
    """
    for c in range(col):
        if board[c] == row or board[c] - c == row - col or \
                board[c] + c == row + col:
            return False
    return True


def algo(board, col, size):
    """
    Recursively attempts to solve the N-Queens problem by placing queens
    column by column.
    """
    if col == size:
        print([[i, board[i]] for i in range(size)])
        return

    for r in range(size):
        if place(board, r, col, size):
            board[col] = r
            algo(board[:], col + 1, size)


def solutions(size):
    """
    Prints all possible solutions for the N-Queens problem of size N x N.
    """
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * size
    algo(board, 0, size)


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions(board_size)
