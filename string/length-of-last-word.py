class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        count = 0
        for i in s:
            count+=1
       
        return len(s[count-1])
        