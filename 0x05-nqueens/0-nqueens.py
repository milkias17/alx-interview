#!/usr/bin/python3
"""Code for n-queens problem"""
import sys


def print_board(board, n):
    """Prints the board"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def check_is_safe(board, i, j, r):
    """Checks if position in the board is safe"""
    return board[i] in (j, j - i + r, i - r + j)


def find_save_positions(board, row, n):
    """Finds all safe positions"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if check_is_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                find_save_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for _ in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
find_save_positions(board, row, int(n))
