class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
                if n == 1:
                    return 1

                if n == 2:
                    return 2

                memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return memo[n]
        return dfs(n)

        
        