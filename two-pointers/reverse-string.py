class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left,right):
            if left > right:
                return
            s[right],s[left] = s[left],s[right]
            helper(left+1,right-1)

        helper(0,len(s)-1)
        return s
            
        