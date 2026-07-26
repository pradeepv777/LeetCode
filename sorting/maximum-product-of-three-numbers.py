class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
            k = 3
            curr = 1
            for i in range(k):
                curr *=nums[i]
            maxi = curr
            for i in range(k,len(nums)):
                curr = (curr // nums[i-k]) * nums[i]
                maxi = max(maxi,curr)
            return maxi
        