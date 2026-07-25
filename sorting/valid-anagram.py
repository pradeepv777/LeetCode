class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        S = {}
        T = {}
        for i in s:
            if i in S:
                S[i]+=1
            else:
                S[i]=1
        for i in t:
            if i in T:
                T[i]+=1
            else:
                T[i]=1
        return S==T
        
    