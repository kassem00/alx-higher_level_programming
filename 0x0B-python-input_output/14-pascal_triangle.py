#!/usr/bin/python3


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i-1] + prev_row[i])
        row.append(1)
        triangle.append(row)
    return triangle
