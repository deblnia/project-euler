

def ways_to_make(coins: list[int], target: int)->int: 
    dp = [0] * (target + 1) # will store number of ways to make ith amount 
    dp[0] = 1 # one way to make amount = 1 

    for coin in coins:
        for amount in range(coin, target + 1): 
            dp[amount] += dp[amount - coin]

    return dp[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(ways_to_make(coins, 200))