class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4 
        
        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            current_take_sum = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    current_take_sum += stoneValue[i + k - 1]
                    max_diff = max(max_diff, current_take_sum - dp[(i + k) % 4])
            
            dp[i % 4] = max_diff
        alice_relative_score = dp[0]
        if alice_relative_score > 0:
            return "Alice"
        elif alice_relative_score < 0:
            return "Bob"
        else:
            return "Tie"
