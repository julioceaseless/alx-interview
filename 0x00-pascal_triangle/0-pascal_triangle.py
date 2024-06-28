#!/usr/bin/python3
"""A function to generate Pascal triangle"""


def pascal_triangle(n):
    """
    generate pascal triangle
    """
    triangle = []

    # return empty triangle if n <= 0
    if n <= 0:
        return triangle

    # generate triangle
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                # Each element is the sum of the two elements above it
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # end each row with a 1
            row.append(1)
        triangle.append(row)

    return triangle
