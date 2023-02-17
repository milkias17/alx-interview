#!/usr/bin/python3

"""
Rotate an nxn 2 dimensional matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
    """
    reversed_matrix = list(reversed([row[:] for row in matrix]))
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = reversed_matrix[column][row]
