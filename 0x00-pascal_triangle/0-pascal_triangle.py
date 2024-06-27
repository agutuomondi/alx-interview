#!/usr/bin/env python3

"""
Module to implement Pascal's triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows to generate.

    Returns:
        List[List[int]]: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

