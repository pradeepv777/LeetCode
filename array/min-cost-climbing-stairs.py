class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} 
        
        def dfs(n):  
            if n in memo:
                return memo[n] 
            if n < 2: 
                return cost[n] 
            
            memo[n] = cost[n] + min(dfs(n-1), dfs(n-2))
            return memo[n]
		
        length = len(cost) 
        return min(dfs(length-1), dfs(length-2))
