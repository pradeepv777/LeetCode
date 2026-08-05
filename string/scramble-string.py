class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        memo = {}
        def dfs(s,t):
            if sorted(s) != sorted(t):
                return False
            if s == t:
                return True

        return dfs(s1,s2)
