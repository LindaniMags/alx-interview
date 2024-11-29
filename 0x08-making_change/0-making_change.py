#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    remaining = total
    coins_used = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining > 0:
        if coin_index >= num_coins:
            return -1

        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            coins_used += 1
        else:
            coin_index += 1

    return coins_used
