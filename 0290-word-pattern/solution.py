class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        pattern_map= {}
        words = {}

        for char, w in zip(pattern, s): #zip - maps words {a:cat, b: dog} etc.
            if char in pattern_map and pattern_map[char] != w:
                return False 
            if w in words and words[w] != char:
                return False

            pattern_map[char] = w
            words[w] = char
            
        return True
        
       


        