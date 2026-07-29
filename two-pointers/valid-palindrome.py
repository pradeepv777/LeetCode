class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for i in s:
            if i.isalnum():
                pal += i.lower()
        left = 0
        right = len(pal)-1
        while left<right:
            if pal[left] != pal[right]:
                return False
            else:
                left+=1
                right-=1
        return True
        
