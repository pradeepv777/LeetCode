class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sets = set()
        maxi = 0


        for right in range(len(s)):
            while s[right] in sets:
                sets.remove(s[left])
                left+=1
            sets.add(s[right])
            maxi = max(maxi,right - left +1)
        return maxi
