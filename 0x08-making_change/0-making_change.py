#!/usr/bin/python3
"""Interview question"""


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
