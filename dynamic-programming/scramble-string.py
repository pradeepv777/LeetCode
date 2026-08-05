class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        memo = {}
        
        def dfs(s, t):
            if (s, t) in memo:
                return memo[(s, t)]
            if s == t:
                return True
            if sorted(s) != sorted(t):
                return False
                
            n = len(s)
            for k in range(1, n):
                if dfs(s[:k], t[:k]) and dfs(s[k:], t[k:]):
                    memo[(s, t)] = True
                    return True
                if dfs(s[:k], t[n-k:]) and dfs(s[k:], t[:n-k]):
                    memo[(s, t)] = True
                    return True
                    
            memo[(s, t)] = False
            return False

        return dfs(s1, s2)
