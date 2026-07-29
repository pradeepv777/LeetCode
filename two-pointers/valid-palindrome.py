class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for i in s:
            if i.isalnum():
                pal += i.lower()
        return pal[::-1] == pal
        