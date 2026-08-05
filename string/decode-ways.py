class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        way = 0
        def dfs(i):
            if i in memo:
                return memo[i]
            if len(s) == i:
                return 1
            if s[i] == "0":
                return 0
            
            way = dfs(i+1)
            if i+1 <len(s) and 10<= int(s[i:i+2])<=26:
                way+= dfs(i+2)
            memo[i] = way
            return memo[i]
        return dfs(0)A
        
        