def minCoins(V, coins):
    dp = [float('inf')] * (V + 1)
    dp[0] = 0

    for i in range(1, V + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[V] == float('inf'):
        return -1

    return dp[V]


V, N = map(int, input().split())
coins = list(map(int, input().split()))

print(minCoins(V, coins))
