#!/usr/bin/python3
"""
Make Change interview problem
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    cur_total = 0
    num_coins = 0
    for coin in sorted_coins:
        while (coin + cur_total) <= total:
            cur_total += coin
            num_coins += 1

        if cur_total == total:
            return num_coins

    if cur_total != total:
        return -1
