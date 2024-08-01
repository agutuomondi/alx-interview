#!/usr/bin/env python3
"""
N Queens Solver
"""

import sys

def validate_args():
    """ Validate command line arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    
    return N

def queens(n, row=0, columns=[], diagonals1=[], diagonals2=[]):
    """ Generate all valid positions for N queens """
    if row == n:
        yield columns
    else:
        for col in range(n):
            if col not in columns and (row + col) not in diagonals1 and (row - col) not in diagonals2:
                yield from queens(n, row + 1, columns + [col], diagonals1 + [row + col], diagonals2 + [row - col])

def solve(n):
    """ Solve the N queens problem and print each solution """
    for solution in queens(n):
        print([[i, col] for i, col in enumerate(solution)])

if __name__ == "__main__":
    N = validate_args()
    solve(N)

