class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        seenS = {}
        seenT = {}

        for i in range(len(s)):
            if s[i] in seenS:
                if seenS[s[i]]!= t[i]:
                    return False
            else:
                seenS[s[i]] = t[i]

            if t[i] in seenT:
                if seenT[t[i]]!=  s[i]:
                    return False
            else:
                seenT[t[i]] = s[i]
        return True

        