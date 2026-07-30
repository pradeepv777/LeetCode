class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sets = []
        for i in s:
            if i in sets:
                return i
            sets.append(i)
        