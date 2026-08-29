class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while l < r:
            if s[r] in vowels and s[l] in vowels :
                s[r],s[l] = s[l],s[r]
                r -= 1
                l += 1

            elif s[r] not in vowels:
                r -=1

            else:
                l+=1

        return "".join(s)



        