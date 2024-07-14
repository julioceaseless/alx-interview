#!/usr/bin/python3
"""
Interview question
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    factors = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors += divisor
            n //= divisor
        divisor += 1
    return factors
