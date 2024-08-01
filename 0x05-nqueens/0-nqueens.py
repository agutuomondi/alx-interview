#!/usr/bin/env python3

"""
Solution to the N-Queens problem.
"""

import sys


def backtrack(row, n, cols, pos_diags, neg_diags, board):
    """
    Backtrack function to solve N-Queens problem.
    
    Args:
        row (int): Current row.
        n (int): Number of queens.
        cols (set): Set of columns occupied by queens.
        pos_diags (set): Set of positive diagonals occupied by queens.
        neg_diags (set): Set of negative diagonals occupied by queens.
        board (list): Chess board.
        
    Returns:
        None
    """
    if row == n:
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    result.append([i, j])
        print(result)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
            continue

        cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diags, neg_diags, board)

        cols.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solve the N-Queens problem.
    
    Args:
        n (int): Number of queens. Must be >= 4.
        
    Returns:
        None
    """
    cols = set()
    pos_diags = set()
    neg_diags = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diags, neg_diags, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

