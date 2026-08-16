class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        final = ""
        for i in t:
            if i in s:
                final+=i
        return final == s
        