#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]

        # Calculate the rest of the elements in the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
