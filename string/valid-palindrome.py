class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        palrev = ""
        for i in s:
            if i.isalnum():
                pal += i.lower()
        for i in pal :
            palrev = i+palrev
        return palrev == pal
        