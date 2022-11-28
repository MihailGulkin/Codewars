def count_change(money, coins):
    dp = [0 for i in range(money + 1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], money + 1):
            dp[j] += dp[j - coins[i]]
    return dp[money]
