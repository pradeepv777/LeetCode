class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curr =0
        best = float("inf")
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>=target:
                best = min(best,i-left+1)
                curr-=nums[left]
                left+=1

        if best == float('inf'):
                    return 0
        return best
        