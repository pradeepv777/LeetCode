class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        l = 0
        r = len(s) - 1
        s = list(s)

        while l < r:
            if s[r] in "aeiouAEIOU" and s[l] in "aeiouAEIOU" :
                s[r],s[l] = s[l],s[r]
                r -= 1
                l += 1
            elif s[r] not in "aeiouAEIOU":
                r -=1
            else:
                l+=1
        return "".join(s)



        