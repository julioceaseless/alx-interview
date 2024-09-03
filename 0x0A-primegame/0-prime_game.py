def generate_primes(n):
    primes = [True] * (n + 1)

    # 0 and 1 are not primes
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = generate_primes(max_num)

    memo = {}

    # memoize
    def get_winner(n):
        if n in memo:
            return memo[n]

        prime_count = sum(primes[2:n+1])

        # Determine the winner
        if prime_count % 2 == 0:
            winner = "Ben"
        else:
            winner = "Maria"

        memo[n] = winner
        return winner

    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        winner = get_winner(n)
        if winner == "Maria":
            Maria_wins += 1
        else:
            Ben_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
