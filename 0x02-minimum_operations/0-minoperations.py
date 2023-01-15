#!/usr/bin/python3

""" Min operations """


def minOperations(n):
    num_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            num_operations += min_operations
            n /= min_operations
        min_operations += 1
    return num_operations
