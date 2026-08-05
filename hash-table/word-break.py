class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if len(s) == i:
                return True
            for j in range(i+1 , len(s)+1):
                word = s[i:j]
                if word in wordDict and dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)

