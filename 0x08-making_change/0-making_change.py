#!/usr/bin/python3
"""Interview question"""


'''
def makeChange(coins, total):
    """
    determine the fewest number of coins needed to
    meet a given amount total
    """
    if total <= 0:
        return 0

    # Initialize dp array with a large number
    dp = [float('inf')] * (total + 1)
    # 0 coins needed to make total 0
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
    '''


def makeChange(coins, total):
    """
    Greedy approach to making change.

    Args:
        coins: A list of coin denominations.
        total: The target amount.

    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if it's impossible.
    """

    coins.sort(reverse=True)  # Sort coins in descending order
    result = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            result += 1

    return result if total == 0 else -1
