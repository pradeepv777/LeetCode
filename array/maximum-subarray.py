class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current= globale =nums[0]
        for i in nums[1:]:
            current = max(i,current+i)
            if current>globale:
               globale = current
        return globale
        