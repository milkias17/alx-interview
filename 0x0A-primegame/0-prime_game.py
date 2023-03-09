#!/usr/bin/python3
"""
Prime Game Interview question
"""


def get_first_prime(values):
    for i in values:
        if isPrime(i):
            return [v for v in values if v % i != 0]
    return False


def isPrime(x):
    """ check if number is a prime number """
    if x < 2 or x == 4:
        return False
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its multiples
    from the set. The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each
    round. Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    if x != len(nums):
        return None

    maria = {"Turn": True, "Score": 0}
    ben = {"Turn": False, "Score": 0}
    round = 0
    while (x):
        ben["Turn"] = False
        maria["Turn"] = True
        if round >= len(nums):
            round = 0
        current = [i for i in range(1, nums[round] + 1)]
        while (len(current) > 1):
            if get_first_prime(current):
                current = get_first_prime(current)
                if maria["Turn"]:
                    maria["Turn"] = False
                    ben["Turn"] = True
                else:
                    ben["Turn"] = False
                    maria["Turn"] = True
        if maria["Turn"]:
            ben["Score"] += 1
        else:
            maria["Score"] += 1
        round += 1
        x -= 1
    if ben["Score"] < maria["Score"]:
        return 'Maria'
    return 'Ben'
