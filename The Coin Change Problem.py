def getWays(n, c):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in c:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]


n, m = map(int, input().split())
c = list(map(int, input().split()))

print(getWays(n, c))
