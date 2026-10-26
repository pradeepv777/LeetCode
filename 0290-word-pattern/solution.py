class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        chars= {}
        words = {}

        for c, w in zip(pattern, s):
            if c in chars and chars[c] != w:
                return False
            if w in words and words[w] != c:
                return False
            chars[c] = w
            words[w] = c
        return True
        
       


        