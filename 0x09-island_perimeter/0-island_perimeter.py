#!/usr/bin/python3
"""
Island Perimeter Interview question
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid:
        grid is a list of list of integers:
            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically (not diagonally).
            grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t
    connected to the water surrounding the island).
    """
    row_index = None
    island_index = None
    for i, row in enumerate(grid):
        if 1 in row:
            island_index = row.index(1)
            row_index = i
            break

    if row_index is None or island_index is None:
        return 0

    width = 0
    for row in grid[row_index:]:
        if row[island_index] != 1:
            break
        width += 1

    length = 0
    for i in range(width):
        length = max(length, grid[island_index + i].count(1))

    return (2 * width) + (2 * length)
