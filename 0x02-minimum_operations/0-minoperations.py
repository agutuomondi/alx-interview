#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """

    str = 'H'  # Character to be formed
    ops = 0  # Number of operations needed
    factor = 2  # Starting factor

    if n < 0:
        return 0  # Return 0 if n is negative

    while n > 1:
        while n % factor == 0:
            ops += factor  # Increment operations by factor
            n //= factor  # Divide n by factor

        factor += 1  # Increment factor

    return ops
