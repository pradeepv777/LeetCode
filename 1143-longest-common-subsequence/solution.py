class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i ,j):
            if i == len(text1) or j == len(text2): #Base Cases
                return 0
            if (i, j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]: # 1. Match chars from each text
                   memo[(i, j)] = 1 + dfs(i+1, j+1) # 2. Increment +1 for each matched char
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1)) # if no match, increment seperately, return max vals.

            return memo[(i, j)]

        return dfs(0, 0)

            
            
            


        