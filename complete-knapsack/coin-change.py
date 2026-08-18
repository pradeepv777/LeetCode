class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if sum(coins) == amount:
            return len(coins)
        if not coins:
            return 0

        memo = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")
            if rem in memo:
                return memo[rem]

            min_coins = float("inf")

            for coin in coins:
                result = dfs(rem - coin)
                min_coins = min(min_coins, 1 + result)

            memo[rem] = min_coins
            return memo[rem]
        

        return dfs(amount) if dfs(amount) != float("inf") else -1

        
        